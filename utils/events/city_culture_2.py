from utils.events._base import _e, _c, _cond

EVENTS = []

EVENTS.append(_e(
    "落云城修仙讲坛",
    "落云城灵材商会今日请来一位金丹修士开讲「灵材辨识与修炼」，不少人在台下听讲。",
    [
        _c("入座听讲", next_event={
            "desc": "真人讲得深入浅出，你需凝神记忆，方能化为己用。",
            "choices": [
                _c("专注听讲并默记要点", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 70}, flavor="你从讲坛中悟出几分道理，悟性与修为皆进。悟性 +1，修为 +70"),
                _c("专注听讲并默记要点", rewards={"cultivation": 45}, flavor="你略有所得。修为 +45"),
                _c("听后向真人请教", condition=_cond("soul", 6), rewards={"soul": 1, "reputation": 15}, flavor="真人答你一问，你神识与名声皆进。神识 +1，声望 +15"),
                _c("听后向真人请教", rewards={"reputation": 10}, flavor="真人略答，你名声略增。声望 +10"),
            ]
        }),
        _c("不入场", rewards={}, flavor="你未听讲。"),
    ],
    city="落云城"
))

EVENTS.append(_e(
    "青云坊炼器展览",
    "青云坊铸造行会举办炼器展览，展出各家名匠作品，并有匠师现场讲解「器纹与灵路」。",
    [
        _c("参观并听讲解", next_event={
            "desc": "匠师讲解器纹与灵路的对应关系，你若神识敏锐可捕捉细节。",
            "choices": [
                _c("以神识感应器纹", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 60}, flavor="你以神识感悟器纹奥义，神识与修为皆进。神识 +1，修为 +60"),
                _c("以神识感应器纹", rewards={"cultivation": 40}, flavor="你略有所得。修为 +40"),
                _c("只观不感", rewards={"cultivation": 25}, flavor="你参观一番，略有所悟。修为 +25"),
            ]
        }),
        _c("不参观", rewards={}, flavor="你未参观。"),
    ],
    city="青云坊"
))

EVENTS.append(_e(
    "碧波城海族节日",
    "碧波城今日是海族与人族共庆的「海灵节」，码头有祭祀与市集，据说参与祭祀可得海灵祝福。",
    [
        _c("参与祭祀", next_event={
            "desc": "你随人群献上祭品，祭司念诵祝词，海风拂面，似有一丝灵韵。",
            "choices": [
                _c("静心感应海灵", condition=_cond("fortune", 6), rewards={"fortune": 1, "lifespan": 15}, flavor="你感应到一缕海灵祝福，机缘与寿元皆进。机缘 +1，寿元 +15"),
                _c("静心感应海灵", rewards={"lifespan": 10}, flavor="你略得祝福。寿元 +10"),
                _c("只当热闹", rewards={"reputation": 5}, flavor="你参与了一番，与海族关系略近。声望 +5"),
            ]
        }),
        _c("不参与", rewards={}, flavor="你未参与。"),
    ],
    city="碧波城"
))

EVENTS.append(_e(
    "天水镇水灵祭典",
    "天水镇每年一度「水灵祭典」，镇民在灵泉边祭祀水灵，修士可借祭典时的灵气潮汐修炼片刻。",
    [
        _c("在祭典时于泉边打坐", next_event={
            "desc": "祭典进行时灵泉涌出大量水灵气，你需引导归元。",
            "choices": [
                _c("以神识引导水灵归元", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 80}, flavor="你稳稳炼化水灵，神识与修为皆进。神识 +1，修为 +80"),
                _c("以神识引导水灵归元", rewards={"cultivation": 50}, flavor="你略有所得。修为 +50"),
                _c("只吸收不深炼", rewards={"cultivation": 35, "lifespan": 5}, flavor="你吸收部分灵气，略有补益。修为 +35，寿元 +5"),
            ]
        }),
        _c("只观礼", rewards={}, flavor="你只观礼未修炼。"),
    ],
    city="天水镇"
))

EVENTS.append(_e(
    "玄风城剑道论坛",
    "玄风城剑修们举办「剑道论坛」，众人轮流阐述对剑道的理解，你可上台发言或只旁听。",
    [
        _c("上台阐述己见", next_event={
            "desc": "你阐述自己对剑道的理解，台下有人赞同有人质疑。",
            "choices": [
                _c("与质疑者论剑理", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "reputation": 25}, flavor="你以理服人，悟性与名声皆进。悟性 +1，声望 +25"),
                _c("与质疑者论剑理", rewards={"reputation": 15}, flavor="你论了一场，名声略增。声望 +15"),
                _c("虚心听台下点评", rewards={"cultivation": 45}, flavor="你从点评中有所得。修为 +45"),
            ]
        }),
        _c("只旁听", rewards={"cultivation": 30}, flavor="你旁听论坛，略有所悟。修为 +30"),
    ],
    city="玄风城"
))

EVENTS.append(_e(
    "赤炎城丹道传承",
    "赤炎城丹师公会开放「丹道传承室」一日，内有前辈丹师留下的心得玉简，可付费参阅。",
    [
        _c("付费参阅玉简", next_event={
            "desc": "玉简中记载丹火控温与灵草君臣佐使之道，需悟性方能领会。",
            "choices": [
                _c("静心参悟玉简", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 70}, flavor="你悟出几分丹道至理，悟性与修为皆进。悟性 +1，修为 +70"),
                _c("静心参悟玉简", rewards={"cultivation": 45}, flavor="你略有所得。修为 +45"),
                _c("强记要点", condition=_cond("soul", 6), rewards={"soul": 1}, flavor="你以神识强记要点，神识略增。神识 +1"),
                _c("强记要点", rewards={"spirit_stones": -20}, flavor="你参阅了一个时辰，收获有限。灵石 -20"),
            ]
        }),
        _c("不参阅", rewards={}, flavor="你未参阅。"),
    ],
    city="赤炎城"
))

EVENTS.append(_e(
    "丹霞谷药典讲解",
    "丹霞谷灵药宗对外开放「药典讲解」半日，由执事讲解常见灵草辨识与采摘禁忌。",
    [
        _c("入谷听讲解", next_event={
            "desc": "执事边讲边示以实物，你若神识敏锐可辨细微差异。",
            "choices": [
                _c("以神识辨草", condition=_cond("soul", 6), rewards={"soul": 1, "fortune": 1}, flavor="你以神识牢记药性与形貌，日后采药不误。神识 +1，机缘 +1"),
                _c("以神识辨草", rewards={"soul": 1}, flavor="你辨草能力略增。神识 +1"),
                _c("只记要点", rewards={"cultivation": 35}, flavor="你记下要点，略有所得。修为 +35"),
            ]
        }),
        _c("不听", rewards={}, flavor="你未听讲解。"),
    ],
    city="丹霞谷"
))

EVENTS.append(_e(
    "炎阳城古法传授",
    "炎阳城有老丹师开坛传授「古法控火」——据说是上古炼丹术的简化版，可助火修精进。",
    [
        _c("听讲并尝试控火", next_event={
            "desc": "老丹师演示古法控火，你需以神识与悟性模仿。",
            "choices": [
                _c("按古法练习", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 100}, flavor="你初步掌握古法控火，神识与修为皆进。神识 +1，修为 +100"),
                _c("按古法练习", rewards={"cultivation": 60}, flavor="你略有所得。修为 +60"),
                _c("只记心法不练", condition=_cond("comprehension", 6), rewards={"comprehension": 1}, flavor="你记下心法，悟性略增。悟性 +1"),
                _c("只记心法不练", rewards={"cultivation": 30}, flavor="你记了心法。修为 +30"),
            ]
        }),
        _c("不听", rewards={}, flavor="你未听讲。"),
    ],
    city="炎阳城"
))

EVENTS.append(_e(
    "翠微城医修义诊",
    "翠微城医修行会今日在城门口义诊，修士可免费问诊，医修会根据体质给出调养建议。",
    [
        _c("排队问诊", next_event={
            "desc": "医修为你把脉观气，道你体内有郁结之处，若按方调养可延寿。",
            "choices": [
                _c("按方调养", condition=_cond("fortune", 6), rewards={"lifespan": 30, "fortune": 1}, flavor="你按方调养数日，寿元与气运皆进。寿元 +30，机缘 +1"),
                _c("按方调养", rewards={"lifespan": 20}, flavor="你按方调养，寿元略增。寿元 +20"),
                _c("只记方不调养", rewards={"reputation": 5}, flavor="你谢过医修，未深调。声望 +5"),
            ]
        }),
        _c("不问诊", rewards={}, flavor="你未问诊。"),
    ],
    city="翠微城"
))

EVENTS.append(_e(
    "望月楼天机推演",
    "望月楼顶今日有占卜师开坛「天机推演」，据说可窥见近日机缘走向，但需付灵石且结果随机。",
    [
        _c("付灵石请占", next_event={
            "desc": "占卜师为你推演后道：「三日内若往东南，有小吉；若往西北，平平。」",
            "choices": [
                _c("信其言往东南", condition=_cond("fortune", 6), rewards={"fortune": 2, "spirit_stones": 40}, flavor="你在东南偶得小机缘，气运与灵石皆进。机缘 +2，灵石 +40"),
                _c("信其言往东南", rewards={"fortune": 1}, flavor="你往东南一行，气运略增。机缘 +1"),
                _c("不当真", rewards={"spirit_stones": -15}, flavor="你付了卦金，未应卦。灵石 -15"),
            ]
        }),
        _c("不占", rewards={}, flavor="你未占卜。"),
    ],
    city="望月楼"
))

EVENTS.append(_e(
    "铁甲城武道传承",
    "铁甲城武馆开放「武道传承碑」一日，碑上刻有前人武学心得，修士可观摩感悟。",
    [
        _c("观摩传承碑", next_event={
            "desc": "碑上刻有拳意与体魄运转之法，需体悟方能化为己用。",
            "choices": [
                _c("以体魄感应碑意", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 55}, flavor="你从碑中悟出淬体之法，体魄与修为皆进。体魄 +1，修为 +55"),
                _c("以体魄感应碑意", rewards={"cultivation": 40}, flavor="你略有所得。修为 +40"),
                _c("以悟性参悟碑文", condition=_cond("comprehension", 6), rewards={"comprehension": 1}, flavor="你从碑文中悟出几分武理。悟性 +1"),
                _c("以悟性参悟碑文", rewards={"cultivation": 30}, flavor="你略有所悟。修为 +30"),
            ]
        }),
        _c("不观摩", rewards={}, flavor="你未观摩。"),
    ],
    city="铁甲城"
))

EVENTS.append(_e(
    "黄沙镇土道感悟",
    "黄沙镇外有古人所留「土灵碑」，碑上刻有土属修炼心得，荒漠土灵气充沛时碑文会显灵光。",
    [
        _c("赴土灵碑感悟", next_event={
            "desc": "你至碑前，今日土灵气尚可，碑文隐约有灵光流转。",
            "choices": [
                _c("静心感悟碑文", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "bone": 1}, flavor="你悟出碑中土属淬体之法，悟性与根骨皆进。悟性 +1，根骨 +1"),
                _c("静心感悟碑文", rewards={"bone": 1}, flavor="你根骨略得淬炼。根骨 +1"),
                _c("只观不悟", rewards={"cultivation": 35}, flavor="你略有所得。修为 +35"),
            ]
        }),
        _c("不去", rewards={}, flavor="你未赴土灵碑。"),
    ],
    city="黄沙镇"
))

EVENTS.append(_e(
    "苍穹城雷道讲法",
    "苍穹城雷修前辈在城楼开讲「雷道讲法」，讲述如何借雷意淬体与悟道。",
    [
        _c("登城听讲", next_event={
            "desc": "前辈讲雷意刚猛与生机并存，你需以悟性领会其中平衡。",
            "choices": [
                _c("专注领悟雷道", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 65}, flavor="你悟出雷道中一丝生机之意，悟性与修为皆进。悟性 +1，修为 +65"),
                _c("专注领悟雷道", rewards={"cultivation": 45}, flavor="你略有所得。修为 +45"),
                _c("只记口诀", rewards={"cultivation": 30}, flavor="你记下口诀。修为 +30"),
            ]
        }),
        _c("不听", rewards={}, flavor="你未听讲。"),
    ],
    city="苍穹城"
))

EVENTS.append(_e(
    "寒冰城冰道秘典",
    "寒冰城玄冰派对外开放「冰道秘典」阅览一个时辰，内有基础冰属心法摘要。",
    [
        _c("付费阅览秘典", next_event={
            "desc": "秘典中记载冰属灵气运转与神识御寒之法。",
            "choices": [
                _c("以神识参悟御寒之法", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 60}, flavor="你悟出神识御寒之法，神识与修为皆进。神识 +1，修为 +60"),
                _c("以神识参悟御寒之法", rewards={"cultivation": 40}, flavor="你略有所得。修为 +40"),
                _c("只记要点", rewards={"spirit_stones": -15, "cultivation": 25}, flavor="你阅览一个时辰，略有所得。灵石 -15，修为 +25"),
            ]
        }),
        _c("不阅览", rewards={}, flavor="你未阅览。"),
    ],
    city="寒冰城"
))

EVENTS.append(_e(
    "北冥港航海传说",
    "北冥港老水手在酒馆里讲「北海航海传说」，据说其中藏有深海灵脉与上古沉船的线索。",
    [
        _c("听传说并追问线索", next_event={
            "desc": "老水手酒后多言，提到某片海域常有灵光浮现，但凶险异常。",
            "choices": [
                _c("记下海域方位", condition=_cond("fortune", 6), rewards={"fortune": 1, "spirit_stones": 50}, flavor="你日后按方位探索，偶得一处小机缘。机缘 +1，灵石 +50"),
                _c("记下海域方位", rewards={"fortune": 1}, flavor="你记下方位，气运略增。机缘 +1"),
                _c("只当故事", rewards={}, flavor="你只当故事听。"),
            ]
        }),
        _c("不听", rewards={}, flavor="你未听传说。"),
    ],
    city="北冥港"
))

EVENTS.append(_e(
    "天京城宗门公告",
    "天京城广场张贴着各大宗门的招募与任务公告，你若符合条件可接取或只是了解动向。",
    [
        _c("浏览公告并接一桩小任务", next_event={
            "desc": "你接下一桩「护送灵材」的小任务，报酬不高但可赚名声。",
            "choices": [
                _c("稳妥完成", condition=_cond("physique", 6), rewards={"physique": 1, "reputation": 20}, flavor="你顺利护送灵材，体魄在途中亦有锻炼。体魄 +1，声望 +20"),
                _c("稳妥完成", rewards={"reputation": 15}, flavor="你完成任务，名声略增。声望 +15"),
                _c("途中遇劫", rewards={"lifespan": -3, "reputation": 5}, flavor="你途中遇劫，受伤后勉强完成。寿元 -3，声望 +5"),
            ]
        }),
        _c("只浏览不接", rewards={}, flavor="你只看了公告。"),
    ],
    city="天京城"
))

EVENTS.append(_e(
    "清虚城道法讲经",
    "清虚城古道观今日由观主亲自讲经，讲「无为与有为」在修行中的运用。",
    [
        _c("入观听经", next_event={
            "desc": "观主讲得玄妙，你需以悟性领会，方能化入修行。",
            "choices": [
                _c("静心悟经", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 70}, flavor="你悟出经中几分真意，悟性与修为皆进。悟性 +1，修为 +70"),
                _c("静心悟经", rewards={"cultivation": 45}, flavor="你略有所得。修为 +45"),
                _c("听后请教观主", condition=_cond("soul", 6), rewards={"soul": 1, "reputation": 15}, flavor="观主答你一问，神识与名声皆进。神识 +1，声望 +15"),
                _c("听后请教观主", rewards={"reputation": 10}, flavor="观主略答。声望 +10"),
            ]
        }),
        _c("不听", rewards={}, flavor="你未听经。"),
    ],
    city="清虚城"
))

EVENTS.append(_e(
    "御剑城剑道碑文",
    "御剑城城头悬剑之下有一面「剑道碑」，据说观碑可感剑意，但剑意凌厉，心神不稳者易伤。",
    [
        _c("近前观碑", next_event={
            "desc": "你仰观剑道碑，碑上剑意扑面而来，需以神识或悟性化解。",
            "choices": [
                _c("以神识承接剑意", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 65}, flavor="你以神识化解剑意并感悟，神识与修为皆进。神识 +1，修为 +65"),
                _c("以神识承接剑意", rewards={"cultivation": 40}, flavor="你略有所得。修为 +40"),
                _c("以悟性参悟剑意", condition=_cond("comprehension", 6), rewards={"comprehension": 1}, flavor="你悟出碑中一缕剑意。悟性 +1"),
                _c("以悟性参悟剑意", rewards={"lifespan": -2}, flavor="剑意伤神，你速速退开。寿元 -2"),
            ]
        }),
        _c("不观碑", rewards={}, flavor="你未观碑。"),
    ],
    city="御剑城"
))

EVENTS.append(_e(
    "问道城修仙大会",
    "问道城一年一度修仙大会开幕，散修可报名参加「论道」「演武」「炼丹」等环节，表现佳者有赏。",
    [
        _c("报名参加论道环节", next_event={
            "desc": "你登台论道，与数名散修交锋，需以悟性与神识支撑。",
            "choices": [
                _c("全力论道", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 120}, flavor="你在论道中脱颖而出，得赏并悟性修为皆进。悟性 +1，修为 +120"),
                _c("全力论道", rewards={"cultivation": 80}, flavor="你论道一番，修为大进。修为 +80"),
                _c("只参与不争胜", rewards={"cultivation": 50, "reputation": 10}, flavor="你参与论道，略有收获与名声。修为 +50，声望 +10"),
            ]
        }),
        _c("不报名", rewards={}, flavor="你未报名。"),
    ],
    city="问道城"
))

EVENTS.append(_e(
    "太虚城上古遗迹",
    "太虚城建于上古大能洞府之上，城中有处开放参观的「遗迹残区」，据说感悟遗迹可助悟道。",
    [
        _c("入遗迹残区感悟", next_event={
            "desc": "残区内有残阵与刻纹，年代久远，灵韵微弱但仍可感。",
            "choices": [
                _c("以悟性感悟残阵", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 80}, flavor="你从残阵中悟出一丝上古道韵，悟性与修为皆进。悟性 +1，修为 +80"),
                _c("以悟性感悟残阵", rewards={"cultivation": 50}, flavor="你略有所得。修为 +50"),
                _c("以神识探查刻纹", condition=_cond("soul", 6), rewards={"soul": 1}, flavor="你以神识探查刻纹，神识略增。神识 +1"),
                _c("以神识探查刻纹", rewards={"cultivation": 35}, flavor="你略有所得。修为 +35"),
            ]
        }),
        _c("不入遗迹", rewards={}, flavor="你未入遗迹。"),
    ],
    city="太虚城"
))
