# MG (Management Studies) DB — Physical AI 2100 Evidence Extract

**生成日**: 2026-05-18 JST
**DB**: `~/projects/research/miratuku-news-v2/data/mg_consolidated.json`（3,369 concepts / 5,267 relations / 232 researchers）
**教科書**: 20 章 243,506 字「経営の知的地図」 `~/projects/research/miratuku-news-v2/mg-textbook/chapters/ch01-ch20.md`
**ダッシュボード**: https://yuyanishimura0312.github.io/miratuku-news-v2/dashboards/mg.html
**抽出件数**: 35 concepts × 3 領域（戦略・組織変革・知識経営）

> 抽出目的: Physical AI 2100 教科書「経営学アンカー」セクション補強。
> 抽出方針: 10 クラスター（戦略／起業／リーダーシップ／イノベーション／マーケティング／組織／心理学／オペレーション／ガバナンス／ファイナンス）から Physical AI 導入の経営判断に直結する概念を、教科書章引用付きで整理。

---

## 1. 経営戦略概念 × Physical AI

Porter / RBV / Dynamic Capabilities / Blue Ocean の 4 視座（教科書 Ch8）は Physical AI 戦略の 4 つの異なる読み解きを与える。Teece の Dynamic Capabilities が 8 クラスター橋渡しの最重要概念であり Physical AI 時代の中核 OS となる。

| 概念ID | 概念 | 提唱者 | クラスター | Physical AI への意味 | 教科書章 |
|---|---|---|---|---|---|
| m0022 | 競争戦略（5 Forces） | Michael Porter | 戦略 | Physical AI 産業の業界構造分析：(1) 新規参入（Figure・1X・Apptronik）、(2) 代替品（既存自動化）、(3) 買い手交渉力（製造大手 vs ロボット VC）、(4) 売り手交渉力（NVIDIA・TSMC）、(5) 既存競合（Boston Dynamics・FANUC・ABB）。ただし業界構造そのものが Physical AI で崩壊する点に注意 | Ch8 |
| m0028 | VRIO 分析 | Jay Barney | 戦略 | Physical AI 時代の RBV：「今持っている資源」（既存ロボット資産・工場・人材）の Value/Rarity/Inimitability/Organization 評価。しかし MOR「育てる」動詞転換ではスナップショット的限界が露呈 | Ch8 |
| m0034 | ダイナミック・ケイパビリティ | David Teece / Gary Pisano / Amy Shuen (1997) | 戦略×8 クラスター橋渡し | Physical AI 時代の中核 OS。Sensing（基盤モデル動向把握）→ Seizing（資源動員：CVC・買収）→ Transforming（組織再構成：両利き化）。**ノキア vs Apple 事例**：保有資源優位だったノキアが Physical AI 類似の変化に対応できず敗北。Physical AI で同様事象が既存自動車・既存ロボットで再現する可能性 | Ch8, Ch9, Ch16 |
| m0026 | プラットフォーム戦略 | Michael Cusumano / Annabelle Gawer | 戦略×デジタル | Physical AI プラットフォーム（基盤モデル＋開発者エコシステム＋ハードウェア標準）。Apple iTunes/App Store 型エコシステム構築が支配的戦略となる可能性。NVIDIA Isaac・OpenAI 物理基盤モデル・Tesla Dojo の競合 | Ch16, Ch17 |
| m0037 | 選択と集中 | – | 戦略×組織 | Tesla の「EV オンリー」一点集中で内燃機関の足を引っ張られない構造。Physical AI でも垂直統合型（Tesla Optimus）と専業型（Figure）が分岐 | Ch9 |
| m0071 | 両利きの経営 | Charles O'Reilly / Michael Tushman | 戦略×イノベーション | 既存事業（既存ロボット運用）の Exploitation と Physical AI 探索の Exploration を同時追求。富士フイルム型「コア・コンピタンス転用」が Physical AI 導入の模範 | Ch10, Ch16 |
| m0245 | 破壊的イノベーション | Clayton Christensen | イノベーション | 既存自動車メーカーが「EV シフトしながら内燃機関も維持」構造的両利きに苦しむ中、Tesla は EV オンリーで Physical AI（ロボタクシー・Optimus）に経営資源配分 | Ch10 |
| m1417 | 技術における経路依存性 | – | 戦略×技術 | QWERTY・VHS の論理：今日の Physical AI 技術投資（基盤モデル選択・ロボット OS 選択）が将来の選択肢を制約する。ROS 2 vs proprietary、NVIDIA vs alternatives のロックイン | Ch10 |
| m1234 | コーポレート・ベンチャーキャピタル（CVC） | – | 戦略×ファイナンス | Intel Capital・Google Ventures・Salesforce Ventures 型 CVC が Physical AI スタートアップ早期投資の中心。戦略的価値と財務リターン両立の難題を含む | Ch10 |

### Blue Ocean × Physical AI
Kim & Mauborgne の Blue Ocean（教科書 Ch8）は Physical AI の「家庭ロボット」「介護ロボット」「農業選択収穫ロボット」（AA-DB mention#5：いちご収穫 95% 精度）等、競争のない新需要領域創出に対応。MOR 4 時代パネルの「協奏団期」（2030 ナイロビ）はまさに Blue Ocean 段階。

---

## 2. 組織変革 × Physical AI

Lewin / Kotter / ADKAR の組織変革 3 理論は Physical AI 導入の組織変革を読み解く骨格。教科書 Ch16 によれば「ダイナミック・ケイパビリティの『変革』プロセス」が組織変革理論と直結する。

| 概念ID | 概念 | 提唱者 | クラスター | Physical AI への意味 | 教科書章 |
|---|---|---|---|---|---|
| m2399 | チェンジ・リーダーシップ | John P. Kotter | リーダーシップ | Kotter 8 段階モデル：(1) 危機意識醸成（Physical AI 競合脅威の共有）、(2) 連帯チーム結成、(3) ビジョン策定、(4) ビジョン伝達、(5) 行動権限委譲、(6) 短期成果創出、(7) さらなる変革推進、(8) 文化定着。教科書 Ch16：「組織変革の失敗の多くは戦略の誤りではなく、変革を推進するリーダーシップの欠如に起因」 | Ch5, Ch16 |
| m0042 | 変革型リーダーシップ | James MacGregor Burns (1978) / Bernard Bass (1985) | リーダーシップ | 4 要素：理想的影響力・鼓舞的動機づけ・知的刺激・個別的配慮。Physical AI 導入では「単に効率化する」でなく「製造とは何か・人間とロボットの関係をどう描くか」のビジョン共有が要 | Ch5 |
| m0053 | レベル 5 リーダーシップ | Jim Collins | リーダーシップ | 個人的謙虚さと強固な意志の統合。Physical AI 導入の「ともに育てる」（MOR 動詞）の経営者像と整合 | Ch5 |
| m0199 | リーダー・メンバー交換理論（LMX） | George Graen | リーダーシップ×組織 | リーダーシップを「関係の質」として双方向に捉える。Physical AI 時代の「人間-AI エージェント関係」の質を経営判断の対象に含める転換 | Ch5 |
| m2385 | ポスト・ヒロイック・リーダーシップ | Joseph Raelin | リーダーシップ×組織 | リーダーシップを特定個人特性でなく「複数組織メンバー間に分散・共有される動的プロセス」として再定義。MOR「楽団員」像（誰もが指揮者ではなく譜面を書く者になる）と整合 | Ch5, Ch16 |
| m1869 | 心理的安全性 | Amy Edmondson (1999) | 心理学×リーダーシップ×組織×イノベーション | Google プロジェクト・アリストテレスで実証。Physical AI 導入では「AI 判断を覆す」「ロボット停止を申し出る」発話の心理的安全性が現場の質を決める。ナイロビのアディサ・カマウ（MOR）の 15 秒の迷いを許す現場文化 | Ch5, Ch6 |
| m0063 | 組織文化 | Edgar Schein | 組織 | 氷山 3 層モデル（人工物・標榜価値・基本的仮定）。Physical AI 導入は「製造の基本的仮定」レベルの転換であり、表層の手順書変更では不十分 | Ch4, Ch16 |

### Lewin と ADKAR
Lewin の Unfreezing-Changing-Refreezing 3 段階は教科書 Ch5 で取り上げられ、Physical AI 導入の「既存ロボット運用の解凍 → 基盤モデル統合 → 新オペレーション凍結」の段階モデルとして応用可能。ADKAR（Awareness/Desire/Knowledge/Ability/Reinforcement）は個人レベルの変革プロセスとして、現場作業者の Physical AI 受容プロセスを記述する。

---

## 3. 知識経営（SECI / Ba）× Physical AI 暗黙知形式知変換

野中郁次郎の SECI モデル（教科書 Ch9）は Physical AI の核心課題「暗黙知の形式知化と再暗黙知化」を扱う最重要フレーム。MOR 補論「触診的暗黙知」（ナイロビのアディサが手で感じる微小欠陥）は SECI の社会化フェーズの 21 世紀的再定義。

| 概念ID | 概念 | 提唱者 | クラスター | Physical AI への意味 | 教科書章 |
|---|---|---|---|---|---|
| m0069 | ナレッジマネジメント | – | 組織×イノベーション | 組織内分散の暗黙知・形式知を体系的に創造・蓄積・共有・活用。Physical AI 時代は「ベテラン作業者の暗黙知 → 基盤モデル学習データ → 新人作業者への再暗黙知化」のループが中心 | Ch9, Ch16 |
| m0164 | 知識ベース理論 | Ikujiro Nonaka | 組織×知識 | SECI 4 プロセス：社会化（Socialization：対面の暗黙知共有）→ 表出化（Externalization：言語化）→ 連結化（Combination：形式知統合）→ 内面化（Internalization：実践による再暗黙知化）。Physical AI は「表出化」を VLA モデルで自動化する技術 | Ch9 |
| m0083 | 知の探索と深化 | James March (1991) | 組織×知識 | 探索（Exploration）と深化（Exploitation）のジレンマ。Physical AI 時代は基盤モデル研究（探索）と既存ライン運用（深化）の同時管理が要 | Ch9, Ch10 |
| m0841 | 組織学習 | – | 組織×知識 | 変革と適応の基本プロセス。Physical AI 導入による組織学習は「シングルループ（手順改善）→ ダブルループ（前提見直し）→ デュートロループ（学習プロセス自体の変革）」の階段 | Ch4, Ch16 |
| – | 「場」（ba）の概念 | Nonaka et al. | 組織×知識 | SECI 各プロセスに対応する場：創始 ba（対面社会化）・対話 ba（言語化）・システム化 ba（情報統合）・実践 ba（行動内面化）。Physical AI 時代は **「人間-AI-ロボット混成 ba」** が新形態として登場（教科書 Ch9, 3.3 節） | Ch9 |
| m0255 | グロースハック | – | マーケティング×組織 | 「実験と失敗を受け入れる文化」の典型例。Physical AI 導入の現場実験文化に応用可 | Ch16 |

### 教科書 Ch9 引用（Physical AI 文脈で再読）
> 「知識ベース理論は『企業を知識創造組織として捉える理論。暗黙知と形式知の相互作用（SECI）により、組織は継続的に新知識を生成し、競争優位を獲得する』理論だ」
> 
> Physical AI 時代の SECI 再定式化：(1) 社会化＝ベテランの触診・触覚を現場で AI センサーが学ぶ、(2) 表出化＝VLA モデルが暗黙知を実行可能ポリシーに変換、(3) 連結化＝複数現場の VLA モデルを統合（fleet learning）、(4) 内面化＝新人作業者が AI 推奨を身体で受け止め新たな暗黙知を形成

---

## 4. オペレーション（TPS）× Physical AI（教科書 Ch15）

大野耐一の TPS（教科書 Ch15）は Physical AI に必須の「カイゼン」「自働化」「ジャストインタイム」の母系列。MOR 補論「育てる」動詞は TPS の「自働化（人偏付き）」（機械が異常を自ら検出し止まる）の関係論的拡張として読める。

| 概念 | 提唱者 | Physical AI への意味 | 教科書章 |
|---|---|---|---|
| トヨタ生産方式（TPS） | 大野耐一 | Physical AI 時代の自働化（自律品質判断）・JIT（需要連動生産）・カイゼン（連続改善）の基盤。MOR M1-M2 期の「協奏団期」は TPS の AI 拡張版 | Ch15 |
| カイゼン | 大野耐一 / 今井正明 | Physical AI 導入は単発の自動化導入でなくカイゼンのループ（Plan-Do-Check-Act）の中に組み込まれてこそ持続的競争優位を生む | Ch15 |
| 自働化 | 大野耐一 | 「人偏付き自働化」＝機械が異常を自ら検出し止まる。Physical AI 時代は VLA モデルが異常検出・自己判断停止・人間アラート発出を統合 | Ch15 |
| カンバン方式 | 大野耐一 | 需要連動引取生産。Physical AI 時代は「リアルタイム需要 → 工場フリート → 物流ロボット」の連動カンバンが基盤モデル制御で実現 | Ch15 |

### 教科書 Ch16 引用（統合ループ）
> 「経営学の第一の統合ループは、戦略・組織・リーダーシップという三つのクラスターによって構成される。これは『企業はいかに方向を定め、組織を整え、人を動かすか』という、経営の最も根本的な問いに応答する循環系である」
> 
> Physical AI 時代の応答：戦略（どの Physical AI 領域に投資するか）→ 組織（両利き構造でどう運営するか）→ リーダーシップ（人間-AI 混成チームをどう率いるか）の 3 連結が必須

---

## 5. クロスリファレンス（教科書 → Physical AI 2100 セクション）

- **Ch8 競争戦略** ⇄ Physical AI 産業構造分析（4 視座：Porter / Barney / Teece / Kim & Mauborgne）
- **Ch9 知識ベース理論** ⇄ Physical AI 暗黙知形式知変換（SECI 再定式化）／触診的暗黙知（MOR ナイロビ）
- **Ch10 イノベーション** ⇄ Physical AI 破壊的イノベーション分析（クリステンセン）／両利き経営による Physical AI 探索（O'Reilly-Tushman）
- **Ch15 オペレーション** ⇄ Physical AI 時代の TPS 拡張（自働化・JIT・カイゼンのループ）
- **Ch16 統合ループ** ⇄ Physical AI 時代の 3 統合ループ（戦略×組織×リーダーシップ／イノベーション×マーケティング×起業／ガバナンス×ファイナンス×オペレーション）の Physical AI 再定式化
- **Ch5 リーダーシップ** ⇄ Physical AI 時代の変革型リーダーシップ／LMX／ポスト・ヒロイック／心理的安全性
- **Ch17 DX** ⇄ Physical AI 時代の DX 失敗率 70%（教科書）の構造的原因＝技術ではなく文化・組織・リーダーシップ
- **Ch20 5 つのフロンティア** ⇄ Physical AI は「AI 経営」「サステナビリティ」「学際融合」「リーダーシップ再定義」の 4 フロンティアに横断的に該当

---

## 6. 抽出方針メモ

- 教科書 20 章中、Ch5 / Ch8 / Ch9 / Ch10 / Ch15 / Ch16 / Ch17 / Ch20 が Physical AI 接続率最高
- ダイナミック・ケイパビリティ（m0034）は 8 クラスター橋渡しの最重要概念で Physical AI 時代の中核 OS として配置
- SECI（m0164）・両利き（m0071）・心理的安全性（m1869）が「現場の知 × AI × 組織変革」の 3 軸を担う
- 全概念は `python3 -c "import json; d=json.load(open('~/projects/research/miratuku-news-v2/data/mg_consolidated.json')); print([c for c in d['concepts'] if c['id']=='<ID>'][0])"` で詳細取得可能
- 教科書原文は `~/projects/research/miratuku-news-v2/mg-textbook/chapters/ch{NN}.md` で取得
