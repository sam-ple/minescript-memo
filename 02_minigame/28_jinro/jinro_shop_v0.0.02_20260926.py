import minescript as m


def add_trade(tag, buy_item, buy_count, sell_item, sell_count):

    m.execute(
        f'/data modify entity @e[type=villager,tag={tag},limit=1] '
        f'Offers.Recipes append value '
        f'{{buy:{{id:"{buy_item}",count:{buy_count}}},'
        f'sell:{{id:"{sell_item}",count:{sell_count}}},'
        f'maxUses:1000}}'
    )


# ==================================================
# 戦闘
# ==================================================

m.execute(
    '/summon villager ~-1 ~ ~ '
    '{'
    'VillagerData:{level:5,profession:"farmer",type:"plains"},'
    'CustomName:"戦闘",'
    'CustomNameVisible:true,'
    'Silent:1b,'
    'Invulnerable:1b,'
    'NoAI:1b,'
    'Tags:["shop_1_battle"]'
    '}'
)

add_trade("shop_1_battle", "emerald", 2, "bow", 1)
add_trade("shop_1_battle", "emerald", 2, "arrow", 1)
add_trade("shop_1_battle", "emerald", 1, "cooked_beef", 5)
add_trade("shop_1_battle", "emerald", 3, "potion", 1)
add_trade("shop_1_battle", "emerald", 1, "snowball", 1)
add_trade("shop_1_battle", "emerald", 2, "trident", 1)
add_trade("shop_1_battle", "emerald", 3, "iron_axe", 1)


# ==================================================
# 補助
# ==================================================

m.execute(
    '/summon villager ~1 ~ ~ '
    '{'
    'VillagerData:{level:5,profession:"farmer",type:"plains"},'
    'CustomName:"補助",'
    'CustomNameVisible:true,'
    'Silent:1b,'
    'Invulnerable:1b,'
    'NoAI:1b,'
    'Tags:["shop_1_support"]'
    '}'
)

add_trade("shop_1_support", "emerald", 8, "heart_of_the_sea", 1)
add_trade("shop_1_support", "emerald", 3, "gunpowder", 1)
add_trade("shop_1_support", "emerald", 2, "golden_horse_armor", 5)
add_trade("shop_1_support", "emerald", 3, "end_crystal", 1)
add_trade("shop_1_support", "emerald", 2, "nether_star", 1)
add_trade("shop_1_support", "emerald", 4, "sunflower", 1)
add_trade("shop_1_support", "emerald", 1, "paper", 1)
