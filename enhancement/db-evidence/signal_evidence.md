# Physical AI 2100 — Signal DB 兆候抽出

> 出典DB: `~/projects/research/pestle-signal-db/data/signal.db.backup-20260426`
> 抽出日: 2026-05-18
> 範囲: signals 6,885件・signal_cross_impact 1,806件・alerts 174件
> (live signal.db は 2026-05-16 リセット後 159件のみ。Wave 1 期の rich snapshot を採用)
> SANGAKU_LINK は signal-extractor rule-based パターン名のため alerts には存在しない
> (該当する産学連携シグナルは Sangaku R&D PR DB 経由で別途参照)
>
> **Tetlock score** は signal-db v5次元評価 (novelty/disruption/connectivity/credibility/composite)
> を 0-5 に正規化したもの (重み: 0.20/0.20/0.20/0.25/0.15)

---

## 1. Physical AI 直接シグナル Top 100
対象: robot / humanoid / embodied / Physical AI / VLA / autonomous / drone / robotic + 日本語 (ロボット / ヒューマノイド / 自律 / 自動運転 / ドローン / 身体性 / フィジカル / エンボディド)
ヒット: 122件 / Top 100 を composite_score 降順で抽出

| # | 年月 | シグナル | 数値・スコア | 出典 | Tetlock |
|---|------|----------|------------|------|--------|
| 1 | 1960-H1 | 生殖技術による女性のライフコース自律化 | comp=9.3 / impact=critical / H3 | — | 4.75 |
| 2 | 2026-04-25 | イラン戦争によるAI自律兵器化と指導者暗殺の現実化 | comp=8.8 / impact=critical / H1 | — | 4.24 |
| 3 | 2015-H2 | 自律型致死兵器システムの急速な現実化と規制の遅延 | comp=8.8 / impact=critical / H2 | — | 4.49 |
| 4 | 1947-H2 | 脱植民地化による国家主権の急速な再編成 | comp=8.6 / impact=critical / H2 | — | 4.47 |
| 5 | 2026-04-20 | 地球圏新規力：無機プロセスの自律的主体化 | comp=8.5 / impact=high / H1 | [ScienceDaily](https://www.sciencedaily.com/releases/2026/04/260419054825.htm) | 4.21 |
| 6 | 2006-H1 | 脳神経技術への倫理的懸念と遠隔操作の可能性 | comp=8.4 / impact=critical / H3 | — | 3.98 |
| 7 | 1970-H2 | ロボット・自動化技術の産業応用の開始 | comp=8.4 / impact=critical / H3 | — | 4.13 |
| 8 | 2026-04-22 | 非国家主体による地政学的代理戦争の自動化 | comp=8.3 / impact=high / H1 | [Eurozine](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) | 4.07 |
| 9 | 2012-H1 | AI・機械知能の進化と人間性の問い直し | comp=8.3 / impact=critical / H3 | — | 4.0 |
| 10 | 2026-04-23 | 「非国家主体による地政学的権力行使」と国家主権の形式的化 | comp=8.2 / impact=high / H1 | [NYT Business](https://www.nytimes.com/2026/04/20/us/politics/trump-administration-tariff-refunds.html) | 4.09 |
| 11 | 2026-04-24 | 地政学的戦争機械化による「文民統制の構造的迂回」 | comp=8.2 / impact=high / H1 | [Eurozine](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) | 3.97 |
| 12 | 1981-H1 | マイクロプロセッサー技術の急速な進化と計算能力の指数関数的増加 | comp=8.2 / impact=critical / H3 | — | 4.12 |
| 13 | 2024-H1 | 「『AI-to-AI競争』による人間による解釈可能性の根本的喪失」 | comp=8.1 / impact=high / H3 | [ITmedia](https://www.itmedia.co.jp/business/articles/2604/24/news009.html) | 4.08 |
| 14 | 2016-H1 | 労働市場の二極化と「仕事抵当権」化 | comp=8.1 / impact=critical / H2 | — | 3.98 |
| 15 | 2016-H1 | AI時代における人間的尊厳と労働価値の根本的危機 | comp=8.1 / impact=critical / H3 | — | 3.98 |
| 16 | 2024-H1 | 量子技術・光学通信における中国の自律的開発加速と「AI時代の供給鎖の再地政学化」 | comp=8.0 / impact=high / H1 | [日経ビジネス](https://business.nikkei.com/atcl/gen/19/00485/042200136/) | 4.1 |
| 17 | 1961-H1 | ロボット工学の産業化と労働力置換の開始 | comp=8.0 / impact=high / H3 | — | 3.9 |
| 18 | 1971-H2 | 産業オートメーション革命の開始 | comp=8.0 / impact=high / H2 | — | 4.12 |
| 19 | 1947-H2 | インド・パキスタン分割による大規模人口移動と暴力 | comp=8.0 / impact=critical / H2 | — | 4.12 |
| 20 | 1900s | Artistic modernism emerging as systematic critique of bourgeois representation | comp=8.0 / impact=medium / H3 | — | 3.93 |
| 21 | 2026-04-22 | 『戦争実装の完全自動化』とAI標的化の予測不可能性 | comp=7.9 / impact=high / H1 | [Eurozine](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) | 3.84 |
| 22 | 2026-04-22 | 戦争の「新しい戦闘ロジック」：自律兵器とAI標的化の予測不可能性 | comp=7.8 / impact=high / H3 | [Eurozine](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) | 3.58 |
| 23 | 2026-04-23 | 生態系の「自律的進化」と人間による管理可能性の喪失 | comp=7.8 / impact=high / H3 | [ScienceDaily](https://www.sciencedaily.com/releases/2026/04/260422044618.htm) | 3.99 |
| 24 | 2026-04-23 | 「統治不可能性の公式認識」と自然システムの『自律的進化』 | comp=7.8 / impact=high / H1 | [ScienceDaily](https://www.sciencedaily.com/releases/2026/04/260419054825.htm) | 3.99 |
| 25 | 2022-H1 | AI知能の自律的目的形成への懸念の顕在化 | comp=7.8 / impact=critical / H3 | — | 3.64 |
| 26 | 2024-H2 | 「自給力」と「資源循環」による主権再奪取の地域実験化 | comp=7.7 / impact=high / H3 | [greenz.jp](https://greenz.jp/2026/03/06/daiju-takahashi/) | 3.73 |
| 27 | 2017-H1 | 労働市場の急速な二極化と不安定化 | comp=7.7 / impact=critical / H1 | — | 3.98 |
| 28 | 2026-04-20 | ドローン技術とAI自律兵器による「戦闘員と民間人の弁別不可能性」と国際人道法の機能停止 | comp=7.6 / impact=high / H1 | [AI Now Institute](https://ainowinstitute.org/news/press/key-questions-on-the-role-of-technology-in-the-expanding-middle-east-war) | 3.97 |
| 29 | 2026-04-25 | ボトムアップ主権回復と地域自治の再構築 | comp=7.6 / impact=high / H3 | — | 3.75 |
| 30 | 2013-H2 | ロボット・AI倫理の制度化前夜 | comp=7.6 / impact=high / H2 | — | 3.87 |
| 31 | 2018-H2 | AI倫理と実装ギャップの顕在化 | comp=7.6 / impact=critical / H2 | — | 3.87 |
| 32 | 2019-H1 | AI倫理と創造者責任の問題化 | comp=7.6 / impact=high / H2 | — | 3.77 |
| 33 | 1940-H1 | 民間産業の軍事生産への強制転換 | comp=7.6 / impact=high / H1 | — | 3.9 |
| 34 | 1963-H1 | 大衆文化における若年層の自律的表現形式の確立 | comp=7.6 / impact=high / H3 | — | 3.77 |
| 35 | 1974-H1 | アジア太平洋地域における工業化と権威主義体制の結合 | comp=7.6 / impact=high / H2 | — | 3.87 |
| 36 | 2014-H2 | 自動運転技術による都市交通体系の根本的転換 | comp=7.5 / impact=critical / H3 | — | 3.84 |
| 37 | 1989-H2 | 遺伝子工学研究の加速と生命倫理の制度的空白 | comp=7.5 / impact=high / H3 | — | 3.64 |
| 38 | 2026-04-20 | 「無機プロセスの自律的主体化」による地球圏の脱人間中心化 | comp=7.4 / impact=medium / H3 | [ScienceDaily](https://www.sciencedaily.com/releases/2026/04/260414075639.htm) | 3.38 |
| 39 | 2011-H2 | 報道メディアの規制的正当性の喪失 | comp=7.4 / impact=high / H1 | — | 3.65 |
| 40 | 2013-H1 | サイバーセキュリティ規制とプライバシーの対立 | comp=7.4 / impact=high / H2 | — | 3.75 |
| 41 | 1981-H2 | 人工知能・ロボット技術による産業自動化の加速 | comp=7.4 / impact=high / H2 | — | 3.63 |
| 42 | 1914-H1 | 中国における帝国主義的支配と近代化の矛盾 | comp=7.4 / impact=critical / H1 | — | 3.76 |
| 43 | 1975-H1 | 冷戦構造の相対的弱体化と地域紛争の多発化 | comp=7.4 / impact=high / H1 | — | 3.78 |
| 44 | 1977-H1 | ロボット技術の製造業への本格導入と労働構造の変化 | comp=7.4 / impact=high / H2 | — | 3.78 |
| 45 | 1958-H1 | 複写機技術による情報流通の民主化の始まり | comp=7.4 / impact=medium / H3 | — | 3.66 |
| 46 | 1969-H2 | 自動化製造システムの進化 | comp=7.4 / impact=high / H2 | — | 3.76 |
| 47 | 1961-H2 | 冷戦の第三世界化と非同盟運動の限界 | comp=7.3 / impact=high / H1 | — | 3.77 |
| 48 | 1953-H2 | 日本の国際社会への復帰と経済的再興の加速化 | comp=7.3 / impact=high / H2 | — | 3.77 |
| 49 | 2026-04-20 | 金融システムの『多極通貨化』と米ドル中心性の侵食 | comp=7.2 / impact=high / H2 | [UN News](https://news.un.org/feed/view/en/story/2026/04/1167308) | 3.84 |
| 50 | 2026-04-21 | オルタナティブ経済・自給自足的自治の実装化と「平和な社会」構想の台頭 | comp=7.2 / impact=medium / H3 | [greenz.jp](https://greenz.jp/2026/03/06/daiju-takahashi/) | 3.51 |
| 51 | 2026-04-22 | 『中央銀行独立性の再定義』と露出した政治的金融工学 | comp=7.2 / impact=high / H1 | [Reuters Environment](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQNjBZcVU0ZWczemdjRUk4bVJmUHRfV0RPb3h5ZzV2aEVJX1VtbG0zYkVqRDQ5T2ZqV0hJN2RlVEpkcEx3emp6SUp5TlowU0dNX3B5Uks4bk5VYW03eDVtRkJsU2owOWhudTVvN09TbnhuN3dWRTQwTm5YeVRPT0xmbUFSc05aSDlGM2JqdlR3SU1CZFBpTFNic1NlZHhiVTJla0Y0cHowOGRGdw?oc=5) | 3.74 |
| 52 | 2025-Q1 | 「光学・量子通信供給鎖」の地政学化と日本メーカーの黙示的支配力 | comp=7.2 / impact=high / H1 | [South China Morning Post](https://www.scmp.com/news/world/united-states-canada/article/3351386/us-and-eu-sign-critical-minerals-plan-push-loosen-chinas-grip-key-materials?utm_source=rss_feed) | 3.71 |
| 53 | 2025-Q3 | 危険なAIの「スイッチオフ」可能性への問い | comp=7.2 / impact=critical / H3 | — | 3.51 |
| 54 | 2026-04-25 | 軍事ドローン産業の急速な資本化と規制空白 | comp=7.2 / impact=critical / H1 | — | 3.74 |
| 55 | 2022-H2 | AI倫理・制御の国家戦略化 | comp=7.2 / impact=high / H2 | — | 3.74 |
| 56 | 2018-H1 | 自動運転技術の安全性危機による信頼喪失の加速 | comp=7.2 / impact=critical / H1 | — | 3.87 |
| 57 | 1954-H1 | 社会主義圏内の多元化と東欧の独立的外交展開 | comp=7.2 / impact=high / H2 | — | 3.64 |
| 58 | 1974-H2 | 工業用ロボットの商用化と製造業の自動化転換 | comp=7.2 / impact=high / H3 | — | 3.61 |
| 59 | 2026-04-21 | 教育デジタル化における『反-スクリーン運動』の国家的制度化 | comp=7.1 / impact=medium / H1 | [Guardian Tech](https://www.theguardian.com/technology/2026/apr/17/liz-kendall-urges-uk-public-to-embrace-ai-as-government-makes-first-500m-fund-investment) | 3.66 |
| 60 | 2013-H2 | ロボットとAIの雇用への影響の可視化と不安 | comp=7.1 / impact=high / H2 | — | 3.61 |
| 61 | 1960-H1 | 大衆文化と権力機構の衝突 | comp=7.1 / impact=medium / H2 | — | 3.53 |
| 62 | 2026-04-21 | 医療正統性の危機と民間医療・自己治療への潜在的回帰の兆し | comp=7.0 / impact=high / H3 | [Wedge Online](https://wedge.ismedia.jp/articles/-/40509) | 3.62 |
| 63 | 2015-H2 | ロボット工学と昆虫知能の融合による自律型システムの出現 | comp=7.0 / impact=medium / H3 | — | 3.4 |
| 64 | 2017-H2 | 労働市場の自動化による構造的失業化 | comp=7.0 / impact=critical / H1 | — | 3.63 |
| 65 | 2008-H1 | ロボット技術の法的・倫理的問題化 | comp=7.0 / impact=medium / H3 | — | 3.28 |
| 66 | 1961-H2 | 東欧衛星国の相対的自律化と東側ブロックの多元化 | comp=7.0 / impact=high / H2 | — | 3.53 |
| 67 | 1903-H2 | 農業から工業への経済構造転換と一次産業の周辺化 | comp=7.0 / impact=high / H1 | — | 3.62 |
| 68 | 2026-04-23 | 「精神活性物質の脱医療化と民主化」：心理的主権の個人化と国家の喪失 | comp=6.9 / impact=medium / H3 | [NYT Health](https://www.nytimes.com/2026/04/21/well/mind/bpd-borderline-personality-disorder.html) | 3.39 |
| 69 | 2025-Q1 | 「コモンズ型保険と相互扶助の『金融制度化』による国家福祉国家の脱中央化」 | comp=6.9 / impact=medium / H3 | [greenz.jp](https://greenz.jp/2026/04/23/collective-insurance/) | 3.37 |
| 70 | 2017-H2 | 自動運転規制枠組みの前倒し構築 | comp=6.9 / impact=high / H2 | — | 3.52 |
| 71 | 1968-H1 | 医学的自己決定権と患者主権の萌芽 | comp=6.9 / impact=medium / H2 | — | 3.42 |
| 72 | 2025-Q1 | 医療制度の「自律的健康管理化」と「予防産業化」による脱医療化の加速 | comp=6.8 / impact=high / H2 | [BBC Health](https://www.bbc.com/news/articles/c3wlpw3l03qo?at_medium=RSS&at_campaign=rss) | 3.48 |
| 73 | 2025-Q1 | 「デジタル権利の『負の権利化』」：アクセス制限から監視回避への転換 | comp=6.8 / impact=medium / H2 | [EFF](https://www.eff.org/press/releases/eff-sues-dhs-and-ice-records-subpoenas-seeking-unmask-online-critics-0) | 3.38 |
| 74 | 2025-Q2 | 医療制度の「自律的健康管理化」における予防産業の爆発的成長と脱医療化の加速 | comp=6.8 / impact=high / H2 | [日経ビジネス](https://business.nikkei.com/atcl/gen/19/00808/031800006/) | 3.48 |
| 75 | 2006-H1 | 携帯電話による児童監視と親権・プライバシーの衝突 | comp=6.8 / impact=medium / H2 | — | 3.28 |
| 76 | 2017-H1 | グローバル不平等の構造化と可視化 | comp=6.8 / impact=high / H1 | — | 3.61 |
| 77 | 1963-H1 | 東欧圏内での権力分散と独立志向の顕在化 | comp=6.8 / impact=high / H2 | — | 3.51 |
| 78 | 1903-H2 | 工業用動力源の多様化と分散型エネルギー利用の開始 | comp=6.8 / impact=medium / H2 | — | 3.28 |
| 79 | 1979-H2 | アジア太平洋地域の核政策の多様化 | comp=6.8 / impact=medium / H3 | — | 3.28 |
| 80 | 2026-04-20 | 戦争長期化による『国際人道法の作動不可能性』の制度的認識 | comp=6.7 / impact=high / H1 | [Eurozine](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) | 3.7 |
| 81 | 1949-H1 | 戦後日本の経済的再編と通貨安定化の構造的依存 | comp=6.7 / impact=high / H2 | — | 3.53 |
| 82 | 2025-Q2 | 「医療制度の『自律的健康管理化』と『予防産業化』による脱医療化」 | comp=6.6 / impact=medium / H2 | [BBC Health](https://www.bbc.com/news/articles/c3wlpw3l03qo?at_medium=RSS&at_campaign=rss) | 3.37 |
| 83 | 1992-H1 | アフリカ大陸の民主化と紛争の並存による不安定化 | comp=6.6 / impact=high / H1 | — | 3.4 |
| 84 | 2014-H2 | ロボット・AI産業の規制フレームワークの欠落 | comp=6.6 / impact=high / H2 | — | 3.37 |
| 85 | 1955-H2 | 東欧における社会主義体制の多様化と自律性の萌芽 | comp=6.6 / impact=high / H3 | — | 3.17 |
| 86 | 1979-H1 | 生殖に関する女性の権利と社会的価値観の対立激化 | comp=6.6 / impact=high / H2 | — | 3.5 |
| 87 | 2015-H2 | デジタル・ウェアラブル技術の身体支配と個人的自律性の侵食 | comp=6.4 / impact=medium / H2 | — | 3.15 |
| 88 | 2011-H1 | テクノロジー企業の独占的支配への抵抗 | comp=6.4 / impact=medium / H2 | — | 3.13 |
| 89 | 2016-H2 | 自動運転車の『雨・工事』問題による実装遅延 | comp=6.3 / impact=high / H2 | — | 3.17 |
| 90 | 2013-H1 | 無人機規制と監視社会の予防的対抗 | comp=6.3 / impact=medium / H2 | — | 3.15 |
| 91 | 2008-H2 | スマートフォンの生活統合の深化 | comp=6.3 / impact=high / H1 | — | 3.27 |
| 92 | 1976-H2 | フランスの中絶法制化と女性の身体的自律権の確立 | comp=6.3 / impact=medium / H2 | — | 3.27 |
| 93 | 2026-04-20 | 「シマ」文化と地縁アイデンティティの言語的再活性化による地域経済主権の奪還 | comp=6.2 / impact=medium / H3 | [greenz.jp](https://greenz.jp/2026/03/19/code-for-japan/) | 3.01 |
| 94 | 2026-04-20 | インド食文化の「グローバル西洋化」に対する組織的な独自文化戦略の国営化 | comp=6.2 / impact=medium / H3 | — | 3.01 |
| 95 | 1901-H1 | オーストラリアにおける連邦制国家形成と自治的権力構造の確立 | comp=6.2 / impact=high / H2 | — | 3.39 |
| 96 | 2026-Q2 | ドローン配送による医療ロジスティクス革新と規制の先制的対応 | comp=6.1 / impact=medium / H2 | — | 3.03 |
| 97 | 2010-H2 | 避妊技術の急速な多様化と利用拡大 | comp=6.1 / impact=medium / H2 | — | 3.16 |
| 98 | 1933-H1 | 労働組織化と国家統制の対立激化 | comp=6.1 / impact=high / H1 | — | 3.26 |
| 99 | 2018-H2 | クラウドコンピューティングによる経済集中と寡占化 | comp=6.0 / impact=high / H1 | — | 3.25 |
| 100 | 2009-H2 | 支援自殺の法的・倫理的パラダイム転換 | comp=6.0 / impact=medium / H2 | — | 3.02 |

## 2. Physical AI クロスインパクト Top 30 (労働 / 教育 / 医療 / 軍事 / 環境)
source = Physical AI 系シグナル / target = 5 ドメイン (labor/employ, educ, health/medical, military/defense, environ/climate/energy + 日本語)
ヒット: 全 1,806 件中該当 30 件超 / |impact_score| 降順 Top 30

| # | impact | type | source | → target | 出典 |
|---|--------|------|--------|---------|------|
| 1 | 3.0 | amplify | 非国家主体による地政学的代理戦争の自動化 | 「AI企業による地政学的プレイヤー化」と国家主権の形骸化 | [link](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) |
| 2 | 2.1 | amplify | 「非国家主体による地政学的権力行使」と国家主権の形式的化 | 超知能規制の階級的分裂による民主的コンセンサス構造の崩壊 | [link](https://www.nytimes.com/2026/04/20/us/politics/trump-administration-tariff-refunds.html) |
| 3 | 2.1 | amplify | 「非国家主体による地政学的権力行使」と国家主権の形式的化 | 地球圏新規力：無機プロセスの自律的主体化 | [link](https://www.nytimes.com/2026/04/20/us/politics/trump-administration-tariff-refunds.html) |
| 4 | 2.1 | amplify | 「非国家主体による地政学的権力行使」と国家主権の形式的化 | 超知能規制の階級的分裂：市民拒否と国家安全保障機関の採用の並行進行 | [link](https://www.nytimes.com/2026/04/20/us/politics/trump-administration-tariff-refunds.html) |
| 5 | 2.1 | amplify | 「非国家主体による地政学的権力行使」と国家主権の形式的化 | 『生命権』から『自己統治権』への環境正義フレームの急進的転換 | [link](https://www.nytimes.com/2026/04/20/us/politics/trump-administration-tariff-refunds.html) |
| 6 | 2.1 | amplify | 「非国家主体による地政学的権力行使」と国家主権の形式的化 | 非国家主体による地政学的代理戦争の自動化 | [link](https://www.nytimes.com/2026/04/20/us/politics/trump-administration-tariff-refunds.html) |
| 7 | 2.0 | amplify | 地球圏新規力：無機プロセスの自律的主体化 | 超知能規制の階級的分裂：市民拒否と国家安全保障機関の採用の並行進行 | [link](https://www.sciencedaily.com/releases/2026/04/260419054825.htm) |
| 8 | 2.0 | transform | 地球圏新規力：無機プロセスの自律的主体化 | 『生命権』から『自己統治権』への環境正義フレームの急進的転換 | [link](https://www.sciencedaily.com/releases/2026/04/260419054825.htm) |
| 9 | 2.0 | amplify | 地球圏新規力：無機プロセスの自律的主体化 | NSAおよび国防部によるクローズドソースAI採用と国家安全保障の新しい脆弱性 | [link](https://www.sciencedaily.com/releases/2026/04/260419054825.htm) |
| 10 | 2.0 | catalyze | 非国家主体による地政学的代理戦争の自動化 | ホルムズ海峡複合インフラ脆弱性の構造化：エネルギー-情報-金融の同時遮断可能性 | [link](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) |
| 11 | 1.4 | amplify | 非国家主体による地政学的代理戦争の自動化 | 『戦争実装の完全自動化』とAI標的化の予測不可能性 | [link](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) |
| 12 | 1.4 | amplify | 非国家主体による地政学的代理戦争の自動化 | 「核兵器技術のSaaS化」と検証不可能な軍事戦力の非対称的拡散 | [link](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) |
| 13 | 1.4 | amplify | 『戦争実装の完全自動化』とAI標的化の予測不可能性 | 非国家主体による地政学的代理戦争の自動化 | [link](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) |
| 14 | 1.4 | amplify | 『戦争実装の完全自動化』とAI標的化の予測不可能性 | 「核兵器技術のSaaS化」と検証不可能な軍事戦力の非対称的拡散 | [link](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) |
| 15 | 1.4 | amplify | 地球圏新規力：無機プロセスの自律的主体化 | 超知能規制の階級的分裂による民主的コンセンサス構造の崩壊 | [link](https://www.sciencedaily.com/releases/2026/04/260419054825.htm) |
| 16 | 1.4 | amplify | 非国家主体による地政学的代理戦争の自動化 | 超知能規制の階級的分裂による民主的コンセンサス構造の崩壊 | [link](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) |
| 17 | 1.4 | amplify | 非国家主体による地政学的代理戦争の自動化 | 超知能規制の階級的分裂：市民拒否と国家安全保障機関の採用の並行進行 | [link](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) |
| 18 | 1.4 | catalyze | 非国家主体による地政学的代理戦争の自動化 | 『生命権』から『自己統治権』への環境正義フレームの急進的転換 | [link](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) |
| 19 | 1.38 | amplify | 「非国家主体による地政学的権力行使」と国家主権の形式的化 | 通貨政策と雇用目標の明示的分離による福祉国家の根本矛盾の露呈 | [link](https://www.nytimes.com/2026/04/20/us/politics/trump-administration-tariff-refunds.html) |
| 20 | 1.28 | amplify | 『戦争実装の完全自動化』とAI標的化の予測不可能性 | 超知能規制の階級的分裂による民主的コンセンサス構造の崩壊 | [link](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) |
| 21 | 1.27 | amplify | 地球圏新規力：無機プロセスの自律的主体化 | 気候災害による民主主義機能の段階的喪失と統治パラダイムの急速転換 | [link](https://www.sciencedaily.com/releases/2026/04/260419054825.htm) |
| 22 | 1.27 | amplify | 『戦争実装の完全自動化』とAI標的化の予測不可能性 | 超知能規制の階級的分裂：市民拒否と国家安全保障機関の採用の並行進行 | [link](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) |
| 23 | 1.26 | amplify | 地球圏新規力：無機プロセスの自律的主体化 | 『データ地層化』による身体的監視と自動管理の深化：デジタル都市基盤への無意識的従属 | [link](https://www.sciencedaily.com/releases/2026/04/260419054825.htm) |
| 24 | 1.26 | amplify | 「非国家主体による地政学的権力行使」と国家主権の形式的化 | 地政学的抗争による『海底インフラの戦場化』と情報物理融合の脆弱性 | [link](https://www.nytimes.com/2026/04/20/us/politics/trump-administration-tariff-refunds.html) |
| 25 | 1.02 | amplify | 地球圏新規力：無機プロセスの自律的主体化 | 『データ地層化』による身体的監視深化と市民の無意識的従属 | [link](https://www.sciencedaily.com/releases/2026/04/260419054825.htm) |
| 26 | 1.02 | amplify | 非国家主体による地政学的代理戦争の自動化 | 地政学的抗争による『海底インフラの戦場化』と情報物理融合の脆弱性 | [link](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) |
| 27 | 1.02 | amplify | 『戦争実装の完全自動化』とAI標的化の予測不可能性 | ホルムズ海峡複合インフラ脆弱性の構造化：エネルギー-情報-金融の同時遮断可能性 | [link](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) |
| 28 | 1.02 | amplify | 『戦争実装の完全自動化』とAI標的化の予測不可能性 | 「AI企業による地政学的プレイヤー化」と国家主権の形骸化 | [link](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) |
| 29 | 1.02 | amplify | 『戦争実装の完全自動化』とAI標的化の予測不可能性 | NSAおよび国防部によるクローズドソースAI採用と国家安全保障の新しい脆弱性 | [link](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) |
| 30 | 1.02 | amplify | 『戦争実装の完全自動化』とAI標的化の予測不可能性 | 「国家外交権の企業化」と非国家主体による条約的交渉の制度化 | [link](https://www.eurozine.com/new-realities-of-war/?utm_source=rss&utm_medium=rss&utm_campaign=new-realities-of-war) |

### rationale (主要5件抜粋)

- **1.** 非国家主体による地政学的代理戦争の自動化 → 「AI企業による地政学的プレイヤー化」と国家主権の形骸化: llm:企業台頭
- **2.** 「非国家主体による地政学的権力行使」と国家主権の形式的化 → 超知能規制の階級的分裂による民主的コンセンサス構造の崩壊: llm_rev:権力分散
- **3.** 「非国家主体による地政学的権力行使」と国家主権の形式的化 → 地球圏新規力：無機プロセスの自律的主体化: llm_rev:国家権力削弱
- **4.** 「非国家主体による地政学的権力行使」と国家主権の形式的化 → 超知能規制の階級的分裂：市民拒否と国家安全保障機関の採用の並行進行: llm_rev:二重権力
- **5.** 「非国家主体による地政学的権力行使」と国家主権の形式的化 → 『生命権』から『自己統治権』への環境正義フレームの急進的転換: llm_rev:権力移転

## 3. アラート (高 confidence) Top 20
level=critical/high 抽出 (ratio 降順) — signal-db Alert system は SURGE/EMERGENCE/CROSSOVER の3パターン

| # | 年月 | type | level | topic | alert | mentions | ratio | hist_avg | 出典 |
|---|------|------|-------|-------|-------|---------|-------|---------|------|
| 1 | 2026-04 | SURGE | high | iran war | ホルムズ海峡危機の顕在化 | 484 | 122532.7 | 0.0 | ["Environmental", "Legal", "Ec |
| 2 | 2026-04 | SURGE | high | iran war | イラン戦争報道の急増 | 467 | 118228.8 | 0.0 | ["Environmental", "Legal", "Ec |
| 3 | 2026-04 | SURGE | high | iran war | イラン戦争関連報道の急増 | 445 | 112659.2 | 0.0 | ["Environmental", "Legal", "Ec |
| 4 | 2026-04 | SURGE | high | iran war | ホルムズ海峡危機の新出現 | 426 | 107849.0 | 0.0 | ["Environmental", "Legal", "Ec |
| 5 | 2026-04 | SURGE | high | iran war | イラン戦争報道の激増 | 410 | 103798.3 | 0.0 | ["Environmental", "Legal", "Ec |
| 6 | 2026-04 | SURGE | high | iran war | イラン戦争の急増報道 | 390 | 98735.0 | 0.0 | ["Environmental", "Legal", "Ec |
| 7 | 2026-04 | SURGE | high | reuters | ロイター報道量の急増 | 445 | 75106.1 | 0.0 | ["Environmental", "Legal", "Ec |
| 8 | 2026-04 | SURGE | high | starmer | プライバシー権と企業統制の対立 | 146 | 73924.7 | 0.0 | ["Environmental", "Legal", "So |
| 9 | 2026-04 | SURGE | high | starmer | イラン停戦交渉の新段階 | 139 | 70380.3 | 0.0 | ["Environmental", "Legal", "So |
| 10 | 2026-04 | SURGE | high | starmer | イラン和平交渉が初浮上 | 137 | 69367.7 | 0.0 | ["Environmental", "Legal", "So |
| 11 | 2026-04 | SURGE | high | artemis | ハンガリー極右台頭と民主主義危機 | 131 | 66329.7 | 0.0 | ["Environmental", "Legal", "Ec |
| 12 | 2026-04 | SURGE | high | artemis | プライバシー防衛運動の拡大 | 130 | 65823.3 | 0.0 | ["Environmental", "Legal", "Ec |
| 13 | 2026-04 | SURGE | high | reuters | イラン戦争の急速な台頭 | 775 | 65401.4 | 0.0 | ["Environmental", "Legal", "Ec |
| 14 | 2026-04 | SURGE | high | starmer | イラン休戦議論の顕在化 | 129 | 65317.0 | 0.0 | ["Environmental", "Legal", "So |
| 15 | 2026-04 | SURGE | high | artemis | トランプ・イラン政策が焦点化 | 128 | 64810.7 | 0.0 | ["Environmental", "Legal", "Ec |
| 16 | 2026-04 | SURGE | high | artemis | プライバシー権擁護運動の拡大 | 125 | 63291.7 | 0.0 | ["Environmental", "Legal", "Ec |
| 17 | 2026-04 | SURGE | high | reuters | ロイター報道の急増 | 496 | 62785.3 | 0.0 | ["Environmental", "Legal", "Ec |
| 18 | 2026-04 | SURGE | high | artemis | アルテミス月面計画の加速 | 124 | 62785.3 | 0.0 | ["Environmental", "Legal", "Ec |
| 19 | 2026-04 | SURGE | high | artemis | イラン石油価格への影響顕在化 | 123 | 62279.0 | 0.0 | ["Environmental", "Legal", "Ec |
| 20 | 2026-04 | SURGE | high | starmer | 英国スターマー首相の政治危機 | 119 | 60253.7 | 0.0 | ["Environmental", "Legal", "So |

## 4. パターン別事例: SURGE / EMERGENCE / CROSSOVER / SANGAKU_LINK
SURGE = 急増 / EMERGENCE = 新出 / CROSSOVER = 横断 / SANGAKU_LINK = 産学連携 (本 alerts には存在しないため別途注記)
各パターン level 優先・ratio 降順 Top 例示

### SURGE (72件中Top10)

| 年月 | level | topic | alert | mentions | ratio | hist_avg |
|------|-------|-------|-------|---------|-------|---------|
| 2026-04 | high | iran war | ホルムズ海峡危機の顕在化 | 484 | 122532.7 | 0.0 |
| 2026-04 | high | iran war | イラン戦争報道の急増 | 467 | 118228.8 | 0.0 |
| 2026-04 | high | iran war | イラン戦争関連報道の急増 | 445 | 112659.2 | 0.0 |
| 2026-04 | high | iran war | ホルムズ海峡危機の新出現 | 426 | 107849.0 | 0.0 |
| 2026-04 | high | iran war | イラン戦争報道の激増 | 410 | 103798.3 | 0.0 |
| 2026-04 | high | iran war | イラン戦争の急増報道 | 390 | 98735.0 | 0.0 |
| 2026-04 | high | reuters | ロイター報道量の急増 | 445 | 75106.1 | 0.0 |
| 2026-04 | high | starmer | プライバシー権と企業統制の対立 | 146 | 73924.7 | 0.0 |
| 2026-04 | high | starmer | イラン停戦交渉の新段階 | 139 | 70380.3 | 0.0 |
| 2026-04 | high | starmer | イラン和平交渉が初浮上 | 137 | 69367.7 | 0.0 |

### EMERGENCE (72件中Top10)

| 年月 | level | topic | alert | mentions | ratio | hist_avg |
|------|-------|-------|-------|---------|-------|---------|
| 2026-04 | high | strait hormuz | 中東全体への技術戦争拡大 | 157 | — | — |
| 2026-04 | high | price latest | ※ノイズの可能性が高い | 54 | — | — |
| 2026-04 | high | latest reuters | ※ノイズの可能性が高い | 54 | — | — |
| 2026-04 | high | iran talks | ※ノイズの可能性が高い | 51 | — | — |
| 2026-04 | high | iran ceasefire | ※ノイズの可能性が高い | 46 | — | — |
| 2026-04 | high | trump iran | ※ノイズの可能性が高い | 45 | — | — |
| 2026-04 | high | privacy defender | ※ノイズの可能性が高い | 43 | — | — |
| 2026-04 | high | hungary election | hungary election | 39 | — | — |
| 2026-04 | high | inside health | inside health | 36 | — | — |
| 2026-04 | high | itmedia mobile | itmedia mobile | 36 | — | — |

### CROSSOVER (30件中Top10)

| 年月 | level | topic | alert | mentions | ratio | hist_avg |
|------|-------|-------|-------|---------|-------|---------|
| 2026-04 | high | iran war | ホルムズ海峡危機の初出現 | 390 | — | — |
| 2026-04 | high | strait hormuz | アルテミス月面計画の注目集中 | 157 | — | — |
| 2026-04 | high | middle east | 英国スターマー首相の政策転換 | 126 | — | — |
| 2026-04 | high | europe | ハンガリー選挙と言論統制強化 | 123 | — | — |
| 2026-04 | high | chinese | 中国テック企業の香港集約化 | 106 | — | — |
| 2026-04 | high | iran war | イラン戦争の多領域影響 | 410 | — | — |
| 2026-04 | high | strait hormuz | ホルムズ海峡の全領域波及 | 168 | — | — |
| 2026-04 | high | europe | 欧州の戦略的模索 | 136 | — | — |
| 2026-04 | high | middle east | 中東紛争の技術化 | 134 | — | — |
| 2026-04 | high | japan | 日本の観光経済変動 | 116 | — | — |

### SANGAKU_LINK (産学連携シグナル)

signal.db.backup-20260426 の `alerts` テーブルには `alert_type='SANGAKU_LINK'` のレコードは存在しない。
これは miratuku-daily-pipeline の `05_signal_extract.py` 内 rule-based extractor が PR Times RSS + 産学連携プレスリリースを対象に独立処理するパターン名で、別 DB (`sangaku_press_releases.db`) に格納される。
代替指標: Sangaku R&D PR DB (`/Users/nishimura+/projects/research/sangaku-rd-database/data/sangaku_rd.db`) 内 11,997 PR から `テーマ LIKE '%ロボット%' OR '%Physical AI%' OR '%自律%'` で抽出すること。

## 5. 2024-2026 の決定的シグナル 30件
signal_period_start ∈ [2024-01, 2026-12] かつ (impact ∈ {critical, high} OR composite_score ≥ 0.5)
composite_score 降順 / period_start 降順

| # | 年月 | シグナル | 数値・スコア | 3H | type | 出典 | Tetlock |
|---|------|----------|------------|----|------|------|--------|
| 1 | 2026-04 | AI生成コンテンツによる情報環境の急速な汚染 | comp=8.7 / critical | H2 | wild_card | — | 4.35 |
| 2 | 2024-01 | 「法的解釈可能性の喪失」としてのAI-to-AI通信システムの制度化 | comp=8.5 / high | H1 | paradigm_shift | [ScienceDaily](https://www.sciencedaily.com/releases/2026/04/260420014748.htm) | 4.21 |
| 3 | 2026-04 | AI安全性評価の分裂と規制ギャップの拡大 | comp=8.4 / critical | H2 | emerging_trend | — | 4.36 |
| 4 | 2025-04 | AI知的財産権紛争の法的パラダイム転換 | comp=8.4 / critical | H2 | paradigm_shift | — | 4.26 |
| 5 | 2026-04 | 民主主義制度への根本的不信と離脱の加速 | comp=8.2 / critical | H2 | paradigm_shift | — | 4.12 |
| 6 | 2024-01 | 極端気象による民主主義システムの脆弱化と権威主義化の正の相関構造化 | comp=8.2 / high | H1 | paradigm_shift | [Guardian World](https://www.theguardian.com/global-development/2026/apr/22/climate-change-extreme-weather-heatwaves-floods-wildfires-threat-democracy-elections) | 4.22 |
| 7 | 2024-01 | 「イラン戦争のAI情報化」による軍事的不確実性の急速化と予測不可能性 | comp=8.2 / high | H1 | wild_card | [Wedge Online](https://wedge.ismedia.jp/articles/-/40497) | 4.07 |
| 8 | 2024-01 | 「戦争のデータセンター化」による軍事戦略の非物理的転換 | comp=8.2 / high | H1 | weak_signal | [Wedge Online](https://wedge.ismedia.jp/articles/-/40497) | 4.21 |
| 9 | 2024-01 | 「AI-to-AI競争」による人間による解釈可能性の根本喪失 | comp=8.2 / high | H1 | weak_signal | [ITmedia](https://www.itmedia.co.jp/business/articles/2604/24/news009.html) | 4.12 |
| 10 | 2026-04 | AI通信能力の自発的発現と人間的知性との融合 | comp=8.1 / critical | H3 | wild_card | — | 3.98 |
| 11 | 2025-07 | 政治的信頼性危機と「嘘の違法化」への動き | comp=8.1 / critical | H2 | paradigm_shift | — | 4.11 |
| 12 | 2024-01 | 「『AI-to-AI競争』による人間による解釈可能性の根本的喪失」 | comp=8.1 / high | H3 | wild_card | [ITmedia](https://www.itmedia.co.jp/business/articles/2604/24/news009.html) | 4.08 |
| 13 | 2024-01 | 「イラン戦争のAI化」による軍事的不確実性の急速化と予測政治の破綻 | comp=8.1 / high | H1 | wild_card | [Wedge Online](https://wedge.ismedia.jp/articles/-/40531) | 3.98 |
| 14 | 2024-01 | ガザ地域の「子ども音声喪失症候群」の大規模化による紛争の神経発達的後遺症化 | comp=8.1 / high | H1 | paradigm_shift | — | 3.98 |
| 15 | 2025-04 | 民主主義の機能不全と権威主義的代替案の台頭 | comp=8.0 / critical | H1 | emerging_trend | — | 4.12 |
| 16 | 2024-01 | 量子技術・光学通信における中国の自律的開発加速と「AI時代の供給鎖の再地政学化」 | comp=8.0 / high | H1 | paradigm_shift | [日経ビジネス](https://business.nikkei.com/atcl/gen/19/00485/042200136/) | 4.1 |
| 17 | 2024-01 | 「選挙制度の根本的脱正当化」と非制度的主権回復の並行化 | comp=8.0 / high | H1 | paradigm_shift | [The Diplomat](https://thediplomat.com/2026/04/philippine-legislators-set-to-vote-on-impeachment-complaint-against-vice-president/) | 4.1 |
| 18 | 2024-01 | 「戦争のAI情報化」による軍事戦略の非人間的高速化 | comp=8.0 / high | H1 | wild_card | [ScienceDaily](https://www.sciencedaily.com/releases/2026/04/260420014748.htm) | 3.83 |
| 19 | 2024-01 | AIデータセンターの隠蔽された炭素負債と気候コスト会計の全面矛盾化 | comp=8.0 / high | H1 | weak_signal | [EnergyShift](https://energyshift.com/recalibrating-the-timeline-for-a-transition-to-renewable-energy-sources/) | 4.1 |
| 20 | 2024-01 | インド民間人投票権喪失の大規模化による選挙システム正当性危機 | comp=8.0 / high | H1 | counter_trend | [Guardian World](https://www.theguardian.com/world/2026/apr/22/india-west-bengal-state-elections-millions-stripped-of-vote) | 4.12 |
| 21 | 2024-01 | 「データセンター化する民主主義」：AI規制と情報インフラの統合による統治モデルの変質 | comp=7.9 / high | H1 | paradigm_shift | [BUSINESS LAWYERS](https://www.businesslawyers.jp/articles/1532) | 3.84 |
| 22 | 2024-01 | 「選挙制度の根本的脱正当化」と非制度的主権表現の並行化 | comp=7.9 / high | H3 | paradigm_shift | [The Diplomat](https://thediplomat.com/2026/04/philippine-legislators-set-to-vote-on-impeachment-complaint-against-vice-president/) | 3.87 |
| 23 | 2024-01 | 「真菌・マイクロバイオーム」の脱人間中心的再発見による生態系価値転換 | comp=7.9 / high | H3 | paradigm_shift | [ScienceDaily](https://www.sciencedaily.com/releases/2026/04/260420014735.htm) | 3.97 |
| 24 | 2024-01 | 「こども選挙」による制度的主権再分配と世代民主主義の実装化 | comp=7.9 / high | H3 | paradigm_shift | [greenz.jp](https://greenz.jp/2026/02/24/kodomo-senkyo/) | 3.84 |
| 25 | 2026-04 | 労働市場の急速な政治化と大量離脱の予兆 | comp=7.8 / critical | H1 | emerging_trend | — | 4.11 |
| 26 | 2026-04 | 環境規制と開発圧力の衝突激化 | comp=7.8 / high | H2 | counter_trend | — | 3.99 |
| 27 | 2026-01 | 政治的分極化による民主主義制度への信頼喪失 | comp=7.8 / critical | H1 | emerging_trend | — | 4.01 |
| 28 | 2026-01 | AI生成児童虐待画像の急速な現実化 | comp=7.8 / critical | H1 | wild_card | — | 4.01 |
| 29 | 2024-01 | エネルギー危機による民主主義形式の脱構築 | comp=7.8 / high | H1 | paradigm_shift | [Guardian World](https://www.theguardian.com/global-development/2026/apr/22/climate-change-extreme-weather-heatwaves-floods-wildfires-threat-democracy-elections) | 3.86 |
| 30 | 2024-01 | 「核自決権」の非公式化と核兵器開発の民主化加速 | comp=7.8 / high | H1 | wild_card | [The Diplomat](https://thediplomat.com/2026/04/why-the-2026-npt-review-conference-and-diplomacy-must-not-fail/) | 3.96 |

### 主要5件 description 全文

**1. AI生成コンテンツによる情報環境の急速な汚染** (`2026-04-01`)

> 「From South Park v Trump to AI slopaganda: deepfakes are now part of the news cycle」で情報真正性の危機が制度化。「Lawyer caught using AI-generated false citations in court case penalised in Australian first」で法的信頼基盤が侵蝕。「Alternative data suggest uneven inflation amid Trump's numbers skepticism」で統計的客観性そのものが疑われ始める。

**2. 「法的解釈可能性の喪失」としてのAI-to-AI通信システムの制度化** (`2024-01-01`)

> DeepSeekやMythosといった対AI防御型AIシステムが人間による解釈・監視を不可能にする速度と複雑性で動作。法執行機関・規制当局が「何が起きているのか理解できない」状態が制度化される兆候。これは法的責任と監視可能性の根本的な前提を破壊する。

出典: ScienceDaily — https://www.sciencedaily.com/releases/2026/04/260420014748.htm

**3. AI安全性評価の分裂と規制ギャップの拡大** (`2026-04-01`)

> 「Google DeepMind Falls Behind OpenAI in Latest Safety Review」「ChatGPT offered bomb recipes and hacking tips during safety tests」など、AI企業間の安全性基準の乖離が顕在化。同時に「China calls for global AI cooperation days after Trump administration unveils low-regulation strategy」で、規制アプローチの地政学的分岐が進行。技術的能力と安全保障の非対称性が構造化している。

**4. AI知的財産権紛争の法的パラダイム転換** (`2025-04-01`)

> 「'Impossible' to create AI tools like ChatGPT without copyrighted material, OpenAI says」と「OpenAI claims New York Times 'hacked' ChatGPT」の対立から、既存著作権法がAI学習に対応不可能であることが露呈。「Scarlett Johansson's OpenAI clash is just the start of legal wrangles」は単なる個別事件ではなく、知的財産権体系全体の再構築が不可避であることを示唆。

**5. 民主主義制度への根本的不信と離脱の加速** (`2026-04-01`)

> 「Kamala Harris says she doesn't plan to return to 'broken' system of US politics」という主流政治家による制度放棄宣言と「Zack Polanski's victory brings hope for a new kind of politics」の新型政治への期待が並立。「We feel duped and insulted by this Labour government」「Labour does not deserve to win next election without change」の市民感情と「Vi

---

## 抽出方法注記

1. **DB ソース**: signal.db.backup-20260426 (2026-04-26 時点 Wave 1 スナップショット)
   - signals 6,885 / signal_cross_impact 1,806 / alerts 174 / signal_article_links 1,483
   - 現行 live signal.db (159 signals) は Wave 1 リセット後再構築中のためバックアップを採用
2. **URL 結合**: `ATTACH '...pestle.db' AS p` + `signal_article_links → articles.url`
3. **Physical AI 定義**: 英語7語 + 日本語10語の OR フィルタ (122 件マッチ)
4. **Tetlock score**: signal-db agent 仕様の 5 次元重み付き合成を 0-5 に正規化
   = (novelty 0.20 + disruption 0.20 + connectivity 0.20 + credibility 0.25 + composite/10 0.15) × 5
5. **時系列基準**: `signal_period_start` (signal が指す時間軸) を優先、無ければ `signal_period` (1900s/2025-Q2 等)
   `detected_date` (2026-04-20〜25 がほぼ全件) は分析実行日であり信号自体の年月ではない点に留意
6. **出典欠落**: signal_article_links 未紐付け signal が約7割 (paradigm_shift 型はクラスタ合成のため
   個別記事に遡れないものが多い)。これらは "—" 表記
