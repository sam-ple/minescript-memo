import minescript as m


# ==================================================
# 共通関数
# ==================================================

def add_trade(tag, buy_item, buy_count, sell_item, sell_count):
    m.execute(
        f'/data modify entity @e[type=villager,tag={tag},limit=1] '
        f'Offers.Recipes append value '
        f'{{buy:{{id:"{buy_item}",count:{buy_count}}},'
        f'sell:{{id:"{sell_item}",count:{sell_count}}},'
        f'maxUses:1000}}'
    )


def set_name(tag, trade_index, name):
    m.execute(
        f'/data modify entity '
        f'@e[type=villager,tag={tag},limit=1] '
        f'Offers.Recipes[{trade_index}].sell.components."minecraft:custom_name" '
        f'set value "{name}"'
    )


def add_lore(tag, trade_index, text):
    m.execute(
        f'/data modify entity '
        f'@e[type=villager,tag={tag},limit=1] '
        f'Offers.Recipes[{trade_index}].sell.components."minecraft:lore" '
        f'append value "{text}"'
    )


def set_damage(tag, trade_index, damage):
    m.execute(
        f'/data modify entity '
        f'@e[type=villager,tag={tag},limit=1] '
        f'Offers.Recipes[{trade_index}].sell.components."minecraft:damage" '
        f'set value {damage}'
    )


# ==================================================
# 初期化
# ==================================================

m.execute('/kill @e[type=villager,tag=shop_test]')


# ==================================================
# 戦闘村人
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
    'Tags:["shop_test"]'
    '}'
)


# ==================================================
# 弓
# ==================================================

add_trade(
    "shop_test",
    "emerald", 2,
    "bow", 1
)

set_name(
    "shop_test",
    0,
    "一発で壊れる弓"
)

set_damage(
    "shop_test",
    0,
    383
)

add_lore(
    "shop_test",
    0,
    "人狼RPG専用武器"
)

add_lore(
    "shop_test",
    0,
    "一度使うと壊れる"
)

# import minescript as m

# # ==================================================
# # テスト村人
# # ==================================================

# m.execute('/kill @e[type=villager]')

# m.execute(
#     '/summon villager ~ ~ ~ '
#     '{'
#     'VillagerData:{level:5,profession:"farmer",type:"plains"},'
#     'CustomName:"戦闘",'
#     'CustomNameVisible:true,'
#     'Silent:1b,'
#     'Invulnerable:1b,'
#     'NoAI:1b,'
#     'Tags:["shop_test"]'
#     '}'
# )

# # ==================================================
# # 弓
# # 名前 + Damage + Lore 1行
# # ==================================================

# m.execute(
#     '/data modify entity @e[type=villager,tag=shop_test,limit=1] '
#     'Offers.Recipes append value '
#     '{'
#     'buy:{id:"emerald",count:2},'
#     'sell:{'
#     'id:"bow",'
#     'count:1,'
#     'components:{'
#     '"minecraft:damage":383,'
#     '"minecraft:custom_name":"一発で壊れる弓",'
#     '"minecraft:lore":["人狼RPG専用武器"]'
#     '}'
#     '},'
#     'maxUses:1000'
#     '}'
# )

# # ==================================================
# # Lore 2行目を追加
# # ==================================================

# m.execute(
#     '/data modify entity '
#     '@e[type=villager,tag=shop_test,limit=1] '
#     'Offers.Recipes[0].sell.components."minecraft:lore" '
#     'append value "一度使うと壊れる"'
# )
