import discord
import json
import time
from utils.db import get_conn
from utils.sects import (
    TECHNIQUES, TECHNIQUE_STAGES, calc_technique_stat_bonus,
    get_technique_cost, next_stage,
)


def _parse_techniques(raw) -> list:
    data = json.loads(raw or "[]")
    result = []
    for item in data:
        if isinstance(item, str):
            result.append({"name": item, "stage": "入门", "equipped": True})
        elif isinstance(item, dict):
            result.append(item)
    return result


def _save_techniques(uid: str, techniques: list):
    with get_conn() as conn:
        conn.execute(
            "UPDATE players SET techniques = ? WHERE discord_id = ?",
            (json.dumps(techniques, ensure_ascii=False), uid),
        )
        conn.commit()


def _get_player(uid: str):
    with get_conn() as conn:
        row = conn.execute("SELECT * FROM players WHERE discord_id = ?", (uid,)).fetchone()
        return dict(row) if row else None


def _build_techniques_embed(player: dict) -> discord.Embed:
    techniques = _parse_techniques(player["techniques"])
    if not techniques:
        embed = discord.Embed(
            title=f"✦ {player['name']} 的功法 ✦",
            description="尚未习得任何功法。",
            color=discord.Color.teal(),
        )
        return embed

    lines = []
    for t in techniques:
        info = TECHNIQUES.get(t["name"], {})
        mark = "✦" if t.get("equipped") else "○"
        grade = t.get("grade") or info.get("grade", "?")
        ttype = info.get("type", "未知")
        stage = t.get("stage", "入门")
        lines.append(f"{mark} **{t['name']}**（{grade} · {ttype}）　阶段：{stage}")

    equipped_count = sum(1 for t in techniques if t.get("equipped"))
    from utils.realms import get_technique_slot_limit
    slot_limit = get_technique_slot_limit(player["realm"])
    embed = discord.Embed(
        title=f"✦ {player['name']} 的功法 ✦",
        description="\n".join(lines),
        color=discord.Color.teal(),
    )
    embed.set_footer(text=f"✦ 已装备　○ 未装备　已装备 {equipped_count}/{slot_limit}")
    if player.get("sect"):
        embed.add_field(name="宗门", value=f"{player['sect']} · {player.get('sect_rank', '外门弟子')}", inline=False)
    return embed


def _format_stat(stat: str, val: float) -> str:
    STAT_LABELS = {
        "comprehension": "悟性", "physique": "体魄", "fortune": "机缘",
        "bone": "根骨", "soul": "神识", "escape_rate": "逃跑成功率",
        "cultivation_speed": "修炼速度", "lifespan_bonus": "寿元加成",
    }
    label = STAT_LABELS.get(stat, stat)
    if stat == "cultivation_speed":
        return f"{label} +{val * 100:.0f}%"
    if stat == "escape_rate":
        return f"{label} +{val:.0f}%"
    return f"{label} +{val:.0f}"


def _calc_single_technique_bonus(t: dict) -> dict:
    from utils.sects import STAGE_STAT_MULTIPLIER, STAGE_PCT_MULTIPLIER, PCT_STATS
    name = t.get("name", "")
    stage = t.get("stage", "入门")
    info = TECHNIQUES.get(name, {})
    base_bonus = info.get("stat_bonus", {})
    result = {}
    for stat, val in base_bonus.items():
        if stat in PCT_STATS:
            mult = STAGE_PCT_MULTIPLIER.get(stage, 1)
        else:
            mult = STAGE_STAT_MULTIPLIER.get(stage, 1)
        result[stat] = val * mult
    return result


def _build_stats_embed(player: dict) -> discord.Embed:
    techniques = _parse_techniques(player["techniques"])
    equipped = [t for t in techniques if t.get("equipped")]

    if not equipped:
        return discord.Embed(
            title="✦ 功法属性加成 ✦",
            description="当前没有装备任何功法。",
            color=discord.Color.teal(),
        )

    embed = discord.Embed(title="✦ 功法属性加成 ✦", color=discord.Color.teal())

    for t in equipped:
        info = TECHNIQUES.get(t["name"], {})
        grade = t.get("grade") or info.get("grade", "?")
        stage = t.get("stage", "入门")
        single_bonus = _calc_single_technique_bonus(t)
        if single_bonus:
            bonus_str = "　".join(_format_stat(s, v) for s, v in single_bonus.items())
        else:
            bonus_str = "无加成"
        embed.add_field(
            name=f"✦ {t['name']}（{grade} · {stage}）",
            value=bonus_str,
            inline=False,
        )

    total = calc_technique_stat_bonus(techniques)
    if total:
        total_str = "　".join(_format_stat(s, v) for s, v in total.items())
    else:
        total_str = "无"
    embed.add_field(name="─── 总加成 ───", value=total_str, inline=False)

    return embed


class TechniquesView(discord.ui.View):
    def __init__(self, author: discord.User, cog):
        super().__init__(timeout=120)
        self.author = author
        self.cog = cog

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("这不是你的面板。", ephemeral=True)
            return False
        return True

    @discord.ui.button(label="装备/卸下", style=discord.ButtonStyle.primary, row=0)
    async def toggle_equip(self, interaction: discord.Interaction, button: discord.ui.Button):
        uid = str(interaction.user.id)
        player = _get_player(uid)
        if not player:
            return await interaction.response.send_message("尚未创建角色。", ephemeral=True)

        techniques = _parse_techniques(player["techniques"])
        if not techniques:
            return await interaction.response.send_message("尚未习得任何功法。", ephemeral=True)

        options = []
        for t in techniques:
            info = TECHNIQUES.get(t["name"], {})
            stage = t.get("stage", "入门")
            mark = "✦ 已装备" if t.get("equipped") else "○ 未装备"
            options.append(discord.SelectOption(
                label=t["name"],
                description=f"{mark} · {info.get('type', '未知')} · {stage}",
                value=t["name"],
            ))

        view = ToggleEquipView(self.author, self.cog)
        view.select.options = options
        await interaction.response.send_message("选择要装备或卸下的功法：", view=view, ephemeral=True)

    @discord.ui.button(label="修炼功法", style=discord.ButtonStyle.success, row=0)
    async def train(self, interaction: discord.Interaction, button: discord.ui.Button):
        uid = str(interaction.user.id)
        player = _get_player(uid)
        if not player:
            return await interaction.response.send_message("尚未创建角色。", ephemeral=True)

        now = time.time()
        if player.get("cultivating_until") and now < player["cultivating_until"]:
            return await interaction.response.send_message("道友正在闭关，无法修炼功法。", ephemeral=True)

        techniques = _parse_techniques(player["techniques"])
        trainable = [t for t in techniques if next_stage(t.get("stage", "入门")) is not None]
        if not trainable:
            return await interaction.response.send_message("所有功法均已达最高阶段。", ephemeral=True)

        options = []
        for t in trainable:
            info = TECHNIQUES.get(t["name"], {})
            stage = t.get("stage", "入门")
            nxt = next_stage(stage)
            stones, years = get_technique_cost(t["name"], stage)
            options.append(discord.SelectOption(
                label=t["name"],
                description=f"{stage} → {nxt}　灵石 {stones}　寿元 {years}年",
                value=t["name"],
            ))

        view = TrainSelectView(self.author, self.cog)
        view.select.options = options
        await interaction.response.send_message("选择要修炼的功法：", view=view, ephemeral=True)

    @discord.ui.button(label="学习功法", style=discord.ButtonStyle.success, row=1)
    async def learn(self, interaction: discord.Interaction, button: discord.ui.Button):
        uid = str(interaction.user.id)
        player = _get_player(uid)
        if not player:
            return await interaction.response.send_message("尚未创建角色。", ephemeral=True)

        with get_conn() as conn:
            rows = conn.execute(
                "SELECT item_id, quantity FROM inventory WHERE discord_id = ?", (uid,)
            ).fetchall()

        books = [(r["item_id"], r["quantity"]) for r in rows if r["item_id"] in TECHNIQUES]
        if not books:
            return await interaction.response.send_message("背包中没有可学习的功法书。", ephemeral=True)

        options = [
            discord.SelectOption(
                label=name,
                description=f"{TECHNIQUES[name].get('grade','?')} · {TECHNIQUES[name].get('type','?')}　×{qty}",
                value=name,
            )
            for name, qty in books
        ]
        view = LearnSelectView(self.author, self.cog)
        view.select.options = options
        await interaction.response.send_message("选择要学习的功法：", view=view, ephemeral=True)

    @discord.ui.button(label="功法属性", style=discord.ButtonStyle.secondary, row=0)
    async def stats(self, interaction: discord.Interaction, button: discord.ui.Button):
        uid = str(interaction.user.id)
        player = _get_player(uid)
        if not player:
            return await interaction.response.send_message("尚未创建角色。", ephemeral=True)
        embed = _build_stats_embed(player)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="返回菜单", style=discord.ButtonStyle.danger, row=0)
    async def back(self, interaction: discord.Interaction, button: discord.ui.Button):
        from utils.views.menu import MainMenuView, _build_menu_embed
        uid = str(interaction.user.id)
        player = _get_player(uid)

        has_player = player is not None and not player.get("is_dead")
        can_bt = has_player and self.cog._can_breakthrough(player) if has_player else False

        has_dual = False
        city_players = []
        if has_player:
            techniques = _parse_techniques(player["techniques"])
            has_dual = any(t.get("name") == "双修功法" for t in techniques)
            with get_conn() as conn:
                rows = conn.execute(
                    "SELECT discord_id, name, realm, cultivation FROM players "
                    "WHERE current_city = ? AND is_dead = 0 AND discord_id != ?",
                    (player["current_city"], uid),
                ).fetchall()
            city_players = [dict(r) for r in rows]

        view = MainMenuView(interaction.user, has_player, can_bt, self.cog, player, city_players)
        await interaction.response.send_message(embed=_build_menu_embed(has_dual), view=view)


class ToggleEquipView(discord.ui.View):
    def __init__(self, author: discord.User, cog):
        super().__init__(timeout=60)
        self.author = author
        self.cog = cog

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("这不是你的面板。", ephemeral=True)
            return False
        return True

    @discord.ui.select(placeholder="选择功法...", min_values=1, max_values=1)
    async def select(self, interaction: discord.Interaction, select: discord.ui.Select):
        uid = str(interaction.user.id)
        name = select.values[0]
        player = _get_player(uid)
        if not player:
            return await interaction.response.send_message("角色不存在。", ephemeral=True)

        techniques = _parse_techniques(player["techniques"])
        target = next((t for t in techniques if t["name"] == name), None)
        if not target:
            return await interaction.response.send_message(f"未习得功法「{name}」。", ephemeral=True)

        if target.get("equipped"):
            tech_info = TECHNIQUES.get(name, {})
            lifespan_bonus = tech_info.get("stat_bonus", {}).get("lifespan_bonus", 0)
            if lifespan_bonus > 0:
                from utils.sects import STAGE_PCT_MULTIPLIER
                stage = target.get("stage", "入门")
                mult = STAGE_PCT_MULTIPLIER.get(stage, 1)
                actual_bonus = int(lifespan_bonus * mult)
                from utils.character import get_effective_lifespan_max
                current_eff_max = get_effective_lifespan_max(player)
                max_after_unequip = current_eff_max - actual_bonus
                if player["lifespan"] > max_after_unequip:
                    return await interaction.response.send_message(
                        f"无法卸下「**{name}**」。\n"
                        f"当前寿元 **{player['lifespan']}年**，卸下后上限降至 **{max_after_unequip}年**。\n"
                        f"寿元需先消耗至 **{max_after_unequip}年** 以下方可卸下。",
                        ephemeral=True
                    )
            target["equipped"] = False
            _save_techniques(uid, techniques)
            msg = f"已卸下功法「**{name}**」。"
        else:
            from utils.realms import get_technique_slot_limit
            equipped_count = sum(1 for t in techniques if t.get("equipped"))
            slot_limit = get_technique_slot_limit(player["realm"])
            if equipped_count >= slot_limit:
                return await interaction.response.send_message(f"当前境界（{player['realm']}）最多装备 {slot_limit} 本功法，请先卸下一本。", ephemeral=True)
            target["equipped"] = True
            _save_techniques(uid, techniques)
            msg = f"已装备功法「**{name}**」。"

        player = _get_player(uid)
        embed = _build_techniques_embed(player)
        try:
            parent_msg = interaction.message.reference and await interaction.channel.fetch_message(interaction.message.reference.message_id)
        except Exception:
            parent_msg = None

        await interaction.response.send_message(msg, ephemeral=True)


class TrainSelectView(discord.ui.View):
    def __init__(self, author: discord.User, cog):
        super().__init__(timeout=60)
        self.author = author
        self.cog = cog

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("这不是你的面板。", ephemeral=True)
            return False
        return True

    @discord.ui.select(placeholder="选择功法...", min_values=1, max_values=1)
    async def select(self, interaction: discord.Interaction, select: discord.ui.Select):
        uid = str(interaction.user.id)
        name = select.values[0]
        player = _get_player(uid)
        if not player:
            return await interaction.response.send_message("角色不存在。", ephemeral=True)
        if player["is_dead"]:
            return await interaction.response.send_message("道友已坐化。", ephemeral=True)

        now = time.time()
        if player.get("cultivating_until") and now < player["cultivating_until"]:
            return await interaction.response.send_message("道友正在闭关，无法修炼功法。", ephemeral=True)

        techniques = _parse_techniques(player["techniques"])
        target = next((t for t in techniques if t["name"] == name), None)
        if not target:
            return await interaction.response.send_message(f"未习得功法「{name}」。", ephemeral=True)

        current_stage = target.get("stage", "入门")
        nxt = next_stage(current_stage)
        if not nxt:
            return await interaction.response.send_message(f"「{name}」已达最高阶段。", ephemeral=True)

        stones_cost, years_cost = get_technique_cost(name, current_stage)

        if player["spirit_stones"] < stones_cost:
            return await interaction.response.send_message(
                f"灵石不足。「{name}」{current_stage} → {nxt} 需要 **{stones_cost} 灵石**，"
                f"当前只有 **{player['spirit_stones']} 灵石**。",
                ephemeral=True,
            )
        if player["lifespan"] < years_cost:
            return await interaction.response.send_message(
                f"寿元不足。修炼「{name}」需消耗 **{years_cost} 年** 寿元。",
                ephemeral=True,
            )

        view = TrainConfirmView(self.author, self.cog, name, current_stage, nxt, stones_cost, years_cost)
        info = TECHNIQUES.get(name, {})
        grade = info.get("grade", "?")
        real_hours = years_cost * 2
        embed = discord.Embed(
            title="✦ 确认修炼功法 ✦",
            description=(
                f"**{name}**（{grade}）\n"
                f"{current_stage} ➜ **{nxt}**\n\n"
                f"消耗灵石：**{stones_cost}**　当前：{player['spirit_stones']}\n"
                f"消耗寿元：**{years_cost} 年**　当前：{player['lifespan']} 年\n"
                f"修炼时间：现实 **{real_hours} 小时**\n\n"
                "确认后将进入闭关状态。"
            ),
            color=discord.Color.teal(),
        )
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


class TrainConfirmView(discord.ui.View):
    def __init__(self, author, cog, tech_name, current_stage, next_stage, stones_cost, years_cost):
        super().__init__(timeout=60)
        self.author = author
        self.cog = cog
        self.tech_name = tech_name
        self.current_stage = current_stage
        self.next_stage_name = next_stage
        self.stones_cost = stones_cost
        self.years_cost = years_cost

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("这不是你的面板。", ephemeral=True)
            return False
        return True

    @discord.ui.button(label="确认修炼", style=discord.ButtonStyle.success)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        uid = str(interaction.user.id)
        player = _get_player(uid)
        if not player:
            return await interaction.response.send_message("角色不存在。", ephemeral=True)

        now = time.time()
        if player.get("cultivating_until") and now < player["cultivating_until"]:
            return await interaction.response.send_message("道友正在闭关。", ephemeral=True)

        if player["spirit_stones"] < self.stones_cost:
            return await interaction.response.send_message("灵石不足。", ephemeral=True)
        if player["lifespan"] < self.years_cost:
            return await interaction.response.send_message("寿元不足。", ephemeral=True)

        techniques = _parse_techniques(player["techniques"])
        target = next((t for t in techniques if t["name"] == self.tech_name), None)
        if not target:
            return await interaction.response.send_message("功法不存在。", ephemeral=True)

        if target.get("stage", "入门") != self.current_stage:
            return await interaction.response.send_message("功法阶段已变化，请重新操作。", ephemeral=True)

        target["stage"] = self.next_stage_name
        cultivating_until = now + self.years_cost * 7200
        new_stones = player["spirit_stones"] - self.stones_cost
        new_lifespan = player["lifespan"] - self.years_cost

        with get_conn() as conn:
            conn.execute(
                "UPDATE players SET techniques = ?, spirit_stones = ?, lifespan = ?, "
                "cultivating_until = ?, cultivating_years = ?, last_active = ? WHERE discord_id = ?",
                (json.dumps(techniques, ensure_ascii=False), new_stones, new_lifespan,
                 cultivating_until, self.years_cost, now, uid),
            )
            conn.commit()

        info = TECHNIQUES.get(self.tech_name, {})
        grade = info.get("grade", "?")
        real_hours = self.years_cost * 2
        embed = discord.Embed(
            title="✦ 功法修炼中 ✦",
            description=(
                f"**{self.tech_name}**（{grade}）\n"
                f"{self.current_stage} ➜ **{self.next_stage_name}**\n\n"
                f"消耗灵石：**{self.stones_cost}**　剩余：{new_stones}\n"
                f"消耗寿元：**{self.years_cost} 年**　剩余：{new_lifespan} 年\n"
                f"修炼时间：现实 **{real_hours} 小时**\n\n"
                "闭关结束后将收到通知。"
            ),
            color=discord.Color.green(),
        )
        await interaction.response.edit_message(embed=embed, view=None)

    @discord.ui.button(label="取消", style=discord.ButtonStyle.secondary)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="已取消修炼。", embed=None, view=None)


class LearnSelectView(discord.ui.View):
    def __init__(self, author: discord.User, cog):
        super().__init__(timeout=60)
        self.author = author
        self.cog = cog

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("这不是你的面板。", ephemeral=True)
            return False
        return True

    @discord.ui.select(placeholder="选择功法书...", min_values=1, max_values=1)
    async def select(self, interaction: discord.Interaction, select: discord.ui.Select):
        uid = str(interaction.user.id)
        name = select.values[0]
        player = _get_player(uid)
        if not player:
            return await interaction.response.send_message("角色不存在。", ephemeral=True)

        with get_conn() as conn:
            row = conn.execute(
                "SELECT quantity FROM inventory WHERE discord_id = ? AND item_id = ?",
                (uid, name)
            ).fetchone()
        if not row or row["quantity"] < 1:
            return await interaction.response.send_message("背包中已没有这本功法书。", ephemeral=True)

        techniques = _parse_techniques(player["techniques"])
        info = TECHNIQUES.get(name, {})

        if any(t.get("name") == name for t in techniques):
            await interaction.response.send_message(
                f"已习得「**{name}**」，背包中的书可留作交易用途。",
                ephemeral=True
            )
            return

        equipped_count = sum(1 for t in techniques if t.get("equipped"))
        techniques.append({
            "name": name,
            "grade": info.get("grade", "黄级下品"),
            "stage": "入门",
            "equipped": equipped_count < 5,
        })

        with get_conn() as conn:
            conn.execute(
                "UPDATE players SET techniques = ? WHERE discord_id = ?",
                (json.dumps(techniques, ensure_ascii=False), uid)
            )
            conn.execute(
                "UPDATE inventory SET quantity = quantity - 1 WHERE discord_id = ? AND item_id = ?",
                (uid, name)
            )
            conn.execute(
                "DELETE FROM inventory WHERE discord_id = ? AND item_id = ? AND quantity <= 0",
                (uid, name)
            )
            conn.commit()

        grade = info.get("grade", "?")
        ttype = info.get("type", "?")
        equipped_str = "已自动装备" if equipped_count < 5 else "未装备（已满5本）"
        await interaction.response.edit_message(
            content=f"成功学习「**{name}**」（{grade} · {ttype}）！{equipped_str}。",
            view=None
        )
