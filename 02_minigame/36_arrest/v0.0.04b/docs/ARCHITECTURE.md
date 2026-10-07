# ARREST GAME - Architecture

## 1. Overall Architecture

```text
                         ARREST GAME
                              │
                ┌─────────────┴─────────────┐
                │                           │
             Control                    Crime System
                │                           │
          core / config              ┌──────┼──────┐
                │                    │      │      │
                │                  grass  flower  idle
                │                    │      │      │
                └────────────────────┴──────┴──────┘
                              │
                              ▼
                         Arrest Process
                              │
                     ┌────────┴────────┐
                     │                 │
                    Jail            BossBar
                     │                 │
                     └────────┬────────┘
                              │
                           Release
```

---

## 2. Module Roles

### Core

ゲーム全体のON/OFF、対象ワールド、共通状態などを管理。

### Config

犯罪の有効・無効や数値等の共通設定を管理。

### Crime

犯罪ごとの判定を担当。

犯罪判定自体と、逮捕後の牢屋処理を分離する。

### Jail

牢屋の生成、登録、収監、保釈、解放、撤去を担当。

### BossBar

収監中のプレイヤーに刑期・罪状等を表示。

---

## 3. Arrest Boundary

犯罪モジュールは「犯罪を検出するところ」までを担当し、逮捕処理は共通化する。

```text
Crime Module
    │
    ▼
Common Arrest
    │
    ├─ Reason
    ├─ Player
    ├─ Jail
    ├─ BossBar
    └─ Timer
```

これにより、犯罪ごとに牢屋処理を重複して実装しない。

---

## 4. State Management

主な状態：

```text
Game ON / OFF
Target World
Player jailed / not jailed
Jail ID
Crime reason
Jail location
Sentence time
BossBar state
```

---

## 5. Restart

サーバー再起動時に残るべき情報と、残す必要のない一時情報を分離する。

特にBossBarなどの表示系オブジェクトは再起動後に不整合を起こさないようにする。

---

## 6. Design Principle

- 罪状ごとにファイルを分ける
- 牢屋処理を共通化する
- UI処理を分離する
- 設定を集約する
- できるだけ小さなモジュールにする
