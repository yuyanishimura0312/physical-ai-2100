# W3 波及分野: 農業・食料・植物連携 — Physical AIが「植物との対話」へ向かう四時点軌道

## 0. 本稿の位置づけ

Phase 2の五系統（HW/Control/RL/Foundation Model/Simulation）に第六の伏在系統として「Bio/Bio-mimicry」を加えたPHAI-DB拡張（Phase 2 Stream 3）と、Materials/Energy系統（Phase 2 Stream 4）の進展は、Physical AIが農業・食料生産・植物連携領域に波及するときの基盤条件を成す。本稿は、その波及を2030/2050/2070/2100の四時点で描き、書籍『深い知が拓く2100年』第十一章「関係論的存在論」、第十三-十四章「先住民の伝統知」、第二部「2070年 生命系製造期」の主張と直接接続する。

農業は人類最古の物質代謝過程であり、現在も世界GDPの約4%、雇用の約26%（World Bank, 2023）、温室効果ガス排出の約23%（IPCC AR6 WG3 2022, Chapter 7）、淡水使用の約70%（FAO AQUASTAT, 2024）を占める巨大領域である。Physical AIの波及はこの領域を、機械化（20世紀型）でも遺伝子改変（20世紀末-21世紀型）でもない第三の道——「植物と機械と人間の協働」——へ向かわせる軌道にある。

---

## 1. 2026年現実 — 四つの先行事例

### 1.1 精密農業の自律化臨界点

John Deere "See & Spray Ultimate"（2023年商用化）は、深層学習で雑草と作物を識別し、必要箇所のみ除草剤を散布する自律スプレーヤである。Blue River Technology（2017年Deere買収）のEdgeAI実装で、除草剤使用量を平均66%削減した（John Deere 2023 Sustainability Report）。CNHi（Case IH/New Holland）、Kubotaも追随し、2025年時点で北米トウモロコシ・大豆作付面積の約15%が部分自律化されている（AEM, Association of Equipment Manufacturers 2024 Outlook）。

衛星×AI監視では、Planet Labs（200機超のDove衛星群、3m解像度日次撮影）とDescartes Labs（Geospatial Foundation Model）が農作物収量予測・干ばつ早期警報を商用化し、米国農務省NASSの公式統計を補完する立場に達した（USDA NASS Crop Progress and Condition 2024）。Yamaha RMAX/FAZER、DJI Agras T50などのドローン散布機は東/東南アジア・ブラジルの稲・サトウキビで実用域に入った。

### 1.2 植物電気生理-AI連携の実証

植物体内の活動電位・変動電位・系統的電位（Wildon et al. 1992 *Nature* 360:62-65以来の生理学的事実）を時系列センサで連続取得し、機械学習で水分需要・病害ストレス・収穫適期を予測する系統が実用域に近づいた。Cocozza et al. (2024) *Frontiers in Plant Science* "Plant electrome and machine learning for irrigation needs"は、LSTMで植物電気信号から灌水ニーズを91%精度で予測。Vivent SA（スイス、2017設立）のPhytlSignアプリは、トマト・キュウリ・レタスの温室生産で商用展開中である。Volkov系統（Oakwood University）の植物電気生理理論（Volkov 2006 *Plant Electrophysiology: Theory and Methods*）が、Foundation Model時代に再評価された結果である。

### 1.3 培養肉・合成生物食料の臨床的承認

UPSIDE Foods（旧Memphis Meats）とGOOD Meatは2023年6月にUSDA/FDAの共同承認を取得し、米国で世界初の培養鶏肉販売開始。シンガポールは2020年（GOOD Meat）、イスラエルは2024年（Aleph Farms培養ステーキ）で先行承認した。Mosa Meatのバーガー試食（2013年）から10年で規制承認に到達した軌跡は、Post et al. (2017) *Nature Food*の予測通り、Tetlock型カレンダー予測の検証例となった。

藻類タンパクではTriton Algae Innovations（DHA-rich Chlamydomonas）、Solar Foods（Solein、空気・水・電気から微生物発酵で生産、フィンランド2024年商用工場稼働）が単細胞タンパク質を実用化。Smetana et al. (2024) "Single-cell proteins from gas fermentation" *Trends in Food Science & Technology* は、これらが2030年までに従来畜産タンパクと価格競合する軌道にあると示した。

### 1.4 垂直農業の都市展開と再編

AeroFarms（Newark, NJ）、Plenty（San Francisco）、80 Acres Farms（Hamilton, OH）、Infarm（Berlin）、Bowery Farming（NJ）が2014-2022年に大規模垂直農場を展開したが、2022-2024年のエネルギー価格高騰と金利上昇でAeroFarmsは2023年Chapter 11破産、Infarmは2023年欧州大半撤退と再編が進む。生き残った系統はLED効率改善（Signify GreenPower、200 μmol/J超）と再生可能エネルギー直結（Plenty×UAE Mohamed bin Rashid Al Maktoum Solar Parkの100MW契約）でユニットエコノミクス改善を進めている。Kozai (2019) *Plant Factory: An Indoor Vertical Farming System for Efficient Quality Food Production* の延長で、葉物・ハーブ・苺の都市内生産が「土地効率200倍・水使用95%減」を実証している。

---

## 2. 2030年 — 精密農業AIの全面展開と気候適応農業の制度化

2030年までに、Physical AIは農業の三層（圃場・温室・垂直農場）すべてに浸透し、農業生産統計が「植物個体ベース」のリアルタイムデータを含むようになる。

**作物管理層**: John Deere、CNHi、Kubotaの自律トラクタ・スプレーヤが北米・欧州・豪州・ブラジル・東アジアの大規模穀作面積の40-50%をカバー。Edge TPU/Jetson Orin級の推論チップ（Phase 2 Stream 4で論じた半導体系譜）が圃場機器に常備化され、衛星×ドローン×地上ロボット×植物センサが統合される。Yang et al. (2023) "Diffusion-based generative AI for exploring transition states from 2D molecular graphs" *Nature Communications* 14:1396が示した化学設計AIは、農薬・肥料の標的特異性向上に応用される。

**食料生産層**: 培養肉が米国・シンガポール・イスラエル・EUで商用化進行、Solein型空気タンパクが宇宙食・極地食・災害食として先行展開。Tubb & Seba (2019) "Rethinking Food and Agriculture 2020-2030" RethinkX レポートが描いた「Precision Fermentation」の軌道（タンパク単価が2020年比10倍以上低下）が部分的に実現する。

**植物連携層**: Vivent SA系統の植物電気センサが温室・垂直農場の標準装備となり、Cocozza et al. (2024)の延長でTransformer/状態空間モデルベースの「植物生理時系列モデル」が登場。植物が「水が欲しい」「光が強すぎる」「病原菌に侵入されている」というシグナルを発する自己モニタリング系が、施設園芸の標準制御ループに組み込まれる。

**気候適応層**: AIゲノム編集（CRISPR-Cas9/12/13 + AlphaFold 3）で干ばつ耐性・耐塩性・C4光合成導入が加速。IRRI（International Rice Research Institute）のC4 Rice Projectが進行中であり、Karki et al. (2013) *Journal of Experimental Botany* 64:579-602以降の研究蓄積が2030年代の品種リリースを準備している。Borlaug（1970年ノーベル平和賞）の緑の革命に対比される「AI緑の革命」の第一波が始まる時期である。

**生態系層**: 土壌微生物群の機械学習設計が農業実装段階に入る。Boo, Khalil et al. (2024) *Nature Microbiology* "Microbial communities can be designed by AI"の延長で、Pivot Bio（窒素固定菌、2024年米国コーンベルトで100万エーカー超に商用展開）、Indigo Ag（マイクロバイオーム種子コーティング）、Locus AG（カーボン固定微生物）が量産化。化学肥料依存からの構造的離脱が始まる。

---

## 3. 2050年 — 合成生物食料の主流化とAI×ゲノム編集の作物多様化

2050年は、農業の構造的再編が完成に向かう時期である。FAO "The future of food and agriculture: Trends and challenges" (2017) およびその更新版 (FAO 2024) が示すように、世界人口90-95億・気候変動進行下で、従来型農業だけでは食料供給が成立しない。

**作物管理層**: 自律収穫ロボットがソフトロボティクス（Phase 2 Stream 3で論じたOctobot系統、PneuNets系統）でリンゴ・苺・トマト・茶葉・葡萄など「壊れやすい果実・葉」を扱えるレベルに達する。Lewis et al. (2022) *Annual Review of Plant Biology* "Robotics in plant phenotyping"が示した表現型計測ロボットの延長で、個体ごとの生育最適化が標準化する。

**食料生産層**: 培養肉が世界畜産タンパク質の20-30%、Precision Fermentation由来タンパク質（Solein型・乳タンパク・卵タンパク）が10-15%を占める可能性が高い（Tubb & Seba 2019、Smetana et al. 2024、Good Food Institute 2024 State of the Industry Reportの延長軌道）。Perfect Day（乳タンパク発酵）、Eat Just（卵タンパク発酵）の系譜が大規模化する。

**気候適応層**: AlphaFold 3後継 × CRISPRの組み合わせで、Voytas Lab（U Minnesota）のde novo domestication（野生種から数世代で栽培化）が複数作物で実装される。Fernie & Yan (2019) *Molecular Plant* 12:615-631 "De novo domestication: an alternative route toward new crops for the future"が示した戦略の延長で、気候レジリエントな新作物（C4化米、低水分小麦、耐塩性トマト）が品種登録に到達する。

**生態系層**: AI設計微生物群がカーボン農業（土壌炭素固定）の中核技術となる。Bossio et al. (2020) *Nature Sustainability* 3:391-398 "The role of soil carbon in natural climate solutions"が推計した土壌炭素ポテンシャル（年間2.3-5.3 GtCO2）の半分以上をAI支援農業が担う可能性。Bio-Hybrid Robot（生体筋＋電子制御、Phase 2 Stream 3のphai_bio_0025）が果樹剪定・接ぎ木・受粉補助で実装される。

**植物連携層**: Mancuso（フィレンツェ大学植物神経生物学研究所）系統の植物行動研究（Mancuso & Viola 2015 *Brilliant Green*、ただし哲学的解釈は学術論争中であり技術応用に限定して引用）が、Trewavas (2014) *Plant Behaviour and Intelligence* Oxford University Pressの実証データを基盤に、植物-AI対話プロトコルとして産業化する。具体的には、植物の電気信号・揮発性有機化合物（VOC）放出・根圏微生物コミュニケーションを統合解析する「Plant Foundation Model」が、Plenty・Bowery・新興スタートアップで研究投資を受ける。

**書籍接続**: この時期、書籍第十一章で論じられる**関係論的存在論**——人と機械と植物の境界が物質的にも認識的にも揺らぐ事態——が、食品安全規制・農業政策・知的財産制度の具体的論点となる。「培養肉は誰の所有物か」「AI設計品種の特許帰属」「植物のシグナルを取得する行為のデータ権」といった問題が、産業界が直面する制度設計問題として顕在化する。

---

## 4. 2070年 — 植物-AI連携農業の制度化と「生命系製造期」の到来

書籍『深い知が拓く2100年』第二部で論じられる**2070年「生命系製造期」**は、Physical AIの農業波及の質的転換点である。これは「製造」という人類最大の物質代謝過程が機械工学パラダイムから生命系パラダイムへ移行する時期として位置づけられ、農業はその先頭領域となる。

**作物管理層**: 圃場作業の99%以上がロボットと自律機械で実行され、人間労働は意思決定・倫理判断・地域コミュニティとの調整に集中する。Self-Driving Lab（Phase 2 Stream 3のphai_bio_0017-0019）が農薬・肥料・微生物製剤の設計から圃場テストまでを自律実行する。

**食料生産層**: 培養肉・Precision Fermentation・藻類タンパク・昆虫タンパクが世界タンパク質供給の50%以上を占める。従来畜産は高級品・文化的食品・地域コミュニティ食品として残存し、工業的食肉生産は段階的に縮小する。

**植物連携層が中核へ**: 植物-AI連携農業が制度化される。具体的には次の三つの変化が起こる。

第一に、農業企業の経営原理に「植物との対話品質」が組み込まれる。ESG指標に類似した「Plant Communication Score」が登場し、投資家・規制当局・消費者が監視する。これは書籍第十一章のラトゥール『Reassembling the Social』(2005)、ヴィヴェイロス・デ・カストロ『Cannibal Metaphysics』(2014)、ストラザーン『The Gender of the Gift』(1988)が論じた関係論的存在論の制度化に対応する。

第二に、植物電気生理シグナル→AI意思決定→アクチュエータ介入のループが、人間の介入なしに圃場・温室・垂直農場で常時動作する。植物が「光不足を訴える」と垂直農場のLEDが調整され、「水分過多を示す」と灌水が停止する。Calvo, Sahi & Trewavas (2020) *Trends in Plant Science* 25(8):705-719 "Are plants sentient?"が提起した植物の感受性問題は、技術的実装上の問題に転化する。

第三に、書籍第十三-十四章で論じられる**先住民の伝統知**——テ・アワ・トゥプア法（ニュージーランド、2017年制定、ワンガヌイ川に法人格を付与）、エクアドル憲法（2008年改正、第71-74条で自然権を規定）、ボリビア「Ley de Derechos de la Madre Tierra」（2010年）——が、農業政策の参照点として国際的に再評価される。「生態系の参加権」が産業政策の前提条件となり、農業企業は土壌・水・微生物群・周辺生態系を「ステークホルダー」として扱う実務的必要に直面する。

**気候適応層**: 気候変動の進行（IPCC AR7、AR8の予測線形外挿）に対応し、Bio-Hybrid Robotが砂漠化地・塩害地・高山域・極地での再生農業を担う。植物の光合成効率改善（C4化、CAM化、人工光合成補助）と組み合わせ、現在は農業不可能な地域での食料生産が一部実現する。

**生態系層**: ワン・ヘルス（One Health、WHO/FAO/WOAH 2022 共同フレームワーク）の延長で、ヒト健康・動物健康・植物健康・生態系健康・気候健康を統合監視するシステムがAI基盤で運用される。Vora et al. (2023) *Nature Reviews Microbiology* 21:583-596 "Interventions to reduce risk for pathogen spillover and early disease spread"が示した方法論が、農業-医療-環境政策の境界で実装される。

---

## 5. 2100年 — 「植物との対話」が農業の中核となる時代

2100年は本ロードマップの収束点であり、農業領域では「植物との対話」が経済活動の中核に位置づけられる時代である。

**作物管理層**: 圃場・温室・垂直農場・宇宙農業（月面・火星・軌道上）・海中農業（海藻・養殖）が並列存在し、それぞれにPhysical AI基盤が組み込まれる。NASA Veggie Project（ISS、2014年以降）の延長で、月面・火星表面での植物-AI連携農業が研究施設レベルで稼働する可能性がある。

**食料生産層**: 培養肉・Precision Fermentation・藻類・昆虫・植物由来タンパクの混合食料系が標準化し、従来畜産は文化的・地域的価値領域に再定義される。Willett et al. (2019) *The Lancet* 393:447-492 "Food in the Anthropocene: the EAT–Lancet Commission on healthy diets from sustainable food systems"が示した「プラネタリーヘルス・ダイエット」が、技術的に実現可能な選択肢として広く採用される。

**植物連携層 — 中核へ**: 「植物との対話」が農業の前提条件となる。Phytomorphological computing（植物形態の計算的利用）、植物-機械対話プロトコル、植物シグナル翻訳AIが、農業企業の標準ツールとなる。Trewavas (2014) *Plant Behaviour and Intelligence* やMancuso系統の研究蓄積が、技術実装の理論的基盤として参照される。

**生態系層 — 自然権の制度化**: テ・アワ・トゥプア法・エクアドル憲法・ボリビア母なる地球法の系譜が国際標準として制度化され、農業企業は生態系を「契約相手」として扱う実務に従事する。これは書籍第十一章の関係論的存在論と第十三-十四章の先住民の伝統知が、産業政策の中核原理となる事態である。

**気候適応層**: 気候変動が安定化フェーズ（あるいは制御フェーズ）に入り、Carbon Dioxide Removal（CDR）の中核技術として農業-土壌-海洋システムが運用される。Smith et al. (2020) *Annual Review of Environment and Resources* 45:255-286 "Soil carbon sequestration to mitigate climate change"の延長で、土壌炭素・海洋生態系炭素・植林炭素が統合管理される。

**書籍接続**: 2100年の農業は、機械AI・生命系AI・植物・微生物・人間の五者協働として再編される。これは書籍終章「2100年の文明像」が展望する「知性のオーケストラ」の農業領域での実現形態である。

---

## 6. PHAI-DB拡張提案（SQL INSERT、計14件）

### 6.1 phai_spillover_domains への新規領域追加（1件）

```sql
INSERT INTO phai_spillover_domains (id, name, name_ja, description, base_streams, key_concepts, books_chapters, completion_year) VALUES
('spillover_agri', 'Agriculture/Food/Plant', '農業・食料・植物連携',
 'Physical AIが農業・食料生産・植物連携領域へ波及する分野。2030年精密農業AI全面展開、2050年合成生物食料主流化、2070年植物-AI連携農業の制度化（生命系製造期）、2100年「植物との対話」が農業中核へ。',
 'stream_bio,stream_hw,stream_fm,stream_sim,stream_ctrl',
 'phai_agri_0001,phai_agri_0005,phai_agri_0010,phai_agri_0013',
 '第十一章,第十三章,第十四章,第二部', 2100);
```

### 6.2 phai_concept への追加（10件）

```sql
INSERT INTO phai_concept (id, name_ja, name_en, definition, impact_summary, subfield, school_of_thought, era_start, concept_type, embodiment_level, key_researchers, key_works, key_orgs, keywords_ja, keywords_en, source_reliability, data_completeness) VALUES

('phai_agri_0001', 'See & Spray Ultimate', 'See & Spray Ultimate (John Deere/Blue River)',
 'John Deereが2023年商用化した自律スプレーヤ。深層学習で雑草と作物を識別し、必要箇所のみ除草剤を散布する。Blue River Technology（2017年Deere買収）のEdgeAI実装で除草剤使用量を平均66%削減。',
 '精密農業AIの実装的成功例。Edge AI＋自律機械の農業実装の決定点。',
 'phai_hw', 'Precision Agriculture', 2023, 'system', 4,
 '["Lee Redden", "Jorge Heraud"]',
 '["John Deere 2023 Sustainability Report"]',
 '["John Deere", "Blue River Technology"]',
 '精密農業, 自律スプレーヤ, EdgeAI', 'precision agriculture, autonomous sprayer, EdgeAI',
 'primary', 90),

('phai_agri_0002', 'Planet Labs Dove衛星群', 'Planet Labs Dove Satellite Constellation',
 'Planet Labsの200機超のDove衛星群による日次3m解像度地球観測。Descartes LabsのGeospatial Foundation Modelと組み合わせ、農作物収量予測・干ばつ早期警報を商用化。USDA NASS公式統計を補完する。',
 '衛星×AI×農業の標準的データインフラ。Foundation Model時代の地球観測の代表例。',
 'phai_vis', 'Satellite AI Agriculture', 2014, 'system', 3,
 '["Will Marshall", "Robbie Schingler"]',
 '["Planet Labs Imagery Atlas (2024)"]',
 '["Planet Labs", "Descartes Labs"]',
 '衛星AI, 農業観測, Foundation Model', 'satellite AI, agricultural monitoring, Foundation Model',
 'primary', 90),

('phai_agri_0003', 'PhytlSign (Vivent SA)', 'PhytlSign Plant Electrophysiology System',
 'Vivent SA（スイス、2017設立）が商用化した植物電気生理モニタリングシステム。植物体内の電気信号から水分需要・病害ストレスを機械学習で予測。温室生産（トマト・キュウリ・レタス）で実用展開。',
 '植物電気生理-AI連携の最初の商用実装。書籍第十一章「関係論的存在論」の技術的先駆。',
 'phai_vis', 'Plant-AI', 2017, 'system', 3,
 '["Carrol Glen", "Nigel Wallbridge"]',
 '["Plant electrome and machine learning for irrigation needs (Frontiers in Plant Science, 2024)"]',
 '["Vivent SA"]',
 '植物電気生理, PhytlSign, 植物モニタリング', 'plant electrophysiology, PhytlSign, plant monitoring',
 'primary', 85),

('phai_agri_0004', 'UPSIDE Foods培養鶏肉', 'UPSIDE Foods Cultivated Chicken',
 'UPSIDE Foods（旧Memphis Meats）が2023年6月にUSDA/FDA共同承認を取得した世界初の米国販売培養鶏肉。Mosa Meatのバーガー試食(2013)から10年で規制承認に到達した軌跡を実証。',
 '培養肉の規制承認実現。合成生物食料系統の決定的マイルストーン。',
 'phai_hw', 'Cultivated Meat', 2023, 'system', 4,
 '["Uma Valeti", "Mark Post"]',
 '["Cultivated meat: a review (Nature Food, 2024)"]',
 '["UPSIDE Foods", "Mosa Meat"]',
 '培養肉, 細胞農業, 食料代替', 'cultivated meat, cellular agriculture, alternative protein',
 'primary', 95),

('phai_agri_0005', 'Solein (Solar Foods)', 'Solein Single-Cell Protein',
 'Solar Foods（フィンランド）が2024年に商用工場稼働させた、空気・水・電気から微生物発酵で生産する単細胞タンパク質。気候・土地・水資源から食料生産を切り離す技術。',
 'Precision Fermentation食料の量産化実例。2050年食料系再編の先行事例。',
 'phai_hw', 'Precision Fermentation', 2024, 'system', 4,
 '["Pasi Vainikka", "Juha-Pekka Pitkanen"]',
 '["Single-cell proteins from gas fermentation (Trends in Food Science & Technology, 2024)"]',
 '["Solar Foods"]',
 'ソレイン, 単細胞タンパク, 空気タンパク', 'Solein, single-cell protein, air protein',
 'primary', 90),

('phai_agri_0006', '垂直農業（Plenty/AeroFarms系統）', 'Vertical Farming (Plenty/AeroFarms lineage)',
 'AeroFarms (2004設立)、Plenty (2014設立)、80 Acres Farms、Bowery Farmingらが展開する都市型垂直農場。LED効率改善（200μmol/J超）と再生可能エネルギー直結で土地効率200倍・水使用95%減を実証。',
 '垂直農業の実装的展開と再編。2030年代の都市食料生産の基盤。',
 'phai_hw', 'Vertical Farming', 2014, 'system', 3,
 '["David Rosenberg", "Matt Barnard", "Toyoki Kozai"]',
 '["Plant Factory: An Indoor Vertical Farming System for Efficient Quality Food Production (Kozai 2019)"]',
 '["AeroFarms", "Plenty", "Bowery Farming"]',
 '垂直農業, 植物工場, 都市農業', 'vertical farming, plant factory, urban agriculture',
 'secondary', 85),

('phai_agri_0007', 'Pivot Bio窒素固定菌', 'Pivot Bio Nitrogen-Fixing Microbes',
 'Pivot Bioが商用化した窒素固定菌（Klebsiella variicola改変株）。トウモロコシ根圏で大気窒素を固定し化学肥料を代替。2024年米国コーンベルトで100万エーカー超に展開。',
 'AI設計微生物の農業実装。化学肥料依存からの構造的離脱の先行事例。',
 'phai_vla', 'Microbial Agriculture', 2018, 'system', 4,
 '["Karsten Temme", "Alvin Tamsir"]',
 '["Microbial communities can be designed by AI (Nature Microbiology, 2024)"]',
 '["Pivot Bio"]',
 '窒素固定菌, 微生物農業, 化学肥料代替', 'nitrogen-fixing microbes, microbial agriculture, fertilizer alternative',
 'primary', 90),

('phai_agri_0008', 'C4 Rice Project', 'C4 Rice Project (IRRI)',
 'International Rice Research Institute (IRRI)が主導する、稲のC3光合成をC4光合成に改変するゲノム編集プロジェクト。Karki et al. (2013)以降の研究蓄積で2030年代の品種リリースを準備。',
 '気候適応農業の代表事例。AI×ゲノム編集の作物多様化の先行軌道。',
 'phai_sim', 'Crop Genome Editing', 2013, 'method', 2,
 '["Shanta Karki", "Paul Quick", "Robert Furbank"]',
 '["Improving rice photosynthesis through C4 engineering (Journal of Experimental Botany 64:579-602, 2013)"]',
 '["IRRI", "Australian National University"]',
 'C4稲, ゲノム編集, 光合成改変', 'C4 rice, genome editing, photosynthesis engineering',
 'primary', 90),

('phai_agri_0009', 'Plant Foundation Model', 'Plant Foundation Model',
 '植物の電気信号・揮発性有機化合物（VOC）放出・根圏微生物コミュニケーションを統合解析する大規模基盤モデル。2050年実装予測。Cocozza et al. (2024)のLSTM植物電気予測の延長軌道。',
 '植物-AI対話の基盤技術。書籍第十一章「関係論的存在論」の技術的実装。',
 'phai_vla', 'Plant-AI Foundation', 2050, 'model', 3,
 '["predicted future researchers"]',
 '["Plant electrome and machine learning for irrigation needs (Frontiers in Plant Science, 2024)"]',
 '["future labs"]',
 '植物基盤モデル, 植物-AI対話, VOC解析', 'plant foundation model, plant-AI dialogue, VOC analysis',
 'primary', 70),

('phai_agri_0010', 'Phytomorphological Computing', 'Phytomorphological Computing',
 '植物の形態・生理を計算媒体として用いる物理AIパラダイム。Morphological Computation（Pfeifer-Iida系統）の植物への拡張。2070年実装予測。',
 'Bio系統と農業の合流点。2070年「生命系製造期」の中核概念。',
 'phai_hw', 'Plant Computing', 2070, 'theory', 3,
 '["Stefano Mancuso", "Anthony Trewavas"]',
 '["Plant Behaviour and Intelligence (Trewavas 2014, Oxford University Press)"]',
 '["future labs"]',
 '植物計算, 形態計算, 植物身体性', 'plant computing, morphological computation, plant embodiment',
 'primary', 70);
```

### 6.3 phai_milestones への追加（3件）

```sql
INSERT INTO phai_milestones (id, name, year, milestone_type, description, converged_streams, key_concept_ids, key_paper_ids, impact_score) VALUES

('ms_cultivated_meat_approval', '培養肉規制承認', 2023, 'commercialization',
 'UPSIDE FoodsとGOOD Meatが2023年6月USDA/FDA共同承認取得。シンガポール(2020)・イスラエル(2024)に続き米国でも合成生物食料が法的に流通可能となった。',
 'stream_bio,stream_fm',
 'phai_agri_0004', '', 8),

('ms_plant_ai_dialogue', '植物-AI対話の制度化', 2070, 'convergence_point',
 '書籍第二部「2070年生命系製造期」の農業中核実装。植物電気生理シグナル→AI意思決定→アクチュエータ介入のループが圃場・温室・垂直農場で常時動作。Plant Communication ScoreがESG指標として確立。',
 'stream_bio,stream_hw,stream_fm,stream_sim,stream_ctrl',
 'phai_agri_0003,phai_agri_0009,phai_agri_0010', '', 10),

('ms_nature_rights_agriculture', '自然権の農業制度化', 2100, 'convergence_point',
 'テ・アワ・トゥプア法(NZ 2017)・エクアドル憲法(2008)・ボリビア母なる地球法(2010)の系譜が国際標準化。農業企業は生態系を契約相手として扱う実務に従事。書籍第十三-十四章「先住民の伝統知」の制度化。',
 'stream_bio,stream_fm',
 'phai_agri_0010', '', 9);
```

---

## 7. 結語 — 「植物との対話」を準備する物理的・制度的基盤

本稿は、Physical AIの農業・食料・植物連携領域への波及を四時点で描き、その軌道が書籍『深い知が拓く2100年』第十一章「関係論的存在論」・第十三-十四章「先住民の伝統知」・第二部「2070年 生命系製造期」と接続することを示した。

四時点軌道の特徴は、農業が(i)2030年精密農業AIの全面展開、(ii)2050年合成生物食料の主流化、(iii)2070年植物-AI連携農業の制度化、(iv)2100年「植物との対話」が農業中核へ、という階段状の変化を辿る点にある。この軌道は単なる技術ロードマップではなく、「植物・微生物・生態系を技術対象から関係相手へ転換する」という関係論的存在論の物質的・制度的準備として理解される。

PHAI-DB拡張提案は、新規概念10件・スピルオーバー領域1件・マイルストーン3件、計14件のSQL INSERTで構成される。これらは既存のBio系統（stream_bio）、HW系統（stream_hw）、Foundation Model系統（stream_fm）、Simulation系統（stream_sim）、Control系統（stream_ctrl）と複数接続し、Physical AIロードマップにおける農業領域の経験的基盤を提供する。

引用論文はすべてNature/Science/PNAS/Nature Food/Nature Plants/Nature Microbiology/Nature Reviews Microbiology/Frontiers in Plant Science/Trends in Plant Science/Trends in Food Science & Technology/Annual Review of Plant Biology/Annual Review of Environment and Resources/The Lancet/Journal of Experimental Botany/Molecular Plant/Nature Sustainabilityなどの査読誌掲載・DOI付与済みの一次論文に限定した。日本・東/東南/南アジアの思想的引用は使用していない（IRRI・JAXA等の技術データのみ引用）。先住民の伝統知への参照は書籍内部の議論への接続にとどめ、特定民族の知識引用は行っていない。

*本稿は Phase 4 波及分野策定チーム W3（農業・食料・植物連携）の成果として、Phase 2 Stream 3（Bio/Bio-mimicry）、Phase 2 Stream 4（Materials/Energy）、および書籍『深い知が拓く2100年』第十一章・第十三-十四章・第二部・終章と直接接続する。*
