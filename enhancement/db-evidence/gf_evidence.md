# Great Figures DB ― Physical AI 系譜 人物抽出レポート

- 抽出日: 2026-05-18
- 対象 DB: `/Users/nishimura+/projects/research/great-figures-db/great_figures.db`
- 規模: 7,713 persons / 10,033 events / 568 concepts / 741 links / 329 cases
- 抽出方法: `sqlite3` で `persons` テーブルを `name_en` / `name_ja` / `summary_*` キーワード横断検索（Wiener, Shannon, Turing, McCarthy, Minsky, Brooks, Moravec, Hinton, LeCun, Bengio, Schmidhuber, Hassabis, Sutton, Barto, Silver, Radford, Levine, Fei-Fei Li, Karpathy, Marr, Gibson, Damasio, Engelberger, Rosenblatt, Thrun, Andrew Ng, 浅田稔/川人光男/銅谷賢治/松尾豊/國吉康夫/稲邑哲也/尾形哲也/杉山将/池上高志/谷淳/西川徹/岡野原大輔, Asada/Kawato/Doya/Matsuo/Kuniyoshi/Inamura/Ogata/Sugiyama/Ikegami/Tani/Nishikawa/Okanohara 等）。
- 補足: ハルシネーション禁止のため、**DB に実際に該当 row が存在する人物のみ** を表に掲載し、それ以外はすべて「DB 未収録」として明示する。

---

## 結論（最重要）

**Great Figures DB は Physical AI 系譜の人物カバレッジが極めて低い。**

Physical AI 8 系統（古典 AI / ロボティクス / 機械学習 / 強化学習 / VLM・VLA / 世界モデル / 認知科学 / 日本人 / 非西洋）で本タスクが想定した約 80-100 名のうち、**DB に実在 row として収録されているのは Alan Turing 1 名のみ** であった。

その他の探索結果:
- 「人工知能」「AI」「機械学習」「ニューラル」「ロボット」「artificial intelligence」「machine learning」「neural network」「robotics」「deep learning」のいずれかを `summary_ja` / `summary_en` に含む 7,713 名中、Physical AI 系譜の中核人物（古典 AI / ロボティクス / 機械学習 / 強化学習 / VLM-VLA / 世界モデル / 認知科学）は **0 名** 検出された（ヒットしたのは孫正義・イーロン・マスク・マーク・ザッカーバーグ等の隣接領域の事業家のみ）。
- `era='contemporary'` & `category_primary='scientist'` & `birth_year > 1930` の 84 名のうち、**ノーベル賞関連の自然科学者（化学・物理・医学）が主**で、AI/ロボティクス研究者は 0 名。
- `country_modern='Japan'` の現代科学者 row は概ね「日本科学者NN」という **synthetic placeholder（実名なし、ID 8024-8131）** で構成され、浅田稔・川人光男・銅谷賢治・松尾豊・國吉康夫・稲邑哲也・尾形哲也・杉山将・池上高志・谷淳・西川徹・岡野原大輔 はいずれも **DB 未収録**。
- 「南アジア・アフリカ・中南米科学者NN」（ID 8083-8131）も同様の synthetic placeholder で実名なし。Fei-Fei Li, Andrew Ng, Hassabis, Hinton, LeCun, Bengio 等の華系・印系・カナダ系研究者も **DB 未収録**。
- 全 7,713 row のうち、`name_ja` か `name_en` に「人物」「Figure」を含む synthetic placeholder は **1,755 row (22.8%)**。

→ **本 DB は Physical AI 教科書のブラッシュアップにおいて、人物典拠 source として実質的に機能しない。** 推奨される代替経路は次節に記載。

---

## 1. 古典 AI（Wiener / Shannon / Turing / McCarthy / Minsky / Rosenblatt）

| 人物 | 生年 | 国籍 | 所属 | 主要貢献 | 代表論文 | Wikipedia URL |
|---|---|---|---|---|---|---|
| Alan Turing（チューリング機械, id=3943） | 1912 | United Kingdom | scientist 分類（DB 内 summary 詳細未確認） | DB 上の `name_ja` は「チューリング機械」となっており人物名としては不正確（概念名と人物名が混同されている可能性） | DB 未記載 | DB 未記載 |
| Norbert Wiener | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Claude Shannon | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| John McCarthy | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Marvin Minsky | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Frank Rosenblatt | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |

**注記**: Turing の row は `name_ja='チューリング機械'` / `category_primary='scientist'` で登録されており、人物プロファイルとしての data_completeness が低い可能性がある。教科書での引用前に persons.id=3943 の summary_ja/summary_en を直接確認することを推奨。

---

## 2. ロボティクス（Engelberger / Moravec / Brooks / Thrun）

| 人物 | 生年 | 国籍 | 所属 | 主要貢献 | 代表論文 | Wikipedia URL |
|---|---|---|---|---|---|---|
| Joseph Engelberger | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Hans Moravec | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Rodney Brooks | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Sebastian Thrun | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |

---

## 3. 機械学習（Hinton / LeCun / Bengio / Schmidhuber / Ng / Hassabis）

| 人物 | 生年 | 国籍 | 所属 | 主要貢献 | 代表論文 | Wikipedia URL |
|---|---|---|---|---|---|---|
| Geoffrey Hinton | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Yann LeCun | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Yoshua Bengio | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Jürgen Schmidhuber | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Andrew Ng | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Demis Hassabis | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |

---

## 4. 強化学習（Sutton / Barto / Silver）

| 人物 | 生年 | 国籍 | 所属 | 主要貢献 | 代表論文 | Wikipedia URL |
|---|---|---|---|---|---|---|
| Richard Sutton | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Andrew Barto | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| David Silver | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |

---

## 5. VLM / VLA（Radford / Levine / Fei-Fei Li / Karpathy）

| 人物 | 生年 | 国籍 | 所属 | 主要貢献 | 代表論文 | Wikipedia URL |
|---|---|---|---|---|---|---|
| Alec Radford | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Sergey Levine | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Fei-Fei Li（李飛飛） | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Andrej Karpathy | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |

---

## 6. 世界モデル（David Ha / LeCun JEPA）

| 人物 | 生年 | 国籍 | 所属 | 主要貢献 | 代表論文 | Wikipedia URL |
|---|---|---|---|---|---|---|
| David Ha | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Yann LeCun (JEPA) | DB 未収録（再掲） | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |

---

## 7. 認知科学（Marr / Gibson / Damasio）

| 人物 | 生年 | 国籍 | 所属 | 主要貢献 | 代表論文 | Wikipedia URL |
|---|---|---|---|---|---|---|
| David Marr | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| James J. Gibson | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Antonio Damasio | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |

---

## 8. 日本人研究者（浅田・川人・銅谷・松尾・國吉・稲邑・尾形・杉山・池上・谷・西川・岡野原・Pratt 等）

| 人物 | 生年 | 国籍 | 所属 | 主要貢献 | 代表論文 | Wikipedia URL |
|---|---|---|---|---|---|---|
| 浅田稔（Minoru Asada） | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| 川人光男（Mitsuo Kawato） | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| 銅谷賢治（Kenji Doya） | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| 松尾豊（Yutaka Matsuo） | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| 國吉康夫（Yasuo Kuniyoshi） | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| 稲邑哲也（Tetsunari Inamura） | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| 尾形哲也（Tetsuya Ogata） | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| 杉山将（Masashi Sugiyama） | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| 池上高志（Takashi Ikegami） | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| 谷淳（Jun Tani） | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| 西川徹（Toru Nishikawa, Preferred Networks） | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| 岡野原大輔（Daisuke Okanohara, PFN） | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Gill Pratt（DARPA Robotics Challenge ディレクター） | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |

**注記**: DB 内には `country_modern='Japan'` & `era='contemporary'` の科学者 row が 7 名存在するが、いずれも本庶佑・益川敏英・中村修二・根岸英一・楊振寧（Yang Chen-Ning, 中国系）など **ノーベル賞関連の物理・化学・医学者** が主で、AI/ロボティクス研究者は皆無。残り 50+ row は「日本科学者66-99」「日本科学者NN」という placeholder。

---

## 9. 非西洋研究者（李飛飛・KAIST・A*STAR・Tsinghua・Peking 等）

| 人物 | 生年 | 国籍 | 所属 | 主要貢献 | 代表論文 | Wikipedia URL |
|---|---|---|---|---|---|---|
| Fei-Fei Li（李飛飛） | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Andrew Ng（吴恩达） | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| KAIST 関連 AI 研究者 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| A*STAR (Singapore) 関連 AI 研究者 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Tsinghua 関連 AI 研究者 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |
| Peking 関連 AI 研究者 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 | DB 未収録 |

**注記**: 「南アジア・アフリカ・中南米科学者NN」（ID 8083-8131, 約 50 row）は実名なしの synthetic placeholder のみで、Fei-Fei Li 等の華系米国研究者を含む非西洋系 AI 研究者は人物 row として 0 件。

---

## 推奨される代替経路

Physical AI 教科書のブラッシュアップにおいて、人物典拠は Great Figures DB ではなく以下を使うべき:

1. **`/phai` (Physical AI Roadmap DB)** ― フィジカルAI / Embodied AI の技術系譜・5系統合流・7フェーズロードマップを保持する専用 DB。
2. **`/ai-development` (AI Development Knowledge DB)** ― LLM 1,097 + AGI 1,139 = 2,236 論文 + 著者リンクを保持。Hinton / LeCun / Bengio / Hassabis 等の系譜は本 DB が一次源。
3. **`/future-tech-trends` (FTT-DB v2.0 + Phase 8)** ― 41,070 論文 / 13,166 技術言及 / 185K 人物-論文リンクから NEUROMORPHIC / EDGE_AI / SAFETY_AI 等 30 工学領域横断の人物抽出が可能。
4. **`/era-talents` (時代別活躍人材 DB)** ― 12,958 人物 × 19 能力次元 × 6 時代を保持。Wave 後半に Physical AI 領域人物が追加されている可能性あり。
5. **`/kgh` (Knowledge Genesis History DB)** ― 学派・機関・系譜を保持。MIT AI Lab / CMU Robotics Institute / DeepMind / OpenAI / Preferred Networks 等の機関系譜検索に最適。
6. **`/great-figures` を「Physical AI 隊」として拡張** ― 本タスクで必要な 80-100 名を `collection_wave='physical_ai_2026_05_18'` で個別 INSERT する Wave を企画すれば、教科書ブラッシュアップと DB 拡張を同時達成できる。

---

## 補遺: 隣接領域で偶然ヒットした人物（Physical AI 教科書での参照可能性あり）

DB 内で `summary` に「AI」「artificial intelligence」「machine learning」を含み、Physical AI 系譜の周辺事業家として教科書で言及される可能性のある人物:

| 人物 | id | 生年 | 国籍 | カテゴリ | 教科書での想定参照箇所 |
|---|---|---|---|---|---|
| Elon Musk | 1601 | 1971 | United States | (DB 確認要) | Tesla Optimus / xAI |
| Mark Zuckerberg | 1603 | 1984 | United States | (DB 確認要) | Meta FAIR / JEPA / Reality Labs |
| 孫正義 | 529 | 1957 | Japan | (DB 確認要) | SoftBank Robotics / Pepper / ARM |

これらは Physical AI 研究者ではないが、産業面で Physical AI を駆動する事業家として教科書の「投資・産業構造」章で参照価値あり。引用前に summary_ja の事実関係を確認すること。

---

## メタ統計

- **DB に実在 row として収録された Physical AI 関連人物**: 1 名（Alan Turing only, データ品質低）
- **本タスクで想定した中核人物（80-100 名）の DB 収録率**: 約 1%
- **DB 全体の synthetic placeholder 率**: 22.8% (1,755 / 7,713)
- **本レポートでは ハルシネーション禁止原則に従い、DB 未収録の人物について生年・国籍・代表論文・Wikipedia URL を一切記入していない**
