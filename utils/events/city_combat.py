from utils.events._base import _e, _c, _cond

EVENTS = []

EVENTS.append(_e(
    "铁甲城擂台",
    "铁甲城的中央擂台今日开擂，擂主是一名以体魄著称的武修，已经连胜十场，赏金丰厚。",
    [
        _c("上台挑战", next_event={
            "desc": "擂主身形魁梧，出手如雷，你需要找准他的破绽。",
            "choices": [
                _c("以速度游走，寻找破绽", condition=_cond("comprehension", 7), rewards={"spirit_stones": 150, "reputation": 50, "comprehension": 1}, flavor="你以精妙步法让擂主无从发力，最终一击制胜，赢得满堂喝彩。灵石 +150，声望 +50，悟性 +1"),
                _c("以速度游走，寻找破绽", rewards={"lifespan": -10, "reputation": 20}, flavor="你落败，但打出了风采，围观者给予掌声。寿元 -10，声望 +20"),
                _c("以力量正面硬撼", condition=_cond("physique", 8), rewards={"spirit_stones": 150, "reputation": 50, "physique": 1}, flavor="你以更强横的体魄压制了擂主，胜出。灵石 +150，声望 +50，体魄 +1"),
                _c("以力量正面硬撼", rewards={"lifespan": -15, "reputation": 15}, flavor="擂主体魄惊人，你被打得落败，受了不轻的伤。寿元 -15，声望 +15"),
            ]
        }),
        _c("在旁观战，感悟战意", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 70}, flavor="你从激烈的战斗中感悟到了一丝战意，悟性有所提升。悟性 +1，修为 +70"),
        _c("在旁观战，感悟战意", rewards={"cultivation": 40}, flavor="你观摩了一番，略有收获。修为 +40"),
        _c("下注押擂主赢", condition=_cond("fortune", 7), rewards={"spirit_stones": 80}, flavor="你押对了，赚了一笔。灵石 +80"),
        _c("下注押擂主赢", rewards={"spirit_stones": -30}, flavor="你押错了，输了一些灵石。灵石 -30"),
    ],
    city="铁甲城"
))

EVENTS.append(_e(
    "苍穹城雷劫观摩",
    "苍穹城外，一名修士正在渡雷劫，天空中雷云翻滚，紫色雷电不断轰落，围观者众多。",
    [
        _c("近距离感悟雷意", condition=_cond("soul", 7), rewards={"soul": 1, "comprehension": 1, "cultivation": 100}, flavor="你从雷劫中感悟到了一丝雷道真意，神识和悟性都有所提升。神识 +1，悟性 +1，修为 +100"),
        _c("近距离感悟雷意", rewards={"cultivation": 60, "lifespan": -5}, flavor="雷劫的余波波及了你，受了些轻伤，但也有所感悟。修为 +60，寿元 -5"),
        _c("协助渡劫者", next_event={
            "desc": "渡劫者感激地看了你一眼，你的协助让他渡劫成功，他走过来向你道谢。",
            "choices": [
                _c("请求他传授雷法", condition=_cond("comprehension", 7), rewards={"comprehension": 1, "cultivation": 120, "soul": 1}, flavor="渡劫者传授了你一些雷法心得，悟性和神识都大幅提升。悟性 +1，修为 +120，神识 +1"),
                _c("请求他传授雷法", rewards={"cultivation": 80, "reputation": 30}, flavor="渡劫者传授了你一些基础雷法，修为有所提升，声望也大涨。修为 +80，声望 +30"),
                _c("只是举手之劳，不求回报", rewards={"reputation": 40, "fortune": 1}, flavor="渡劫者感动不已，说日后必有回报，声望大涨，机缘也有所提升。声望 +40，机缘 +1"),
            ]
        }),
        _c("在远处观望，不靠近", rewards={"cultivation": 30}, flavor="你在远处观摩了一番，略有收获。修为 +30"),
    ],
    city="苍穹城"
))

EVENTS.append(_e(
    "寒冰城冰封试炼",
    "寒冰城有一处古老的冰封试炼场，据说在极寒之中修炼可以大幅提升体魄，但危险性极高。",
    [
        _c("进入试炼场", next_event={
            "desc": "试炼场内寒气刺骨，你感到体内灵气开始凝滞，但同时也感受到了一股奇异的淬炼之力。",
            "choices": [
                _c("坚持到底", condition=_cond("physique", 8), rewards={"physique": 2, "bone": 1, "lifespan": 30}, flavor="你以强横体魄撑过了极寒淬炼，体魄和根骨都得到了蜕变，寿元也有所增长。体魄 +2，根骨 +1，寿元 +30"),
                _c("坚持到底", condition=_cond("physique", 6), rewards={"physique": 1, "lifespan": 15}, flavor="你撑过了淬炼，体魄有所提升，寿元也略有增长。体魄 +1，寿元 +15"),
                _c("坚持到底", rewards={"lifespan": -20, "physique": 1}, flavor="极寒超出了你的承受极限，你受了重伤，但体魄也有所提升。寿元 -20，体魄 +1"),
                _c("中途退出", rewards={"cultivation": 50}, flavor="你在退出前吸收了一些寒气，修为略有提升。修为 +50"),
            ]
        }),
        _c("在试炼场外感应寒气", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 60}, flavor="你在外围感应寒气，神识有所提升，修为也略有增长。神识 +1，修为 +60"),
        _c("在试炼场外感应寒气", rewards={"cultivation": 30}, flavor="你感应了一番，略有收获。修为 +30"),
        _c("不感兴趣，离开", rewards={}, flavor="你继续赶路。"),
    ],
    city="寒冰城"
))

EVENTS.append(_e(
    "幽冥镇鬼修交流",
    "幽冥镇的阴气弥漫，一名鬼修主动上前，说他有一门阴属功法愿意交流，但需要你提供一些阳气作为代价。",
    [
        _c("接受交流", next_event={
            "desc": "鬼修将一枚玉简递给你，说里面记载着一门感应阴阳之道的功法。",
            "choices": [
                _c("研读玉简", condition=_cond("soul", 7), rewards={"soul": 2, "lifespan": -10, "cultivation": 150}, flavor="玉简中的功法深奥，你研读后神识大幅提升，但消耗了一些阳寿。神识 +2，寿元 -10，修为 +150"),
                _c("研读玉简", rewards={"soul": 1, "lifespan": -15, "cultivation": 80}, flavor="你勉强领悟了一些，神识略有提升，但消耗了不少阳寿。神识 +1，寿元 -15，修为 +80"),
                _c("拒绝研读，转卖玉简", condition=_cond("fortune", 6), rewards={"spirit_stones": 100}, flavor="你将玉简卖给了另一名修士，赚了一笔。灵石 +100"),
            ]
        }),
        _c("拒绝，不想与鬼修打交道", rewards={}, flavor="你拒绝了，继续赶路。"),
        _c("以神识感应鬼修", condition=_cond("soul", 8), rewards={"soul": 1, "fortune": 1}, flavor="你以神识感应鬼修，从中感悟到了一丝阴阳之道，神识和机缘都有所提升。神识 +1，机缘 +1"),
    ],
    city="幽冥镇"
))

EVENTS.append(_e(
    "雪狼城猎妖队",
    "雪狼城的猎妖队正在招募临时成员，说北域近日有一只雪狼妖兽出没，悬赏丰厚。",
    [
        _c("加入猎妖队", next_event={
            "desc": "队伍在雪原中追踪了半日，终于发现了雪狼的踪迹，它比预想的要强大得多。",
            "choices": [
                _c("正面迎战", condition=_cond("physique", 7), rewards={"spirit_stones": 120, "reputation": 40, "physique": 1}, flavor="你以强横体魄正面击败了雪狼，获得了丰厚赏金，声望大涨。灵石 +120，声望 +40，体魄 +1"),
                _c("正面迎战", rewards={"lifespan": -15, "spirit_stones": 50, "reputation": 20}, flavor="你受了伤，但也出了力，获得部分赏金。寿元 -15，灵石 +50，声望 +20"),
                _c("智取，引雪狼入陷阱", condition=_cond("comprehension", 7), rewards={"spirit_stones": 150, "reputation": 50, "comprehension": 1}, flavor="你设计了一个陷阱，成功捕获了雪狼，成为此次猎妖的最大功臣。灵石 +150，声望 +50，悟性 +1"),
                _c("智取，引雪狼入陷阱", rewards={"spirit_stones": 80, "reputation": 25}, flavor="陷阱奏效，你获得了不少赏金。灵石 +80，声望 +25"),
            ]
        }),
        _c("拒绝，太危险", rewards={}, flavor="你拒绝了，继续赶路。"),
        _c("打听雪狼妖丹的价值", condition=_cond("fortune", 6), rewards={"spirit_stones": 60}, flavor="你从打听中得知了妖丹的市价，提前布局赚了一笔。灵石 +60"),
    ],
    city="雪狼城"
))

EVENTS.append(_e(
    "玄冰谷探险",
    "玄冰谷入口处，一名受伤的修士正在休息，说他在谷内发现了一处宝地，但独自无法取出，愿意五五分成。",
    [
        _c("答应合作", next_event={
            "desc": "你们进入玄冰谷，寒气刺骨，但那名修士带你找到了一处冰封的宝物。",
            "choices": [
                _c("打破冰封取出宝物", condition=_cond("physique", 7), rewards={"spirit_stones": 150, "bone": 1, "lifespan": 20}, flavor="宝物是一块万年玄冰晶，你们平分后，你的那份价值连城，根骨也得到了滋养。灵石 +150，根骨 +1，寿元 +20"),
                _c("打破冰封取出宝物", rewards={"spirit_stones": 80, "lifespan": -10}, flavor="寒气反噬，你受了些轻伤，但也分到了一些宝物。灵石 +80，寿元 -10"),
                _c("独吞宝物，背刺同伴", condition=_cond("physique", 8), rewards={"spirit_stones": 250, "reputation": -60}, flavor="你独吞了宝物，但此举大损声望。灵石 +250，声望 -60"),
            ]
        }),
        _c("拒绝，可能是陷阱", rewards={"fortune": 1}, flavor="你拒绝了，机缘略有提升，说明你的直觉是对的。机缘 +1"),
        _c("以神识感应受伤修士", condition=_cond("soul", 7), rewards={"soul": 1}, flavor="你感应到了受伤修士的真实意图，神识有所提升，选择了离开。神识 +1"),
    ],
    city="玄冰谷"
))

EVENTS.append(_e(
    "铁甲城武道论坛",
    "铁甲城的武道论坛今日开讲，一名元婴期的武修正在传授战斗心得，座无虚席。",
    [
        _c("认真聆听", condition=_cond("comprehension", 7), rewards={"comprehension": 1, "physique": 1, "cultivation": 80}, flavor="你从武修的讲解中悟出了一丝战道真意，悟性和体魄都有所提升。悟性 +1，体魄 +1，修为 +80"),
        _c("认真聆听", rewards={"cultivation": 50, "physique": 1}, flavor="你学到了一些战斗技巧，体魄略有提升。体魄 +1，修为 +50"),
        _c("上台提问", next_event={
            "desc": "武修见你提问犀利，邀请你上台切磋，说若能接下他三招，便传授你一门秘法。",
            "choices": [
                _c("接受切磋", condition=_cond("physique", 8), rewards={"physique": 2, "bone": 1, "reputation": 50}, flavor="你接下了三招，武修赞叹不已，传授了你一门体魄秘法，声望大涨。体魄 +2，根骨 +1，声望 +50"),
                _c("接受切磋", rewards={"lifespan": -10, "reputation": 30, "physique": 1}, flavor="你没能接下三招，但打出了风采，声望有所提升。寿元 -10，声望 +30，体魄 +1"),
                _c("婉拒，只是来学习的", rewards={"reputation": 15}, flavor="武修点头，说谦逊也是一种修炼。声望 +15"),
            ]
        }),
        _c("不感兴趣，离开", rewards={}, flavor="你继续赶路。"),
    ],
    city="铁甲城"
))

EVENTS.append(_e(
    "烈风关守城战",
    "烈风关突然响起警报，一支妖兽群正在向城关冲来，守城修士紧急招募援手。",
    [
        _c("参与守城", next_event={
            "desc": "妖兽群数量庞大，但战斗力参差不齐，你需要找准位置发挥最大作用。",
            "choices": [
                _c("守卫城门正面", condition=_cond("physique", 7), rewards={"spirit_stones": 100, "reputation": 60, "physique": 1}, flavor="你在城门正面奋勇杀敌，击退了大量妖兽，获得了丰厚赏金，声望大涨。灵石 +100，声望 +60，体魄 +1"),
                _c("守卫城门正面", rewards={"lifespan": -15, "spirit_stones": 50, "reputation": 30}, flavor="你受了伤，但也出了力，获得部分赏金。寿元 -15，灵石 +50，声望 +30"),
                _c("支援侧翼薄弱处", condition=_cond("comprehension", 7), rewards={"spirit_stones": 120, "reputation": 70, "comprehension": 1}, flavor="你发现了侧翼的薄弱点并及时支援，成为此战关键，声望暴涨。灵石 +120，声望 +70，悟性 +1"),
                _c("支援侧翼薄弱处", rewards={"spirit_stones": 70, "reputation": 40}, flavor="你的支援起到了作用，获得了赏金和声望。灵石 +70，声望 +40"),
            ]
        }),
        _c("趁乱收集妖兽材料", condition=_cond("fortune", 7), rewards={"spirit_stones": 100}, flavor="你趁乱收集了大量妖兽材料，价值不菲。灵石 +100"),
        _c("趁乱收集妖兽材料", rewards={"spirit_stones": 40, "lifespan": -5}, flavor="你收集了一些材料，但也被妖兽波及，受了轻伤。灵石 +40，寿元 -5"),
        _c("撤离，不参与", rewards={}, flavor="你选择撤离，继续赶路。"),
    ],
    city="烈风关"
))

EVENTS.append(_e(
    "御剑城无主飞剑",
    "御剑城城头悬挂着一柄传说中的无主飞剑，据说每隔百年会认主一次，今日恰好是百年之期。",
    [
        _c("尝试与飞剑感应", next_event={
            "desc": "飞剑散发出一道剑光，似乎在考验你的剑道悟性。",
            "choices": [
                _c("以剑意回应", condition=_cond("comprehension", 9), rewards={"comprehension": 2, "soul": 1, "cultivation": 300, "bone": 1}, flavor="飞剑认主，剑意涌入你的意识，悟性和神识都大幅提升，修为暴涨，根骨也得到了蜕变。悟性 +2，神识 +1，修为 +300，根骨 +1"),
                _c("以剑意回应", condition=_cond("comprehension", 7), rewards={"comprehension": 1, "cultivation": 150}, flavor="飞剑散出一缕剑气滋养了你，悟性有所提升，修为大进。悟性 +1，修为 +150"),
                _c("以剑意回应", rewards={"cultivation": 80}, flavor="飞剑没有认主，但散出的剑气让你修为略有提升。修为 +80"),
            ]
        }),
        _c("在旁观看，感悟剑意", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 60}, flavor="你从飞剑散发的剑意中感悟到了一丝剑道，悟性有所提升。悟性 +1，修为 +60"),
        _c("在旁观看，感悟剑意", rewards={"cultivation": 30}, flavor="你感应了一番，略有收获。修为 +30"),
        _c("不感兴趣，离开", rewards={}, flavor="你继续赶路。"),
    ],
    city="御剑城"
))

EVENTS.append(_e(
    "凌霄城云端修炼",
    "凌霄城建于云端，灵气极为纯粹，城中有一处专供修士修炼的云台，据说在此修炼效率是地面的三倍。",
    [
        _c("在云台修炼", condition=_cond("comprehension", 7), rewards={"cultivation": 200, "comprehension": 1, "lifespan": 20}, flavor="云台灵气纯粹，你在此修炼，修为暴涨，悟性有所提升，寿元也得到了滋养。修为 +200，悟性 +1，寿元 +20"),
        _c("在云台修炼", rewards={"cultivation": 130, "lifespan": 10}, flavor="云台灵气辅助修炼，收获颇丰。修为 +130，寿元 +10"),
        _c("感应云端天道", condition=_cond("soul", 7), rewards={"soul": 1, "comprehension": 1, "cultivation": 100}, flavor="你在云端感应天道，神识和悟性都有所提升，修为也大进。神识 +1，悟性 +1，修为 +100"),
        _c("感应云端天道", rewards={"soul": 1, "cultivation": 60}, flavor="你感应了一番，神识略有提升。神识 +1，修为 +60"),
        _c("欣赏云端风景，放松心神", rewards={"cultivation": 40, "lifespan": 5}, flavor="云端风景令人心旷神怡，你放松心神后修炼效率有所提升。修为 +40，寿元 +5"),
    ],
    city="凌霄城"
))
