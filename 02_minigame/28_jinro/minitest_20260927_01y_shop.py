import minescript as m


# ==================================================
# Jinro RPG Shop Mini Test
#
# 戦闘ショップ
#   tag = battle
#   distance = 5
#
# 補助ショップ
#   tag = support
#   distance = 5
#
# ==================================================


# ==================================================
# 設定
# ==================================================

SHOP_DISTANCE = 5


# ==================================================
# 村人検索
# ==================================================

def villager_selector(tag):
    return (
        f'@e[type=villager,tag={tag},'
        f'distance=..{SHOP_DISTANCE},'
        f'sort=nearest,limit=1]'
    )


# ==================================================
# 取引追加
# ==================================================

def add_trade(tag, buy_item, buy_count, sell_item, sell_count):

    selector = villager_selector(tag)

    m.execute(
        f'/data modify entity {selector} '
        f'Offers.Recipes append value '
        f'{{buy:{{id:"{buy_item}",count:{buy_count}}},'
        f'sell:{{id:"{sell_item}",count:{sell_count}}},'
        f'maxUses:1000}}'
    )


# ==================================================
# アイテム名
# ==================================================

def set_name(tag, trade_index, name):

    selector = villager_selector(tag)

    m.execute(
        f'/data modify entity {selector} '
        f'Offers.Recipes[{trade_index}].sell.components."minecraft:custom_name" '
        f'set value "{name}"'
    )


# ==================================================
# Lore追加
# ==================================================

def add_lore(tag, trade_index, text):

    selector = villager_selector(tag)

    m.execute(
        f'/data modify entity {selector} '
        f'Offers.Recipes[{trade_index}].sell.components."minecraft:lore" '
        f'append value "{text}"'
    )


# ==================================================
# 耐久値
# ==================================================

def set_damage(tag, trade_index, damage):

    selector = villager_selector(tag)

    m.execute(
        f'/data modify entity {selector} '
        f'Offers.Recipes[{trade_index}].sell.components."minecraft:damage" '
        f'set value {damage}'
    )


# ==================================================
# エンチャント
# ==================================================

def set_enchantment(tag, trade_index, enchantment, level):

    selector = villager_selector(tag)

    m.execute(
        f'/data modify entity {selector} '
        f'Offers.Recipes[{trade_index}].sell.components."minecraft:enchantments" '
        f'set value {{levels:{{"{enchantment}":{level}}}}}'
    )


# ==================================================
# テスト用村人削除
# ==================================================

m.execute('/kill @e[type=villager,tag=battle]')
m.execute('/kill @e[type=villager,tag=support]')


# ==================================================
# 戦闘村人召喚
# ==================================================

m.execute(
    '/summon villager ~ ~ ~ '
    '{'
    'VillagerData:{level:5,profession:"farmer",type:"plains"},'
    'CustomName:"戦闘",'
    'CustomNameVisible:true,'
    'Silent:1b,'
    'Invulnerable:1b,'
    'NoAI:1b,'
    'Tags:["battle"]'
    '}'
)


# ==================================================
# 戦闘ショップ
#
# トライデント
# ==================================================

add_trade(
    "battle",
    "emerald", 2,
    "trident", 1
)


# 名前
set_name(
    "battle",
    0,
    "忠誠のトライデント"
)


# 耐久
set_damage(
    "battle",
    0,
    248
)


# 忠誠 III
set_enchantment(
    "battle",
    0,
    "minecraft:loyalty",
    3
)


# 説明1
add_lore(
    "battle",
    0,
    "人狼RPG専用武器"
)


# 説明2
add_lore(
    "battle",
    0,
    "忠誠 III"
)
