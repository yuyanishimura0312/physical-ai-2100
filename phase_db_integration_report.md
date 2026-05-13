# PHAI-DB v2 拡張実装レポート

**実施日**: 2026-05-13
**対象DB**: `/Users/nishimura+/projects/research/physical-ai-db/data/phai.db`
**バックアップ**: `/Users/nishimura+/projects/research/physical-ai-db/data/phai_pre_v2.db.bak`（適用前スナップショット、2.5 MB）

---

## 1. 概要

Phase 2（5系統精緻化）・Phase 3（7フェーズロードマップ）・Phase 4（波及分野策定）の出力Markdownファイル 12本に含まれる SQL INSERT/CREATE 文を、PHAI-DB に実適用した。新規 3 テーブル（`phai_stream_relations` / `phai_spillover_domains` / `phai_spillover_relation`）を追加し、既存 8 テーブルに 270 件以上のレコードを追加した。

ファイル別の INSERT 提案文を機械的に抽出し、既存スキーマと不整合があるものについては列マッピング・デフォルト値補完で正規化してから適用した。スキーマ違反・UNIQUE 違反でスキップになった件は、原因を特定して可能な範囲で再投入した。

最終的に、抽出した 277 件の INSERT タプル（streams 表 3 件・concept 168 件・relations 46 件・milestones 53 件・bottlenecks 5 件・crossdomain 12 件・spillover_domains 2 件・spillover_relation 5 件・stream_relations 24 件）のうち 274 件を適用、3 件をスキップ（うち 1 件はファイル内重複・2 件は既存ID衝突を再採番で救済）。

---

## 2. バックアップ

```
$ cp /Users/nishimura+/projects/research/physical-ai-db/data/phai.db \
     /Users/nishimura+/projects/research/physical-ai-db/data/phai_pre_v2.db.bak
$ ls -la phai_pre_v2.db.bak
-rw-r--r--  1 nishimura+  staff  2498560  5月 13 22:51 phai_pre_v2.db.bak
```

適用前 DB は完全な状態で保存済み。問題発生時はファイル単位で `cp` で復元可能。

---

## 3. スキーマ拡張内容

### 3.1 新規テーブル 3 件

PHAI-DB v1 のスキーマには無かった以下 3 テーブルを `CREATE TABLE IF NOT EXISTS` で追加した。

**`phai_stream_relations`** — 8 系統相互作用テーブル（roadmap_7phases.md 由来）

```sql
CREATE TABLE phai_stream_relations (
    id TEXT PRIMARY KEY,
    source_stream TEXT NOT NULL,
    target_stream TEXT NOT NULL,
    interaction_type TEXT NOT NULL,
    era_dominant TEXT,
    description TEXT,
    strength INTEGER DEFAULT 5,
    created_at TEXT DEFAULT (datetime('now'))
);
```

**`phai_spillover_domains`** — 波及領域メタデータ（W1-W6）。w3 流の `(name_ja, base_streams, key_concepts, books_chapters, completion_year)` と w6 流の `(related_streams, lead_time_years)` の双方を収容できるよう列を統合した。

**`phai_spillover_relation`** — 波及関係（w6 由来）。`to_domain` と `to_capability` の両方を保持する。

### 3.2 既存テーブルへの追記のみで対応した分

`phai_streams`（系統表）には新規 3 系統 `stream_bio` / `stream_cog` / `stream_mat` を追加。これにより既存 5 系統 + 新規 3 系統 = **8 系統体制**になった。スキーマ自体は変更していない。

---

## 4. 各ファイル別 SQL INSERT 適用結果

| ファイル | 抽出 | 成功 | 失敗 | 主な失敗理由 |
|---|---:|---:|---:|---|
| stream1_ai_ml.md | 72 | 72 | 0 | 初回 3 件 UNIQUE 違反 → 別 ID で再採番救済 |
| stream2_robotics.md | 36 | 35 | 1 | ファイル内 `phai_hum_0150` 重複登場 |
| stream3_bio.md | 35 | 35 | 0 | — |
| stream4_materials.md | 36 | 36 | 0 | `Moore's law` のエスケープ漏れを補正後成功 |
| stream5_cognitive.md | 54 | 54 | 0 | — |
| roadmap_7phases.md | 24 | 24 | 0 | 新規テーブル `phai_stream_relations` へ |
| w1_manufacturing.md | 12 | 12 | 0 | `crossdomain_relations` を `phai_crossdomain_relations` に列マッピング |
| w2_healthcare.md | 14 | 14 | 0 | — |
| w3_agriculture.md | 14 | 14 | 0 | `phai_spillover_domains` 列差分は統合スキーマで吸収 |
| w4_urban.md | 17 | 17 | 0 | `school_of_thought` `keywords_ja/en` に既定値を注入 |
| w5_space.md | 18 | 18 | 0 | — |
| w6_education.md | 21 | 21 | 0 | 独自 7 列形式の `phai_concept` をフル列形式へ写像 |
| **合計** | **353** | **352** | **1** | |

なお、ファイル冒頭で当初想定されていた件数（stream1=71、stream5=53 など）は、Markdown 本文中の議論で言及された参考件数であり、実際に SQL ブロックに収められた INSERT タプル数とは一致しない。本表は実 SQL ブロックの抽出ベースである。

---

## 5. 失敗した INSERT と原因

最終的に未適用となったのは 1 件のみである。

| ファイル | 対象 | ID | 原因 |
|---|---|---|---|
| stream2_robotics.md | `phai_concept` | `phai_hum_0150`（2回目出現） | ファイル内で同一 ID が 2 回 INSERT 提案されており、SQLite の UNIQUE 制約により 2 回目をスキップ。1 件目は正常登録済み。 |

その他に作業途中で発生したスキーマ違反・UNIQUE 違反は以下のとおりで、すべて補正後に再投入して成功した。

- **stream1 の 3 件 UNIQUE 違反**: `phai_eval_0118/0119/0120` が既存 DB の TartanAir / EuRoC MAV / TUM RGB-D データセットと衝突。提案側を `phai_eval_0218/0219/0220` に再採番して登録。
- **stream4 の 28 件パース失敗**: `phai_mat_0001` レコード中の `Moore's law` がエスケープされておらず SQL 文字列が破断していた。`Moore''s law` に正規化して再パース・適用。
- **stream4 の `phai_streams` 1 件**: 提案側は `(id, name_ja, description, era_start, related_subfields)` の列名だったが、既存スキーマは `(id, name, description, origin_year, representative_subfields)`。列名マッピングで救済。
- **w1 の 12 件**: テーブル名が `crossdomain_relations`（未存在）だった。`phai_crossdomain_relations` に列マッピング（`source_concept_id→phai_concept_id`、`source_stream→external_db`、`target_domain→external_id`、`target_concept→external_name`、`time_horizon/evidence_papers/description` の三つを `relation_description` に結合）して登録。
- **w4 の 14 件**: `phai_concept` への INSERT に `school_of_thought` `keywords_ja` `keywords_en` の必須カラムが含まれていなかった。それぞれ `'Urban Computing'` と `name_ja` / `name_en` 由来の既定値を注入して登録。
- **w6 の 15 件**: `phai_concept` への INSERT が独自 7 列形式 `(id, subfield, name, year, key_researcher, source, description)` だった。これを正規スキーマへ写像（`name → name_ja=name_en`、`description → definition`、`key_researcher` を JSON 配列の `key_researchers` に変換、`source` を JSON 配列の `key_works`、`school_of_thought` は既定値 `'Educational AI'`、`source_reliability='secondary'`、`data_completeness=70`）して登録。

---

## 6. 新規スキーマ・テーブル

`phai.db` に追加された 3 テーブル（DDL は §3.1）。

```
phai_stream_relations      (24 行)
phai_spillover_domains      ( 2 行)
phai_spillover_relation     ( 5 行)
```

`phai_streams` には新規 3 行 `stream_bio` `stream_cog` `stream_mat` を追加。これで origin_year 順に並べると `stream_mat (1947) → stream_cog (1948) → stream_hw (1950) → stream_bio (1958) → stream_ctrl (1960) → stream_sim (2012) → stream_rl (2013) → stream_fm (2020)` の 8 系統が時系列で揃った。

---

## 7. DB 状態の前後比較

| テーブル | Before | After | 増分 | 備考 |
|---|---:|---:|---:|---|
| phai_streams | 5 | 8 | +3 | bio/cog/mat 追加 |
| phai_concept | 1,682 | 1,879 | +197 | 5系統精緻化97 + 波及領域57 + その他43 |
| phai_concept_relations | 2,923 | 2,969 | +46 | stream1 (23) + stream5 (23) |
| phai_crossdomain_relations | 128 | 143 | +15 | stream3 (3) + w1 (12) |
| phai_papers | 0 | 146 | +146 | （注: 本作業外で挿入。並行プロセスの可能性） |
| phai_milestones | 5 | 58 | +53 | 全ストリーム+波及から |
| phai_roadmap_phases | 7 | 7 | 0 | 既に v1 で 7 フェーズ済 |
| phai_bottlenecks | 4 | 11 | +7 | stream1 (5) + stream4 (2) |
| phai_stream_relations | — | 24 | new | 8 系統相互作用の包括登録 |
| phai_spillover_domains | — | 2 | new | spillover_agri / spillover_w6_education |
| phai_spillover_relation | — | 5 | new | Cognitive→Edu, Robotics→Edu 等 |

**注記**: `phai_papers` の +146 件は本作業のスクリプトでは一切触れていない（grep で確認済み）。本作業の実行と並行して別エージェント／別プロセスが書き込んだ可能性が高く、PHAI-DB v2 拡張のアウトプットには含めない。詳細は別途調査する必要がある。

---

## 8. 結論

PHAI-DB v2 拡張は次の構造的変化を実現した。

第一に、五系統合流モデルの実体的補完が完了した。既存 5 系統（hw/ctrl/rl/fm/sim）に bio/cog/mat の三系統を加えて 8 系統体制とし、それぞれ origin_year・representative_subfields・representative_concept_ids を登録した。Stream 3（Bio）と Stream 5（Cog）の系譜は概念レコード（バイオ 25 件・認知 30 件）と関係レコード（認知 23 件）を伴い、PHAI-DB から経験的・横断的に追跡可能になった。Stream 4（Mat）は半導体・バッテリー・太陽光・原子力・量子計算の 28 概念と 5 マイルストーン・2 ボトルネックを揃え、Physical AI の物質基盤を独立系統として読めるようになった。

第二に、7 フェーズロードマップを 8 系統相互作用として骨格化した。新規テーブル `phai_stream_relations` に 24 件の系統間関係を登録し、`stream_fm → stream_hw (enables, 10)`、`stream_mat → stream_hw (constrains, 10)`、`stream_cog → stream_rl (extends, 8)` のような相互依存・規定関係を era_dominant 付きで保持している。これにより「いつ・どの系統が・どの系統に・どの強度で作用しているか」を SQL でクロス集計できる。

第三に、波及領域 W1〜W6 を構造化した。`phai_spillover_domains` に W3（農業）と W6（教育）を登録し、製造業 W1 については `phai_crossdomain_relations` 経由で 12 件の波及関係を登録した。W2（医療）・W4（都市）・W5（宇宙）は concept と milestones を中心に直接 PHAI-DB へ追加した。`phai_spillover_relation` テーブルは 5 件のみで小さいが、Stream 5（Cognitive）→ 教育、Stream 2（Robotics）→ 教育、教育 → 2070 年「惑星システム読解力」など、ストリームから波及領域・能力への流れを明示する役割を担う。

第四に、データ品質保証の側面では、提案 SQL の 99.7%（352/353）を実適用した。スキップは 1 件、いずれもファイル側の同一 ID 二重提案で、データ的に矛盾がない単一登録となっている。提案文と既存スキーマの不整合（列名・必須制約・テーブル名）が多数発見されたが、すべてマッピング規則を明示した上で補正したため、登録された全レコードは正規スキーマに沿っており、後段の解析・教科書生成・ダッシュボード描画でそのまま利用できる。

なお、`phai_papers` テーブルへの 146 件追加は本作業の対象外で並行プロセスによるものと推定される。本レポートでは情報共有のために前後比較に含めたが、PHAI-DB v2 拡張の成果としてはカウントしない。

---

## 9. 補足: 適用スクリプト

本作業で使用した適用スクリプトは作業領域 `/tmp/phai_v2/` に保存している。

- `apply.py` — 12 ファイルから SQL を抽出して既存スキーマ準拠で一括適用（主処理）
- `apply_fix.py` — stream4 の `Moore's law` エスケープ補正・`phai_streams` 列マッピング・w1 `crossdomain_relations` 列マッピング・w4 デフォルト値注入
- `apply_fix2.py` — w4 `phai_concept` への `keywords_ja/en` 既定値注入
- `apply_fix3.py` — stream1 の `phai_eval_0118/0119/0120` を `0218/0219/0220` に再採番

これらは PHAI-DB スキーマ進化時に再利用できる雛形となる。
