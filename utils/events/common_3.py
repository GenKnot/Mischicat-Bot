from utils.events._base import _e, _c, _cond

EVENTS = []

EVENTS.append(_e(
    "法宝争夺",
    "前方传来激烈的打斗声，两名修士正在争夺一件散发着金光的法宝，双方都已精疲力竭。",
    [
        _c("趁乱出手，抢夺法宝", next_event={
            "desc": "你突然出手，两名修士都被打了个措手不及，法宝落入你手中，但两人随即将怒火转向了你。",
            "choices": [
                _c("迅速逃离", condition=_cond("physique", 7), rewards={"spirit_stones": 150, "reputation": -20}, flavor="你凭借速度甩开了两人，法宝到手，但名声受损。灵石 +150，声望 -20"),
                _c("迅速逃离", rewards={"lifespan": -12, "reputation": -20}, flavor="你没能逃脱，被两人联手痛打，法宝也丢了。寿元 -12，声望 -20"),
                _c("以法宝为筹码谈判", condition=_cond("comprehension", 7), rewards={"spirit_stones": 100, "reputation": -10}, flavor="你凭借口才从两人手中各要了些好处，三方各退一步。灵石 +100，声望 -10"),
            ]
        }),
        _c("在旁观看，等分出胜负", condition=_cond("fortune", 7), rewards={"spirit_stones": 80}, flavor="胜者精疲力竭，你趁机捡走了战场上散落的灵石和法器碎片。灵石 +80"),
        _c("在旁观看，等分出胜负", rewards={"cultivation": 40}, flavor="你从旁观战中学到了些战斗技巧。修为 +40"),
        _c("上前劝架，平息纷争", condition=_cond("reputation", 30), rewards={"reputation": 30, "fortune": 1}, flavor="你的声望让两人都给了几分面子，纷争平息，双方各自感谢了你。声望 +30，机缘 +1"),
        _c("上前劝架，平息纷争", rewards={"lifespan": -5}, flavor="两人不买账，你反而被波及受了些伤。寿元 -5"),
    ]
))

EVENTS.append(_e(
    "算命摊",
    "路边有一个算命摊，摊主是一位蒙着面纱的神秘女子，她抬头看了你一眼，说：「你今日必有一劫。」",
    [
        _c("付钱请她细说", next_event={
            "desc": "女子掐指一算，说：「你今日若向东行，必遇凶险；若向西行，或有奇遇。」",
            "choices": [
                _c("向西行", condition=_cond("fortune", 6), rewards={"fortune": 1, "spirit_stones": 100}, flavor="你向西行，果然遇到了一处无人知晓的灵石矿脉。机缘 +1，灵石 +100"),
                _c("向西行", rewards={"spirit_stones": 30}, flavor="你向西行，只找到了些普通灵石。灵石 +30"),
                _c("向东行，不信邪", condition=_cond("physique", 7), rewards={"physique": 1}, flavor="你遇到了一只妖兽，但将其击败，体魄得到了锻炼。体魄 +1"),
                _c("向东行，不信邪", rewards={"lifespan": -8}, flavor="你遇到了一只强大的妖兽，狼狈逃脱，受伤不轻。寿元 -8"),
            ]
        }),
        _c("不理会，继续赶路", condition=_cond("fortune", 5), rewards={}, flavor="你没有理会，平安无事地继续赶路。"),
        _c("不理会，继续赶路", rewards={"lifespan": -3}, flavor="你没有理会，果然遭遇了些小麻烦。寿元 -3"),
        _c("嘲笑她是骗子", rewards={"fortune": -1}, flavor="女子淡淡一笑，你总觉得今日运气差了些。机缘 -1"),
    ]
))

EVENTS.append(_e(
    "破庙古镜",
    "破庙正殿中央，一面古朴的铜镜静静矗立，镜面尘封已久，但隐约能看到镜中有影像流动。",
    [
        _c("擦拭铜镜，照出自身", next_event={
            "desc": "镜中出现了你的影像，但随即出现了另一个画面——是你未来的某个场景，模糊难辨。",
            "choices": [
                _c("凝神细看，试图看清", condition=_cond("soul", 7), rewards={"soul": 1, "fortune": 1}, flavor="你从模糊的画面中捕捉到了一丝天机，神识和机缘都有所提升。神识 +1，机缘 +1"),
                _c("凝神细看，试图看清", rewards={"soul": 1}, flavor="你看到了些模糊的画面，神识略有提升。神识 +1"),
                _c("立刻移开视线", rewards={"fortune": 1}, flavor="你及时移开视线，感觉躲过了什么，机缘好了些。机缘 +1"),
            ]
        }),
        _c("将铜镜带走", condition=_cond("fortune", 7), rewards={"spirit_stones": 200}, flavor="你将铜镜带到城中，被一位识货的修士高价收购。灵石 +200"),
        _c("将铜镜带走", rewards={"spirit_stones": 50, "lifespan": -3}, flavor="铜镜沉重，搬运途中你受了些损耗，卖价也一般。灵石 +50，寿元 -3"),
        _c("不去理会，离开破庙", rewards={}, flavor="你没有理会铜镜，转身离去。"),
    ]
))

EVENTS.append(_e(
    "灵兽蛋",
    "林间草丛中，你发现了一个散发着淡淡灵光的蛋，约有拳头大小，温热异常，显然是某种灵兽的蛋。",
    [
        _c("将蛋带走", next_event={
            "desc": "你将蛋放入储物袋，走了没多远，感到蛋在微微颤动，似乎快要孵化了。",
            "choices": [
                _c("停下来等待孵化", condition=_cond("fortune", 7), rewards={"fortune": 2, "spirit_stones": 50}, flavor="蛋孵化出一只罕见的灵兽幼崽，与你亲昵异常，机缘大涨。机缘 +2，灵石 +50"),
                _c("停下来等待孵化", rewards={"spirit_stones": 80}, flavor="孵化出一只普通灵兽，你将其卖给了灵兽商人。灵石 +80"),
                _c("将蛋卖给路过的商人", rewards={"spirit_stones": 100}, flavor="商人出了个不错的价格，你欣然成交。灵石 +100"),
            ]
        }),
        _c("将蛋放回原处", rewards={"fortune": 1}, flavor="你将蛋轻轻放回草丛，感觉做了件好事，机缘好了些。机缘 +1"),
        _c("直接离开，不去理会", rewards={}, flavor="你没有理会，继续赶路。"),
    ]
))

EVENTS.append(_e(
    "野果误食",
    "赶路途中腹中饥饿，路边有一丛结满果实的灌木，果实色泽鲜艳，香气扑鼻，但你不确定是否有毒。",
    [
        _c("直接摘来吃", condition=_cond("physique", 7), rewards={"lifespan": 5}, flavor="你体魄强健，轻松化解了果实中的微毒，反而吸收了其中的灵气。寿元 +5"),
        _c("直接摘来吃", rewards={"lifespan": -6, "physique": -1}, flavor="果实有毒，你上吐下泻，虚弱了好几天，根基受损。寿元 -6，体魄 -1"),
        _c("仔细辨别后再决定", condition=_cond("comprehension", 6), rewards={"lifespan": 8}, flavor="你辨别出这是一种罕见的灵果，服下后颇有补益。寿元 +8"),
        _c("仔细辨别后再决定", rewards={}, flavor="你辨别不出，为了安全起见放弃了。"),
        _c("不吃，继续赶路", rewards={}, flavor="你忍着饥饿继续赶路，安全无虞。"),
    ]
))

EVENTS.append(_e(
    "山顶日出",
    "你登上一座山峰，恰逢日出，金色的阳光洒满大地，天地间灵气随之涌动，这一刻仿佛天地都在呼吸。",
    [
        _c("静心感悟，与天地共鸣", condition=_cond("comprehension", 7), rewards={"comprehension": 1, "cultivation": 80}, flavor="你从日出中感悟到了一丝天地之道，悟性和修为都有所提升。悟性 +1，修为 +80"),
        _c("静心感悟，与天地共鸣", rewards={"cultivation": 50}, flavor="你感受到了天地灵气的涌动，修为有所提升。修为 +50"),
        _c("运功修炼，借助灵气", condition=_cond("soul", 6), rewards={"soul": 1, "lifespan": 10}, flavor="你借助日出时的灵气涌动修炼，神识和寿元都有所恢复。神识 +1，寿元 +10"),
        _c("运功修炼，借助灵气", rewards={"cultivation": 40}, flavor="你借助灵气修炼，有些收获。修为 +40"),
        _c("欣赏风景，放松心情", rewards={"fortune": 1}, flavor="你难得地放松了心情，感觉今日运气会不错。机缘 +1"),
    ]
))

EVENTS.append(_e(
    "夜宿荒野",
    "天色已晚，附近没有城镇，你只能在荒野中露宿，四周虫鸣鸟叫，偶尔传来远处妖兽的嚎叫。",
    [
        _c("布置简单的防御阵法", next_event={
            "desc": "夜半时分，你感到有什么东西在阵法外徘徊，似乎在试探。",
            "choices": [
                _c("保持警惕，静待天明", condition=_cond("soul", 6), rewards={"soul": 1}, flavor="你在警戒中度过了一夜，神识得到了锻炼。神识 +1"),
                _c("保持警惕，静待天明", rewards={"lifespan": -2}, flavor="你一夜未眠，精神疲惫，略有损耗。寿元 -2"),
                _c("主动出击，驱逐来者", condition=_cond("physique", 7), rewards={"physique": 1, "spirit_stones": 40}, flavor="你击退了一只妖兽，取其妖丹换了些灵石。体魄 +1，灵石 +40"),
                _c("主动出击，驱逐来者", rewards={"lifespan": -6}, flavor="妖兽比你想象的强，你受伤后才将其驱走。寿元 -6"),
            ]
        }),
        _c("找一处隐蔽的地方休息", condition=_cond("fortune", 6), rewards={"lifespan": 5, "fortune": 1}, flavor="你找到了一处极为隐蔽的山洞，安然度过了一夜，还发现了前人留下的一些物资。寿元 +5，机缘 +1"),
        _c("找一处隐蔽的地方休息", rewards={"lifespan": 3}, flavor="你找到了一处还算安全的地方，休息了一夜。寿元 +3"),
        _c("彻夜修炼，不去睡觉", condition=_cond("comprehension", 6), rewards={"cultivation": 60}, flavor="夜间灵气充沛，你借机修炼，收获颇丰。修为 +60"),
        _c("彻夜修炼，不去睡觉", rewards={"lifespan": -3, "cultivation": 30}, flavor="你修炼了一夜，但精力消耗过大。寿元 -3，修为 +30"),
    ]
))

EVENTS.append(_e(
    "神秘商队",
    "一支神秘的商队从你身旁经过，领队是一位气质不凡的中年人，他的马车上装满了用黑布遮盖的货物。",
    [
        _c("上前搭话，询问货物", next_event={
            "desc": "领队打量了你一眼，说：「我们贩卖的是各地的奇珍异宝，你若有兴趣，可以看看。」他掀开一角黑布，里面是各种灵材。",
            "choices": [
                _c("购买一件灵材（100灵石）", condition=_cond("fortune", 7), rewards={"spirit_stones": -100, "bone": 1, "comprehension": 1}, flavor="你买到了一件极品灵材，对根骨和悟性都有极大裨益。灵石 -100，根骨 +1，悟性 +1"),
                _c("购买一件灵材（100灵石）", rewards={"spirit_stones": -100, "cultivation": 100}, flavor="你买到了一颗修炼丹药，修为大进。灵石 -100，修为 +100"),
                _c("讨价还价", condition=_cond("comprehension", 6), rewards={"spirit_stones": -60, "lifespan": 20}, flavor="你以六十灵石买到了一颗延寿丹，物超所值。灵石 -60，寿元 +20"),
                _c("讨价还价", rewards={}, flavor="领队不为所动，你只好作罢。"),
                _c("不感兴趣，离开", rewards={}, flavor="你婉拒了领队，继续赶路。"),
            ]
        }),
        _c("跟随商队同行一段", condition=_cond("fortune", 6), rewards={"fortune": 1, "spirit_stones": 50}, flavor="同行途中，你从商队成员口中得知了一些有价值的消息，还顺手做了笔小生意。机缘 +1，灵石 +50"),
        _c("跟随商队同行一段", rewards={"reputation": 10}, flavor="同行途中，你结交了几位新朋友。声望 +10"),
        _c("不理会，继续赶路", rewards={}, flavor="你没有理会商队，继续赶路。"),
    ]
))

EVENTS.append(_e(
    "江湖恩怨",
    "前方两名修士剑拔弩张，其中一人突然转向你，说：「你可是见过一名身穿青衫的修士从此路过？」",
    [
        _c("如实回答", next_event={
            "desc": "你如实告知，那人点头道谢，随即追了上去。另一人却拦住你，说那人是他的仇家，请你帮忙拦截。",
            "choices": [
                _c("拒绝，不想卷入恩怨", rewards={"reputation": 5}, flavor="你婉拒了，两人各自离去，你落得清净。声望 +5"),
                _c("帮助拦截，收取报酬", condition=_cond("physique", 7), rewards={"spirit_stones": 80, "reputation": -10}, flavor="你帮忙拦截，收了报酬，但此事传出后名声略有影响。灵石 +80，声望 -10"),
                _c("帮助拦截，收取报酬", rewards={"lifespan": -8, "reputation": -10}, flavor="对方比你想象的强，你受了伤，报酬也没拿到。寿元 -8，声望 -10"),
            ]
        }),
        _c("说没见过，不想惹麻烦", rewards={}, flavor="你撒了个谎，两人失望离去，你继续赶路。"),
        _c("调解双方矛盾", condition=_cond("reputation", 20), rewards={"reputation": 25, "fortune": 1}, flavor="你凭借声望和口才化解了这场恩怨，双方各退一步，对你颇为感激。声望 +25，机缘 +1"),
        _c("调解双方矛盾", rewards={"lifespan": -4}, flavor="你好心调解，却被双方迁怒，受了些皮外伤。寿元 -4"),
    ]
))

EVENTS.append(_e(
    "枯骨遗物",
    "荒野中，你发现了一堆枯骨，旁边散落着一个破旧的储物袋，骨架旁插着一把锈迹斑斑的长剑。",
    [
        _c("检查储物袋", next_event={
            "desc": "储物袋内有些灵石和一封未完成的书信，信中写着一处秘地的位置，字迹已经模糊。",
            "choices": [
                _c("按照信中线索寻找秘地", condition=_cond("fortune", 7), rewards={"spirit_stones": 160, "fortune": 1}, flavor="你找到了信中所指的秘地，收获了一批前人遗留的灵石和灵材。灵石 +160，机缘 +1"),
                _c("按照信中线索寻找秘地", rewards={"lifespan": -3, "spirit_stones": 40}, flavor="你找到了秘地，但里面已被人捷足先登，只剩些残余。寿元 -3，灵石 +40"),
                _c("只取灵石，放弃线索", rewards={"spirit_stones": 60}, flavor="你取走了储物袋中的灵石，继续赶路。灵石 +60"),
            ]
        }),
        _c("拔出长剑查看", condition=_cond("physique", 6), rewards={"spirit_stones": 80}, flavor="长剑虽然锈迹斑斑，但剑身材质不凡，卖给铸剑师换了不少灵石。灵石 +80"),
        _c("拔出长剑查看", rewards={"lifespan": -2}, flavor="长剑上有残余的煞气，你受了些影响，精神略感不适。寿元 -2"),
        _c("为枯骨立碑，超度亡魂", rewards={"fortune": 1, "reputation": 10}, flavor="你为无名枯骨立了一块简陋的石碑，心中莫名感到一丝宽慰。机缘 +1，声望 +10"),
        _c("绕道而行，不去理会", rewards={}, flavor="你绕开枯骨，继续赶路。"),
    ]
))
