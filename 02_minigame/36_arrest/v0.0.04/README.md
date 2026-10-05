# ARREST GAME v0.0.04

## 方針

v0.0.03を原本として、ゲーム内容を増やさず内部構造を整理したリファクタリング版。

v0.0.03で存在していた罪状判定ロジックを原則として維持し、逮捕・牢屋・BossBar・収監中保護・設定などの共通処理を整理する。

## 主な変更

- 罪状の収監時間・保釈アイテム・保釈数・表示名を `config/crimes.sk` に集約
- 全罪状の逮捕処理を `core/crime.sk` に集約
- 牢屋を `core/jail.sk` に分離
- BossBarを `core/bossbar.sk` に分離
- 収監中保護を `core/protection.sk` に分離
- メッセージを `config/messages.sk` に集約
- サウンド用の置き場所を `core/sound.sk` に用意（v0.0.04では未使用）
- 既存の罪状判定ロジックは原則そのまま移植
- `grass.sk` と `drop.sk` はv0.0.03 ZIPに存在しなかったため、今回のv0.0.04で別途追加

## v0.0.04に含まれる罪状

- 暴行罪
- ボート無免許罪
- 窃盗罪
- たまご泥棒罪
- 花踏み罪
- 火遊び危険罪
- サボり罪
- なんかかわいそう罪
- 凝視罪
- 銃刀法違反
- 環境破壊罪
- 不法投棄罪

### 追加分

#### 環境破壊罪
- 短い草・背の高い草を壊した場合
- 収監：30秒
- 保釈：銅インゴット × 5

#### 不法投棄罪
- アイテムを捨てた場合
- 収監：30秒
- 保釈：銅インゴット × 3

## ファイル構成

```text
arrest/
├── arrest.sk
│
├── config/
│   ├── general.sk
│   ├── crimes.sk
│   └── messages.sk
│
├── core/
│   ├── crime.sk
│   ├── jail.sk
│   ├── bossbar.sk
│   ├── protection.sk
│   └── sound.sk
│
└── crime/
    ├── attack.sk
    ├── boat.sk
    ├── chest.sk
    ├── egg.sk
    ├── flower.sk
    ├── gunpowder.sk
    ├── idle.sk
    ├── mob.sk
    ├── stare.sk
    ├── sword.sk
    ├── grass.sk
    └── drop.sk
```

## リファクタリングの考え方

罪状ファイルは「何をしたか」の判定を担当する。

```text
crime/*.sk
    ↓
arrest_crime(player, "crime-id")
    ↓
core/crime.sk
    ↓
config/crimes.sk から設定取得
    ↓
arrest_create_jail(...)
```

これにより、今後の罪状追加・収監時間変更・保釈条件変更を、できるだけ個別ファイルに影響させず管理できる構造を目指す。

## テスト方針

まず `/arrest on` を実行し、以下を確認する。

1. 花踏み
2. 牢屋生成
3. BossBar表示
4. 収監中保護
5. 保釈
6. 時間経過による釈放

その後、各罪状を個別に確認する。

## 注意

v0.0.04はリファクタリング版であり、まだ実サーバーでの全機能確認前。

そのため、まずSkriptのreload時にエラーがないことを確認し、その後に罪状を1つずつテストする。

## バージョン

- v0.0.03：動作確認を進めた原本
- v0.0.04：内部構造のリファクタリング版
