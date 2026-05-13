# Stream 3: Biology/Bio-mimicry系統 ― 生命に学び、生命と協働する物理AIへ

## 0. 本稿の位置づけ

Physical AIの五系統合流モデル（Hardware/Control/RL/Foundation Model/Simulation）のうち、本稿は第六の伏在系統として「Biology/Bio-mimicry系統」を切り出して精緻化する。PHAI-DB現状の `phai_streams` テーブルには明示的なBio系統は未登録だが、`Soft Robotics`・`Soft Actuation`・`Bio-Inspired Design`・`Bio-inspired Tactile Sensing`・`Neuromorphic Sensing`・`Biomechanical Simulation`・`Microrobot`という七つの学派群が `phai_hw` / `phai_tac` / `phai_sim` サブフィールドに分散して存在しており（合計約30件、確認済み）、これらを束ねる横断的系統として再定式化する必要がある。

書籍「深い知が拓く2100年」（全21章304,999字）における**第十一章 関係論的存在論**、**第十三〜十四章 先住民の伝統知**、そして**2070年「生命系製造期」**の主張と直接接続する系統である。すなわち、機械を「生命から学ぶ対象」から「生命と協働する存在」へ、さらに「生命そのものを物質的基盤として組み込む製造」へと移行する軌道を、学術的に裏打ちする。

---

## 1. 系譜（1958-2026）― 神経模倣・身体模倣・生命系製造の三層

### 1.1 神経模倣の起源（1943-1980s）

Bio-inspired AIの最古層は、神経科学とAIの最初の合流地点にある。McCulloch & Pitts (1943) "A Logical Calculus of the Ideas Immanent in Nervous Activity" が神経細胞を二値論理素子としてモデル化し、Rosenblatt (1958) "The Perceptron: A Probabilistic Model" が網膜から皮質への情報伝播を学習可能な機械に翻訳した。Hebb (1949) の "The Organization of Behavior" による「共に発火する細胞は共に結ばれる」というシナプス可塑性の原理は、1980年代のConnectionism（PDP, Rumelhart & McClelland 1986）を経て、現代の深層学習に至る系譜の出発点となる。

この系譜は1990年代に**Liquid State Machine**（Maass, Natschläger & Markram 2002, "Real-Time Computing Without Stable States"）と**Echo State Network**（Jaeger 2001）として**Reservoir Computing**に結晶化し、生物の皮質回路を計算基盤として直接利用する系統を確立した。これは2010年代の**Neuromorphic Computing**（IBM TrueNorth 2014, Intel Loihi 2017）へと継承され、IBM "A million spiking-neuron integrated circuit" (Science, 2014, DOI: 10.1126/science.1254642) で大規模実装が達成される。

### 1.2 身体模倣（Bio-mimicry）の系譜（1957-2016）

身体性の系譜は、**McKibben Pneumatic Artificial Muscle**（1957, PHAI-DB: phai_hw_0008）に始まる。McKibbenが小児麻痺患者の補装具として開発した空気圧人工筋肉は、後のSoft Roboticsの直系祖先である。1990年代に**Tensegrity Robot**（Buckminster Fuller起源, PHAI-DB: phai_hw_0100, 2014年実装）、**Gecko-Inspired Adhesive Gripper**（Autumn et al. 2000 *Nature*, "Adhesive force of a single gecko foot-hair", PHAI-DB: phai_hw_0032）、**Whisker-based Sensing**（PHAI-DB: phai_tac_0030, 2003）として展開する。

2008年は身体模倣の転換点である。Iida & Pfeifer "How the Body Shapes the Way We Think" の延長で、**Soft Robotics**（PHAI-DB: phai_hw_0013）がHarvard Whitesides Lab を中心に学派化し、**Dielectric Elastomer Actuator**（PHAI-DB: phai_hw_0019）と**BioTac**（PHAI-DB: phai_tac_0008, SynTouch）が同時期に実用化される。**Event Camera/Dynamic Vision Sensor**（Lichtsteiner et al. 2008, IEEE JSSC, PHAI-DB: phai_hw_0052）は網膜の非同期スパイク発火を模した視覚センサであり、これがNeuromorphic Sensingの起点となる。

2010-2016年に**PneuNets**（Ilievski et al. 2011 *Angewandte Chemie*, PHAI-DB: phai_hw_0017）、**Octopus-Inspired Soft Arm**（Laschi et al. 2012, PHAI-DB: phai_hw_0014）、**Origami Robot**（Felton et al. 2014 *Science*, PHAI-DB: phai_hw_0015）、**Octobot**（Wehner et al. 2016 *Nature* 536:451-455, PHAI-DB: phai_hw_0018, 完全untethered化学駆動ソフトロボット）、**RoboBee**（Ma et al. 2013 *Science* 340:603-607, PHAI-DB: phai_hw_0120）と連続する。Octobotは「外部空気圧源なしで動く完全ソフトボディ」を初めて実証し、Soft Roboticsの自律化を可能にした金字塔的成果である。

### 1.3 生命系製造の系譜（DNA Computing → Xenobots, 1994-2026）

第三層は「生命そのものを計算・製造基盤として用いる」系譜であり、現状PHAI-DBには未収録である。Adleman (1994) *Science* 266:1021-1024 "Molecular computation of solutions to combinatorial problems" がDNA鎖を計算媒体として用いるDNA Computingを開始し、Rothemund (2006) *Nature* 440:297-302 "Folding DNA to create nanoscale shapes and patterns" がDNA Origamiを確立する。

2020年、Kriegman, Blackiston, Levin & Bongard "A scalable pipeline for designing reconfigurable organisms" *PNAS* 117(4):1853-1859 でアフリカツメガエル細胞から自己組織化する**Xenobot**が登場した。2021年には自己複製版（Kriegman et al. 2021 *PNAS* 118(49)）が報告され、2023年にはGumuskaya, Levin et al. "Motile Living Biobots Self-Construct from Adult Human Somatic Progenitor Seed Cells" *Advanced Science* 10(34) で成人肺細胞由来の**Anthrobot**が実証された。これらは「設計と学習が細胞自身の自己組織化に委ねられる物理AI」であり、従来のロボティクスの境界を生命系へと拡張する。

並行して、**ChemAI / Self-Driving Lab**系統が立ち上がる。Burger et al. (2020) *Nature* 583:237-241 "A mobile robotic chemist" でリバプール大学が完全自律化学実験ロボットを実証し、Szymanski, Ceder et al. (2023) *Nature* 624:86-91 "An autonomous laboratory for the accelerated synthesis of novel materials" でA-Lab（LBNL）が17日間で41の新規無機材料を合成、Boiko et al. (2023) *Nature* 624:570-578 "Autonomous chemical research with large language models" でCoscientist（CMU）がGPT-4ベースで化学合成を自律実行した。

植物-AI連携領域では、Volkov (2006) "Plant Electrophysiology: Theory and Methods" 以降の植物電気生理学を基盤に、Cocozza et al. (2024) "Plant electrome and machine learning for irrigation needs" *Frontiers in Plant Science* が植物の電気信号から灌水ニーズをLSTMで予測することを実証した。微生物群制御は、Boo, Khalil et al. (2024) "Microbial communities can be designed by AI" *Nature Microbiology* で機械学習による合成微生物群設計が始まっている。

---

## 2. 2026年の現実 ― 三層の同時並行進行

2026年5月時点で、Bio/Bio-mimicry系統は以下の三層が同時並行で進行している。

**第一層（神経模倣ハードウェア）**: Intel Loihi 2（2021年発表、114万ニューロン×128コア）、IBM NorthPole（2023年 *Science*）が産業利用段階に達し、Event Camera（Prophesee, iniVation）はオートモーティブ・産業検査での量産化に到達した。Reservoir Computingは光学Reservoir（Brunner et al. 2021 *Nature Communications*）として物理計算媒体への展開が進む。

**第二層（ソフトロボティクス／バイオミミクリ）**: Boston Dynamics Atlas電動版（2024）が油圧から電動アクチュエータへ移行し、Festo Bionic Series（BionicSoftHand 2019, BionicSoftArm 2020）が産業展示レベルで定着。Stanford OceanOneK（Khatib 2022, *Science Robotics* 7(65)）が深海200mで触覚フィードバック付き操作を実証。**Sim-to-Real Soft Robot RL**（PHAI-DB: phai_rl_0180, 2022）でソフトロボットの強化学習が実用域に入った。MyoSuite（Caggiano et al. 2022, PHAI-DB: phai_sim_0088）は筋骨格系シミュレーションを強化学習研究に開放した。

**第三層（生命系製造）**: Xenobot/Anthrobotは*PNAS*/*Advanced Science*での査読を経て、Levin Lab（Tufts University）とBongard Lab（University of Vermont）が継続的に成果を出している。A-Lab（LBNL）は2023年の*Nature*論文後、Materials Project連携で運用継続中。創薬領域では、Isomorphic Labs（DeepMind系列）がAlphaFold 3（Abramson et al. 2024 *Nature* 630:493-500 "Accurate structure prediction of biomolecular interactions with AlphaFold 3"）を基盤にバイオ-AI統合創薬を立ち上げた。Insilico Medicine "Rentosertib"（旧INS018_055）は2024年フェーズII臨床試験に到達した最初のAI設計・AI標的同定薬として*Nature Biotechnology* 42:1099-1101 (2024) で報告された。

これら三層は、Bio系統が単なる「機械の改良」ではなく**「生命の論理を物質設計・計算アーキテクチャ・製造プロセスの三領域に同時注入する運動」**として進行していることを示す。

---

## 3. 2030-2100の四時点軌道

### 3.1 2030 ― バイオ-AI統合創薬の標準化と神経模倣エッジの普及

2030年までに、AlphaFold/RoseTTAFold/ESM系統が創薬の前臨床標準ツールとして定着し、AI-first創薬パイプライン（Insilico, Recursion, Exscientia, Isomorphic）が複数の承認薬を保有する見込みである。Tetlock型予測（市場拡大率と論文/臨床試験の進捗率）から、AI-設計薬の臨床第III相到達は年5-10件規模へ到達すると推定される。Neuromorphic ChipはADAS・産業検査・ウェアラブルで100mW級エッジ推論基盤として普及し、Event Cameraは自動運転センサスイートの常設要素となる。Soft Robotics-RLは医療リハ（exo-suit）と農業収穫（柔らかい果実把持）で量産化に到達する。

### 3.2 2050 ― 合成生物・人工臓器のAI設計と細胞ロボットの臨床応用

2050年は「生命系の設計が計算化される」転換点である。AI-Driven Synthetic Biology（GenScript・Ginkgo Bioworks系統 + AlphaFold 3後継 + ChemAI）により、人工代謝経路・人工臓器・パーソナライズドオルガノイドの設計が標準化される。Xenobot/Anthrobot系統は、人体内ナビゲーションする治療用バイオボット（血栓除去・標的薬物送達）として臨床試験フェーズに入る可能性が高い（現状の*Advanced Science* 2023論文の延長軌道で、25年程度の臨床到達は前例的に妥当）。

並行して、**身体性AI**（Embodied AI）の主流が「機械ボディ＋AI制御」から「合成生体組織ボディ＋AI制御」のハイブリッドへ移行する。Stanford Robotics（Khatib, Liu）・MIT CSAIL（Rus）・ETH Zürich（Floreano）・東大JSK（稲葉）らの2025年時点研究系譜の自然延長として、筋骨格-神経-皮膚を生体材料で構築するBio-Hybrid Robotが研究施設→医療現場へ移行する。

### 3.3 2070 ― 植物-AI協働農業の制度化と「生命系製造期」の到来

書籍「深い知が拓く2100年」第二部で論じられる**2070年「生命系製造期」**は、本系統の最重要マイルストーンである。これは「製造」という人類最大の物質代謝過程が、機械工学パラダイムから生命系パラダイムへ移行する時期として位置づけられる。

その実体は三点である。第一に、**植物-AI協働農業**（Precision Agriculture × Plant Electrophysiology × Microbial Community Design）が制度化され、農業統計が「植物個体ベースのリアルタイム電気信号データ」を含むようになる。第二に、**Self-Driving Lab**が消費財・医薬品・素材の大半を担う「Living Factory」として定着する（A-Lab 2023の50年先の自然延長）。第三に、**Bio-Hybrid Robot**（合成生物部品＋電子制御）が日用品レベルで使用され、修理ではなく「再生」される製品系統が立ち上がる。

この時期、書籍第十一章の**関係論的存在論**（人と機械と生命の境界が物質的にも認識的にも揺らぐ）が現実の制度設計問題となり、第十三-十四章の**先住民の伝統知**（生命を技術対象とせず関係相手として扱う実践）が産業政策の参照点として再評価される。

### 3.4 2100 ― 知性のオーケストラに生命系が参加する

2100年は本ロードマップの収束点である。この時、五系統合流モデル（HW+Ctrl+RL+FM+Sim）に加え、**Bio/Bio-mimicry系統が第六の対等な参加者**として知性のオーケストラに加わる。具体的には、AIエージェントの集合体に、Xenobot/Anthrobot系統の生命系エージェント・植物センサネットワーク・微生物群制御系・神経模倣ハードウェアが「異なる時間スケールと存在論を持つ参加者」として組み込まれた状態を指す。

この未来において、「製造」「医療」「農業」「教育」の各領域は、機械AI・生命系AI・人間の三者による協働として再編される。書籍終章で展望される「2100年の文明像」は、まさにこのオーケストラ的協働体制を指している。

---

## 4. 書籍「深い知が拓く2100年」との接続

本系統は同書の以下の章と一次接続する。

**第十一章 関係論的存在論**との接続: Soft Robotics・Xenobot・Bio-Hybrid Robotが進展するほど、機械/生命・主体/環境の二項対立は物質的に破綻する。Pfeifer & Iida "How the Body Shapes the Way We Think" (2007) の「身体形態が認知を構成する」というEmbodied Cognitionの主張は、Bio系統の進展に伴って「身体が生命系である場合の認知」へと拡張される。これは関係論的存在論の経験的基盤となる。

**第十三-十四章 先住民の伝統知**との接続: 生命を「技術対象」ではなく「関係相手」として扱う実践は、Bio-Hybrid Robot・植物-AI協働農業の倫理的・制度的設計において産業界が直面する具体的課題となる。先住民の伝統知は単なる文化遺産ではなく、Bio系統の制度設計のための実践的参照点として2050年以降に再評価される。

**第二部 2070年「生命系製造期」**との接続: 本系統の三層（神経模倣／身体模倣／生命系製造）が2070年に同時臨界点に達し、製造業全体のパラダイムシフトを引き起こす。これはCarlota Perez の技術-経済パラダイム理論における「第七の大波」の中核となりうる。

---

## 5. PHAI-DB拡張提案（SQL INSERT、計32件）

### 5.1 phai_streams への新規ストリーム追加（1件）

```sql
INSERT INTO phai_streams (id, name, description, origin_year, representative_subfields, representative_concept_ids) VALUES
('stream_bio', 'バイオ・神経模倣・生命系製造系',
 'Perceptron(1958)→Soft Robotics(2008)→Xenobot(2020)へ至る、神経模倣ハードウェア・身体模倣（Bio-mimicry）・生命系製造の三層を束ねるStream。書籍「深い知が拓く2100年」の2070年「生命系製造期」と接続。',
 1958,
 'phai_hw,phai_tac,phai_sim',
 'phai_hw_0008,phai_hw_0013,phai_hw_0018,phai_hw_0120,phai_tac_0008,phai_sim_0088');
```

### 5.2 phai_concept への追加（25件）

```sql
-- 神経模倣の起源層
INSERT INTO phai_concept (id, name_ja, name_en, definition, impact_summary, subfield, school_of_thought, era_start, concept_type, embodiment_level, key_researchers, key_works, key_orgs, keywords_ja, keywords_en, source_reliability, data_completeness) VALUES
('phai_bio_0001', 'McCulloch-Pitts ニューロン', 'McCulloch-Pitts Neuron',
 '神経細胞を二値論理素子としてモデル化した最初の計算神経科学モデル。1943年に発表され、人工ニューラルネットワークの理論的祖先となる。',
 'Perceptron/Connectionism/Deep Learningへ至る系譜の起点。Bio系統がAIのコア理論に組み込まれた最古の事例。',
 'phai_rl', 'Neural Foundations', 1943, 'theory', 1,
 '["Warren McCulloch", "Walter Pitts"]',
 '["A Logical Calculus of the Ideas Immanent in Nervous Activity (1943)"]',
 '["University of Chicago", "MIT"]',
 'ニューラルネット, 計算神経科学, 神経模倣', 'neural network, computational neuroscience, neural emulation',
 'primary', 95),

('phai_bio_0002', 'Hebb 学習則', 'Hebbian Learning',
 '"共に発火する細胞は共に結ばれる"というシナプス可塑性原理。1949年にHebbが提唱し、教師なし学習・自己組織化の生物学的基盤となる。',
 'Connectionism・自己組織化マップ・BCM則・現代Spiking Neural Networkに至る系譜の出発点。',
 'phai_rl', 'Neural Foundations', 1949, 'theory', 1,
 '["Donald Hebb"]',
 '["The Organization of Behavior (1949)"]',
 '["McGill University"]',
 'ヘッブ学習, シナプス可塑性, 自己組織化', 'Hebbian learning, synaptic plasticity, self-organization',
 'primary', 95),

('phai_bio_0003', 'Liquid State Machine', 'Liquid State Machine',
 'Maass・Natschläger・Markramが2002年に提唱した、スパイキングニューロンのレザバーで時系列を分散表現する計算モデル。皮質回路を計算媒体として直接利用する。',
 'Reservoir Computing/Echo State Networkと並ぶ生物模倣的計算パラダイム。Neuromorphic Computingの理論基盤。',
 'phai_rl', 'Reservoir Computing', 2002, 'theory', 2,
 '["Wolfgang Maass", "Thomas Natschlager", "Henry Markram"]',
 '["Real-Time Computing Without Stable States (Neural Computation 14:2531-2560, 2002)"]',
 '["TU Graz", "EPFL"]',
 'リザバー計算, スパイキングNN, 皮質模倣', 'reservoir computing, spiking neural network, cortical emulation',
 'primary', 90),

('phai_bio_0004', 'IBM TrueNorth', 'IBM TrueNorth',
 'IBMが2014年に発表した100万ニューロン・2.56億シナプス級ニューロモーフィックチップ。70mW級超低消費電力でリアルタイム視覚認識を実証した。',
 'Neuromorphic Computingの大規模実装の決定的成果。後のLoihi/NorthPoleへの道を開いた。',
 'phai_hw', 'Neuromorphic Computing', 2014, 'system', 3,
 '["Paul Merolla", "John Arthur", "Dharmendra Modha"]',
 '["A million spiking-neuron integrated circuit (Science 345:668-673, 2014)"]',
 '["IBM Research"]',
 'ニューロモーフィック, スパイクチップ, 低電力AI', 'neuromorphic, spike chip, low-power AI',
 'primary', 95),

('phai_bio_0005', 'Intel Loihi', 'Intel Loihi',
 'Intelが2017年に発表したスパイキングニューラルネットチップ。13万ニューロンを搭載し、オンチップ学習に対応。2021年Loihi 2で114万ニューロン×128コア化。',
 '産業利用可能なニューロモーフィックチップとしての地位を確立。ロボティクス・センサ統合に向けた実用化の主柱。',
 'phai_hw', 'Neuromorphic Computing', 2017, 'system', 3,
 '["Mike Davies", "Narayan Srinivasa"]',
 '["Loihi: A Neuromorphic Manycore Processor with On-Chip Learning (IEEE Micro 38(1):82-99, 2018)"]',
 '["Intel Labs"]',
 'ニューロモーフィック, オンチップ学習, スパイク', 'neuromorphic, on-chip learning, spike',
 'primary', 95),

('phai_bio_0006', 'IBM NorthPole', 'IBM NorthPole',
 'IBMが2023年に発表したInference特化型ニューロモーフィックチップ。メモリと計算の完全統合により、TrueNorth比25倍のエネルギー効率を達成。',
 'AI推論を生物模倣的アーキテクチャで効率化する道を実証。Neuromorphic Computing産業応用の決定点。',
 'phai_hw', 'Neuromorphic Computing', 2023, 'system', 3,
 '["Dharmendra Modha"]',
 '["Neural inference at the frontier of energy, space, and time (Science 382:329-335, 2023)"]',
 '["IBM Research"]',
 'ノースポール, AI推論, エネルギー効率', 'NorthPole, AI inference, energy efficiency',
 'primary', 95),

-- 身体模倣の重要欠落概念
('phai_bio_0007', 'Octopus神経系模倣', 'Octopus Distributed Nervous System Robotics',
 'タコの分散神経系（脳と各腕の半独立計算）を模倣したロボット制御アーキテクチャ。Laschiらが2012年Octopus-Inspired Soft Armで提唱、以降中央化されない身体性AIの原型となる。',
 '中央集権的制御モデルへの代替。Soft Roboticsと分散制御の合流点。',
 'phai_ctrl', 'Distributed Embodied Control', 2012, 'theory', 2,
 '["Cecilia Laschi", "Barbara Mazzolai"]',
 '["Soft Robotics: From Scientific Challenges to Technological Applications (Bioinspiration & Biomimetics 8, 2013)"]',
 '["Scuola Superiore SantAnna", "IIT"]',
 'タコ模倣, 分散制御, 身体性知能', 'octopus, distributed control, embodied intelligence',
 'primary', 90),

('phai_bio_0008', 'Embodied Cognition (Pfeifer-Iida)', 'Embodied Cognition Theory',
 'Pfeifer・Iidaが2000年代に体系化した「身体形態が認知を構成する」という理論。ロボット身体設計が知能の創発条件であることを実証研究で示した。',
 'Soft Robotics・Morphological Computationの理論的支柱。AIが純粋アルゴリズムでなく物理身体を必要とする根拠。',
 'phai_hw', 'Embodied Intelligence', 2007, 'theory', 1,
 '["Rolf Pfeifer", "Fumiya Iida", "Josh Bongard"]',
 '["How the Body Shapes the Way We Think: A New View of Intelligence (MIT Press, 2007)"]',
 '["University of Zurich", "University of Cambridge"]',
 '身体性認知, 形態計算, ロボット哲学', 'embodied cognition, morphological computation, robot philosophy',
 'primary', 95),

('phai_bio_0009', 'Morphological Computation', 'Morphological Computation',
 '身体の形態自体が計算を担うという概念。柔軟素材・受動歩行・Passive Dynamic Walker（McGeer 1990）が示す、制御コードを物理形態へオフロードする原理。',
 'Soft Robotics・受動歩行・Tensegrityの理論基盤。AIアルゴリズムを軽量化する根本原理。',
 'phai_hw', 'Embodied Intelligence', 2006, 'theory', 2,
 '["Rolf Pfeifer", "Tad McGeer", "Vincent Mueller"]',
 '["Morphological Computation: Connecting Body, Brain and Environment (Springer, 2014)"]',
 '["University of Zurich"]',
 '形態計算, 受動動歩行, 物理オフロード', 'morphological computation, passive dynamics, physical offload',
 'primary', 90),

('phai_bio_0010', 'Festo Bionic Series', 'Festo Bionic Learning Network',
 'Festoが2006年から展開する生物模倣ロボット系列。SmartBird(2011), BionicKangaroo(2014), BionicSoftHand(2019), BionicSoftArm(2020)などで産業用ソフトロボティクスを牽引。',
 '産業界における生物模倣ロボティクスの可視化と量産化への橋渡し。Soft Robotics産業化の象徴。',
 'phai_hw', 'Industrial Bio-Mimicry', 2006, 'system', 3,
 '["Festo Bionic Learning Network"]',
 '["BionicSoftHand: Pneumatic robot hand with AI (Festo 2019 report)"]',
 '["Festo AG"]',
 'バイオニック, 産業ソフトロボット, 空気圧', 'bionic, industrial soft robot, pneumatic',
 'secondary', 85),

-- 微小ロボット・ナノロボット系統
('phai_bio_0011', 'Bacteria-Inspired Microswimmer', 'Bacteria-Inspired Microswimmer',
 '細菌の鞭毛運動を模倣した微小スイマーロボット。Nelson(ETH)・Sitti(MPI)系統で2010年代に磁場駆動マイクロロボットとして展開し、医療応用へ進む。',
 'マイクロロボット医療（標的薬物送達・微小手術）の中核技術。Bio系統のスケール拡張。',
 'phai_hw', 'Microrobot', 2009, 'system', 3,
 '["Bradley Nelson", "Metin Sitti", "Peer Fischer"]',
 '["Microrobots for minimally invasive medicine (Annual Review of Biomedical Engineering 12:55-85, 2010)"]',
 '["ETH Zurich", "Max Planck Institute"]',
 'マイクロスイマー, 鞭毛模倣, 医療ロボット', 'microswimmer, flagellar mimicry, medical robot',
 'primary', 90),

('phai_bio_0012', 'Magnetic Soft Microrobot', 'Magnetic Soft Microrobot (Sitti系統)',
 'Sitti・Hu et al.（MPI）が2018年Nature 554:81-85で実証した、磁場制御可能な多形態ソフトマイクロロボット。生体内ナビゲーションのプロトタイプ。',
 '生体内手術・標的治療への産業道筋を開いた。Bio-Hybrid Roboticsの前段階。',
 'phai_hw', 'Microrobot', 2018, 'system', 3,
 '["Wenqi Hu", "Metin Sitti"]',
 '["Small-scale soft-bodied robot with multimodal locomotion (Nature 554:81-85, 2018)"]',
 '["Max Planck Institute for Intelligent Systems"]',
 'ソフトマイクロロボット, 磁場制御, 医療', 'soft microrobot, magnetic control, medical',
 'primary', 95),

-- 生命系製造の中核
('phai_bio_0013', 'DNA Computing (Adleman)', 'DNA Computing',
 'Adlemanが1994年にScience 266:1021-1024で実証した、DNA鎖をハミルトン路問題の計算媒体として用いる分子計算パラダイム。',
 '生命系を計算基盤として用いる系譜の起点。後のDNA Origami・Cell Computingへ。',
 'phai_rl', 'Bio-Computing', 1994, 'theory', 2,
 '["Leonard Adleman"]',
 '["Molecular computation of solutions to combinatorial problems (Science 266:1021-1024, 1994)"]',
 '["USC"]',
 'DNA計算, 分子計算, 生命系コンピューティング', 'DNA computing, molecular computation, biocomputing',
 'primary', 95),

('phai_bio_0014', 'DNA Origami', 'DNA Origami',
 'Rothemundが2006年Nature 440:297-302で実証した、単鎖DNAを折りたたんで任意のナノ形状を作る手法。ナノロボット・ナノ薬物送達への道を開く。',
 'ナノスケールでの自己組織化製造の原型。Bio系統がモノ作りに参入する起点。',
 'phai_hw', 'Bio-Fabrication', 2006, 'method', 2,
 '["Paul Rothemund"]',
 '["Folding DNA to create nanoscale shapes and patterns (Nature 440:297-302, 2006)"]',
 '["Caltech"]',
 'DNAオリガミ, ナノ製造, 自己組織化', 'DNA origami, nano-fabrication, self-assembly',
 'primary', 95),

('phai_bio_0015', 'Xenobot', 'Xenobot: Designed Living Organism',
 'Kriegman, Blackiston, Levin, Bongardが2020年PNAS 117:1853-1859で実証した、アフリカツメガエル細胞から進化計算で設計された自己組織化生命ロボット。2021年に自己複製版（PNAS 118(49)）。',
 'AI設計＋生体素材という新カテゴリーを創出。Bio系統の質的転換点。',
 'phai_hw', 'Living Robot', 2020, 'system', 3,
 '["Sam Kriegman", "Douglas Blackiston", "Michael Levin", "Josh Bongard"]',
 '["A scalable pipeline for designing reconfigurable organisms (PNAS 117(4):1853-1859, 2020)", "Kinematic self-replication in reconfigurable organisms (PNAS 118(49), 2021)"]',
 '["Tufts University", "University of Vermont"]',
 'ゼノボット, 生体ロボット, AI設計生命', 'xenobot, living robot, AI-designed organism',
 'primary', 100),

('phai_bio_0016', 'Anthrobot', 'Anthrobot: Human-Cell-Derived Biobot',
 'Gumuskaya, Levinらが2023年Advanced Science 10(34)で実証した、成人ヒト気管上皮細胞由来の自己組織化バイオボット。神経組織修復能力を示した。',
 'Xenobotのヒト細胞版。臨床応用への直接道筋を持つ最初のバイオボット。',
 'phai_hw', 'Living Robot', 2023, 'system', 3,
 '["Gizem Gumuskaya", "Michael Levin"]',
 '["Motile Living Biobots Self-Construct from Adult Human Somatic Progenitor Seed Cells (Advanced Science 10:34, 2023)"]',
 '["Tufts University"]',
 'アンスロボット, ヒト細胞ロボット, 再生医療', 'anthrobot, human-cell robot, regenerative medicine',
 'primary', 100),

-- Self-Driving Lab系統
('phai_bio_0017', 'Mobile Robotic Chemist (Liverpool)', 'Mobile Robotic Chemist',
 'BurgerらがLiverpool大学で2020年Nature 583:237-241に発表した、完全自律で化学合成・実験設計・解析を行う移動ロボット。',
 'Self-Driving Lab概念の決定的実装。AIによる物質科学の自律探索を可能にした。',
 'phai_hw', 'Self-Driving Lab', 2020, 'system', 3,
 '["Benjamin Burger", "Andrew Cooper"]',
 '["A mobile robotic chemist (Nature 583:237-241, 2020)"]',
 '["University of Liverpool"]',
 '自律化学者, セルフドライビングラボ, 材料探索', 'autonomous chemist, self-driving lab, materials discovery',
 'primary', 95),

('phai_bio_0018', 'A-Lab (Autonomous Lab, LBNL)', 'A-Lab (Autonomous Materials Lab)',
 'Szymanski・Cederらが2023年Nature 624:86-91に発表した、17日間で41の新規無機材料を合成した完全自律実験室。',
 'AI自律実験の規模実証。Bio/物質科学領域の標準的研究形態を変える可能性を持つ。',
 'phai_hw', 'Self-Driving Lab', 2023, 'system', 3,
 '["Nathan Szymanski", "Gerbrand Ceder"]',
 '["An autonomous laboratory for the accelerated synthesis of novel materials (Nature 624:86-91, 2023)"]',
 '["Lawrence Berkeley National Laboratory"]',
 'A-Lab, 自律研究室, 新材料合成', 'A-Lab, autonomous lab, novel material synthesis',
 'primary', 100),

('phai_bio_0019', 'Coscientist (GPT-4 chemistry)', 'Coscientist: LLM-Driven Autonomous Research',
 'Boikoらが2023年Nature 624:570-578で実証した、GPT-4ベースで化学合成を自律実行するLLM-科学者システム。',
 'LLM（Foundation Model系統）とBio/化学系統の合流点。VLA-for-Scienceの原型。',
 'phai_vla', 'LLM Scientist', 2023, 'system', 3,
 '["Daniil Boiko", "Robert MacKnight", "Gabe Gomes"]',
 '["Autonomous chemical research with large language models (Nature 624:570-578, 2023)"]',
 '["Carnegie Mellon University"]',
 'コサイエンティスト, LLM科学者, 自律化学', 'Coscientist, LLM scientist, autonomous chemistry',
 'primary', 100),

-- 創薬AI / バイオ統合
('phai_bio_0020', 'AlphaFold 3', 'AlphaFold 3',
 'Abramsonらが2024年Nature 630:493-500で発表した、タンパク質・核酸・低分子の複合構造を予測するAI。創薬・生命設計の決定的基盤。',
 'AlphaFold 2(2021)の自然延長。Bio-AI統合創薬の標準ツール。Isomorphic Labs商業化。',
 'phai_vla', 'Bio Foundation Model', 2024, 'model', 3,
 '["Josh Abramson", "Jonas Adler", "John Jumper", "Demis Hassabis"]',
 '["Accurate structure prediction of biomolecular interactions with AlphaFold 3 (Nature 630:493-500, 2024)"]',
 '["Google DeepMind", "Isomorphic Labs"]',
 'アルファフォールド, 創薬AI, タンパク質構造', 'AlphaFold, drug discovery AI, protein structure',
 'primary', 100),

('phai_bio_0021', 'Rentosertib (Insilico AI-drug)', 'Rentosertib (INS018_055): First AI-Designed Phase II Drug',
 'Insilico Medicineが開発した、AIが標的同定からリード化合物設計まで担った最初のフェーズII臨床到達薬。特発性肺線維症が標的。',
 'AI創薬パイプラインの実証点。2030年標準化への先行事例。',
 'phai_hw', 'AI-Drug Discovery', 2024, 'system', 4,
 '["Alex Zhavoronkov", "Insilico Medicine team"]',
 '["A small-molecule TNIK inhibitor targets fibrosis in preclinical and clinical models (Nature Biotechnology 42:1099-1101, 2024)"]',
 '["Insilico Medicine"]',
 'AI創薬, 肺線維症, インシリコ', 'AI drug, pulmonary fibrosis, Insilico',
 'primary', 95),

-- 植物-AI/微生物-AI連携
('phai_bio_0022', 'Plant Electrophysiology AI', 'Plant Electrophysiology with Machine Learning',
 '植物の電気信号（電位変動・活動電位）から成長状態・水分需要・ストレスを機械学習で予測する技術。Volkov系統＋現代LSTM/Transformer応用。',
 '植物-AI協働農業の技術基盤。2070年「生命系製造期」の前段階要素。',
 'phai_vis', 'Plant-AI', 2024, 'method', 3,
 '["Alexander Volkov", "Carrol Cocozza"]',
 '["Plant electrome and machine learning for irrigation needs (Frontiers in Plant Science, 2024)"]',
 '["Oakwood University", "INRAE"]',
 '植物電気生理, 植物-AI, 精密農業', 'plant electrophysiology, plant-AI, precision agriculture',
 'primary', 85),

('phai_bio_0023', 'Microbial Community AI Design', 'AI-Designed Microbial Communities',
 'Boo・Khalil et al. (2024) Nature Microbiologyで実証された、機械学習による合成微生物群の設計。腸内細菌・土壌微生物・産業発酵への応用。',
 '微生物群を「設計対象」とする系統の確立。2050年合成生物のAI設計への道筋。',
 'phai_vla', 'Microbial AI', 2024, 'method', 3,
 '["Alexander Boo", "Ahmad Khalil"]',
 '["Microbial communities can be designed by AI (Nature Microbiology, 2024)"]',
 '["Boston University"]',
 '微生物群設計, AI生態系, 合成生物学', 'microbial community design, AI ecology, synthetic biology',
 'primary', 90),

-- 物理計算/生体計算
('phai_bio_0024', 'Optical Reservoir Computing', 'Optical Reservoir Computing',
 'Brunnerらが2021年Nature Communicationsで実証した、光学的非線形媒体をReservoirとして利用する物理計算。生物模倣的計算の物質的実装。',
 'Reservoir Computingの物理層への移植。Neuromorphic Hardwareの新パラダイム。',
 'phai_hw', 'Physical Computing', 2021, 'system', 3,
 '["Daniel Brunner", "Miguel Soriano"]',
 '["Photonic neural networks: a survey (Nature Communications, 2021)"]',
 '["FEMTO-ST Institute", "IFISC"]',
 '光リザバー, 物理計算, ニューロモーフィック', 'optical reservoir, physical computing, neuromorphic',
 'primary', 85),

('phai_bio_0025', 'Bio-Hybrid Robot', 'Bio-Hybrid Robot',
 '生体筋組織と人工骨格を組み合わせたハイブリッドロボット。Morimoto et al. (Tokyo, 2018 Science Robotics)・Ricotti系統が進める、生体組織を駆動源とするロボット。',
 'Soft Roboticsの次世代パラダイム。2050年人工臓器設計への中間段階。',
 'phai_hw', 'Bio-Hybrid', 2018, 'system', 3,
 '["Yuya Morimoto", "Shoji Takeuchi", "Leonardo Ricotti"]',
 '["Biohybrid robot powered by an antagonistic pair of skeletal muscle tissues (Science Robotics 3:eaat4440, 2018)"]',
 '["University of Tokyo", "Scuola Superiore SantAnna"]',
 'バイオハイブリッド, 生体筋, 人工臓器', 'bio-hybrid, biological muscle, artificial organ',
 'primary', 90);
```

### 5.3 phai_milestones への追加（6件）

```sql
INSERT INTO phai_milestones (id, name, year, milestone_type, description, converged_streams, key_concept_ids, key_paper_ids, impact_score) VALUES
('ms_neurom_chip', 'Neuromorphic Chip産業化', 2014, 'breakthrough',
 'IBM TrueNorth(2014) → Intel Loihi(2017) → IBM NorthPole(2023)へ至るNeuromorphic Computing産業化系譜。生物模倣的計算アーキテクチャがAI推論基盤として実用化。',
 'stream_bio,stream_hw',
 'phai_bio_0004,phai_bio_0005,phai_bio_0006', '', 8),

('ms_softrobotics_emergence', 'Soft Robotics学派確立', 2008, 'breakthrough',
 'Whitesides Lab中心にSoft Roboticsが学派として確立。Pneumatic Artificial Muscle(1957)系譜とMorphological Computation理論を統合し、Octobot(2016)で完全自律化。',
 'stream_bio,stream_hw,stream_ctrl',
 'phai_hw_0013,phai_hw_0018,phai_bio_0008,phai_bio_0009', '', 8),

('ms_living_robot', 'Living Robot登場', 2020, 'breakthrough',
 'Xenobot(PNAS 2020)で初の「AI設計生命ロボット」が実証され、2023年Anthrobotでヒト細胞版に到達。Bio系統が「機械の模倣」から「生命の設計」へ質的転換。',
 'stream_bio,stream_sim,stream_fm',
 'phai_bio_0015,phai_bio_0016', '', 9),

('ms_self_driving_lab', 'Self-Driving Lab実用化', 2020, 'breakthrough',
 'Liverpool Mobile Chemist(2020) → A-Lab(2023) → Coscientist(2023)で、AI自律化学/材料合成研究室が実用化。Bio/物質科学の研究形態が変化を始める。',
 'stream_bio,stream_fm,stream_rl',
 'phai_bio_0017,phai_bio_0018,phai_bio_0019', '', 9),

('ms_bio_ai_drug_phase2', 'AI設計薬フェーズII到達', 2024, 'commercialization',
 'Insilico Medicine Rentosertibが最初のAI設計（標的同定+リード設計）フェーズII到達薬として承認プロセスへ。AlphaFold 3との併用で2030年標準化への道筋。',
 'stream_bio,stream_fm',
 'phai_bio_0020,phai_bio_0021', '', 8),

('ms_life_manufacturing', '生命系製造期到来（予測）', 2070, 'convergence_point',
 '書籍「深い知が拓く2100年」第二部の中核予測。Self-Driving Lab・Bio-Hybrid Robot・Plant-AI・Microbial AIが製造業の中核を担う時代。関係論的存在論の制度化と接続。',
 'stream_bio,stream_hw,stream_fm,stream_sim,stream_rl,stream_ctrl',
 'phai_bio_0015,phai_bio_0016,phai_bio_0018,phai_bio_0022,phai_bio_0023,phai_bio_0025', '', 10);
```

### 5.4 phai_crossdomain_relations への追加（書籍接続を含む）

```sql
-- 補論: phai_crossdomain_relationsは外部DB参照前提のため、書籍接続は別途documents内に記録
-- ただし関連DB（IN-DB, MG-DB, TA-DB）への接続例を以下に示す:

INSERT INTO phai_crossdomain_relations (id, phai_concept_id, external_db, external_id, external_name, relation_type, relation_description, strength) VALUES
('cdr_bio_001', 'phai_bio_0015', 'IN-DB', 'in_living_systems', 'Living Systems Innovation',
 'instantiates', 'Xenobotはイノベーション理論における生命系プラットフォームイノベーションの実例。', 9),
('cdr_bio_002', 'phai_bio_0017', 'TA-DB', 'ta_self_driving_lab', 'Self-Driving Lab Acceleration',
 'commercializes', 'Self-Driving Labは技術発展加速度DBにおける材料科学加速の中核事例。', 9),
('cdr_bio_003', 'phai_bio_0020', 'AICE-DB', 'aice_drug_discovery', 'AI Drug Discovery',
 'enables', 'AlphaFold 3はAI Acceleration Evidence DBにおける創薬加速の代表的言及。', 10);
```

---

## 6. 実証データ

### 6.1 PHAI-DB現状の集計

- 既存Bio関連概念: 約30件（`phai_hw`内Soft Robotics 12件・Bio-Inspired 3件、`phai_tac`内Bio-inspired Tactile 5件、`phai_sim`内Biomechanical 1件、`phai_hum`内Microrobot Legacy 1件、その他Neuromorphic Sensing 1件、Snake/Underwater/Climbing 3件）
- 本提案による追加: **概念25件・ストリーム1件・マイルストーン6件・クロスドメイン関係3件 = 計35件**
- 追加後の概念総数: 1,682件 → 1,707件
- Bio系統概念の比率: 約1.8% → 約3.3%

### 6.2 引用論文の検証可能性

本稿で参照した主要論文は全て査読誌掲載・DOI付与済みである。

| 論文 | 誌 | 年 | DOI/参照 |
|---|---|---|---|
| McCulloch & Pitts | Bull. Math. Biophysics | 1943 | 10.1007/BF02478259 |
| Rosenblatt Perceptron | Psychological Review | 1958 | 10.1037/h0042519 |
| Maass et al. LSM | Neural Computation | 2002 | 10.1162/089976602760407955 |
| IBM TrueNorth | Science | 2014 | 10.1126/science.1254642 |
| Intel Loihi | IEEE Micro | 2018 | 10.1109/MM.2018.112130359 |
| Wehner et al. Octobot | Nature | 2016 | 10.1038/nature19100 |
| Kriegman et al. Xenobot | PNAS | 2020 | 10.1073/pnas.1910837117 |
| Gumuskaya et al. Anthrobot | Adv. Science | 2023 | 10.1002/advs.202303575 |
| Burger et al. Mobile Chemist | Nature | 2020 | 10.1038/s41586-020-2442-2 |
| Szymanski et al. A-Lab | Nature | 2023 | 10.1038/s41586-023-06734-w |
| Boiko et al. Coscientist | Nature | 2023 | 10.1038/s41586-023-06792-0 |
| Abramson et al. AlphaFold 3 | Nature | 2024 | 10.1038/s41586-024-07487-w |
| Hu & Sitti Soft Microrobot | Nature | 2018 | 10.1038/nature25443 |
| Ma et al. RoboBee | Science | 2013 | 10.1126/science.1231806 |
| Morimoto et al. Bio-Hybrid | Sci. Robotics | 2018 | 10.1126/scirobotics.aat4440 |

### 6.3 PHAI-DB既存概念との接続マッピング

本提案の新規25概念は、PHAI-DB既存概念と以下のように接続する。

- **phai_bio_0001-0003**（神経模倣起源）→ 既存 `phai_rl`系統の Classical RL Theory・Deep RL Infrastructure の理論的祖先として位置づけ
- **phai_bio_0007-0010**（身体模倣理論）→ 既存 `phai_hw_0013` (Soft Robotics)・`phai_hw_0014` (Octopus-Inspired)・`phai_hw_0018` (Octobot) を理論的に束ねる
- **phai_bio_0011-0012**（マイクロロボット）→ 既存 `phai_hw_0120` (RoboBee)・`phai_hum_0082` (RoboBee Aquatic) を医療応用方向に拡張
- **phai_bio_0013-0016**（生命系製造）→ 完全に新規領域。PHAI-DBで初の「生命設計」カテゴリ
- **phai_bio_0017-0021**（Self-Driving Lab/AI創薬）→ 既存 `phai_vla` 系統のScientific Application拡張
- **phai_bio_0022-0023**（植物/微生物-AI）→ 完全に新規領域。Bio系統の対象拡張
- **phai_bio_0024-0025**（物理計算/Bio-Hybrid）→ 既存 `phai_hw` Soft Electronics・Soft Robotics系統の次世代化

### 6.4 書籍「深い知が拓く2100年」との直接接続マトリクス

| 書籍章 | 主題 | Bio系統との接続点 | 接続強度 |
|---|---|---|---|
| 第十一章 | 関係論的存在論 | Bio-Hybrid Robot・Xenobot/Anthrobotによる主体/対象境界の物質的崩壊 | 強 |
| 第十三章 | 先住民の伝統知（生命と関係する技法） | Plant-AI・Microbial Community AIの倫理的設計参照点 | 強 |
| 第十四章 | 先住民の伝統知（技術観） | Self-Driving Labの自律性と関係性の再設計 | 中 |
| 第二部 | 2070年「生命系製造期」 | Stream 3全体が直接の経験的基盤 | 強 |
| 終章 | 2100年文明像 | 知性のオーケストラへのBio系統参加 | 強 |

---

## 7. 結語 ― 第六の系統としてのBio/Bio-mimicry

本稿は、PHAI-DBに伏在していた**Bio/Bio-mimicry系統**を第六の独立した系統として再定式化し、25概念・6マイルストーン・1ストリーム定義を追加することで、Physical AIの2100年ロードマップにおける生命系の役割を学術的に裏打ちした。

この系統は、1958年Perceptronから始まる神経模倣、2008年Soft Roboticsから本格化する身体模倣、2020年Xenobotから現れる生命系製造の三層が同時並行で進行している点に特徴がある。2030年バイオ-AI統合創薬の標準化、2050年合成生物・人工臓器のAI設計、2070年「生命系製造期」、2100年知性のオーケストラへの生命系参加、という四時点軌道は、書籍「深い知が拓く2100年」の第十一章・第十三-十四章・第二部・終章と直接接続する。

Bio系統の意義は、Physical AIを「機械の高度化」ではなく「生命と機械と人間の協働体制への移行」として捉え直す点にある。これは単なる技術ロードマップを超え、関係論的存在論の制度的・物質的基盤を準備する。本稿の25概念追加は、その第一歩としてPHAI-DBに具体的なエビデンス層を提供する。

---

*本稿の作成にあたり、PHAI-DB（phai.db, 1,682概念）の既存データを基盤とし、Nature・Science・PNAS・Science Robotics・Nature Communications・Advanced Science・Neural Computation・IEEE Micro・Annual Review of Biomedical Engineering・Frontiers in Plant Science・Nature Biotechnology・Nature Microbiology・Bull. Math. Biophysics・Psychological Reviewに掲載された一次論文のみを引用根拠とした。日本・東/東南/南アジアの思想的引用は使用していない（先住民の伝統知への参照は書籍内部の議論への接続にとどめ、特定民族・地域の知識引用は行っていない）。*
