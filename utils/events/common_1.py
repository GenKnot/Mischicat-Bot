from utils.events._base import _e, _c, _cond

EVENTS = []

EVENTS.append(_e(
    "神秘洞穴",
    "在山间游历时，你发现一处隐于藤蔓之后的洞穴，洞口隐约有灵气流动，不知深浅。",
    [
        _c("拔剑在手，直接闯入", next_event={
            "desc": "洞内昏暗，灵气浓郁，深处传来低沉的喘息声。你握紧手中剑，继续前行还是就此止步？",
            "choices": [
                _c("继续深入，一探究竟", condition=_cond("physique", 7), rewards={"spirit_stones": 100}, flavor="你击败了洞中妖兽，发现了一处小型灵石矿脉。灵石 +100"),
                _c("继续深入，一探究竟", rewards={"lifespan": -8, "spirit_stones": 20}, flavor="妖兽凶猛，你受伤逃出，所幸捡到几块散落的灵石。寿元 -8，灵石 +20"),
                _c("原路退出，不值得冒险", rewards={}, flavor="你谨慎退出，安然无恙。"),
            ]
        }),
        _c("在洞口静候片刻，观察动静", next_event={
            "desc": "片刻后，一只灵狐从洞中跑出，见到你后停下打量，似乎在评估你的善意。",
            "choices": [
                _c("拿出食物引诱它靠近", condition=_cond("fortune", 6), rewards={"spirit_stones": 80}, flavor="灵狐带你找到一处灵草丛，采摘后售出颇为值钱。灵石 +80"),
                _c("拿出食物引诱它靠近", rewards={}, flavor="灵狐嗅了嗅，转身跑掉了。"),
                _c("跟着灵狐进入洞穴", condition=_cond("comprehension", 7), rewards={"cultivation": 80}, flavor="洞内深处有前人留下的功法残卷，你悉心研读，修为大进。修为 +80"),
                _c("跟着灵狐进入洞穴", rewards={"spirit_stones": 30}, flavor="洞内只有些普通灵石，聊胜于无。灵石 +30"),
            ]
        }),
        _c("绕行洞穴一圈，寻找其他入口", condition=_cond("fortune", 7), rewards={"lifespan": 20}, flavor="你发现了一处隐藏侧洞，内有一颗品质不错的丹药，服下后神清气爽。寿元 +20"),
        _c("绕行洞穴一圈，寻找其他入口", rewards={"lifespan": -1}, flavor="绕了一圈什么都没有，略感疲惫。寿元 -1"),
        _c("转身离去，多一事不如少一事", rewards={"fortune": 1}, flavor="你转身离去，走了几步却隐约感觉背后有目光注视。也许是错觉，也许不是。机缘 +1"),
    ]
))

EVENTS.append(_e(
    "受伤的灵兽",
    "山道旁，一只受伤的灵兽正在哀鸣，伤口渗血，眼神中带着警惕与恐惧。",
    [
        _c("上前救治它", next_event={
            "desc": "灵兽在你的救治下渐渐平静，它舔了舔你的手，随后跑进了林中。片刻后它叼着什么东西回来了。",
            "choices": [
                _c("接受它带来的东西", condition=_cond("fortune", 6), rewards={"spirit_stones": 120, "fortune": 1}, flavor="竟是一颗品相极佳的灵珠，价值不菲。灵石 +120，机缘 +1"),
                _c("接受它带来的东西", rewards={"spirit_stones": 50}, flavor="是几块普通灵石，聊表心意。灵石 +50"),
            ]
        }),
        _c("绕道而行，不想惹麻烦", rewards={}, flavor="你绕道离开，心中隐隐有些不安。"),
        _c("将其击杀，取其妖丹", condition=_cond("physique", 6), rewards={"spirit_stones": 60, "lifespan": -3}, flavor="灵兽垂死挣扎，你受了些轻伤，但妖丹换了不少灵石。灵石 +60，寿元 -3"),
        _c("将其击杀，取其妖丹", rewards={"lifespan": -10}, flavor="灵兽爆发出惊人的战力，你狼狈逃脱，伤势不轻。寿元 -10"),
    ]
))

EVENTS.append(_e(
    "神秘老人",
    "路边坐着一位衣衫褴褛的老人，他抬头看了你一眼，笑道：「有缘人，老夫这里有样东西，不知你可有兴趣？」",
    [
        _c("停下来听他说", next_event={
            "desc": "老人从怀中掏出一个布包，里面是一颗散发着淡淡光芒的丹药。「五十灵石，你要不要？」",
            "choices": [
                _c("掏出灵石购买", condition=_cond("soul", 6), rewards={"spirit_stones": -50, "lifespan": 30, "comprehension": 1}, flavor="丹药入口，一股暖流遍布全身，竟是一颗难得的益寿延年丹。寿元 +30，悟性 +1"),
                _c("掏出灵石购买", rewards={"spirit_stones": -50, "lifespan": 10}, flavor="普通的培元丹，但也物有所值。寿元 +10"),
                _c("婉言拒绝", rewards={}, flavor="老人点点头，不再多言。你总觉得他的眼神意味深长。"),
            ]
        }),
        _c("不理会，继续赶路", rewards={"fortune": 1}, flavor="走出几步，身后传来老人的笑声：「有缘再见。」莫名地，你感觉今日运气会不错。机缘 +1"),
        _c("警惕地打量他，试探问道", condition=_cond("comprehension", 7), rewards={"comprehension": 1}, flavor="你察觉此人深藏不露，两人交谈片刻，你受益良多。悟性 +1"),
        _c("警惕地打量他，试探问道", rewards={}, flavor="老人只是笑而不语，你问不出什么，只好离去。"),
    ]
))

EVENTS.append(_e(
    "山贼劫道",
    "前方山路突然窜出数名彪悍汉子，为首者横刀立马：「此路是我开，此树是我栽，要想过此路，留下买路财！」",
    [
        _c("拔剑迎战", next_event={
            "desc": "山贼们见你不惧，一拥而上。你奋力拼杀，局势渐渐明朗。",
            "choices": [
                _c("全力出击，一举击溃", condition=_cond("physique", 7), rewards={"spirit_stones": 80, "physique": 1}, flavor="山贼溃败，你缴获了他们的财物，体魄也在战斗中得到锻炼。灵石 +80，体魄 +1"),
                _c("全力出击，一举击溃", rewards={"lifespan": -6, "spirit_stones": -30}, flavor="你击退了山贼，但自身也受了伤，还丢失了部分灵石。寿元 -6，灵石 -30"),
            ]
        }),
        _c("掏出灵石打发他们", rewards={"spirit_stones": -40}, flavor="破财消灾，山贼们拿了灵石便散去了。灵石 -40"),
        _c("施展身法，绕道而行", condition=_cond("fortune", 7), rewards={"fortune": 1, "spirit_stones": 50}, flavor="你轻松甩开山贼，还顺手捡到了他们之前劫来的一个钱袋。机缘 +1，灵石 +50"),
        _c("施展身法，绕道而行", rewards={"lifespan": -2}, flavor="你勉强逃脱，但在慌乱中扭伤了脚踝。寿元 -2"),
    ]
))

EVENTS.append(_e(
    "废弃道观",
    "山间有一座废弃的道观，门扉半掩，里面隐约有灵气残留，不知荒废了多少年。",
    [
        _c("推门进入探索", next_event={
            "desc": "道观内尘埃遍布，正殿供奉的神像已经残破。角落里有一个落满灰尘的书架。",
            "choices": [
                _c("仔细翻找书架", condition=_cond("comprehension", 6), rewards={"cultivation": 100, "soul": 1}, flavor="你发现了一本残缺的修炼心得，虽不完整，但字字珠玑。修为 +100，神识 +1"),
                _c("仔细翻找书架", rewards={"cultivation": 40}, flavor="只找到几页残破的功法碎片，勉强有些参考价值。修为 +40"),
                _c("在正殿打坐冥想", condition=_cond("soul", 6), rewards={"soul": 1, "lifespan": 5}, flavor="残存的道韵让你心神宁静，神识得到了些许提升。神识 +1，寿元 +5"),
                _c("在正殿打坐冥想", rewards={"cultivation": 30}, flavor="灵气稀薄，但静心修炼片刻也有些收获。修为 +30"),
            ]
        }),
        _c("在门口观望，不进入", rewards={"fortune": 1, "spirit_stones": 30}, flavor="你没有进入，却在门口的石阶下发现了一个小布袋，里面有几枚灵石。机缘 +1，灵石 +30"),
        _c("转身离去", rewards={}, flavor="你感觉此地阴气略重，还是离开为妙。"),
    ]
))

EVENTS.append(_e(
    "灵泉",
    "林间深处，你发现一处隐秘的灵泉，泉水清澈，灵气氤氲，泉边野花盛开，宛如仙境。",
    [
        _c("脱衣入泉沐浴", next_event={
            "desc": "泉水温热，灵气从毛孔渗入，你感到前所未有的舒畅。沐浴片刻后，你察觉泉底似乎有什么东西。",
            "choices": [
                _c("潜入泉底探查", condition=_cond("fortune", 7), rewards={"lifespan": 20, "bone": 1}, flavor="泉底有一块温润的灵玉，长期浸泡在灵泉中已有灵性。根骨 +1，寿元 +20"),
                _c("潜入泉底探查", rewards={"lifespan": 15}, flavor="只是普通的泉底石块，但灵泉本身已让你受益不少。寿元 +15"),
                _c("不去理会，继续享受", rewards={"lifespan": 20}, flavor="你尽情沐浴，神清气爽，寿元得到了恢复。寿元 +20"),
            ]
        }),
        _c("掬水饮用", condition=_cond("fortune", 6), rewards={"lifespan": 10, "comprehension": 1}, flavor="灵泉入喉，甘甜清冽，你感到思维前所未有地清晰。寿元 +10，悟性 +1"),
        _c("掬水饮用", rewards={"lifespan": 8}, flavor="灵泉甘甜，略有补益。寿元 +8"),
        _c("取些泉水装入水囊带走", rewards={"spirit_stones": 60}, flavor="灵泉水在市集上颇受欢迎，你换得了不少灵石。灵石 +60"),
    ]
))

EVENTS.append(_e(
    "迷雾山林",
    "前方山路突然被一片浓雾笼罩，能见度极低，方向难辨，你不知不觉已经迷失在其中。",
    [
        _c("静下心来，感应灵气方向", next_event={
            "desc": "你闭目感应，隐约察觉到灵气流动的方向，顺着走去，雾中出现了一个模糊的身影。",
            "choices": [
                _c("上前询问", condition=_cond("fortune", 6), rewards={"fortune": 1, "spirit_stones": 50}, flavor="竟是一位迷路的丹师，他感激你的帮助，赠予你一颗丹药换成灵石。机缘 +1，灵石 +50"),
                _c("上前询问", rewards={"lifespan": -3}, flavor="那只是一只迷路的妖兽，你仓皇逃脱，受了些轻伤。寿元 -3"),
                _c("绕开身影，自行寻路", rewards={"lifespan": -2}, flavor="你在迷雾中兜转许久才走出，耗费了不少精力。寿元 -2"),
            ]
        }),
        _c("原路返回，等雾散再走", rewards={"lifespan": -1}, flavor="你耐心等待，雾气散去后继续赶路，只是耽误了些时间。寿元 -1"),
        _c("强行闯入，凭感觉走", condition=_cond("physique", 7), rewards={"physique": 1}, flavor="你凭借强健的体魄硬闯迷雾，虽然走了不少弯路，但体魄得到了锻炼。体魄 +1"),
        _c("强行闯入，凭感觉走", rewards={"lifespan": -5}, flavor="你在迷雾中迷失了很久，精疲力竭才走出。寿元 -5"),
    ]
))

EVENTS.append(_e(
    "集市奇遇",
    "途经一处热闹的集市，各色摊贩叫卖声此起彼伏，一个不起眼的角落里，一位老者正在兜售一个蒙着黑布的笼子。",
    [
        _c("上前询问笼中是何物", next_event={
            "desc": "老者掀开黑布，里面是一只通体雪白的小兽，眼睛如红宝石般明亮。「一百灵石，有缘人才能买。」",
            "choices": [
                _c("掏出一百灵石购买", condition=_cond("fortune", 7), rewards={"spirit_stones": -100, "fortune": 2}, flavor="小兽与你亲昵异常，似乎与你有缘，日后必有大用。灵石 -100，机缘 +2"),
                _c("掏出一百灵石购买", rewards={"spirit_stones": -100, "fortune": 1}, flavor="小兽乖巧可爱，机缘似乎好了些。灵石 -100，机缘 +1"),
                _c("讨价还价，五十灵石", condition=_cond("fortune", 6), rewards={"spirit_stones": -50, "fortune": 1}, flavor="老者犹豫片刻，点头答应了。机缘 +1，灵石 -50"),
                _c("讨价还价，五十灵石", rewards={}, flavor="老者摇头，你只好作罢。"),
                _c("不感兴趣，离开", rewards={}, flavor="你转身离去，总觉得错过了什么。"),
            ]
        }),
        _c("在集市上随意逛逛", condition=_cond("fortune", 6), rewards={"spirit_stones": 70}, flavor="你在一个不起眼的摊位上发现了一件被低估的灵器，转手卖出大赚一笔。灵石 +70"),
        _c("在集市上随意逛逛", rewards={"spirit_stones": -20}, flavor="你被热情的摊贩拉着买了些用处不大的东西。灵石 -20"),
        _c("直接离开，不感兴趣", rewards={}, flavor="你匆匆离去，集市的喧嚣渐渐远去。"),
    ]
))

EVENTS.append(_e(
    "悬崖采药",
    "悬崖峭壁上，一株散发着淡淡金光的灵草映入眼帘，那是难得一见的金芝，价值不菲。",
    [
        _c("徒手攀爬悬崖采摘", next_event={
            "desc": "你奋力攀爬，距离灵草越来越近，但崖壁湿滑，脚下一松……",
            "choices": [
                _c("稳住身形，继续攀爬", condition=_cond("physique", 7), rewards={"spirit_stones": 150, "physique": 1}, flavor="你成功采到金芝，体魄也在极限挑战中得到提升。灵石 +150，体魄 +1"),
                _c("稳住身形，继续攀爬", rewards={"lifespan": -10, "spirit_stones": 80}, flavor="你跌落后被藤蔓挂住，惊魂未定，但金芝已在手中。寿元 -10，灵石 +80"),
                _c("放弃，原路返回", rewards={"lifespan": -2}, flavor="你谨慎退回，虽然安全，但心有不甘。寿元 -2"),
            ]
        }),
        _c("寻找其他路径绕上去", condition=_cond("comprehension", 6), rewards={"spirit_stones": 150}, flavor="你找到了一条隐蔽的山路，轻松采到了金芝。灵石 +150"),
        _c("寻找其他路径绕上去", rewards={"lifespan": -3}, flavor="绕路耗费了大量时间和体力，最终还是没找到上去的路。寿元 -3"),
        _c("放弃，此地太危险", rewards={}, flavor="你叹了口气，转身离去。"),
    ]
))

EVENTS.append(_e(
    "古井",
    "荒野中有一口古井，井沿上刻满了看不懂的符文，井底隐约有微光闪烁。",
    [
        _c("俯身查看井底", next_event={
            "desc": "井底的光芒越来越亮，你感到一股神秘的力量在牵引着你。",
            "choices": [
                _c("顺着绳子下井", condition=_cond("fortune", 7), rewards={"spirit_stones": 200, "bone": 1}, flavor="井底有一个古老的储物袋，内有大量灵石和一块温润的根骨玉。灵石 +200，根骨 +1"),
                _c("顺着绳子下井", rewards={"lifespan": -8}, flavor="井底阴气极重，你强撑着爬上来，元气大伤。寿元 -8"),
                _c("投入一枚灵石试探", condition=_cond("soul", 6), rewards={"soul": 1}, flavor="灵石落入井底，激起一圈涟漪，你从中感悟到了一丝天地法则。神识 +1"),
                _c("投入一枚灵石试探", rewards={"spirit_stones": -1}, flavor="灵石落入井底，什么都没发生。"),
            ]
        }),
        _c("研究井沿上的符文", condition=_cond("comprehension", 7), rewards={"comprehension": 1, "cultivation": 50}, flavor="你花了些时间研究符文，竟从中悟出了一丝阵法之道。悟性 +1，修为 +50"),
        _c("研究井沿上的符文", rewards={"cultivation": 20}, flavor="符文深奥难懂，你只看出了些皮毛。修为 +20"),
        _c("绕道而行，不去招惹", rewards={}, flavor="你绕开古井继续赶路，心中隐隐觉得此地不寻常。"),
    ]
))
