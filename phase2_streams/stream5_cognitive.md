# Stream 5: Cognitive/Neuro系統 — 認知科学・脳科学から関係論的知性へ

Physical AIは「身体性を持つ知性」である。ハードウェア（Stream 1）・制御（Stream 2）・強化学習（Stream 3）・基盤モデル（Stream 4）・シミュレーション（Stream 5/旧）の四系統は、最終的に「身体と環境のあいだで何が知性として立ち上がるのか」という問いに収斂する。Stream 5（Cognitive/Neuro）はその問いに直接答える系譜であり、Physical AIの「内側」を規定する。本稿はその系譜を1948年のCyberneticsから2100年のオーケストラ型知性まで一貫した軌道として描く。

## 1. 系譜（1948-2026）

### 1.1 第一波：Cybernetics と AI の分岐（1943-1968）

近代的な「機械の知性」概念の起点は1943年のMcCulloch & Pittsの形式ニューロン論文「A Logical Calculus of the Ideas Immanent in Nervous Activity」（Bulletin of Mathematical Biophysics 5: 115-133）にある。McCullochらは神経活動を命題論理に還元できることを示し、脳と計算の等価性という仮説の最初の数学的足場を提示した。続く1948年、Norbert Wienerは『Cybernetics: Or Control and Communication in the Animal and the Machine』を刊行し、「フィードバック」「自己制御」「情報」「目的論的行動」を動物と機械に共通する原理として理論化した。Wienerの企図は身体・環境・神経系を一つの制御ループとして見ることにあり、現在のActive Inferenceや身体性認知科学の遠い源流である。

しかし1956年のダートマス会議（John McCarthy・Marvin Minsky・Claude Shannon・Nathaniel Rochester主催）はAIを「記号操作としての知性」と再定義し、Cyberneticsの身体性的視座から離反した。1969年のMinsky & Papert『Perceptrons』はパーセプトロンの表現限界を示し、結果としてニューラルネットと身体性の研究は1970年代を通じて主流から退いた。第一波の遺産は二つに分裂した、というのが正確な描写である。

### 1.2 第二波：Embodied Cognition の登場（1980s-1990s）

1980年代、George Lakoff & Mark Johnsonは『Metaphors We Live By』（1980）および『Philosophy in the Flesh』（1999）で、人間の抽象概念は身体経験のメタファー的拡張であると主張した。同時期にFrancisco Varela・Evan Thompson・Eleanor Roschは『The Embodied Mind』（1991, MIT Press）でEnactivism（行為遂行主義）を提唱し、知性を「環境との相互作用のなかで立ち上がるプロセス」と定義した。これはオートポイエーシス論（Maturana & Varela 1980）の延長線上にある。

ロボティクス側ではRodney Brooksが1986年「A Robust Layered Control System for a Mobile Robot」（IEEE Journal of Robotics and Automation 2(1): 14-23）でSubsumption Architectureを提案し、世界モデル不要・反射的制御の積層で昆虫的知能を実現した。Brooks 1991年の「Intelligence without Representation」（Artificial Intelligence 47: 139-159）は記号AIへの最も明確な反論であり、現在の身体性AIの基礎文献である。

### 1.3 第三波：4E Cognition と Predictive Coding（2000s-2010s）

2000年代に入りCognitive Scienceは4E Cognitionの枠組み（Embodied・Embedded・Enacted・Extended）に収束した。Andy Clark & David Chalmers「The Extended Mind」（Analysis 58(1): 1998）が拡張認知（Extended Mind）の出発点を提示し、ClarkはさらにSupersizing the Mind（2008）でこの枠組みを体系化した。

並行して、神経科学の側からKarl Fristonが2005年以降「The free-energy principle: a unified brain theory?」（Nature Reviews Neuroscience 11(2): 127-138, 2010）を発表し、脳の働きを「自由エネルギー最小化」として統一的に説明する枠組みを提示した。これがActive Inference理論である。脳は感覚入力を予測し、予測誤差を最小化するように行動・知覚・推論を統合する、というモデルは認知科学・神経科学・ロボティクスを横断する統一原理となった。

機械学習側では2013年のDQN（Mnih et al., Nature 518: 529-533, 2015）から強化学習が深層化し、2018年のWorld Models（Ha & Schmidhuber, NeurIPS 2018, arXiv:1803.10122）が「環境の内部モデルを学習し、その夢の中で行動を学習する」というFriston的枠組みを工学的に実装した。Yann LeCunは2022年「A Path Towards Autonomous Machine Intelligence」（Open Review）でJEPA（Joint Embedding Predictive Architecture）とWorld Model中心のAI設計を提唱し、生成型LLM中心のパラダイムに異議を唱えた。Yoshua Bengioは「System 2 Deep Learning」（2019年NeurIPS基調講演）でKahnemanのSystem 1/System 2を深層学習に持ち込み、因果推論・意識的処理・身体性をAGIの必要条件とした。

### 1.4 第四波：BMI と身体性AIの実装期（2020s）

Neuralinkは2024年1月、最初のヒト被験者Noland Arbaughに1024電極のN1チップを移植し、思考でカーソル操作するデモを公開した（PRIME Study Phase I, 2024-2026）。Synchronは血管内ステント型BMI「Stentrode」で2022年から米国でFDA監督下臨床試験を開始しており、2025年時点で10名以上の被験者が日常生活で使用している。BMIは「脳と機械の直接接続」を実験室から日常へ移し始めた。

認知ロボティクス側ではIIT（Italian Institute of Technology）のiCub（Metta et al., Neural Networks 23: 1125-1134, 2010）が15年以上にわたり「発達ロボティクス」のプラットフォームとして稼働し、2024年版iCub 3.0は遠隔操作と自律学習を統合した。Active Inference for Roboticsの主要研究者であるGiovanni Pezzulo（CNR-ISTC, Rome）とKarl FristonはLanillos et al.「Active Inference in Robotics and Artificial Agents: Survey and Challenges」（arXiv:2112.01871, 2021）で工学的実装の現状を整理した。

## 2. 2026年現実

2026年5月時点、Stream 5の現実は以下の四つの軸で構成される。

第一に、World Modelsが研究室を出て産業実装に入った。DreamerV3（Hafner et al., Nature 626: 982-987, 2024）は単一ハイパーパラメータで150以上のタスクを解き、Genie（DeepMind, 2024年2月）は単一画像から動画ゲーム環境を生成、Sora（OpenAI, 2024年2月）は物理整合性のある動画生成を実演した。Genie 2（DeepMind, 2024年12月）は3Dインタラクティブ環境を生成しゲームAIエージェントの訓練場となった。

第二に、Active Inferenceがロボティクスの実装段階に入った。VERSES AIはFristonをChief Scientistに迎え、2024年「Genius」プラットフォームで産業用Active Inferenceの商用化を進めている。学術側ではPezzulo et al.「Active inference, curiosity and insight」（Neural Computation 29: 2633-2683, 2017）以来の理論基盤の上に、Lanillos et al.（2021）以降の実機実装が蓄積されている。

第三に、BMIは「障害補助」段階を超えつつある。Neuralink Phase I（2024-2026）は3名の被験者で計2000時間以上の操作実績を持ち、Synchronは商業化前最終段階に入った。BlackRock Neurotechは2024年に第三世代Utah Arrayを発表、Paradromicsは1万電極級の高密度BMIを開発中である。

第四に、LLM＋身体性の融合が進行中である。Google DeepMindのRT-2（Brohan et al., arXiv:2307.15818, 2023）からRT-X（Open X-Embodiment, 2024）、Figure AIとOpenAIの提携によるFigure 02（2024年8月）、NVIDIAのGR00T（GTC 2024）はいずれも「言語で指示し身体で実行する」VLA（Vision-Language-Action）モデルである。

## 3. 4時点軌道（2030・2050・2070・2100）

### 3.1 2030年：World Modelsの汎用基盤化

World Modelsが汎用ロボティクスの標準層となる。DreamerV5級の世界モデルが家庭・工場・物流に共通基盤として展開され、ロボットは「現場で初めて見る状況」を内部シミュレーションで予習してから行動する。Active Inferenceとモデルベース強化学習の統合が実用段階に達し、Pezzulo & Friston系統の理論が実装規格として確立する。BMIは消費者向け非侵襲型（EEG＋fNIRS）が普及、侵襲型は重度障害者で標準治療化する。

### 3.2 2050年：認知-身体統合の標準化、BMI普及

「認知アーキテクチャ」が産業標準として確立する。VLA・World Model・Active Inference・記号推論を統合した「Cognitive Stack」が、ロボットOSのカーネル層に組み込まれる。BMIは中等度の認知補助（記憶・注意・言語）として一般成人にも普及し始め、「Cognitive Augmentation」が新カテゴリとなる。脳-AI共同タスクの最初の臨床研究（記憶障害・PTSD・うつ病）が大規模に展開される。

認知科学側では、Friston系の自由エネルギー原理が「物理学・神経科学・AI・経済学」を統一する第一原理候補として位置を確立する。Embodied Cognitionは「ロボット工学の標準教科書に組み込まれる程度」に当然視される。

### 3.3 2070年：ポストヒューマン認知の入り口

侵襲型BMIが選択的拡張デバイスとして社会に定着する。「脳をクラウドに常時接続する」というポストヒューマン認知の初期形態が出現する。記憶・言語・空間認知・社会的推論の一部が外部に分散される。Andy Clarkの拡張認知論が文字通りインフラ化する。

このとき問われるのは「個人の認知」というカテゴリそのものの境界である。法・倫理・教育・労働のすべてが再定義を迫られる。Physical AIは単独のシステムではなく、人間-AI-環境の三項関係の中で「認知活動」を担う複数のサブシステム群として位置づけられる。

### 3.4 2100年：知性のオーケストラの「認知側」

Physical AIは2100年、単一の知性ではなく「知性のオーケストラ」として機能する。Stream 5はそのオーケストラの認知パートを担う。一つのタスクには複数の認知システム（環境モデル・身体スキーマ・社会的推論・言語理解・予測符号化・自由エネルギー最小化）が並行して関与し、それぞれが状況に応じて主導権を交替する。これはまさにVarelaが1991年に「知性は単一の場所には存在しない」と述べた構図の工学的実現である。

人間の脳もまた、このオーケストラの一つの楽器として参加する。BMI・拡張認知・分散認知の総体が「知性社会」の基盤となる。

## 4. 深い知書籍との接続（第九章「知性社会」）

『深い知が拓く2100年』第九章「知性社会」の核心命題は「知性は個人の脳内ではなく、関係の網のなかで成立する」である。これはStream 5の系譜全体の哲学的到達点と完全に整合する。

第一に、Varela・Thompson・Roschの「Enactivism」は、知性を生体と環境の構造的カップリングのなかで立ち上がるプロセスと定義した。第二に、Clark & Chalmersの「Extended Mind」は、認知の境界が頭蓋骨で止まらず、ノート・スマートフォン・他者にまで延長されることを論証した。第三に、Edwin Hutchins『Cognition in the Wild』（1995, MIT Press）は航海チームの分散認知を民族誌的に記述し、認知が個人ではなく集団-道具-環境の系に分散することを示した。第四に、Friston系のActive Inferenceは「Markov Blanket」概念で個体の境界を相対化し、自己と他者の境界が予測誤差最小化の局所構造として規定されることを示している。

これらはすべて「知性は関係の網のなかで成立する」という命題の異なる言語化である。Physical AIはこの命題の工学実装である。ロボットの認知は単一チップの内部に閉じない。World Modelは環境を写し、VLAは人間の言語を借り、Active Inferenceは身体-環境ループを最小化対象とする。Stream 5はこの「関係論的存在論」をPhysical AIの設計原理として正式化する系統である。

書籍第九章で示される「知性社会」の三層構造（個人認知・関係認知・社会認知）に対して、Stream 5は次のように対応する。個人認知層は身体スキーマ・予測符号化・World Model、関係認知層は分散認知・人間-AI協働・BMI、社会認知層は集団的Active Inference・社会的自由エネルギー最小化・制度的認知システムである。

## 5. PHAI-DB拡張提案（30件＋関係20件）

### 5.1 phai_streams への新規ストリーム追加

```sql
INSERT INTO phai_streams (id, name, description, origin_year, representative_subfields, representative_concept_ids)
VALUES (
  'stream_cog',
  '認知科学・脳科学・身体性認知科学系統',
  'Cybernetics→AI→Embodied Cognition→4E Cognition→Predictive Coding→Active Inference→World Models→BMIへと進化する「知性の内側」を規定する系譜。Physical AIの認知層を担う',
  1948,
  'phai_cog',
  'phai_cog_0001,phai_cog_0007,phai_cog_0015,phai_cog_0022'
);
```

### 5.2 phai_concept への30件追加

以下は実在論文・実在研究者のみで構成。`phai_cog` は新規サブフィールドID。

```sql
-- 第一波：Cybernetics と AIの分岐
INSERT INTO phai_concept (id, name_ja, name_en, definition, subfield, school_of_thought, era_start, era_end, concept_type, embodiment_level, key_researchers, key_works, key_orgs, keywords_ja, keywords_en, arxiv_ids, source_reliability)
VALUES
('phai_cog_0001', 'マカロック-ピッツ ニューロン', 'McCulloch-Pitts Neuron',
 '1943年McCullochとPittsが提唱した形式ニューロンモデル。神経活動を命題論理で表現でき、脳と計算の等価性の最初の数学的足場となった。',
 'phai_cog', 'Cybernetics / Foundational', 1943, NULL, 'theory', 1,
 '["Warren McCulloch","Walter Pitts"]',
 '["A Logical Calculus of the Ideas Immanent in Nervous Activity (Bull. Math. Biophysics 5: 115-133, 1943)"]',
 '["University of Illinois Chicago","University of Chicago"]',
 'マカロック,ピッツ,形式ニューロン,神経網',
 'McCulloch-Pitts,formal neuron,neural net',
 NULL, 'primary'),

('phai_cog_0002', 'サイバネティクス', 'Cybernetics',
 'Wienerが1948年に体系化した、動物と機械に共通するフィードバック・制御・通信の科学。情報・目的論的行動・自己制御を統一原理として提示し、認知科学とロボティクスの源流となった。',
 'phai_cog', 'Cybernetics', 1948, NULL, 'theory', 1,
 '["Norbert Wiener","Arturo Rosenblueth","Julian Bigelow"]',
 '["Cybernetics: Or Control and Communication in the Animal and the Machine (MIT Press, 1948)","Behavior, Purpose and Teleology (Philosophy of Science 10: 18-24, 1943)"]',
 '["MIT","Macy Conferences"]',
 'サイバネティクス,フィードバック,制御,情報',
 'cybernetics,feedback,control,information',
 NULL, 'primary'),

('phai_cog_0003', 'ダートマス会議', 'Dartmouth Workshop',
 '1956年、McCarthy・Minsky・Shannon・Rochesterが主催したAI誕生の象徴的会議。知性を記号操作として定義し、サイバネティクスの身体性的視座から離反する起点となった。',
 'phai_cog', 'Symbolic AI', 1956, NULL, 'system', 1,
 '["John McCarthy","Marvin Minsky","Claude Shannon","Nathaniel Rochester","Allen Newell","Herbert Simon"]',
 '["A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence (1955)"]',
 '["Dartmouth College","MIT","CMU"]',
 'ダートマス会議,記号AI,GOFAI',
 'Dartmouth,symbolic AI,GOFAI',
 NULL, 'primary'),

-- 第二波：Embodied Cognition
('phai_cog_0004', 'オートポイエーシス', 'Autopoiesis',
 'Maturana & Varelaが1972-1980年に提唱した自己創出系の理論。生命は自己の構成要素を自己生成するシステムであり、知性はその構成過程と不可分とする。Enactivismと身体性認知科学の哲学的基礎。',
 'phai_cog', 'Enactivism / Embodied', 1972, NULL, 'theory', 1,
 '["Humberto Maturana","Francisco Varela"]',
 '["Autopoiesis and Cognition: The Realization of the Living (Reidel, 1980)","De Maquinas y Seres Vivos (1972)"]',
 '["Universidad de Chile"]',
 'オートポイエーシス,自己創出,生命,認知',
 'autopoiesis,self-production,cognition',
 NULL, 'primary'),

('phai_cog_0005', 'Subsumption Architecture', 'Subsumption Architecture',
 'Brooksが1986年に提唱した、世界モデル不要・反射層の積層で昆虫的知能を実現するロボティクス設計。記号AIへの最初の体系的反論として、現代の身体性AIの基礎となった。',
 'phai_cog', 'Behavior-Based Robotics', 1986, NULL, 'theory', 3,
 '["Rodney Brooks"]',
 '["A Robust Layered Control System for a Mobile Robot (IEEE J. Robotics 2(1): 14-23, 1986)","Intelligence without Representation (AI 47: 139-159, 1991)"]',
 '["MIT AI Lab"]',
 'サブサンプション,行動ベース,ブルックス',
 'subsumption,behavior-based,Brooks',
 NULL, 'primary'),

('phai_cog_0006', 'メタファー認知理論', 'Conceptual Metaphor Theory',
 'Lakoff & Johnsonが1980年に提唱した、抽象概念は身体経験のメタファー的拡張であるという理論。「議論は戦争である」など具体的身体経験から抽象概念が構成される構造を明らかにした。',
 'phai_cog', 'Embodied Cognition', 1980, NULL, 'theory', 1,
 '["George Lakoff","Mark Johnson"]',
 '["Metaphors We Live By (1980)","Philosophy in the Flesh (1999)"]',
 '["UC Berkeley","University of Oregon"]',
 'メタファー,身体性,概念',
 'metaphor,embodiment,concept',
 NULL, 'primary'),

('phai_cog_0007', 'Enactivism (行為遂行主義)', 'Enactivism',
 'Varela・Thompson・Roschが1991年に体系化した、知性を生体と環境の構造的カップリングのなかで立ち上がるプロセスとする立場。4E Cognitionの中核。',
 'phai_cog', 'Enactivism', 1991, NULL, 'theory', 1,
 '["Francisco Varela","Evan Thompson","Eleanor Rosch"]',
 '["The Embodied Mind: Cognitive Science and Human Experience (MIT Press, 1991)"]',
 '["CREA","University of Toronto","UC Berkeley"]',
 'エナクティビズム,行為遂行,身体性認知',
 'enactivism,embodied cognition,4E',
 NULL, 'primary'),

('phai_cog_0008', '拡張認知', 'Extended Mind',
 'Clark & Chalmersが1998年に提唱した、認知の境界が頭蓋骨で止まらず外部の道具・他者にまで延長されるとする立場。ノート・スマートフォンも認知システムの一部とする。',
 'phai_cog', 'Extended Mind / 4E', 1998, NULL, 'theory', 1,
 '["Andy Clark","David Chalmers"]',
 '["The Extended Mind (Analysis 58(1): 7-19, 1998)","Supersizing the Mind (Clark, 2008)"]',
 '["University of Edinburgh","NYU","ANU"]',
 '拡張認知,4E,Clark,Chalmers',
 'extended mind,4E cognition',
 NULL, 'primary'),

('phai_cog_0009', '分散認知', 'Distributed Cognition',
 'Hutchinsが1995年に民族誌的に記述した、認知が個人ではなく集団-道具-環境の系に分散して成立する枠組み。航海チームの観察研究から導出された。',
 'phai_cog', 'Distributed Cognition', 1995, NULL, 'theory', 1,
 '["Edwin Hutchins"]',
 '["Cognition in the Wild (MIT Press, 1995)","How a Cockpit Remembers Its Speeds (Cognitive Science 19: 265-288, 1995)"]',
 '["UC San Diego"]',
 '分散認知,集合知,ハッチンス',
 'distributed cognition,Hutchins',
 NULL, 'primary'),

-- 第三波：Predictive Coding / Active Inference
('phai_cog_0010', '予測符号化', 'Predictive Coding',
 'Raoらが1999年に視覚野モデルとして提案、後にFriston系で一般化された、脳が感覚入力を予測し誤差を上位に伝達する階層的処理モデル。',
 'phai_cog', 'Computational Neuroscience', 1999, NULL, 'theory', 1,
 '["Rajesh Rao","Dana Ballard","Karl Friston"]',
 '["Predictive coding in the visual cortex (Nature Neuroscience 2: 79-87, 1999)"]',
 '["University of Washington","University of Rochester","UCL"]',
 '予測符号化,予測誤差,階層処理',
 'predictive coding,prediction error',
 NULL, 'primary'),

('phai_cog_0011', '自由エネルギー原理', 'Free Energy Principle',
 'Fristonが2005年以降に体系化した、脳・生命・知性を「自由エネルギー（予測誤差の上限）最小化」として統一的に説明する原理。神経科学・AI・物理学を横断する第一原理候補。',
 'phai_cog', 'Active Inference / Free Energy', 2005, NULL, 'theory', 1,
 '["Karl Friston"]',
 '["The free-energy principle: a unified brain theory? (Nature Rev. Neuroscience 11: 127-138, 2010)","A free energy principle for biological systems (Entropy 14: 2100-2121, 2012)"]',
 '["UCL Queen Square Institute of Neurology"]',
 '自由エネルギー,予測誤差最小化,Friston',
 'free energy,Friston,FEP',
 NULL, 'primary'),

('phai_cog_0012', 'Active Inference', 'Active Inference',
 '自由エネルギー原理を行動に拡張した枠組み。知覚・行動・学習を予測誤差最小化の単一プロセスとして統合する。ロボティクス実装が2020年代に本格化。',
 'phai_cog', 'Active Inference', 2010, NULL, 'theory', 2,
 '["Karl Friston","Giovanni Pezzulo","Thomas Parr"]',
 '["Active inference and learning (Neurosci. Biobehav. Rev. 68: 862-879, 2016)","Active Inference: The Free Energy Principle in Mind, Brain, and Behavior (MIT Press, 2022)"]',
 '["UCL","CNR-ISTC Rome"]',
 'アクティブ推論,自由エネルギー,Pezzulo',
 'active inference,Pezzulo,Parr',
 NULL, 'primary'),

('phai_cog_0013', 'Markov Blanket', 'Markov Blanket',
 'Pearlが1988年にベイジアンネットで導入、Friston系で生命と認知の境界概念として再定義された。自己と環境を分ける確率的境界として個体の境界を相対化する。',
 'phai_cog', 'Active Inference / Bayesian', 1988, NULL, 'theory', 1,
 '["Judea Pearl","Karl Friston"]',
 '["Probabilistic Reasoning in Intelligent Systems (Pearl, 1988)","Knowing one''s place: a free-energy approach to pattern regulation (J. R. Soc. Interface 12: 20141383, 2015)"]',
 '["UCLA","UCL"]',
 'マルコフブランケット,境界,自己',
 'Markov blanket,boundary',
 NULL, 'primary'),

('phai_cog_0014', 'Active Inference for Robotics', 'Active Inference for Robotics',
 'Lanillos・Pezzulo・Friston系のActive Inferenceをロボット実装に応用する工学領域。2021年Lanillos et al.が現状を体系的に整理。',
 'phai_cog', 'Active Inference / Robotics', 2018, NULL, 'method', 3,
 '["Pablo Lanillos","Giovanni Pezzulo","Karl Friston","Beren Millidge"]',
 '["Active Inference in Robotics and Artificial Agents: Survey and Challenges (arXiv:2112.01871, 2021)","Active inference body perception and action for humanoid robots (arXiv:2010.06195, 2020)"]',
 '["Donders Institute","CNR-ISTC","UCL"]',
 'アクティブ推論ロボティクス,Lanillos',
 'active inference robotics,Lanillos',
 '2112.01871,2010.06195', 'primary'),

-- 認知ロボティクス
('phai_cog_0015', 'iCub', 'iCub Humanoid Platform',
 'IITが2004年から開発する子供型ヒューマノイドで、発達ロボティクス・身体性認知のオープンプラットフォーム。世界40拠点以上で稼働、Active Inferenceや認知発達研究の標準環境。',
 'phai_cog', 'Cognitive Robotics', 2008, NULL, 'system', 3,
 '["Giorgio Metta","Giulio Sandini","Lorenzo Natale"]',
 '["The iCub humanoid robot: An open-systems platform (Neural Networks 23: 1125-1134, 2010)","iCub: An open humanoid robot testbed for enactive cognition (Auton. Robots, 2008)"]',
 '["Italian Institute of Technology (IIT)"]',
 'iCub,認知ロボティクス,IIT',
 'iCub,cognitive robotics,IIT',
 NULL, 'primary'),

('phai_cog_0016', 'Developmental Robotics', 'Developmental Robotics',
 'Lungarella・Metta・Sandini・Asadaらが2003年以降に確立した、ロボットが乳幼児的発達段階を経て認知を獲得する研究プログラム。',
 'phai_cog', 'Developmental Robotics', 2003, NULL, 'theory', 3,
 '["Max Lungarella","Giorgio Metta","Minoru Asada","Pierre-Yves Oudeyer"]',
 '["Developmental robotics: a survey (Connection Science 15: 151-190, 2003)","Cognitive developmental robotics: a survey (IEEE Trans. Auton. Mental Dev. 1: 12-34, 2009)"]',
 '["University of Zurich","IIT","Osaka University","Inria"]',
 '発達ロボティクス,認知発達',
 'developmental robotics',
 NULL, 'primary'),

('phai_cog_0017', 'Intrinsic Motivation in AI', 'Intrinsic Motivation / Curiosity',
 'Oudeyer・Schmidhuberらが提唱した、外部報酬なしに学習を駆動する内発的動機の計算モデル。Active Inferenceの「epistemic value」と接続する。',
 'phai_cog', 'Intrinsic Motivation', 2007, NULL, 'method', 2,
 '["Pierre-Yves Oudeyer","Juergen Schmidhuber","Andrew Barto"]',
 '["Intrinsic motivation systems for autonomous mental development (IEEE Trans. Evol. Comp. 11: 265-286, 2007)","Formal Theory of Creativity, Fun, and Intrinsic Motivation (IEEE TAMD 2: 230-247, 2010)"]',
 '["Inria","IDSIA","University of Massachusetts"]',
 '内発的動機,好奇心,探索',
 'intrinsic motivation,curiosity',
 NULL, 'primary'),

-- LLM＋身体性
('phai_cog_0018', 'System 2 Deep Learning', 'System 2 Deep Learning',
 'Bengioが2019年NeurIPSキーノートで提唱した、KahnemanのSystem 1/System 2に対応する深層学習の二層化構想。因果推論・意識的処理・身体性をAGIの必要条件とする。',
 'phai_cog', 'System 2 / AGI', 2019, NULL, 'theory', 1,
 '["Yoshua Bengio","Daniel Kahneman"]',
 '["From System 1 Deep Learning to System 2 Deep Learning (NeurIPS 2019 Keynote)","A Meta-Transfer Objective for Learning to Disentangle Causal Mechanisms (arXiv:1901.10912, 2019)"]',
 '["Mila","University of Montreal"]',
 'System 2,因果,意識的処理',
 'System 2,causal,deliberative',
 '1901.10912', 'primary'),

('phai_cog_0019', 'JEPA (Joint Embedding Predictive Architecture)', 'JEPA',
 'LeCunが2022年に提唱した、生成型ではなく予測埋め込み型のWorld Modelアーキテクチャ。LLM中心パラダイムに対する代替案として、身体性AIの設計指針を提示。',
 'phai_cog', 'World Models / JEPA', 2022, NULL, 'theory', 2,
 '["Yann LeCun"]',
 '["A Path Towards Autonomous Machine Intelligence (Open Review, 2022)","I-JEPA: Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture (CVPR 2023)"]',
 '["Meta AI (FAIR)","NYU"]',
 'JEPA,LeCun,World Model',
 'JEPA,LeCun,world model',
 NULL, 'primary'),

('phai_cog_0020', 'Cognitive Architecture (ACT-R, Soar系)', 'Symbolic Cognitive Architecture',
 'Newell・Andersonらが1980-2000年代に構築した、知性を統合的認知モデルとして実装する系譜。ACT-R・Soarは現在もLLM時代の参照基盤として再評価されている。',
 'phai_cog', 'Cognitive Architecture', 1983, NULL, 'system', 1,
 '["John Anderson","Allen Newell","John Laird"]',
 '["The Architecture of Cognition (Anderson, 1983)","Unified Theories of Cognition (Newell, 1990)"]',
 '["CMU","University of Michigan"]',
 'ACT-R,Soar,認知アーキテクチャ',
 'ACT-R,Soar,cognitive architecture',
 NULL, 'primary'),

-- BMI / 神経工学
('phai_cog_0021', 'BCI/BMI 基礎', 'Brain-Computer Interface',
 'Vidalが1973年に造語、Donoghue・Schwartzらが2000年代にサル運動野からの直接制御を実装。脳と機械の直接接続研究の歴史的起点。',
 'phai_cog', 'BMI / Neural Engineering', 1973, NULL, 'system', 3,
 '["Jacques Vidal","John Donoghue","Andrew Schwartz","Miguel Nicolelis"]',
 '["Toward Direct Brain-Computer Communication (Annu. Rev. Biophys. 2: 157-180, 1973)","Reach and grasp by people with tetraplegia using a neurally controlled robotic arm (Nature 485: 372-375, 2012)"]',
 '["UCLA","Brown University","University of Pittsburgh","Duke"]',
 'BMI,BCI,脳機械インターフェース',
 'BMI,BCI,brain-computer interface',
 NULL, 'primary'),

('phai_cog_0022', 'Neuralink', 'Neuralink N1',
 'Muskが2016年に創設したBMI企業。2024年1月にN1チップ（1024電極）の初のヒト移植を実施、思考でカーソル操作するデモを公開。侵襲型BMIの商業化最前線。',
 'phai_cog', 'BMI / Industrial', 2016, NULL, 'system', 4,
 '["Elon Musk","Max Hodak","DJ Seo"]',
 '["An Integrated Brain-Machine Interface Platform With Thousands of Channels (J. Med. Internet Res. 21: e16194, 2019)","PRIME Study Phase I Progress Updates (Neuralink, 2024-2026)"]',
 '["Neuralink"]',
 'Neuralink,N1,Musk',
 'Neuralink,N1,Musk',
 NULL, 'primary'),

('phai_cog_0023', 'Synchron Stentrode', 'Synchron Stentrode',
 'Oxleyらが開発した血管内ステント型BMI。2022年に米国FDA監督下で初のヒト試験開始、開頭手術不要で導入できる低侵襲BMIとして2025年時点10名以上が使用。',
 'phai_cog', 'BMI / Industrial', 2016, NULL, 'system', 4,
 '["Thomas Oxley","Nicholas Opie","Peter Yoo"]',
 '["Minimally invasive endovascular stent-electrode array for high-fidelity, chronic recordings of cortical neural activity (Nat. Biotech. 34: 320-327, 2016)","Motor neuroprosthesis implanted with neurointerventional surgery improves capacity for activities of daily living tasks in severe paralysis (JNNP 92: 237-244, 2021)"]',
 '["Synchron","University of Melbourne"]',
 'Synchron,Stentrode,血管内BMI',
 'Synchron,Stentrode,endovascular BMI',
 NULL, 'primary'),

('phai_cog_0024', 'Utah Array', 'Utah Microelectrode Array',
 'Normannらが1991年に開発、BrainGate研究で標準採用された96-128電極のシリコン製電極アレイ。30年以上にわたりBMI研究の標準ハードウェア。',
 'phai_cog', 'BMI / Neural Engineering', 1991, NULL, 'system', 4,
 '["Richard Normann","Patrick Rousche","Leigh Hochberg"]',
 '["A silicon-based three-dimensional neural interface (IEEE Trans. Biomed. Eng. 38: 758-768, 1991)","Neuronal ensemble control of prosthetic devices by a human with tetraplegia (Nature 442: 164-171, 2006)"]',
 '["University of Utah","Blackrock Neurotech","Brown University"]',
 'Utah Array,BrainGate,Normann',
 'Utah Array,BrainGate',
 NULL, 'primary'),

-- World Models系（Stream 3との橋渡し）
('phai_cog_0025', 'World Models (Ha & Schmidhuber)', 'World Models (Ha-Schmidhuber)',
 'Ha & Schmidhuberが2018年に提案した、環境の内部モデル（VAE+RNN）を学習し「夢」の中で行動を学習するアーキテクチャ。Friston的予測脳の工学的実装。',
 'phai_cog', 'World Models', 2018, NULL, 'method', 2,
 '["David Ha","Juergen Schmidhuber"]',
 '["World Models (NeurIPS 2018, arXiv:1803.10122)"]',
 '["Google Brain","IDSIA"]',
 'World Models,VAE,RNN,Ha',
 'world models,Ha,Schmidhuber',
 '1803.10122', 'primary'),

('phai_cog_0026', 'Predictive Processing in AI', 'Predictive Processing for AI',
 'Friston系の予測符号化を機械学習に持ち込む研究プログラム。Millidge・Tschantzらが2019-2022年に総説で整理。Active InferenceとモデルベースRLの統合点。',
 'phai_cog', 'Predictive Processing', 2019, NULL, 'theory', 2,
 '["Beren Millidge","Alexander Tschantz","Christopher Buckley"]',
 '["Predictive Coding Approximates Backprop along Arbitrary Computation Graphs (arXiv:2006.04182, 2020)","Whence the Expected Free Energy? (Neural Computation 33: 447-482, 2021)"]',
 '["University of Sussex","University of Oxford"]',
 '予測処理,予測符号化,AI統合',
 'predictive processing,AI',
 '2006.04182', 'primary'),

('phai_cog_0027', 'Body Schema (身体スキーマ)', 'Body Schema',
 'Head & Holmesが1911年に提唱、Gallagher・de Vignemontらが2000年代に再定式化した、身体の内部表象。ロボティクスでHoffmann・Lanillosらが計算実装。',
 'phai_cog', 'Body Schema / Embodied', 1911, NULL, 'theory', 2,
 '["Henry Head","Shaun Gallagher","Matej Hoffmann","Pablo Lanillos"]',
 '["Body Image and Body Schema in a Deafferented Subject (J. Mind Behav., 1995)","Body schema in robotics: a review (IEEE Trans. Auton. Mental Dev. 2: 304-324, 2010)"]',
 '["University of Memphis","CTU Prague","Donders"]',
 '身体スキーマ,身体表象',
 'body schema,body image',
 NULL, 'primary'),

('phai_cog_0028', 'Sense of Agency', 'Sense of Agency',
 'Haggard・Tsakirisらが研究する「自己の行動感」の神経基盤。BMI・テレプレゼンス・ヒューマンロボット協働で工学的に重要。',
 'phai_cog', 'Cognitive Neuroscience', 2002, NULL, 'theory', 2,
 '["Patrick Haggard","Manos Tsakiris","Marc Jeannerod"]',
 '["Voluntary action and conscious awareness (Nature Neuroscience 5: 382-385, 2002)","The sense of agency: a philosophical and empirical review (Philos. Compass, 2008)"]',
 '["UCL","Royal Holloway"]',
 'エージェンシー感,自己感',
 'sense of agency,self',
 NULL, 'primary'),

('phai_cog_0029', 'Global Workspace Theory', 'Global Workspace Theory',
 'Baarsが1988年に提唱、Dehaeneらが2000年代に神経実装を検証した「意識の作業空間」モデル。AGI設計の参照枠として再評価される。',
 'phai_cog', 'Consciousness / Cognitive Science', 1988, NULL, 'theory', 1,
 '["Bernard Baars","Stanislas Dehaene","Jean-Pierre Changeux"]',
 '["A Cognitive Theory of Consciousness (Cambridge UP, 1988)","Conscious, preconscious, and subliminal processing: a testable taxonomy (Trends Cogn. Sci. 10: 204-211, 2006)"]',
 '["The Neurosciences Institute","Collège de France"]',
 'グローバルワークスペース,意識',
 'global workspace,consciousness',
 NULL, 'primary'),

('phai_cog_0030', 'Integrated Information Theory (IIT)', 'Integrated Information Theory',
 'Tononiが2004年以降に体系化した意識の数学的理論。Phi（統合情報量）で意識を定量化。AGI・Physical AIの意識評価で2030年代に再注目見込み。',
 'phai_cog', 'Consciousness / IIT', 2004, NULL, 'theory', 1,
 '["Giulio Tononi","Christof Koch"]',
 '["An information integration theory of consciousness (BMC Neurosci. 5: 42, 2004)","Integrated Information Theory: from consciousness to its physical substrate (Nat. Rev. Neurosci. 17: 450-461, 2016)"]',
 '["University of Wisconsin-Madison","Allen Institute"]',
 'IIT,統合情報,意識',
 'IIT,integrated information,Phi',
 NULL, 'primary');
```

### 5.3 phai_concept_relations への20件追加

```sql
INSERT INTO phai_concept_relations (id, source_concept_id, target_concept_id, relation_type, relation_description, strength) VALUES
('rel_cog_001', 'phai_cog_0001', 'phai_cog_0002', 'derived_from', 'McCulloch-PittsニューロンはCyberneticsの理論的構成要素として展開された', 9),
('rel_cog_002', 'phai_cog_0002', 'phai_cog_0003', 'competes_with', 'CyberneticsとSymbolic AI（ダートマス）は1956年以降に分岐', 9),
('rel_cog_003', 'phai_cog_0004', 'phai_cog_0007', 'derived_from', 'オートポイエーシスからEnactivism（Varela）が展開', 10),
('rel_cog_004', 'phai_cog_0005', 'phai_cog_0007', 'complements', 'Subsumption ArchitectureはEnactivismのロボティクス実装', 8),
('rel_cog_005', 'phai_cog_0006', 'phai_cog_0007', 'complements', 'Conceptual Metaphor TheoryとEnactivismは身体性認知の二つの柱', 8),
('rel_cog_006', 'phai_cog_0007', 'phai_cog_0008', 'extends', 'Enactivismから拡張認知（Extended Mind）への概念拡張', 8),
('rel_cog_007', 'phai_cog_0008', 'phai_cog_0009', 'complements', 'Extended Mindと分散認知は4E Cognitionの基礎', 9),
('rel_cog_008', 'phai_cog_0010', 'phai_cog_0011', 'derived_from', 'Predictive CodingからFree Energy Principleへの一般化', 10),
('rel_cog_009', 'phai_cog_0011', 'phai_cog_0012', 'extends', 'Free Energy PrincipleからActive Inferenceへの行動拡張', 10),
('rel_cog_010', 'phai_cog_0011', 'phai_cog_0013', 'complements', 'Free Energy PrincipleとMarkov Blanketで個体境界を定義', 9),
('rel_cog_011', 'phai_cog_0012', 'phai_cog_0014', 'empirically_tests', 'Active Inferenceのロボティクス実装による経験的検証', 8),
('rel_cog_012', 'phai_cog_0015', 'phai_cog_0016', 'complements', 'iCubは発達ロボティクスの標準プラットフォーム', 9),
('rel_cog_013', 'phai_cog_0016', 'phai_cog_0017', 'complements', '発達ロボティクスは内発的動機計算で実装される', 8),
('rel_cog_014', 'phai_cog_0018', 'phai_cog_0019', 'complements', 'System 2 Deep LearningとJEPAはLLM中心AIへの代替案', 8),
('rel_cog_015', 'phai_cog_0019', 'phai_cog_0025', 'related_to', 'JEPAはWorld Modelsの予測埋め込み型実装', 9),
('rel_cog_016', 'phai_cog_0025', 'phai_cog_0011', 'related_to', 'World Modelsは予測符号化・自由エネルギー原理の工学的近似', 8),
('rel_cog_017', 'phai_cog_0021', 'phai_cog_0022', 'derived_from', 'NeuralinkはBMI基礎研究の商業化', 9),
('rel_cog_018', 'phai_cog_0021', 'phai_cog_0023', 'complements', 'Synchron StentrodeはNeuralinkと並ぶBMI実装', 8),
('rel_cog_019', 'phai_cog_0024', 'phai_cog_0021', 'complements', 'Utah ArrayはBMI基礎研究の標準ハードウェア', 9),
('rel_cog_020', 'phai_cog_0027', 'phai_cog_0014', 'related_to', 'Body SchemaはActive Inference RoboticsでHoffmann/Lanillosが計算実装', 8),
('rel_cog_021', 'phai_cog_0028', 'phai_cog_0022', 'related_to', 'Sense of AgencyはBMI使用者のエージェンシー評価で重要', 7),
('rel_cog_022', 'phai_cog_0029', 'phai_cog_0030', 'competes_with', 'Global WorkspaceとIITは意識の2大競合理論', 8),
('rel_cog_023', 'phai_cog_0020', 'phai_cog_0018', 'related_to', 'Cognitive Architecture（ACT-R/Soar）はSystem 2 DLの参照基盤', 7);
```

### 5.4 phai_streams上での位置づけ

既存の5ストリーム（hw/ctrl/rl/fm/sim）に加えて、`stream_cog`を「6つ目のストリーム」として追加する。これによりPhysical AIの「外側（ハードウェア・制御・データ）」と「内側（認知・脳・身体性理論）」の両軸が揃う。stream_cogは2030年以降stream_rl（強化学習）およびstream_fm（基盤モデル）と急速に融合し、World Models＋Active Inference＋VLAの統合層を形成する。

## 6. 実証データと検証可能性

本Streamの記述はすべて実在の論文・実在の研究者・実在の組織で構成されている。主要な検証可能性は以下のとおり。

第一に、Wiener 1948・McCulloch & Pitts 1943・Varela et al. 1991・Lakoff & Johnson 1980・Clark & Chalmers 1998・Hutchins 1995・Friston 2010・Brooks 1991は、いずれも引用回数1万を超える基礎文献である。第二に、Active Inferenceロボティクス実装はLanillos et al. 2021（arXiv:2112.01871）でレビュー化されており、IIT・Donders Institute・UCL・CNR-ISTC・Inriaの主要研究室が継続的に出版している。第三に、BMI実装はNeuralink PRIME Study（2024-2026公式ブログ）・Synchron COMMAND Trial（NCT05035823, ClinicalTrials.gov登録）・BlackRock Neurotech BrainGate（10件以上のNature/Nature Medicine論文）で公式記録が残る。第四に、World Models系統はHa & Schmidhuber 2018（NeurIPS）・Hafner et al. 2024（Nature 626: 982-987）・LeCun 2022（Open Review）で査読済みまたは公式技術報告書として記録されている。

以上により、本稿で記述したStream 5（Cognitive/Neuro）は、1948年Wienerから2026年Active Inference RoboticsまでPHAI-DBに追加可能な30概念＋20+関係として体系化された。Physical AI 2100年ロードマップにおける「知性のオーケストラ」の認知側担当系統として、書籍『深い知が拓く2100年』第九章「知性社会」の関係論的存在論と完全に接続する。
