# doc-verify レポート ── `output/index_v4.html`

**対象**: `/Users/nishimura+/projects/research/physical-ai-2100/output/index_v4.html`
**規模**: 453,922 chars / 4,202 lines / 134 h2 / 35 SVG / 23 figure / 23 figcaption / 44 unique URL
**検証日**: 2026-05-18
**検証者**: doc-verify エージェント (自動 grep + WebSearch 8件サンプリング)

---

## 総合グレード

| カテゴリ | グレード | 概要 |
|---|---|---|
| 1. スナップショット不整合 | **A−** | TOC missing 0件 / SVG 35 vs figure 23 不一致 / 図番号体系の不揃いあり |
| 2. ハルシネーション疑い | **A** | 8件サンプル全件実在確認 (arXiv ID 2件・人物/年代 4件・NBER 1件・Transformer) |
| 3. カバレッジギャップ | **B** | URL 44 unique は規模対比やや少ない / 日本人研究者 19名カウント・付録B-9 で 16 mentions / `<strong>`数値強調 16.1% |
| 4. チーム間不整合 | **B+** | 文体 (である調) は 134章中 133章で統一 / 用語ゆらぎあり (Physical AI / フィジカルAI / 8系統 / 8系) |
| **総合** | **B+** | Critical 0 件 / Major 4 件 / Minor 多数 |

---

## 1. スナップショット不整合 ── Grade A−

### 計測
- **TOC anchor**: 21 件 (`href="#..."`)
- **Element ids**: 58 件
- **Missing anchors** (TOC が指すが id 不存在): **0 件** ✅
- **Orphan ids** (id があるが参照なし): 37 件 (figure/section の自動生成 id を含む)
- **Section ids**: 21 件 (重複なし)

### 図表
- `<svg>`: **35 個**
- `<figure>`: **23 個** → SVG だけで `<figure>` ラッパーを持たない要素が 12 個ある
- `<figcaption>`: 23 個 (figure と完全一致)
- **図番号体系の不揃い**:
  - 「図N1」「図1-1」「図 D5-2」「図2-1」「図3-1」 など命名規則が**少なくとも 5 種類混在**
  - 連番として抽出した数 `[1,2,3,4,5,6,7,8,9,13,14]` → 10,11,12 欠番、13/14 と続き 15 以上不在
  - 一方付録Cに「全40図」の宣言あり (整合性ギャップ大)

### 章番号体系
- 134 h2 のうち、`9.1〜9.5` `10.1〜10.8` `11.1〜11.11` `A-1〜A-6` `B-1〜B-11` `C-1〜C-5` `D-1〜D-5` `E-1〜E-5` の連番は揃っている
- 一方で序章〜第8章相当のセクションでは番号なし (h2 タイトルのみ) ── 章構造の明示性が不均一

### Major
- **M1**: 図番号体系の不揃い (図N1 / 図1-1 / 図 D5-2 など 5 系統混在)。付録C「全40図」宣言と実際の23 figcaption に**ギャップ 17 図**
- **M2**: SVG 35 vs figure 23 ── 12 個の SVG が figure/figcaption 無しで挿入されている可能性

### Minor
- Orphan id 37 件 (TOC リンク追加で navigability 向上可能)

---

## 2. ハルシネーション疑い ── Grade A

WebSearch 8 件で**全件実在・年代/著者ともに正確**を確認:

| # | 主張 | 実在検証結果 |
|---|---|---|
| 1 | arXiv 2212.06817 = RT-1: Robotics Transformer (2022年12月) | ✅ Brohan et al. 2022-12-13 |
| 2 | arXiv 2307.15818 = RT-2: VLA Models (2023年7月) | ✅ Brohan et al. 2023-07-28 |
| 3 | arXiv 1706.03762 = Attention Is All You Need (2017) | ✅ Vaswani et al. 2017-06-12 |
| 4 | WABOT-1, 1973年, 加藤一郎, 早稲田大学 | ✅ 世界初の二足歩行ヒューマノイド (1973) |
| 5 | アル=フワーリズミー 780-850, 820年バグダード | ✅ House of Wisdom, c.820, Kitab al-Jabr |
| 6 | 湯川秀樹 1949 Nobel / 1935 中間子予言 | ✅ 完全一致 |
| 7 | Brooks Subsumption 1986 | ✅ MIT 1986 (1985に "Robust Layered Control System" 発表) |
| 8 | NBER w23285 = Acemoglu & Restrepo "Robots and Jobs" | ✅ 2017, 一台で雇用5.6人減 |

### Major
- **M3**: 抽出した arXiv ID 一覧 (35件) と DOI (25件) の本文構造上の貼り付けが「`10.1038/s41586-024-07472-3）が`」のように**括弧と地の文の境界が不安定** ── 機械パースしづらく、自動検証パイプラインで取りこぼす可能性

### 推奨
- 残り arXiv ID 33 件と DOI 24 件は未サンプル。production 公開前にバッチ検証を推奨 (`citation-existence-checker` で全件 HEAD リクエスト)

---

## 3. カバレッジギャップ ── Grade B

### (a) 日本人研究者の章別配置
- **検出された日本人名**: 19名 (川人17 / 松尾11 / 浅田8 / 中沢6 / 稲葉3 / 池上3 / 銅谷3 / 國吉2 / 金出1 / 石黒1 / Kitano1 等)
- **付録 B-9「日本人研究者 (20名)」**: 16 mentions が集中 → 序章〜本論で実際に駆動軸として機能しているのは **5〜6 章のみ** (Ch5 jp=8, Ch17 jp=6, Ch24 jp=6, Ch27 jp=3, Ch36/38/42 jp=3 等)
- **JP mentions = 0 の章**: 134 章中 **約 100 章** (本書宣言「日本人駆動軸 8名を各章の論理展開の中央に据える」とギャップ)

### (b) 非西洋系譜の組込
- Varela 22 / アル=フワーリズミー 4 / Maturana 3 / オートポイエーシス 2 / Khwārizmī 1 / ヴァレラ 1
- **非西洋言及は本論前半 (Ch11, Ch17 中心) に集中**、Phase C 以降 (Ch36〜) ではほぼ消失
- Ubuntu / Buen Vivir / Ibn al-Haytham / 屠呦呦 等の**多元的非西洋知の引照は 0 件**
- 本居宣長 / 西田幾多郎 / 京都学派は Ch11 で言及だが、Phase G (Ch44) 哲学的結論との明示的接続が薄い

### (c) 一次ソース URL の充足率
- 総 URL 78 件 (unique 44 件) ── 453K chars / 44 URL = **約 1 URL / 10K chars**
- ドメイン Top: arxiv.org 5 / goldmansachs.com 2 / aist.go.jp 2 / jsk.t.u-tokyo.ac.jp 2 / unitree.com 2
- **官公庁・国際機関 URL**: pib.gov.in / diu.mil / miit.gov.cn / digital-strategy.ec.europa.eu / cao.go.jp / iea.org / weforum.org / reuters.com = **政策層 URL は十分**
- **学術論文 URL**: arxiv.org 5 のみ → 35 arXiv ID 言及に対し**実 URL 化は 5/35 = 14%**

### (d) 数値根拠の `<strong>` 強調率
- `<strong>` 総数: 373
- うち数字を含む: 60 (**16.1%**) ── journal-essay-style ルールの「数値強調必須」より低い
- 散文部分で `<strong>` 強調が散発的、数値の重要度を視覚的に追えない箇所が多い

### Major
- **M4**: 日本人駆動軸 8名宣言と実装ギャップ (Phase C 以降の章で日本人研究者言及がほぼ消失)
- **M5**: arXiv ID 35件中、実際の URL ハイパーリンク化は 5件のみ (一次ソース到達性が低い)

### Minor
- 非西洋系譜の章別分布の偏り (前半集中・後半消失)
- `<strong>` 数値強調率 16.1% は文書規模対比やや低い

---

## 4. チーム間不整合 ── Grade B+

### 文体一貫性 (です/ます vs である)
- **134 章中 133 章で「である調」統一** (Ch1 序章のみ「です/ます」1 件混在)
- グローバル統計: です/ます=1 / である=375 → **文体統一は実質完璧** ✅
- W1〜W5 ライター跨ぎでも文体に齟齬なし

### 用語ゆらぎ (Major)
- **`Physical AI` vs `フィジカルAI` vs `物理AI`**:
  - フィジカルAI 231 / Physical AI 83 / フィジカル AI 2 / 物理AI 1
  - **「フィジカルAI」優位**だが Physical AI も同等の概念として併用 → 統一推奨
- **`8系統` vs `8系` vs `八系統` vs `八系`**:
  - 8系統 44 / 8系 44 / 八系統 7 / 八系 7 / 8 系統 6 → **5 種類混在**
  - 「8系統」を正本とするのが妥当だが、「8系」省略形が同数出現
- **`Foundation Model` vs `基盤モデル`**: 18 vs 46 (基盤モデル優位、英語形は技術文脈で出現)
- **`World Model` vs `世界モデル`**: 33 vs 28 (拮抗)
- **`Embodied AI` vs `身体性AI` vs `具身AI`**: 1 / 5 / 0 → 身体性AI 優位、ただし mention 全体が薄い

### 概念定義の一貫性
- 「Physical AI = 知性が物質に降りる場所」(Ch8) と「Physical AI = 関係論的に現れる」(Ch8) の**3定義併記**は意図的
- 「5系統合流」(Ch13-19) と「8系統への拡張」(Ch21-27) の段階的拡張は構造化されており整合
- 「Phase A〜G」の年代区分 (2026-2100) は全章で一貫

### Writer markers
- W1 〜 W5 マーカーは本文中ほぼ未出現 (W3:1 / W5:1 のみ) → ライター跨ぎの境界が文中に痕跡を残していない (good)

### Major
- **M6**: 用語「8系統」と「8系」の同数 (44/44) 混在 → 中央表記の選定と統一が必要

### Minor
- 「Physical AI / フィジカルAI」「Foundation Model / 基盤モデル」「World Model / 世界モデル」の英和混在は技術文書として許容範囲だが、用語表 (Glossary D-1〜D-5) との対応を明示すると親切

---

## Critical / Major / Minor 一覧

### Critical (公開停止級)
**該当なし** ── 0 件

### Major (公開前に対応推奨) ── 6 件
- **M1**: 図番号体系不揃い (5 系統混在 + 付録C「全40図」宣言と実装23のギャップ)
- **M2**: SVG 35 vs figure 23 → 12 個の SVG が figure ラッパー欠如
- **M3**: arXiv/DOI 引用の括弧構造が不安定 (機械パース困難)
- **M4**: 日本人駆動軸 8名宣言と実装ギャップ (Phase C 以降で言及消失)
- **M5**: arXiv ID 35件中、URL ハイパーリンク化 5件のみ
- **M6**: 「8系統 / 8系」用語混在 (44/44 拮抗)

### Minor (継続改善) ── 5 件
- 図番号連番の欠番 (10/11/12/15-)
- Orphan id 37 件 (内部リンク追加余地)
- 非西洋系譜の章別分布偏り (前半集中)
- `<strong>` 数値強調率 16.1% (もう少し増やすと数値根拠が立つ)
- 用語表 (D-1〜D-5) と本文用語の cross_ref 明示

---

## 推奨アクション

1. **公開前 Quick fix (1-2h)**
   - 用語統一: 「Physical AI」→「フィジカルAI」または逆方向で本文全体一括 (`sed -i 's/Physical AI/フィジカルAI/g'`)
   - 「8系」 → 「8系統」へ一括統一
   - arXiv ID 35件を `<a href="https://arxiv.org/abs/{id}">` に自動ラッピング

2. **公開前 Medium fix (半日)**
   - SVG 12件を `<figure>` + `<figcaption>` でラップ、付録C「全40図」宣言を実装数に整合
   - 図番号体系を統一 (「図1-1」「図2-3」のように章番号-連番 で正規化)

3. **継続改善 (Phase A〜G章の補強)**
   - 日本人駆動軸 8名 (加藤一郎/川人光男/浅田稔/松尾豊/國吉康夫/岡野原大輔/西川徹/David Ha) を Phase C/D/E/F/G の各章へ最低 1 言及ずつ配置
   - 非西洋系譜 (Varela / アル=フワーリズミー / 本居宣長 / 西田幾多郎) を Phase G/結論章で再度参照、首尾呼応を実装
   - 残り arXiv ID 33件 + DOI 24件のバッチ HEAD 検証

---

## 検証手順 (再現性)

```bash
# 1. grep 解析
/usr/bin/python3 /tmp/doc_verify.py
# → /tmp/doc_verify_dump.json (構造化結果)

# 2. ハルシネーション抽出
/usr/bin/python3 /tmp/sample_claims.py

# 3. WebSearch 5件以上で固有名詞 + 年代 + 機関を実在検証
```

**実行成果物**:
- `/tmp/doc_verify_dump.json` ── 全 134 章の jp 言及・文体比率・URL ドメイン集計
- `/tmp/doc_verify.py` ── 解析スクリプト (再現可能)
- 本レポート ── `/Users/nishimura+/projects/research/physical-ai-2100/enhancement/integration/doc_verify_report.md`
