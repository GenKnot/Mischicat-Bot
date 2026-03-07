from utils.events._base import _e, _c, _cond

EVENTS = []

EVENTS.append(_e(
    "天京城宗门招募",
    "天京城的广场上，几大顶级宗门的弟子正在摆摊招募新人，人群熙攘，气氛热烈。",
    [
        _c("上前了解各宗门", next_event={
            "desc": "各宗门弟子纷纷介绍自家宗门的优势，你感到有些心动。",
            "choices": [
                _c("表达加入意向", condition=_cond("fortune", 7), rewards={"fortune": 1, "reputation": 30, "cultivation": 80}, flavor="宗门弟子对你印象不错，给了你一枚引荐玉符，机缘和声望都有所提升。机缘 +1，声望 +30，修为 +80"),
                _c("表达加入意向", rewards={"reputation": 20, "cultivation": 50}, flavor="宗门弟子给了你一些基础修炼资料，声望略有提升。声望 +20，修为 +50"),
                _c("只是打听，不表态", condition=_cond("soul", 6), rewards={"soul": 1, "fortune": 1}, flavor="你从各宗门弟子的介绍中感悟到了一些修炼之道，神识和机缘都有所提升。神识 +1，机缘 +1"),
                _c("只是打听，不表态", rewards={"cultivation": 40}, flavor="你了解了一些宗门情况，修为略有提升。修为 +40"),
            ]
        }),
        _c("不感兴趣，继续赶路", rewards={}, flavor="你继续赶路。"),
        _c("在人群中打探消息", condition=_cond("fortune", 6), rewards={"spirit_stones": 60, "fortune": 1}, flavor="你从人群中打探到了一条有价值的消息，机缘略有提升。灵石 +60，机缘 +1"),
    ],
    city="天京城"
))

EVENTS.append(_e(
    "灵虚城议事",
    "灵虚城的议事厅外，各大势力的代表正在进出，一名散修悄悄告诉你，今日议事的内容关系到整个修仙界的格局。",
    [
        _c("想办法打探消息", next_event={
            "desc": "你通过各种渠道打探到了一些内幕：各大宗门正在争夺一处新发现的灵脉。",
            "choices": [
                _c("将消息卖给出价最高的人", condition=_cond("fortune", 7), rewards={"spirit_stones": 200, "fortune": 1}, flavor="你将消息卖给了一名神秘买家，获得了丰厚报酬，机缘也有所提升。灵石 +200，机缘 +1"),
                _c("将消息卖给出价最高的人", rewards={"spirit_stones": 100}, flavor="你卖出了消息，获得了一些报酬。灵石 +100"),
                _c("自己去灵脉处抢先布局", condition=_cond("fortune", 8), rewards={"fortune": 2, "spirit_stones": 150, "cultivation": 100}, flavor="你抢先赶到灵脉处，占据了有利位置，机缘大涨，收获颇丰。机缘 +2，灵石 +150，修为 +100"),
                _c("自己去灵脉处抢先布局", rewards={"lifespan": -10, "spirit_stones": 50}, flavor="你赶到时已有人捷足先登，与人争抢中受了轻伤，但也有些收获。寿元 -10，灵石 +50"),
            ]
        }),
        _c("不去掺和，继续赶路", rewards={"fortune": 1}, flavor="你感到此事水深，选择不去掺和，机缘略有提升。机缘 +1"),
        _c("在议事厅外感应各方气息", condition=_cond("soul", 7), rewards={"soul": 1, "comprehension": 1}, flavor="你感应到了各大势力高手的气息，神识和悟性都有所提升。神识 +1，悟性 +1"),
    ],
    city="灵虚城"
))

EVENTS.append(_e(
    "清虚城古道观",
    "清虚城内有一座传承千年的古道观，观内的老道长正在为有缘人讲道，据说每次讲道都有不同的感悟。",
    [
        _c("进入道观聆听", next_event={
            "desc": "老道长的讲道深入浅出，你感到天地间的法则在你眼前变得清晰了许多。",
            "choices": [
                _c("专注感悟道法", condition=_cond("comprehension", 8), rewards={"comprehension": 2, "soul": 1, "cultivation": 150, "lifespan": 30}, flavor="你从老道长的讲道中悟出了一丝大道真意，悟性和神识都大幅提升，修为暴涨，寿元也得到了滋养。悟性 +2，神识 +1，修为 +150，寿元 +30"),
                _c("专注感悟道法", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 100, "lifespan": 20}, flavor="你从讲道中有所感悟，悟性有所提升，修为大进，寿元也略有增长。悟性 +1，修为 +100，寿元 +20"),
                _c("专注感悟道法", rewards={"cultivation": 60, "lifespan": 10}, flavor="你听了一些，略有收获。修为 +60，寿元 +10"),
                _c("向老道长请教延寿之法", condition=_cond("soul", 7), rewards={"soul": 1, "lifespan": 50}, flavor="老道长传授了你一门延寿心法，神识有所提升，寿元大涨。神识 +1，寿元 +50"),
                _c("向老道长请教延寿之法", rewards={"lifespan": 25}, flavor="老道长传授了你一些延寿方法，寿元有所增长。寿元 +25"),
            ]
        }),
        _c("在道观外感应道气", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 50}, flavor="你感应到了道观内散发的道气，神识略有提升。神识 +1，修为 +50"),
        _c("不感兴趣，离开", rewards={}, flavor="你继续赶路。"),
    ],
    city="清虚城"
))

EVENTS.append(_e(
    "望月楼占卜",
    "望月楼以占卜问道闻名，楼内的占卜师据说能窥见天机，但每次占卜都需要消耗一定的寿元。",
    [
        _c("花费寿元占卜", next_event={
            "desc": "占卜师掐指一算，神色凝重地说：「你近日有一劫，但劫中有机，关键在于你的选择。」",
            "choices": [
                _c("请他详细指点", condition=_cond("fortune", 7), rewards={"lifespan": -10, "fortune": 2, "cultivation": 100}, flavor="占卜师详细指点了你如何化劫为机，机缘大涨，修为也有所提升。寿元 -10，机缘 +2，修为 +100"),
                _c("请他详细指点", rewards={"lifespan": -10, "fortune": 1, "cultivation": 60}, flavor="占卜师给了你一些指点，机缘略有提升。寿元 -10，机缘 +1，修为 +60"),
                _c("谢过，自行应对", rewards={"lifespan": -10, "fortune": 1}, flavor="你谢过占卜师，心中有了准备，机缘略有提升。寿元 -10，机缘 +1"),
            ]
        }),
        _c("不花寿元，只是参观", condition=_cond("soul", 7), rewards={"soul": 1, "fortune": 1}, flavor="你以神识感应望月楼的天机气息，神识和机缘都有所提升。神识 +1，机缘 +1"),
        _c("不花寿元，只是参观", rewards={"cultivation": 30}, flavor="你参观了一番，略有收获。修为 +30"),
        _c("不感兴趣，离开", rewards={}, flavor="你继续赶路。"),
    ],
    city="望月楼"
))

EVENTS.append(_e(
    "问道城修仙大会",
    "问道城一年一度的修仙大会正在举行，各路散修聚集论道，气氛热烈，偶有高手现身。",
    [
        _c("参与论道", next_event={
            "desc": "论道台上，一名修士正在阐述自己对天地法则的理解，引发了众多修士的讨论。",
            "choices": [
                _c("上台发表见解", condition=_cond("comprehension", 7), rewards={"comprehension": 1, "reputation": 50, "cultivation": 100}, flavor="你的见解独到，引发了众多修士的共鸣，声望大涨，悟性也有所提升。悟性 +1，声望 +50，修为 +100"),
                _c("上台发表见解", rewards={"reputation": 25, "cultivation": 60}, flavor="你发表了一些见解，声望略有提升。声望 +25，修为 +60"),
                _c("在台下聆听感悟", condition=_cond("soul", 6), rewards={"soul": 1, "comprehension": 1, "cultivation": 80}, flavor="你从众多修士的论道中感悟到了一丝天地法则，神识和悟性都有所提升。神识 +1，悟性 +1，修为 +80"),
                _c("在台下聆听感悟", rewards={"cultivation": 50}, flavor="你聆听了一番，修为略有提升。修为 +50"),
            ]
        }),
        _c("结交各路散修", condition=_cond("fortune", 6), rewards={"fortune": 1, "reputation": 30}, flavor="你结交了几位志同道合的散修，机缘和声望都有所提升。机缘 +1，声望 +30"),
        _c("结交各路散修", rewards={"reputation": 20}, flavor="你结交了一些新朋友，声望略有提升。声望 +20"),
        _c("不感兴趣，离开", rewards={}, flavor="你继续赶路。"),
    ],
    city="问道城"
))

EVENTS.append(_e(
    "紫霄城灵气修炼",
    "紫霄城灵气为中州之最，城中有一处公共修炼广场，修士们在此修炼效率极高，但需要缴纳一定的灵石。",
    [
        _c("缴纳灵石入场修炼", next_event={
            "desc": "广场内灵气浓郁，你感到修炼速度比平时快了数倍，但时间有限，需要选择修炼方向。",
            "choices": [
                _c("专注提升修为", condition=_cond("comprehension", 7), rewards={"spirit_stones": -50, "cultivation": 200, "comprehension": 1}, flavor="你在浓郁灵气中专注修炼，修为暴涨，还悟出了一丝天地之道。灵石 -50，修为 +200，悟性 +1"),
                _c("专注提升修为", rewards={"spirit_stones": -50, "cultivation": 150}, flavor="你在浓郁灵气中修炼，修为大进。灵石 -50，修为 +150"),
                _c("专注淬炼体魄", condition=_cond("physique", 6), rewards={"spirit_stones": -50, "physique": 1, "bone": 1, "lifespan": 20}, flavor="你以浓郁灵气淬炼体魄，体魄和根骨都有所提升，寿元也略有增长。灵石 -50，体魄 +1，根骨 +1，寿元 +20"),
                _c("专注淬炼体魄", rewards={"spirit_stones": -50, "physique": 1, "lifespan": 10}, flavor="你淬炼了体魄，略有提升。灵石 -50，体魄 +1，寿元 +10"),
            ]
        }),
        _c("在广场外蹭灵气修炼", condition=_cond("comprehension", 6), rewards={"cultivation": 80}, flavor="你在广场外感应溢出的灵气，修为有所提升。修为 +80"),
        _c("在广场外蹭灵气修炼", rewards={"cultivation": 40}, flavor="你蹭了一些灵气，略有收获。修为 +40"),
        _c("不感兴趣，离开", rewards={}, flavor="你继续赶路。"),
    ],
    city="紫霄城"
))

EVENTS.append(_e(
    "太虚城地脉感应",
    "太虚城建于上古大能的洞府之上，地脉灵气源源不断，城中某处地面偶尔会涌出一股奇异的地脉之气。",
    [
        _c("就地感应地脉之气", condition=_cond("soul", 7), rewards={"soul": 1, "comprehension": 1, "cultivation": 120, "lifespan": 20}, flavor="你感应到了地脉深处的上古大能遗留的一丝意志，神识和悟性都有所提升，修为大进，寿元也得到了滋养。神识 +1，悟性 +1，修为 +120，寿元 +20"),
        _c("就地感应地脉之气", rewards={"cultivation": 80, "lifespan": 10}, flavor="地脉之气滋养，修为和寿元都有所提升。修为 +80，寿元 +10"),
        _c("寻找地脉涌出的源头", condition=_cond("fortune", 7), rewards={"fortune": 1, "spirit_stones": 100, "bone": 1}, flavor="你找到了地脉涌出的源头，发现了一块凝聚了地脉精华的灵晶，机缘和根骨都有所提升。机缘 +1，灵石 +100，根骨 +1"),
        _c("寻找地脉涌出的源头", rewards={"spirit_stones": 60, "cultivation": 50}, flavor="你找到了一些地脉散落的灵石，略有收获。灵石 +60，修为 +50"),
        _c("不去理会，继续赶路", rewards={}, flavor="你继续赶路。"),
    ],
    city="太虚城"
))

EVENTS.append(_e(
    "炎阳城炼丹传承",
    "炎阳城有一门古老的炼丹传承，城中的炼丹师公会今日开放参观，并提供免费的炼丹体验课。",
    [
        _c("参加体验课", next_event={
            "desc": "炼丹师为你讲解了基础炼丹之道，并让你亲手尝试炼制一枚简单的丹药。",
            "choices": [
                _c("认真炼制", condition=_cond("comprehension", 7), rewards={"comprehension": 1, "lifespan": 30, "cultivation": 80}, flavor="你成功炼制出了一枚品质不错的丹药，服下后寿元和修为都有所提升，悟性也大进。悟性 +1，寿元 +30，修为 +80"),
                _c("认真炼制", rewards={"lifespan": 15, "cultivation": 50}, flavor="你炼制出了一枚普通丹药，略有补益。寿元 +15，修为 +50"),
                _c("炼制失败，但有所感悟", condition=_cond("soul", 6), rewards={"soul": 1, "comprehension": 1}, flavor="你炼制失败，但从失败中悟出了一丝炼丹之道，神识和悟性都有所提升。神识 +1，悟性 +1"),
                _c("炼制失败，但有所感悟", rewards={"cultivation": 30}, flavor="你炼制失败，但略有收获。修为 +30"),
            ]
        }),
        _c("只是参观，不参与", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 50}, flavor="你从参观中感悟到了一丝丹道，悟性有所提升。悟性 +1，修为 +50"),
        _c("只是参观，不参与", rewards={"cultivation": 30}, flavor="你参观了一番，略有收获。修为 +30"),
        _c("不感兴趣，离开", rewards={}, flavor="你继续赶路。"),
    ],
    city="炎阳城"
))

EVENTS.append(_e(
    "万宝楼秘密拍卖",
    "万宝楼的一名伙计悄悄告诉你，今晚有一场不对外公开的秘密拍卖，拍品都是来历不明的珍稀宝物，邀请你参加。",
    [
        _c("参加秘密拍卖", next_event={
            "desc": "拍卖在地下室进行，参与者都蒙着面，拍品中有一件散发着奇异光芒的古玉。",
            "choices": [
                _c("竞拍古玉", condition=_cond("fortune", 8), rewards={"spirit_stones": -150, "fortune": 2, "lifespan": 50, "soul": 1}, flavor="古玉入手，你感到一股奇异的灵气涌入，机缘大涨，寿元和神识都大幅提升。灵石 -150，机缘 +2，寿元 +50，神识 +1"),
                _c("竞拍古玉", rewards={"spirit_stones": -150, "lifespan": 30, "fortune": 1}, flavor="古玉略有补益，机缘略有提升。灵石 -150，寿元 +30，机缘 +1"),
                _c("竞拍其他宝物", condition=_cond("comprehension", 6), rewards={"spirit_stones": -100, "cultivation": 180, "comprehension": 1}, flavor="你以独到眼光拍下了一件被低估的修炼宝物，悟性有所提升，修为大进。灵石 -100，修为 +180，悟性 +1"),
                _c("竞拍其他宝物", rewards={"spirit_stones": -80, "cultivation": 120}, flavor="你拍下了一件修炼宝物，修为有所提升。灵石 -80，修为 +120"),
            ]
        }),
        _c("拒绝，可能是陷阱", rewards={"fortune": 1}, flavor="你拒绝了，机缘略有提升，说明你的直觉是对的。机缘 +1"),
        _c("举报给城主府", condition=_cond("fortune", 6), rewards={"reputation": 50, "spirit_stones": 80}, flavor="你举报了秘密拍卖，获得了赏金，声望大涨。声望 +50，灵石 +80"),
    ],
    city="万宝楼"
))

EVENTS.append(_e(
    "天水镇水道感悟",
    "天水镇水灵气充沛，镇外有一条灵气充沛的溪流，据说在此打坐可以感悟水道真意。",
    [
        _c("在溪边打坐感悟", condition=_cond("soul", 7), rewards={"soul": 1, "comprehension": 1, "cultivation": 100, "lifespan": 15}, flavor="你在溪边感悟水道，神识和悟性都有所提升，修为大进，寿元也略有增长。神识 +1，悟性 +1，修为 +100，寿元 +15"),
        _c("在溪边打坐感悟", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 70}, flavor="你感悟到了一丝水道真意，悟性有所提升，修为大进。悟性 +1，修为 +70"),
        _c("在溪边打坐感悟", rewards={"cultivation": 50, "lifespan": 8}, flavor="水灵气滋养，修为和寿元都略有提升。修为 +50，寿元 +8"),
        _c("在溪中沐浴，以水灵气淬体", condition=_cond("physique", 6), rewards={"physique": 1, "lifespan": 20}, flavor="水灵气淬体，体魄有所提升，寿元也略有增长。体魄 +1，寿元 +20"),
        _c("在溪中沐浴，以水灵气淬体", rewards={"lifespan": 12}, flavor="水灵气滋养，寿元略有增长。寿元 +12"),
        _c("不感兴趣，离开", rewards={}, flavor="你继续赶路。"),
    ],
    city="天水镇"
))
