import minescript as m
import math
import time


# ==================================================
# MINECRAFT 26.2 TEST AREA
# VERIFIED / DIRECT EXECUTE VERSION
#
# Version : v0.2.00
#
# ==================================================
#
# CHANGES
#
# ・cmd()関数を使用しない
# ・すべて直接 m.execute()
# ・gamerule spawn_mobs false
# ・右側クリック看板を削除
# ・金ブロックを踏むとダイヤモンド出現
# ・ボタンを押すとアイテム配布
# ・Armor Standに腕＋武器追加
# ・Wolf Variantを安全な種類に修正
#
# ==================================================


# ==================================================
# PLAYER POSITION
# ==================================================

p = m.player()

px, py, pz = p.position

x = math.floor(px)
y = math.floor(py)
z = math.floor(pz)


def pos(dx=0, dy=0, dz=0):
    return f"{x + dx} {y + dy} {z + dz}"


HEAD_NAME = "crocadooo"

ROT = "[0f,0f]"


# ==================================================
# START
# ==================================================

m.echo("================================")
m.echo("MINECRAFT 26.2 TEST AREA START")
m.echo("================================")

m.echo("GET PLAYER POSITION")
m.echo(f"PLAYER POSITION: {px} {py} {pz}")
m.echo(f"BASE POSITION: {x} {y} {z}")


# ==================================================
# INITIAL SETTINGS
# ==================================================

m.echo("INITIAL SETTINGS")

m.execute("gamerule spawn_mobs false")
m.execute("difficulty easy")
m.execute("time set night")
m.execute("clear @a")

# プレイヤーの向きを北向き
m.execute("tp @p ~ ~ ~ 180 0")


# ==================================================
# TEST AREA
# ==================================================

m.echo("CREATE TEST AREA")


# ==================================================
# GROUND
# ==================================================

m.echo("CREATE GROUND")

m.execute(
    f"fill "
    f"{pos(-25, -1, -25)} "
    f"{pos(25, -1, 25)} "
    f"minecraft:grass_block"
)


# ==================================================
# CLEAR AREA
# ==================================================

m.echo("CLEAR LOWER AREA")

m.execute(
    f"fill "
    f"{pos(-25, 0, -25)} "
    f"{pos(25, 9, 25)} "
    f"minecraft:air"
)


m.echo("CLEAR UPPER AREA")

m.execute(
    f"fill "
    f"{pos(-25, 10, -25)} "
    f"{pos(25, 20, 25)} "
    f"minecraft:air"
)


# ==================================================
# ARMOR STAND 1
#
# Player Head
# Iron Armor
# Iron Sword
#
# ==================================================

m.echo("================================")
m.echo("ARMOR STAND 1")
m.echo("================================")


m.echo("AS1 SUMMON")

m.execute(
    f"summon minecraft:armor_stand "
    f"{pos(-14, 0, -5)} "
    f"{{"
    f"ShowArms:true,"
    f"NoGravity:true,"
    f"PersistenceRequired:true"
    f"}}"
)


time.sleep(0.1)


m.echo("AS1 HEAD")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,sort=nearest,limit=1,distance=..2] "
    f"armor.head "
    f"with minecraft:player_head"
    f"[profile={{name:\"{HEAD_NAME}\"}}]"
)


m.echo("AS1 CHEST")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,sort=nearest,limit=1,distance=..2] "
    f"armor.chest "
    f"with minecraft:iron_chestplate"
)


m.echo("AS1 LEGS")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,sort=nearest,limit=1,distance=..2] "
    f"armor.legs "
    f"with minecraft:iron_leggings"
)


m.echo("AS1 FEET")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,sort=nearest,limit=1,distance=..2] "
    f"armor.feet "
    f"with minecraft:iron_boots"
)


m.echo("AS1 MAINHAND")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,sort=nearest,limit=1,distance=..2] "
    f"weapon.mainhand "
    f"with minecraft:iron_sword"
)


# ==================================================
# ARMOR STAND 2
#
# Wither Skeleton Skull
# Diamond Armor
# Diamond Axe
#
# ==================================================

m.echo("================================")
m.echo("ARMOR STAND 2")
m.echo("================================")


m.echo("AS2 SUMMON")

m.execute(
    f"summon minecraft:armor_stand "
    f"{pos(-13, 0, -5)} "
    f"{{"
    f"ShowArms:true,"
    f"NoGravity:true,"
    f"PersistenceRequired:true"
    f"}}"
)


time.sleep(0.1)


m.echo("AS2 HEAD")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,sort=nearest,limit=1,x={x-13},y={y},z={z-5},distance=..2] "
    f"armor.head "
    f"with minecraft:wither_skeleton_skull"
)


m.echo("AS2 CHEST")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,sort=nearest,limit=1,x={x-13},y={y},z={z-5},distance=..2] "
    f"armor.chest "
    f"with minecraft:diamond_chestplate"
)


m.echo("AS2 LEGS")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,sort=nearest,limit=1,x={x-13},y={y},z={z-5},distance=..2] "
    f"armor.legs "
    f"with minecraft:diamond_leggings"
)


m.echo("AS2 FEET")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,sort=nearest,limit=1,x={x-13},y={y},z={z-5},distance=..2] "
    f"armor.feet "
    f"with minecraft:diamond_boots"
)


m.echo("AS2 MAINHAND")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,sort=nearest,limit=1,x={x-13},y={y},z={z-5},distance=..2] "
    f"weapon.mainhand "
    f"with minecraft:diamond_axe"
)


# ==================================================
# ARMOR STAND 3
#
# Netherite Armor
# Netherite Pickaxe
# Shield
#
# ==================================================

m.echo("================================")
m.echo("ARMOR STAND 3")
m.echo("================================")


m.echo("AS3 SUMMON")

m.execute(
    f"summon minecraft:armor_stand "
    f"{pos(-12, 0, -5)} "
    f"{{"
    f"ShowArms:true,"
    f"NoGravity:true,"
    f"PersistenceRequired:true"
    f"}}"
)


time.sleep(0.1)


m.echo("AS3 HEAD")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,sort=nearest,limit=1,x={x-12},y={y},z={z-5},distance=..2] "
    f"armor.head "
    f"with minecraft:netherite_helmet"
)


m.echo("AS3 CHEST")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,sort=nearest,limit=1,x={x-12},y={y},z={z-5},distance=..2] "
    f"armor.chest "
    f"with minecraft:netherite_chestplate"
)


m.echo("AS3 LEGS")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,sort=nearest,limit=1,x={x-12},y={y},z={z-5},distance=..2] "
    f"armor.legs "
    f"with minecraft:netherite_leggings"
)


m.echo("AS3 FEET")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,sort=nearest,limit=1,x={x-12},y={y},z={z-5},distance=..2] "
    f"armor.feet "
    f"with minecraft:netherite_boots"
)


m.echo("AS3 MAINHAND")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,sort=nearest,limit=1,x={x-12},y={y},z={z-5},distance=..2] "
    f"weapon.mainhand "
    f"with minecraft:netherite_pickaxe"
)


m.echo("AS3 OFFHAND")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,sort=nearest,limit=1,x={x-12},y={y},z={z-5},distance=..2] "
    f"weapon.offhand "
    f"with minecraft:shield"
)


# ==================================================
# BASIC BLOCKS
# ==================================================

m.echo("================================")
m.echo("CREATE BASIC BLOCKS")
m.echo("================================")


# 模様入り本棚

m.execute(
    f"setblock "
    f"{pos(-10, 0, -5)} "
    f"minecraft:chiseled_bookshelf"
)


# エンチャントテーブル

m.execute(
    f"setblock "
    f"{pos(-9, 0, -5)} "
    f"minecraft:enchanting_table"
)


# 醸造台

m.execute(
    f"setblock "
    f"{pos(-8, 0, -5)} "
    f"minecraft:brewing_stand"
)


# 溶鉱炉

m.execute(
    f"setblock "
    f"{pos(-7, 0, -5)} "
    f"minecraft:blast_furnace[facing=south]"
)


# ==================================================
# DOUBLE CHEST
# ==================================================

m.echo("CREATE DOUBLE CHEST")


m.execute(
    f"setblock "
    f"{pos(-6, 0, -5)} "
    f"minecraft:chest[facing=south,type=right]"
)


m.execute(
    f"setblock "
    f"{pos(-5, 0, -5)} "
    f"minecraft:chest[facing=south,type=left]"
)


# ==================================================
# CHEST ITEMS
# ==================================================

m.echo("SET CHEST ITEMS")


m.execute(
    f"item replace block {pos(-6, 0, -5)} container.0 "
    f"with minecraft:cobblestone 64"
)

m.execute(
    f"item replace block {pos(-6, 0, -5)} container.1 "
    f"with minecraft:iron_ingot 64"
)

m.execute(
    f"item replace block {pos(-6, 0, -5)} container.2 "
    f"with minecraft:stone_pickaxe 1"
)

m.execute(
    f"item replace block {pos(-6, 0, -5)} container.3 "
    f"with minecraft:shield 1"
)

m.execute(
    f"item replace block {pos(-6, 0, -5)} container.4 "
    f"with minecraft:bow 1"
)

m.execute(
    f"item replace block {pos(-6, 0, -5)} container.5 "
    f"with minecraft:arrow 64"
)

m.execute(
    f"item replace block {pos(-6, 0, -5)} container.6 "
    f"with minecraft:trident 1"
)

m.execute(
    f"item replace block {pos(-6, 0, -5)} container.7 "
    f"with minecraft:obsidian 64"
)

m.execute(
    f"item replace block {pos(-6, 0, -5)} container.8 "
    f"with minecraft:crying_obsidian 64"
)

m.execute(
    f"item replace block {pos(-6, 0, -5)} container.9 "
    f"with minecraft:diamond 64"
)


# ==================================================
# BED
# ==================================================

m.execute(
    f"setblock "
    f"{pos(-4, 0, -5)} "
    f"minecraft:red_bed[facing=south,part=foot]"
)

m.execute(
    f"setblock "
    f"{pos(-4, 0, -4)} "
    f"minecraft:red_bed[facing=south,part=head]"
)


# ==================================================
# VILLAGER
# ==================================================

m.execute(
    f"summon minecraft:villager "
    f"{pos(-3, 0, -5)} "
    f"{{"
    f'VillagerData:{{level:5,profession:"farmer",type:"plains"}},'
    f"Silent:1b,"
    f"Invulnerable:1b,"
    f"NoAI:1b"
    f"}}"
)


# ==================================================
# SKELETON
# ==================================================

m.execute(
    f"summon minecraft:skeleton "
    f"{pos(-2, 0, -5)} "
    f"{{"
    f"NoAI:1b,"
    f"PersistenceRequired:1b,"
    f"Health:2f,"
    f"Rotation:{ROT}"
    f"}}"
)


# ==================================================
# CRAFTING TABLE
# ==================================================

m.execute(
    f"setblock "
    f"{pos(0, 0, -5)} "
    f"minecraft:crafting_table"
)


# ==================================================
# ANIMALS
# ==================================================

m.execute(
    f"summon minecraft:parrot "
    f"{pos(1, 0, -5)} "
    f"{{NoAI:1b,Silent:1b,Rotation:{ROT}}}"
)


m.execute(
    f"summon minecraft:armadillo "
    f"{pos(2, 0, -5)} "
    f"{{NoAI:1b,Silent:1b,Rotation:{ROT}}}"
)


m.execute(
    f"summon minecraft:allay "
    f"{pos(3, 0, -5)} "
    f"{{"
    f"Silent:1b,"
    f"NoGravity:1b,"
    f"PersistenceRequired:1b"
    f"}}"
)


# ==================================================
# GOLD BLOCK → DIAMOND DROP
# ==================================================
#
# 金ブロックの上に乗ったプレイヤーを検知。
# 指定位置にダイヤモンドをアイテムとして出す。
#
# ==================================================

m.echo("GOLD BLOCK DIAMOND SYSTEM")


# 金ブロック

m.execute(
    f"setblock "
    f"{pos(10, -1, -5)} "
    f"minecraft:gold_block"
)


# 繰り返しコマンドブロック

gold_cmd = (
    f"execute as @a at @s "
    f"if block ~ ~-1 ~ minecraft:gold_block "
    f"run summon minecraft:item {pos(10, 0, -7)} "
    f'{{Item:{{id:"minecraft:diamond",count:1}}}}'
)

gold_cmd = gold_cmd.replace('"', '\\"')


m.execute(
    f"setblock "
    f"{pos(10, -2, -5)} "
    f"minecraft:repeating_command_block"
    f"{{"
    f"auto:1b,"
    f'Command:"{gold_cmd}"'
    f"}}"
)


# ==================================================
# BUTTON ITEM SYSTEM
# ==================================================
#
# ボタンを押す
# ↓
# コマンドブロックが実行
# ↓
# プレイヤーにエメラルドを渡す
#
# ==================================================

m.echo("BUTTON ITEM SYSTEM")


button_cmd = (
    f"give @p minecraft:emerald 5"
)


m.execute(
    f"setblock "
    f"{pos(11, -1, -5)} "
    f"minecraft:command_block"
    f"{{"
    f'Command:"{button_cmd}"'
    f"}}"
)


# 上の石ブロック

m.execute(
    f"setblock "
    f"{pos(11, 0, -5)} "
    f"minecraft:stone"
)


# ボタン

m.execute(
    f"setblock "
    f"{pos(11, 0, -4)} "
    f"minecraft:stone_button[facing=south]"
)


# ==================================================
# COMPASS + SNEAK RETURN
# ==================================================

m.echo("COMPASS RETURN SYSTEM")


# スコアボード

m.execute(
    "scoreboard objectives add "
    "isSneaking "
    "minecraft.custom:minecraft.sneak_time"
)


# TP処理

tp_cmd = (
    f'execute as @a[nbt={{SelectedItem:{{id:"minecraft:compass"}}}}] '
    f'if score @s isSneaking matches 1.. '
    f'run tp @s {pos(0, 1, 0)}'
)

tp_cmd = tp_cmd.replace('"', '\\"')


m.execute(
    f"setblock "
    f"{pos(0, -2, 0)} "
    f"minecraft:repeating_command_block"
    f"{{"
    f"auto:1b,"
    f'Command:"{tp_cmd}"'
    f"}}"
)


# スコアリセット

reset_cmd = (
    "scoreboard players set @a isSneaking 0"
)


m.execute(
    f"setblock "
    f"{pos(1, -2, 0)} "
    f"minecraft:repeating_command_block"
    f"{{"
    f"auto:1b,"
    f'Command:"{reset_cmd}"'
    f"}}"
)


# ==================================================
# WATER / LAVA AREA
# ==================================================

m.echo("WATER AND LAVA AREA")


# 水

m.execute(
    f"fill "
    f"{pos(-5, -1, 0)} "
    f"{pos(-2, -1, 1)} "
    f"minecraft:water"
)


# 溶岩

m.execute(
    f"fill "
    f"{pos(2, -1, 0)} "
    f"{pos(2, -1, 1)} "
    f"minecraft:lava"
)


# 水生生物

m.execute(
    f"summon minecraft:axolotl "
    f"{pos(-3, -1, 0)} "
    f"{{NoAI:1b}}"
)


m.execute(
    f"summon minecraft:tadpole "
    f"{pos(-5, -1, 1)} "
    f"{{NoAI:1b}}"
)


# ==================================================
# NETHER PORTAL
# ==================================================

m.echo("CREATE NETHER PORTAL")


BASE_X = 5
BASE_Y = -1
BASE_Z = -5


for dy in range(5):

    for dx in range(4):

        if dx in [0, 3] or dy in [0, 4]:
            block = "minecraft:obsidian"
        else:
            block = "minecraft:air"

        m.execute(
            f"setblock "
            f"{pos(BASE_X + dx, BASE_Y + dy, BASE_Z)} "
            f"{block}"
        )


# 点火

m.execute(
    f"setblock "
    f"{pos(BASE_X + 1, BASE_Y + 1, BASE_Z)} "
    f"minecraft:fire"
)


# ==================================================
# ITEM DISTRIBUTION
# ==================================================

m.echo("ITEM DISTRIBUTION")


items = [

    'minecraft:fishing_rod[enchantments={"minecraft:luck_of_the_sea":3,"minecraft:lure":3,"minecraft:unbreaking":3,"minecraft:mending":1}] 1',

    "minecraft:emerald 64",
    "minecraft:bone 64",
    "minecraft:glow_ink_sac 64",
    "minecraft:copper_ingot 64",
    "minecraft:feather 64",
    "minecraft:stick 64",
    "minecraft:suspicious_sand 64",
    "minecraft:compass 1"

]


for item in items:

    m.execute(
        f"give @a {item}"
    )


# ==================================================
# WOLF LINE
# ==================================================
#
# Minecraftで安全なWolf Variantのみ使用。
#
# ==================================================

m.echo("WOLF LINE")


WOLF_VARIANTS = [

    "pale",
    "woods",
    "ashen",
    "black",
    "chestnut",
    "rusty",
    "spotted",
    "striped",
    "snowy"

]


base_x = -11
z_line = -10


for i, variant in enumerate(WOLF_VARIANTS):

    m.execute(
        f"summon minecraft:wolf "
        f"{pos(base_x + i, 0, z_line)} "
        f"{{"
        f"NoAI:1b,"
        f"Sitting:1b,"
        f"Silent:1b,"
        f"CollarColor:14b,"
        f'variant:"minecraft:{variant}"'
        f"}}"
    )


# ==================================================
# BONE CHEST
# ==================================================

m.execute(
    f"setblock "
    f"{pos(-12, 0, -10)} "
    f"minecraft:chest[facing=south]"
)


BONE_ITEMS = [

    ("minecraft:bone", 64),
    ("minecraft:bone", 64),
    ("minecraft:bone", 64),
    ("minecraft:bone", 64),
    ("minecraft:bone", 64),
    ("minecraft:bone", 64),
    ("minecraft:bone", 64),
    ("minecraft:bone", 64)

]


for slot, item_data in enumerate(BONE_ITEMS):

    item_id, count = item_data

    m.execute(
        f"item replace block "
        f"{pos(-12, 0, -10)} "
        f"container.{slot} "
        f"with {item_id} {count}"
    )


# ==================================================
# CAT LINE
# ==================================================

m.echo("CAT LINE")


CAT_VARIANTS = [

    "tabby",
    "black",
    "red",
    "siamese",
    "british_shorthair",
    "calico",
    "persian",
    "ragdoll",
    "white",
    "jellie",
    "all_black"

]


base_x = -11
z_line = -14


for i, variant in enumerate(CAT_VARIANTS):

    m.execute(
        f"summon minecraft:cat "
        f"{pos(base_x + i, 0, z_line)} "
        f"{{"
        f"NoAI:1b,"
        f"Sitting:1b,"
        f"Silent:1b,"
        f'variant:"minecraft:{variant}"'
        f"}}"
    )


# ==================================================
# FISH CHEST
# ==================================================

m.execute(
    f"setblock "
    f"{pos(-12, 0, -14)} "
    f"minecraft:chest[facing=south]"
)


FISH_ITEMS = [

    ("minecraft:cod", 64),
    ("minecraft:cod", 64),
    ("minecraft:salmon", 64),
    ("minecraft:salmon", 64)

]


for slot, item_data in enumerate(FISH_ITEMS):

    item_id, count = item_data

    m.execute(
        f"item replace block "
        f"{pos(-12, 0, -14)} "
        f"container.{slot} "
        f"with {item_id} {count}"
    )


# ==================================================
# FROG LINE
# ==================================================

m.echo("FROG LINE")


FROG_VARIANTS = [

    "temperate",
    "warm",
    "cold"

]


base_x = -11
z_line = -18


for i, variant in enumerate(FROG_VARIANTS):

    m.execute(
        f"summon minecraft:frog "
        f"{pos(base_x + i, 0, z_line)} "
        f"{{"
        f"NoAI:1b,"
        f"Silent:1b,"
        f'variant:"minecraft:{variant}"'
        f"}}"
    )


# ==================================================
# LEAD CHEST
# ==================================================

m.execute(
    f"setblock "
    f"{pos(-12, 0, -18)} "
    f"minecraft:chest[facing=south]"
)


LEAD_ITEMS = [

    ("minecraft:lead", 64),
    ("minecraft:lead", 64),
    ("minecraft:lead", 64)

]


for slot, item_data in enumerate(LEAD_ITEMS):

    item_id, count = item_data

    m.execute(
        f"item replace block "
        f"{pos(-12, 0, -18)} "
        f"container.{slot} "
        f"with {item_id} {count}"
    )


# ==================================================
# COMPLETE
# ==================================================

m.echo("================================")
m.echo("MINECRAFT 26.2 TEST AREA COMPLETE")
m.echo("================================")
