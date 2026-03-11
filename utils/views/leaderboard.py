import discord
from utils.db import get_conn
from utils.realms import get_realm_index


MEDALS = ["🥇", "🥈", "🥉"]


def _medal(i: int) -> str:
    return MEDALS[i] if i < 3 else f"`{i+1}.`"


def _build_realm_embed() -> discord.Embed:
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT name, realm, rebirth_count FROM players WHERE is_dead = 0"
        ).fetchall()
    rows = sorted(rows, key=lambda r: get_realm_index(r["realm"]), reverse=True)[:10]
    embed = discord.Embed(title="✦ 境界榜 ✦", color=discord.Color.gold())
    lines = []
    for i, r in enumerate(rows):
        rebirth = f"（轮回 {r['rebirth_count']} 次）" if r["rebirth_count"] > 0 else ""
        lines.append(f"{_medal(i)} **{r['name']}** — {r['realm']}{rebirth}")
    embed.description = "\n".join(lines) or "暂无数据"
    return embed


def _build_power_embed() -> discord.Embed:
    from utils.combat import calc_power
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT * FROM players WHERE is_dead = 0"
        ).fetchall()
    players = [dict(r) for r in rows]
    ranked = sorted(players, key=lambda p: calc_power(p), reverse=True)[:10]
    embed = discord.Embed(title="✦ 战力榜 ✦", color=discord.Color.red())
    lines = []
    for i, p in enumerate(ranked):
        power = calc_power(p)
        lines.append(f"{_medal(i)} **{p['name']}** — {power:.1f}　{p['realm']}")
    embed.description = "\n".join(lines) or "暂无数据"
    return embed


def _build_lifespan_embed() -> discord.Embed:
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT name, lifespan, realm FROM players WHERE is_dead = 0 ORDER BY lifespan DESC LIMIT 10"
        ).fetchall()
    embed = discord.Embed(title="✦ 寿元榜 ✦", color=discord.Color.green())
    lines = []
    for i, r in enumerate(rows):
        lines.append(f"{_medal(i)} **{r['name']}** — {r['lifespan']} 年　{r['realm']}")
    embed.description = "\n".join(lines) or "暂无数据"
    return embed


def _build_reputation_embed() -> discord.Embed:
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT name, reputation, realm FROM players WHERE is_dead = 0 ORDER BY reputation DESC LIMIT 10"
        ).fetchall()
    embed = discord.Embed(title="✦ 声望榜 ✦", color=discord.Color.blue())
    lines = []
    for i, r in enumerate(rows):
        lines.append(f"{_medal(i)} **{r['name']}** — {r['reputation']} 声望　{r['realm']}")
    embed.description = "\n".join(lines) or "暂无数据"
    return embed


def _build_alchemy_embed() -> discord.Embed:
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT name, alchemy_level, alchemy_exp FROM players WHERE is_dead = 0 AND alchemy_level > 0 "
            "ORDER BY alchemy_level DESC, alchemy_exp DESC LIMIT 10"
        ).fetchall()
    embed = discord.Embed(title="✦ 炼丹榜 ✦", color=discord.Color.orange())
    lines = []
    for i, r in enumerate(rows):
        lines.append(f"{_medal(i)} **{r['name']}** — {r['alchemy_level']} 品　经验 {r['alchemy_exp']}")
    embed.description = "\n".join(lines) or "暂无入门炼丹师"
    return embed


def _build_wealth_embed() -> discord.Embed:
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT name, spirit_stones, realm FROM players WHERE is_dead = 0 ORDER BY spirit_stones DESC LIMIT 10"
        ).fetchall()
    embed = discord.Embed(title="✦ 富豪榜 ✦", color=discord.Color.yellow())
    lines = []
    for i, r in enumerate(rows):
        lines.append(f"{_medal(i)} **{r['name']}** — {r['spirit_stones']:,} 灵石　{r['realm']}")
    embed.description = "\n".join(lines) or "暂无数据"
    return embed


_BOARDS = {
    "境界榜": _build_realm_embed,
    "战力榜": _build_power_embed,
    "寿元榜": _build_lifespan_embed,
    "声望榜": _build_reputation_embed,
    "炼丹榜": _build_alchemy_embed,
    "富豪榜": _build_wealth_embed,
}


class LeaderboardView(discord.ui.View):
    def __init__(self, author, cog=None):
        super().__init__(timeout=120)
        self.author = author
        self.cog = cog

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("这不是你的面板。", ephemeral=True)
            return False
        return True

    async def _show(self, interaction: discord.Interaction, key: str):
        embed = _BOARDS[key]()
        embed.set_footer(text="仅显示存活修士 · 前十名")
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="境界榜", style=discord.ButtonStyle.primary, row=0)
    async def realm_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self._show(interaction, "境界榜")

    @discord.ui.button(label="战力榜", style=discord.ButtonStyle.danger, row=0)
    async def power_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self._show(interaction, "战力榜")

    @discord.ui.button(label="寿元榜", style=discord.ButtonStyle.success, row=0)
    async def lifespan_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self._show(interaction, "寿元榜")

    @discord.ui.button(label="声望榜", style=discord.ButtonStyle.secondary, row=1)
    async def reputation_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self._show(interaction, "声望榜")

    @discord.ui.button(label="炼丹榜", style=discord.ButtonStyle.secondary, row=1)
    async def alchemy_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self._show(interaction, "炼丹榜")

    @discord.ui.button(label="富豪榜", style=discord.ButtonStyle.secondary, row=1)
    async def wealth_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self._show(interaction, "富豪榜")

    @discord.ui.button(label="返回世界", style=discord.ButtonStyle.secondary, row=2)
    async def back_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        from utils.views.world import WorldMenuView, _world_overview_embed
        await interaction.response.edit_message(embed=_world_overview_embed(), view=WorldMenuView(interaction.user, self.cog))
