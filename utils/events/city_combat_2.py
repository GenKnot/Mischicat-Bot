from utils.events._base import _e, _c, _cond

EVENTS = []

EVENTS.append(_e(
    "落云城护卫纠纷",
    "落云城灵材市场外，一队商队护卫与地痞发生冲突，双方剑拔弩张，围观者众多。",
    [
        _c("上前劝架", next_event={
            "desc": "你挤进人群调停，护卫头领与地痞头目各执一词，需以声望或实力压服双方。",
            "choices": [
                _c("以声望劝和", condition=_cond("reputation", 25), rewards={"reputation": 25}, flavor="双方卖你面子，纠纷平息，你在落云城名声更响。声望 +25"),
                _c("以声望劝和", rewards={"reputation": 10}, flavor="双方勉强罢手，你略得名声。声望 +10"),
                _c("站在护卫一方驱散地痞", condition=_cond("physique", 6), rewards={"physique": 1, "reputation": 20}, flavor="你出手助护卫，地痞散去，护卫酬谢你。体魄 +1，声望 +20"),
                _c("站在护卫一方驱散地痞", rewards={"reputation": 5}, flavor="你助拳后纠纷平息。声望 +5"),
            ]
        }),
        _c("不掺和，离开", rewards={}, flavor="你绕开冲突离开。"),
    ],
    city="落云城"
))

EVENTS.append(_e(
    "青云坊炼器比试",
    "青云坊铸造行会举办「炼器比试」，参赛者以同一批灵铁铸器，成器品质高者得赏。",
    [
        _c("报名参赛", next_event={
            "desc": "你与数名炼器师同台铸器，需以神识控火、悟性把握器纹。",
            "choices": [
                _c("全力铸器", condition=_cond("soul", 6), rewards={"soul": 1, "spirit_stones": 60}, flavor="你铸成一件上品，夺得名次，神识与灵石皆进。神识 +1，灵石 +60"),
                _c("全力铸器", rewards={"spirit_stones": 35}, flavor="你铸成一件合格品，得了安慰赏。灵石 +35"),
                _c("铸器时感悟器道", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "bone": 1}, flavor="你在铸器中悟出一丝器道，悟性与根骨皆进。悟性 +1，根骨 +1"),
                _c("铸器时感悟器道", rewards={"cultivation": 40}, flavor="你略有所得。修为 +40"),
            ]
        }),
        _c("只观摩不参赛", rewards={"cultivation": 25}, flavor="你观摩比试，略有所悟。修为 +25"),
    ],
    city="青云坊"
))

EVENTS.append(_e(
    "碧波城海妖残党",
    "碧波城码头传来警报：一股海妖残党趁夜偷袭商船，城主府悬赏剿妖。",
    [
        _c("接赏剿妖", next_event={
            "desc": "你与数名修士登船迎战，海妖残党数量不多但悍不畏死。",
            "choices": [
                _c("冲在前方斩妖", condition=_cond("physique", 7), rewards={"physique": 1, "spirit_stones": 80}, flavor="你力斩数名海妖，赏金与体魄皆得。体魄 +1，灵石 +80"),
                _c("冲在前方斩妖", rewards={"lifespan": -4, "spirit_stones": 50}, flavor="你受伤但坚持到底，得了赏金。寿元 -4，灵石 +50"),
                _c("以神识配合队友", condition=_cond("soul", 6), rewards={"soul": 1, "reputation": 20}, flavor="你以神识预警配合，减少伤亡，声望与神识皆进。神识 +1，声望 +20"),
                _c("以神识配合队友", rewards={"reputation": 10}, flavor="你配合队友击退海妖。声望 +10"),
            ]
        }),
        _c("不接赏，离开", rewards={}, flavor="你未参与剿妖。"),
    ],
    city="碧波城"
))

EVENTS.append(_e(
    "天水镇水贼劫道",
    "天水镇外水道传来求救声，一伙水贼正在打劫过往灵舟。",
    [
        _c("赶去相助", next_event={
            "desc": "你御气踏水而至，水贼见有人来，分出一半人迎向你。",
            "choices": [
                _c("速战速决", condition=_cond("physique", 6), rewards={"physique": 1, "spirit_stones": 60}, flavor="你击溃水贼，救下灵舟，船主酬谢。体魄 +1，灵石 +60"),
                _c("速战速决", rewards={"spirit_stones": 40}, flavor="你击退水贼，得了部分酬谢。灵石 +40"),
                _c("以巧劲擒贼首", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "reputation": 25}, flavor="你擒下贼首，余贼溃散，官府赏你。悟性 +1，声望 +25"),
                _c("以巧劲擒贼首", rewards={"reputation": 15}, flavor="你助官府擒贼，名声略增。声望 +15"),
            ]
        }),
        _c("不理会", rewards={}, flavor="你未前往。"),
    ],
    city="天水镇"
))

EVENTS.append(_e(
    "玄风城剑修挑衅",
    "玄风城广场上，一名外来的剑修正在叫阵，称「玄风城剑修不过如此」，已有数人落败。",
    [
        _c("上台应战", next_event={
            "desc": "对方剑法凌厉，你需以悟性寻破绽或以体魄硬抗。",
            "choices": [
                _c("以剑意破招", condition=_cond("comprehension", 7), rewards={"comprehension": 1, "reputation": 30}, flavor="你以精妙剑意胜出，玄风城修士喝彩。悟性 +1，声望 +30"),
                _c("以剑意破招", rewards={"lifespan": -5, "reputation": 10}, flavor="你落败但打出风采。寿元 -5，声望 +10"),
                _c("以体魄硬撼", condition=_cond("physique", 7), rewards={"physique": 1, "spirit_stones": 50}, flavor="你以体魄压制对方剑势，胜出得彩头。体魄 +1，灵石 +50"),
                _c("以体魄硬撼", rewards={"lifespan": -6}, flavor="对方剑快，你受伤落败。寿元 -6"),
            ]
        }),
        _c("不应战", rewards={}, flavor="你未上台。"),
    ],
    city="玄风城"
))

EVENTS.append(_e(
    "赤炎城火修斗法",
    "赤炎城丹师公会外，两名火修因琐事斗法，火焰四溅，路人纷纷躲避。",
    [
        _c("上前制止", next_event={
            "desc": "你介入二人之间，需以实力或口才压下火头。",
            "choices": [
                _c("以灵力隔开二人", condition=_cond("physique", 6), rewards={"physique": 1, "reputation": 20}, flavor="你以体魄与灵力隔开斗法，二人罢手。体魄 +1，声望 +20"),
                _c("以灵力隔开二人", rewards={"reputation": 10}, flavor="你勉强隔开二人。声望 +10"),
                _c("出言调解", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "reputation": 25}, flavor="你以理服人，二人悻悻收手。悟性 +1，声望 +25"),
                _c("出言调解", rewards={"reputation": 5}, flavor="二人略给你面子。声望 +5"),
            ]
        }),
        _c("不理会", rewards={}, flavor="你绕道离开。"),
    ],
    city="赤炎城"
))

EVENTS.append(_e(
    "丹霞谷药材争夺",
    "丹霞谷外有人为争一株灵草大打出手，双方皆称是自己先发现。",
    [
        _c("劝双方罢手并提议平分", condition=_cond("reputation", 15), rewards={"reputation": 20, "spirit_stones": 30}, flavor="双方卖你面子，灵草平分，各赠你一点谢礼。声望 +20，灵石 +30"),
        _c("劝双方罢手并提议平分", rewards={"reputation": 10}, flavor="双方勉强同意平分。声望 +10"),
        _c("趁乱取走灵草", condition=_cond("fortune", 6), rewards={"fortune": 1, "spirit_stones": 60}, flavor="你趁乱取走灵草，二人未追及。机缘 +1，灵石 +60"),
        _c("趁乱取走灵草", rewards={"lifespan": -5, "spirit_stones": 20}, flavor="你被二人发现，受伤后带灵草逃逸。寿元 -5，灵石 +20"),
        _c("不掺和", rewards={}, flavor="你未掺和。"),
    ],
    city="丹霞谷"
))

EVENTS.append(_e(
    "炎阳城擂台赛",
    "炎阳城广场设擂，擂主是一名火修，已连胜数场。胜者可获赏金与一枚「火纹丹」。",
    [
        _c("上台挑战", next_event={
            "desc": "擂主火法凶猛，你需以体魄硬抗或悟性寻隙。",
            "choices": [
                _c("以体魄扛火再反击", condition=_cond("physique", 7), rewards={"physique": 1, "spirit_stones": 70, "reputation": 30}, flavor="你扛住火法后反击得手，赢得赏金与名声。体魄 +1，灵石 +70，声望 +30"),
                _c("以体魄扛火再反击", rewards={"lifespan": -6, "reputation": 15}, flavor="你受伤落败，但打出气势。寿元 -6，声望 +15"),
                _c("以身法避火寻隙", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 60}, flavor="你以巧破千斤，胜出后服火纹丹修为大进。悟性 +1，修为 +60"),
                _c("以身法避火寻隙", rewards={"lifespan": -4, "cultivation": 30}, flavor="你寻隙不成反被灼伤。寿元 -4，修为 +30"),
            ]
        }),
        _c("不挑战", rewards={}, flavor="你未上台。"),
    ],
    city="炎阳城"
))

EVENTS.append(_e(
    "铁甲城武修擂台",
    "铁甲城中央擂台今日开放「体修专场」，只许以体魄与拳脚相搏，胜者赏金翻倍。",
    [
        _c("上台参战", next_event={
            "desc": "对手是一名专修体魄的武修，拳重如山。",
            "choices": [
                _c("硬碰硬", condition=_cond("physique", 7), rewards={"physique": 1, "spirit_stones": 80}, flavor="你以体魄压制对手，赢得赏金，体魄亦在战中精进。体魄 +1，灵石 +80"),
                _c("硬碰硬", rewards={"lifespan": -8, "spirit_stones": 30}, flavor="你力战不敌，带伤下台。寿元 -8，灵石 +30"),
                _c("以巧劲卸力", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "spirit_stones": 65}, flavor="你以巧劲化解蛮力，胜出。悟性 +1，灵石 +65"),
                _c("以巧劲卸力", rewards={"lifespan": -5, "spirit_stones": 25}, flavor="你卸力不及，落败。寿元 -5，灵石 +25"),
            ]
        }),
        _c("只观战", rewards={"cultivation": 35}, flavor="你观战有所得。修为 +35"),
    ],
    city="铁甲城"
))

EVENTS.append(_e(
    "沙罗城刺客袭击",
    "沙罗城巷中传出打斗声，一名商人正遭刺客围攻。西域商路凶险，此类事偶有发生。",
    [
        _c("出手相救", next_event={
            "desc": "你杀入战团，刺客见有人援手，分出一人缠住你。",
            "choices": [
                _c("速杀缠斗者再助商人", condition=_cond("physique", 6), rewards={"physique": 1, "spirit_stones": 70, "reputation": 25}, flavor="你击退刺客，商人重谢。体魄 +1，灵石 +70，声望 +25"),
                _c("速杀缠斗者再助商人", rewards={"spirit_stones": 45}, flavor="你助商人脱险，商人酬谢。灵石 +45"),
                _c("以神识预警助商人躲避", condition=_cond("soul", 6), rewards={"soul": 1, "fortune": 1}, flavor="你以神识提前预警，商人躲过致命一击，刺客退走。神识 +1，机缘 +1"),
                _c("以神识预警助商人躲避", rewards={"reputation": 15}, flavor="你助商人脱险。声望 +15"),
            ]
        }),
        _c("不掺和", rewards={}, flavor="你未出手。"),
    ],
    city="沙罗城"
))

EVENTS.append(_e(
    "烈风关边境冲突",
    "烈风关外有小股流寇试探关防，守关修士人手不足，临时征募路人助守。",
    [
        _c("应募助守", next_event={
            "desc": "你随守关修士出关迎击，流寇见有关内援军，且战且退。",
            "choices": [
                _c("追击流寇", condition=_cond("physique", 6), rewards={"physique": 1, "reputation": 25}, flavor="你追出数里击溃流寇残部，守关修士为你请功。体魄 +1，声望 +25"),
                _c("追击流寇", rewards={"reputation": 15}, flavor="你参与追击，略立功。声望 +15"),
                _c("稳守关墙不追", rewards={"reputation": 20}, flavor="你稳守关墙，流寇退走后守将谢你。声望 +20"),
            ]
        }),
        _c("不应募", rewards={}, flavor="你未应募。"),
    ],
    city="烈风关"
))

EVENTS.append(_e(
    "苍穹城雷修比试",
    "苍穹城雷修之间流行「引雷比试」——谁能在雷云下引雷更多而不伤，谁胜。",
    [
        _c("参与引雷比试", next_event={
            "desc": "你站上比试台，雷云低垂。需以神识引导雷意或体魄硬抗余波。",
            "choices": [
                _c("以神识引雷", condition=_cond("soul", 7), rewards={"soul": 1, "bone": 1}, flavor="你以神识引导雷意入体淬骨，神识与根骨皆进。神识 +1，根骨 +1"),
                _c("以神识引雷", rewards={"cultivation": 55}, flavor="你引下一道雷，略有所得。修为 +55"),
                _c("以体魄硬抗", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 50}, flavor="你以体魄承受雷击，淬体有效。体魄 +1，修为 +50"),
                _c("以体魄硬抗", rewards={"lifespan": -5, "cultivation": 30}, flavor="雷击过猛，你受伤但有所得。寿元 -5，修为 +30"),
            ]
        }),
        _c("只观摩", rewards={"cultivation": 30}, flavor="你观摩雷修比试，略有所悟。修为 +30"),
    ],
    city="苍穹城"
))

EVENTS.append(_e(
    "寒冰城冰修决斗",
    "寒冰城有两位冰修因私怨约战冰窟，观战者需自担寒气。",
    [
        _c("入冰窟观战", next_event={
            "desc": "二人冰法对轰，窟内寒气逼人。你需运功抵御寒气，同时观摩冰意。",
            "choices": [
                _c("运功抵御并专注观战", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 60}, flavor="你从冰法对决中悟出一丝冰意，神识与修为皆进。神识 +1，修为 +60"),
                _c("运功抵御并专注观战", rewards={"cultivation": 40}, flavor="你略有所得。修为 +40"),
                _c("以体魄硬抗寒气", condition=_cond("physique", 6), rewards={"physique": 1}, flavor="你以体魄扛住寒气观完全程，体魄略增。体魄 +1"),
                _c("以体魄硬抗寒气", rewards={"lifespan": -3}, flavor="寒气侵体，你提前退出。寿元 -3"),
            ]
        }),
        _c("不观战", rewards={}, flavor="你未入冰窟。"),
    ],
    city="寒冰城"
))

EVENTS.append(_e(
    "幽冥镇鬼修骚扰",
    "幽冥镇外有野鬼骚扰过路修士，镇中鬼修不愿管「镇外事」。你若出手驱鬼，或可赚赏金。",
    [
        _c("接赏驱鬼", next_event={
            "desc": "你在镇外蹲守，野鬼现身时阴风阵阵，需以神识或阳气克制。",
            "choices": [
                _c("以神识冲击野鬼", condition=_cond("soul", 6), rewards={"soul": 1, "spirit_stones": 60}, flavor="你以神识击散野鬼，赏金与神识皆得。神识 +1，灵石 +60"),
                _c("以神识冲击野鬼", rewards={"spirit_stones": 40}, flavor="你驱散野鬼，得了赏金。灵石 +40"),
                _c("以灵力化阳火驱鬼", condition=_cond("physique", 6), rewards={"physique": 1, "spirit_stones": 50}, flavor="你以阳刚灵力驱鬼，体魄在运功中略增。体魄 +1，灵石 +50"),
                _c("以灵力化阳火驱鬼", rewards={"lifespan": -3, "spirit_stones": 30}, flavor="野鬼反扑，你略损元气后驱散。寿元 -3，灵石 +30"),
            ]
        }),
        _c("不接赏", rewards={}, flavor="你未接赏。"),
    ],
    city="幽冥镇"
))

EVENTS.append(_e(
    "雪狼城兽潮预警",
    "雪狼城接到预警：附近兽潮即将过境，城主府征募修士协防，酬金从丰。",
    [
        _c("应征协防", next_event={
            "desc": "兽潮来时你与守军并肩作战，雪狼与冰兽前赴后继。",
            "choices": [
                _c("死守防线", condition=_cond("physique", 7), rewards={"physique": 1, "spirit_stones": 100}, flavor="你顶住兽潮，战后赏金丰厚，体魄亦在战中精进。体魄 +1，灵石 +100"),
                _c("死守防线", rewards={"lifespan": -6, "spirit_stones": 60}, flavor="你受伤但守住防线，得了赏金。寿元 -6，灵石 +60"),
                _c("以神识指挥侧翼", condition=_cond("soul", 6), rewards={"soul": 1, "reputation": 25}, flavor="你以神识协调侧翼，减少伤亡，声望与神识皆进。神识 +1，声望 +25"),
                _c("以神识指挥侧翼", rewards={"reputation": 15}, flavor="你协防有功。声望 +15"),
            ]
        }),
        _c("不应征", rewards={}, flavor="你未应征。"),
    ],
    city="雪狼城"
))

EVENTS.append(_e(
    "天京城宗门冲突",
    "天京城两大宗门弟子在坊市争执，险些动手。若有人调停得当，两宗皆会记一份人情。",
    [
        _c("出面调停", condition=_cond("reputation", 20), rewards={"reputation": 40}, flavor="你声望足够，两宗弟子卖你面子，各自退让。声望 +40"),
        _c("出面调停", rewards={"reputation": 20}, flavor="你勉强劝住双方。声望 +20"),
        _c("站在一方施压", condition=_cond("physique", 6), rewards={"physique": 1, "reputation": 15}, flavor="你助一方压过对方，但得罪另一宗。体魄 +1，声望 +15"),
        _c("站在一方施压", rewards={"reputation": -10}, flavor="你助拳后反被两宗记恨。声望 -10"),
        _c("不掺和", rewards={}, flavor="你未掺和。"),
    ],
    city="天京城"
))

EVENTS.append(_e(
    "灵虚城势力博弈",
    "灵虚城某势力派人暗中试探你的立场，若应对得当，或可得一方赏识；应对不当则惹祸。",
    [
        _c("含糊应对，不表态", rewards={"fortune": 1}, flavor="你滴水不漏，对方觉得你深不可测，未再纠缠。机缘 +1"),
        _c("明确拒绝卷入", rewards={"reputation": 5}, flavor="你表明不掺和，对方悻悻而去。声望 +5"),
        _c("顺势接下一桩小任务", next_event={
            "desc": "对方请你送一封密信到某处，事成有赏，但若泄露可能惹麻烦。",
            "choices": [
                _c("稳妥送达", condition=_cond("fortune", 6), rewards={"fortune": 1, "spirit_stones": 70}, flavor="你顺利送达，获赏，机缘略增。机缘 +1，灵石 +70"),
                _c("稳妥送达", rewards={"spirit_stones": 45}, flavor="你送达密信，得了赏金。灵石 +45"),
                _c("途中遇劫", rewards={"lifespan": -4, "spirit_stones": 20}, flavor="你途中遇劫，受伤后勉强送达。寿元 -4，灵石 +20"),
            ]
        }),
    ],
    city="灵虚城"
))

EVENTS.append(_e(
    "御剑城飞剑比试",
    "御剑城有「飞剑竞速」之俗——修士御剑绕城一周，先归者胜。",
    [
        _c("参加飞剑竞速", next_event={
            "desc": "你御剑而起，需以神识控剑、悟性择路。",
            "choices": [
                _c("全速飞行", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "spirit_stones": 55}, flavor="你择捷径且控剑精准，夺得名次。悟性 +1，灵石 +55"),
                _c("全速飞行", rewards={"spirit_stones": 30}, flavor="你完成竞速，得了安慰赏。灵石 +30"),
                _c("稳中求进", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 50}, flavor="你以神识稳控飞剑，虽未夺魁但感悟剑意。神识 +1，修为 +50"),
                _c("稳中求进", rewards={"cultivation": 35}, flavor="你完成竞速，略有所得。修为 +35"),
            ]
        }),
        _c("不参加", rewards={}, flavor="你未参加。"),
    ],
    city="御剑城"
))

EVENTS.append(_e(
    "问道城论道争锋",
    "问道城有「论道争锋」——二人对坐论道，以神识与悟性相抗，先心神失守者败。",
    [
        _c("参与论道争锋", next_event={
            "desc": "你与一名散修对坐论道，对方神识不弱，句句机锋。",
            "choices": [
                _c("以神识固守本心", condition=_cond("soul", 6), rewards={"soul": 1, "reputation": 20}, flavor="你神识稳固，对方先露破绽，你胜出。神识 +1，声望 +20"),
                _c("以神识固守本心", rewards={"reputation": 10}, flavor="你勉强撑住，和局收场。声望 +10"),
                _c("以悟性反攻", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 55}, flavor="你以妙语反制，对方心服口服。悟性 +1，修为 +55"),
                _c("以悟性反攻", rewards={"lifespan": -2, "cultivation": 30}, flavor="你反攻不成反伤神。寿元 -2，修为 +30"),
            ]
        }),
        _c("不参与", rewards={}, flavor="你未参与。"),
    ],
    city="问道城"
))

EVENTS.append(_e(
    "紫霄城宗门弟子冲突",
    "紫霄城内两派宗门弟子因争夺一处灵气充沛的修炼位而冲突，旁人不敢劝。",
    [
        _c("以声望劝开", condition=_cond("reputation", 30), rewards={"reputation": 30}, flavor="你声望足够，两派弟子各退一步。声望 +30"),
        _c("以声望劝开", rewards={"reputation": 10}, flavor="你劝了几句，冲突略缓。声望 +10"),
        _c("提议抽签定修炼位", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "reputation": 25}, flavor="你提议抽签，两派接受，对你印象不错。悟性 +1，声望 +25"),
        _c("提议抽签定修炼位", rewards={"reputation": 15}, flavor="两派接受抽签。声望 +15"),
        _c("不掺和", rewards={}, flavor="你未掺和。"),
    ],
    city="紫霄城"
))
