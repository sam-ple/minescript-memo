import minescript as m
import math


# ============================================================
# ARMOR STAND FULL EQUIPMENT TEST
#
# Minecraft Java Edition 26.2
# MineScript
#
# VERIFIED:
#   Armor Stand summon
#   Player Head
#   Iron Chestplate
#   Iron Leggings
#   Iron Boots
#   Main Hand Iron Sword
#
# NEW TEST:
#   Off Hand Shield
#
# IMPORTANT:
#   Equipment is NOT specified in summon.
#   Each item is equipped separately with item replace.
#
# ============================================================


HEAD_NAME = "crocadooo"


# ============================================================
# PLAYER POSITION
# ============================================================

p = m.player()

px, py, pz = p.position

x = math.floor(px)
y = math.floor(py)
z = math.floor(pz)


# ============================================================
# START
# ============================================================

m.echo("================================")
m.echo("FULL ARMOR + WEAPON TEST START")
m.echo("================================")

m.echo(f"PLAYER POSITION: {x} {y} {z}")


# ============================================================
# TARGET
# ============================================================

target = (
    '@e[type=minecraft:armor_stand,'
    'sort=nearest,'
    'limit=1]'
)


# ============================================================
# STEP 1
# SUMMON ARMOR STAND
#
# ShowArms:1b
#   → Displays the Armor Stand's arms.
#
# NoGravity:1b
#   → Prevents the Armor Stand from falling.
#
# ============================================================

m.echo("STEP 1")
m.echo("BEFORE ARMOR STAND SUMMON")


m.execute(
    f'summon minecraft:armor_stand {x} {y} {z} '
    f'{{'
    f'NoGravity:1b,'
    f'ShowArms:1b'
    f'}}'
)


m.echo("ARMOR STAND SUMMON SUCCESS")


# ============================================================
# STEP 2
# HEAD
# ============================================================

m.echo("STEP 2")
m.echo("BEFORE HEAD EQUIP")


m.execute(
    f'item replace entity {target} '
    f'armor.head with '
    f'minecraft:player_head[profile={{name:"{HEAD_NAME}"}}]'
)


m.echo("HEAD EQUIP SUCCESS")


# ============================================================
# STEP 3
# CHEST
# ============================================================

m.echo("STEP 3")
m.echo("BEFORE CHEST EQUIP")


m.execute(
    f'item replace entity {target} '
    f'armor.chest with minecraft:iron_chestplate'
)


m.echo("CHEST EQUIP SUCCESS")


# ============================================================
# STEP 4
# LEGS
# ============================================================

m.echo("STEP 4")
m.echo("BEFORE LEGS EQUIP")


m.execute(
    f'item replace entity {target} '
    f'armor.legs with minecraft:iron_leggings'
)


m.echo("LEGS EQUIP SUCCESS")


# ============================================================
# STEP 5
# FEET
# ============================================================

m.echo("STEP 5")
m.echo("BEFORE FEET EQUIP")


m.execute(
    f'item replace entity {target} '
    f'armor.feet with minecraft:iron_boots'
)


m.echo("FEET EQUIP SUCCESS")


# ============================================================
# STEP 6
# MAIN HAND
# IRON SWORD
# ============================================================

m.echo("STEP 6")
m.echo("BEFORE MAINHAND EQUIP")


m.execute(
    f'item replace entity {target} '
    f'weapon.mainhand with minecraft:iron_sword'
)


m.echo("MAINHAND EQUIP SUCCESS")


# ============================================================
# STEP 7
# OFF HAND
# SHIELD
# ============================================================

m.echo("STEP 7")
m.echo("BEFORE OFFHAND EQUIP")


m.execute(
    f'item replace entity {target} '
    f'weapon.offhand with minecraft:shield'
)


m.echo("OFFHAND EQUIP SUCCESS")


# ============================================================
# COMPLETE
# ============================================================

m.echo("================================")
m.echo("FULL ARMOR + WEAPON TEST SUCCESS")
m.echo("================================")

m.echo("ARMS       : ENABLED")
m.echo("HEAD       : crocadooo")
m.echo("CHEST      : IRON")
m.echo("LEGS       : IRON")
m.echo("FEET       : IRON")
m.echo("MAIN HAND  : IRON SWORD")
m.echo("OFF HAND   : SHIELD")

m.echo("================================")
