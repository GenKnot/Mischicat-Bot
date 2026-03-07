from utils.events._base import _e, _c, _cond

EVENTS = []

EVENTS.append(_e(
    "落难修士",
    "路边躺着一位受了重伤的修士，气息奄奄，身旁散落着几件法器碎片，显然刚经历了一场恶战。",
    [
        _c("上前救治", next_event={
            "desc": "修士在你的帮助下渐渐恢复了些许意识，他感激地看着你，从怀中掏出一个玉简。",
            "choices": [
                _c("接受玉简", condition=_cond("comprehension", 6), rewards={"cultivation": 120, "reputation": 20}, flavor="玉简中记载着一段珍贵的修炼心得，你受益匪浅。修为 +120，声望 +20"),
                _c("接受玉简", rewards={"spirit_stones": 80, "reputation": 20}, flavor="玉简中是一张藏宝图，你按图索骥找到了一处灵石藏匿处。灵石 +80，声望 +20"),
                _c("婉拒，只是举手之劳", rewards={"fortune": 1, "reputation": 30}, flavor="修士感动不已，临别时说了一句：「此恩必报。」机缘 +1，声望 +30"),
            ]
        }),
        _c("搜刮他身上的财物后离去", condition=_cond("physique", 6), rewards={"spirit_stones": 100, "reputation": -30}, flavor="你搜刮了他的财物，但此事若传出去，名声必然受损。灵石 +100，声望 -30"),
        _c("搜刮他身上的财物后离去", rewards={"spirit_stones": 60, "lifespan": -5, "reputation": -30}, flavor="修士突然爆发，你受了伤才抢到些财物，声望大损。灵石 +60，寿元 -5，声望 -30"),
        _c("绕道而行，不想惹麻烦", rewards={}, flavor="你绕道离去，心中隐隐有些不安。"),
    ]
))

EVENTS.append(_e(
    "毒雾山谷",
    "山谷中弥漫着淡紫色的雾气，隐约有异香传来，令人心神迷醉，但经验告诉你这可能是毒雾。",
    [
        _c("捂住口鼻，强行穿越", next_event={
            "desc": "毒雾比你想象的更浓，你感到头晕目眩，但谷中隐约有什么东西在发光。",
            "choices": [
                _c("坚持走向光源", condition=_cond("physique", 7), rewards={"spirit_stones": 180, "lifespan": -5}, flavor="你强撑着找到了光源——一株极品灵草，代价是中了些毒。灵石 +180，寿元 -5"),
                _c("坚持走向光源", rewards={"lifespan": -15}, flavor="毒素侵入经脉，你拼命运功逼毒，元气大伤。寿元 -15"),
                _c("立刻退出山谷", rewards={"lifespan": -3}, flavor="你及时退出，只中了些轻毒，休息片刻便恢复了。寿元 -3"),
            ]
        }),
        _c("绕道而行", rewards={"lifespan": -1}, flavor="绕路耗费了不少时间，但安全无虞。寿元 -1"),
        _c("在谷口观察，寻找规律", condition=_cond("comprehension", 7), rewards={"spirit_stones": 150}, flavor="你发现毒雾有间歇性消散的规律，趁机进入采到了灵草。灵石 +150"),
        _c("在谷口观察，寻找规律", rewards={}, flavor="你观察了许久，没有发现什么规律，只好放弃。"),
    ]
))

EVENTS.append(_e(
    "对弈老者",
    "茶馆中，一位白发老者正在独自摆弄棋局，见你路过，抬头笑道：「小友，可愿与老夫对弈一局？」",
    [
        _c("欣然应战", next_event={
            "desc": "棋局进行到中盘，你发现老者棋力深不可测，但棋局中似乎隐藏着某种道理。",
            "choices": [
                _c("专注于棋局，用心感悟", condition=_cond("comprehension", 7), rewards={"comprehension": 1, "soul": 1}, flavor="你从棋局中悟出了一丝天地之道，受益匪浅。悟性 +1，神识 +1"),
                _c("专注于棋局，用心感悟", rewards={"comprehension": 1}, flavor="虽然输了棋，但你从中学到了不少。悟性 +1"),
                _c("故意输棋，观察老者反应", condition=_cond("fortune", 7), rewards={"fortune": 1, "spirit_stones": 50}, flavor="老者哈哈大笑，说你是个聪明人，临别赠你一个锦囊。机缘 +1，灵石 +50"),
                _c("故意输棋，观察老者反应", rewards={}, flavor="老者只是平静地收起棋子，什么都没说。"),
            ]
        }),
        _c("婉言拒绝，继续赶路", rewards={}, flavor="老者点点头，不再多言。"),
        _c("下注对弈，赌上灵石", condition=_cond("comprehension", 8), rewards={"spirit_stones": 100}, flavor="你棋高一筹，赢得了赌注。灵石 +100"),
        _c("下注对弈，赌上灵石", rewards={"spirit_stones": -60}, flavor="老者棋力远超你，你输得心服口服。灵石 -60"),
    ]
))

EVENTS.append(_e(
    "暴风雪",
    "天色骤变，一场突如其来的暴风雪席卷而来，前方道路已被大雪封堵，附近有一座破旧的木屋。",
    [
        _c("进入木屋避雪", next_event={
            "desc": "木屋内已有一人，是一位同样避雪的修士，他正在生火取暖，见你进来，点头示意。",
            "choices": [
                _c("友好交谈，互通有无", condition=_cond("fortune", 6), rewards={"spirit_stones": 60, "reputation": 15}, flavor="对方是一位经验丰富的散修，交流中你获益良多，临别还互赠了些灵石。灵石 +60，声望 +15"),
                _c("友好交谈，互通有无", rewards={"cultivation": 40}, flavor="两人交流修炼心得，各有收获。修为 +40"),
                _c("保持警惕，各自休息", rewards={"lifespan": 5}, flavor="你谨慎地休息了一夜，第二天雪停后继续赶路，精神恢复了些。寿元 +5"),
            ]
        }),
        _c("强行在风雪中赶路", condition=_cond("physique", 8), rewards={"physique": 1}, flavor="你凭借强健的体魄硬闯风雪，体魄得到了极大锻炼。体魄 +1"),
        _c("强行在风雪中赶路", rewards={"lifespan": -10, "bone": -1}, flavor="严寒侵入骨髓，你冻伤了根基，元气大伤。寿元 -10，根骨 -1"),
        _c("就地打坐，以内力抵御严寒", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 60}, flavor="你以内力抵御严寒，反而借此机会深入修炼，有所感悟。神识 +1，修为 +60"),
        _c("就地打坐，以内力抵御严寒", rewards={"lifespan": -5}, flavor="内力不足以完全抵御严寒，你还是受了些冻伤。寿元 -5"),
    ]
))

EVENTS.append(_e(
    "拍卖会",
    "途经一处城镇，恰逢一年一度的小型拍卖会，门口的告示上写着今日有一件来历不明的宝物拍卖。",
    [
        _c("进场参与竞拍", next_event={
            "desc": "拍卖台上摆着一个古朴的玉盒，主持人说里面是一件「机缘之物」，起拍价一百灵石。",
            "choices": [
                _c("出价一百灵石", condition=_cond("fortune", 7), rewards={"spirit_stones": -100, "fortune": 2, "bone": 1}, flavor="玉盒中是一枚天材地宝，对你的根骨和机缘都有极大裨益。灵石 -100，机缘 +2，根骨 +1"),
                _c("出价一百灵石", rewards={"spirit_stones": -100, "cultivation": 80}, flavor="玉盒中是一颗修炼丹药，服下后修为大进。灵石 -100，修为 +80"),
                _c("出价两百灵石，志在必得", condition=_cond("fortune", 8), rewards={"spirit_stones": -200, "fortune": 3}, flavor="你以高价拍得，玉盒中的宝物让你机缘大涨。灵石 -200，机缘 +3"),
                _c("出价两百灵石，志在必得", rewards={"spirit_stones": -200, "lifespan": 30}, flavor="宝物是一颗延寿丹，物有所值。灵石 -200，寿元 +30"),
                _c("放弃竞拍，观望", rewards={}, flavor="你没有出手，宝物被他人拍走。"),
            ]
        }),
        _c("在会场外打听消息", condition=_cond("fortune", 6), rewards={"spirit_stones": 80}, flavor="你从一位知情者口中得知了一个内幕消息，提前布局赚了一笔。灵石 +80"),
        _c("在会场外打听消息", rewards={}, flavor="你没打听到什么有用的消息。"),
        _c("直接离开", rewards={}, flavor="你对拍卖会不感兴趣，继续赶路。"),
    ]
))

EVENTS.append(_e(
    "渡口等船",
    "你来到一处渡口，船家说要等到明日才能开船，渡口旁有几位修士也在等候。",
    [
        _c("与等候的修士们交流", next_event={
            "desc": "其中一位修士主动搭话，自称是某宗门的外门弟子，正在外出历练，他提议大家互相切磋。",
            "choices": [
                _c("接受切磋", condition=_cond("physique", 7), rewards={"physique": 1, "reputation": 20}, flavor="你在切磋中胜出，赢得了众人的尊重。体魄 +1，声望 +20"),
                _c("接受切磋", rewards={"lifespan": -3, "cultivation": 50}, flavor="你虽然落败，但从对手的招式中学到了不少。寿元 -3，修为 +50"),
                _c("婉拒切磋，只是闲聊", condition=_cond("comprehension", 6), rewards={"comprehension": 1}, flavor="你从闲聊中获得了不少修炼感悟。悟性 +1"),
                _c("婉拒切磋，只是闲聊", rewards={"reputation": 10}, flavor="你结交了几位新朋友，声望略有提升。声望 +10"),
            ]
        }),
        _c("独自打坐修炼", condition=_cond("soul", 6), rewards={"cultivation": 70, "soul": 1}, flavor="你借此机会静心修炼，神识有所提升。修为 +70，神识 +1"),
        _c("独自打坐修炼", rewards={"cultivation": 40}, flavor="你静心修炼，有些收获。修为 +40"),
        _c("在渡口附近探索", condition=_cond("fortune", 6), rewards={"spirit_stones": 60}, flavor="你在河边发现了一些被水流冲来的灵材，换了些灵石。灵石 +60"),
        _c("在渡口附近探索", rewards={}, flavor="你在附近转了转，什么都没发现。"),
    ]
))

EVENTS.append(_e(
    "废弃矿洞",
    "山壁上有一处废弃的矿洞，洞口的木架已经腐朽，但洞内隐约有灵石的光泽。",
    [
        _c("进入矿洞挖掘", next_event={
            "desc": "你进入矿洞，发现里面比想象中深得多，深处的矿壁上确实有灵石矿脉，但洞顶不时有碎石落下。",
            "choices": [
                _c("快速挖掘，尽快离开", condition=_cond("physique", 6), rewards={"spirit_stones": 120}, flavor="你快速挖出了一批灵石，在洞顶塌陷前安全撤出。灵石 +120"),
                _c("快速挖掘，尽快离开", rewards={"spirit_stones": 60, "lifespan": -5}, flavor="你挖到了些灵石，但撤退时被落石砸中，受了些伤。灵石 +60，寿元 -5"),
                _c("仔细探查，寻找最佳矿脉", condition=_cond("comprehension", 7), rewards={"spirit_stones": 200}, flavor="你找到了一处品质极佳的灵石矿脉，收获颇丰。灵石 +200"),
                _c("仔细探查，寻找最佳矿脉", rewards={"spirit_stones": 40, "lifespan": -8}, flavor="你在矿洞中耗费太多时间，洞顶塌陷，你狼狈逃出。灵石 +40，寿元 -8"),
            ]
        }),
        _c("在洞口观察，不进入", condition=_cond("comprehension", 6), rewards={"spirit_stones": 50}, flavor="你在洞口发现了前人遗落的一个储物袋，里面有些灵石。灵石 +50"),
        _c("在洞口观察，不进入", rewards={}, flavor="你观察了一番，觉得风险太大，放弃了。"),
        _c("直接离开", rewards={}, flavor="你没有进入，继续赶路。"),
    ]
))

EVENTS.append(_e(
    "神秘符箓",
    "路边的树干上贴着一张泛黄的符箓，符文奇异，散发着微弱的灵光，不知是何人所留。",
    [
        _c("取下符箓研究", next_event={
            "desc": "符箓在你手中微微发热，符文开始流动，似乎在等待你做出选择。",
            "choices": [
                _c("将灵力注入符箓", condition=_cond("soul", 7), rewards={"soul": 1, "cultivation": 80}, flavor="符箓爆发出耀眼的光芒，你从中感悟到了一丝符道真意。神识 +1，修为 +80"),
                _c("将灵力注入符箓", rewards={"lifespan": -5}, flavor="符箓突然爆炸，你受了些轻伤。寿元 -5"),
                _c("将符箓收入储物袋", condition=_cond("fortune", 6), rewards={"spirit_stones": 100}, flavor="你将符箓带到城中，被一位符师高价收购。灵石 +100"),
                _c("将符箓收入储物袋", rewards={"spirit_stones": 30}, flavor="符箓品质一般，只卖了些普通价格。灵石 +30"),
            ]
        }),
        _c("不去理会，绕道而行", rewards={}, flavor="你绕道而行，符箓的灵光渐渐消失在视野中。"),
        _c("将符箓撕毁", condition=_cond("physique", 6), rewards={"physique": 1}, flavor="符箓爆发出一股冲击力，你硬抗了下来，体魄得到了锻炼。体魄 +1"),
        _c("将符箓撕毁", rewards={"lifespan": -3}, flavor="符箓爆炸，你受了些轻伤。寿元 -3"),
    ]
))

EVENTS.append(_e(
    "迷路孩童",
    "山道上，一个约莫七八岁的孩童独自坐在路边哭泣，说自己迷路了，找不到回家的路。",
    [
        _c("帮助孩童找到家人", next_event={
            "desc": "你带着孩童走了许久，终于找到了他的家。孩童的父母感激涕零，非要答谢你。",
            "choices": [
                _c("接受答谢", condition=_cond("fortune", 6), rewards={"spirit_stones": 80, "reputation": 20, "fortune": 1}, flavor="孩童父母拿出了家中珍藏的灵石和一件小法器答谢你。灵石 +80，声望 +20，机缘 +1"),
                _c("接受答谢", rewards={"spirit_stones": 40, "reputation": 20}, flavor="孩童父母拿出了些灵石答谢你。灵石 +40，声望 +20"),
                _c("婉拒答谢，举手之劳", rewards={"reputation": 40, "fortune": 1}, flavor="孩童父母感动不已，你的善举在附近传为美谈。声望 +40，机缘 +1"),
            ]
        }),
        _c("指引方向，让孩童自己回去", rewards={"reputation": 5}, flavor="你指了个大概方向，孩童道谢后跑去了。声望 +5"),
        _c("不理会，继续赶路", rewards={"fortune": -1}, flavor="你视而不见地走过，心中隐隐有些不安，似乎错过了什么。机缘 -1"),
    ]
))

EVENTS.append(_e(
    "古树异象",
    "山间有一棵参天古树，树龄不知几百年，树干上有一个奇异的树洞，洞内散发着淡淡的木灵气。",
    [
        _c("将手伸入树洞", next_event={
            "desc": "你的手触碰到了一个温润的物体，似乎是一颗果实，但同时你感到一股意识在审视着你。",
            "choices": [
                _c("取出果实", condition=_cond("fortune", 7), rewards={"lifespan": 25, "bone": 1}, flavor="是一颗千年灵果，服下后根骨得到了滋养。寿元 +25，根骨 +1"),
                _c("取出果实", rewards={"lifespan": 15}, flavor="是一颗普通的灵果，但也有些补益。寿元 +15"),
                _c("将果实放回，退手", rewards={"fortune": 1}, flavor="古树似乎对你的尊重表示认可，你感到运气好了些。机缘 +1"),
            ]
        }),
        _c("在古树下打坐冥想", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 60}, flavor="古树的木灵气辅助你修炼，你若有所悟。悟性 +1，修为 +60"),
        _c("在古树下打坐冥想", rewards={"cultivation": 30}, flavor="木灵气有些补益，修为略有提升。修为 +30"),
        _c("砍下一截树枝带走", condition=_cond("physique", 5), rewards={"spirit_stones": 70}, flavor="古树木质坚硬，是上好的炼器材料，卖了个好价钱。灵石 +70"),
        _c("砍下一截树枝带走", rewards={"lifespan": -5}, flavor="古树突然爆发出一股木灵气将你弹飞，你受了些轻伤。寿元 -5"),
    ]
))
