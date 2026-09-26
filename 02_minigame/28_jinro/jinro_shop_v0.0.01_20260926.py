import minescript as m

# ==================================================
# TEST NPC
# 戦闘ショップ
# ==================================================


# ==================================================
# 村人召喚
# ==================================================

m.execute(
    '/summon villager ~ ~ ~ '
    '{'
    'VillagerData:{level:5,profession:"farmer",type:"plains"},'
    'CustomName:"戦闘",'
    'CustomNameVisible:true,'
    'Silent:1b,'
    'Invulnerable:1b,'
    'NoAI:1b'
    '}'
)


# ==================================================
# 取引①
# ==================================================

m.execute(
    '/data modify entity @e[type=villager,limit=1,sort=nearest] '
    'Offers.Recipes append value '
    '{buy:{id:"emerald",count:2},sell:{id:"bow",count:1},maxUses:1000}'
)


# ==================================================
# 取引②
# ==================================================

m.execute(
    '/data modify entity @e[type=villager,limit=1,sort=nearest] '
    'Offers.Recipes append value '
    '{buy:{id:"emerald",count:2},sell:{id:"arrow",count:1},maxUses:1000}'
)


# ==================================================
# 取引③
# ==================================================

m.execute(
    '/data modify entity @e[type=villager,limit=1,sort=nearest] '
    'Offers.Recipes append value '
    '{buy:{id:"emerald",count:1},sell:{id:"cooked_beef",count:5},maxUses:1000}'
)


# ==================================================
# 取引④
# ==================================================

m.execute(
    '/data modify entity @e[type=villager,limit=1,sort=nearest] '
    'Offers.Recipes append value '
    '{buy:{id:"emerald",count:3},sell:{id:"potion",count:1},maxUses:1000}'
)


# ==================================================
# 取引⑤
# ==================================================

m.execute(
    '/data modify entity @e[type=villager,limit=1,sort=nearest] '
    'Offers.Recipes append value '
    '{buy:{id:"emerald",count:1},sell:{id:"snowball",count:1},maxUses:1000}'
)


# ==================================================
# 取引⑥
# ==================================================

m.execute(
    '/data modify entity @e[type=villager,limit=1,sort=nearest] '
    'Offers.Recipes append value '
    '{buy:{id:"emerald",count:2},sell:{id:"trident",count:1},maxUses:1000}'
)


# ==================================================
# 取引⑦
# ==================================================

m.execute(
    '/data modify entity @e[type=villager,limit=1,sort=nearest] '
    'Offers.Recipes append value '
    '{buy:{id:"emerald",count:3},sell:{id:"iron_axe",count:1},maxUses:1000}'
)
