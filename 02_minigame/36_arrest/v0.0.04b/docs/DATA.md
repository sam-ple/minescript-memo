# ARREST GAME - Data Structure

この文書は、Skript内で利用する主要な状態・データの考え方をまとめる。

## Game State

```text
{arrest.enabled}
```

ARREST GAMEが稼働中かどうか。

---

## Target World

ARREST GAMEが対象とするワールドを保持する。

ゲームON/OFFと対象ワールドを分離して管理する。

---

## Jail

牢屋一覧：

```text
{arrest::jail::ids::*}
```

牢屋IDを管理する。

牢屋ごとに、

```text
player
reason
location
sentence
```

等の情報を関連付ける。

---

## Player

プレイヤーごとの収監状態を管理する。

```text
jailed
jail-id
```

等を利用して、収監中かどうか、どの牢屋に所属しているかを判定する。

---

## UUID

プレイヤー・ワールド等の識別にはUUIDを優先する。

名前変更等による参照不整合を避けることを目的とする。

---

## Cleanup

以下は特に残骸を残さない。

- BossBar
- Jail ID
- Jail location
- Prisoner state
- Temporary crime state
- Timer state
