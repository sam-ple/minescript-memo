import minescript as m

# ==================================================
# テスト村人
# ==================================================

m.execute('/kill @e[type=villager]')

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
# 名前 + Damage + Lore 1行
# ==================================================

m.execute(
    '/data modify entity @e[type=villager,tag=shop_test,limit=1] '
    'Offers.Recipes append value '
    '{'
    'buy:{id:"emerald",count:2},'
    'sell:{'
    'id:"bow",'
    'count:1,'
    'components:{'
    '"minecraft:damage":383,'
    '"minecraft:custom_name":"一発で壊れる弓",'
    '"minecraft:lore":["人狼RPG専用武器"]'
    '}'
    '},'
    'maxUses:1000'
    '}'
)

# ==================================================
# Lore 2行目を追加
# ==================================================

m.execute(
    '/data modify entity '
    '@e[type=villager,tag=shop_test,limit=1] '
    'Offers.Recipes[0].sell.components."minecraft:lore" '
    'append value "一度使うと壊れる"'
)
