# ============================================================
# BINGO STAGE GENERATOR
#
# Minecraft Java Edition + MineScript
#
# Version : v0.1.00
#
# ============================================================
#
# PURPOSE
#
#   BINGOゲーム用の会場を一括生成する。
#
#   MineScriptの担当は会場設営のみ。
#
#   ・整地
#   ・5部隊分の盤面
#   ・3x3 額縁
#   ・入力用額縁
#   ・プレイヤー登録ボタン
#   ・プレイヤーヘッド表示スペース
#
#   プレイヤー登録・アイテム・ゲーム進行は
#   すべて Skript 側で管理する。
#
# ============================================================

import minescript as m
import math


# ============================================================
# SETTINGS
# ============================================================

# 部隊数
TEAM_COUNT = 5

# 各部隊のX方向オフセット
SET_OFFSETS = [-20, -10, 0, 10, 20]

# 盤面のZ位置
BOARD_Z_OFFSET = -7

# 会場サイズ
AREA_RADIUS = 30


# ============================================================
# BLOCK SETTINGS
# ============================================================

FLOOR_BLOCK = "minecraft:grass_block"

BASE_BLOCK = "minecraft:quartz_block"

FRAME_BLOCK = "minecraft:white_stained_glass"

INPUT_BASE_BLOCK = "minecraft:emerald_block"

INPUT_STONE_BLOCK = "minecraft:stone"

BUTTON_BLOCK = "minecraft:stone_button"


# ============================================================
# PLAYER POSITION
# ============================================================

px, py, pz = m.player().position

x, y, z = map(math.floor, (px, py, pz))


# ============================================================
# CLEANUP
# ============================================================

def cleanup():

    print("[BINGO] Cleaning area...")

    # 額縁削除
    m.execute(
        f"kill @e[type=minecraft:item_frame,"
        f"x={x-AREA_RADIUS},y={y-5},z={z-AREA_RADIUS},"
        f"dx={AREA_RADIUS*2},dy=30,dz={AREA_RADIUS*2}]"
    )

    m.execute(
        f"kill @e[type=minecraft:glow_item_frame,"
        f"x={x-AREA_RADIUS},y={y-5},z={z-AREA_RADIUS},"
        f"dx={AREA_RADIUS*2},dy=30,dz={AREA_RADIUS*2}]"
    )

    # Skript側で生成する巨大ヘッド用 item_display
    m.execute(
        f"kill @e[type=minecraft:item_display,"
        f"x={x-AREA_RADIUS},y={y-5},z={z-AREA_RADIUS},"
        f"dx={AREA_RADIUS*2},dy=30,dz={AREA_RADIUS*2}]"
    )

    # marker削除
    m.execute(
        f"kill @e[type=minecraft:marker,"
        f"x={x-AREA_RADIUS},y={y-5},z={z-AREA_RADIUS},"
        f"dx={AREA_RADIUS*2},dy=30,dz={AREA_RADIUS*2}]"
    )


# ============================================================
# FLATTEN
# ============================================================

def flatten():

    print("[BINGO] Flattening area...")

    # 地面
    m.execute(
        f"fill "
        f"{x-AREA_RADIUS} {y-1} {z-AREA_RADIUS} "
        f"{x+AREA_RADIUS} {y-1} {z+AREA_RADIUS} "
        f"{FLOOR_BLOCK}"
    )

    # 空間確保
    m.execute(
        f"fill "
        f"{x-AREA_RADIUS} {y} {z-AREA_RADIUS} "
        f"{x+AREA_RADIUS} {y+15} {z+AREA_RADIUS} "
        f"minecraft:air"
    )


# ============================================================
# BUILD TEAM BOARD
# ============================================================

def build_team(si, offset):

    base_x = x + offset
    base_z = z + BOARD_Z_OFFSET

    print(f"[BINGO] Building Team {si + 1}...")


    # ========================================================
    # BOARD BASE
    # ========================================================

    # 盤面下部
    m.execute(
        f"fill "
        f"{base_x+1} {y} {base_z} "
        f"{base_x+3} {y} {base_z} "
        f"{BASE_BLOCK}"
    )


    # ========================================================
    # 3x3 BACK BLOCK
    #
    # 額縁の後ろ。
    # Skriptが達成時に gold_block に変更する。
    # ========================================================

    m.execute(
        f"fill "
        f"{base_x+1} {y+1} {base_z} "
        f"{base_x+3} {y+3} {base_z} "
        f"{FRAME_BLOCK}"
    )


    # ========================================================
    # 3x3 ITEM FRAMES
    # ========================================================

    for idx in range(9):

        dx = idx % 3
        dy = idx // 3

        fx = base_x + 1 + dx
        fy = y + 3 - dy
        fz = base_z + 1

        m.execute(
            f'summon minecraft:item_frame '
            f'{fx} {fy} {fz} '
            f'{{Facing:3b,Fixed:1b}}'
        )


    # ========================================================
    # PLAYER HEAD DISPLAY SPACE
    #
    # 実際のヘッドはSkriptが登録時に生成する。
    # ========================================================

    # プレイヤーヘッド下の台座
    m.execute(
        f"setblock "
        f"{base_x+2} {y} {base_z+3} "
        f"minecraft:quartz_block"
    )


    # ========================================================
    # INPUT AREA
    # ========================================================

    input_x = base_x
    input_z = base_z


    # エメラルド土台
    m.execute(
        f"setblock "
        f"{input_x} {y} {input_z} "
        f"{INPUT_BASE_BLOCK}"
    )


    # 石ブロック
    m.execute(
        f"setblock "
        f"{input_x} {y+1} {input_z} "
        f"{INPUT_STONE_BLOCK}"
    )


    # 入力用額縁
    m.execute(
        f'summon minecraft:item_frame '
        f'{input_x} {y+1} {input_z+1} '
        f'{{Facing:3b,Fixed:1b,Invulnerable:1b}}'
    )


    # 登録ボタン
    #
    # 石ブロック上部に設置
    m.execute(
        f"setblock "
        f"{input_x} {y+2} {input_z} "
        f"{BUTTON_BLOCK}[face=floor,facing=north,powered=false]"
    )


    # ========================================================
    # SLOT MARKER
    #
    # Skriptが座標を計算するため必須ではないが、
    # 会場識別用として marker を設置。
    # ========================================================

    m.execute(
        f'summon minecraft:marker '
        f'{base_x+2} {y} {base_z} '
        f'{{Tags:["bingo_board_{si+1}"]}}'
    )


# ============================================================
# BUILD
# ============================================================

def build():

    print("")
    print("====================================")
    print(" BINGO STAGE GENERATOR")
    print("====================================")

    cleanup()

    flatten()

    for si, offset in enumerate(SET_OFFSETS):

        build_team(si, offset)


    # ========================================================
    # SPAWN
    # ========================================================

    m.execute(f"setworldspawn {x} {y} {z}")

    m.execute(f"spawnpoint @a {x} {y+1} {z}")


    # ========================================================
    # CENTER MARKER
    #
    # Skriptの /bingo setup でも同じ座標を登録する。
    # ========================================================

    m.execute(
        f'summon minecraft:marker '
        f'{x} {y} {z} '
        f'{{Tags:["bingo_origin"]}}'
    )


    print("")
    print("[BINGO] Stage Complete!")
    print(f"[BINGO] Origin: {x}, {y}, {z}")
    print("")


# ============================================================
# MAIN
# ============================================================

build()
