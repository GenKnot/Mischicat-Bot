import discord
from utils.world import CITIES, SPECIAL_REGIONS, cities_by_region
from utils.sects import SECTS, check_requirements


def _get_joinable_sects(player: dict) -> list[str]:
    if not player or player.get("sect"):
        return []
    city = player.get("current_city", "")
    result = []
    for name, data in SECTS.items():
        if data["alignment"] == "隐世":
            continue
        if data["location"] != city:
            continue
        ok, _ = check_requirements(dict(player), name)
        if ok:
            result.append(name)
    return result


class MainMenuView(discord.ui.View):
    def __init__(self, author, has_player: bool, can_breakthrough: bool, cog, player=None, city_players=None):
        super().__init__(timeout=120)
        self.author = author
        self.cog = cog

        if not has_player:
            self.add_item(MenuButton("创建角色", discord.ButtonStyle.success, "create"))
        self.add_item(MenuButton("我的角色", discord.ButtonStyle.primary, "profile"))
        self.add_item(MenuButton("修炼", discord.ButtonStyle.success, "cultivate"))
        self.add_item(MenuButton("世界", discord.ButtonStyle.secondary, "world"))
        self.add_item(MenuButton("移动", discord.ButtonStyle.secondary, "travel"))
        if can_breakthrough:
            self.add_item(MenuButton("突破", discord.ButtonStyle.danger, "breakthrough"))
        self.add_item(MenuButton("探险", discord.ButtonStyle.secondary, "explore"))
        if city_players:
            self.add_item(MenuButton("玩家", discord.ButtonStyle.secondary, "city_players"))
        if player:
            for sect_name in _get_joinable_sects(player):
                self.add_item(MenuButton(f"加入{sect_name}", discord.ButtonStyle.success, f"join_sect:{sect_name}"))
        self._city_players = city_players or []
        self._player = player


class MenuButton(discord.ui.Button):
    def __init__(self, label: str, style: discord.ButtonStyle, action: str, disabled: bool = False):
        super().__init__(label=label, style=style, disabled=disabled)
        self.action = action

    async def callback(self, interaction: discord.Interaction):
        cog = self.view.cog

        if self.action == "world":
            await interaction.response.send_message(
                embed=_world_overview_embed(),
                view=WorldMenuView(interaction.user),
            )
            return

        if self.action == "travel":
            await interaction.response.send_message(
                embed=discord.Embed(
                    title="✦ 移动 · 选择地区 ✦",
                    description="请选择目标地区：",
                    color=discord.Color.teal(),
                ),
                view=TravelRegionView(interaction.user, self.view.cog),
            )
            return

        if self.action == "city_players":
            city_players = getattr(self.view, "_city_players", [])
            player = getattr(self.view, "_player", None)
            await interaction.response.send_message(
                embed=_city_players_embed(city_players, player),
                ephemeral=True,
            )
            return

        await interaction.response.defer()

        try:
            if self.action == "create":
                ctx = await cog.bot.get_context(interaction.message)
                ctx.author = interaction.user
                await cog.create_character(ctx)
            elif self.action == "profile":
                await cog.send_profile(interaction)
            elif self.action == "cultivate":
                await cog.send_cultivate(interaction)
            elif self.action == "breakthrough":
                await cog.send_breakthrough(interaction)
            elif self.action == "stop":
                await cog.send_stop(interaction)
            elif self.action == "explore":
                explore_cog = cog.bot.cogs.get("Explore")
                if explore_cog:
                    ctx = await cog.bot.get_context(interaction.message)
                    ctx.author = interaction.user
                    await explore_cog.explore(ctx)
                else:
                    await interaction.followup.send("探险系统暂时不可用。", ephemeral=True)
            elif self.action.startswith("join_sect:"):
                sect_name = self.action[len("join_sect:"):]
                sect_cog = cog.bot.cogs.get("Sect")
                if sect_cog:
                    ctx = await cog.bot.get_context(interaction.message)
                    ctx.author = interaction.user
                    ctx.kwargs = {"name": sect_name}
                    await sect_cog.join_sect(ctx, name=sect_name)
                else:
                    await interaction.followup.send("宗门系统暂时不可用。", ephemeral=True)
        except Exception as e:
            await interaction.followup.send(f"出错了：{e}", ephemeral=True)


class ProfileView(discord.ui.View):
    def __init__(self, author, can_breakthrough: bool, is_cultivating: bool, cog):
        super().__init__(timeout=120)
        self.author = author
        self.cog = cog

        self.add_item(MenuButton("修炼", discord.ButtonStyle.success, "cultivate"))
        if is_cultivating:
            self.add_item(MenuButton("停止闭关", discord.ButtonStyle.danger, "stop"))
        if can_breakthrough:
            self.add_item(MenuButton("突破", discord.ButtonStyle.danger, "breakthrough"))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("这不是你的面板。", ephemeral=True)
            return False
        return True


def _world_overview_embed() -> discord.Embed:
    return discord.Embed(
        title="✦ 天下舆图 ✦",
        description=(
            "此方天地幅员辽阔，分东域、南域、西域、北域、中州五大区域，"
            "共三十座城市，另有十处特殊秘地散布其间。\n\n"
            "天下宗门林立，正邪各据一方。除世人皆知的十大宗门外，"
            "据传尚有数个隐世宗门隐匿于天地之间——"
            "有的需极高机缘方可得见，有的需历经奇遇方能叩响山门，"
            "更有传言某些宗门只对特定之人开放，凡人难以企及。\n\n"
            "请选择你想了解的内容："
        ),
        color=discord.Color.teal(),
    )


class WorldMenuView(discord.ui.View):
    def __init__(self, author):
        super().__init__(timeout=120)
        self.author = author

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("这不是你的面板。", ephemeral=True)
            return False
        return True

    @discord.ui.button(label="城市", style=discord.ButtonStyle.primary)
    async def cities_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            embed=_cities_embed(),
            view=CityRegionView(interaction.user),
        )

    @discord.ui.button(label="秘地", style=discord.ButtonStyle.secondary)
    async def regions_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(embed=_special_regions_embed())

    @discord.ui.button(label="宗门", style=discord.ButtonStyle.secondary)
    async def sects_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            embed=_sects_overview_embed(),
            view=SectAlignmentView(interaction.user),
        )


def _cities_embed() -> discord.Embed:
    return discord.Embed(
        title="✦ 天下城市 ✦",
        description="共三十座城市，分布于五大区域，请选择区域查看详情：",
        color=discord.Color.blue(),
    )


class CityRegionView(discord.ui.View):
    def __init__(self, author):
        super().__init__(timeout=120)
        self.author = author
        for region in ["东域", "南域", "西域", "北域", "中州"]:
            self.add_item(CityRegionButton(region))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("这不是你的面板。", ephemeral=True)
            return False
        return True


class CityRegionButton(discord.ui.Button):
    def __init__(self, region: str):
        super().__init__(label=region, style=discord.ButtonStyle.secondary)
        self.region = region

    async def callback(self, interaction: discord.Interaction):
        cities = cities_by_region(self.region)
        embed = discord.Embed(title=f"✦ {self.region} ✦", color=discord.Color.blue())
        for c in cities:
            embed.add_field(name=c["name"], value=c["desc"], inline=False)
        await interaction.response.send_message(embed=embed)


class TravelRegionView(discord.ui.View):
    def __init__(self, author, cog):
        super().__init__(timeout=120)
        self.author = author
        self.cog = cog
        for region in ["东域", "南域", "西域", "北域", "中州"]:
            self.add_item(TravelRegionButton(region))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("这不是你的面板。", ephemeral=True)
            return False
        return True


class TravelRegionButton(discord.ui.Button):
    def __init__(self, region: str):
        super().__init__(label=region, style=discord.ButtonStyle.secondary)
        self.region = region

    async def callback(self, interaction: discord.Interaction):
        cities = cities_by_region(self.region)
        embed = discord.Embed(
            title=f"✦ {self.region} · 选择目的地 ✦",
            color=discord.Color.teal(),
        )
        for c in cities:
            embed.add_field(name=c["name"], value=c["desc"], inline=False)
        await interaction.response.send_message(
            embed=embed,
            view=TravelCityView(self.view.author, self.view.cog, cities),
        )


class TravelCityView(discord.ui.View):
    def __init__(self, author, cog, cities: list):
        super().__init__(timeout=120)
        self.author = author
        self.cog = cog
        for c in cities:
            self.add_item(TravelCityButton(c["name"]))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("这不是你的面板。", ephemeral=True)
            return False
        return True


class TravelCityButton(discord.ui.Button):
    def __init__(self, city_name: str):
        super().__init__(label=city_name, style=discord.ButtonStyle.primary)
        self.city_name = city_name

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        ctx = await self.view.cog.bot.get_context(interaction.message)
        ctx.author = interaction.user
        await self.view.cog.travel(ctx, city_name=self.city_name)


def _special_regions_embed() -> discord.Embed:
    embed = discord.Embed(
        title="✦ 特殊秘地 ✦",
        description="天地间散布着十处特殊秘地，各有奇险：",
        color=discord.Color.gold(),
    )
    for r in SPECIAL_REGIONS:
        req = f"（需 {r['min_realm']} 以上）" if r["min_realm"] != "炼气期1层" else ""
        embed.add_field(
            name=f"{r['name']}  [{r['type']}]{req}",
            value=r["desc"],
            inline=False,
        )
    return embed


def _sects_overview_embed() -> discord.Embed:
    return discord.Embed(
        title="✦ 天下宗门 ✦",
        description=(
            "天下宗门分正道与邪道两派，各有传承。\n"
            "另有隐世宗门数个，行踪不定，有缘自会相遇。\n\n"
            "请选择阵营查看详情："
        ),
        color=discord.Color.teal(),
    )


class SectAlignmentView(discord.ui.View):
    def __init__(self, author):
        super().__init__(timeout=120)
        self.author = author

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("这不是你的面板。", ephemeral=True)
            return False
        return True

    @discord.ui.button(label="正道宗门", style=discord.ButtonStyle.primary)
    async def righteous(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(embed=_sects_embed("正道"))

    @discord.ui.button(label="邪道宗门", style=discord.ButtonStyle.danger)
    async def evil(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(embed=_sects_embed("邪道"))

    @discord.ui.button(label="隐世宗门", style=discord.ButtonStyle.secondary)
    async def hidden(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="✦ 隐世宗门 ✦",
            description=(
                "隐世宗门行踪隐秘，不为世人所知。\n\n"
                "据传共有五个隐世宗门散布于天地之间，"
                "有的深藏于秘境之中，有的隐于闹市却无人察觉。\n\n"
                "想要找到他们，或需极高的机缘，或需历经特殊奇遇，"
                "或需满足某些常人难以企及的条件。\n\n"
                "一切，皆看天意。"
            ),
            color=discord.Color.dark_purple(),
        )
        await interaction.response.send_message(embed=embed)


class CultivateView(discord.ui.View):
    """Panel shown when user clicks 修炼 — lets them pick cultivation duration."""

    YEAR_OPTIONS = [
        (1,  "1年",  "现实 2 小时"),
        (2,  "2年",  "现实 4 小时"),
        (4,  "4年",  "现实 8 小时"),
        (8,  "8年",  "现实 16 小时"),
    ]

    def __init__(self, author, cog, player: dict):
        super().__init__(timeout=60)
        self.author = author
        self.cog = cog
        self.player = player
        for years, label, hint in self.YEAR_OPTIONS:
            disabled = player["lifespan"] < years
            self.add_item(CultivateButton(years, label, hint, disabled))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("这不是你的面板。", ephemeral=True)
            return False
        return True


class CultivateButton(discord.ui.Button):
    def __init__(self, years: int, label: str, hint: str, disabled: bool):
        super().__init__(
            label=f"{label}（{hint}）",
            style=discord.ButtonStyle.primary,
            disabled=disabled,
        )
        self.years = years

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        await self.view.cog.start_cultivate(interaction, self.years)
        self.view.stop()


class ClaimCultivationView(discord.ui.View):
    """Shown in DM notification when cultivation finishes — lets player claim rewards."""

    def __init__(self, cog, uid: str):
        super().__init__(timeout=300)
        self.cog = cog
        self.uid = uid

    @discord.ui.button(label="领取修炼成果", style=discord.ButtonStyle.success)
    async def claim(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await self.cog.claim_cultivation(interaction, self.uid)
        self.stop()


class YinYangView(discord.ui.View):
    def __init__(self, author, event: dict, finale_event: dict, player, cog, uid: str):
        super().__init__(timeout=300)
        self.author = author
        self.event = event
        self.finale_event = finale_event
        self.player = player
        self.cog = cog
        self.uid = uid
        seen = set()
        for i, choice in enumerate(event["choices"]):
            if choice["label"] in seen:
                continue
            seen.add(choice["label"])
            self.add_item(YinYangButton(choice["label"], i))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("这不是你的奇遇。", ephemeral=True)
            return False
        return True


class YinYangButton(discord.ui.Button):
    def __init__(self, label: str, index: int):
        super().__init__(label=label, style=discord.ButtonStyle.primary)
        self.index = index

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        for item in self.view.children:
            item.disabled = True
        self.view.stop()
        choice = self.view.event["choices"][self.index]
        if choice.get("next"):
            embed = discord.Embed(
                title=f"✦ {self.view.event['title']} ✦",
                description=choice["next"]["desc"],
                color=discord.Color.dark_purple(),
            )
            await interaction.followup.send(
                embed=embed,
                view=YinYangNextView(self.view.author, self.view.event, choice["next"],
                                     self.view.finale_event, self.view.player, self.view.cog, self.view.uid)
            )
        else:
            from cogs.explore import _apply_rewards, _pick_choice_result
            same = [c for c in self.view.event["choices"] if c["label"] == choice["label"]]
            result = _pick_choice_result(same, dict(self.view.player))
            _apply_rewards(self.view.uid, result.get("rewards", {}))
            await _send_yinyang_finale(interaction, self.view.finale_event, self.view.player, self.view.cog, self.view.uid, result.get("flavor", ""))


class YinYangNextView(discord.ui.View):
    def __init__(self, author, original_event, next_event, finale_event, player, cog, uid):
        super().__init__(timeout=300)
        self.author = author
        self.original_event = original_event
        self.next_event = next_event
        self.finale_event = finale_event
        self.player = player
        self.cog = cog
        self.uid = uid
        seen = set()
        for i, choice in enumerate(next_event["choices"]):
            if choice["label"] in seen:
                continue
            seen.add(choice["label"])
            self.add_item(YinYangNextButton(choice["label"], i))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("这不是你的奇遇。", ephemeral=True)
            return False
        return True


class YinYangNextButton(discord.ui.Button):
    def __init__(self, label: str, index: int):
        super().__init__(label=label, style=discord.ButtonStyle.secondary)
        self.index = index

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        for item in self.view.children:
            item.disabled = True
        self.view.stop()
        from cogs.explore import _apply_rewards, _pick_choice_result
        choices = self.view.next_event["choices"]
        choice = choices[self.index]

        if choice.get("next"):
            embed = discord.Embed(
                title=f"✦ {self.view.original_event['title']} ✦",
                description=choice["next"]["desc"],
                color=discord.Color.dark_purple(),
            )
            await interaction.followup.send(
                embed=embed,
                view=YinYangNextView(self.view.author, self.view.original_event, choice["next"],
                                     self.view.finale_event, self.view.player, self.view.cog, self.view.uid)
            )
            return

        same = [c for c in choices if c["label"] == choice["label"]]
        result = _pick_choice_result(same, dict(self.view.player))
        _apply_rewards(self.view.uid, result.get("rewards", {}))
        await _send_yinyang_finale(interaction, self.view.finale_event, self.view.player, self.view.cog, self.view.uid, result.get("flavor", ""))


async def _send_yinyang_finale(interaction, finale_event, player, cog, uid, prev_flavor):
    embed = discord.Embed(
        title=f"✦ {finale_event['title']} ✦",
        description=(f"*{prev_flavor}*\n\n" if prev_flavor else "") + finale_event["desc"],
        color=discord.Color.dark_purple(),
    )
    await interaction.followup.send(
        embed=embed,
        view=YinYangFinaleView(interaction.user, finale_event, player, cog, uid)
    )


class YinYangFinaleView(discord.ui.View):
    def __init__(self, author, event, player, cog, uid):
        super().__init__(timeout=300)
        self.author = author
        self.event = event
        self.player = player
        self.cog = cog
        self.uid = uid
        seen = set()
        for i, choice in enumerate(event["choices"]):
            if choice["label"] in seen:
                continue
            seen.add(choice["label"])
            self.add_item(YinYangFinaleButton(choice["label"], i))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("这不是你的奇遇。", ephemeral=True)
            return False
        return True


class YinYangFinaleButton(discord.ui.Button):
    def __init__(self, label: str, index: int):
        super().__init__(label=label, style=discord.ButtonStyle.primary)
        self.index = index

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        for item in self.view.children:
            item.disabled = True
        self.view.stop()
        from cogs.explore import _apply_rewards, _pick_choice_result
        choices = self.view.event["choices"]
        choice = choices[self.index]

        if choice.get("next"):
            embed = discord.Embed(
                title=f"✦ {self.view.event['title']} ✦",
                description=choice["next"]["desc"],
                color=discord.Color.dark_purple(),
            )
            await interaction.followup.send(
                embed=embed,
                view=YinYangFinaleSubView(self.view.author, self.view.event, choice["next"],
                                          self.view.player, self.view.cog, self.view.uid)
            )
            return

        same = [c for c in choices if c["label"] == choice["label"]]
        result = _pick_choice_result(same, dict(self.view.player))
        _apply_rewards(self.view.uid, result.get("rewards", {}))
        await _do_yinyang_rebirth(interaction, self.view.player, self.view.cog, self.view.uid, result.get("flavor", ""))


class YinYangFinaleSubView(discord.ui.View):
    def __init__(self, author, original_event, next_event, player, cog, uid):
        super().__init__(timeout=300)
        self.author = author
        self.original_event = original_event
        self.next_event = next_event
        self.player = player
        self.cog = cog
        self.uid = uid
        seen = set()
        for i, choice in enumerate(next_event["choices"]):
            if choice["label"] in seen:
                continue
            seen.add(choice["label"])
            self.add_item(YinYangFinaleSubButton(choice["label"], i))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.author:
            await interaction.response.send_message("这不是你的奇遇。", ephemeral=True)
            return False
        return True


class YinYangFinaleSubButton(discord.ui.Button):
    def __init__(self, label: str, index: int):
        super().__init__(label=label, style=discord.ButtonStyle.secondary)
        self.index = index

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        for item in self.view.children:
            item.disabled = True
        self.view.stop()
        from cogs.explore import _apply_rewards, _pick_choice_result
        choices = self.view.next_event["choices"]
        same = [c for c in choices if c["label"] == choices[self.index]["label"]]
        result = _pick_choice_result(same, dict(self.view.player))
        _apply_rewards(self.view.uid, result.get("rewards", {}))
        await _do_yinyang_rebirth(interaction, self.view.player, self.view.cog, self.view.uid, result.get("flavor", ""))


async def _do_yinyang_rebirth(interaction, player, cog, uid, final_flavor):
    import time
    from utils.db import get_conn
    from utils.realms import lifespan_max_for_realm
    now = time.time()
    new_lifespan = lifespan_max_for_realm(player["realm"])
    with get_conn() as conn:
        conn.execute("""
            UPDATE players SET
                lifespan = ?, cultivation = 0,
                cultivating_until = NULL, cultivating_years = NULL,
                is_dead = 0, is_virgin = 1,
                rebirth_count = rebirth_count + 1,
                has_bahongchen = 1, escape_rate = 50,
                last_active = ?
            WHERE discord_id = ?
        """, (new_lifespan, now, uid))
        conn.commit()
    embed = discord.Embed(
        title="✦ 大梦初醒 ✦",
        description=(
            (f"*{final_flavor}*\n\n" if final_flavor else "") +
            "——\n\n"
            "你猛地睁开眼睛。\n\n"
            "天花板。\n\n"
            "是你熟悉的天花板，木纹，裂缝，还有角落里那块陈年的水渍。\n"
            "你躺在床上，被褥还是原来的被褥，枕头还是原来的枕头。\n\n"
            "窗外有鸟叫，有风，有人声。\n"
            "阳光从窗缝里透进来，落在你的手背上，暖的。\n\n"
            "你坐起来，大口喘气，发现自己满身冷汗。\n\n"
            "洛道村，秋叶青，沈渡，杨敬远——\n"
            "一切像是一场梦。\n\n"
            "但那些悲欢离合，那些选择与沉默，那个女孩最后的笑，\n"
            "却清晰地刻在心里，像是真实发生过的事，\n"
            "挥之不去。\n\n"
            "你低下头，发现手心里有一道淡淡的印记——\n"
            "那块令牌留下的，冰凉的触感，像是某种证明。\n\n"
            "杨敬远的声音最后一次在耳边响起，\n"
            "像是从很远很远的地方传来：\n\n"
            "*「霸红尘会在你需要的时候出现。」*\n"
            "*「好好活着。」*\n\n"
            "——\n\n"
            f"寿元恢复至 **{new_lifespan} 年**，修为清零，处身重置。\n"
            "永久获得：**逃跑成功率 +50%**\n"
            "灵魂深处铭刻：**【一梦浮生·霸红尘使者】**"
        ),
        color=discord.Color.gold(),
    )
    await interaction.followup.send(embed=embed)


class DualCultivateInviteView(discord.ui.View):
    """邀请对方双修的确认面板，只有被邀请者可以点击。"""

    def __init__(self, cog, inviter: discord.User, target: discord.User, multiplier: float, both_virgin: bool):
        super().__init__(timeout=60)
        self.cog = cog
        self.inviter = inviter
        self.target = target
        self.multiplier = multiplier
        self.both_virgin = both_virgin

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.target:
            await interaction.response.send_message("这不是发给你的邀请。", ephemeral=True)
            return False
        return True

    @discord.ui.button(label="接受双修", style=discord.ButtonStyle.success)
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await self.cog.do_dual_cultivate(interaction, self.inviter, self.target, self.multiplier, self.both_virgin)
        self.stop()

    @discord.ui.button(label="拒绝", style=discord.ButtonStyle.danger)
    async def reject(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            f"**{interaction.user.display_name}** 拒绝了双修邀请。"
        )
        self.stop()


def _city_players_embed(city_players: list, viewer: dict) -> discord.Embed:
    from utils.realms import get_realm_index
    viewer_realm_idx = get_realm_index(viewer["realm"]) if viewer else 0
    embed = discord.Embed(title="✦ 同城修士 ✦", color=discord.Color.teal())
    if not city_players:
        embed.description = "此地暂无其他修士。"
        return embed
    lines = []
    for p in city_players:
        p_realm_idx = get_realm_index(p["realm"])
        if p_realm_idx > viewer_realm_idx:
            lines.append(f"**{p['name']}** · {p['realm']}　修为：???")
        else:
            lines.append(f"**{p['name']}** · {p['realm']}　修为：{p['cultivation']}")
    embed.description = "\n".join(lines)
    return embed


def _sects_embed(alignment: str) -> discord.Embed:
    stat_names = {"comprehension": "悟性", "physique": "体魄",
                  "fortune": "机缘", "bone": "根骨", "soul": "神识"}
    embed = discord.Embed(title=f"✦ {alignment}宗门 ✦", color=discord.Color.teal())
    for name, data in SECTS.items():
        if data["alignment"] != alignment:
            continue
        req = data["req"]
        req_parts = []
        if req["min_realm"]:
            req_parts.append(req["min_realm"])
        if req["spirit_roots"]:
            req_parts.append(f"{'或'.join(req['spirit_roots'])}灵根")
        if req["single_root"]:
            req_parts.append("单灵根")
        if req["min_stat"]:
            for stat, val in req["min_stat"].items():
                req_parts.append(f"{stat_names.get(stat, stat)}{val}+")
        if req["min_fortune"]:
            req_parts.append(f"机缘{req['min_fortune']}+")
        req_str = "、".join(req_parts) if req_parts else "无特殊要求"
        embed.add_field(
            name=f"{name} · {data['location']}",
            value=f"{data['desc']}\n入门要求：{req_str}",
            inline=False,
        )
    return embed
