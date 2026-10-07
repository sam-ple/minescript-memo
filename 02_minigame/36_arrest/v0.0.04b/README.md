# ARREST GAME

Minecraft の世界で、日常的な行動を「犯罪」として判定し、犯罪者をその場で逮捕・収監するゲーム。

本作品は、**ドズル社の動画で扱われていた「やったら逮捕される世界」の企画・ゲーム性を再現することを目的として制作した個人制作作品**です。

> ※本リポジトリはゲームシステムをMinecraft + Paper + Skriptで再現・実装するものであり、ドズル社および関係者による公式作品ではありません。

---

## Overview

プレイヤーが特定の行動をすると犯罪として判定されます。

```text
プレイヤーの行動
      ↓
犯罪判定
      ↓
罪状決定
      ↓
逮捕
      ↓
牢屋生成・収監
      ↓
BossBarで刑期表示
      ↓
刑期終了 または 保釈
      ↓
解放
```

現在は、ゲームとしてほぼ完成した正式版仕様を基準として管理しています。

---

## Current Version

**v0.0.04b**

v0.0.04aまでにゲーム本体の主要機能を実装・調整し、v0.0.04bではドキュメント、フォルダ構成、Git管理用ファイル等を整備します。

---

## Environment

- Minecraft: 26.2
- Paper: 26.2
- Skript: 2.16.1
- Java: 25

---

## Main Features

### Arrest

- 犯罪行為を検知
- 罪状を表示
- プレイヤーを逮捕
- その場に牢屋を生成
- 収監時間を管理
- BossBarで刑期を表示
- 刑期終了時に解放

### Jail

- 5 × 5
- 高さ5
- reinforced_deepslateによる床・天井
- iron_barsによる壁
- 四方向に保釈看板
- 鉄インゴット5個で保釈
- 牢屋IDによる管理
- プレイヤーと牢屋の紐付け
- 牢屋の破壊防止

### Prisoner Protection

収監中のプレイヤーには以下の保護を行います。

- 無敵
- 耐性V
- 水中呼吸
- 火炎耐性
- 体力減少防止
- 満腹度減少防止
- 収監中は他の犯罪判定を行わない

### Crime Detection

現在実装・調整された犯罪システム：

- 花踏み
- 環境破壊
- サボり
- 不法投棄
- ボート無免許
- 友好モブへの攻撃・殺害
- 凝視
- 攻撃
- 剣
- チェスト
- 卵
- 火薬

※犯罪の有効・無効や判定条件は設定・実装状況により管理します。

---

## Game Operation

基本的な管理コマンド：

```text
/arrest on
/arrest off
/arrest status
```

ARREST GAMEの稼働状態、対象ワールド、設定等を管理します。

---

## Project Structure

```text
ARREST-GAME/
│
├─ README.md
├─ LICENSE
│
├─ docs/
│  ├─ ARCHITECTURE.md
│  ├─ SPECIFICATION.md
│  ├─ FILE_STRUCTURE.md
│  ├─ CRIMES.md
│  ├─ JAIL.md
│  ├─ DATA.md
│  ├─ TEST.md
│  └─ CHANGELOG.md
│
└─ skript/
   └─ arrest/
      ├─ core.sk
      ├─ config.sk
      ├─ jail.sk
      ├─ bossbar.sk
      └─ crime/
         ├─ grass.sk
         ├─ flower.sk
         ├─ idle.sk
         ├─ drop.sk
         └─ ...
```

実際のファイル名・分割は開発時点の最新版を優先します。

---

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Specification](docs/SPECIFICATION.md)
- [File Structure](docs/FILE_STRUCTURE.md)
- [Crimes](docs/CRIMES.md)
- [Jail System](docs/JAIL.md)
- [Data Structure](docs/DATA.md)
- [Test Guide](docs/TEST.md)
- [Changelog](docs/CHANGELOG.md)

---

## Development Policy

この作品は「複雑なシステムを作ること」よりも、

**実際にMinecraft上で遊べること**

を優先して開発しています。

そのため、コードは役割ごとに分割し、犯罪判定・牢屋・BossBar・設定等をできるだけ独立して管理します。

---

## Versioning

Git tagを使用してバージョンを管理します。

```text
v0.0.01
v0.0.02
v0.0.03
v0.0.04
v0.0.04a
v0.0.04b
```

各タグには、その時点のコードとドキュメントをセットで保存します。
