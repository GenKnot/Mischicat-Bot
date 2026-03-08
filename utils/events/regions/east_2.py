from utils.events._base import _e, _c, _cond

EVENTS = []

EVENTS.append(_e(
    "东域海岸奇遇",
    "你在东域海岸行走时，发现一处被潮水冲开的礁石缝，内有灵光闪烁。",
    [
        _c("探手取物", next_event={
            "desc": "缝内有一枚灵蚌与几块被海水打磨过的灵晶，灵蚌紧闭。",
            "choices": [
                _c("取灵蚌", condition=_cond("fortune", 6), rewards={"fortune": 1, "spirit_stones": 70}, flavor="灵蚌内有一颗小珠，售出得利，机缘略增。机缘 +1，灵石 +70"),
                _c("取灵蚌", rewards={"spirit_stones": 40}, flavor="灵蚌内无珠，蚌肉可售。灵石 +40"),
                _c("只取灵晶", rewards={"spirit_stones": 50}, flavor="你取走灵晶，未动灵蚌。灵石 +50"),
            ]
        }),
        _c("不取，离开", rewards={}, flavor="你未动礁石缝。"),
    ]
))

EVENTS.append(_e(
    "东域水灵异变",
    "东域某处水潭忽然灵气翻涌，据说是地脉短暂异动，在此修炼可事半功倍。",
    [
        _c("趁机在潭边打坐", next_event={
            "desc": "你盘坐潭边吸纳水灵，需以神识引导，否则灵气驳杂易伤经脉。",
            "choices": [
                _c("以神识引导水灵", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 80}, flavor="你稳稳炼化水灵，神识与修为皆进。神识 +1，修为 +80"),
                _c("以神识引导水灵", rewards={"cultivation": 50}, flavor="你略有所得。修为 +50"),
                _c("强行吸纳", rewards={"lifespan": -3, "cultivation": 60}, flavor="灵气略伤经脉，你有所得但损元气。寿元 -3，修为 +60"),
            ]
        }),
        _c("不修炼", rewards={}, flavor="你未在潭边修炼。"),
    ]
))

EVENTS.append(_e(
    "东域剑修传承",
    "东域山道旁有一块残碑，碑上刻着半式剑招，据说是某位剑修所留。",
    [
        _c("驻足参悟剑招", next_event={
            "desc": "你凝神观碑，剑意隐约浮现，需以悟性捕捉。",
            "choices": [
                _c("以悟性参悟", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 70}, flavor="你悟出半式剑意，悟性与修为皆进。悟性 +1，修为 +70"),
                _c("以悟性参悟", rewards={"cultivation": 45}, flavor="你略有所得。修为 +45"),
                _c("只记形不悟意", rewards={"cultivation": 25}, flavor="你记下剑招外形。修为 +25"),
            ]
        }),
        _c("不参悟", rewards={}, flavor="你未驻足。"),
    ]
))

EVENTS.append(_e(
    "东域海底遗迹",
    "东域近海有渔民称水下有古遗迹露出，修士可闭气下潜一探，但需神识辨路。",
    [
        _c("下潜探查", next_event={
            "desc": "你潜入水下，遗迹残垣中有灵光闪烁，但水压与暗流令人不适。",
            "choices": [
                _c("以神识辨路取宝", condition=_cond("soul", 6), rewards={"soul": 1, "spirit_stones": 80}, flavor="你以神识寻到一处灵材，带回售出。神识 +1，灵石 +80"),
                _c("以神识辨路取宝", rewards={"spirit_stones": 50}, flavor="你取到部分灵材。灵石 +50"),
                _c("体魄硬撑多待片刻", condition=_cond("physique", 6), rewards={"physique": 1, "spirit_stones": 60}, flavor="你多待片刻多取一物，体魄在水压中略增。体魄 +1，灵石 +60"),
                _c("体魄硬撑多待片刻", rewards={"lifespan": -4, "spirit_stones": 35}, flavor="你略受水压所伤。寿元 -4，灵石 +35"),
            ]
        }),
        _c("不下潜", rewards={}, flavor="你未下潜。"),
    ]
))

EVENTS.append(_e(
    "东域渔村求援",
    "东域渔村有村民拦路求援，说村中灵舟被海兽所伤，请修士帮忙驱赶近海妖兽。",
    [
        _c("答应相助", next_event={
            "desc": "你随村民至海边，果有低阶海兽在近海游荡。驱赶需动手或震慑。",
            "choices": [
                _c("出手驱赶海兽", condition=_cond("physique", 6), rewards={"physique": 1, "reputation": 30}, flavor="你击退海兽，村民感激，名声传开。体魄 +1，声望 +30"),
                _c("出手驱赶海兽", rewards={"reputation": 20}, flavor="你驱赶海兽，村民酬谢。声望 +20"),
                _c("以神识震慑", condition=_cond("soul", 6), rewards={"soul": 1, "reputation": 25}, flavor="你以神识震慑，海兽退走。神识 +1，声望 +25"),
                _c("以神识震慑", rewards={"reputation": 15}, flavor="海兽略退，村民略谢。声望 +15"),
            ]
        }),
        _c("不答应", rewards={}, flavor="你未答应。"),
    ]
))

EVENTS.append(_e(
    "东域灵石矿脉",
    "东域某山脚因山体滑坡露出一小段灵石矿脉，已有修士在争抢开采。",
    [
        _c("加入开采", next_event={
            "desc": "你挤进人群抢采，矿脉品质一般但量不少，需防他人争抢。",
            "choices": [
                _c("抢采后速退", condition=_cond("physique", 6), rewards={"physique": 1, "spirit_stones": 100}, flavor="你采到一批灵石后速退，体魄在拥挤中亦有锻炼。体魄 +1，灵石 +100"),
                _c("抢采后速退", rewards={"spirit_stones": 65}, flavor="你采到部分灵石。灵石 +65"),
                _c("与人协商平分", condition=_cond("reputation", 15), rewards={"reputation": 15, "spirit_stones": 70}, flavor="你提议平分，众人同意，名声与灵石皆得。声望 +15，灵石 +70"),
                _c("与人协商平分", rewards={"spirit_stones": 50}, flavor="你与人平分，略有所得。灵石 +50"),
            ]
        }),
        _c("不参与", rewards={}, flavor="你未参与开采。"),
    ]
))

EVENTS.append(_e(
    "东域古剑出世",
    "东域一处古修洞府坍塌，有人从废墟中捡到一柄锈剑，剑身仍有一丝剑意残留。",
    [
        _c("以灵石换锈剑", next_event={
            "desc": "你换到锈剑后尝试感悟剑意，需根骨与悟性方能承受。",
            "choices": [
                _c("以悟性化解剑意再感悟", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "bone": 1}, flavor="你化解剑意后悟出一式残招，悟性与根骨皆进。悟性 +1，根骨 +1"),
                _c("以悟性化解剑意再感悟", rewards={"bone": 1}, flavor="剑意淬体，根骨略增。根骨 +1"),
                _c("强行感悟", rewards={"lifespan": -3, "cultivation": 40}, flavor="剑意伤身，你略有所得。寿元 -3，修为 +40"),
            ]
        }),
        _c("不换", rewards={}, flavor="你未换锈剑。"),
    ]
))

EVENTS.append(_e(
    "东域海族使者",
    "东域海岸有海族使者上岸，称愿与人族修士「以物易物」，但只与有缘人交易。",
    [
        _c("上前求易", next_event={
            "desc": "海族使者打量你后，取出一颗灵珠与一截珊瑚，要你以等值灵材或灵石来换。",
            "choices": [
                _c("以灵石换灵珠", condition=_cond("fortune", 6), rewards={"spirit_stones": -40, "fortune": 1, "lifespan": 20}, flavor="灵珠品质上乘，服后机缘与寿元皆进。灵石 -40，机缘 +1，寿元 +20"),
                _c("以灵石换灵珠", rewards={"spirit_stones": -40, "lifespan": 12}, flavor="灵珠略有补益。灵石 -40，寿元 +12"),
                _c("以灵石换珊瑚", rewards={"spirit_stones": -35, "cultivation": 50}, flavor="珊瑚可入药修炼。灵石 -35，修为 +50"),
                _c("不换", rewards={}, flavor="你未交易。"),
            ]
        }),
        _c("不上前", rewards={}, flavor="你未与海族交易。"),
    ]
))

EVENTS.append(_e(
    "东域风暴前兆",
    "东域海上风暴将至，沿岸修士纷纷加固洞府或收船。你若在此时出海或留守岸边，皆有可能遇机缘或遇险。",
    [
        _c("留守岸边观风暴", next_event={
            "desc": "风暴席卷而过，你在岸边以体魄扛住余波，同时感悟天地之威。",
            "choices": [
                _c("以体魄硬抗余波", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 55}, flavor="你扛住风暴余波，体魄与修为皆进。体魄 +1，修为 +55"),
                _c("以体魄硬抗余波", rewards={"cultivation": 35}, flavor="你略有所得。修为 +35"),
                _c("避入洞府修炼", rewards={"cultivation": 45}, flavor="你避入洞府，借风暴灵气略增修为。修为 +45"),
            ]
        }),
        _c("不观风暴", rewards={}, flavor="你未观风暴。"),
    ]
))

EVENTS.append(_e(
    "东域炼器秘法",
    "东域青云坊外有一名散修炼器师在摆摊，称可传授「控火三诀」——炼器控火的基础秘法，收费不菲。",
    [
        _c("付费学习", next_event={
            "desc": "炼器师演示三诀，你需以悟性与神识模仿。",
            "choices": [
                _c("专心模仿", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 60}, flavor="你初步掌握控火三诀，悟性与修为皆进。悟性 +1，修为 +60"),
                _c("专心模仿", rewards={"cultivation": 40}, flavor="你略有所得。修为 +40"),
                _c("只记口诀", rewards={"spirit_stones": -30, "cultivation": 25}, flavor="你付了费但只记下口诀。灵石 -30，修为 +25"),
            ]
        }),
        _c("不学", rewards={}, flavor="你未学习。"),
    ]
))
