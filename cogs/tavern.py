import json
import time
import random

import discord
from discord.ext import commands

from utils.db import get_conn
from utils.quests import get_tavern_quests, get_quest
from utils.combat import roll_combat, calc_power
from utils.realms import get_realm_index
from utils.sects import TECHNIQUES


def _get_player(discord_id: str):
    with get_conn() as conn:
        row = conn.execute("SELECT * FROM players WHERE discord_id = ?", (discord_id,)).fetchone()
        return dict(row) if row else None


def _reward_lines(rewards: dict) -> list[str]:
    lines = []
    stat_names = {"comprehension": "悟性", "physique": "体魄", "fortune": "机缘",
                  "bone": "根骨", "soul": "神识", "lifespan": "寿元"}
    if rewards.get("spirit_stones"):
        lines.append(f"灵石 +{rewards['spirit_stones']}")
    if rewards.get("reputation"):
        lines.append(f"声望 +{rewards['reputation']}")
    if rewards.get("cultivation"):
        lines.append(f"修为 +{rewards['cultivation']}")
    if rewards.get("lifespan"):
        lines.append(f"寿元 +{rewards['lifespan']} 年")
    if rewards.get("technique"):
        t = rewards["technique"]
        grade = TECHNIQUES.get(t, {}).get("grade", "?")
        lines.append(f"功法：**{t}**（{grade}）")
    if rewards.get("stat_bonus"):
        for stat, val in rewards["stat_bonus"].items():
            lines.append(f"{stat_names.get(stat, stat)} 永久 +{val}")
    return lines


def _apply_quest_rewards(uid: str, rewards: dict):
    fields = []
    values = []
    for key in ["spirit_stones", "reputation", "cultivation", "lifespan"]:
        if rewards.get(key):
            fields.append(f"{key} = {key} + ?")
            values.append(rewards[key])
    if rewards.get("stat_bonus"):
        for stat, val in rewards["stat_bonus"].items():
            fields.append(f"{stat} = {stat} + ?")
            values.append(val)
    if fields:
        values.append(uid)
        with get_conn() as conn:
            conn.execute(f"UPDATE players SET {', '.join(fields)} WHERE discord_id = ?", values)
            conn.commit()
    if rewards.get("technique"):
        t_name = rewards["technique"]
        with get_conn() as conn:
            row = conn.execute("SELECT techniques FROM players WHERE discord_id = ?", (uid,)).fetchone()
            techs = json.loads(row["techniques"] or "[]")
            existing = {(t if isinstance(t, str) else t.get("name", "")) for t in techs}
            if t_name not in existing:
                equipped_count = sum(1 for t in techs if isinstance(t, dict) and t.get("equipped"))
                techs.append({
                    "name": t_name,
                    "grade": TECHNIQUES.get(t_name, {}).get("grade", "黄级上品"),
                    "stage": "入门",
                    "equipped": equipped_count < 5,
                })
                conn.execute("UPDATE players SET techniques = ? WHERE discord_id = ?",
                             (json.dumps(techs, ensure_ascii=False), uid))
                conn.commit()


TIER_COLOR = {
    "普通": discord.Color.teal(),
    "精英": discord.Color.gold(),
    "传说": discord.Color.dark_purple(),
}

TIER_EMOJI = {"普通": "📋", "精英": "⚔️", "传说": "🌟"}


class TavernCog(commands.Cog, name="Tavern"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="茶馆")
    async def tavern(self, ctx):
        uid = str(ctx.author.id)
        player = _get_player(uid)
        if not player or player["is_dead"]:
            return await ctx.send(f"{ctx.author.mention} 尚未踏入修仙之路或已坐化。")

        quests = get_tavern_quests(player)
        if not quests:
            return await ctx.send(f"{ctx.author.mention} 当前没有适合你境界的任务。")

        embed = discord.Embed(
            title=f"✦ {player['current_city']} · 茶馆任务栏 ✦",
            description="掌柜将任务榜递来，上面贴满了各色悬赏……",
            color=discord.Color.teal(),
        )
        for tier, quest_list in quests.items():
            lines = []
            for q in quest_list:
                reward_preview = "、".join(_reward_lines(q["rewards"])[:2])
                lines.append(f"{TIER_EMOJI[tier]} **{q['title']}**\n　{q['desc'][:30]}…\n　奖励：{reward_preview}")
            embed.add_field(name=f"── {tier}任务 ──", value="\n\n".join(lines), inline=False)

        embed.set_footer(text="点击下方按钮接取任务")
        await ctx.send(embed=embed, view=TavernView(ctx.author, quests, self))


class TavernView(discord.ui.View):
    def __init__(self, author, quests: dict, cog):
        super().__init__(timeout=120)
        self.author = author
        self.cog = cog
        for tier, quest_list in quests.items():
            for q in quest_list:
                self.add_item(QuestButton(q, tier))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("这不是你的任务栏。", ephemeral=True)
            return False
        return True


class QuestButton(discord.ui.Button):
    def __init__(self, quest: dict, tier: str):
        colors = {"普通": discord.ButtonStyle.secondary,
                  "精英": discord.ButtonStyle.primary,
                  "传说": discord.ButtonStyle.danger}
        super().__init__(
            label=f"{TIER_EMOJI[tier]} {quest['title']}",
            style=colors.get(tier, discord.ButtonStyle.secondary),
        )
        self.quest = quest
        self.tier = tier

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        uid = str(interaction.user.id)
        player = _get_player(uid)
        if not player or player["is_dead"]:
            return await interaction.followup.send("角色状态异常。", ephemeral=True)

        q = self.quest
        reward_lines = _reward_lines(q["rewards"])

        embed = discord.Embed(
            title=f"{TIER_EMOJI[self.tier]} {q['title']}",
            description=q["desc"],
            color=TIER_COLOR.get(self.tier, discord.Color.teal()),
        )
        if q["type"] == "combat":
            embed.add_field(name="目标", value=f"击败 **{q['enemy']['name']}**（战力约 {q['enemy']['power']}）", inline=False)
        else:
            embed.add_field(name="目标", value=f"前往 **{q['location']}** 完成采集", inline=False)
        embed.add_field(name="奖励", value="\n".join(reward_lines), inline=False)

        await interaction.followup.send(
            embed=embed,
            view=QuestConfirmView(interaction.user, q, self.tier, self.view.cog),
        )


class QuestConfirmView(discord.ui.View):
    def __init__(self, author, quest: dict, tier: str, cog):
        super().__init__(timeout=60)
        self.author = author
        self.quest = quest
        self.tier = tier
        self.cog = cog

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("这不是你的任务。", ephemeral=True)
            return False
        return True

    @discord.ui.button(label="接取任务", style=discord.ButtonStyle.success)
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        uid = str(interaction.user.id)
        player = _get_player(uid)
        q = self.quest
        self.stop()

        if q["type"] == "combat":
            enemy = q["enemy"]
            from utils.combat import calc_power
            player_power = calc_power(player) * random.uniform(0.85, 1.15)
            enemy_power = enemy["power"] * random.uniform(0.85, 1.15)
            won = player_power > enemy_power

            result_embed = discord.Embed(
                title=f"⚔️ {q['title']} · 战斗结算",
                description=(
                    f"**{player['name']}** 战力：{player_power:.1f}\n"
                    f"**{enemy['name']}** 战力：{enemy_power:.1f}\n\n"
                ),
                color=discord.Color.green() if won else discord.Color.red(),
            )
            if won:
                _apply_quest_rewards(uid, q["rewards"])
                reward_lines = _reward_lines(q["rewards"])
                result_embed.description += "**胜利！任务完成。**"
                result_embed.add_field(name="获得奖励", value="\n".join(reward_lines), inline=False)
            else:
                result_embed.description += "**败北，任务失败。**\n下次再来吧。"
            await interaction.followup.send(embed=result_embed)

        else:
            location = q["location"]
            if player["current_city"] != location:
                await interaction.followup.send(
                    f"需要前往 **{location}** 才能完成此任务。\n"
                    f"当前位置：**{player['current_city']}**"
                )
                return
            _apply_quest_rewards(uid, q["rewards"])
            reward_lines = _reward_lines(q["rewards"])
            result_embed = discord.Embed(
                title=f"✅ {q['title']} · 任务完成",
                description=f"你在 **{location}** 完成了采集任务。",
                color=discord.Color.green(),
            )
            result_embed.add_field(name="获得奖励", value="\n".join(reward_lines), inline=False)
            await interaction.followup.send(embed=result_embed)

    @discord.ui.button(label="放弃", style=discord.ButtonStyle.secondary)
    async def decline(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("已放弃任务。", ephemeral=True)
        self.stop()


async def setup(bot):
    await bot.add_cog(TavernCog(bot))
