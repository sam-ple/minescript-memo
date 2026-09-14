# ============================================================
# MINECRAFT 26.2 TEST AREA
# MineScript VERIFIED DIRECT EXECUTE VERSION
#
# Version : v0.2.00
#
# ============================================================
#
# IMPORTANT
#
# Minecraft Java 26.2
#
# ・cmd関数を使用しない
# ・すべて直接 m.execute()
# ・Armor Standは summon → item replace方式
# ・Chestは item replace block方式
# ・実行間隔を少し入れる
#
# ============================================================


import minescript as m
import math
import time


# ============================================================
# SETTINGS
# ============================================================

HEAD_NAME = "crocadooo"

DELAY = 0.05

ROT = "[0f,0f]"


# ============================================================
# PLAYER POSITION
# ============================================================

m.echo("================================")
m.echo("MINECRAFT 26.2 TEST AREA START")
m.echo("================================")

m.echo("GET PLAYER POSITION")

p = m.player()

px, py, pz = p.position

x = math.floor(px)
y = math.floor(py)
z = math.floor(pz)

m.echo(f"PLAYER POSITION: {px} {py} {pz}")
m.echo(f"BASE POSITION: {x} {y} {z}")


# ============================================================
# INITIAL SETTINGS
# ============================================================

m.echo("INITIAL SETTINGS")

# m.execute("gamerule spawnMonsters false")
m.execute("gamerule spawn_mobs false")
time.sleep(DELAY)

m.execute("difficulty easy")
time.sleep(DELAY)

m.execute("time set night")
time.sleep(DELAY)

m.execute("clear @a")
time.sleep(DELAY)

m.execute("tp @p ~ ~ ~ 180 0")
time.sleep(DELAY)


# ============================================================
# TEST AREA
# ============================================================

m.echo("CREATE TEST AREA")


# ============================================================
# GROUND
# ============================================================

m.echo("CREATE GROUND")

m.execute(
    f"fill "
    f"{x-25} {y-1} {z-25} "
    f"{x+25} {y-1} {z+25} "
    f"minecraft:grass_block"
)

time.sleep(DELAY)


# ============================================================
# CLEAR AREA
# ============================================================

m.echo("CLEAR LOWER AREA")

m.execute(
    f"fill "
    f"{x-25} {y} {z-25} "
    f"{x+25} {y+9} {z+25} "
    f"minecraft:air"
)

time.sleep(DELAY)


m.echo("CLEAR UPPER AREA")

m.execute(
    f"fill "
    f"{x-25} {y+10} {z-25} "
    f"{x+25} {y+20} {z+25} "
    f"minecraft:air"
)

time.sleep(DELAY)


# ============================================================
# ARMOR STAND 1
# PLAYER HEAD + IRON ARMOR
#
# VERIFIED METHOD
# summon
# ↓
# item replace entity
#
# ============================================================

m.echo("================================")
m.echo("ARMOR STAND 1")
m.echo("================================")


AS1_X = x - 14
AS1_Y = y
AS1_Z = z - 5


m.echo("AS1 SUMMON")

m.execute(
    f"summon minecraft:armor_stand "
    f"{AS1_X} {AS1_Y} {AS1_Z} "
    f"{{ShowArms:1b,NoGravity:1b,PersistenceRequired:1b}}"
)

time.sleep(DELAY)


m.echo("AS1 HEAD")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,x={AS1_X},y={AS1_Y},z={AS1_Z},distance=..1,limit=1] "
    f"armor.head "
    f"with minecraft:player_head[profile={{name:\"{HEAD_NAME}\"}}]"
)

time.sleep(DELAY)


m.echo("AS1 CHEST")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,x={AS1_X},y={AS1_Y},z={AS1_Z},distance=..1,limit=1] "
    f"armor.chest "
    f"with minecraft:iron_chestplate"
)

time.sleep(DELAY)


m.echo("AS1 LEGS")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,x={AS1_X},y={AS1_Y},z={AS1_Z},distance=..1,limit=1] "
    f"armor.legs "
    f"with minecraft:iron_leggings"
)

time.sleep(DELAY)


m.echo("AS1 FEET")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,x={AS1_X},y={AS1_Y},z={AS1_Z},distance=..1,limit=1] "
    f"armor.feet "
    f"with minecraft:iron_boots"
)

time.sleep(DELAY)


# ============================================================
# ARMOR STAND 2
# WITHER SKELETON SKULL + DIAMOND ARMOR
# ============================================================

m.echo("================================")
m.echo("ARMOR STAND 2")
m.echo("================================")


AS2_X = x - 13
AS2_Y = y
AS2_Z = z - 5


m.echo("AS2 SUMMON")

m.execute(
    f"summon minecraft:armor_stand "
    f"{AS2_X} {AS2_Y} {AS2_Z} "
    f"{{ShowArms:1b,NoGravity:1b,PersistenceRequired:1b}}"
)

time.sleep(DELAY)


m.echo("AS2 HEAD")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,x={AS2_X},y={AS2_Y},z={AS2_Z},distance=..1,limit=1] "
    f"armor.head "
    f"with minecraft:wither_skeleton_skull"
)

time.sleep(DELAY)


m.echo("AS2 CHEST")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,x={AS2_X},y={AS2_Y},z={AS2_Z},distance=..1,limit=1] "
    f"armor.chest "
    f"with minecraft:diamond_chestplate"
)

time.sleep(DELAY)


m.echo("AS2 LEGS")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,x={AS2_X},y={AS2_Y},z={AS2_Z},distance=..1,limit=1] "
    f"armor.legs "
    f"with minecraft:diamond_leggings"
)

time.sleep(DELAY)


m.echo("AS2 FEET")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,x={AS2_X},y={AS2_Y},z={AS2_Z},distance=..1,limit=1] "
    f"armor.feet "
    f"with minecraft:diamond_boots"
)

time.sleep(DELAY)


# ============================================================
# ARMOR STAND 3
# NETHERITE ARMOR
# ============================================================

m.echo("================================")
m.echo("ARMOR STAND 3")
m.echo("================================")


AS3_X = x - 12
AS3_Y = y
AS3_Z = z - 5


m.echo("AS3 SUMMON")

m.execute(
    f"summon minecraft:armor_stand "
    f"{AS3_X} {AS3_Y} {AS3_Z} "
    f"{{ShowArms:1b,NoGravity:1b,PersistenceRequired:1b}}"
)

time.sleep(DELAY)


m.echo("AS3 HEAD")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,x={AS3_X},y={AS3_Y},z={AS3_Z},distance=..1,limit=1] "
    f"armor.head "
    f"with minecraft:netherite_helmet"
)

time.sleep(DELAY)


m.echo("AS3 CHEST")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,x={AS3_X},y={AS3_Y},z={AS3_Z},distance=..1,limit=1] "
    f"armor.chest "
    f"with minecraft:netherite_chestplate"
)

time.sleep(DELAY)


m.echo("AS3 LEGS")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,x={AS3_X},y={AS3_Y},z={AS3_Z},distance=..1,limit=1] "
    f"armor.legs "
    f"with minecraft:netherite_leggings"
)

time.sleep(DELAY)


m.echo("AS3 FEET")

m.execute(
    f"item replace entity "
    f"@e[type=minecraft:armor_stand,x={AS3_X},y={AS3_Y},z={AS3_Z},distance=..1,limit=1] "
    f"armor.feet "
    f"with minecraft:netherite_boots"
)

time.sleep(DELAY)


# ============================================================
# BASIC BLOCKS
# ============================================================

m.echo("================================")
m.echo("CREATE BASIC BLOCKS")
m.echo("================================")


# 模様入り本棚

m.execute(
    f"setblock "
    f"{x-10} {y} {z-5} "
    f"minecraft:chiseled_bookshelf"
)

time.sleep(DELAY)


# エンチャントテーブル

m.execute(
    f"setblock "
    f"{x-9} {y} {z-5} "
    f"minecraft:enchanting_table"
)

time.sleep(DELAY)


# 醸造台

m.execute(
    f"setblock "
    f"{x-8} {y} {z-5} "
    f"minecraft:brewing_stand"
)

time.sleep(DELAY)


# 溶鉱炉

m.execute(
    f"setblock "
    f"{x-7} {y} {z-5} "
    f"minecraft:blast_furnace[facing=south]"
)

time.sleep(DELAY)


# ============================================================
# DOUBLE CHEST
# VERIFIED METHOD
# ============================================================

m.echo("================================")
m.echo("CREATE DOUBLE CHEST")
m.echo("================================")


CHEST_X = x - 6
CHEST_Y = y
CHEST_Z = z - 5


m.execute(
    f"setblock "
    f"{CHEST_X} {CHEST_Y} {CHEST_Z} "
    f"minecraft:chest[facing=south,type=right]"
)

time.sleep(DELAY)


m.execute(
    f"setblock "
    f"{CHEST_X+1} {CHEST_Y} {CHEST_Z} "
    f"minecraft:chest[facing=south,type=left]"
)

time.sleep(DELAY)


# ============================================================
# CHEST ITEMS
#
# data mergeを使用せず
# 成功確認済みitem replace方式
# ============================================================

m.echo("SET CHEST ITEMS")


CHEST_ITEMS = [

    ("minecraft:cobblestone", 64),
    ("minecraft:iron_ingot", 64),
    ("minecraft:stone_pickaxe", 1),
    ("minecraft:shield", 1),
    ("minecraft:bow", 1),
    ("minecraft:arrow", 64),
    ("minecraft:trident", 1),

    ("minecraft:obsidian", 64),
    ("minecraft:crying_obsidian", 64),

    ("minecraft:diamond", 64),
    ("minecraft:dried_ghast", 1),
    ("minecraft:sniffer_egg", 1),
    ("minecraft:wheat_seeds", 64),
    ("minecraft:blaze_rod", 64),
    ("minecraft:dragon_egg", 1),
    ("minecraft:dragon_breath", 64),
    ("minecraft:elytra", 1),
    ("minecraft:pumpkin", 64),

]


for slot, item_data in enumerate(CHEST_ITEMS):

    item_id, count = item_data

    m.execute(
        f"item replace block "
        f"{CHEST_X} {CHEST_Y} {CHEST_Z} "
        f"container.{slot} "
        f"with {item_id} {count}"
    )

    time.sleep(DELAY)


# ============================================================
# BED
# ============================================================

m.echo("CREATE BED")


m.execute(
    f"setblock "
    f"{x-4} {y} {z-5} "
    f"minecraft:red_bed[facing=south,part=foot]"
)

time.sleep(DELAY)


m.execute(
    f"setblock "
    f"{x-4} {y} {z-4} "
    f"minecraft:red_bed[facing=south,part=head]"
)

time.sleep(DELAY)


# ============================================================
# VILLAGER
# ============================================================

m.echo("CREATE VILLAGER")


m.execute(
    f"summon minecraft:villager "
    f"{x-3} {y} {z-5} "
    f"{{"
    f"VillagerData:{{level:5,profession:\"farmer\",type:\"plains\"}},"
    f"Silent:1b,"
    f"Invulnerable:1b,"
    f"NoAI:1b"
    f"}}"
)

time.sleep(DELAY)


# ============================================================
# SKELETON
# ============================================================

m.echo("CREATE SKELETON")


m.execute(
    f"summon minecraft:skeleton "
    f"{x-2} {y} {z-5} "
    f"{{"
    f"NoAI:1b,"
    f"PersistenceRequired:1b,"
    f"Health:2f,"
    f"Rotation:{ROT}"
    f"}}"
)

time.sleep(DELAY)


# ============================================================
# SIGN
# ============================================================

m.echo("CREATE SIGN")


m.execute(
    f"setblock "
    f"{x-1} {y} {z-5} "
    f"minecraft:oak_sign[rotation=0]"
)

time.sleep(DELAY)


# ============================================================
# CRAFTING TABLE
# ============================================================

m.execute(
    f"setblock "
    f"{x} {y} {z-5} "
    f"minecraft:crafting_table"
)

time.sleep(DELAY)


# ============================================================
# ANIMALS
# ============================================================

m.echo("CREATE ANIMALS")


# PARROT

m.execute(
    f"summon minecraft:parrot "
    f"{x+1} {y} {z-5} "
    f"{{NoAI:1b,Silent:1b,Rotation:{ROT}}}"
)

time.sleep(DELAY)


# ARMADILLO

m.execute(
    f"summon minecraft:armadillo "
    f"{x+2} {y} {z-5} "
    f"{{NoAI:1b,Silent:1b,Rotation:{ROT}}}"
)

time.sleep(DELAY)


# ALLAY

m.execute(
    f"summon minecraft:allay "
    f"{x+3} {y} {z-5} "
    f"{{Silent:1b,NoGravity:1b,PersistenceRequired:1b}}"
)

time.sleep(DELAY)


# ============================================================
# GOLD BLOCK / SUSPICIOUS SAND TEST
# ============================================================

m.echo("CREATE GOLD BLOCK TEST")


m.execute(
    f"setblock "
    f"{x+10} {y-1} {z-5} "
    f"minecraft:gold_block"
)

time.sleep(DELAY)


GOLD_COMMAND = (
    f"execute as @a at @s "
    f"if block ~ ~-1 ~ minecraft:gold_block "
    f"run setblock {x+10} {y} {z-7} minecraft:suspicious_sand"
)


GOLD_COMMAND_ESCAPED = GOLD_COMMAND.replace('"', '\\"')


m.execute(
    f"setblock "
    f"{x+10} {y-2} {z-5} "
    f"minecraft:repeating_command_block"
    f"{{auto:1b,Command:\"{GOLD_COMMAND_ESCAPED}\"}}"
)

time.sleep(DELAY)


# ============================================================
# TP BUTTON
# ============================================================

m.echo("CREATE TP BUTTON")


TP_X = x + 11
TP_Y = y
TP_Z = z - 5


# Command Block

m.execute(
    f"setblock "
    f"{TP_X} {TP_Y-1} {TP_Z} "
    f"minecraft:command_block"
    f"{{Command:\"tp @p {x} {y+1} {z}\"}}"
)

time.sleep(DELAY)


# Stone

m.execute(
    f"setblock "
    f"{TP_X} {TP_Y} {TP_Z} "
    f"minecraft:stone"
)

time.sleep(DELAY)


# Button

m.execute(
    f"setblock "
    f"{TP_X} {TP_Y} {TP_Z+1} "
    f"minecraft:stone_button[facing=south]"
)

time.sleep(DELAY)


# ============================================================
# SIGN CLICK TEST
#
# ここは26.2で別途検証対象
# ============================================================

m.echo("CREATE CLICK SIGN")


m.execute(
    f"setblock "
    f"{x+12} {y} {z-5} "
    f"minecraft:oak_sign"
)

time.sleep(DELAY)


# ============================================================
# COMPASS + SNEAK TP SYSTEM
# ============================================================

m.echo("CREATE COMPASS TP SYSTEM")


m.execute(
    "scoreboard objectives add "
    "isSneaking "
    "minecraft.custom:minecraft.sneak_time"
)

time.sleep(DELAY)


TP_COMMAND = (
    f"execute as @a[nbt={{SelectedItem:{{id:\"minecraft:compass\"}}}}] "
    f"if score @s isSneaking matches 1.. "
    f"run tp @s {x} {y+1} {z}"
)

TP_COMMAND_ESCAPED = TP_COMMAND.replace('"', '\\"')


m.execute(
    f"setblock "
    f"{x} {y-2} {z} "
    f"minecraft:repeating_command_block"
    f"{{auto:1b,Command:\"{TP_COMMAND_ESCAPED}\"}}"
)

time.sleep(DELAY)


RESET_COMMAND = (
    "scoreboard players set @a isSneaking 0"
)


m.execute(
    f"setblock "
    f"{x+1} {y-2} {z} "
    f"minecraft:repeating_command_block"
    f"{{auto:1b,Command:\"{RESET_COMMAND}\"}}"
)

time.sleep(DELAY)


# ============================================================
# WATER AREA
# ============================================================

m.echo("CREATE WATER AREA")


m.execute(
    f"fill "
    f"{x-5} {y-1} {z} "
    f"{x-2} {y-1} {z+1} "
    f"minecraft:water"
)

time.sleep(DELAY)


# ============================================================
# LAVA AREA
# ============================================================

m.execute(
    f"fill "
    f"{x+2} {y-1} {z} "
    f"{x+2} {y-1} {z+1} "
    f"minecraft:lava"
)

time.sleep(DELAY)


# ============================================================
# AQUATIC ANIMALS
# ============================================================

m.echo("CREATE AQUATIC ANIMALS")


m.execute(
    f"summon minecraft:axolotl "
    f"{x-3} {y-1} {z} "
    f"{{NoAI:1b}}"
)

time.sleep(DELAY)


m.execute(
    f"summon minecraft:tadpole "
    f"{x-5} {y-1} {z+1} "
    f"{{NoAI:1b}}"
)

time.sleep(DELAY)


# ============================================================
# NETHER PORTAL
# ============================================================

m.echo("CREATE NETHER PORTAL")


BASE_X = 5
BASE_Y = -1
BASE_Z = -5


for dy in range(5):

    for dx in range(4):

        if dx == 0 or dx == 3 or dy == 0 or dy == 4:

            block = "minecraft:obsidian"

        else:

            block = "minecraft:air"


        m.execute(
            f"setblock "
            f"{x + BASE_X + dx} "
            f"{y + BASE_Y + dy} "
            f"{z + BASE_Z} "
            f"{block}"
        )

        time.sleep(DELAY)


# Portal Fire

m.execute(
    f"setblock "
    f"{x+BASE_X+1} "
    f"{y+BASE_Y+1} "
    f"{z+BASE_Z} "
    f"minecraft:fire"
)

time.sleep(DELAY)


# ============================================================
# ITEM GIVE
# ============================================================

m.echo("GIVE ITEMS")


ITEMS = [

    'minecraft:fishing_rod[enchantments={"minecraft:luck_of_the_sea":3,"minecraft:lure":3,"minecraft:unbreaking":3,"minecraft:mending":1}] 1',

    "minecraft:emerald 64",

    "minecraft:bone 64",

    "minecraft:glow_ink_sac 64",

    "minecraft:copper_ingot 64",

    "minecraft:feather 64",

    "minecraft:stick 64",

    "minecraft:suspicious_sand 64",

    "minecraft:compass 1",

]


for item in ITEMS:

    m.execute(
        f"give @a {item}"
    )

    time.sleep(DELAY)


# ============================================================
# WOLVES
# ============================================================

m.echo("CREATE WOLVES")


WOLF_VARIANTS = [

    "pale",
    "woods",
    "ashen",
    "black",
    "chestnut",
    "rusty",
    "spotted",
    "striped",
    "snowy",
    "classic",
    "big",
    "grumpy"

]


WOLF_BASE_X = -11
WOLF_Z = -10


for i, variant in enumerate(WOLF_VARIANTS):

    m.execute(
        f"summon minecraft:wolf "
        f"{x + WOLF_BASE_X + i} "
        f"{y} "
        f"{z + WOLF_Z} "
        f"{{"
        f"NoAI:1b,"
        f"Sitting:1b,"
        f"Silent:1b,"
        f"CollarColor:14b,"
        f'variant:"minecraft:{variant}",'
        f'sound_variant:"minecraft:{variant}"'
        f"}}"
    )

    time.sleep(DELAY)


# ============================================================
# BONE CHEST
# ============================================================

m.echo("CREATE BONE CHEST")


BONE_CHEST_X = x - 12
BONE_CHEST_Y = y
BONE_CHEST_Z = z - 10


m.execute(
    f"setblock "
    f"{BONE_CHEST_X} {BONE_CHEST_Y} {BONE_CHEST_Z} "
    f"minecraft:chest[facing=south]"
)

time.sleep(DELAY)


for slot in range(8):

    m.execute(
        f"item replace block "
        f"{BONE_CHEST_X} {BONE_CHEST_Y} {BONE_CHEST_Z} "
        f"container.{slot} "
        f"with minecraft:bone 64"
    )

    time.sleep(DELAY)


# ============================================================
# CATS
# ============================================================

m.echo("CREATE CATS")


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


CAT_BASE_X = -11
CAT_Z = -14


for i, variant in enumerate(CAT_VARIANTS):

    m.execute(
        f"summon minecraft:cat "
        f"{x + CAT_BASE_X + i} "
        f"{y} "
        f"{z + CAT_Z} "
        f"{{"
        f"NoAI:1b,"
        f"Sitting:1b,"
        f"Silent:1b,"
        f'variant:"minecraft:{variant}"'
        f"}}"
    )

    time.sleep(DELAY)


# ============================================================
# FISH CHEST
# ============================================================

m.echo("CREATE FISH CHEST")


FISH_CHEST_X = x - 12
FISH_CHEST_Y = y
FISH_CHEST_Z = z - 14


m.execute(
    f"setblock "
    f"{FISH_CHEST_X} {FISH_CHEST_Y} {FISH_CHEST_Z} "
    f"minecraft:chest[facing=south]"
)

time.sleep(DELAY)


FISH_ITEMS = [

    ("minecraft:cod", 64),

    ("minecraft:cod", 64),

    ("minecraft:salmon", 64),

    ("minecraft:salmon", 64),

]


for slot, item_data in enumerate(FISH_ITEMS):

    item_id, count = item_data

    m.execute(
        f"item replace block "
        f"{FISH_CHEST_X} {FISH_CHEST_Y} {FISH_CHEST_Z} "
        f"container.{slot} "
        f"with {item_id} {count}"
    )

    time.sleep(DELAY)


# ============================================================
# FROGS
# ============================================================

m.echo("CREATE FROGS")


FROG_VARIANTS = [

    "temperate",

    "warm",

    "cold"

]


FROG_BASE_X = -11
FROG_Z = -18


for i, variant in enumerate(FROG_VARIANTS):

    m.execute(
        f"summon minecraft:frog "
        f"{x + FROG_BASE_X + i} "
        f"{y} "
        f"{z + FROG_Z} "
        f"{{"
        f"NoAI:1b,"
        f"Silent:1b,"
        f'variant:"minecraft:{variant}"'
        f"}}"
    )

    time.sleep(DELAY)


# ============================================================
# LEAD CHEST
# ============================================================

m.echo("CREATE LEAD CHEST")


LEAD_CHEST_X = x - 12
LEAD_CHEST_Y = y
LEAD_CHEST_Z = z - 18


m.execute(
    f"setblock "
    f"{LEAD_CHEST_X} {LEAD_CHEST_Y} {LEAD_CHEST_Z} "
    f"minecraft:chest[facing=south]"
)

time.sleep(DELAY)


for slot in range(3):

    m.execute(
        f"item replace block "
        f"{LEAD_CHEST_X} {LEAD_CHEST_Y} {LEAD_CHEST_Z} "
        f"container.{slot} "
        f"with minecraft:lead 64"
    )

    time.sleep(DELAY)


# ============================================================
# COMPLETE
# ============================================================

m.echo("================================")
m.echo("MINECRAFT 26.2 TEST AREA COMPLETE")
m.echo("================================")

print("================================")
print("MINECRAFT 26.2 TEST AREA COMPLETE")
print("================================")
