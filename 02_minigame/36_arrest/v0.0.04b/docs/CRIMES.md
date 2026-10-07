# ARREST GAME - Crimes

## Current Crime List

| Crime | Description | Status |
|---|---|---|
| 花踏み | 花の上に乗る | Implemented |
| 環境破壊 | 草などを壊す | Implemented |
| サボり | 一定時間まったく動かない | Implemented |
| 不法投棄 | アイテムを捨てる | Implemented |
| ボート無免許 | ボートに関する行為 | Implemented / Adjusted |
| なんかかわいそう | 友好モブへの攻撃・殺害 | Implemented / Adjusted |
| 凝視 | 対象を見続ける | Implemented / Adjusted |
| 攻撃 | 特定の攻撃行為 | Implemented / Adjusted |
| 剣 | 剣に関する行為 | Implemented / Adjusted |
| チェスト | チェストに関する行為 | Implemented / Adjusted |
| 卵 | 卵に関する行為 | Implemented / Adjusted |
| 火薬 | 火薬に関する行為 | Implemented / Adjusted |

---

## Common Conditions

基本的に以下を共通条件とする。

```text
ARREST GAME = ON
        AND
対象ワールド
        AND
Survival Mode
        AND
収監中ではない
```

---

## Environmental Destruction

草などの破壊を犯罪として扱う。

罪状：

```text
環境破壊罪
```

---

## Flower

花を踏む行為を犯罪として扱う。

罪状・表示文言は実装中のメッセージ設定を優先する。

---

## Idleness

一定時間まったく移動しない場合に犯罪として扱う。

現在の基準：

```text
30 seconds
```

---

## Item Drop

プレイヤーがアイテムを投棄した場合に犯罪として扱う。

罪状：

```text
不法投棄罪
```

---

## Future Expansion

犯罪追加時には以下を確認する。

- Survivalのみか
- 対象ワールドは正しいか
- 収監中を除外しているか
- 連続判定で逮捕が重複しないか
- 既存犯罪と競合しないか
- 処理負荷が過大にならないか
