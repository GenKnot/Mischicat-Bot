from utils.events._base import _e, _c, _cond

EVENTS = []

EVENTS.append(_e(
    "北域冰原迷路",
    "你在北域冰原上赶路时遇暴风雪，迷失方向。需以神识辨位或体魄硬撑，方能脱困。",
    [
        _c("以神识辨方向", condition=_cond("soul", 6), rewards={"soul": 1, "fortune": 1}, flavor="你以神识感应地脉与风雪走向，辨明方向脱困。神识 +1，机缘 +1"),
        _c("以神识辨方向", rewards={"lifespan": -2}, flavor="你勉强辨出方向，多耗半日。寿元 -2"),
        _c("以体魄硬撑等雪停", condition=_cond("physique", 6), rewards={"physique": 1}, flavor="你以体魄扛住严寒，雪停后辨路脱困。体魄 +1"),
        _c("以体魄硬撑等雪停", rewards={"lifespan": -5}, flavor="严寒侵体，你元气大伤后脱困。寿元 -5"),
    ]
))

EVENTS.append(_e(
    "北域冰修传承",
    "北域寒冰城郊外有一块「冰修传承碑」，据说感悟碑意可助冰属或水属修士精进。",
    [
        _c("赴碑前感悟", next_event={
            "desc": "碑上刻有冰属心法要诀，寒气逼人，需以神识或体魄承受。",
            "choices": [
                _c("以神识承接碑意", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 70}, flavor="你以神识化解碑意并感悟，神识与修为皆进。神识 +1，修为 +70"),
                _c("以神识承接碑意", rewards={"cultivation": 45}, flavor="你略有所得。修为 +45"),
                _c("以体魄硬抗寒气", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 55}, flavor="你以体魄承受寒气观碑，体魄与修为皆进。体魄 +1，修为 +55"),
                _c("以体魄硬抗寒气", rewards={"lifespan": -3, "cultivation": 35}, flavor="寒气伤身，你略有所得。寿元 -3，修为 +35"),
            ]
        }),
        _c("不感悟", rewards={}, flavor="你未赴碑前。"),
    ]
))

EVENTS.append(_e(
    "北域兽潮来袭",
    "北域雪狼城接到兽潮预警，城主府征募修士协防。你若应征，需与守军并肩抵御妖兽。",
    [
        _c("应征协防", next_event={
            "desc": "兽潮来时你与守军并肩作战，雪狼与冰兽前赴后继。",
            "choices": [
                _c("死守防线", condition=_cond("physique", 6), rewards={"physique": 1, "spirit_stones": 90}, flavor="你顶住兽潮，赏金与体魄皆得。体魄 +1，灵石 +90"),
                _c("死守防线", rewards={"lifespan": -5, "spirit_stones": 55}, flavor="你受伤但守住防线。寿元 -5，灵石 +55"),
                _c("以神识预警侧翼", condition=_cond("soul", 6), rewards={"soul": 1, "reputation": 25}, flavor="你以神识预警，减少伤亡，神识与名声皆进。神识 +1，声望 +25"),
                _c("以神识预警侧翼", rewards={"reputation": 15}, flavor="你协防有功。声望 +15"),
            ]
        }),
        _c("不应征", rewards={}, flavor="你不应征。"),
    ]
))

EVENTS.append(_e(
    "北域深海灵珠",
    "北冥港有渔民从深海捞到一批灵珠，正在码头贱卖。灵珠品质参差不齐，全凭眼力与运气。",
    [
        _c("在码头挑选灵珠", next_event={
            "desc": "你在一堆灵珠中挑选，需以神识辨成色，否则易买到劣品。",
            "choices": [
                _c("以神识辨成色", condition=_cond("soul", 6), rewards={"soul": 1, "spirit_stones": 80}, flavor="你挑到上品灵珠，服下或售出皆宜。神识 +1，灵石 +80"),
                _c("以神识辨成色", rewards={"spirit_stones": 50}, flavor="你挑到中品灵珠。灵石 +50"),
                _c("随手抓几颗", condition=_cond("fortune", 6), rewards={"fortune": 1, "lifespan": 15}, flavor="你随手抓到的竟是上品，服下后寿元与机缘皆进。机缘 +1，寿元 +15"),
                _c("随手抓几颗", rewards={"lifespan": 8}, flavor="你买到普通灵珠，略滋寿元。寿元 +8"),
            ]
        }),
        _c("不买", rewards={}, flavor="你未买灵珠。"),
    ]
))

EVENTS.append(_e(
    "北域鬼修奇遇",
    "北域幽冥镇外有野鬼游荡，一名鬼修称可「以阴养神」——若你愿让他在你识海外围下一道阴印，可助神识精进，但有风险。",
    [
        _c("答应尝试", next_event={
            "desc": "鬼修在你识海外围种下阴印，你需以神识化解阴气，否则易伤神魂。",
            "choices": [
                _c("以神识化解阴气", condition=_cond("soul", 6), rewards={"soul": 1, "bone": 1}, flavor="你化解阴气并反哺己身，神识与根骨皆进。神识 +1，根骨 +1"),
                _c("以神识化解阴气", rewards={"soul": 1}, flavor="你化解阴气，神识略增。神识 +1"),
                _c("未化解", rewards={"lifespan": -5, "soul": 1}, flavor="阴气略伤心神与寿元，但神识亦有锻炼。寿元 -5，神识 +1"),
            ]
        }),
        _c("不答应", rewards={}, flavor="你未答应。"),
    ]
))

EVENTS.append(_e(
    "北域极寒感悟",
    "北域玄冰谷外围有一处「极寒风口」，修士可在此借极寒之气淬体悟道，但不宜久留。",
    [
        _c("赴风口感悟", next_event={
            "desc": "你在风口边缘打坐，极寒之气侵入体内，需以体魄或功法化解。",
            "choices": [
                _c("以体魄承受极寒", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 80}, flavor="你以体魄承受极寒淬体，体魄与修为皆进。体魄 +1，修为 +80"),
                _c("以体魄承受极寒", rewards={"cultivation": 50}, flavor="你略有所得。修为 +50"),
                _c("以神识引导寒气", condition=_cond("soul", 6), rewards={"soul": 1, "lifespan": 15}, flavor="你以神识引导寒气滋养神魂，神识与寿元皆进。神识 +1，寿元 +15"),
                _c("以神识引导寒气", rewards={"lifespan": -4, "soul": 1}, flavor="寒气略伤寿元，但神识有进。寿元 -4，神识 +1"),
            ]
        }),
        _c("不赴风口", rewards={}, flavor="你未赴风口。"),
    ]
))

EVENTS.append(_e(
    "北域万年玄冰",
    "北域玄冰谷深处偶有「万年玄冰」碎块被寒气推出谷口，修士可尝试取走炼化或出售。",
    [
        _c("在谷口守候", next_event={
            "desc": "你守了一日，果然有碎块被推出。取时需抵御寒气，炼化需体魄或神识。",
            "choices": [
                _c("取碎块炼化", condition=_cond("physique", 6), rewards={"physique": 1, "lifespan": 40}, flavor="你以体魄承受玄冰寒气炼化，体魄与寿元皆进。体魄 +1，寿元 +40"),
                _c("取碎块炼化", rewards={"lifespan": 25}, flavor="你炼化玄冰，寿元略增。寿元 +25"),
                _c("取碎块出售", rewards={"spirit_stones": 90}, flavor="你将玄冰碎块售出。灵石 +90"),
            ]
        }),
        _c("不守候", rewards={}, flavor="你未守候。"),
    ]
))

EVENTS.append(_e(
    "北域雪狼群袭",
    "你在北域雪原上遇雪狼群，狼群未主动攻击但拦路不退。你可战可绕。",
    [
        _c("出手驱狼", next_event={
            "desc": "你与狼群交手，头狼凶悍，需体魄或巧劲制胜。",
            "choices": [
                _c("以体魄硬撼头狼", condition=_cond("physique", 6), rewards={"physique": 1, "spirit_stones": 70}, flavor="你击退头狼，狼群散去，你取狼皮售出。体魄 +1，灵石 +70"),
                _c("以体魄硬撼头狼", rewards={"lifespan": -5, "spirit_stones": 40}, flavor="你受伤但击退狼群。寿元 -5，灵石 +40"),
                _c("以神识震慑", condition=_cond("soul", 6), rewards={"soul": 1}, flavor="你以神识震慑头狼，狼群退走。神识 +1"),
                _c("以神识震慑", rewards={}, flavor="狼群略退，你趁机绕路。"),
            ]
        }),
        _c("绕路", rewards={"lifespan": -2}, flavor="你绕远路避开狼群。寿元 -2"),
    ]
))

EVENTS.append(_e(
    "北域阴气异变",
    "北域幽冥镇附近阴气忽然加重，有鬼修称是「阴脉喷发」，在此修炼阴属或神识可事半功倍。",
    [
        _c("借阴气修炼", next_event={
            "desc": "你在阴气浓郁处打坐，需以神识引导阴气，否则易伤阳气。",
            "choices": [
                _c("以神识引导阴气", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 65}, flavor="你以神识化阴气为用，神识与修为皆进。神识 +1，修为 +65"),
                _c("以神识引导阴气", rewards={"cultivation": 45}, flavor="你略有所得。修为 +45"),
                _c("未引导", rewards={"lifespan": -5, "soul": 1}, flavor="阴气略伤寿元，但神识有进。寿元 -5，神识 +1"),
            ]
        }),
        _c("不借阴气修炼", rewards={}, flavor="你未在阴气处修炼。"),
    ]
))

EVENTS.append(_e(
    "北域冰晶矿脉",
    "北域寒冰城附近发现一小段冰晶矿脉，修士可付费入内开采半日。",
    [
        _c("付费入内开采", next_event={
            "desc": "矿脉内极寒，开采时需运功御寒，体魄强者可多采。",
            "choices": [
                _c("以体魄御寒多采", condition=_cond("physique", 6), rewards={"physique": 1, "spirit_stones": 90}, flavor="你以体魄扛住寒气，采到不少冰晶。体魄 +1，灵石 +90"),
                _c("以体魄御寒多采", rewards={"spirit_stones": 60}, flavor="你采到部分冰晶。灵石 +60"),
                _c("浅采即退", rewards={"spirit_stones": 50, "lifespan": -2}, flavor="你浅层开采后速退，略受寒气。灵石 +50，寿元 -2"),
            ]
        }),
        _c("不开采", rewards={}, flavor="你未开采。"),
    ]
))
