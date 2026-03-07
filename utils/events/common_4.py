from utils.events._base import _e, _c, _cond

EVENTS = []

EVENTS.append(_e(
    "擂台比武",
    "城中广场搭着擂台，一名壮汉正在叫阵：「可有道友敢与某家过招？胜者五十灵石！」围观者窃窃私语，无人上台。",
    [
        _c("登台应战", next_event={
            "desc": "壮汉抱拳一礼，旋即出手。数招过后，你察觉他力大但招法粗疏。",
            "choices": [
                _c("以巧破千斤，寻隙制胜", condition=_cond("comprehension", 7), rewards={"spirit_stones": 50, "reputation": 15}, flavor="你以巧劲化解其刚猛，台下喝彩连连。灵石 +50，声望 +15"),
                _c("以巧破千斤，寻隙制胜", rewards={"lifespan": -4, "spirit_stones": 20}, flavor="你寻隙不成反被震伤，勉强认输下台。寿元 -4，灵石 +20"),
                _c("硬碰硬，以力相抗", condition=_cond("physique", 7), rewards={"spirit_stones": 50, "physique": 1}, flavor="你与他硬撼数十招，最终险胜，体魄也在激斗中有所精进。灵石 +50，体魄 +1"),
                _c("硬碰硬，以力相抗", rewards={"lifespan": -6}, flavor="你力不如人，被一掌震下擂台，内息紊乱。寿元 -6"),
                _c("认输下台", rewards={}, flavor="你拱手认输，壮汉一笑置之，未再为难。"),
            ]
        }),
        _c("在台下观摩学习", condition=_cond("comprehension", 6), rewards={"cultivation": 60}, flavor="你从几场比斗中悟出些门道，修为略有所得。修为 +60"),
        _c("在台下观摩学习", rewards={"cultivation": 25}, flavor="你看得热闹，略有所得。修为 +25"),
        _c("不感兴趣，离开", rewards={}, flavor="你对擂台比斗无甚兴趣，转身离开。"),
    ]
))

EVENTS.append(_e(
    "古籍阁",
    "坊市深处有一间不起眼的古籍阁，门口挂着「只阅不售」的牌子。推门而入，满架旧书，墨香扑鼻。",
    [
        _c("请求翻阅功法类典籍", next_event={
            "desc": "掌柜打量你一眼，指着一排书架道：「三楼左手第三架，只能在此翻阅，不得抄录。」你上楼找到几本残卷。",
            "choices": [
                _c("静心研读残卷", condition=_cond("comprehension", 7), rewards={"cultivation": 100, "comprehension": 1}, flavor="你从残卷中悟出一式心法，修为与悟性皆有进境。修为 +100，悟性 +1"),
                _c("静心研读残卷", rewards={"cultivation": 50}, flavor="残卷艰深，你只读懂部分，修为略增。修为 +50"),
                _c("暗中默记关键段落", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 40}, flavor="你神识过人，强记数段要诀，神识与修为皆有收获。神识 +1，修为 +40"),
                _c("暗中默记关键段落", rewards={"cultivation": 20}, flavor="内容繁杂，你只记下零碎几句。修为 +20"),
            ]
        }),
        _c("翻阅杂闻轶事", condition=_cond("fortune", 6), rewards={"fortune": 1, "spirit_stones": 30}, flavor="你在轶闻中看到一处藏宝暗示，按图索骥得了些灵石。机缘 +1，灵石 +30"),
        _c("翻阅杂闻轶事", rewards={"reputation": 5}, flavor="掌柜见你爱书，与你聊了几句，对你印象不错。声望 +5"),
        _c("告辞离开", rewards={}, flavor="你未多逗留，拱手离开古籍阁。"),
    ]
))

EVENTS.append(_e(
    "灵田纠纷",
    "田埂旁两名修士争执不休，一人说对方灵稻越界吸了自己灵田的肥力，另一人矢口否认。二人几乎要动起手来。",
    [
        _c("上前调解", next_event={
            "desc": "二人见有外人，暂收火气，各执一词要你评理。你细看灵田边界与稻株长势。",
            "choices": [
                _c("据理分析，划分边界", condition=_cond("comprehension", 6), rewards={"reputation": 25, "spirit_stones": 40}, flavor="你看出确有一方灵稻根系过界，提出折中方案，二人心服，各赠谢礼。声望 +25，灵石 +40"),
                _c("据理分析，划分边界", rewards={"reputation": 10}, flavor="你的分析二人半信半疑，但争执暂歇。声望 +10"),
                _c("提议共同培育一块公田", condition=_cond("fortune", 7), rewards={"fortune": 1, "reputation": 20}, flavor="二人觉得可行，合作后收成更好，对你感激有加。机缘 +1，声望 +20"),
                _c("提议共同培育一块公田", rewards={"reputation": 5}, flavor="二人兴趣不大，但也没再争吵。声望 +5"),
            ]
        }),
        _c("帮一方作证", condition=_cond("physique", 6), rewards={"spirit_stones": 60, "reputation": -15}, flavor="你替其中一方说话，得了好处，但另一方记恨于你。灵石 +60，声望 -15"),
        _c("不掺和，绕道离开", rewards={}, flavor="你不想卷入邻里纠纷，从旁绕行。"),
    ]
))

EVENTS.append(_e(
    "路遇乞丐",
    "巷口一名衣衫褴褛的老者伸手讨要，面前摆着破碗。他目光浑浊，口中念念有词，细听竟是半句残缺心法。",
    [
        _c("施舍几块灵石", next_event={
            "desc": "老者收下灵石，嘿嘿一笑，从怀里摸出一块脏兮兮的玉简递给你：「拿去，有缘人。」",
            "choices": [
                _c("接过玉简查探", condition=_cond("fortune", 7), rewards={"cultivation": 120, "bone": 1}, flavor="玉简中竟是一门残缺的炼体法门，你依法修炼，根骨与修为皆进。修为 +120，根骨 +1"),
                _c("接过玉简查探", rewards={"cultivation": 50}, flavor="玉简里是些零散口诀，聊胜于无。修为 +50"),
                _c("婉拒玉简，只当行善", rewards={"reputation": 10, "fortune": 1}, flavor="老者点头不语。你离去后心境平和，机缘似有提升。声望 +10，机缘 +1"),
            ]
        }),
        _c("追问那半句心法", condition=_cond("comprehension", 7), rewards={"comprehension": 1}, flavor="老者与你对答几句，你从中悟出些道理。悟性 +1"),
        _c("追问那半句心法", rewards={}, flavor="老者装疯卖傻，你问不出所以然。"),
        _c("目不斜视走过", rewards={}, flavor="你未作理会，径直离开。"),
    ]
))

EVENTS.append(_e(
    "秘境入口",
    "山壁间有一道若隐若现的光幕，灵气自其中丝丝外泄。旁立残碑，字迹斑驳，仅能辨出「禁」「入者」数字。",
    [
        _c("尝试以灵力触碰光幕", next_event={
            "desc": "光幕荡开涟漪，一股吸力传来，你险些被扯入。稳住身形后，发现光幕后似有空间。",
            "choices": [
                _c("顺势进入一探", condition=_cond("fortune", 7), rewards={"spirit_stones": 150, "cultivation": 80}, flavor="秘境已荒废多年，你搜到些灵石与灵药，安然退出。灵石 +150，修为 +80"),
                _c("顺势进入一探", rewards={"lifespan": -10, "spirit_stones": 30}, flavor="内里阵法残存，你触发了禁制，带伤逃出，只摸到几块灵石。寿元 -10，灵石 +30"),
                _c("收手退开", rewards={}, flavor="你不敢冒险，退后观察。光幕渐渐恢复平静。"),
            ]
        }),
        _c("研读残碑文字", condition=_cond("comprehension", 6), rewards={"cultivation": 60}, flavor="你从残碑中推演出部分禁制规律，对阵法有所领悟。修为 +60"),
        _c("研读残碑文字", rewards={"cultivation": 20}, flavor="碑文残缺太甚，所得有限。修为 +20"),
        _c("记下位置后离开", rewards={"fortune": 1}, flavor="你将此地记在心里，留待日后准备充分再来。机缘 +1"),
    ]
))

EVENTS.append(_e(
    "古碑参悟",
    "荒野中矗立着一块巨大古碑，碑面刻满符文与剑痕，不知经历多少岁月。靠近时，隐约有剑意扑面。",
    [
        _c("静坐碑前感悟剑意", next_event={
            "desc": "你闭目感应，剑意时强时弱，有时如清风，有时如雷霆。你需在合适时机捕捉那一丝真意。",
            "choices": [
                _c("全神贯注，捕捉剑意", condition=_cond("soul", 7), rewards={"soul": 1, "cultivation": 80}, flavor="你于刹那间捕捉到一缕剑意，神识与修为皆有所得。神识 +1，修为 +80"),
                _c("全神贯注，捕捉剑意", rewards={"cultivation": 40}, flavor="剑意缥缈，你只抓住一点余韵。修为 +40"),
                _c("以自身剑意与之相和", condition=_cond("comprehension", 7), rewards={"comprehension": 1, "cultivation": 70}, flavor="你以意会意，与古碑产生共鸣，悟性大增。悟性 +1，修为 +70"),
                _c("以自身剑意与之相和", rewards={"lifespan": -2}, flavor="古碑剑意反震，你心神受创。寿元 -2"),
            ]
        }),
        _c("以手摹刻碑上符文", condition=_cond("bone", 6), rewards={"bone": 1}, flavor="摹刻过程中，你体悟到符文中的炼体之意。根骨 +1"),
        _c("以手摹刻碑上符文", rewards={"cultivation": 30}, flavor="符文深奥，你只学到皮毛。修为 +30"),
        _c("不敢久留，离去", rewards={}, flavor="剑意压迫感太强，你选择离开。"),
    ]
))

EVENTS.append(_e(
    "灵厨试吃",
    "一家小酒楼门口挂着「新菜试吃，分文不取」的牌子。掌柜笑呵呵地招呼过路人，说是以灵植入馔，需修士品评。",
    [
        _c("进店试吃", next_event={
            "desc": "掌柜端上一碟灵菇炒笋、一盅灵米粥。你尝了几口，腹中暖洋洋的，灵气化开。",
            "choices": [
                _c("细细品评并提建议", condition=_cond("comprehension", 6), rewards={"lifespan": 15, "reputation": 15}, flavor="你的点评切中要害，掌柜大喜，又赠你一碗滋补汤。寿元 +15，声望 +15"),
                _c("细细品评并提建议", rewards={"lifespan": 8}, flavor="掌柜谢过，你吃得满意。寿元 +8"),
                _c("直言火候有瑕", condition=_cond("soul", 6), rewards={"soul": 1, "spirit_stones": 30}, flavor="掌柜佩服你的敏锐，赠你灵石以表谢意。神识 +1，灵石 +30"),
                _c("直言火候有瑕", rewards={"reputation": -5}, flavor="掌柜脸色一沉，你尴尬离场。声望 -5"),
            ]
        }),
        _c("谢绝，匆匆离开", rewards={}, flavor="你对口腹之欲兴趣不大，婉拒后离开。"),
    ]
))

EVENTS.append(_e(
    "炼器坊",
    "铁匠铺里炉火正旺，一名赤膊大汉正在捶打一块灵铁。他抬头见你，道：「客官可要定制法器？材料自备可打折。」",
    [
        _c("委托炼制一件防具", next_event={
            "desc": "大汉掂了掂你提供的灵材，点头道：「够打一副护腕。三日后来取，炼坏了不赔。」",
            "choices": [
                _c("三日后取货", condition=_cond("fortune", 6), rewards={"physique": 1, "spirit_stones": -30}, flavor="护腕炼成，品质不错，你戴上后体魄有所增益。体魄 +1，灵石 -30"),
                _c("三日后取货", rewards={"spirit_stones": -30}, flavor="护腕炼成了，但品质普通。灵石 -30"),
                _c("留下帮忙鼓风添柴", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 40}, flavor="你出了一身力气，大汉传你几句炼体口诀。体魄 +1，修为 +40"),
                _c("留下帮忙鼓风添柴", rewards={"cultivation": 20}, flavor="你帮了忙，大汉送你一点碎灵铁。修为 +20"),
            ]
        }),
        _c("只买现成的法器", rewards={"spirit_stones": -50, "physique": 1}, flavor="你挑了一副现成护腕，略贵但省事。灵石 -50，体魄 +1"),
        _c("不炼制，离开", rewards={}, flavor="你暂无炼器之需，告辞离开。"),
    ]
))

EVENTS.append(_e(
    "灵兽斗场",
    "地下斗场中两只灵兽正在撕咬，周围修士呐喊下注。一名管事凑过来低声道：「下一场缺个裁判，道友可愿？有酬劳。」",
    [
        _c("答应做裁判", next_event={
            "desc": "你站上高台，两只灵兽被牵出，一只是赤焰犬，一只是铁甲龟。开斗后场面血腥。",
            "choices": [
                _c("公正判罚，及时叫停", condition=_cond("soul", 6), rewards={"soul": 1, "spirit_stones": 60}, flavor="你神识敏锐，在紧要关头叫停，避免一方毙命。斗场赏你灵石。神识 +1，灵石 +60"),
                _c("公正判罚，及时叫停", rewards={"spirit_stones": 40}, flavor="你尽力维持秩序，得了酬劳。灵石 +40"),
                _c("暗中偏向一方以获贿赂", condition=_cond("fortune", 6), rewards={"spirit_stones": 100, "reputation": -20}, flavor="你收了某方好处，判罚不公，事后拿钱走人，名声受损。灵石 +100，声望 -20"),
                _c("暗中偏向一方以获贿赂", rewards={"lifespan": -5, "reputation": -25}, flavor="事情败露，你被斗场的人教训了一顿。寿元 -5，声望 -25"),
            ]
        }),
        _c("下注赌一把", condition=_cond("fortune", 7), rewards={"spirit_stones": 80}, flavor="你押对了，小赚一笔。灵石 +80"),
        _c("下注赌一把", rewards={"spirit_stones": -40}, flavor="你押错了，输掉赌注。灵石 -40"),
        _c("不愿参与，离开", rewards={}, flavor="你对斗兽无感，转身离开。"),
    ]
))

EVENTS.append(_e(
    "茶馆说书",
    "茶馆里说书人正讲到「剑仙一剑破万法」的段子，满堂喝彩。他醒木一拍，道：「欲知后事，且听下回。诸位若赏几块灵石，明日接着说。」",
    [
        _c("打赏灵石，求明日续讲", next_event={
            "desc": "说书人收下灵石，对你拱手：「多谢道友。明日除了剑仙，还有一桩本地奇闻，与城外古墓有关。」",
            "choices": [
                _c("追问古墓奇闻", condition=_cond("fortune", 6), rewards={"spirit_stones": 70, "fortune": 1}, flavor="说书人透露了一处古墓方位，你按图索骥得了些好处。灵石 +70，机缘 +1"),
                _c("追问古墓奇闻", rewards={"cultivation": 30}, flavor="说书人只说了些传闻，你当故事听，心境略有所得。修为 +30"),
                _c("不再多问，明日再来", rewards={"reputation": 10}, flavor="说书人觉得你识趣，对你印象不错。声望 +10"),
            ]
        }),
        _c("只喝茶不打赏", rewards={"lifespan": 5}, flavor="你静静喝茶歇脚，精神稍复。寿元 +5"),
        _c("离开茶馆", rewards={}, flavor="你离开茶馆，继续赶路。"),
    ]
))

EVENTS.append(_e(
    "比武招亲",
    "城楼下搭着彩台，一名红衣女子立于台上，朗声道：「小女子设擂三日，能接我十招者，可入府一叙。」台下议论纷纷。",
    [
        _c("登台接招", next_event={
            "desc": "女子抱拳，旋即出手。她剑法凌厉，你堪堪接下数招，已觉吃力。",
            "choices": [
                _c("全力撑过十招", condition=_cond("physique", 7), rewards={"reputation": 25, "spirit_stones": 50}, flavor="你咬牙撑满十招，女子点头邀你入府，赠礼相谢。声望 +25，灵石 +50"),
                _c("全力撑过十招", rewards={"lifespan": -4}, flavor="你在第八招时被剑气所伤，败下阵来。寿元 -4"),
                _c("故意在第五招认输", condition=_cond("comprehension", 6), rewards={"comprehension": 1}, flavor="你看出她意在试人而非真招亲，适时认输，她对你另眼相看，赠你一句修炼心得。悟性 +1"),
                _c("故意在第五招认输", rewards={}, flavor="她淡淡一笑，未再多言。"),
            ]
        }),
        _c("在台下观战", rewards={"cultivation": 35}, flavor="你从剑招中悟出些门道。修为 +35"),
        _c("不参与，离开", rewards={}, flavor="你对招亲无兴趣，径自离开。"),
    ]
))

EVENTS.append(_e(
    "护送商队",
    "一支小商队正在招人护送，领队道：「此去三百里，常有妖兽出没。愿随行者，到地头分二十灵石。」",
    [
        _c("应募护送", next_event={
            "desc": "途中果然遇上一群低阶妖兽袭击商队。你与护卫们并肩御敌。",
            "choices": [
                _c("冲在前方斩杀妖兽", condition=_cond("physique", 7), rewards={"spirit_stones": 50, "physique": 1}, flavor="你奋勇当先，击退妖兽，领队额外赏你。灵石 +50，体魄 +1"),
                _c("冲在前方斩杀妖兽", rewards={"lifespan": -5, "spirit_stones": 25}, flavor="你受了些伤，但坚持到终点，得了酬劳。寿元 -5，灵石 +25"),
                _c("护住车队侧翼，稳守为主", condition=_cond("soul", 6), rewards={"soul": 1, "spirit_stones": 35}, flavor="你神识敏锐，多次预警，减少伤亡。领队感激，多给了赏钱。神识 +1，灵石 +35"),
                _c("护住车队侧翼，稳守为主", rewards={"spirit_stones": 20}, flavor="一路有惊无险，你拿到约定酬劳。灵石 +20"),
            ]
        }),
        _c("谢绝，自行赶路", rewards={}, flavor="你不想耽搁，婉拒后离开。"),
    ]
))

EVENTS.append(_e(
    "寻人告示",
    "城门口贴着一张寻人告示：某家族悬赏百块灵石寻找一名离家历练的子弟，最后出现在城西山林。",
    [
        _c("揭榜寻人", next_event={
            "desc": "你在城西山林搜寻数日，终于在一处山洞外发现有人活动的痕迹。",
            "choices": [
                _c("入洞查探", condition=_cond("fortune", 6), rewards={"spirit_stones": 100, "reputation": 30}, flavor="洞中正是那名子弟，他随你回城，家族如约付赏。灵石 +100，声望 +30"),
                _c("入洞查探", rewards={"lifespan": -3, "spirit_stones": 40}, flavor="洞中是一伙散修，你险些冲突，勉强脱身，只拿到部分赏金。寿元 -3，灵石 +40"),
                _c("在洞外呼喊姓名", condition=_cond("comprehension", 6), rewards={"spirit_stones": 90, "reputation": 25}, flavor="你以智取，先喊话表明来意，对方放心出洞，你顺利完成任务。灵石 +90，声望 +25"),
                _c("在洞外呼喊姓名", rewards={"spirit_stones": 30}, flavor="无人应答，你只好扩大范围再找，最终在别处找到，赏金打折。灵石 +30"),
            ]
        }),
        _c("不揭榜，离开", rewards={}, flavor="你对此事无兴趣，径自离开。"),
    ]
))

EVENTS.append(_e(
    "鬼市",
    "子夜时分，巷尾支起零星摊位，灯火昏黄。据说此地是鬼市，真假货混杂，全凭眼力。",
    [
        _c("在鬼市闲逛淘宝", next_event={
            "desc": "你走过几个摊位，有残破法器、不明丹药、古旧玉简，价格高低不一。",
            "choices": [
                _c("买下一块古旧玉简", condition=_cond("fortune", 7), rewards={"spirit_stones": -40, "cultivation": 100}, flavor="玉简中竟是一门残缺心法，你修炼后修为大进。灵石 -40，修为 +100"),
                _c("买下一块古旧玉简", rewards={"spirit_stones": -40}, flavor="玉简内容残缺无用，你当交了学费。灵石 -40"),
                _c("买下一瓶不明丹药", condition=_cond("soul", 6), rewards={"spirit_stones": -30, "lifespan": 15}, flavor="你神识辨出是延寿类丹药，服下有效。灵石 -30，寿元 +15"),
                _c("买下一瓶不明丹药", rewards={"lifespan": -5, "spirit_stones": -30}, flavor="丹药有问题，你服后不适，损了元气。寿元 -5，灵石 -30"),
                _c("什么都不买，只看", rewards={}, flavor="你逛了一圈，未敢下手，安然离开。"),
            ]
        }),
        _c("不进鬼市，绕道", rewards={}, flavor="你对鬼市心存戒备，选择绕行。"),
    ]
))

EVENTS.append(_e(
    "灵植园",
    "一片灵田被篱笆围起，田中灵稻、灵蔬长势喜人。守园的老农见你张望，道：「想买灵米可以，想偷可不行。」",
    [
        _c("提出购买灵米", next_event={
            "desc": "老农领你到仓房，打开几袋灵米任你挑选。「上品五十灵石一斗，中品二十。」",
            "choices": [
                _c("买一斗上品灵米", condition=_cond("fortune", 6), rewards={"spirit_stones": -50, "lifespan": 20, "cultivation": 40}, flavor="上品灵米灵气充沛，你食用后寿元与修为皆有增益。灵石 -50，寿元 +20，修为 +40"),
                _c("买一斗上品灵米", rewards={"spirit_stones": -50, "cultivation": 30}, flavor="上品灵米物有所值。灵石 -50，修为 +30"),
                _c("买中品灵米，讨价还价", condition=_cond("comprehension", 6), rewards={"spirit_stones": -15, "cultivation": 25}, flavor="你说动老农让价，以十五灵石买了一斗中品。灵石 -15，修为 +25"),
                _c("买中品灵米，讨价还价", rewards={"spirit_stones": -20, "cultivation": 20}, flavor="老农不肯让价，你按原价买了一斗。灵石 -20，修为 +20"),
            ]
        }),
        _c("提出帮忙干活换灵米", condition=_cond("physique", 6), rewards={"physique": 1, "spirit_stones": 25}, flavor="你干了一日农活，老农赠你些灵米和一点灵石。体魄 +1，灵石 +25"),
        _c("提出帮忙干活换灵米", rewards={"spirit_stones": 15}, flavor="老农让你帮忙浇水除草，给了你一点灵米抵工。灵石 +15"),
        _c("不买，离开", rewards={}, flavor="你婉拒后离开灵植园。"),
    ]
))

EVENTS.append(_e(
    "剑冢",
    "荒谷中插满残剑断刃，风吹过时嗡鸣阵阵。据说此地是古时剑修葬剑之处，有缘人可感应到剑意。",
    [
        _c("步入剑冢感应", next_event={
            "desc": "你穿行于剑林之间，有的剑毫无反应，有的微微震颤。深处有一柄锈剑，剑身隐约有光。",
            "choices": [
                _c("尝试拔取锈剑", condition=_cond("fortune", 7), rewards={"bone": 1, "cultivation": 80}, flavor="锈剑认主，剑意淬体，你根骨与修为皆进。根骨 +1，修为 +80"),
                _c("尝试拔取锈剑", rewards={"lifespan": -5}, flavor="锈剑反噬，你被剑意所伤。寿元 -5"),
                _c("只在外围感悟剑意", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 50}, flavor="你未贪心深入，在外围静悟，神识与修为皆有收获。神识 +1，修为 +50"),
                _c("只在外围感悟剑意", rewards={"cultivation": 30}, flavor="剑意杂乱，你只悟得零碎。修为 +30"),
            ]
        }),
        _c("取走一柄无主断剑", rewards={"spirit_stones": 45}, flavor="你挑了一柄材质尚可的断剑，到城中卖了炼器铺。灵石 +45"),
        _c("不敢久留，退出", rewards={}, flavor="剑冢杀意凛然，你及时退出。"),
    ]
))

EVENTS.append(_e(
    "雷雨遇险",
    "赶路时忽然雷雨大作，你躲进一处山檐下。闪电接连劈落，不远处一株古树被击中，树身焦黑却隐隐有灵光闪烁。",
    [
        _c("雨停后去查看焦树", next_event={
            "desc": "你走近焦树，发现树心处有一块雷击木，蕴含雷灵之气。取之需破开焦壳。",
            "choices": [
                _c("破开焦壳取雷击木", condition=_cond("physique", 7), rewards={"spirit_stones": 120, "physique": 1}, flavor="你成功取出雷击木，体魄在雷气余韵中有所淬炼。灵石 +120，体魄 +1"),
                _c("破开焦壳取雷击木", rewards={"lifespan": -6, "spirit_stones": 60}, flavor="焦壳内残存雷力，你被电伤，只取到半块。寿元 -6，灵石 +60"),
                _c("只取表面一小块", rewards={"spirit_stones": 50}, flavor="你谨慎取了一小块，未触雷力。灵石 +50"),
            ]
        }),
        _c("在檐下打坐，借雷意悟道", condition=_cond("comprehension", 7), rewards={"comprehension": 1, "cultivation": 60}, flavor="你在雷雨中感悟天地之威，悟性与修为皆进。悟性 +1，修为 +60"),
        _c("在檐下打坐，借雷意悟道", rewards={"cultivation": 30}, flavor="雷意难捉摸，你略有所得。修为 +30"),
        _c("雨停后直接赶路", rewards={}, flavor="你未理会焦树，继续行程。"),
    ]
))

EVENTS.append(_e(
    "渡劫观礼",
    "远处山头雷云密布，有人正在渡劫。不少修士在安全处观望，有人低声道：「若能从中悟出一二，对日后破境大有裨益。」",
    [
        _c("静心观摩天劫", next_event={
            "desc": "雷劫一道接一道落下，渡劫者或挡或扛，你全神贯注，试图捕捉其中道韵。",
            "choices": [
                _c("专注感悟雷劫中的道韵", condition=_cond("comprehension", 7), rewards={"comprehension": 1, "cultivation": 80}, flavor="你从雷劫中悟出一丝天道至理，悟性与修为皆进。悟性 +1，修为 +80"),
                _c("专注感悟雷劫中的道韵", rewards={"cultivation": 50}, flavor="道韵玄奥，你只抓住一点余韵。修为 +50"),
                _c("观察渡劫者的应对之法", condition=_cond("soul", 6), rewards={"soul": 1, "cultivation": 60}, flavor="你从渡劫者的应对中有所领悟，神识与修为皆有收获。神识 +1，修为 +60"),
                _c("观察渡劫者的应对之法", rewards={"cultivation": 35}, flavor="你学到些皮毛。修为 +35"),
            ]
        }),
        _c("怕被波及，退得更远", rewards={}, flavor="你退到更远处，未再观望。"),
    ]
))

EVENTS.append(_e(
    "坊市冲突",
    "坊市中两伙人争执起来，一方说对方卖假货，另一方说对方故意找茬。眼看就要动手，周围摊主纷纷收摊。",
    [
        _c("上前劝架", next_event={
            "desc": "你挤进人群，试图分开双方。其中一人瞪着你道：「关你何事？」",
            "choices": [
                _c("提议请坊市执事仲裁", condition=_cond("reputation", 25), rewards={"reputation": 20, "spirit_stones": 30}, flavor="你的声望让双方愿意听你一句，执事到场后纠纷平息，有人谢你。声望 +20，灵石 +30"),
                _c("提议请坊市执事仲裁", rewards={"reputation": 5}, flavor="双方勉强同意，你抽身离开。声望 +5"),
                _c("自掏腰包补差价息事宁人", condition=_cond("fortune", 6), rewards={"spirit_stones": -35, "reputation": 25}, flavor="你出了点灵石摆平双方，众人赞你大气。灵石 -35，声望 +25"),
                _c("自掏腰包补差价息事宁人", rewards={"spirit_stones": -20}, flavor="你补了部分差价，争执暂歇。灵石 -20"),
            ]
        }),
        _c("绕道离开，不掺和", rewards={}, flavor="你不想惹事，从旁绕行。"),
    ]
))

EVENTS.append(_e(
    "灵舟渡江",
    "江边有灵舟待客，船公道：「对岸有灵脉支脉，不少道友去那边历练。十灵石一位，凑齐五人开船。」",
    [
        _c("付灵石上船", next_event={
            "desc": "灵舟行至江心，忽然水浪翻涌，似有妖兽在船底游动。船公脸色大变。",
            "choices": [
                _c("与船公联手御敌", condition=_cond("physique", 7), rewards={"spirit_stones": 60, "physique": 1}, flavor="你与船公击退水兽，船公免了你的船资并赠谢礼。灵石 +60，体魄 +1"),
                _c("与船公联手御敌", rewards={"lifespan": -5, "spirit_stones": 20}, flavor="你受了些伤，灵舟勉强靠岸，船公退你部分船资。寿元 -5，灵石 +20"),
                _c("以神识探查水下，指引船公避让", condition=_cond("soul", 6), rewards={"soul": 1, "spirit_stones": 45}, flavor="你以神识探路，灵舟有惊无险靠岸，船公感激赠礼。神识 +1，灵石 +45"),
                _c("以神识探查水下，指引船公避让", rewards={"spirit_stones": 30}, flavor="你尽力指引，灵舟脱险，船公退你部分船资。灵石 +30"),
            ]
        }),
        _c("不乘船，沿江步行", rewards={"lifespan": -2}, flavor="你沿江绕行，多花了不少时日。寿元 -2"),
        _c("改日再来", rewards={}, flavor="你暂不渡江，转身离开。"),
    ]
))

EVENTS.append(_e(
    "古琴遗音",
    "废亭中放着一张古琴，琴弦已断了两根，琴身布满灰尘。你轻轻一触，残弦竟发出一声清鸣，久久不散。",
    [
        _c("试着拨动残弦", next_event={
            "desc": "琴音一起，你心神随之震荡。若心静，可与之共鸣；若心乱，反受其扰。",
            "choices": [
                _c("凝神静心，与琴音相和", condition=_cond("soul", 7), rewards={"soul": 1, "cultivation": 70}, flavor="你与古琴遗音共鸣，神识与修为皆进。神识 +1，修为 +70"),
                _c("凝神静心，与琴音相和", rewards={"cultivation": 40}, flavor="琴音玄妙，你略有所得。修为 +40"),
                _c("以自身灵力注入琴身", condition=_cond("fortune", 6), rewards={"fortune": 1, "lifespan": 10}, flavor="古琴吸收灵力后，反馈你一丝生机。机缘 +1，寿元 +10"),
                _c("以自身灵力注入琴身", rewards={"lifespan": 5}, flavor="古琴吸收灵力后，琴身微暖，你略感舒泰。寿元 +5"),
            ]
        }),
        _c("将古琴带走", condition=_cond("physique", 6), rewards={"spirit_stones": 80}, flavor="古琴沉重，你费力带走，到城中卖与乐坊。灵石 +80"),
        _c("将古琴带走", rewards={"lifespan": -2}, flavor="搬运时琴身磕碰，你心神莫名一痛。寿元 -2"),
        _c("不动古琴，离去", rewards={}, flavor="你未再动古琴，悄然离开。"),
    ]
))

EVENTS.append(_e(
    "灵酒窖",
    "山脚有一处废弃酒窖，门半掩着，窖内飘出浓郁酒香。据说此地曾酿灵酒，荒废后偶有修士来寻残酒。",
    [
        _c("入窖搜寻", next_event={
            "desc": "窖内昏暗，你摸到几只酒坛，有的已空，有的尚有残酒。还有一坛封泥完好，沉在角落。",
            "choices": [
                _c("启封那坛完好的酒", condition=_cond("fortune", 6), rewards={"lifespan": 15, "cultivation": 50}, flavor="竟是陈年灵酒，你饮后神清气爽，寿元与修为皆增。寿元 +15，修为 +50"),
                _c("启封那坛完好的酒", rewards={"lifespan": -3}, flavor="酒已变质，你饮后腹痛，损了元气。寿元 -3"),
                _c("只取残酒尝一口", condition=_cond("physique", 6), rewards={"physique": 1, "cultivation": 30}, flavor="残酒中仍有一丝灵性，你体魄与修为略增。体魄 +1，修为 +30"),
                _c("只取残酒尝一口", rewards={"cultivation": 20}, flavor="残酒寡淡，聊胜于无。修为 +20"),
            ]
        }),
        _c("不进去，只在门口闻闻", rewards={"lifespan": 5}, flavor="酒香沁人，你深吸几口，精神稍振。寿元 +5"),
        _c("离开酒窖", rewards={}, flavor="你未入窖，径自离开。"),
    ]
))

EVENTS.append(_e(
    "毒虫巢穴",
    "树根下有一个碗口大的洞穴，洞口爬满紫黑色毒虫，腥气扑鼻。据说巢穴深处有时会凝出解毒灵珠。",
    [
        _c("设法取灵珠", next_event={
            "desc": "你以灵力驱散部分毒虫，探手入洞。洞壁黏滑，深处隐约有微光。",
            "choices": [
                _c("深入取珠", condition=_cond("physique", 7), rewards={"spirit_stones": 100, "bone": 1}, flavor="你强忍毒气取到灵珠，根骨在抗毒中有所淬炼。灵石 +100，根骨 +1"),
                _c("深入取珠", rewards={"lifespan": -10, "spirit_stones": 40}, flavor="毒气侵体，你勉强取到一颗小珠，带伤退出。寿元 -10，灵石 +40"),
                _c("以火驱虫再取", condition=_cond("comprehension", 6), rewards={"spirit_stones": 80, "cultivation": 40}, flavor="你以火诀驱虫，顺利取珠，并从中悟出些控火心得。灵石 +80，修为 +40"),
                _c("以火驱虫再取", rewards={"lifespan": -4, "spirit_stones": 30}, flavor="火势惊动虫群，你被蜇了几口，只取到残珠。寿元 -4，灵石 +30"),
            ]
        }),
        _c("不冒险，离开", rewards={}, flavor="你不想招惹毒虫，绕道离开。"),
    ]
))

EVENTS.append(_e(
    "幻阵迷途",
    "你明明沿大路走，却不知何时进入一片白雾，兜转许久又回到原地。像是误入了某种幻阵。",
    [
        _c("静心感应阵眼", next_event={
            "desc": "你闭目以神识探查，雾中隐约有几点灵光闪烁，似是阵基。",
            "choices": [
                _c("朝最亮的一处灵光走去", condition=_cond("soul", 7), rewards={"soul": 1, "cultivation": 70}, flavor="你破开幻象，找到阵眼所在，神识与修为皆进。神识 +1，修为 +70"),
                _c("朝最亮的一处灵光走去", rewards={"lifespan": -5}, flavor="那处是陷阱，你陷入更深一层幻境，耗费良久才脱身。寿元 -5"),
                _c("以力破阵，胡乱出招", condition=_cond("physique", 7), rewards={"physique": 1}, flavor="你蛮力轰击，竟误打误撞震散部分阵基，脱困而出。体魄 +1"),
                _c("以力破阵，胡乱出招", rewards={"lifespan": -8}, flavor="你消耗巨大却未破阵，精疲力竭。寿元 -8"),
            ]
        }),
        _c("原地打坐，等阵势自消", condition=_cond("fortune", 6), rewards={"cultivation": 50}, flavor="不知过了多久，雾散阵消，你趁机感悟到一丝阵法余韵。修为 +50"),
        _c("原地打坐，等阵势自消", rewards={"lifespan": -3}, flavor="你等了很久才脱困，略感疲惫。寿元 -3"),
        _c("不再乱走，保存体力", rewards={}, flavor="你索性坐下不动，最终雾散，你安然离开。"),
    ]
))

EVENTS.append(_e(
    "前辈洞府",
    "山腰有一处被藤蔓遮掩的洞府，石门半开，内里幽深。门侧刻着「有缘者入，贪者慎之」。",
    [
        _c("入内探访", next_event={
            "desc": "洞府内石床、石桌尚在，已无主人。墙角有一口小箱，桌上有一枚玉简。",
            "choices": [
                _c("先取玉简查看", condition=_cond("comprehension", 7), rewards={"comprehension": 1, "cultivation": 100}, flavor="玉简中是前辈的修炼心得，你悟性大进，修为亦有收获。悟性 +1，修为 +100"),
                _c("先取玉简查看", rewards={"cultivation": 60}, flavor="玉简内容深奥，你只读懂部分。修为 +60"),
                _c("先开箱取物", condition=_cond("fortune", 6), rewards={"spirit_stones": 120, "fortune": 1}, flavor="箱中是灵石与一件小法器，你收获颇丰。灵石 +120，机缘 +1"),
                _c("先开箱取物", rewards={"lifespan": -5}, flavor="箱上有禁制，你触发了机关，受了轻伤。寿元 -5"),
                _c("对遗物行礼后只取玉简", rewards={"reputation": 15, "cultivation": 50}, flavor="你恭敬行礼后只取玉简，心有所得，冥冥中似有福报。声望 +15，修为 +50"),
            ]
        }),
        _c("只在门口观望不入", rewards={"fortune": 1}, flavor="你未贪心，记下位置后离开，心境平和。机缘 +1"),
        _c("离开，不打扰前辈清静", rewards={}, flavor="你合十行礼后离开。"),
    ]
))

EVENTS.append(_e(
    "灵宠走失",
    "一名女修焦急地在路边张望，见你就问：「道友可曾见到一只雪白的灵狐？它偷跑出来，我找了好久。」",
    [
        _c("答应帮忙寻找", next_event={
            "desc": "你与她分头寻找。不久你在灌木丛中听到窸窣声，拨开一看，正是那只灵狐。",
            "choices": [
                _c("轻声引诱，抱回灵狐", condition=_cond("fortune", 6), rewards={"reputation": 25, "spirit_stones": 50}, flavor="灵狐温顺地跟你回去，女修感激涕零，赠你灵石与谢意。声望 +25，灵石 +50"),
                _c("轻声引诱，抱回灵狐", rewards={"reputation": 15}, flavor="灵狐跟你回去，女修连连道谢。声望 +15"),
                _c("强行抓住灵狐", condition=_cond("physique", 6), rewards={"reputation": 10, "spirit_stones": 20}, flavor="灵狐挣扎间抓伤了你，但你还是送回去了，女修谢意一般。声望 +10，灵石 +20"),
                _c("强行抓住灵狐", rewards={"lifespan": -2, "reputation": 5}, flavor="灵狐反抗激烈，你受了些伤，女修略有不悦。寿元 -2，声望 +5"),
            ]
        }),
        _c("说没看见，继续赶路", rewards={}, flavor="你未多事，摇头离开。"),
    ]
))

EVENTS.append(_e(
    "当铺鉴宝",
    "当铺掌柜拿着一件顾客寄售的法器发愁：「这东西有人说是古物，有人说是仿品，老夫眼力有限，敢请道友帮忙掌眼。」",
    [
        _c("接过法器细看", next_event={
            "desc": "法器是一面铜镜，背面符文斑驳。你以神识探查，感应其内灵气流转。",
            "choices": [
                _c("断定是古物，建议高价", condition=_cond("soul", 7), rewards={"soul": 1, "spirit_stones": 60}, flavor="你判断无误，掌柜按你的建议售出，分你酬劳。神识 +1，灵石 +60"),
                _c("断定是古物，建议高价", rewards={"reputation": -10}, flavor="你判断有误，实为仿品，掌柜亏了钱，对你颇有微词。声望 -10"),
                _c("说是仿品，建议低价", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "spirit_stones": 40}, flavor="你看出破绽，掌柜按你的建议定价，避免损失，赠你谢礼。悟性 +1，灵石 +40"),
                _c("说是仿品，建议低价", rewards={"spirit_stones": 20}, flavor="掌柜半信半疑，最终低价售出，给你一点辛苦费。灵石 +20"),
            ]
        }),
        _c("推说不懂，婉拒", rewards={}, flavor="你婉拒后离开当铺。"),
    ]
))

EVENTS.append(_e(
    "灵药失窃",
    "药园主人拦住你，怒道：「我家灵药昨夜被偷，有人说是往这边跑的。你可曾见过可疑之人？」",
    [
        _c("否认并愿意帮忙搜查", next_event={
            "desc": "药园主人见你态度诚恳，语气稍缓：「那贼人修为不高，若你能帮我寻回灵药，必有重谢。」你答应在附近搜查。",
            "choices": [
                _c("沿小路追踪", condition=_cond("soul", 6), rewards={"spirit_stones": 70, "reputation": 20}, flavor="你以神识捕捉到残留气息，追回部分灵药，园主酬谢。灵石 +70，声望 +20"),
                _c("沿小路追踪", rewards={"reputation": 5}, flavor="你搜了一圈未果，园主叹气作罢。声望 +5"),
                _c("在岔路口蹲守", condition=_cond("fortune", 6), rewards={"fortune": 1, "spirit_stones": 50}, flavor="你守到贼人再次现身，将其擒获，灵药追回。机缘 +1，灵石 +50"),
                _c("在岔路口蹲守", rewards={"lifespan": -2}, flavor="你守了一夜无果，疲惫不堪。寿元 -2"),
            ]
        }),
        _c("坚称不知情，要求离开", condition=_cond("physique", 6), rewards={}, flavor="园主打量你一番，侧身让路。"),
        _c("坚称不知情，要求离开", rewards={"reputation": -15}, flavor="园主疑心未消，记下你的形貌，你名声受损。声望 -15"),
        _c("主动让园主搜身以证清白", rewards={"reputation": 20}, flavor="园主搜后道歉，对你印象大好。声望 +20"),
    ]
))

EVENTS.append(_e(
    "风水先生",
    "路边一位风水先生正在为人看宅，见你路过，忽然道：「这位道友，你印堂发暗，近日恐有小人缠身。可要卜一卦？」",
    [
        _c("付钱卜卦", next_event={
            "desc": "风水先生掐指推演，又观你面相，道：「三日内勿往东南，可避一劫。若往西北，或有小喜。」",
            "choices": [
                _c("依言三日内往西北", condition=_cond("fortune", 6), rewards={"fortune": 1, "spirit_stones": 60}, flavor="你在西北方向偶得一处小机缘，灵石与气运皆增。机缘 +1，灵石 +60"),
                _c("依言三日内往西北", rewards={"spirit_stones": 30}, flavor="你往西北走了一趟，小有收获。灵石 +30"),
                _c("偏要往东南一探", condition=_cond("physique", 7), rewards={"physique": 1}, flavor="你在东南遇险但化险为夷，体魄在应对中有所提升。体魄 +1"),
                _c("偏要往东南一探", rewards={"lifespan": -6}, flavor="你在东南遭遇麻烦，受伤而归。寿元 -6"),
            ]
        }),
        _c("不信，一笑而过", rewards={}, flavor="你未理会，径自离开。"),
    ]
))

EVENTS.append(_e(
    "画中秘境",
    "古宅中挂着一幅山水画，画中云雾缭绕，似有修士御剑飞行。你凝神细看，竟觉画中景物在微微流动。",
    [
        _c("以神识探入画中", next_event={
            "desc": "你的神识触及画境的刹那，一股吸力传来。再睁眼时，你已站在画中山道上。",
            "choices": [
                _c("在画境中寻找出路", condition=_cond("comprehension", 7), rewards={"comprehension": 1, "cultivation": 90}, flavor="你参破画境规律，安然脱出，悟性与修为皆进。悟性 +1，修为 +90"),
                _c("在画境中寻找出路", rewards={"lifespan": -5, "cultivation": 40}, flavor="你在画境中困了许久才找到出口，略损元气。寿元 -5，修为 +40"),
                _c("在画境中采摘灵草", condition=_cond("fortune", 6), rewards={"spirit_stones": 100, "fortune": 1}, flavor="画境中灵草颇多，你采了一些后寻路离开，收获不菲。灵石 +100，机缘 +1"),
                _c("在画境中采摘灵草", rewards={"spirit_stones": 50}, flavor="你采了些灵草，寻路离开时已所剩无几。灵石 +50"),
            ]
        }),
        _c("不再深看，移开视线", rewards={}, flavor="你怕陷入画境，及时收神离开。"),
    ]
))
