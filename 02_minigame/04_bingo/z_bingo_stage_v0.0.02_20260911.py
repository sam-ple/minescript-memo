# ============================================================
# BINGO STAGE GENERATOR
#
# Minecraft Java Edition + MineScript
#
# Version : v0.2.00
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
#
# IMPORTANT
#
#   盤面座標は以前動作していたものを維持。
#
#   BOARD:
#       base_x + 1 ～ +3
#
#   INPUT:
#       base_x
#
#   INPUT FRAME:
#       base_x / y+1 / base_z+1
#
#   SMALL PLAYER HEAD:
#       base_x+2 / y+1 / base_z+3
#
#   Skript側で盤面のみ1ブロック右へ補正する。
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
#
# TEAM 1 : -20
# TEAM 2 : -10
# TEAM 3 :   0
# TEAM 4 : +10
# TEAM 5 : +20
#
SET_OFFSETS = [-20, -10, 0, 10, 20]


# 盤面のZ位置
BOARD_Z_OFFSET = -7


# 会場サイズ
AREA_RADIUS = 30


# ============================================================
# BLOCK SETTINGS
# ============================================================

# 地面
FLOOR_BLOCK = "minecraft:grass_block"


# 盤面下部
BASE_BLOCK = "minecraft:quartz_block"


# 盤面背面
#
# Skriptが達成時に
# white_stained_glass → gold_block
# に変更する。
#
FRAME_BLOCK = "minecraft:white_stained_glass"


# 入力エリア
INPUT_BASE_BLOCK = "minecraft:emerald_block"

INPUT_STONE_BLOCK = "minecraft:stone"


# 登録ボタン
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


    # ========================================================
    # ITEM FRAME
    # ========================================================

    m.execute(
        f"kill @e[type=minecraft:item_frame,"
        f"x={x-AREA_RADIUS},y={y-5},z={z-AREA_RADIUS},"
        f"dx={AREA_RADIUS*2},dy=30,dz={AREA_RADIUS*2}]"
    )


    # ========================================================
    # GLOW ITEM FRAME
    # ========================================================

    m.execute(
        f"kill @e[type=minecraft:glow_item_frame,"
        f"x={x-AREA_RADIUS},y={y-5},z={z-AREA_RADIUS},"
        f"dx={AREA_RADIUS*2},dy=30,dz={AREA_RADIUS*2}]"
    )


    # ========================================================
    # ITEM DISPLAY
    #
    # Skriptが生成する大型プレイヤーヘッド
    # ========================================================

    m.execute(
        f"kill @e[type=minecraft:item_display,"
        f"x={x-AREA_RADIUS},y={y-5},z={z-AREA_RADIUS},"
        f"dx={AREA_RADIUS*2},dy=30,dz={AREA_RADIUS*2}]"
    )


    # ========================================================
    # MARKER
    # ========================================================

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


    # ========================================================
    # FLOOR
    # ========================================================

    m.execute(
        f"fill "
        f"{x-AREA_RADIUS} {y-1} {z-AREA_RADIUS} "
        f"{x+AREA_RADIUS} {y-1} {z+AREA_RADIUS} "
        f"{FLOOR_BLOCK}"
    )


    # ========================================================
    # CLEAR SPACE
    # ========================================================

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

    # ========================================================
    # TEAM BASE
    # ========================================================

    base_x = x + offset
    base_z = z + BOARD_Z_OFFSET


    print(
        f"[BINGO] Building Team {si + 1}..."
    )


    # ========================================================
    # BOARD BASE
    #
    # 旧コードと同じ。
    #
    # X:
    #   base_x+1
    #   base_x+2
    #   base_x+3
    #
    # ========================================================

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
    #
    # 旧コードと同じ。
    #
    # ========================================================

    m.execute(
        f"fill "
        f"{base_x+1} {y+1} {base_z} "
        f"{base_x+3} {y+3} {base_z} "
        f"{FRAME_BLOCK}"
    )


    # ========================================================
    # 3x3 ITEM FRAMES
    #
    #   1 2 3
    #   4 5 6
    #   7 8 9
    #
    # 旧コードと同じ座標。
    #
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
            f'{{Facing:3b,Fixed:1b,Invulnerable:1b}}'
        )


    # ========================================================
    # SMALL PLAYER HEAD AREA
    #
    # 小さいプレイヤーヘッドを置く場所。
    #
    # 旧コードと同じ。
    #
    # base_x+2
    # base_z+3
    #
    # ========================================================

    head_x = base_x + 2
    head_z = base_z + 3


    # ========================================================
    # PLAYER HEAD BASE
    # ========================================================

    m.execute(
        f"setblock "
        f"{head_x} {y} {head_z} "
        f"{BASE_BLOCK}"
    )


    # ========================================================
    # INPUT AREA
    #
    # ★ここは変更しない
    #
    # Emerald
    # Stone
    # Input Frame
    #
    # 以前動作していた位置を維持。
    #
    # ========================================================

    input_x = base_x
    input_z = base_z


    # ========================================================
    # EMERALD BLOCK
    # ========================================================

    m.execute(
        f"setblock "
        f"{input_x} {y} {input_z} "
        f"{INPUT_BASE_BLOCK}"
    )


    # ========================================================
    # STONE BLOCK
    # ========================================================

    m.execute(
        f"setblock "
        f"{input_x} {y+1} {input_z} "
        f"{INPUT_STONE_BLOCK}"
    )


    # ========================================================
    # INPUT ITEM FRAME
    #
    # ★重要
    #
    # 以前動作していた座標を完全維持。
    #
    # X = base_x
    # Y = y+1
    # Z = base_z+1
    #
    # ========================================================

    m.execute(
        f'summon minecraft:item_frame '
        f'{input_x} {y+1} {input_z+1} '
        f'{{Facing:3b,Fixed:1b,Invulnerable:1b}}'
    )


    # ========================================================
    # REGISTER BUTTON
    #
    # 小さいプレイヤーヘッド用ブロックの
    # 「手前側」にボタンを配置。
    #
    # Head:
    #
    #   X = base_x+2
    #   Y = y
    #   Z = base_z+3
    #
    # Button:
    #
    #   X = base_x+2
    #   Y = y+1
    #   Z = base_z+2
    #
    # ========================================================

    button_x = base_x + 2
    button_y = y + 1
    button_z = base_z + 2


    m.execute(
        f"setblock "
        f"{button_x} {button_y} {button_z} "
        f"{BUTTON_BLOCK}"
        f"[face=wall,facing=south,powered=false]"
    )


    # ========================================================
    # BOARD MARKER
    #
    # 盤面中央下部。
    #
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
    print(" Version : v0.2.00")
    print("====================================")


    # ========================================================
    # CLEAN
    # ========================================================

    cleanup()


    # ========================================================
    # FLATTEN
    # ========================================================

    flatten()


    # ========================================================
    # BUILD 5 TEAMS
    # ========================================================

    for si, offset in enumerate(SET_OFFSETS):

        build_team(si, offset)


    # ========================================================
    # WORLD SPAWN
    # ========================================================

    m.execute(
        f"setworldspawn "
        f"{x} {y} {z}"
    )


    # ========================================================
    # PLAYER SPAWN
    # ========================================================

    m.execute(
        f"spawnpoint @a "
        f"{x} {y+1} {z}"
    )


    # ========================================================
    # CENTER MARKER
    #
    # Skriptの /bingo set で使用する
    # Originと同じ場所。
    #
    # ========================================================

    m.execute(
        f'summon minecraft:marker '
        f'{x} {y} {z} '
        f'{{Tags:["bingo_origin"]}}'
    )


    # ========================================================
    # COMPLETE
    # ========================================================

    print("")
    print("[BINGO] Stage Complete!")
    print(
        f"[BINGO] Origin: {x}, {y}, {z}"
    )
    print("")


# ============================================================
# MAIN
# ============================================================

build()
