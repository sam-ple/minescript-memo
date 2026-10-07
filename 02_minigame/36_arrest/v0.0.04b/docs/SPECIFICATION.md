# ARREST GAME - Specification

## 1. Concept

Minecraft内の特定行動を犯罪として扱い、犯罪者を逮捕・収監するゲーム。

ドズル社の動画で扱われていた「やったら逮捕される世界」のゲーム性を、Paper + Skriptで再現することを目的とする。

---

## 2. Basic Rules

- ARREST GAMEがONのときのみ犯罪判定を行う
- 対象ワールドでのみ犯罪判定を行う
- Survival Modeのプレイヤーを基本的な判定対象とする
- 収監中のプレイヤーには通常の犯罪判定を行わない
- 逮捕されたプレイヤーには牢屋を生成する
- 収監中はプレイヤーを保護する
- 刑期終了または保釈によって解放する

---

## 3. Arrest Flow

```text
Crime Event
    ↓
Condition Check
    ↓
Crime Identified
    ↓
Arrest
    ↓
Jail Creation
    ↓
Prisoner Registration
    ↓
BossBar
    ↓
Timer
    ↓
Release
```

---

## 4. Jail

### Size

- Width: 5 blocks
- Length: 5 blocks
- Height: 5 blocks

### Materials

- Floor: reinforced_deepslate
- Walls: iron_bars
- Ceiling: reinforced_deepslate
- Bail signs: oak sign

### Bail

- Cost: Iron Ingot × 5

### Sentence

- Current standard sentence: 180 seconds

---

## 5. Prisoner Protection

収監中は、ゲームとして安全に待機できる状態を維持する。

- 無敵
- 耐性V
- 水中呼吸
- 火炎耐性
- 体力減少防止
- 満腹度減少防止

保護状態は解放時に解除する。

---

## 6. Release

以下のいずれかで解放。

1. 刑期終了
2. 保釈金支払い

解放時：

- 牢屋を撤去
- BossBarを削除
- 収監状態を解除
- プレイヤー保護を解除
- 必要な一時データを削除

---

## 7. Persistence

サーバー再起動・停止を考慮して、BossBar等の一時的な状態を適切に初期化する。

ARREST GAMEは再起動後に `/arrest on` することで再稼働できる構成を基本とする。

---

## 8. Multiple Jail

牢屋同士の重複を避けるため、牢屋位置を管理する。

通常は犯罪発生地点を基準に牢屋を生成し、既存牢屋との重複が問題になる場合には安全な場所を探索する構成を想定する。

---

## 9. Game Philosophy

このゲームでは、犯罪判定そのものが遊びの中心となる。

そのため、犯罪を追加する際も、

- 分かりやすい
- Minecraft上で判定可能
- 遊んでいて面白い
- 過剰に重くならない

ことを重視する。
