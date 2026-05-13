# Stream 4: Materials/Energy系統 — Physical AIを支える物質基盤の系譜と未来軌道

Physical AI は計算アルゴリズムだけで成立する技術ではない。身体を動かすアクチュエータ、感覚を取り出すセンサ、電力を貯蔵するバッテリー、推論を担う半導体、そしてそれら全体を駆動する一次エネルギー — これらの物理基盤の進化速度に律動されて、Physical AI のロードマップは伸縮する。本稿は PHAI-DB の既存5系統（HW / Control / RL / FM / Sim）に **Stream 4: Materials/Energy** を独立系統として加える根拠と、その系譜・現状・2030-2100軌道・PHAI-DB拡張提案を整理する。

---

## 1. 系譜 — 4本の柱で読む過去70年

Physical AI のハードウェア層は、概ね次の4本の柱の積み重なりとして読める。それぞれが独立に進化しつつ、Moore的曲線・Wright的経験曲線・Swanson的太陽光曲線という異なる学習率で進んでいる。

### 1.1 半導体（計算と推論の物理基盤）

1947年に Bardeen / Brattain / Shockley がベル研で点接触トランジスタを実証してから、半導体は集積度を約2年で倍化する Moore's law（Gordon Moore, 1965, *Electronics* 38(8)）を50年以上維持してきた。1990年代の銅配線・2000年代の歪みシリコン・2011年の Intel 22nm FinFET・2022年の Samsung / TSMC 3nm GAA（Gate-All-Around）と、構造変化で延命を続けてきた。

2010年代後半からは「Post-Moore」と呼ばれる転換が並行している。アクセラレータ専用化（NVIDIA H100/B200, Google TPU v5/v6, AWS Trainium2）、3次元積層（HBM3E, CFET in development at imec/TSMC）、Chiplet（AMD MI300, UCIe 規格）、そして光インターコネクト（Ayar Labs TeraPHY, Lightmatter Passage）。Physical AI 文脈では特に **エッジ推論用低電力チップ** の系譜が重要で、Google Edge TPU（2018）→ NVIDIA Jetson Orin（2022）→ Qualcomm Cloud AI 100 / Hexagon NPU（2023-2025）と進む。

### 1.2 バッテリー（移動体の自律時間を決める）

鉛蓄電池（Gaston Planté, 1859）→ NiCd（1899）→ NiMH（1989）→ Li-ion（Whittingham / Goodenough / Yoshino, 1980-1991商用化, 2019年ノーベル化学賞）と進んだ。1991年 Sony 18650 セル商用化時点で 80 Wh/kg だった重量エネルギー密度は、2024年時点で NMC811 セルで 270-300 Wh/kg、CATL Qilin / BYD Blade のパック効率向上で実効 250 Wh/kg に近づいた。

次の主戦場が **全固体電池**。Goodenough らの 2017 年の Li-glass 電池論文、Toyota の硫化物系（2014年特許群、2027-2028年量産予告）、QuantumScape の酸化物系（NASDAQ:QS, Volkswagen 提携）、Samsung SDI / SK On / LG Energy Solution のパイロットライン稼働。理論密度 500 Wh/kg を超える可能性があり、Physical AI のヒューマノイドや配送ドローンの **稼働時間 4-8時間 → 16-24時間** という質的転換の前提となる。

並行して **Li-S（Lyten, Stellantis 提携 2023）**、**Na-ion（CATL 2023, Northvolt 2024）**、**金属空気電池（IBM Air Battery, Toyota Li-air）**、**レドックスフロー（Sumitomo Electric V-flow, ESS Inc 鉄フロー）** が用途別に分岐している。

### 1.3 太陽光（一次エネルギーの限界費用ゼロ化）

c-Si（結晶シリコン）モジュール価格は1976年の106 USD/W から2024年に約0.10-0.13 USD/W へ約1000倍下落した（IEA PVPS Trends 2024, BNEF）。Swansonの法則（出荷量倍加で約20%価格低下）が50年間持続している学習曲線の代表例である。

2009年に Miyasaka らが報告したペロブスカイト太陽電池（*JACS* 131:6050）が、わずか15年で研究室効率 26.7%（NREL Best Research-Cell Efficiency Chart, 2024）に到達。c-Si とのタンデムでは 33-34% を超え（HZB 2024, LONGi 2024, Oxford PV 商用化準備）、シリコン単体の理論限界 29.4% を破った。商用化の障壁は耐久性（屋外20年保証）と Pb 環境規制で、Saule Technologies / Oxford PV / Microquanta が屋根向け・建材向けで先行展開。

### 1.4 量子計算（最適化と材料設計の指数加速候補）

Richard Feynman の 1982 年講演（*Int J Theor Phys* 21:467）に源流を持つ。1994年 Shor algorithm、1998年 NMR 2量子ビット実証、2019年 Google Sycamore の量子超越（53qubit, *Nature* 574:505）、2023年 IBM Condor 1121qubit、2024年 Google Willow による表面符号エラー訂正で「論理量子ビット数を増やすほどエラー率が下がる」しきい値突破（*Nature* 638:920, 2025）。

Physical AI 文脈での量子計算は、(i) ロボット最適化（経路計画・スケジューリング）、(ii) 材料設計（DFTのスケーラビリティ突破）、(iii) 化学反応シミュレーション（バッテリー電解質・触媒設計）で意味を持つ。ただし 2026 年時点ではフォールトトレラント量子計算機は研究段階で、Physical AI 実装への直接寄与は限定的。

---

## 2. 2026年現実 — 4つの臨界事象

### 2.1 AIによる材料発見の10倍加速

DeepMind GNoME（Graph Networks for Materials Exploration, *Nature* 624:80, 2023）は 220 万件の新規結晶構造候補を生成し、うち 38 万件が DFT で安定と評価された。LBNL の A-Lab（自律実験ロボット, *Nature* 624:86, 2023）はこの候補から 17 日間で 41 種の新規材料を合成成功した。Materials Project（Persson Group, LBNL, 15万化合物の物性データベース）と組み合わせ、従来 5-10 年かかった新材料発見が **数週間から数ヶ月** に短縮する基盤が整った。Physical AI への波及は、新規アクチュエータ材料（EAP, LCE）・触覚センサ膜・固体電解質・廃熱回収材で先行する。

### 2.2 固体電池の商用化前夜

Toyota は 2023 年 6 月の技術説明会で 2027-2028 年の全固体BEV商用化、航続 1200km・充電 10 分以下を公式宣言。Samsung SDI は 2024 年に S-Line（全固体パイロットライン）稼働、Mercedes-Benz / Stellantis にサンプル出荷開始。固体電池は Physical AI のヒューマノイド普及の最大律速要因の一つ（Boston Dynamics Atlas 電動版、Figure 02、Apptronik Apollo、Unitree H1/H2、Agility Digit 全てが稼働時間制約を抱える）。

### 2.3 SMRと核融合の二正面前進

SMR（Small Modular Reactor）は NuScale VOYGR（NRC 認証 2023, ただし UAMPS プロジェクトは 2024 年中止）、GE Hitachi BWRX-300（Ontario Power Generation 2029 稼働予定）、Rolls-Royce SMR（英国規制承認進行中）、TerraPower Natrium（ビル・ゲイツ、Wyoming 2030 稼働予定）が並走。

核融合では Commonwealth Fusion Systems（MIT スピンアウト、SPARC 装置 2026-2027 稼働予定、ARC 商用機 2030 年代）、TAE Technologies、Helion Energy（Microsoft が 2028 年から 50MW 電力購入契約）、Tokamak Energy が私的資金で先行。ITER は 2025-2026 年に First Plasma 予定（公式 ITER Council, 2024 update）。データセンター電力需要急増がこれらの「先延ばし不可」な投資判断を生んでいる。

### 2.4 データセンター電力の急増

IEA *Electricity 2024* レポートはデータセンターの世界電力消費を 2022 年 460 TWh → 2026 年に倍増（最大 1050 TWh）と推計。米国では 2024 年時点で総電力消費の約 4.5%（EIA, Lawrence Berkeley National Lab 報告）、2030 年に 7-12% との予測（EPRI 2024, Goldman Sachs Research 2024）。Microsoft の Three Mile Island Unit 1 再稼働契約（2024 年 9 月、Constellation Energy と 20 年 PPA）、Amazon の Talen Energy 原子力データセンター隣接、Google の Kairos Power 小型炉契約（2030-2035 稼働、500MW）は **AI と原子力の構造的合流** を示す。

---

## 3. 4時点軌道 — 2030 / 2050 / 2070 / 2100

### 3.1 2030年: 物質発見の自動化、固体電池量産

- **GNoME 後継 × A-Lab スケール展開**：自律実験ロボットが世界10カ所以上の国立研究所・大学で稼働、年間新規材料発見数 数千件規模。
- **固体電池 EV 標準化第一波**：Toyota / Samsung SDI / QuantumScape が NMC 全固体を量産（パック 350 Wh/kg）。ヒューマノイドの連続稼働時間 8-12 時間に到達。
- **ペロブスカイト・タンデムの商用屋根材**：効率 30-32% / kWh 単価 2-3 セント、建材一体型 PV が建築コード対応。
- **SMR 商用初号機稼働**：BWRX-300（Ontario）、NuScale 次案件、Rolls-Royce SMR、TerraPower Natrium のうち 2-3 機が運転開始。
- **半導体は 2nm-GAA → 1.4nm**：TSMC N2/A14、Samsung SF1.4、Intel 14A、エッジ AI 推論電力効率 2024 比 8-10 倍。

### 3.2 2050年: 核融合多基稼働、エネルギー単価半減

- **核融合の複数商用稼働**：CFS ARC、Helion、TAE が GW 級発電所として運転。地理的に集中する初期は AI データセンター・水素製造拠点に直結。
- **固体電池 / Li-S / 金属空気のミックス**：用途別に最適化、ヒューマノイド連続 24 時間稼働、配送ドローン 8 時間航続。
- **宇宙太陽光発電 (SBSP) 実証**：JAXA / ESA / Caltech SSPP（2023 年 MAPLE 軌道伝送実証済み）の延長で GW 級プロトタイプ。
- **AI 設計触媒で電解水素 < 1 USD/kg**：DOE Hydrogen Shot（2021 設定）の目標値達成、グリーンスチール・グリーンアンモニア商用化。
- **2D材料 / トポロジカル材料の量産デバイス**：MoS2 トランジスタ、グラフェン熱拡散、Weyl 半金属センサが Physical AI ハードに組み込み。

### 3.3 2070年: 量子-古典ハイブリッド基盤、宇宙太陽光本格化

- **フォールトトレラント量子計算機の論理量子ビット 10^4-10^6 級**：材料・触媒・タンパク設計の探索空間が古典 HPC の指数倍に。
- **宇宙太陽光発電 (GW 級) 商用**：地上 24 時間定常電力源として核融合と並列、AI データセンター電力の十分性が確保される。
- **海水ウラン抽出・トリウム溶融塩炉の補完運用**：化石資源依存からの完全脱却。
- **生物-機械ハイブリッド材料**：自己修復ポリマー、ミオシン駆動ソフトアクチュエータ、植物光合成ハイブリッドが Physical AI に統合。
- **AI 経済の電力単価 < 0.01 USD/kWh**：限界費用ゼロ化に近づき、計算とエネルギーが事業ボトルネックでなくなる。

### 3.4 2100年: エネルギー量制約の解消、ストック型事業へ

- **一人当たり一次エネルギー 数十 kW 規模が現実的**：核融合 + SBSP + 高効率蓄電でエネルギー希少性が消える。
- **Physical AI が物理世界の任意作業を実行**：原料採掘 → 精錬 → 製造 → リサイクルの全工程をロボットが担い、人類は意志決定と意味付けに集中。
- **事業はフロー型からストック型へ**：「年間販売台数」ではなく「設置されたインフラ群の運用」が利益源泉に。電力・水・廃熱・廃材の循環がコモディティ。
- **量子-古典-生物計算の三層化**：用途別に計算方式が並立、Physical AI は最適計算リソースを動的に選択。

---

## 4. AIとエネルギーの相互依存 — 二律背反と合流点

Physical AI ロードマップを描くとき、**「AI が進化するならエネルギー転換が加速し、エネルギーが律速ならば AI が失速する」** という強い結合を見落とすと、楽観過剰または悲観過剰のどちらかに振れる。

### 4.1 需要側の圧力

OpenAI GPT-4 の訓練電力は推定 50 GWh（公式値非開示、Lawrence Berkeley の Patterson et al. 2021 手法による推計）、Meta Llama 3.1 405B は約 30 GWh。推論はさらに大きく、ChatGPT のクエリ単位電力は約 2.9 Wh（Google検索の約10倍, IEA 2024）。Physical AI（ロボット）はクラウド推論依存型なら倍率がさらに上がる。**1台のヒューマノイドが24時間稼働するとき、本体のバッテリー消費（数 kWh）よりクラウド推論コスト（数十 kWh 換算）の方が大きくなる**可能性がある。

### 4.2 供給側の制約

米 PJM 系統では 2024 年に容量市場価格が前年比 9 倍に高騰し、データセンター需要が直接の原因として指摘された（PJM Capacity Auction 2025/2026, Reuters 2024年7月）。送電網増強は 8-12 年スパンの計画事項で、AI の指数成長スピード（年率 2-4 倍の演算需要増）に追いつかない。Northern Virginia（Loudoun County）、Dublin、Singapore で新規データセンター接続停止・遅延が起きている。

### 4.3 合流点（deep-knowledge 第八章「AGI×エネルギー転換」の構造）

書籍『深い知が拓く2100年』第八章は、AGI による分散制御（送電網最適化、需要応答、需要側柔軟性の獲得）が逆にエネルギー転換を加速させる相互強化サイクルを描く。**AI が電力を食うほど、AI が電力供給を設計する圧力が高まり、その設計能力が AI を支える** という正のフィードバックが 2025-2040 年の中核ダイナミクスとなる。Physical AI はこのループの両側に立つ — 計算需要としての負担と、エネルギーシステム運用主体としての貢献の両方で。

### 4.4 二つのリスクシナリオ

- **シナリオA（エネルギー律速）**：核融合・SMR が 2035 年までに商用化しない場合、データセンター新設が物理的に不可能となり、AI 進化が 2-3 年停滞 → Physical AI 普及も連動遅延。
- **シナリオB（材料律速）**：固体電池が 2030 年までに量産化できない場合、ヒューマノイドの稼働時間が現行 1-2 時間に留まり、産業実用域に届かない → Physical AI が「実験室で動く」段階で滞留。

両シナリオを同時に避ける条件として、**AI 設計の材料発見 × 自律実験ロボット** の正のフィードバックが 2026-2030 年に立ち上がるかが決定的。これが Stream 4 を独立系統として PHAI-DB に加える根拠である。

---

## 5. PHAI-DB拡張提案 — 35件のSQL INSERT

以下、`phai_concept`（28件）、`phai_milestones`（5件）、`phai_bottlenecks`（2件）に追加すべきレコード。subfield は新設の `phai_mat`（Materials/Energy系統）とする。`phai_streams` への追加も必要。

### 5.1 phai_streams 追加（新ストリーム定義）

```sql
INSERT INTO phai_streams (id, name_ja, description, era_start, related_subfields)
VALUES (
  'stream_mat',
  'マテリアル・エネルギー系',
  '半導体・バッテリー・太陽光・核分裂/融合・量子計算・新材料発見など、Physical AI の物理基盤を構成する材料とエネルギー技術の系統。AI設計材料・自律実験ロボット・固体電池量産・核融合実証で2026年現在が転換点',
  1947,
  'phai_mat'
);
```

### 5.2 phai_concept 追加（抜粋・代表28件）

```sql
-- 半導体系譜
INSERT INTO phai_concept VALUES ('phai_mat_0001', '点接触トランジスタ', 'Point-Contact Transistor', 'Point-Contact Transistor', 'ベル研で1947年に Bardeen / Brattain / Shockley が実証した最初のトランジスタ。半導体革命の起点。Moore's law の前提となる微細化の物理基盤を作った', 'Physical AI 全層の計算基盤の起点', 'phai_mat', 'Semiconductor', 1947, 1948, 'system', 4, '["John Bardeen","Walter Brattain","William Shockley"]', '["Bardeen & Brattain (1948) Physical Review 74:230"]', '["Bell Labs"]', '半導体,トランジスタ', 'semiconductor,transistor', NULL, NULL, 'active', 'primary', 95, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0002', 'Moore''s law', 'Moore''s Law', 'Moore''s Law', '1965年 Gordon Moore がIC上のトランジスタ数が約2年で倍化すると予測した経験則。50年以上維持され、半導体ロードマップの基本軸となった', 'Physical AI の計算能力曲線の歴史的トレンド', 'phai_mat', 'Semiconductor', 1965, NULL, 'theory', 1, '["Gordon Moore"]', '["Moore (1965) Electronics 38(8):114"]', '["Intel","Fairchild"]', 'ムーアの法則,半導体ロードマップ', 'Moore law,scaling', NULL, NULL, 'active', 'primary', 95, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0003', 'FinFET', 'FinFET (3D Transistor)', 'FinFET', '2011年 Intel 22nm世代で量産化された3次元構造トランジスタ。平面型MOSFETのスケーリング限界を突破し、20nm以下世代を可能にした', 'エッジAI推論用低電力チップの物理基盤', 'phai_mat', 'Semiconductor', 2011, 2022, 'system', 4, '["Chenming Hu"]', '["Hisamoto et al. (1989) IEDM"]', '["Intel","TSMC","Samsung"]', 'FinFET,3次元トランジスタ', 'FinFET,3D transistor', NULL, NULL, 'active', 'primary', 90, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0004', 'GAA-FET (Gate-All-Around)', 'Gate-All-Around FET', 'GAAFET', '2022年 Samsung SF3 / 2024年 TSMC N2 で量産化されたナノシート構造トランジスタ。FinFETの後継として3nm以下世代を担う', 'Physical AI 用エッジ推論SoCの2025-2035年世代基盤', 'phai_mat', 'Semiconductor', 2022, NULL, 'system', 4, '[]', '["Samsung 3nm GAA announcement 2022"]', '["Samsung","TSMC","Intel","imec"]', 'GAA,ナノシート', 'gate all around,nanosheet', NULL, NULL, 'active', 'primary', 85, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0005', '3次元積層DRAM (HBM)', 'High Bandwidth Memory (HBM)', 'HBM', '2013年 SK hynix が量産化した3次元積層メモリ。HBM3E は2024年に GPU 1基あたり 192GB 級を実現。LLM・基盤モデル推論の前提条件', 'Physical AI の基盤モデル推論レイヤを物理的に支える', 'phai_mat', 'Semiconductor', 2013, NULL, 'system', 4, '[]', '["JEDEC HBM JESD235"]', '["SK hynix","Samsung","Micron","NVIDIA"]', 'HBM,3D積層メモリ', 'HBM,3D memory', NULL, NULL, 'active', 'primary', 90, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0006', 'NVIDIA H100/B200', 'NVIDIA H100/B200 GPU', 'H100,B200', '2022年 H100 (Hopper) / 2024年 B200 (Blackwell) は LLM 訓練・推論の事実上の標準。Physical AI のクラウド推論基盤の中核', 'Physical AI 学習・推論のグローバル計算基盤', 'phai_mat', 'Semiconductor', 2022, NULL, 'system', 4, '["Bill Dally"]', '["NVIDIA Hopper whitepaper 2022","Blackwell whitepaper 2024"]', '["NVIDIA"]', 'GPU,H100,B200', 'GPU,H100,B200', NULL, NULL, 'active', 'primary', 90, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0007', 'NPU / エッジAIチップ', 'Neural Processing Unit (Edge)', 'NPU', 'Google Edge TPU (2018), NVIDIA Jetson Orin (2022), Qualcomm Hexagon NPU (2023) など、ロボット搭載用の低電力推論アクセラレータ', 'Physical AI のオンボード推論の中核', 'phai_mat', 'Semiconductor', 2018, NULL, 'system', 4, '[]', '["Google Coral docs","NVIDIA Jetson docs"]', '["Google","NVIDIA","Qualcomm","Apple"]', 'NPU,エッジAI', 'NPU,edge AI', NULL, NULL, 'active', 'primary', 85, NULL, NULL);

-- バッテリー系譜
INSERT INTO phai_concept VALUES ('phai_mat_0008', 'リチウムイオン電池', 'Lithium-ion Battery', 'Li-ion', '1980-1991年 Whittingham/Goodenough/Yoshino が確立し Sony が18650セルとして商用化。2019年ノーベル化学賞。Physical AI 移動体の標準動力源', 'ヒューマノイド・ドローン・配送ロボの稼働時間決定要因', 'phai_mat', 'Battery', 1991, NULL, 'system', 4, '["John Goodenough","M. Stanley Whittingham","Akira Yoshino"]', '["Yoshino (2012) Angew Chem 51:5798"]', '["Sony","CATL","LG Energy Solution","Panasonic","BYD"]', 'リチウムイオン電池,Li-ion', 'lithium-ion,Li-ion battery', NULL, NULL, 'active', 'primary', 95, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0009', 'NMC811高ニッケル正極', 'NMC811 Cathode', 'NMC811', 'ニッケル80%含有の三元系正極材料。270-300 Wh/kg のセル密度を実現し2020年代前半の EV / ロボット動力の主流に', 'ヒューマノイド連続稼働時間2-4時間を可能にした材料', 'phai_mat', 'Battery', 2019, NULL, 'method', 4, '[]', '["Manthiram (2020) Nature Comm 11:1550"]', '["LG Energy Solution","CATL","Tesla","Panasonic"]', 'NMC811,高ニッケル正極', 'NMC811,high-nickel cathode', NULL, NULL, 'active', 'primary', 85, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0010', '全固体電池（硫化物系）', 'Sulfide-based All-Solid-State Battery', 'ASSB', '硫化物固体電解質を用いる次世代電池。Toyota が 2027-2028 年商用化を公式宣言。理論密度 500 Wh/kg+、安全性・急速充電性で液系を凌駕', 'Physical AI のヒューマノイド連続稼働 24 時間化の鍵', 'phai_mat', 'Battery', 2014, NULL, 'system', 2, '["Ryoji Kanno"]', '["Kato et al. (2016) Nature Energy 1:16030"]', '["Toyota","Samsung SDI","Idemitsu","東京工業大学"]', '全固体電池,硫化物', 'all-solid-state,sulfide electrolyte', NULL, NULL, 'active', 'primary', 80, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0011', '全固体電池（酸化物系）', 'Oxide-based All-Solid-State Battery', 'Oxide ASSB', 'QuantumScape 等が開発する LLZO 系セラミック電解質型固体電池。室温作動・サイクル寿命で硫化物系を補完', 'Physical AI 移動体の安全性・寿命を質的に高める', 'phai_mat', 'Battery', 2010, NULL, 'system', 2, '["Werner Weppner"]', '["Murugan et al. (2007) Angew Chem 46:7778"]', '["QuantumScape","Volkswagen","Murata"]', '全固体電池,酸化物,LLZO', 'oxide solid electrolyte,LLZO', NULL, NULL, 'active', 'primary', 80, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0012', 'リチウム硫黄電池', 'Lithium-Sulfur Battery', 'Li-S', '理論密度 2600 Wh/kg のポストLi-ion 候補。Lyten が 2023 年 Stellantis と航空・自動車向けで提携。寿命・多硫化物シャトル問題が課題', 'Physical AI のドローン・配送ロボの長距離化', 'phai_mat', 'Battery', 2010, NULL, 'system', 2, '["Linda Nazar"]', '["Manthiram et al. (2014) Chem Rev 114:11751"]', '["Lyten","Oxis Energy","Sion Power"]', 'リチウム硫黄,Li-S', 'lithium-sulfur,Li-S', NULL, NULL, 'active', 'primary', 75, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0013', 'ナトリウムイオン電池', 'Sodium-ion Battery', 'Na-ion', 'CATL が 2023 年に量産化発表、BYD が 2024 年 EV 搭載。リチウム資源制約の代替として定置・低速移動体向け', 'Physical AI のローエンド大量普及（清掃ロボ等）の経済性確保', 'phai_mat', 'Battery', 2023, NULL, 'system', 4, '[]', '["Hwang et al. (2017) Chem Soc Rev 46:3529"]', '["CATL","BYD","Northvolt","HiNa"]', 'ナトリウムイオン,Na-ion', 'sodium-ion,Na-ion', NULL, NULL, 'active', 'primary', 85, NULL, NULL);

-- 太陽光系譜
INSERT INTO phai_concept VALUES ('phai_mat_0014', '結晶シリコン太陽電池', 'Crystalline Silicon (c-Si) Solar Cell', 'c-Si PV', '1954年 Bell Labs Chapin/Fuller/Pearson が実証。Swanson の法則で 70 年間価格低下、2024 年に 0.10-0.13 USD/W、世界 PV 出荷の 95%+', 'Physical AI 時代のエネルギー基盤の中核', 'phai_mat', 'Solar PV', 1954, NULL, 'system', 4, '["Daryl Chapin","Calvin Fuller","Gerald Pearson"]', '["Chapin et al. (1954) J Appl Phys 25:676"]', '["Bell Labs","LONGi","Jinko","Trina","Canadian Solar"]', '結晶シリコン,c-Si,太陽電池', 'crystalline silicon,c-Si,PV', NULL, NULL, 'active', 'primary', 95, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0015', 'ペロブスカイト太陽電池', 'Perovskite Solar Cell', 'PSC', '2009年 宮坂力 が報告（JACS 131:6050）以降15年で研究室効率 26.7% に到達。c-Si タンデムで 33%+。低温・印刷プロセスで建材一体型に強み', 'Physical AI のエッジデバイス自給電力源', 'phai_mat', 'Solar PV', 2009, NULL, 'system', 3, '["宮坂力","Henry Snaith","NREL"]', '["Kojima et al. (2009) JACS 131:6050"]', '["桐蔭横浜大学","Oxford PV","Saule Technologies","LONGi"]', 'ペロブスカイト,PSC', 'perovskite,PSC', NULL, NULL, 'active', 'primary', 90, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0016', 'タンデム太陽電池', 'Perovskite-Silicon Tandem Solar Cell', 'Tandem PV', '2024年 HZB / LONGi / Oxford PV が 33-34% 効率を達成し c-Si 単体限界 29.4% を突破。商用化は 2025-2027 年予定', 'Physical AI 普及時代のエネルギー供給上限引き上げ', 'phai_mat', 'Solar PV', 2017, NULL, 'system', 3, '["Stefaan De Wolf","Henry Snaith"]', '["Al-Ashouri et al. (2020) Science 370:1300"]', '["HZB","Oxford PV","LONGi","KAUST"]', 'タンデム太陽電池,ペロブスカイトシリコン', 'tandem,perovskite-silicon', NULL, NULL, 'active', 'primary', 85, NULL, NULL);

-- 核分裂・核融合系譜
INSERT INTO phai_concept VALUES ('phai_mat_0017', 'SMR (Small Modular Reactor)', 'Small Modular Reactor', 'SMR', '50-300MWe 級の小型モジュール式原子炉。BWRX-300 (GE-Hitachi), VOYGR (NuScale), Natrium (TerraPower) が 2029-2030 稼働予定。データセンター電源として注目', 'AI データセンター × 原子力の構造的合流', 'phai_mat', 'Nuclear Fission', 2010, NULL, 'system', 2, '["Bill Gates (TerraPower)","Christer Dahlgren"]', '["NRC NuScale design certification (2023)"]', '["NuScale","GE-Hitachi","TerraPower","Rolls-Royce","X-energy"]', 'SMR,小型モジュール炉', 'SMR,small modular reactor', NULL, NULL, 'active', 'primary', 85, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0018', 'トカマク型核融合', 'Tokamak Fusion', 'Tokamak', 'ITER (フランス, 2025-2026 First Plasma 予定) と CFS SPARC (MIT スピンアウト, 2026-2027 稼働予定) が代表。Q>1 実証は 2030 年代に商用化を視野', 'Physical AI 普及時代のエネルギー希少性解消の本命', 'phai_mat', 'Nuclear Fusion', 1985, NULL, 'system', 2, '["Lev Artsimovich","Dennis Whyte"]', '["ITER Research Plan 2018","Sorbom et al. (2015) FED 100:378"]', '["ITER","CFS","Tokamak Energy","JT-60SA"]', 'トカマク,核融合', 'tokamak,fusion', NULL, NULL, 'active', 'primary', 85, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0019', '慣性閉じ込め核融合', 'Inertial Confinement Fusion', 'ICF', '2022年12月 NIF (LLNL) で Q=1.5 のエネルギー利得実証（点火）。商用化には多パルス・量産レーザー駆動が必要', 'エネルギー転換の研究的マイルストーン', 'phai_mat', 'Nuclear Fusion', 1972, NULL, 'system', 2, '["John Nuckolls"]', '["Abu-Shawareb et al. (2024) Phys Rev Lett 132:065102"]', '["LLNL NIF","Focused Energy","Marvel Fusion"]', '慣性閉じ込め核融合,ICF', 'inertial confinement,ICF,NIF', NULL, NULL, 'active', 'primary', 85, NULL, NULL);

-- AI設計材料系譜
INSERT INTO phai_concept VALUES ('phai_mat_0020', 'GNoME (DeepMind)', 'Graph Networks for Materials Exploration', 'GNoME', '2023年 DeepMind がグラフニューラルネットワークで220万件の新規結晶構造候補を生成、38万件がDFTで安定。従来の材料発見を10倍以上加速', 'AI×素材によるPhysical AI 物理基盤の指数加速の起点', 'phai_mat', 'AI Materials Discovery', 2023, NULL, 'method', 2, '["Amil Merchant","Ekin Dogus Cubuk"]', '["Merchant et al. (2023) Nature 624:80"]', '["DeepMind"]', 'GNoME,AI材料探索', 'GNoME,AI materials discovery', NULL, NULL, 'active', 'primary', 90, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0021', 'A-Lab (LBNL)', 'Autonomous Laboratory for Materials', 'A-Lab', 'Lawrence Berkeley National Lab の自律実験ロボット。GNoME 候補から17日間で41種の新規材料を合成成功。AI×ロボの代表事例', 'Physical AI 自身が材料発見ループに参加する自己加速の実例', 'phai_mat', 'AI Materials Discovery', 2023, NULL, 'system', 3, '["Gerbrand Ceder","Yan Zeng"]', '["Szymanski et al. (2023) Nature 624:86"]', '["LBNL","UC Berkeley"]', 'A-Lab,自律実験室,材料発見', 'A-Lab,autonomous lab,materials', NULL, NULL, 'active', 'primary', 90, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0022', 'Materials Project', 'Materials Project Database', 'MP', '2011年 LBNL Kristin Persson らが立ち上げた DFT 物性データベース。15 万化合物超を収載し、GNoME / A-Lab の前提基盤', '材料発見の知識共有基盤', 'phai_mat', 'AI Materials Discovery', 2011, NULL, 'dataset', 4, '["Kristin Persson","Anubhav Jain"]', '["Jain et al. (2013) APL Mater 1:011002"]', '["LBNL","MIT"]', 'Materials Project,材料データベース', 'Materials Project,DFT database', NULL, NULL, 'active', 'primary', 95, NULL, NULL);

-- 量子計算系譜
INSERT INTO phai_concept VALUES ('phai_mat_0023', 'Feynman量子シミュレーション提案', 'Feynman Quantum Simulation Proposal', 'Feynman Lectures', '1982年 Richard Feynman が量子系のシミュレーションには量子計算機が必要と提唱（Int J Theor Phys 21:467）。量子計算の理論的起点', 'Physical AI の材料設計を加速する将来計算基盤の起源', 'phai_mat', 'Quantum Computing', 1982, NULL, 'theory', 1, '["Richard Feynman"]', '["Feynman (1982) Int J Theor Phys 21:467"]', '["Caltech"]', 'ファインマン,量子シミュレーション', 'Feynman,quantum simulation', NULL, NULL, 'active', 'primary', 95, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0024', '量子超越 (Google Sycamore)', 'Quantum Supremacy', 'Sycamore', '2019年 Google が 53qubit の Sycamore プロセッサで古典計算機では現実的時間で解けないタスクを実証（Nature 574:505）', '量子計算の実用化への分水嶺', 'phai_mat', 'Quantum Computing', 2019, NULL, 'breakthrough', 3, '["John Martinis","Sergio Boixo"]', '["Arute et al. (2019) Nature 574:505"]', '["Google Quantum AI"]', '量子超越,Sycamore', 'quantum supremacy,Sycamore', NULL, NULL, 'active', 'primary', 90, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0025', 'フォールトトレラント量子計算', 'Fault-Tolerant Quantum Computing', 'FTQC', '2024年 Google Willow が表面符号エラー訂正で論理量子ビット数増加に伴い誤り率が指数的に低下する閾値を突破（Nature 638:920, 2025）', 'Physical AI 用材料探索・最適化の指数加速候補', 'phai_mat', 'Quantum Computing', 1995, NULL, 'method', 2, '["Peter Shor","John Preskill","Hartmut Neven"]', '["Shor (1995) PRA 52:R2493","Acharya et al. (2025) Nature 638:920"]', '["Google Quantum AI","IBM","IonQ","Quantinuum","PsiQuantum"]', 'FTQC,フォールトトレラント', 'fault-tolerant,FTQC,surface code', NULL, NULL, 'active', 'primary', 85, NULL, NULL);

-- スマート材料・センサ
INSERT INTO phai_concept VALUES ('phai_mat_0026', '形状記憶合金アクチュエータ', 'Shape Memory Alloy Actuator', 'SMA', 'NiTi合金 (Nitinol) が温度変化で形状回復。コンパクト・静音アクチュエータとして医療ロボ・微小ロボに採用', 'Physical AI のソフト・小型アクチュエータ系統', 'phai_mat', 'Smart Materials', 1995, NULL, 'system', 4, '["William Buehler"]', '["Mohd Jani et al. (2014) Mater Des 56:1078"]', '["NDC","SAES Smart Materials"]', '形状記憶合金,SMA', 'shape memory alloy,SMA', NULL, NULL, 'active', 'primary', 85, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0027', '液晶エラストマー (LCE)', 'Liquid Crystal Elastomer', 'LCE', '光・熱で大変形する高分子素材。2017年以降ソフトロボ・人工筋肉素材として急成長。Harvard Wyss / Stuttgart Max Planck が先行', 'Physical AI のソフトロボティクス物質基盤', 'phai_mat', 'Smart Materials', 2017, NULL, 'system', 3, '["Eugene Terentjev","Mark Warner"]', '["Ware et al. (2015) Science 347:982"]', '["Harvard Wyss","MPI Stuttgart","CU Boulder"]', '液晶エラストマー,LCE,ソフト', 'liquid crystal elastomer,LCE', NULL, NULL, 'active', 'primary', 85, NULL, NULL);

INSERT INTO phai_concept VALUES ('phai_mat_0028', '宇宙太陽光発電 (SBSP)', 'Space-Based Solar Power', 'SBSP', '軌道上の太陽光パネルで発電しマイクロ波で地上伝送。Caltech SSPP が 2023 年 MAPLE 軌道伝送実証成功。商用は 2050 年代見込み', 'Physical AI 普及時代のエネルギー上限突破候補', 'phai_mat', 'Energy Generation', 1968, NULL, 'system', 2, '["Peter Glaser","Sergio Pellegrino"]', '["Glaser (1968) Science 162:857","Caltech SSPP MAPLE 2023"]', '["Caltech","JAXA","ESA","Northrop Grumman"]', '宇宙太陽光,SBSP', 'space-based solar,SBSP', NULL, NULL, 'active', 'primary', 75, NULL, NULL);
```

### 5.3 phai_milestones 追加（5件）

```sql
INSERT INTO phai_milestones VALUES ('mile_mat_0001', 'AI設計材料の自律発見ループ確立', 2023, 'breakthrough', 'GNoME (DeepMind, Nature 624:80) と A-Lab (LBNL, Nature 624:86) が同時掲載され、AI生成→DFT検証→ロボット合成の閉ループが17日間で41種を実証', 'stream_mat,stream_sim,stream_fm', 'phai_mat_0020,phai_mat_0021,phai_mat_0022', NULL, 9, NULL);

INSERT INTO phai_milestones VALUES ('mile_mat_0002', '全固体電池の量産フェーズ突入', 2024, 'commercialization', 'Toyota 2027-2028量産宣言、Samsung SDI S-Line 稼働、QuantumScape Volkswagen 提携進展。Physical AI ヒューマノイドの稼働時間ボトルネック解消が視野に', 'stream_mat,stream_hw,stream_hum', 'phai_mat_0010,phai_mat_0011', NULL, 9, NULL);

INSERT INTO phai_milestones VALUES ('mile_mat_0003', '核融合エネルギー利得点火 (NIF)', 2022, 'breakthrough', '2022年12月 LLNL NIF が慣性閉じ込め核融合で Q=1.5 を達成。商用核融合への科学的閾値突破', 'stream_mat', 'phai_mat_0019', NULL, 8, NULL);

INSERT INTO phai_milestones VALUES ('mile_mat_0004', 'AI×原子力契約の合流', 2024, 'commercialization', 'Microsoft Three Mile Island 再稼働 (Constellation 20年PPA), Amazon Talen Energy 隣接, Google Kairos Power 小型炉契約 (500MW)。AIとエネルギー転換が事業契約レベルで結合', 'stream_mat,stream_fm', 'phai_mat_0017', NULL, 9, NULL);

INSERT INTO phai_milestones VALUES ('mile_mat_0005', 'フォールトトレラント量子計算閾値突破', 2024, 'breakthrough', 'Google Willow が表面符号エラー訂正で論理量子ビット数増加に伴う指数的エラー率低下を実証。Physical AI 用材料設計の量子加速が現実的視野に', 'stream_mat,stream_sim', 'phai_mat_0025', NULL, 8, NULL);
```

### 5.4 phai_bottlenecks 追加（2件）

```sql
INSERT INTO phai_bottlenecks VALUES ('btl_mat_0001', 'バッテリーエネルギー密度の物理限界', 'リチウムイオン現行密度 270-300 Wh/kg ではヒューマノイド連続稼働2-4時間が限界。固体電池 500 Wh/kg 級の量産化が2028-2030年に間に合わなければ Physical AI 普及が3-5年停滞', 'critical', 'phase2,phase3,phase4', 12, 'high', 0.2, 'phai_mat_0008,phai_mat_0010,phai_mat_0011', NULL);

INSERT INTO phai_bottlenecks VALUES ('btl_mat_0002', 'データセンター電力供給制約', 'IEA推計でデータセンター世界消費は2022年460TWh→2026年最大1050TWhへ倍増。米PJMで2024年容量市場価格9倍。送電網増強の8-12年計画スパンとAI需要急成長の不整合', 'critical', 'phase2,phase3,phase4', 18, 'high', 0.15, 'phai_mat_0017,phai_mat_0018', NULL);
```

---

## 6. 実証データ — 引用と数値の出典

| 項目 | 数値 | 出典 |
|------|------|------|
| Moore's law 起源 | 1965年 | Moore G.E. (1965) Electronics 38(8):114 |
| Li-ion商用化 | 1991年 Sony 18650 | Yoshino A. (2012) Angew Chem 51:5798 |
| Li-ion 2024年密度 | 270-300 Wh/kg (NMC811) | BNEF Battery Price Survey 2024 |
| c-Si価格 1976→2024 | 106 → 0.10-0.13 USD/W | IEA PVPS Trends 2024 / BNEF |
| ペロブスカイト効率 | 26.7% (2024研究室) | NREL Best Research-Cell Efficiency Chart 2024 |
| GNoME材料候補 | 220万→38万安定 | Merchant et al. (2023) Nature 624:80 |
| A-Lab 合成成功 | 17日間で41種 | Szymanski et al. (2023) Nature 624:86 |
| NIF Q値 | Q=1.5 (2022年12月) | Abu-Shawareb et al. (2024) Phys Rev Lett 132:065102 |
| Google量子超越 | 53qubit (2019) | Arute et al. (2019) Nature 574:505 |
| Google Willow FTQC | 表面符号閾値突破 | Acharya et al. (2025) Nature 638:920 |
| DC電力消費 | 2022:460 → 2026:1050 TWh | IEA Electricity 2024 |
| 米DC比率 | 2024年 約4.5% | EIA / LBNL 2024 reports |
| Microsoft TMI再稼働 | 2024年9月 20年PPA | Constellation Energy press release 2024-09-20 |
| Amazon Talen契約 | 2024年3月 | Talen Energy 8-K filing 2024-03 |
| Google Kairos契約 | 500MW 2030-2035 | Google + Kairos Power 共同発表 2024-10 |
| Helion Microsoft契約 | 50MW 2028年 | Helion Energy press release 2023-05 |
| 宇宙太陽光MAPLE実証 | 2023年 軌道伝送成功 | Caltech SSPP MAPLE mission report 2023 |

---

## まとめ — Stream 4 を独立系統として PHAI-DB に加える根拠

Physical AI のロードマップは、計算アルゴリズム（Stream 2/3/4: Control/RL/FM）とハードウェア機構（Stream 1: HW）、データ生成基盤（Stream 5: Sim）の合流として描かれてきた。しかし2023-2026年に起きた4つの臨界事象 — AI 設計材料の自律発見ループ確立、固体電池量産フェーズ突入、核融合点火、AI×原子力契約の合流 — は、Materials/Energy を独立した第6系統（stream_mat）として扱う必要性を示している。

特に重要なのは、Stream 4 が他の5系統と異なり **AIを物理的に支える基盤と、AIによって加速される対象の両方を兼ねる二重性** を持つことである。GNoME / A-Lab は AI が材料発見を加速する例、固体電池 / 核融合 / SMR は材料・エネルギーが AI を支える例だが、これらが正のフィードバックループで結合する 2026-2040 年が Physical AI 普及の本質的な転換期となる。PHAI-DB は本提案の 35 件のレコード追加により、この合流ダイナミクスを明示的に分析できる構造を獲得する。
