# ============================================================
# MINECRAFT 26.2 TEST SCRIPT
# PHASE 1
#
# Safe / Direct m.execute Version
#
# Minecraft Java Edition 26.2
# MineScript
#
# ============================================================
#
# IMPORTANT
#
# ・関数は使用しない
# ・Minecraftコマンドはすべて m.execute() を直接使用
# ・Armor Standのequipment一括指定は使用しない
# ・Armor Standは summon 後に1部位ずつ装備
# ・Armor Standの対象指定は nearest を使用
#
# ============================================================


import minescript as m
import math
import time


# ============================================================
# SETTINGS
# ============================================================

HEAD_NAME = "crocadooo"

COMMAND_DELAY = 0.05


# ============================================================
# START
# ============================================================

m.echo("================================")
m.echo("PHASE 1 DIRECT EXECUTE TEST")
m.echo("================================")


# ============================================================
# GET PLAYER POSITION
# ============================================================

m.echo("GET PLAYER POSITION")

player = m.player()

px, py, pz = player.position

x = math.floor(px)
y = math.floor(py)
z = math.floor(pz)

print(f"PLAYER POSITION: {px} {py} {pz}")
print(f"BASE POSITION: {x} {y} {z}")


# ============================================================
# INITIAL SETTINGS
# ============================================================

m.echo("INITIAL SETTINGS")


# Difficulty
m.execute("difficulty easy")
time.sleep(COMMAND_DELAY)


# Time
m.execute("time set night")
time.sleep(COMMAND_DELAY)


# Clear inventory
m.execute("clear @a")
time.sleep(COMMAND_DELAY)


# ============================================================
# CREATE TEST AREA
# ============================================================

m.echo("CREATE TEST AREA")


# ============================================================
# GROUND
#
# 51 x 1 x 51
# ============================================================

m.echo("CREATE GROUND")

m.execute(
    f"fill "
    f"{x - 25} {y - 1} {z - 25} "
    f"{x + 25} {y - 1} {z + 25} "
    f"minecraft:grass_block"
)

time.sleep(COMMAND_DELAY)


# ============================================================
# CLEAR LOWER AREA
#
# 51 x 12 x 51
#
# Y 0 ～ 11
# ============================================================

m.echo("CLEAR LOWER AREA")

m.execute(
    f"fill "
    f"{x - 25} {y} {z - 25} "
    f"{x + 25} {y + 11} {z + 25} "
    f"minecraft:air"
)

time.sleep(COMMAND_DELAY)


# ============================================================
# CLEAR UPPER AREA
#
# Y 12 ～ 20
# ============================================================

m.echo("CLEAR UPPER AREA")

m.execute(
    f"fill "
    f"{x - 25} {y + 12} {z - 25} "
    f"{x + 25} {y + 20} {z + 25} "
    f"minecraft:air"
)

time.sleep(COMMAND_DELAY)


# ============================================================
# ARMOR STAND 1
#
# Position:
#   X -14
#   Y  0
#   Z -5
#
# Player Head
# Iron Armor
#
# ============================================================

m.echo("================================")
m.echo("ARMOR STAND 1")
m.echo("================================")


# ------------------------------------------------------------
# SUMMON
# ------------------------------------------------------------

m.echo("AS1 SUMMON")

m.execute(
    f"summon minecraft:armor_stand "
    f"{x - 14} {y} {z - 5} "
    f"{{"
    f"ShowArms:1b,"
    f"NoGravity:1b,"
    f"PersistenceRequired:1b"
    f"}}"
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# TARGET
#
# 直前に召喚したArmor Standをnearestで取得
# ------------------------------------------------------------

m.echo("AS1 HEAD")

m.execute(
    f'item replace entity '
    f'@e[type=minecraft:armor_stand,sort=nearest,limit=1] '
    f'armor.head with '
    f'minecraft:player_head[profile={{name:"{HEAD_NAME}"}}]'
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# CHEST
# ------------------------------------------------------------

m.echo("AS1 CHEST")

m.execute(
    f'item replace entity '
    f'@e[type=minecraft:armor_stand,sort=nearest,limit=1] '
    f'armor.chest with '
    f'minecraft:iron_chestplate'
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# LEGS
# ------------------------------------------------------------

m.echo("AS1 LEGS")

m.execute(
    f'item replace entity '
    f'@e[type=minecraft:armor_stand,sort=nearest,limit=1] '
    f'armor.legs with '
    f'minecraft:iron_leggings'
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# FEET
# ------------------------------------------------------------

m.echo("AS1 FEET")

m.execute(
    f'item replace entity '
    f'@e[type=minecraft:armor_stand,sort=nearest,limit=1] '
    f'armor.feet with '
    f'minecraft:iron_boots'
)

time.sleep(COMMAND_DELAY)


# ============================================================
# ARMOR STAND 2
#
# Position:
#   X -13
#   Y  0
#   Z -5
#
# Wither Skeleton Skull
# Diamond Armor
#
# ============================================================

m.echo("================================")
m.echo("ARMOR STAND 2")
m.echo("================================")


# ------------------------------------------------------------
# SUMMON
# ------------------------------------------------------------

m.echo("AS2 SUMMON")

m.execute(
    f"summon minecraft:armor_stand "
    f"{x - 13} {y} {z - 5} "
    f"{{"
    f"ShowArms:1b,"
    f"NoGravity:1b,"
    f"PersistenceRequired:1b"
    f"}}"
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# HEAD
# ------------------------------------------------------------

m.echo("AS2 HEAD")

m.execute(
    f'item replace entity '
    f'@e[type=minecraft:armor_stand,sort=nearest,limit=1] '
    f'armor.head with '
    f'minecraft:wither_skeleton_skull'
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# CHEST
# ------------------------------------------------------------

m.echo("AS2 CHEST")

m.execute(
    f'item replace entity '
    f'@e[type=minecraft:armor_stand,sort=nearest,limit=1] '
    f'armor.chest with '
    f'minecraft:diamond_chestplate'
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# LEGS
# ------------------------------------------------------------

m.echo("AS2 LEGS")

m.execute(
    f'item replace entity '
    f'@e[type=minecraft:armor_stand,sort=nearest,limit=1] '
    f'armor.legs with '
    f'minecraft:diamond_leggings'
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# FEET
# ------------------------------------------------------------

m.echo("AS2 FEET")

m.execute(
    f'item replace entity '
    f'@e[type=minecraft:armor_stand,sort=nearest,limit=1] '
    f'armor.feet with '
    f'minecraft:diamond_boots'
)

time.sleep(COMMAND_DELAY)


# ============================================================
# ARMOR STAND 3
#
# Position:
#   X -12
#   Y  0
#   Z -5
#
# Netherite Armor
#
# ============================================================

m.echo("================================")
m.echo("ARMOR STAND 3")
m.echo("================================")


# ------------------------------------------------------------
# SUMMON
# ------------------------------------------------------------

m.echo("AS3 SUMMON")

m.execute(
    f"summon minecraft:armor_stand "
    f"{x - 12} {y} {z - 5} "
    f"{{"
    f"ShowArms:1b,"
    f"NoGravity:1b,"
    f"PersistenceRequired:1b"
    f"}}"
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# HEAD
# ------------------------------------------------------------

m.echo("AS3 HEAD")

m.execute(
    f'item replace entity '
    f'@e[type=minecraft:armor_stand,sort=nearest,limit=1] '
    f'armor.head with '
    f'minecraft:netherite_helmet'
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# CHEST
# ------------------------------------------------------------

m.echo("AS3 CHEST")

m.execute(
    f'item replace entity '
    f'@e[type=minecraft:armor_stand,sort=nearest,limit=1] '
    f'armor.chest with '
    f'minecraft:netherite_chestplate'
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# LEGS
# ------------------------------------------------------------

m.echo("AS3 LEGS")

m.execute(
    f'item replace entity '
    f'@e[type=minecraft:armor_stand,sort=nearest,limit=1] '
    f'armor.legs with '
    f'minecraft:netherite_leggings'
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# FEET
# ------------------------------------------------------------

m.echo("AS3 FEET")

m.execute(
    f'item replace entity '
    f'@e[type=minecraft:armor_stand,sort=nearest,limit=1] '
    f'armor.feet with '
    f'minecraft:netherite_boots'
)

time.sleep(COMMAND_DELAY)


# ============================================================
# BASIC BLOCKS
# ============================================================

m.echo("================================")
m.echo("CREATE BASIC BLOCKS")
m.echo("================================")


# ------------------------------------------------------------
# CHISELED BOOKSHELF
# ------------------------------------------------------------

m.execute(
    f"setblock "
    f"{x - 10} {y} {z - 5} "
    f"minecraft:chiseled_bookshelf"
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# ENCHANTING TABLE
# ------------------------------------------------------------

m.execute(
    f"setblock "
    f"{x - 9} {y} {z - 5} "
    f"minecraft:enchanting_table"
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# BREWING STAND
# ------------------------------------------------------------

m.execute(
    f"setblock "
    f"{x - 8} {y} {z - 5} "
    f"minecraft:brewing_stand"
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# BLAST FURNACE
# ------------------------------------------------------------

m.execute(
    f"setblock "
    f"{x - 7} {y} {z - 5} "
    f"minecraft:blast_furnace[facing=south]"
)

time.sleep(COMMAND_DELAY)


# ============================================================
# DOUBLE CHEST
# ============================================================

m.echo("================================")
m.echo("CREATE DOUBLE CHEST")
m.echo("================================")


# ------------------------------------------------------------
# RIGHT CHEST
# ------------------------------------------------------------

m.execute(
    f"setblock "
    f"{x - 6} {y} {z - 5} "
    f"minecraft:chest[facing=south,type=right]"
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# LEFT CHEST
# ------------------------------------------------------------

m.execute(
    f"setblock "
    f"{x - 5} {y} {z - 5} "
    f"minecraft:chest[facing=south,type=left]"
)

time.sleep(COMMAND_DELAY)


# ============================================================
# CHEST ITEMS
#
# Chest position:
# X -6
# Y  0
# Z -5
#
# ============================================================

m.echo("================================")
m.echo("SET CHEST ITEMS")
m.echo("================================")


# ------------------------------------------------------------
# SLOT 0
# Cobblestone x64
# ------------------------------------------------------------

m.execute(
    f"item replace block "
    f"{x - 6} {y} {z - 5} "
    f"container.0 "
    f"with minecraft:cobblestone 64"
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# SLOT 1
# Iron Ingot x64
# ------------------------------------------------------------

m.execute(
    f"item replace block "
    f"{x - 6} {y} {z - 5} "
    f"container.1 "
    f"with minecraft:iron_ingot 64"
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# SLOT 2
# Stone Pickaxe
# ------------------------------------------------------------

m.execute(
    f"item replace block "
    f"{x - 6} {y} {z - 5} "
    f"container.2 "
    f"with minecraft:stone_pickaxe 1"
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# SLOT 3
# Shield
# ------------------------------------------------------------

m.execute(
    f"item replace block "
    f"{x - 6} {y} {z - 5} "
    f"container.3 "
    f"with minecraft:shield 1"
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# SLOT 4
# Bow
# ------------------------------------------------------------

m.execute(
    f"item replace block "
    f"{x - 6} {y} {z - 5} "
    f"container.4 "
    f"with minecraft:bow 1"
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# SLOT 5
# Arrow x64
# ------------------------------------------------------------

m.execute(
    f"item replace block "
    f"{x - 6} {y} {z - 5} "
    f"container.5 "
    f"with minecraft:arrow 64"
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# SLOT 6
# Trident
# ------------------------------------------------------------

m.execute(
    f"item replace block "
    f"{x - 6} {y} {z - 5} "
    f"container.6 "
    f"with minecraft:trident 1"
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# SLOT 7
# Obsidian x64
# ------------------------------------------------------------

m.execute(
    f"item replace block "
    f"{x - 6} {y} {z - 5} "
    f"container.7 "
    f"with minecraft:obsidian 64"
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# SLOT 8
# Crying Obsidian x64
# ------------------------------------------------------------

m.execute(
    f"item replace block "
    f"{x - 6} {y} {z - 5} "
    f"container.8 "
    f"with minecraft:crying_obsidian 64"
)

time.sleep(COMMAND_DELAY)


# ------------------------------------------------------------
# SLOT 9
# Diamond x64
# ------------------------------------------------------------

m.execute(
    f"item replace block "
    f"{x - 6} {y} {z - 5} "
    f"container.9 "
    f"with minecraft:diamond 64"
)

time.sleep(COMMAND_DELAY)


# ============================================================
# COMPLETE
# ============================================================

m.echo("================================")
m.echo("PHASE 1 DIRECT EXECUTE COMPLETE")
m.echo("================================")

print("PHASE 1 DIRECT EXECUTE COMPLETE")
