# ARREST GAME - Jail System

## 1. Structure

### Size

```text
5 × 5
Height: 5
```

### Materials

```text
Floor   : reinforced_deepslate
Walls   : iron_bars
Ceiling : reinforced_deepslate
Signs   : oak sign
```

---

## 2. Conceptual Layout

```text
        NORTH
          ↑

       [Sign]
          │
    ┌─────────┐
    │         │
[Sign]       [Sign]
    │         │
    │    P    │
    │         │
    └─────────┘
          │
       [Sign]

          ↓
        SOUTH
```

四方向に保釈看板を設置する。

---

## 3. Bail

```text
Iron Ingot × 5
```

看板をクリックし、必要な鉄インゴットを所持している場合に保釈する。

保釈成功時：

- 鉄インゴットを消費
- 収監解除
- BossBar削除
- 牢屋撤去
- プレイヤー保護解除

---

## 4. Sentence

標準収監時間：

```text
180 seconds
```

BossBarで残り時間を表示する。

---

## 5. Jail Registration

牢屋にはIDを付与して管理する。

```text
Jail ID
  ↓
Player
  ↓
Crime Reason
  ↓
Location
  ↓
Sentence
```

これにより複数人が同時に収監されても、それぞれの牢屋を個別に管理できる。

---

## 6. Protection

収監中：

- 無敵
- 耐性V
- 水中呼吸
- 火炎耐性
- 体力減少防止
- 満腹度減少防止
- 牢屋の破壊防止

---

## 7. Overlap

牢屋が既存牢屋と重なる場合は、その場所への生成を避け、安全な位置を探す。

通常時は犯罪発生地点を基準とする。

---

## 8. Cleanup

解放時には、牢屋・BossBar・プレイヤー状態・関連データを適切に整理する。

サーバー再起動後に古いBossBar等が残らないことも確認対象とする。
