from utils.events._base import _e, _c, _cond

EVENTS = []

EVENTS.append(_e(
    "南域火山异动",
    "南域某座火山近日异动，喷出大量火灵气。有修士在火山口外围吸纳火灵修炼。",
    [
        _c("赴火山外围修炼", next_event={
            "desc": "你在外围打坐，火灵气扑面而来，需以功法引导，否则易灼伤经脉。",
            "choices": [
                _c("以神识引导火灵", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 80}, flavor="你稳稳炼化火灵，神识与修为皆进。神识 +1，修为 +80"),
                _c("以神识引导火灵", rewards={"cultivation": 50}, flavor="你略有所得。修为 +50"),
                _c("以体魄硬抗", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 60}, flavor="你以体魄承受火灵淬体。体魄 +1，修为 +60"),
                _c("以体魄硬抗", rewards={"lifespan": -4, "cultivation": 40}, flavor="火灵略伤经脉。寿元 -4，修为 +40"),
            ]
        }),
        _c("不赴火山", rewards={}, flavor="你未赴火山。"),
    ]
))

EVENTS.append(_e(
    "南域丹师传承",
    "南域一处荒废丹房被人发现，内有前人留下的丹方残卷与一只旧丹炉。",
    [
        _c("入丹房查探", next_event={
            "desc": "你翻阅残卷，丹方残缺但可辨出几味主药；丹炉已裂，但炉壁刻有控火口诀。",
            "choices": [
                _c("参悟控火口诀", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 70}, flavor="你悟出控火口诀精髓，悟性与修为皆进。悟性 +1，修为 +70"),
                _c("参悟控火口诀", rewards={"cultivation": 45}, flavor="你略有所得。修为 +45"),
                _c("只抄丹方", rewards={"spirit_stones": 40}, flavor="你将残卷抄录，售与丹师得灵石。灵石 +40"),
            ]
        }),
        _c("不入丹房", rewards={}, flavor="你未入丹房。"),
    ]
))

EVENTS.append(_e(
    "南域灵草秘地",
    "南域翠微城附近有人发现一处隐蔽灵草秘地，消息传开后不少人在寻入口。",
    [
        _c("随人寻找秘地", next_event={
            "desc": "你寻到入口后进入，秘地内灵草已被采走大半，但角落仍有遗漏。",
            "choices": [
                _c("以神识搜寻遗漏", condition=_cond("soul", 6), rewards={"soul": 1, "spirit_stones": 100}, flavor="你以神识找到几株遗漏灵草，售出得利。神识 +1，灵石 +100"),
                _c("以神识搜寻遗漏", rewards={"spirit_stones": 60}, flavor="你找到部分灵草。灵石 +60"),
                _c("以机缘碰运气", condition=_cond("fortune", 6), rewards={"fortune": 1, "spirit_stones": 80}, flavor="你误打误撞找到一株珍稀灵草。机缘 +1，灵石 +80"),
                _c("以机缘碰运气", rewards={"spirit_stones": 40}, flavor="你采到几株普通灵草。灵石 +40"),
            ]
        }),
        _c("不寻", rewards={}, flavor="你未寻秘地。"),
    ]
))

EVENTS.append(_e(
    "南域占卜奇遇",
    "南域望月楼附近有一名游方占卜师摆摊，称可「测机缘走向」，一卦二十灵石。",
    [
        _c("付灵石占卦", next_event={
            "desc": "占卜师道：「你机缘在火与木之间，往南域丹霞、翠微一带或有所得。」",
            "choices": [
                _c("信其言往丹霞/翠微", condition=_cond("fortune", 6), rewards={"fortune": 1, "cultivation": 60}, flavor="你在那一带偶得小机缘，修为与气运皆进。机缘 +1，修为 +60"),
                _c("信其言往丹霞/翠微", rewards={"cultivation": 40}, flavor="你走了一趟，略有所得。修为 +40"),
                _c("不当真", rewards={"spirit_stones": -20}, flavor="你付了卦金未应卦。灵石 -20"),
            ]
        }),
        _c("不占", rewards={}, flavor="你未占卦。"),
    ]
))

EVENTS.append(_e(
    "南域火灵感悟",
    "南域赤炎城郊外有一处地火裂缝，修士可在此感悟火灵之意，但需神识守心以免心火过旺。",
    [
        _c("赴地火裂缝感悟", next_event={
            "desc": "你盘坐于裂缝旁，地火之意涌入识海，需以神识化解。",
            "choices": [
                _c("以神识化解火意", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 65}, flavor="你化解火意并感悟，神识与修为皆进。神识 +1，修为 +65"),
                _c("以神识化解火意", rewards={"cultivation": 45}, flavor="你略有所得。修为 +45"),
                _c("强忍感悟", rewards={"lifespan": -3, "soul": 1}, flavor="火意略伤心神，但神识亦有锻炼。寿元 -3，神识 +1"),
            ]
        }),
        _c("不感悟", rewards={}, flavor="你未赴地火裂缝。"),
    ]
))

EVENTS.append(_e(
    "南域医修义诊",
    "南域翠微城医修行会下乡义诊，路过修士可免费问诊，医修会据体质赠一味调养方。",
    [
        _c("排队问诊", next_event={
            "desc": "医修为你把脉后，赠你一道「养神方」，需以灵石购齐药材自煎。",
            "choices": [
                _c("购药按方调养", condition=_cond("fortune", 6), rewards={"spirit_stones": -25, "lifespan": 30, "fortune": 1}, flavor="你按方调养，寿元与气运皆进。灵石 -25，寿元 +30，机缘 +1"),
                _c("购药按方调养", rewards={"spirit_stones": -25, "lifespan": 20}, flavor="你按方调养，寿元略增。灵石 -25，寿元 +20"),
                _c("只记方不购药", rewards={}, flavor="你记下方子，未购药。"),
            ]
        }),
        _c("不问诊", rewards={}, flavor="你未问诊。"),
    ]
))

EVENTS.append(_e(
    "南域古丹炉",
    "南域某处遗迹出土一座古丹炉，炉身刻有符文，据说以特定手法催动可助炼丹成丹率。",
    [
        _c("近前观摩丹炉符文", next_event={
            "desc": "你细看炉身符文，需以悟性领会其中规律。",
            "choices": [
                _c("以悟性参悟符文", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "bone": 1}, flavor="你悟出符文中的控火与凝丹之理，悟性与根骨皆进。悟性 +1，根骨 +1"),
                _c("以悟性参悟符文", rewards={"bone": 1}, flavor="你略有所得，根骨略增。根骨 +1"),
                _c("只记形不悟意", rewards={"cultivation": 35}, flavor="你记下符文外形。修为 +35"),
            ]
        }),
        _c("不观摩", rewards={}, flavor="你未观摩。"),
    ]
))

EVENTS.append(_e(
    "南域木灵异变",
    "南域一片灵木林忽然疯长，木灵气外泄。有修士在林边吸纳木灵修炼。",
    [
        _c("赴林边修炼", next_event={
            "desc": "木灵气温和但量大，你需引导归元，否则易滞塞经脉。",
            "choices": [
                _c("以神识引导木灵", condition=_cond("soul", 6), rewards={"soul": 1, "lifespan": 15}, flavor="木灵滋养神魂与寿元，神识与寿元皆进。神识 +1，寿元 +15"),
                _c("以神识引导木灵", rewards={"lifespan": 10}, flavor="你略有所得。寿元 +10"),
                _c("只吸收不深炼", rewards={"cultivation": 50}, flavor="你吸收部分木灵。修为 +50"),
            ]
        }),
        _c("不修炼", rewards={}, flavor="你未赴林边。"),
    ]
))

EVENTS.append(_e(
    "南域天机泄露",
    "南域望月楼有占卜师酒后失言，泄露「某处三日后将现灵光」的模糊天机，听者众多。",
    [
        _c("信其言三日后赴该处", next_event={
            "desc": "三日后你赶赴传闻方位，是否真有灵光全凭机缘。",
            "choices": [
                _c("静候灵光", condition=_cond("fortune", 6), rewards={"fortune": 2, "cultivation": 60}, flavor="灵光如期出现，你吸纳后机缘与修为皆进。机缘 +2，修为 +60"),
                _c("静候灵光", rewards={"fortune": 1}, flavor="灵光微弱，你略有所得。机缘 +1"),
                _c("未等到灵光", rewards={"lifespan": -1}, flavor="你白等一日。寿元 -1"),
            ]
        }),
        _c("不信", rewards={}, flavor="你未赴该处。"),
    ]
))

EVENTS.append(_e(
    "南域炼丹比试",
    "南域赤炎城举办小型炼丹比试，参赛者同炼一炉「培元丹」，成丹品质高者得赏。",
    [
        _c("报名参赛", next_event={
            "desc": "你与数名丹师同台炼丹，需以神识控火、悟性把握时机。",
            "choices": [
                _c("全力炼丹", condition=_cond("soul", 6), rewards={"soul": 1, "reputation": 25}, flavor="你炼成上品培元丹，夺得名次，神识与名声皆进。神识 +1，声望 +25"),
                _c("全力炼丹", rewards={"reputation": 15}, flavor="你炼成合格丹，名声略增。声望 +15"),
                _c("炼丹时感悟丹道", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 50}, flavor="你在炼丹中悟出几分丹道。悟性 +1，修为 +50"),
                _c("炼丹时感悟丹道", rewards={"cultivation": 35}, flavor="你略有所得。修为 +35"),
            ]
        }),
        _c("不参赛", rewards={}, flavor="你未参赛。"),
    ]
))
