from utils.events._base import _e, _c, _cond

EVENTS = []

EVENTS.append(_e(
    "落云城灵石兑换",
    "落云城灵材市场旁新开了一家兑换铺，掌柜声称可低价兑换东海灵脉产出的「水灵晶」，今日限兑。",
    [
        _c("用灵石兑换水灵晶", next_event={
            "desc": "掌柜为你称量灵晶，你若神识敏锐可辨成色，否则全凭运气。",
            "choices": [
                _c("仔细辨成色再兑", condition=_cond("soul", 6), rewards={"spirit_stones": 70, "soul": 1}, flavor="你辨出上品水灵晶，兑得一批转手小赚，神识亦有锻炼。灵石 +70，神识 +1"),
                _c("仔细辨成色再兑", rewards={"spirit_stones": 40}, flavor="你兑了一批灵晶，略有赚头。灵石 +40"),
                _c("不辨成色，直接兑", condition=_cond("fortune", 6), rewards={"fortune": 1, "spirit_stones": 55}, flavor="你随手一兑，竟拿到成色不错的一批。机缘 +1，灵石 +55"),
                _c("不辨成色，直接兑", rewards={"spirit_stones": 20}, flavor="灵晶成色一般，勉强不亏。灵石 +20"),
            ]
        }),
        _c("不兑，只逛逛", rewards={}, flavor="你未参与兑换，继续赶路。"),
    ],
    city="落云城"
))

EVENTS.append(_e(
    "青云坊法器折扣",
    "青云坊一家铸造坊因师傅要闭关，将一批库存法器打折出售，门口已排起长队。",
    [
        _c("排队抢购", next_event={
            "desc": "轮到你时只剩几件：一柄短剑、一面护心镜、一双灵靴。",
            "choices": [
                _c("买短剑", condition=_cond("comprehension", 6), rewards={"spirit_stones": -50, "cultivation": 80}, flavor="短剑内蕴一缕剑意，你参悟后修为大进。灵石 -50，修为 +80"),
                _c("买短剑", rewards={"spirit_stones": -50, "cultivation": 40}, flavor="短剑品质尚可，略助修炼。灵石 -50，修为 +40"),
                _c("买护心镜", condition=_cond("physique", 6), rewards={"spirit_stones": -45, "physique": 1}, flavor="护心镜淬体效果不错，体魄略增。灵石 -45，体魄 +1"),
                _c("买护心镜", rewards={"spirit_stones": -45}, flavor="护心镜可护身，聊胜于无。灵石 -45"),
                _c("不买，离开", rewards={}, flavor="你觉得不合算，未买。"),
            ]
        }),
        _c("不排队，离开", rewards={}, flavor="你未参与抢购。"),
    ],
    city="青云坊"
))

EVENTS.append(_e(
    "碧波城海货市集",
    "碧波城码头今日有海族商队靠岸，海货市集上摆满了深海灵珠、珊瑚灵枝与各类海兽材料。",
    [
        _c("在市集挑选海货", next_event={
            "desc": "一名海族摊主指着几样货品：一袋灵珠、一根珊瑚枝、一瓶海兽精血。",
            "choices": [
                _c("买灵珠", condition=_cond("fortune", 6), rewards={"spirit_stones": -40, "soul": 1, "lifespan": 15}, flavor="灵珠品质上乘，滋养神识与寿元。灵石 -40，神识 +1，寿元 +15"),
                _c("买灵珠", rewards={"spirit_stones": -40, "lifespan": 10}, flavor="灵珠略有补益。灵石 -40，寿元 +10"),
                _c("买珊瑚枝", rewards={"spirit_stones": -35, "cultivation": 50}, flavor="珊瑚枝可入药修炼，修为略增。灵石 -35，修为 +50"),
                _c("买海兽精血", condition=_cond("physique", 6), rewards={"spirit_stones": -50, "physique": 1}, flavor="精血淬体，体魄略增。灵石 -50，体魄 +1"),
                _c("买海兽精血", rewards={"spirit_stones": -50}, flavor="精血略有淬体之效。灵石 -50"),
            ]
        }),
        _c("只看不买", rewards={}, flavor="你逛了一圈未下手。"),
    ],
    city="碧波城"
))

EVENTS.append(_e(
    "天水镇灵泉水售卖",
    "天水镇郊外灵泉今日开放取水，镇民在泉眼旁设摊售卖已灌好的灵泉水，价格比城中便宜。",
    [
        _c("购买灵泉水", next_event={
            "desc": "摊主说有一壶「泉心水」和两壶普通灵泉水，泉心水价高但效佳。",
            "choices": [
                _c("买泉心水", condition=_cond("fortune", 6), rewards={"spirit_stones": -30, "lifespan": 25, "cultivation": 60}, flavor="泉心水品质极佳，寿元与修为皆进。灵石 -30，寿元 +25，修为 +60"),
                _c("买泉心水", rewards={"spirit_stones": -30, "lifespan": 15}, flavor="泉心水物有所值。灵石 -30，寿元 +15"),
                _c("买两壶普通灵泉水", rewards={"spirit_stones": -20, "lifespan": 10}, flavor="两壶灵泉水略有补益。灵石 -20，寿元 +10"),
            ]
        }),
        _c("不买，离开", rewards={}, flavor="你未购买灵泉水。"),
    ],
    city="天水镇"
))

EVENTS.append(_e(
    "玄风城御剑材料铺",
    "玄风城专营御剑材料的铺子里新到了一批「剑胚石」与「风灵羽」，剑修们争相询价。",
    [
        _c("进店选购", next_event={
            "desc": "掌柜说剑胚石可温养本命剑意，风灵羽可炼入飞剑增速度。你灵石有限，只能择一。",
            "choices": [
                _c("买剑胚石", condition=_cond("comprehension", 6), rewards={"spirit_stones": -55, "comprehension": 1, "cultivation": 70}, flavor="剑胚石助你感悟剑意，悟性与修为皆进。灵石 -55，悟性 +1，修为 +70"),
                _c("买剑胚石", rewards={"spirit_stones": -55, "cultivation": 45}, flavor="剑胚石略助修炼。灵石 -55，修为 +45"),
                _c("买风灵羽", condition=_cond("fortune", 6), rewards={"spirit_stones": -50, "fortune": 1}, flavor="风灵羽炼入法器后你气运似有提升。灵石 -50，机缘 +1"),
                _c("买风灵羽", rewards={"spirit_stones": -50}, flavor="风灵羽可作炼器之用。灵石 -50"),
            ]
        }),
        _c("不买，离开", rewards={}, flavor="你未购材料。"),
    ],
    city="玄风城"
))

EVENTS.append(_e(
    "赤炎城丹材收购",
    "赤炎城丹师公会今日挂牌收购一批「火纹草」与「地心莲」，出价高于平日。",
    [
        _c("出售手中丹材", condition=_cond("fortune", 6), rewards={"spirit_stones": 90, "fortune": 1}, flavor="你手中恰有公会所需丹材，卖得高价。灵石 +90，机缘 +1"),
        _c("出售手中丹材", rewards={"spirit_stones": 55}, flavor="你卖出部分丹材，收入尚可。灵石 +55"),
        _c("接取收购任务，去城外采药", next_event={
            "desc": "你接下了采火纹草的任务，城外火山脚下有生长，但需小心地火。",
            "choices": [
                _c("小心采摘", condition=_cond("soul", 6), rewards={"soul": 1, "spirit_stones": 80}, flavor="你以神识避让地火，采足火纹草交差。神识 +1，灵石 +80"),
                _c("小心采摘", rewards={"spirit_stones": 50}, flavor="你采到部分火纹草，勉强完成任务。灵石 +50"),
                _c("冒险深入", condition=_cond("physique", 6), rewards={"physique": 1, "spirit_stones": 100}, flavor="你体魄扛住地火，采到更多灵草。体魄 +1，灵石 +100"),
                _c("冒险深入", rewards={"lifespan": -5, "spirit_stones": 40}, flavor="地火灼伤，你带伤交差。寿元 -5，灵石 +40"),
            ]
        }),
        _c("不参与，离开", rewards={}, flavor="你未参与收购。"),
    ],
    city="赤炎城"
))

EVENTS.append(_e(
    "炎阳城古法器摊",
    "炎阳城坊市角落有人摆摊卖「古法器」，摊主说是从遗迹里挖出的，真伪难辨。",
    [
        _c("挑一件问价", next_event={
            "desc": "摊主指着一面铜镜、一柄断刃、一枚玉扣，各要价不同。你若懂行可辨真假。",
            "choices": [
                _c("以神识辨真伪后买铜镜", condition=_cond("soul", 6), rewards={"spirit_stones": -35, "soul": 1}, flavor="你辨出铜镜内蕴灵性，买下后温养神识。灵石 -35，神识 +1"),
                _c("以神识辨真伪后买铜镜", rewards={"spirit_stones": -35}, flavor="铜镜似有灵性，你买下把玩。灵石 -35"),
                _c("买断刃", condition=_cond("fortune", 6), rewards={"spirit_stones": -30, "cultivation": 60}, flavor="断刃残存一丝战意，你参悟后修为略增。灵石 -30，修为 +60"),
                _c("买断刃", rewards={"spirit_stones": -30}, flavor="断刃当纪念品买下。灵石 -30"),
                _c("不买，离开", rewards={}, flavor="你怕上当，未买。"),
            ]
        }),
        _c("不理会地摊", rewards={}, flavor="你未驻足。"),
    ],
    city="炎阳城"
))

EVENTS.append(_e(
    "望月楼占卜摊",
    "望月楼下的占卜摊今日开张，摊主说可占「近日机缘」或「修行瓶颈」，一卦十灵石。",
    [
        _c("付灵石占一卦", next_event={
            "desc": "占卜师掐指推演，道：「你机缘在西北，三日内若往西北行，或有小喜。」",
            "choices": [
                _c("信其言，三日内往西北", condition=_cond("fortune", 6), rewards={"fortune": 1, "spirit_stones": 50}, flavor="你在西北方向偶得一处小机缘，灵石与气运皆增。机缘 +1，灵石 +50"),
                _c("信其言，三日内往西北", rewards={"spirit_stones": 25}, flavor="你往西北走了一趟，小有收获。灵石 +25"),
                _c("只当娱乐，不刻意应卦", rewards={"spirit_stones": -10}, flavor="你付了卦金，未当真。灵石 -10"),
            ]
        }),
        _c("不占卜，离开", rewards={}, flavor="你未占卜。"),
    ],
    city="望月楼"
))

EVENTS.append(_e(
    "铁甲城武器铺",
    "铁甲城武修常光顾的武器铺新到一批「淬体刃」——专供体修对练用的钝刃，据说对练可助体魄精进。",
    [
        _c("买一柄淬体刃并找人对练", next_event={
            "desc": "你在擂台下找到一名愿意对练的武修，双方以淬体刃互击，痛楚与收获并存。",
            "choices": [
                _c("咬牙对练到底", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 50}, flavor="你撑完全程，体魄与修为皆进。体魄 +1，修为 +50"),
                _c("咬牙对练到底", rewards={"cultivation": 30}, flavor="你对练一番，略有收获。修为 +30"),
                _c("对练片刻便停", rewards={"spirit_stones": -20}, flavor="你只练了一会儿，淬体刃算白买。灵石 -20"),
            ]
        }),
        _c("只买不练", rewards={"spirit_stones": -25}, flavor="你买了淬体刃备用。灵石 -25"),
        _c("不买，离开", rewards={}, flavor="你未购淬体刃。"),
    ],
    city="铁甲城"
))

EVENTS.append(_e(
    "苍穹城雷晶交易",
    "苍穹城因雷灵气充沛，常有雷修在此交易「雷晶」与「引雷符」。今日有一批雷晶到货，价格被炒高。",
    [
        _c("参与雷晶竞价", next_event={
            "desc": "你加入竞价，若机缘好可抢到成色佳的雷晶；否则可能高价买普通货。",
            "choices": [
                _c("适可而止，拍到一块即停", condition=_cond("fortune", 6), rewards={"spirit_stones": -40, "bone": 1}, flavor="你拍到的雷晶成色不错，淬体后根骨略增。灵石 -40，根骨 +1"),
                _c("适可而止，拍到一块即停", rewards={"spirit_stones": -40, "cultivation": 40}, flavor="雷晶略助修炼。灵石 -40，修为 +40"),
                _c("高价抢拍多块", condition=_cond("soul", 6), rewards={"spirit_stones": -80, "soul": 1, "cultivation": 70}, flavor="你以神识辨出佳品，多块雷晶助你神识与修为皆进。灵石 -80，神识 +1，修为 +70"),
                _c("高价抢拍多块", rewards={"spirit_stones": -80}, flavor="你抢到多块但成色一般。灵石 -80"),
            ]
        }),
        _c("不参与竞价", rewards={}, flavor="你未参与。"),
    ],
    city="苍穹城"
))

EVENTS.append(_e(
    "寒冰城冰晶市场",
    "寒冰城冰晶市场今日有「千年寒髓」碎片出售，是炼制冰属法器的顶级辅料，但价格不菲。",
    [
        _c("询价后购买一小块", condition=_cond("physique", 6), rewards={"spirit_stones": -60, "physique": 1, "lifespan": 15}, flavor="你以体魄承受寒髓寒气炼化，体魄与寿元皆进。灵石 -60，体魄 +1，寿元 +15"),
        _c("询价后购买一小块", rewards={"spirit_stones": -60, "lifespan": 10}, flavor="寒髓略滋体魄与寿元。灵石 -60，寿元 +10"),
        _c("只观不买，感受寒气", rewards={"cultivation": 35}, flavor="你在市场边感受寒气，略有所得。修为 +35"),
        _c("不买，离开", rewards={}, flavor="你未购买。"),
    ],
    city="寒冰城"
))

EVENTS.append(_e(
    "幽冥镇阴物交易",
    "幽冥镇鬼修聚集，坊间有「阴魂木」「养魂香」等阴物出售，据说可助神识修炼，但常人久触易损阳气。",
    [
        _c("购买养魂香试用", next_event={
            "desc": "你点燃养魂香打坐，需以神识引导阴气，否则反伤神魂。",
            "choices": [
                _c("以神识引导阴气", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 55}, flavor="你以神识化用养魂香，神识与修为皆进。神识 +1，修为 +55"),
                _c("以神识引导阴气", rewards={"cultivation": 35}, flavor="你略有所得。修为 +35"),
                _c("未引导，强吸", rewards={"lifespan": -5, "soul": 1}, flavor="阴气反噬略伤寿元，但神识亦有锻炼。寿元 -5，神识 +1"),
            ]
        }),
        _c("不买阴物", rewards={}, flavor="你未购阴物。"),
    ],
    city="幽冥镇"
))

EVENTS.append(_e(
    "雪狼城皮毛市集",
    "雪狼城以极寒灵材闻名，今日市集上有一批雪狼皮与冰狐尾出售，是制作防具与法器的好材料。",
    [
        _c("购买雪狼皮", condition=_cond("physique", 6), rewards={"spirit_stones": -45, "physique": 1}, flavor="雪狼皮制成护具后淬体，体魄略增。灵石 -45，体魄 +1"),
        _c("购买雪狼皮", rewards={"spirit_stones": -45}, flavor="雪狼皮可制护具。灵石 -45"),
        _c("购买冰狐尾", condition=_cond("fortune", 6), rewards={"spirit_stones": -40, "fortune": 1}, flavor="冰狐尾制成法器后你气运似有提升。灵石 -40，机缘 +1"),
        _c("购买冰狐尾", rewards={"spirit_stones": -40}, flavor="冰狐尾可作炼器。灵石 -40"),
        _c("不买，离开", rewards={}, flavor="你未购买。"),
    ],
    city="雪狼城"
))

EVENTS.append(_e(
    "玄冰谷冰材收购",
    "玄冰谷入口处有修士设点收购「谷内冰棱」与「玄冰碎屑」，入谷者可将所采卖给他们。",
    [
        _c("入谷浅层采冰棱", next_event={
            "desc": "你入谷浅层，寒气已重，采到几块冰棱后需尽快退出。",
            "choices": [
                _c("采够即退", condition=_cond("physique", 6), rewards={"physique": 1, "spirit_stones": 65}, flavor="你体魄扛住寒气，采到冰棱售出。体魄 +1，灵石 +65"),
                _c("采够即退", rewards={"spirit_stones": 45}, flavor="你采到部分冰棱售出。灵石 +45"),
                _c("多采一会儿", condition=_cond("fortune", 6), rewards={"fortune": 1, "spirit_stones": 80}, flavor="你多采到一块玄冰碎屑，卖得高价。机缘 +1，灵石 +80"),
                _c("多采一会儿", rewards={"lifespan": -5, "spirit_stones": 50}, flavor="你略受寒伤，但多采了些。寿元 -5，灵石 +50"),
            ]
        }),
        _c("不入谷，离开", rewards={}, flavor="你未入谷。"),
    ],
    city="玄冰谷"
))

EVENTS.append(_e(
    "天京城顶级拍卖",
    "天京城一场小型顶级拍卖正在举行，入场需验资。你勉强够格入场，场内多是大宗门子弟。",
    [
        _c("入场观摩并择机出价", next_event={
            "desc": "台上有一件「无名古卷」起拍价不高，但无人识货；另有一件热门法器被争抢。",
            "choices": [
                _c("拍无名古卷", condition=_cond("comprehension", 6), rewards={"spirit_stones": -70, "comprehension": 1, "cultivation": 90}, flavor="古卷竟是残篇心法，你参悟后悟性与修为皆进。灵石 -70，悟性 +1，修为 +90"),
                _c("拍无名古卷", rewards={"spirit_stones": -70, "cultivation": 50}, flavor="古卷内容零散，略有所得。灵石 -70，修为 +50"),
                _c("拍热门法器", rewards={"spirit_stones": -100}, flavor="你以高价拍下法器，品质尚可。灵石 -100"),
                _c("不出价，只观摩", rewards={"reputation": 5}, flavor="你见识了顶级拍卖氛围。声望 +5"),
            ]
        }),
        _c("不入场", rewards={}, flavor="你未入场。"),
    ],
    city="天京城"
))

EVENTS.append(_e(
    "灵虚城情报交易",
    "灵虚城各大势力博弈，情报贩子暗中有售「某宗门动向」「灵脉争夺内幕」等，真伪难辨。",
    [
        _c("买一条情报", next_event={
            "desc": "贩子卖给你一条「某处灵脉三日后开放」的情报，要价五十灵石。",
            "choices": [
                _c("信情报，三日后前往", condition=_cond("fortune", 6), rewards={"fortune": 1, "cultivation": 80, "spirit_stones": 30}, flavor="情报属实，你在灵脉处修炼并捡到散落灵石。机缘 +1，修为 +80，灵石 +30"),
                _c("信情报，三日后前往", rewards={"cultivation": 50}, flavor="灵脉确有开放，你略有所得。修为 +50"),
                _c("不信，当打水漂", rewards={"spirit_stones": -50}, flavor="你未前往，灵石白花。灵石 -50"),
            ]
        }),
        _c("不买情报", rewards={}, flavor="你未买情报。"),
    ],
    city="灵虚城"
))

EVENTS.append(_e(
    "清虚城道法典籍",
    "清虚城古道观对外开放藏经阁一层，修士可付费翻阅道法典籍一个时辰，不得抄录。",
    [
        _c("付费入阁翻阅", next_event={
            "desc": "你在藏经阁中翻阅，有的晦涩难懂，有的与你功法相合。需以悟性抓住要点。",
            "choices": [
                _c("专注感悟与己相关的内容", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 80}, flavor="你悟出几分道理，悟性与修为皆进。悟性 +1，修为 +80"),
                _c("专注感悟与己相关的内容", rewards={"cultivation": 50}, flavor="你略有所得。修为 +50"),
                _c("泛泛而览", rewards={"spirit_stones": -25, "cultivation": 30}, flavor="你翻了一个时辰，略有所得。灵石 -25，修为 +30"),
            ]
        }),
        _c("不入阁", rewards={}, flavor="你未入阁。"),
    ],
    city="清虚城"
))

EVENTS.append(_e(
    "御剑城飞剑材料",
    "御剑城剑道圣地，飞剑材料铺里常年有「剑心铁」「流云钢」等出售，今日流云钢打折。",
    [
        _c("购买流云钢", condition=_cond("comprehension", 6), rewards={"spirit_stones": -50, "comprehension": 1}, flavor="你以悟性感悟流云钢中的剑意，悟性略增。灵石 -50，悟性 +1"),
        _c("购买流云钢", rewards={"spirit_stones": -50}, flavor="流云钢可炼入飞剑。灵石 -50"),
        _c("只观不买", rewards={"cultivation": 25}, flavor="你在铺中观剑材，略有所悟。修为 +25"),
        _c("离开", rewards={}, flavor="你未购买。"),
    ],
    city="御剑城"
))

EVENTS.append(_e(
    "问道城论道集市",
    "问道城散修聚集，今日有「论道集市」——修士可摆摊以物易物或论道换心得。",
    [
        _c("摆摊与人论道", next_event={
            "desc": "你与人论道数场，有人与你契合，有人与你相左。若能提炼收获，可助修为。",
            "choices": [
                _c("静心提炼论道所得", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "cultivation": 70}, flavor="你从论道中悟出几分道理，悟性与修为皆进。悟性 +1，修为 +70"),
                _c("静心提炼论道所得", rewards={"cultivation": 45}, flavor="你略有所得。修为 +45"),
                _c("只当闲聊，不深究", rewards={"reputation": 10}, flavor="你与人混了个脸熟。声望 +10"),
            ]
        }),
        _c("只逛不摆摊", rewards={}, flavor="你逛了一圈离开。"),
    ],
    city="问道城"
))

EVENTS.append(_e(
    "紫霄城灵气结晶",
    "紫霄城灵气为中州之最，城中有人将灵气凝成「灵晶」出售，价高但纯度高。",
    [
        _c("购买一块灵晶炼化", condition=_cond("soul", 6), rewards={"spirit_stones": -60, "soul": 1, "cultivation": 75}, flavor="你以神识引导灵晶灵气归元，神识与修为皆进。灵石 -60，神识 +1，修为 +75"),
        _c("购买一块灵晶炼化", rewards={"spirit_stones": -60, "cultivation": 55}, flavor="灵晶助你修炼。灵石 -60，修为 +55"),
        _c("不买，只在城中打坐片刻", rewards={"cultivation": 40}, flavor="你借城中灵气修炼片刻。修为 +40"),
        _c("不买，离开", rewards={}, flavor="你未购买。"),
    ],
    city="紫霄城"
))
