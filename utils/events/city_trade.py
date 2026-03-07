from utils.events._base import _e, _c, _cond

EVENTS = []

EVENTS.append(_e(
    "万宝楼月拍",
    "万宝楼今日举行月度大拍卖，门口人山人海，各路修士携带珍宝而来，空气中弥漫着灵气与铜臭味。",
    [
        _c("入场竞拍", next_event={
            "desc": "拍卖台上摆着数件宝物，其中一件散发着淡淡金光的玉瓶引起了你的注意，起拍价一百灵石。",
            "choices": [
                _c("竞拍玉瓶", condition=_cond("fortune", 7), rewards={"spirit_stones": -100, "lifespan": 60, "bone": 1}, flavor="玉瓶内装有一枚延寿丹，服下后寿元大涨，根骨也得到了滋养。灵石 -100，寿元 +60，根骨 +1"),
                _c("竞拍玉瓶", rewards={"spirit_stones": -100, "lifespan": 30}, flavor="玉瓶内是一枚普通延寿丹，略有补益。灵石 -100，寿元 +30"),
                _c("竞拍其他宝物", condition=_cond("comprehension", 6), rewards={"spirit_stones": -80, "cultivation": 150}, flavor="你以独到眼光拍下了一件被低估的修炼宝物，大赚一笔。灵石 -80，修为 +150"),
                _c("竞拍其他宝物", rewards={"spirit_stones": -60, "cultivation": 80}, flavor="你拍下了一件修炼辅助宝物，有些收获。灵石 -60，修为 +80"),
            ]
        }),
        _c("在场外打探消息", condition=_cond("fortune", 6), rewards={"fortune": 1, "spirit_stones": 80}, flavor="你从人群中打探到了一条内幕消息，转手卖出赚了一笔。机缘 +1，灵石 +80"),
        _c("在场外打探消息", rewards={"spirit_stones": 30}, flavor="你打探到了一些普通消息，略有收获。灵石 +30"),
        _c("不感兴趣，离开", rewards={}, flavor="你对拍卖不感兴趣，继续赶路。"),
    ],
    city="万宝楼"
))

EVENTS.append(_e(
    "沙罗城情报贩子",
    "沙罗城的茶馆角落里，一名神色鬼祟的修士正在低声兜售各方势力的情报，声称无所不知。",
    [
        _c("购买情报", next_event={
            "desc": "情报贩子压低声音说：「最近有一支商队要经过漠北，携带大量灵石，但护卫不多。」",
            "choices": [
                _c("打劫商队", condition=_cond("physique", 8), rewards={"spirit_stones": 200, "reputation": -50}, flavor="你成功打劫了商队，但此举大损声望。灵石 +200，声望 -50"),
                _c("打劫商队", rewards={"lifespan": -20, "reputation": -30}, flavor="商队护卫比情报说的多，你被打得落荒而逃。寿元 -20，声望 -30"),
                _c("通风报信给商队", condition=_cond("fortune", 6), rewards={"spirit_stones": 100, "reputation": 40, "fortune": 1}, flavor="商队感激你的通报，给了你丰厚酬谢，机缘也有所提升。灵石 +100，声望 +40，机缘 +1"),
                _c("通风报信给商队", rewards={"spirit_stones": 60, "reputation": 25}, flavor="商队给了你一些酬谢。灵石 +60，声望 +25"),
            ]
        }),
        _c("拒绝，不想惹麻烦", rewards={}, flavor="你拒绝了，继续赶路。"),
        _c("反向出卖情报贩子", condition=_cond("soul", 7), rewards={"reputation": 30, "spirit_stones": 50}, flavor="你将情报贩子的行踪告知了城主府，获得了赏金。声望 +30，灵石 +50"),
    ],
    city="沙罗城"
))

EVENTS.append(_e(
    "落云城灵材市场",
    "落云城的灵材市场今日格外热闹，一批来自东海的珍稀灵材刚刚到货，各家商铺门口都排起了长龙。",
    [
        _c("排队购买灵材", next_event={
            "desc": "轮到你时，货架上只剩下两种灵材：一株百年灵芝和一块海底玄铁。",
            "choices": [
                _c("购买百年灵芝", condition=_cond("fortune", 6), rewards={"spirit_stones": -80, "lifespan": 40, "cultivation": 100}, flavor="灵芝品质极佳，服下后寿元和修为都大幅提升。灵石 -80，寿元 +40，修为 +100"),
                _c("购买百年灵芝", rewards={"spirit_stones": -80, "lifespan": 25}, flavor="灵芝略有补益。灵石 -80，寿元 +25"),
                _c("购买海底玄铁", condition=_cond("physique", 6), rewards={"spirit_stones": -60, "bone": 1, "physique": 1}, flavor="玄铁淬体，根骨和体魄都得到了提升。灵石 -60，根骨 +1，体魄 +1"),
                _c("购买海底玄铁", rewards={"spirit_stones": -60, "bone": 1}, flavor="玄铁淬体，根骨略有提升。灵石 -60，根骨 +1"),
            ]
        }),
        _c("在市场外倒卖消息", condition=_cond("fortune", 7), rewards={"spirit_stones": 100}, flavor="你将到货消息提前卖给了几名修士，赚了一笔中介费。灵石 +100"),
        _c("在市场外倒卖消息", rewards={"spirit_stones": 40}, flavor="你卖出了一些消息，略有收获。灵石 +40"),
        _c("不感兴趣，离开", rewards={}, flavor="你继续赶路。"),
    ],
    city="落云城"
))

EVENTS.append(_e(
    "北冥港海货交易",
    "北冥港今日有一批深海灵材到港，码头上热闹非凡，各路商人和修士争相抢购。",
    [
        _c("抢购深海灵材", next_event={
            "desc": "你挤进人群，发现有一颗深海灵珠和一瓶海妖精血，价格都不菲。",
            "choices": [
                _c("购买深海灵珠", condition=_cond("fortune", 7), rewards={"spirit_stones": -120, "soul": 1, "lifespan": 30}, flavor="灵珠品质极佳，神识和寿元都大幅提升。灵石 -120，神识 +1，寿元 +30"),
                _c("购买深海灵珠", rewards={"spirit_stones": -120, "lifespan": 20}, flavor="灵珠略有补益。灵石 -120，寿元 +20"),
                _c("购买海妖精血", condition=_cond("physique", 7), rewards={"spirit_stones": -100, "physique": 2, "bone": 1}, flavor="精血淬体，体魄和根骨都得到了蜕变。灵石 -100，体魄 +2，根骨 +1"),
                _c("购买海妖精血", rewards={"spirit_stones": -100, "physique": 1}, flavor="精血淬体，体魄略有提升。灵石 -100，体魄 +1"),
            ]
        }),
        _c("在码头帮忙卸货换报酬", rewards={"spirit_stones": 50, "physique": 1}, flavor="你帮忙卸了半天货，赚了些灵石，体魄也得到了锻炼。灵石 +50，体魄 +1"),
        _c("打听海上奇遇", condition=_cond("fortune", 6), rewards={"fortune": 1, "cultivation": 50}, flavor="你从水手口中听到了一些海上奇遇，机缘略有提升。机缘 +1，修为 +50"),
        _c("不感兴趣，离开", rewards={}, flavor="你继续赶路。"),
    ],
    city="北冥港"
))

EVENTS.append(_e(
    "丹霞谷药材收购",
    "丹霞谷的药材收购站今日开门，一名丹师正在高价收购各类灵草，尤其是百年以上的品种。",
    [
        _c("出售手中灵草", condition=_cond("fortune", 7), rewards={"spirit_stones": 150, "fortune": 1}, flavor="你手中恰好有几株珍稀灵草，卖了个极好的价格，机缘也有所提升。灵石 +150，机缘 +1"),
        _c("出售手中灵草", rewards={"spirit_stones": 80}, flavor="你卖出了一些灵草，收入不菲。灵石 +80"),
        _c("向丹师请教炼丹之道", next_event={
            "desc": "丹师见你诚心求教，放下手中事务，为你讲解了一些炼丹基础。",
            "choices": [
                _c("专心聆听", condition=_cond("comprehension", 7), rewards={"comprehension": 1, "cultivation": 80}, flavor="你从丹师的讲解中悟出了一丝丹道真意，悟性大进。悟性 +1，修为 +80"),
                _c("专心聆听", rewards={"cultivation": 50}, flavor="你学到了一些炼丹知识，修为略有提升。修为 +50"),
                _c("顺手帮丹师整理药材", rewards={"reputation": 20, "spirit_stones": 30}, flavor="丹师感谢你的帮忙，给了你一些报酬。声望 +20，灵石 +30"),
            ]
        }),
        _c("在谷中采集灵草", condition=_cond("fortune", 6), rewards={"spirit_stones": 70}, flavor="你在谷中采集了一批灵草，卖了不少灵石。灵石 +70"),
        _c("在谷中采集灵草", rewards={"spirit_stones": 30}, flavor="你采集了一些普通药材，略有收获。灵石 +30"),
    ],
    city="丹霞谷"
))

EVENTS.append(_e(
    "黄沙镇法器铺",
    "黄沙镇的一家法器铺正在清仓大甩卖，店主说要关门歇业，所有存货半价出售。",
    [
        _c("进店挑选", next_event={
            "desc": "店内法器琳琅满目，你看中了一件防御类法器和一件攻击类法器，但只够买一件。",
            "choices": [
                _c("购买防御法器", condition=_cond("fortune", 6), rewards={"spirit_stones": -80, "physique": 1, "lifespan": 20}, flavor="防御法器品质极佳，穿戴后体魄和寿元都有所提升。灵石 -80，体魄 +1，寿元 +20"),
                _c("购买防御法器", rewards={"spirit_stones": -80, "physique": 1}, flavor="防御法器略有补益。灵石 -80，体魄 +1"),
                _c("购买攻击法器", condition=_cond("comprehension", 6), rewards={"spirit_stones": -80, "cultivation": 100, "bone": 1}, flavor="攻击法器蕴含战意，使用后修为和根骨都有所提升。灵石 -80，修为 +100，根骨 +1"),
                _c("购买攻击法器", rewards={"spirit_stones": -80, "cultivation": 60}, flavor="攻击法器略有补益。灵石 -80，修为 +60"),
            ]
        }),
        _c("打听店主关门原因", condition=_cond("soul", 6), rewards={"fortune": 1, "spirit_stones": 50}, flavor="你从店主口中得知了一个商机，机缘略有提升。机缘 +1，灵石 +50"),
        _c("帮店主搬运货物", rewards={"spirit_stones": 40, "reputation": 15}, flavor="店主感谢你的帮忙，给了你一些报酬。灵石 +40，声望 +15"),
        _c("不感兴趣，离开", rewards={}, flavor="你继续赶路。"),
    ],
    city="黄沙镇"
))

EVENTS.append(_e(
    "赤炎城丹药拍卖",
    "赤炎城的丹师公会今日举行季度丹药拍卖，各类珍稀丹药一字排开，香气扑鼻。",
    [
        _c("竞拍延寿丹", next_event={
            "desc": "延寿丹起拍价一百五十灵石，竞争激烈，价格节节攀升。",
            "choices": [
                _c("不惜代价竞拍", condition=_cond("fortune", 7), rewards={"spirit_stones": -150, "lifespan": 80, "bone": 1}, flavor="你拍得了一枚品质极佳的延寿丹，寿元暴涨，根骨也得到了滋养。灵石 -150，寿元 +80，根骨 +1"),
                _c("不惜代价竞拍", rewards={"spirit_stones": -200, "lifespan": 50}, flavor="你以高价拍得了延寿丹，寿元大涨。灵石 -200，寿元 +50"),
                _c("适可而止，放弃竞拍", rewards={"fortune": 1}, flavor="你放弃了竞拍，但机缘略有提升，说明此丹与你无缘。机缘 +1"),
            ]
        }),
        _c("竞拍修炼丹", condition=_cond("fortune", 6), rewards={"spirit_stones": -100, "cultivation": 200}, flavor="你拍得了一枚修炼丹，修为大进。灵石 -100，修为 +200"),
        _c("竞拍修炼丹", rewards={"spirit_stones": -120, "cultivation": 150}, flavor="你以略高的价格拍得了修炼丹。灵石 -120，修为 +150"),
        _c("只是观摩，不参与竞拍", condition=_cond("comprehension", 6), rewards={"comprehension": 1}, flavor="你从丹药的气息中感悟到了一丝丹道，悟性有所提升。悟性 +1"),
        _c("只是观摩，不参与竞拍", rewards={"cultivation": 30}, flavor="你观摩了一番，略有收获。修为 +30"),
    ],
    city="赤炎城"
))

EVENTS.append(_e(
    "翠微城药农",
    "翠微城郊外，一名老药农正在采集灵草，他见到你后，说自己年迈体衰，愿意以低价出售一批珍稀灵草。",
    [
        _c("购买灵草", next_event={
            "desc": "老药农拿出了三株灵草：一株百年人参、一株千年灵芝、一株罕见的七彩莲花。",
            "choices": [
                _c("购买七彩莲花", condition=_cond("fortune", 8), rewards={"spirit_stones": -100, "fortune": 2, "lifespan": 50}, flavor="七彩莲花极为罕见，服下后机缘大涨，寿元也大幅提升。灵石 -100，机缘 +2，寿元 +50"),
                _c("购买七彩莲花", rewards={"spirit_stones": -100, "lifespan": 30, "fortune": 1}, flavor="七彩莲花略有补益。灵石 -100，寿元 +30，机缘 +1"),
                _c("购买千年灵芝", condition=_cond("physique", 6), rewards={"spirit_stones": -80, "physique": 1, "lifespan": 40}, flavor="千年灵芝滋补，体魄和寿元都大幅提升。灵石 -80，体魄 +1，寿元 +40"),
                _c("购买千年灵芝", rewards={"spirit_stones": -80, "lifespan": 30}, flavor="千年灵芝略有补益。灵石 -80，寿元 +30"),
            ]
        }),
        _c("帮老药农采集灵草", rewards={"spirit_stones": 60, "reputation": 20}, flavor="老药农感谢你的帮忙，给了你一些报酬。灵石 +60，声望 +20"),
        _c("向老药农请教识草之道", condition=_cond("comprehension", 6), rewards={"comprehension": 1, "fortune": 1}, flavor="老药农传授了你一些识别灵草的方法，悟性和机缘都有所提升。悟性 +1，机缘 +1"),
        _c("不感兴趣，离开", rewards={}, flavor="你继续赶路。"),
    ],
    city="翠微城"
))

EVENTS.append(_e(
    "烈风关走私商",
    "烈风关的城门附近，一名鬼鬼祟祟的修士悄悄拉住你，说他有一批从西域深处带来的禁忌灵材，价格公道。",
    [
        _c("查看货物", next_event={
            "desc": "货物中有一瓶妖兽精血和一块来历不明的黑色矿石，散发着奇异的气息。",
            "choices": [
                _c("购买妖兽精血", condition=_cond("physique", 7), rewards={"spirit_stones": -80, "physique": 2, "bone": 1}, flavor="精血淬体效果惊人，体魄和根骨都得到了蜕变。灵石 -80，体魄 +2，根骨 +1"),
                _c("购买妖兽精血", rewards={"spirit_stones": -80, "physique": 1}, flavor="精血淬体，体魄略有提升。灵石 -80，体魄 +1"),
                _c("购买黑色矿石", condition=_cond("soul", 7), rewards={"spirit_stones": -60, "soul": 1, "cultivation": 100}, flavor="矿石蕴含奇异灵气，神识和修为都有所提升。灵石 -60，神识 +1，修为 +100"),
                _c("购买黑色矿石", rewards={"spirit_stones": -60, "cultivation": 60}, flavor="矿石略有补益。灵石 -60，修为 +60"),
            ]
        }),
        _c("举报走私商", condition=_cond("fortune", 6), rewards={"reputation": 40, "spirit_stones": 60}, flavor="你向城门守卫举报了走私商，获得了赏金，声望大涨。声望 +40，灵石 +60"),
        _c("不理会，继续赶路", rewards={}, flavor="你拒绝了，继续赶路。"),
    ],
    city="烈风关"
))

EVENTS.append(_e(
    "归元镇初来乍到",
    "归元镇是中州的门户小镇，你刚踏入此地，便有一名热情的老修士上前搭话，说愿意为你介绍中州的情况。",
    [
        _c("听他介绍", next_event={
            "desc": "老修士滔滔不绝地介绍了中州各大城市的特色，还提到了几处隐秘的修炼宝地。",
            "choices": [
                _c("打听修炼宝地", condition=_cond("fortune", 6), rewards={"fortune": 1, "cultivation": 80}, flavor="老修士告诉了你一处隐秘的灵气汇聚之地，机缘和修为都有所提升。机缘 +1，修为 +80"),
                _c("打听修炼宝地", rewards={"cultivation": 50}, flavor="你得到了一些有用的信息，修为略有提升。修为 +50"),
                _c("打听各大势力情况", condition=_cond("soul", 6), rewards={"soul": 1, "reputation": 20}, flavor="你从老修士口中了解了中州各大势力的格局，神识和声望都有所提升。神识 +1，声望 +20"),
                _c("打听各大势力情况", rewards={"reputation": 15}, flavor="你了解了一些基本情况，声望略有提升。声望 +15"),
            ]
        }),
        _c("婉拒，自己探索", rewards={"fortune": 1}, flavor="你婉拒了老修士，独自踏入中州，机缘略有提升。机缘 +1"),
        _c("给老修士一些灵石答谢", rewards={"spirit_stones": -20, "reputation": 30, "fortune": 1}, flavor="老修士感激不已，额外告诉了你一个重要消息，声望和机缘都有所提升。灵石 -20，声望 +30，机缘 +1"),
    ],
    city="归元镇"
))
