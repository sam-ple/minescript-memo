その方針でいこう。
**MineScript＝看板・商人の設置、Skript＝ゲーム進行・役職・アイテム効果**に分けるのがきれいです。

最初は全部を入れず、まず **Phase 1** として、

* 2人まで看板登録
* 4パターンの役職切替
* 昼／夜の自動切替
* 実際のMinecraft時間も昼夜になる
* スケルトンはまだ出さない
* `/jinro start / stop / reset`
* 役職は本人だけに通知

までにします。

### ファイル構成

```text
scripts/
├─ jinro_core.sk
├─ jinro_role.sk
├─ jinro_daynight.sk
├─ jinro_sign.sk
└─ jinro_item.sk       ← 次の段階で追加
```

まずこの4本を動かします。

---

## 1. `jinro_core.sk`

```vb
# ============================================================
# Jinro RPG Prototype
# File : jinro_core.sk
#
# Phase 1
#   2人プレイ用
#   ゲーム開始 / 停止 / リセット
#
# ============================================================


options:
    max-players: 2


# ============================================================
# /jinro start
# ============================================================

command /jinro start:
    permission: op

    trigger:

        if size of {jinro.players::*} < 2:
            send "&c[JINRO] 2人登録してから開始してください"
            stop

        if {jinro.running} is true:
            send "&c[JINRO] すでにゲーム中です"
            stop

        set {jinro.running} to true
        set {jinro.phase} to "day"
        set {jinro.time} to 60

        # ゲームワールドを保存
        set {jinro.world} to world of player

        # 難易度 Easy
        execute console command "difficulty easy"

        # 自然スポーン停止
        execute console command "gamerule doMobSpawning false"

        # 昼にする
        set time of {jinro.world} to 1000

        send "&a========================================"
        send "&a[JINRO] ゲーム開始"
        send "&a[JINRO] 参加者: %size of {jinro.players::*}%人"
        send "&a[JINRO] 昼フェーズ開始"
        send "&a========================================"

        loop {jinro.players::*}:
            send "&e[JINRO] ゲーム開始" to loop-value


# ============================================================
# /jinro stop
# ============================================================

command /jinro stop:
    permission: op

    trigger:

        if {jinro.running} is not true:
            send "&c[JINRO] ゲームは開始されていません"
            stop

        set {jinro.running} to false

        send "&c[JINRO] ゲーム停止"


# ============================================================
# /jinro reset
# ============================================================

command /jinro reset:
    permission: op

    trigger:

        set {jinro.running} to false
        delete {jinro.phase}
        delete {jinro.time}
        delete {jinro.world}

        send "&e[JINRO] ゲーム状態をリセットしました"


# ============================================================
# /jinro info
# ============================================================

command /jinro info:
    permission: op

    trigger:

        send "&6========== JINRO INFO =========="

        if {jinro.running} is true:
            send "&a状態: ゲーム中"
        else:
            send "&c状態: 停止"

        if {jinro.phase} is set:
            send "&eフェーズ: %{jinro.phase}%"

        if {jinro.time} is set:
            send "&e残り時間: %{jinro.time}%秒"

        send "&e参加者: %size of {jinro.players::*}%人"

        loop {jinro.players::*}:
            send "&f- %loop-value%"

        send "&6================================"
```

---

## 2. `jinro_sign.sk`

MineScriptで看板を置いたあと、1行目を

```text
[JINRO]
```

にしておきます。

プレイヤーが右クリックすると登録。

```vb
# ============================================================
# Jinro RPG
# File : jinro_sign.sk
#
# 看板登録
#
# 看板1行目
#   [JINRO]
#
# 最大2人
#
# ============================================================


# ============================================================
# 看板を右クリック
# ============================================================

on right click on sign:

    if line 1 of event-block is not "[JINRO]":
        stop

    # すでに登録済み
    if player is in {jinro.players::*}:
        send "&e[JINRO] あなたはすでに登録されています"
        stop

    # 2人以上
    if size of {jinro.players::*} >= 2:
        send "&c[JINRO] 参加者は2人までです"
        stop

    add player to {jinro.players::*}

    send "&a[JINRO] 登録しました"
    send "&a[JINRO] プレイヤー %size of {jinro.players::*}%"

    loop {jinro.players::*}:
        send "&e- %loop-value%" to player


# ============================================================
# /jinro players
# ============================================================

command /jinro players:
    permission: op

    trigger:

        send "&6========== JINRO PLAYERS =========="

        if {jinro.players::*} is not set:
            send "&c登録者なし"
            stop

        loop {jinro.players::*}:
            send "&f%loop-index% : %loop-value%"

        send "&6==================================="


# ============================================================
# /jinro clearplayers
# ============================================================

command /jinro clearplayers:
    permission: op

    trigger:

        delete {jinro.players::*}

        send "&e[JINRO] 参加者登録を全消去しました"
```

---

## 3. `jinro_role.sk`

ここが今回かなり重要。

**2人の組み合わせをコマンド一発で切り替えます。**

```text
/jinro pair vv
/jinro pair wv
/jinro pair va
/jinro pair vl
```

意味は、

```text
vv = 村人 ＋ 村人
wv = 人狼 ＋ 村人
va = 村人 ＋ 吸血鬼
vl = 村人 ＋ 狼付き
```

です。

```vb
# ============================================================
# Jinro RPG
# File : jinro_role.sk
#
# 2人テスト用役職設定
#
# vv = 村人 + 村人
# wv = 人狼 + 村人
# va = 村人 + 吸血鬼
# vl = 村人 + 狼付き
#
# ============================================================


# ============================================================
# 役職表示名
# ============================================================

function jinro_role_name(role: text) :: text:

    if {_role} is "villager":
        return "村人"

    if {_role} is "wolf":
        return "人狼"

    if {_role} is "vampire":
        return "吸血鬼"

    if {_role} is "wolf_attendant":
        return "狼付き"

    return "不明"


# ============================================================
# 役職セット
# ============================================================

function jinro_set_roles(role1: text, role2: text):

    if size of {jinro.players::*} < 2:
        send "&c[JINRO] 先に2人を登録してください"
        stop

    set {jinro.role::%{jinro.players::1}%} to {_role1}
    set {jinro.role::%{jinro.players::2}%} to {_role2}

    send "&a[JINRO] 役職を設定しました"

    send "&e%{jinro.players::1}% → %jinro_role_name({_role1})%"
    send "&e%{jinro.players::2}% → %jinro_role_name({_role2})%"

    # 本人だけに通知
    send "&6[JINRO] あなたの役職は &f%jinro_role_name({_role1})%" to {jinro.players::1}
    send "&6[JINRO] あなたの役職は &f%jinro_role_name({_role2})%" to {jinro.players::2}


# ============================================================
# /jinro pair
# ============================================================

command /jinro pair [<text>]:
    permission: op

    trigger:

        if arg-1 is not set:
            send "&e[JINRO] 使用方法:"
            send "&f/jinro pair vv &7村人 + 村人"
            send "&f/jinro pair wv &7人狼 + 村人"
            send "&f/jinro pair va &7村人 + 吸血鬼"
            send "&f/jinro pair vl &7村人 + 狼付き"
            stop

        if arg-1 is "vv":
            jinro_set_roles("villager", "villager")
            stop

        if arg-1 is "wv":
            jinro_set_roles("wolf", "villager")
            stop

        if arg-1 is "va":
            jinro_set_roles("villager", "vampire")
            stop

        if arg-1 is "vl":
            jinro_set_roles("villager", "wolf_attendant")
            stop

        send "&c[JINRO] 不明な組み合わせです"


# ============================================================
# /jinro myrole
# ============================================================

command /jinro myrole:
    trigger:

        if {jinro.role::%player%} is not set:
            send "&c[JINRO] 役職が設定されていません"
            stop

        send "&6[JINRO] あなたの役職: &f%jinro_role_name({jinro.role::%player%})%"


# ============================================================
# /jinro roles
#
# 管理者確認用
# ============================================================

command /jinro roles:
    permission: op

    trigger:

        send "&6========== JINRO ROLES =========="

        loop {jinro.players::*}:

            if {jinro.role::%loop-value%} is set:
                send "&f%loop-value% → &e%jinro_role_name({jinro.role::%loop-value%})%"
            else:
                send "&f%loop-value% → &c未設定"

        send "&6================================="
```

---

## 4. `jinro_daynight.sk`

まずは**昼60秒 → 夜30秒 → 昼60秒**で回します。

スケルトンは一切出しません。

```vb
# ============================================================
# Jinro RPG
# File : jinro_daynight.sk
#
# 昼 / 夜 サイクル
#
# 昼   60秒
# 夜   30秒
#
# 実際のMinecraft時間も変更
#
# ============================================================


options:

    day-time: 60
    night-time: 30


# ============================================================
# 1秒ごとの処理
# ============================================================

every 1 second:

    if {jinro.running} is not true:
        stop

    if {jinro.world} is not set:
        stop

    # ========================================================
    # カウントダウン
    # ========================================================

    subtract 1 from {jinro.time}


    # ========================================================
    # 時間切れ
    # ========================================================

    if {jinro.time} <= 0:

        # ====================================================
        # 昼 → 夜
        # ====================================================

        if {jinro.phase} is "day":

            set {jinro.phase} to "night"
            set {jinro.time} to {@night-time}

            set time of {jinro.world} to 13000

            send "&1========================================" to {jinro.players::*}
            send "&9[JINRO] 夜になりました" to {jinro.players::*}
            send "&7夜時間: {@night-time}秒" to {jinro.players::*}
            send "&1========================================" to {jinro.players::*}

        # ====================================================
        # 夜 → 昼
        # ====================================================

        else:

            set {jinro.phase} to "day"
            set {jinro.time} to {@day-time}

            set time of {jinro.world} to 1000

            send "&e========================================" to {jinro.players::*}
            send "&6[JINRO] 朝になりました" to {jinro.players::*}
            send "&7昼時間: {@day-time}秒" to {jinro.players::*}
            send "&e========================================" to {jinro.players::*}


# ============================================================
# 手動で昼
# ============================================================

command /jinro day:
    permission: op

    trigger:

        if {jinro.world} is not set:
            set {jinro.world} to world of player

        set {jinro.phase} to "day"
        set {jinro.time} to {@day-time}
        set time of {jinro.world} to 1000

        send "&6[JINRO] 昼にしました"


# ============================================================
# 手動で夜
# ============================================================

command /jinro night:
    permission: op

    trigger:

        if {jinro.world} is not set:
            set {jinro.world} to world of player

        set {jinro.phase} to "night"
        set {jinro.time} to {@night-time}
        set time of {jinro.world} to 13000

        send "&9[JINRO] 夜にしました"


# ============================================================
# 現在の時間情報
# ============================================================

command /jinro time:
    trigger:

        if {jinro.phase} is not set:
            send "&c[JINRO] フェーズ未設定"
            stop

        send "&6[JINRO] %{jinro.phase}% / %{jinro.time}%秒"
```

---

# ここまででできるテスト

まず看板をMineScriptで置いて、

```text
[JINRO]
参加受付
```

などにしておく。

2人が右クリック。

```text
/jinro players
```

で、

```text
1 : crocadooo
2 : Player2
```

のようになればOK。

次に、

```text
/jinro pair vv
```

なら、

```text
1 → 村人
2 → 村人
```

```text
/jinro pair wv
```

なら、

```text
1 → 人狼
2 → 村人
```

```text
/jinro pair va
```

なら、

```text
1 → 村人
2 → 吸血鬼
```

```text
/jinro pair vl
```

なら、

```text
1 → 村人
2 → 狼付き
```

と切り替えられます。

その後、

```text
/jinro start
```

でゲーム開始。

```text
昼 60秒
↓
夜 30秒
↓
昼 60秒
↓
夜 30秒
...
```

となります。

そして、

```text
/jinro stop
```

で停止、

```text
/jinro reset
```

で状態リセットです。

---

## `jinro_item.sk` はまだ最小にする

ここは今の段階では**空に近い状態でOK**です。

次の段階でまず、

```text
Phase 2
弓       → プレイヤーに一撃
人狼の斧 → プレイヤーに一撃
```

だけ入れる。

その2つが安定したら、

```text
Phase 3
海洋の心 → 占い
トライデント → 2回で死亡
```

さらに、

```text
Phase 4
ネザースター → 吸血鬼死亡
```

へ進める。

最後に、

```text
Phase 5
役職ごとのアイテム制限
勝利判定
死亡処理
昼夜ごとの行動制限
```

を追加する。

**スケルトンはさらに後**にして、ゲーム本体が安定してから `jinro_mob.sk` として分離するのがいいです。

なお、今回の `jinro_role.sk` は「2人テスト専用」なので、以前考えていた**参加人数 → 固定役職 → 確率抽選 → 村人残数 → 最終役職決定**の本番方式とは切り離しておけます。2人テストが終わったら、そこだけ差し替えれば済みます。
