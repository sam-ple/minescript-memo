# ARREST GAME - File Structure

## Root

```text
ARREST-GAME/
├─ README.md
├─ LICENSE
├─ docs/
└─ skript/
```

---

## docs

| File | Purpose |
|---|---|
| ARCHITECTURE.md | システム全体の構成・関連 |
| SPECIFICATION.md | 正式なゲーム仕様 |
| FILE_STRUCTURE.md | ファイル構成 |
| CRIMES.md | 犯罪一覧・判定仕様 |
| JAIL.md | 牢屋システム詳細 |
| DATA.md | Skript変数・状態管理 |
| TEST.md | テスト項目 |
| CHANGELOG.md | バージョン履歴 |

---

## skript/arrest

```text
arrest/
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

### core.sk

ARREST GAME全体の管理。

- `/arrest on`
- `/arrest off`
- `/arrest status`
- 対象ワールド
- 共通初期化

### config.sk

共通設定。

### jail.sk

牢屋の生成・登録・収監・保釈・解放。

### bossbar.sk

収監中BossBarの生成・更新・削除。

### crime/

犯罪ごとの判定。

---

## Principle

新しい犯罪を追加する場合は、原則として `crime/` 配下に独立したファイルを追加する。

犯罪ファイルに牢屋生成処理を直接大量に書かず、共通の逮捕処理を利用する。
