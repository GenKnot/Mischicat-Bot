from utils.events._base import _e, _c, _cond

EVENTS = []

EVENTS.append(_e(
    "中州宗门招募",
    "中州天京城几大宗门联合设点招募，你若符合条件可报名试炼，通过者可获引荐与赏赐。",
    [
        _c("报名试炼", next_event={
            "desc": "试炼分「悟性」「体魄」「机缘」三关，你需择一关主攻。",
            "choices": [
                _c("主攻悟性关", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "reputation": 30}, flavor="你通过悟性关，得宗门赏识，悟性与名声皆进。悟性 +1，声望 +30"),
                _c("主攻悟性关", rewards={"reputation": 15}, flavor="你未通过但表现尚可。声望 +15"),
                _c("主攻体魄关", condition=_cond("physique", 6), rewards={"physique": 1, "reputation": 30}, flavor="你通过体魄关，得赏。体魄 +1，声望 +30"),
                _c("主攻体魄关", rewards={"reputation": 15}, flavor="你未通过但表现尚可。声望 +15"),
                _c("主攻机缘关", condition=_cond("fortune", 6), rewards={"fortune": 1, "reputation": 30}, flavor="你通过机缘关，得赏。机缘 +1，声望 +30"),
                _c("主攻机缘关", rewards={"reputation": 15}, flavor="你未通过但表现尚可。声望 +15"),
            ]
        }),
        _c("不报名", rewards={}, flavor="你未报名。"),
    ]
))

EVENTS.append(_e(
    "中州古道感悟",
    "中州清虚城郊外有一段「古道」，据说是上古修士常行之路，石阶上残存道韵。",
    [
        _c("踏古道而行", next_event={
            "desc": "你一步步踏过古道，道韵时隐时现，需以悟性捕捉。",
            "choices": [
                _c("以悟性感悟道韵", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 80}, flavor="你从古道中悟出一丝道意，悟性与修为皆进。悟性 +1，修为 +80"),
                _c("以悟性感悟道韵", rewards={"cultivation": 50}, flavor="你略有所得。修为 +50"),
                _c("以神识感应道韵", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 60}, flavor="你以神识感应道韵，神识与修为皆进。神识 +1，修为 +60"),
                _c("以神识感应道韵", rewards={"cultivation": 40}, flavor="你略有所得。修为 +40"),
            ]
        }),
        _c("不走古道", rewards={}, flavor="你未走古道。"),
    ]
))

EVENTS.append(_e(
    "中州势力博弈",
    "中州灵虚城各大势力明争暗斗，你若肯替某方跑腿送信，可得报酬，但可能得罪另一方。",
    [
        _c("接下一桩送信", next_event={
            "desc": "你将密信送至指定地点，途中是否顺利全凭机缘。",
            "choices": [
                _c("稳妥送达", condition=_cond("fortune", 6), rewards={"fortune": 1, "spirit_stones": 70}, flavor="你顺利送达，雇主重谢。机缘 +1，灵石 +70"),
                _c("稳妥送达", rewards={"spirit_stones": 45}, flavor="你送达密信，得了报酬。灵石 +45"),
                _c("途中遇劫", rewards={"lifespan": -4, "spirit_stones": 25}, flavor="你途中遇劫，受伤后勉强送达。寿元 -4，灵石 +25"),
            ]
        }),
        _c("不接", rewards={}, flavor="你未接活。"),
    ]
))

EVENTS.append(_e(
    "中州灵气汇聚",
    "中州紫霄城因灵气冠绝，每逢月圆有「灵气潮汐」，修士可借机在城中打坐，事半功倍。",
    [
        _c("月圆夜在紫霄城打坐", next_event={
            "desc": "灵气潮汐涌来，你需以神识引导归元，否则易撑伤经脉。",
            "choices": [
                _c("以神识引导灵气", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 120}, flavor="你稳稳炼化潮汐灵气，神识与修为皆进。神识 +1，修为 +120"),
                _c("以神识引导灵气", rewards={"cultivation": 80}, flavor="你略有所得。修为 +80"),
                _c("强行吸纳", rewards={"lifespan": -5, "cultivation": 90}, flavor="灵气略伤经脉，你有所得但损元气。寿元 -5，修为 +90"),
            ]
        }),
        _c("不打坐", rewards={}, flavor="你未借潮汐修炼。"),
    ]
))

EVENTS.append(_e(
    "中州上古遗迹",
    "中州太虚城开放「遗迹残区」第二层，据说内有上古修士留下的神识考验，通过者可获感悟。",
    [
        _c("入第二层接受考验", next_event={
            "desc": "你进入遗迹二层，神识考验袭来，需固守本心。",
            "choices": [
                _c("以神识固守", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 80}, flavor="你通过神识考验，获得上古修士一丝感悟。神识 +1，修为 +80"),
                _c("以神识固守", rewards={"cultivation": 55}, flavor="你勉强通过，略有所得。修为 +55"),
                _c("未通过", rewards={"lifespan": -3}, flavor="你神识受创，速速退出。寿元 -3"),
            ]
        }),
        _c("不入第二层", rewards={}, flavor="你未入第二层。"),
    ]
))

EVENTS.append(_e(
    "中州飞剑奇遇",
    "中州御剑城传说城头无主飞剑偶有「择主」之兆，若在城下感悟剑意，或可得飞剑一丝认可。",
    [
        _c("在城下感悟剑意", next_event={
            "desc": "你仰观城头飞剑，剑意凛然，需以悟性与根骨承受。",
            "choices": [
                _c("以悟性承接剑意", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 70}, flavor="你悟出飞剑中一缕剑意，悟性与修为皆进。悟性 +1，修为 +70"),
                _c("以悟性承接剑意", rewards={"cultivation": 45}, flavor="你略有所得。修为 +45"),
                _c("以根骨承受剑压", condition=_cond("bone", 6), rewards={"bone": 1}, flavor="你以根骨承受剑压，根骨略增。根骨 +1"),
                _c("以根骨承受剑压", rewards={"lifespan": -2}, flavor="剑压过重，你速速退开。寿元 -2"),
            ]
        }),
        _c("不感悟", rewards={}, flavor="你未在城下感悟。"),
    ]
))

EVENTS.append(_e(
    "中州论道大会",
    "中州问道城举办论道大会，散修可报名登台论道，胜者可获赏金与名声。",
    [
        _c("报名登台论道", next_event={
            "desc": "你与一名对手对坐论道，以神识与悟性相抗。",
            "choices": [
                _c("以悟性论道", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "reputation": 25}, flavor="你论道胜出，悟性与名声皆进。悟性 +1，声望 +25"),
                _c("以悟性论道", rewards={"reputation": 15}, flavor="你论道一番，名声略增。声望 +15"),
                _c("以神识固守", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 60}, flavor="你以神识固守本心，未败且有所得。神识 +1，修为 +60"),
                _c("以神识固守", rewards={"cultivation": 40}, flavor="你略有所得。修为 +40"),
            ]
        }),
        _c("不报名", rewards={}, flavor="你未报名。"),
    ]
))

EVENTS.append(_e(
    "中州顶级拍卖",
    "中州万宝楼举办小型顶级拍卖，入场需验资。你若入场，可竞拍或只观摩。",
    [
        _c("入场并择机竞拍", next_event={
            "desc": "台上有一件「无名古物」起拍价不高，另有一件热门法器被争抢。",
            "choices": [
                _c("拍无名古物", condition=_cond("comprehension", 6), rewards={"spirit_stones": -60, "comprehension": 1, "cultivation": 80}, flavor="古物竟是残篇心法，你参悟后悟性与修为皆进。灵石 -60，悟性 +1，修为 +80"),
                _c("拍无名古物", rewards={"spirit_stones": -60, "cultivation": 50}, flavor="古物略有灵性。灵石 -60，修为 +50"),
                _c("只观摩不拍", rewards={"reputation": 5}, flavor="你见识了顶级拍卖。声望 +5"),
            ]
        }),
        _c("不入场", rewards={}, flavor="你未入场。"),
    ]
))

EVENTS.append(_e(
    "中州道观传承",
    "中州清虚城古道观开放「道观传承阁」半日，修士可付费入内参阅道法心得。",
    [
        _c("付费入阁参阅", next_event={
            "desc": "阁中玉简记载道法心得，需以悟性领会。",
            "choices": [
                _c("静心参悟", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 100}, flavor="你悟出心得中几分真意，悟性与修为皆进。悟性 +1，修为 +100"),
                _c("静心参悟", rewards={"cultivation": 65}, flavor="你略有所得。修为 +65"),
                _c("只记不悟", rewards={"spirit_stones": -25, "cultivation": 35}, flavor="你参阅半日，略有所得。灵石 -25，修为 +35"),
            ]
        }),
        _c("不参阅", rewards={}, flavor="你未入阁。"),
    ]
))

EVENTS.append(_e(
    "中州地脉异动",
    "中州太虚城因建于上古洞府之上，近日地脉异动，城中灵气短暂暴涨。修士可借机修炼。",
    [
        _c("借异动在城中打坐", next_event={
            "desc": "地脉灵气涌来，你需以神识引导，否则易撑伤经脉。",
            "choices": [
                _c("以神识引导灵气", condition=_cond("soul", 6), rewards={"soul": 1, "lifespan": 30}, flavor="你稳稳炼化地脉灵气，神识与寿元皆进。神识 +1，寿元 +30"),
                _c("以神识引导灵气", rewards={"lifespan": 20}, flavor="你略有所得。寿元 +20"),
                _c("强行吸纳", rewards={"lifespan": 10, "cultivation": 70}, flavor="你吸纳部分灵气，寿元与修为皆有进。寿元 +10，修为 +70"),
            ]
        }),
        _c("不借机修炼", rewards={}, flavor="你未借异动修炼。"),
    ]
))
