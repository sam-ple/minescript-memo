# ============================================================
# Minecraft 26.2 Compatibility Test Stage Generator
#
# Minecraft Java Edition 26.2 + Paper + MineScript
#
# Purpose:
#   Minecraftの様々な機能が26.2環境で正常に動作するか確認する
#
# Main Features:
#   ・フィールド整地
#   ・アーマースタンド装備
#   ・各種ブロック
#   ・ダブルチェスト＋アイテム投入
#   ・村人
#   ・Mob
#   ・看板
#   ・コマンドブロック
#   ・クリックイベント付き看板
#   ・コンパス＋スニークTP
#   ・水・溶岩
#   ・ネザーゲート
#   ・アイテム配布
#   ・オオカミバリエーション
#   ・猫バリエーション
#   ・カエルバリエーション
#
# 26.2 Compatibility Policy:
#   ・Entity NBTは26.2で動作実績のある形式を使用
#   ・チェスト内容投入は /data merge block ではなく
#     /item replace block を使用
#   ・アイテムは新しいcomponents形式を優先
#
# ============================================================

import minescript as m
import math


# ============================================================
# BASIC FUNCTIONS
# ============================================================

def cmd(command):
    """
    Minecraftコマンドを実行する簡易関数
    """
    m.execute(command)


# ============================================================
# PLAYER POSITION
# ============================================================

# スクリプト実行時のプレイヤー位置を取得
p = m.player()
px, py, pz = p.position

# 小数点座標を整数化
x = math.floor(px)
y = math.floor(py)
z = math.floor(pz)


def pos(dx=0, dy=0, dz=0):
    """
    基準座標からの相対位置を絶対座標に変換する

    例:
        pos(1, 0, -5)

    → 基準位置から
        X +1
        Y +0
        Z -5
    """
    return f"{x + dx} {y + dy} {z + dz}"


# ============================================================
# INITIAL SETTINGS
# ============================================================

# モンスター自然スポーン停止
cmd("gamerule spawnMonsters false")

# 難易度
cmd("difficulty easy")

# 夜に設定
cmd("time set night")

# 全プレイヤーのインベントリをクリア
cmd("clear @a")

# プレイヤーの向きを北向きにする
cmd("tp @p ~ ~ ~ 180 0")


# ============================================================
# FIELD PREPARATION
# ============================================================

# ------------------------------------------------------------
# 地面
#
# 基準位置のY-1に草ブロックを敷く
# ------------------------------------------------------------

cmd(
    f"fill "
    f"{pos(-25, -1, -25)} "
    f"{pos(25, -1, 25)} "
    f"minecraft:grass_block"
)


# ------------------------------------------------------------
# 建築エリアを空気にする
#
# 51 × 21 × 51程度の空間を確保
# ------------------------------------------------------------

cmd(
    f"fill "
    f"{pos(-25, 0, -25)} "
    f"{pos(25, 9, 25)} "
    f"minecraft:air"
)

cmd(
    f"fill "
    f"{pos(-25, 10, -25)} "
    f"{pos(25, 20, 25)} "
    f"minecraft:air"
)


# ============================================================
# DISPLAY ENTITIES
#
# Z = -5 ラインに各種Entity・Blockを配置
# ============================================================

ROT = "[0f,0f]"

# プレイヤーヘッドに使用するプレイヤー名
HEAD_NAME = "crocadooo"


# ============================================================
# ARMOR STANDS
# ============================================================

# ------------------------------------------------------------
# 鉄装備アーマースタンド
#
# 26.x系のequipment形式を使用
# ------------------------------------------------------------

cmd(
    f'/summon minecraft:armor_stand {pos(-14, 0, -5)} '
    f'{{'
    f'ShowArms:true,'
    f'NoGravity:true,'
    f'PersistenceRequired:true,'
    f'equipment:{{'
    f'head:{{'
    f'id:"minecraft:player_head",'
    f'Count:1,'
    f'components:{{'
    f'profile:{{name:"{HEAD_NAME}"}}'
    f'}}'
    f'}},'
    f'chest:{{id:"minecraft:iron_chestplate",Count:1}},'
    f'legs:{{id:"minecraft:iron_leggings",Count:1}},'
    f'feet:{{id:"minecraft:iron_boots",Count:1}}'
    f'}}'
    f'}}'
)


# ------------------------------------------------------------
# ダイヤ装備アーマースタンド
# ------------------------------------------------------------

cmd(
    f'/summon minecraft:armor_stand {pos(-13, 0, -5)} '
    f'{{'
    f'ShowArms:true,'
    f'NoGravity:true,'
    f'PersistenceRequired:true,'
    f'equipment:{{'
    f'head:{{id:"minecraft:wither_skeleton_skull",Count:1}},'
    f'chest:{{id:"minecraft:diamond_chestplate",Count:1}},'
    f'legs:{{id:"minecraft:diamond_leggings",Count:1}},'
    f'feet:{{id:"minecraft:diamond_boots",Count:1}}'
    f'}}'
    f'}}'
)


# ------------------------------------------------------------
# ネザライト装備アーマースタンド
# ------------------------------------------------------------

cmd(
    f'/summon minecraft:armor_stand {pos(-12, 0, -5)} '
    f'{{'
    f'ShowArms:1b,'
    f'NoGravity:1b,'
    f'PersistenceRequired:1b,'
    f'equipment:{{'
    f'head:{{id:"minecraft:netherite_helmet",Count:1}},'
    f'chest:{{id:"minecraft:netherite_chestplate",Count:1}},'
    f'legs:{{id:"minecraft:netherite_leggings",Count:1}},'
    f'feet:{{id:"minecraft:netherite_boots",Count:1}}'
    f'}}'
    f'}}'
)


# ============================================================
# BLOCK DISPLAY
# ============================================================

# ------------------------------------------------------------
# 模様入り本棚
# ------------------------------------------------------------

cmd(
    f"setblock "
    f"{pos(-10, 0, -5)} "
    f"minecraft:chiseled_bookshelf"
)


# ------------------------------------------------------------
# エンチャントテーブル
# ------------------------------------------------------------

cmd(
    f"setblock "
    f"{pos(-9, 0, -5)} "
    f"minecraft:enchanting_table"
)


# ------------------------------------------------------------
# 醸造台
# ------------------------------------------------------------

cmd(
    f"setblock "
    f"{pos(-8, 0, -5)} "
    f"minecraft:brewing_stand"
)


# ------------------------------------------------------------
# 溶鉱炉
# ------------------------------------------------------------

cmd(
    f"setblock "
    f"{pos(-7, 0, -5)} "
    f"minecraft:blast_furnace[facing=south]"
)


# ============================================================
# DOUBLE CHEST
# ============================================================

# ------------------------------------------------------------
# ダブルチェストを生成
#
# 左右のchest typeを正しく指定
# ------------------------------------------------------------

cmd(
    f"setblock "
    f"{pos(-6, 0, -5)} "
    f"minecraft:chest[facing=south,type=right]"
)

cmd(
    f"setblock "
    f"{pos(-5, 0, -5)} "
    f"minecraft:chest[facing=south,type=left]"
)


# ------------------------------------------------------------
# チェストへアイテム投入
#
# 旧コード:
#   /data merge block {Items:[...]}
#
# 26.2対応方針:
#   /item replace block
#
# TETSUSEN BASE GENERATORで26.2動作確認済み方式
# ------------------------------------------------------------

chest_x = x - 6
chest_y = y
chest_z = z - 5


CHEST_ITEMS = [
    # 基本素材
    ("minecraft:cobblestone", 64),
    ("minecraft:iron_ingot", 64),

    # ツール・装備
    ("minecraft:stone_pickaxe", 1),
    ("minecraft:shield", 1),
    ("minecraft:bow", 1),
    ("minecraft:arrow", 64),
    ("minecraft:trident", 1),

    # ブロック
    ("minecraft:obsidian", 64),
    ("minecraft:crying_obsidian", 64),

    # レアアイテム
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


# 左側チェストの各スロットに投入
#
# ダブルチェストなので、
# 左チェスト側 container.0 ～ container.26
# を使用

for slot, (item_id, count) in enumerate(CHEST_ITEMS):

    cmd(
        f"item replace block "
        f"{chest_x} {chest_y} {chest_z} "
        f"container.{slot} "
        f"with {item_id} {count}"
    )


# ============================================================
# BED
# ============================================================

# ------------------------------------------------------------
# 赤いベッド
#
# footとheadを別々に配置
# ------------------------------------------------------------

cmd(
    f"setblock "
    f"{pos(-4, 0, -5)} "
    f"minecraft:red_bed[facing=south,part=foot]"
)

cmd(
    f"setblock "
    f"{pos(-4, 0, -4)} "
    f"minecraft:red_bed[facing=south,part=head]"
)


# ============================================================
# VILLAGER
# ============================================================

# ------------------------------------------------------------
# 農民村人
#
# ・レベル5
# ・AIなし
# ・無敵
# ・雪玉との交換
# ------------------------------------------------------------

cmd(
    (
        f"""
        summon minecraft:villager {pos(-3, 0, -5)} {{
            VillagerData:{{
                level:5,
                profession:"farmer",
                type:"plains"
            }},
            Silent:1b,
            Invulnerable:1b,
            NoAI:1b,
            Offers:{{
                Recipes:[
                    {{
                        buy:{{id:"minecraft:emerald",count:1}},
                        sell:{{id:"minecraft:snowball",count:1}},
                        maxUses:9999
                    }}
                ]
            }}
        }}
        """
    ).replace("\n", "").replace(" ", "")
)


# ============================================================
# SKELETON
# ============================================================

# ------------------------------------------------------------
# 動かないスケルトン
#
# ・AIなし
# ・体力2
# ・消えない
# ------------------------------------------------------------

cmd(
    f"summon minecraft:skeleton "
    f"{pos(-2, 0, -5)} "
    f'{{'
    f'NoAI:1b,'
    f'PersistenceRequired:1b,'
    f'Health:2f,'
    f'Rotation:{ROT}'
    f'}}'
)


# ============================================================
# SIGN
# ============================================================

# ------------------------------------------------------------
# 普通の看板
# ------------------------------------------------------------

cmd(
    f'setblock '
    f'{pos(-1, 0, -5)} '
    f'minecraft:oak_sign[rotation=0]'
    f'{{'
    f'front_text:{{'
    f'messages:["","crocadooo","",""]'
    f'}}'
    f'}}'
)


# ============================================================
# CRAFTING TABLE
# ============================================================

cmd(
    f"setblock "
    f"{pos(0, 0, -5)} "
    f"minecraft:crafting_table"
)


# ============================================================
# ANIMALS / FRIENDLY MOBS
# ============================================================

# ------------------------------------------------------------
# オウム
# ------------------------------------------------------------

cmd(
    f"summon minecraft:parrot "
    f"{pos(1, 0, -5)} "
    f'{{'
    f'NoAI:1b,'
    f'Silent:1b,'
    f'Rotation:{ROT}'
    f'}}'
)


# ------------------------------------------------------------
# アルマジロ
# ------------------------------------------------------------

cmd(
    f"summon minecraft:armadillo "
    f"{pos(2, 0, -5)} "
    f'{{'
    f'NoAI:1b,'
    f'Silent:1b,'
    f'Rotation:{ROT}'
    f'}}'
)


# ------------------------------------------------------------
# アレイ
# ------------------------------------------------------------

cmd(
    f"summon minecraft:allay "
    f"{pos(3, 0, -5)} "
    f'{{'
    f'Silent:1b,'
    f'NoGravity:1b,'
    f'PersistenceRequired:1b'
    f'}}'
)


# ============================================================
# GOLD BLOCK TRIGGER
# ============================================================

# ------------------------------------------------------------
# 金ブロックを踏むと怪しげな砂を生成する仕掛け
#
# 金ブロックの下にリピートコマンドブロックを配置
# ------------------------------------------------------------

# プレイヤーが踏む金ブロック
cmd(
    f"setblock "
    f"{pos(10, -1, -5)} "
    f"minecraft:gold_block"
)


# 地下のリピートコマンドブロック
gold_trigger_command = (
    f"execute as @a at @s "
    f"if block ~ ~-1 ~ minecraft:gold_block "
    f"run setblock {pos(10, 0, -7)} minecraft:suspicious_sand"
)


cmd(
    f'setblock '
    f'{pos(10, -2, -5)} '
    f'minecraft:repeating_command_block'
    f'{{'
    f'auto:1b,'
    f'Command:"{gold_trigger_command}"'
    f'}}'
)


# ============================================================
# TELEPORT BUTTON SYSTEM
# ============================================================

# ------------------------------------------------------------
# 地下にコマンドブロックを設置
#
# ボタンを押すと基準地点へTP
# ------------------------------------------------------------

teleport_command = f"tp @p {pos(0, 1, 0)}"

cmd(
    f'setblock '
    f'{pos(11, -1, -5)} '
    f'minecraft:command_block'
    f'{{'
    f'Command:"{teleport_command}"'
    f'}}'
)


# ------------------------------------------------------------
# コマンドブロックの上に見た目用の石
# ------------------------------------------------------------

cmd(
    f"setblock "
    f"{pos(11, 0, -5)} "
    f"minecraft:stone"
)


# ------------------------------------------------------------
# 石の側面にボタン
# ------------------------------------------------------------

cmd(
    f"setblock "
    f"{pos(11, 0, -4)} "
    f"minecraft:stone_button[facing=south]"
)


# ============================================================
# CLICKABLE SIGN
# ============================================================

# ------------------------------------------------------------
# クリックイベント付き看板
#
# 「ダイヤGET」をクリックするとダイヤを取得
#
# ※26.2で実際に要テスト
# ------------------------------------------------------------

# 看板設置
cmd(
    f"setblock "
    f"{pos(12, 0, -5)} "
    f"minecraft:oak_sign"
)


# 看板テキスト＋クリックイベント設定
clickable_sign_data = (
    '{"front_text":{"messages":['
    '"{\\"text\\":\\"ダイヤGET\\",'
    '\\"clickEvent\\":{'
    '\\"action\\":\\"run_command\\",'
    '\\"value\\":\\"give @s minecraft:diamond 1\\"'
    '}}"'
    ',"","",""]}}'
)


cmd(
    f"data merge block "
    f"{pos(12, 0, -5)} "
    f"{clickable_sign_data}"
)


# ============================================================
# COMPASS + SNEAK TELEPORT SYSTEM
# ============================================================

# ------------------------------------------------------------
# スコアボード作成
#
# sneak_time:
# プレイヤーがしゃがんだ時間を記録
# ------------------------------------------------------------

cmd(
    "scoreboard objectives add "
    "isSneaking "
    "minecraft.custom:minecraft.sneak_time"
)


# ------------------------------------------------------------
# コンパスを持ってしゃがんだ場合
# 基準地点へTP
# ------------------------------------------------------------

tp_cmd = (
    f'execute as @a['
    f'nbt={{SelectedItem:{{id:"minecraft:compass"}}}}'
    f'] '
    f'if score @s isSneaking matches 1.. '
    f'run tp @s {pos(0, 1, 0)}'
)


# ダブルクォーテーションをエスケープ
tp_cmd_escaped = tp_cmd.replace('"', '\\"')


# リピートコマンドブロック
cmd(
    f'setblock '
    f'{pos(0, -2, 0)} '
    f'minecraft:repeating_command_block'
    f'{{'
    f'auto:1b,'
    f'Command:"{tp_cmd_escaped}"'
    f'}}'
)


# ------------------------------------------------------------
# スニークスコアをリセット
#
# リセットしないと一度しゃがんだ後、
# 永久にTP条件が成立し続けるため重要
# ------------------------------------------------------------

reset_cmd = (
    "scoreboard players set @a isSneaking 0"
).replace('"', '\\"')


cmd(
    f'setblock '
    f'{pos(1, -2, 0)} '
    f'minecraft:repeating_command_block'
    f'{{'
    f'auto:1b,'
    f'Command:"{reset_cmd}"'
    f'}}'
)


# ============================================================
# WATER / LAVA AREA
# ============================================================

# ------------------------------------------------------------
# 水エリア
# ------------------------------------------------------------

cmd(
    f"fill "
    f"{pos(-5, -1, 0)} "
    f"{pos(-2, -1, 1)} "
    f"minecraft:water"
)


# ------------------------------------------------------------
# 溶岩エリア
# ------------------------------------------------------------

cmd(
    f"fill "
    f"{pos(2, -1, 0)} "
    f"{pos(2, -1, 1)} "
    f"minecraft:lava"
)


# ------------------------------------------------------------
# 水中Mob
# ------------------------------------------------------------

cmd(
    f"summon minecraft:axolotl "
    f"{pos(-3, -1, 0)} "
    f'{{NoAI:1b}}'
)

cmd(
    f"summon minecraft:tadpole "
    f"{pos(-5, -1, 1)} "
    f'{{NoAI:1b}}'
)


# ============================================================
# NETHER PORTAL
# ============================================================

# ------------------------------------------------------------
# ネザーゲート枠を生成
# ------------------------------------------------------------

BASE_X = 5
BASE_Y = -1
BASE_Z = -5


for dy in range(5):

    for dx in range(4):

        # 外枠だけ黒曜石
        if dx in [0, 3] or dy in [0, 4]:
            block = "minecraft:obsidian"
        else:
            block = "minecraft:air"

        cmd(
            f"setblock "
            f"{pos(BASE_X + dx, BASE_Y + dy, BASE_Z)} "
            f"{block}"
        )


# ------------------------------------------------------------
# ネザーゲート点火
# ------------------------------------------------------------

cmd(
    f"setblock "
    f"{pos(BASE_X + 1, BASE_Y + 1, BASE_Z)} "
    f"minecraft:fire"
)


# ============================================================
# ITEM DISTRIBUTION
# ============================================================

# ------------------------------------------------------------
# 全プレイヤーへアイテム配布
#
# エンチャントは新しいcomponents形式
# ------------------------------------------------------------

items = [

    # エンチャント付き釣竿
    (
        'minecraft:fishing_rod'
        '[enchantments={'
        '"minecraft:luck_of_the_sea":3,'
        '"minecraft:lure":3,'
        '"minecraft:unbreaking":3,'
        '"minecraft:mending":1'
        '}] 1'
    ),

    # 各種アイテム
    "minecraft:emerald 64",
    "minecraft:bone 64",
    "minecraft:glow_ink_sac 64",
    "minecraft:copper_ingot 64",
    "minecraft:feather 64",
    "minecraft:stick 64",
    "minecraft:suspicious_sand 64",
    "minecraft:compass 1",
]


for item in items:

    cmd(
        f"give @a {item}"
    )


# ============================================================
# WOLF VARIANTS
# ============================================================

# ------------------------------------------------------------
# 26.2で存在するオオカミバリエーションを横一列に配置
# ------------------------------------------------------------

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
    "grumpy",
]


base_x = -11
z_line = -10


for i, variant in enumerate(WOLF_VARIANTS):

    cmd(
        f"summon minecraft:wolf "
        f"{pos(base_x + i, 0, z_line)} "
        f'{{'
        f'NoAI:1b,'
        f'Sitting:1b,'
        f'Silent:1b,'
        f'CollarColor:14b,'
        f'variant:"minecraft:{variant}",'
        f'sound_variant:"minecraft:{variant}"'
        f'}}'
    )


# ------------------------------------------------------------
# 骨チェスト
#
# /item replace block方式
# ------------------------------------------------------------

wolf_chest_x = x - 12
wolf_chest_y = y
wolf_chest_z = z - 10


cmd(
    f"setblock "
    f"{wolf_chest_x} {wolf_chest_y} {wolf_chest_z} "
    f"minecraft:chest[facing=south]"
)


for slot in range(8):

    cmd(
        f"item replace block "
        f"{wolf_chest_x} {wolf_chest_y} {wolf_chest_z} "
        f"container.{slot} "
        f"with minecraft:bone 64"
    )


# ============================================================
# CAT VARIANTS
# ============================================================

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
    "all_black",
]


base_x = -11
z_line = -14


for i, variant in enumerate(CAT_VARIANTS):

    cmd(
        f"summon minecraft:cat "
        f"{pos(base_x + i, 0, z_line)} "
        f'{{'
        f'NoAI:1b,'
        f'Sitting:1b,'
        f'Silent:1b,'
        f'variant:"minecraft:{variant}"'
        f'}}'
    )


# ------------------------------------------------------------
# 魚チェスト
# ------------------------------------------------------------

cat_chest_x = x - 12
cat_chest_y = y
cat_chest_z = z - 14


cmd(
    f"setblock "
    f"{cat_chest_x} {cat_chest_y} {cat_chest_z} "
    f"minecraft:chest[facing=south]"
)


CAT_CHEST_ITEMS = [

    ("minecraft:cod", 64),
    ("minecraft:cod", 64),
    ("minecraft:salmon", 64),
    ("minecraft:salmon", 64),
]


for slot, (item_id, count) in enumerate(CAT_CHEST_ITEMS):

    cmd(
        f"item replace block "
        f"{cat_chest_x} {cat_chest_y} {cat_chest_z} "
        f"container.{slot} "
        f"with {item_id} {count}"
    )


# ============================================================
# FROG VARIANTS
# ============================================================

FROG_VARIANTS = [

    "temperate",
    "warm",
    "cold",
]


base_x = -11
z_line = -18


for i, variant in enumerate(FROG_VARIANTS):

    cmd(
        f"summon minecraft:frog "
        f"{pos(base_x + i, 0, z_line)} "
        f'{{'
        f'NoAI:1b,'
        f'Silent:1b,'
        f'variant:"minecraft:{variant}"'
        f'}}'
    )


# ------------------------------------------------------------
# リードチェスト
# ------------------------------------------------------------

frog_chest_x = x - 12
frog_chest_y = y
frog_chest_z = z - 18


cmd(
    f"setblock "
    f"{frog_chest_x} {frog_chest_y} {frog_chest_z} "
    f"minecraft:chest[facing=south]"
)


for slot in range(3):

    cmd(
        f"item replace block "
        f"{frog_chest_x} {frog_chest_y} {frog_chest_z} "
        f"container.{slot} "
        f"with minecraft:lead 64"
    )


# ============================================================
# COMPLETE
# ============================================================

m.echo(
    "Minecraft 26.2 Compatibility Test Stage completed."
)
