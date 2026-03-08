from utils.events._base import _e, _c, _cond

EVENTS = []

EVENTS.append(_e(
    "西域沙漠迷途",
    "你在西域荒漠中行走时迷失方向，沙丘起伏难辨东西。若选对方向可尽快脱困，选错则多耗时日。",
    [
        _c("以神识辨方向", condition=_cond("soul", 6), rewards={"soul": 1, "fortune": 1}, flavor="你以神识感应地脉与星位，辨明方向走出荒漠。神识 +1，机缘 +1"),
        _c("以神识辨方向", rewards={"lifespan": -2}, flavor="你勉强辨出方向，多花半日脱困。寿元 -2"),
        _c("凭体魄硬走", condition=_cond("physique", 6), rewards={"physique": 1}, flavor="你凭体魄在荒漠中多撑了一日，终遇商队得救。体魄 +1"),
        _c("凭体魄硬走", rewards={"lifespan": -4}, flavor="你在荒漠中困了两日才脱困。寿元 -4"),
    ]
))

EVENTS.append(_e(
    "西域武修擂台",
    "西域铁甲城外设有一座露天擂台，过路修士可自由上台切磋，胜者得赏金。",
    [
        _c("上台切磋", next_event={
            "desc": "擂主是一名体修，拳重如山。你需以体魄或巧劲应对。",
            "choices": [
                _c("以体魄硬撼", condition=_cond("physique", 7), rewards={"physique": 1, "spirit_stones": 70}, flavor="你以体魄压制擂主，胜出得赏。体魄 +1，灵石 +70"),
                _c("以体魄硬撼", rewards={"lifespan": -6, "spirit_stones": 25}, flavor="你力战不敌，带伤下台。寿元 -6，灵石 +25"),
                _c("以巧劲寻破绽", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "spirit_stones": 60}, flavor="你以巧破千斤，胜出。悟性 +1，灵石 +60"),
                _c("以巧劲寻破绽", rewards={"lifespan": -4, "spirit_stones": 20}, flavor="你寻隙不成反被击中。寿元 -4，灵石 +20"),
            ]
        }),
        _c("不切磋", rewards={}, flavor="你未上台。"),
    ]
))

EVENTS.append(_e(
    "西域商路劫匪",
    "西域沙罗城商路上有劫匪出没，你若护送商队一程，可得酬金；若独自赶路，也可能遇劫。",
    [
        _c("接护送任务", next_event={
            "desc": "你随商队行至半途，劫匪果然出现。需击退或震慑对方。",
            "choices": [
                _c("出手击退劫匪", condition=_cond("physique", 6), rewards={"physique": 1, "spirit_stones": 80}, flavor="你击退劫匪，商队酬谢。体魄 +1，灵石 +80"),
                _c("出手击退劫匪", rewards={"lifespan": -4, "spirit_stones": 50}, flavor="你受伤但击退劫匪。寿元 -4，灵石 +50"),
                _c("以神识震慑", condition=_cond("soul", 6), rewards={"soul": 1, "spirit_stones": 65}, flavor="你以神识震慑，劫匪未战先怯。神识 +1，灵石 +65"),
                _c("以神识震慑", rewards={"spirit_stones": 45}, flavor="劫匪略退，商队酬谢。灵石 +45"),
            ]
        }),
        _c("不接任务", rewards={}, flavor="你未接任务。"),
    ]
))

EVENTS.append(_e(
    "西域雷灵感悟",
    "西域苍穹城附近有一处雷击谷，谷中常有余雷游走，修士可在此借雷意淬体悟道。",
    [
        _c("入谷感悟", next_event={
            "desc": "你在谷中行走，余雷偶有劈落，需以体魄或神识承受。",
            "choices": [
                _c("以体魄承受余雷", condition=_cond("physique", 6), rewards={"physique": 1, "bone": 1}, flavor="余雷淬体，体魄与根骨皆进。体魄 +1，根骨 +1"),
                _c("以体魄承受余雷", rewards={"bone": 1}, flavor="你根骨略得淬炼。根骨 +1"),
                _c("以神识引导雷意", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 55}, flavor="你以神识化雷意入体，神识与修为皆进。神识 +1，修为 +55"),
                _c("以神识引导雷意", rewards={"lifespan": -3, "cultivation": 35}, flavor="雷意略伤神魂。寿元 -3，修为 +35"),
            ]
        }),
        _c("不入谷", rewards={}, flavor="你未入谷。"),
    ]
))

EVENTS.append(_e(
    "西域古战遗迹",
    "西域古战场边缘有新塌陷的坑洞，有人从坑中捡到法器残片与功法碎简。",
    [
        _c("入坑探查", next_event={
            "desc": "坑内阴气与煞气混杂，你需尽快搜寻并退出，否则易伤神魂。",
            "choices": [
                _c("以神识搜寻后速退", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 100}, flavor="你以神识寻到一枚功法碎简，参悟后神识与修为皆进。神识 +1，修为 +100"),
                _c("以神识搜寻后速退", rewards={"cultivation": 60}, flavor="你寻到残片售出，略有所得。修为 +60"),
                _c("多待片刻深搜", condition=_cond("fortune", 6), rewards={"fortune": 1, "spirit_stones": 80}, flavor="你多搜片刻，找到一件完整小法器。机缘 +1，灵石 +80"),
                _c("多待片刻深搜", rewards={"lifespan": -5, "spirit_stones": 40}, flavor="煞气侵体，你带伤退出。寿元 -5，灵石 +40"),
            ]
        }),
        _c("不入坑", rewards={}, flavor="你未入坑。"),
    ]
))

EVENTS.append(_e(
    "西域土灵矿脉",
    "西域黄沙镇外发现一小段土灵矿脉，镇民与过路修士可付费入内开采半日。",
    [
        _c("付费入内开采", next_event={
            "desc": "矿脉内土灵气浓郁，开采时若以体魄承受重压，可兼得淬体之效。",
            "choices": [
                _c("边采边以体魄承压", condition=_cond("physique", 6), rewards={"physique": 1, "spirit_stones": 90}, flavor="你采到不少土灵矿并淬体。体魄 +1，灵石 +90"),
                _c("边采边以体魄承压", rewards={"spirit_stones": 60}, flavor="你采到部分土灵矿。灵石 +60"),
                _c("只采不炼体", rewards={"spirit_stones": 55}, flavor="你专注开采。灵石 +55"),
            ]
        }),
        _c("不开采", rewards={}, flavor="你未开采。"),
    ]
))

EVENTS.append(_e(
    "西域流沙秘境",
    "西域荒漠中有流沙秘境传闻——流沙下偶有古修洞府被冲出，但陷入流沙极为凶险。",
    [
        _c("在流沙边缘试探", next_event={
            "desc": "你在流沙边缘以神识探查，若机缘好可感应到下方灵物。",
            "choices": [
                _c("以神识探流沙深处", condition=_cond("soul", 6), rewards={"soul": 1, "spirit_stones": 70}, flavor="你以神识探到一处灵物，以灵力摄出。神识 +1，灵石 +70"),
                _c("以神识探流沙深处", rewards={"spirit_stones": 45}, flavor="你探到零星灵材。灵石 +45"),
                _c("冒险入流沙取宝", condition=_cond("physique", 7), rewards={"physique": 1, "spirit_stones": 90}, flavor="你以体魄与灵力硬闯流沙，取到灵物。体魄 +1，灵石 +90"),
                _c("冒险入流沙取宝", rewards={"lifespan": -8, "spirit_stones": 35}, flavor="你险些陷落，带伤取到少许。寿元 -8，灵石 +35"),
            ]
        }),
        _c("不试探", rewards={}, flavor="你未试探流沙。"),
    ]
))

EVENTS.append(_e(
    "西域情报网络",
    "西域沙罗城以消息灵通著称，你若肯花灵石，可从情报贩子处买到「某地近日机缘」类情报。",
    [
        _c("买一条情报", next_event={
            "desc": "贩子卖给你一条「某矿脉三日后开放」的情报，要价四十灵石。",
            "choices": [
                _c("信情报三日后前往", condition=_cond("fortune", 6), rewards={"fortune": 1, "spirit_stones": 65}, flavor="情报属实，你在矿脉处有所收获。机缘 +1，灵石 +65"),
                _c("信情报三日后前往", rewards={"spirit_stones": 40}, flavor="矿脉确有开放，你略有所得。灵石 +40"),
                _c("不信", rewards={"spirit_stones": -40}, flavor="你未前往，灵石白花。灵石 -40"),
            ]
        }),
        _c("不买", rewards={}, flavor="你未买情报。"),
    ]
))

EVENTS.append(_e(
    "西域防御法器",
    "西域黄沙镇以防御类法器著称，镇中炼器铺开放「防御阵纹」观摩半日，修士可付费参悟。",
    [
        _c("付费观摩阵纹", next_event={
            "desc": "阵纹繁复，需以悟性领会其中防护之理。",
            "choices": [
                _c("以悟性参悟阵纹", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 55}, flavor="你悟出阵纹中几分防护至理，悟性与修为皆进。悟性 +1，修为 +55"),
                _c("以悟性参悟阵纹", rewards={"cultivation": 40}, flavor="你略有所得。修为 +40"),
                _c("只记形不悟意", rewards={"spirit_stones": -20, "cultivation": 25}, flavor="你观摩半日，略有所得。灵石 -20，修为 +25"),
            ]
        }),
        _c("不观摩", rewards={}, flavor="你未观摩。"),
    ]
))

EVENTS.append(_e(
    "西域边关守将",
    "西域烈风关守将征募临时「协防修士」，协防三日可得赏金与军功名声。",
    [
        _c("应募协防", next_event={
            "desc": "你随守军巡关三日，偶有小股流寇试探，你参与击退。",
            "choices": [
                _c("主动出击驱寇", condition=_cond("physique", 6), rewards={"physique": 1, "reputation": 30}, flavor="你主动出击击退流寇，守将为你请功。体魄 +1，声望 +30"),
                _c("主动出击驱寇", rewards={"reputation": 20}, flavor="你参与驱寇，名声略增。声望 +20"),
                _c("稳守关墙", rewards={"reputation": 25, "spirit_stones": 40}, flavor="你稳守关墙三日，守将酬谢。声望 +25，灵石 +40"),
            ]
        }),
        _c("不应募", rewards={}, flavor="你不应募。"),
    ]
))
