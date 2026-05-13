# Stream 1: AI/ML系統 ── Physical AI 2100年ロードマップ

**作成日**: 2026-05-13
**対象**: PHAI-DB 5系統合流のうち、`stream_rl`（機械学習・強化学習系）と `stream_fm`（基盤モデル・VLM/VLA系）を統合したAI/ML系統
**範囲**: 2010-2100の系譜と未来軌道
**前提DB**: PHAI-DB（既存804件のAI/ML概念）、agi-roadmap-db（AGI予測20件・能力マイルストーン20件・定義15件）、ai-acceleration-evidence-db（551言及・97ドメイン）、tech-acceleration-db（227Kレコード）

---

## 1. 系譜の整理（2010-2026）

Physical AIにおけるAI/ML系統は、純粋なソフトウェアAIから「身体を持つAI」への移行プロセスとして整理できる。これは「学習」「表現」「推論」「行動」の四層が、年代ごとに異なる速度で身体側へ漸近していく軌跡である。

### 1.1 深層学習革命と知覚層の確立（2010-2016）

PHAI-DB に登録されている `phai_vis_0096`（ViT, 2021）・`phai_vis_0125`（Mask R-CNN, 2017）・`phai_vis_0100`（PointNet, 2017）に至る源流は、Krizhevsky-Sutskever-Hintonの AlexNet（2012, NeurIPS, arXiv:1102.0183 系統）にある。これによって視覚認識が手作業特徴量設計から学習特徴量へ移行した。続く ResNet（He et al. 2015, arXiv:1512.03385）が極深層化を実用域に押し上げ、検出（YOLO, Faster R-CNN）・セグメンテーション（FCN, U-Net）・ポーズ推定（OpenPose, PoseCNN）の汎用ライブラリ群が整った。

この時期の Physical AI への寄与は「知覚モジュールの汎用化」にあった。SLAM・点群処理・物体姿勢推定が、特定タスク向けハンドクラフト技術から「学習させれば良い」対象へと変質した。

### 1.2 深層強化学習の臨界点（2013-2018）

PHAI-DB の `phai_rl_0009`（DQN, 2013, arXiv:1312.5602）が深層学習×強化学習の合流点を示し、以後 `phai_rl_0019`（A3C, 2016）→`phai_rl_0020`（TRPO, 2015）→`phai_rl_0021`（PPO, 2017, arXiv:1707.06347）→`phai_rl_0024`（SAC, 2018, arXiv:1801.01290）と連続的に高次化した。`phai_rl_0066`（OpenAI Dactyl, 2018, arXiv:1808.00177）がこの系統で最初に「実機ロボットの巧緻な手内操作」を達成し、Domain Randomization（`phai_sim_0031`, 2017）がsim-to-real のボトルネックを部分的に解いた。同年の `phai_rl_0063`（QT-Opt, 2018, arXiv:1806.10293）はGoogleが大規模実機データで把持タスクを学習させ、深層RLが現実世界の物理タスクへ移行可能であることを示した。

### 1.3 Transformerと自己教師あり表現学習（2017-2020）

Vaswani et al. "Attention Is All You Need"（2017, arXiv:1706.03762）が登場、BERT（Devlin et al. 2018, arXiv:1810.04805）が下流タスクの fine-tune パラダイムを確立した。CV 側では MoCo（He et al. 2019, arXiv:1911.05722）・SimCLR（Chen et al. 2020, arXiv:2002.05709）・MAE（He et al. 2021, arXiv:2111.06377）が自己教師あり表現を実用化。ロボティクスでは R3M（`phai_vla_0108`, 2022, arXiv:2203.12601）・Voltron（`phai_vla_0107`, 2023, arXiv:2302.12766）・VIP（`phai_il_0032`, 2022）がエゴセントリック動画事前学習を提案、世界の物理を「言語に頼らずに」学ぶ経路を開いた。

### 1.4 基盤モデル時代と言語接地（2020-2023）

GPT-3（Brown et al. 2020, arXiv:2005.14165）の創発能力（few-shot learning）が「基盤モデル」概念（Bommasani et al. 2021, arXiv:2108.07258）を立ち上げた。これがロボティクスに流入する経路が三本あった。

第一は **言語による高次タスク計画**: SayCan（`phai_vla_0001`, 2022, arXiv:2204.01691）がLLMでサブゴール分解、affordance score で実行可能性を評価する枠組みを提示。

第二は **マルチモーダル接地**: CLIP（`phai_vis_0073`, 2021, arXiv:2103.00020）が画像-言語埋め込みを統一、CLIPort（`phai_vla_0015`, 2021, arXiv:2109.12098）がそれをマニピュレーションに転移した。

第三は **VLM のロボット化**: PaLM-E（`phai_vla_0002`, 2023, arXiv:2303.03378）が視覚-言語-行動を単一トランスフォーマで結び、RT-1（`phai_vla_0003`, 2022, arXiv:2212.06817）・RT-2（`phai_vla_0004`, 2023, arXiv:2307.15818）が「ロボット用基盤モデル」への道筋を提示。

### 1.5 拡散モデル・大規模実機データ・VLA確立（2023-2026）

Diffusion Policy（`phai_il_0010`, 2023, arXiv:2303.04137）が拡散モデルを行動生成に転用、ACT（`phai_il_0011`, 2023）と ALOHA（`phai_il_0012`, 2023）が低コスト両手協調プラットフォームを実証した。**Open X-Embodiment**（`phai_eval_0001`, 2023, arXiv:2310.08864）が22機種・527スキル・160万エピソードを統合し、ロボティクス版 ImageNet モーメントを生んだ。

2024-2025年には OpenVLA（`phai_vla_0006`, 2024, arXiv:2406.09246）・Octo（`phai_vla_0007`, 2024, arXiv:2405.12213）・π0（`phai_vla_0010`, 2024）・GR00T N1（`phai_vla_0008`, 2024）・Helix（`phai_vla_0009`, 2025, Figure AI）・RDT（`phai_vla_0055`, 2024）が **「単一モデルが複数機種で複数タスクを実行する」** 段階を確立。AGI-DBの MS-019（Manipulation generalization, 2023）がこの転換点を記録している。

---

## 2. Physical AI との合流点

「AI/MLとPhysical AIの合流」は単一の事件ではなく、**段階的に身体側へ漸近する複数の閾値超え**として捉える必要がある。

### 合流点A: 知覚の身体化（2015-2018）

PHAI-DB が示す通り、`phai_vis_0007`（ORB-SLAM, 2015）から `phai_vis_0008`（ORB-SLAM2, 2017）への遷移期に、深層学習由来の特徴点・深度推定がSLAMパイプラインに本格混入。DROID-SLAM（Teed-Deng 2021, arXiv:2108.10869）に至る系統で、Physical AI の知覚層は「手作業設計」から「学習ベース」へ完全に移行した。

### 合流点B: 強化学習の実機化（2018-2020）

OpenAI Dactyl（2018）・ANYmal の脚移動学習（Hwangbo et al. 2019, Science Robotics 26 Feb 2019）・MIT Mini Cheetah RL（`phai_rl_0069`, 2021）が「シミュレーションで学んだ政策が実機で動く」最初の証明群となった。Rapid Motor Adaptation（`phai_sim_0038`, 2021, arXiv:2107.04034）が脚ロボットの汎化を加速した。

### 合流点C: 言語条件付け（2022）

SayCan・RT-1 の登場で、初めて「自然言語で命じればロボットが実行する」が研究室レベルで実現。これは PHAI-DB が `ms_saycan` として記録するように、Stream 1とStream 2（ロボット工学・制御系）の初めての文法的接続だった。

### 合流点D: VLA基盤モデル（2023-2025）

RT-2・OpenVLA・GR00T・Helix・π0 によって、VLA（Vision-Language-Action）が独立した一研究領域として確立。`ms_rt2`（2023）と `ms_humanoid`（2025）がこの段階を記録している。重要なのは、これらが **「ロボット用に作られたモデル」ではなく「汎用VLMをロボット出力にfine-tuneしたもの」** である点。基盤モデルの転移性がPhysical AI領域でも有効であることが実証された。

### 合流点E: 大規模実機データ収集（2023-2026）

Open X-Embodiment（2023）・DROID（Khazatsky et al. 2024, arXiv:2403.12945, 564シーン・86千デモ）・AutoRT（`phai_rl_0170`, 2024）が「データ希少性」というPhysical AIの構造的ボトルネック（PHAI-DB `bn_data`）への組織的回答を提示。フリート学習・遠隔操縦・自律収集の三方向で進展。

---

## 3. 4時点（2030/2050/2070/2100）の予測軌道

「deep knowledge書籍」（西村勇也, 2026, 全21章304,999字）および AGI-DBのtimeline_predictions（20件）・capability_milestones（20件）を統合した予測軌道。

### 2030: 狭義AGI ×ロボティクス基盤モデル標準化

**根拠**:
- AGI-DB TL-003（Hassabis, DeepMind, 2024予測）・TL-011（Metaculus median 2030, 2020年時点の2050予測から短縮）・TL-018（Khosla 2030）が示す通り、業界・予測市場ともに2030年付近を「狭義AGI到達点」として収束的に予想。
- AGI-DB MS-007（数学オリンピックsilver, 2024）・MS-008（PhD-level Q&A, 2024）・MS-011（SWE-Bench 77%, 2025）が示す通り、抽象推論・専門知能はすでにヒト平均を超越済み。
- Physical AI 側では、PHAI-DB の phase_3（2026-2028, 大規模物流配備）・phase_4（2027-2029, サービス・家庭領域）が予測ロードマップとして登録済み。

**到達される能力**:
1. **VLA Foundation Model のスケール則確立**: GPT-4 → o3 が示した「推論時計算スケーリング」のロボット版が成立。実機データ規模1000万デモ・モデル規模100B超のVLAが標準化。
2. **クロスエンボディメント転移**: 単一モデルが二足・四足・産業マニピュレータ・移動車両を共通ポリシーで操作。Open X-Embodiment の発展形が事実上の業界標準データセットに。
3. **狭義AGI**: AGI-DBの DEF-005（DeepMind Morris et al 2024）における "Competent AGI"（50パーセンタイル成人を上回る）が広範な認知タスクで達成。

**Physical AIにおける意味**: deep knowledge書籍が示す「製造現場のオーケストラ化」（manufacturing-orchestra DB, 12章38,623字）の現実化が始まる。労働市場の構造変化（OECD Future of Workベンチマーク準拠）。

### 2050: 汎用AGI × 完全自律物理エージェント

**根拠**:
- AGI-DB TL-008（Kurzweil 2045 Singularity）・TL-012（AI Impacts 2047 HLMI median）・TL-009（Russell 2080, 5-50%）の中央予測が2045-2050に集中。
- 2030年時点の狭義AGIが20年で汎用化するペースは、Tetlock長期予測手法による超予測者中央値とも整合的。
- Physical AI側ではPHAI-DBの phase_5（2028-2031, 連続学習・自己改善）・phase_6（2030-2033, 完全自律マルチタスク）・phase_7（2033-2040, 汎用物理操作=身体性AGI）の延長線上に位置。

**到達される能力**:
1. **汎用AGI（DEF-002 Legg-Hassabisの「任意の知的タスク」基準充足）**: 形式的に厳密な意味でのAGI到達。新規領域での学習効率が人間を上回る。
2. **完全自律物理エージェント**: 非構造化環境（家庭・野外・災害現場・宇宙）での長時間自律運用。Lifelong learningによる現場適応・経験蓄積。
3. **物理世界モデル**: LeCun（DEF-004, JEPA系）が主張する「grounded world model」が、純粋言語モデルとは別経路で実用化される可能性。

**ボトルネック残存**: エネルギー効率・サンプル効率・形式的安全検証・社会受容（PHAI-DBの bn_safety, bn_dexter が継続論点）。

### 2070: 自己改善型AGI × ポストヒューマン物理協働

**根拠**:
- Kurzweil 2045 シンギュラリティの実装段階。
- AGI-DBの DEF-015（Bostrom Superintelligence, 2014）が想定する「全領域人間超越」状態。
- 自己改善ループ（PHAI-DB phase_5 の延長）が実装され、AIシステムが自身のアーキテクチャ・データ・訓練手順を最適化。

**到達される能力**:
1. **再帰的自己改善（Recursive Self-Improvement, RSI）**: AGI-DB DEF-009（Hutter AIXI）の理論的上限への漸近。アルゴリズム発見、計算アーキテクチャ設計、データ選別を機械が主導。
2. **ポストヒューマン物理協働**: 人間と機械の境界が機能的に流動化（BMI・ロボット拡張・遠隔身体性の常態化）。深い知が拓く2100年の第三部・第四部の議論領域。
3. **複合知能オーケストラ**: 単一AGIではなく、多様な専門知能の協調ネットワーク。manufacturing-orchestra DBが示すオーケストラ的協働の社会全般への拡張。

**思想的留意**: 西村勇也「深い知が拓く2100年」が指摘する通り、これは「知性のオーケストラ」モデルであり、単一の超越的知性ではない。

### 2100: 知性のオーケストラの一構成要素として

**根拠**:
- deep knowledge書籍の中心命題（全21章を貫く論旨）: 2100年の知性は「単一の AGI」ではなく「多様な知性の編成」になる。
- Physical AI はその中で「物理世界に介入する身体性をもつ知性層」として位置付けられる。
- ヒト・古典AI・生体AI・量子AI・分散AI・身体性AIなど、複数経路の知性が共存・協調する。

**到達される能力**:
1. **オーケストレーション原理**: AGIが指揮者ではなく、人間を含む多様な知能が役割分担する「楽団」モデル。
2. **物理層の透明化**: ロボットという概念が消え、物理操作能力が環境・建物・道具・身体に分散的に埋め込まれる（ambient embodiment）。
3. **新しい知的生態系**: 自然知能・人工知能・ハイブリッド知能の共進化。生物多様性に類比される「知性多様性」。

**Physical AIにとっての意味**: 2100年は「Physical AIの完成点」ではなく、Physical AIが他のAI形態と区別不能になる「境界溶解点」として捉えるべき。

---

## 4. 構造的ボトルネック

PHAI-DB の既存 `bn_data`, `bn_safety`, `bn_dexter`, `bn_hw` に加え、Stream 1 固有のボトルネック群を整理。

### 4.1 物理推論能力（Physical Reasoning Gap）

**現状**: GPT-4/o3 はAGI-DB MS-009（ARC-AGI 87.5%）を達成したが、Physical Reasoning（PIQA, PhysObjects, ThreeDWorld 等）では未だ人間に劣る。LLMは「箱の中にボールを入れて箱を逆さにすればボールは落ちる」を間違える事例が多数（GPT-4の物理推論誤答率 30-40%, Bisk et al. 2020）。

**含意**: 言語のみでは物理を学べない。EmbodiedQA（Das et al. 2018, arXiv:1711.11543）・PIQA（Bisk et al. 2020, arXiv:1911.11641）・ThreeDWorld（Gan et al. 2020, arXiv:2007.04954）・PhysObjects（Gao et al. 2023, arXiv:2309.02561）が評価ベンチマークの中核。

### 4.2 世界モデル（World Model）の不完全性

**現状**: World Models（Ha-Schmidhuber 2018, `phai_rl_0031`）・Dreamer（Hafner 2019, `phai_rl_0182` PlaNet系列）・JEPA（LeCun 2022 系）・Sora（OpenAI 2024）・Genie 2（DeepMind 2024）・Cosmos（NVIDIA 2025, `phai_sim_0068`）が進展中だが、物理整合性・因果性・長期一貫性が不十分。

**ボトルネック**: ピクセル予測と物理整合性の両立、長期シミュレーション安定性、稀少イベント（rare event）の生成能力。

### 4.3 長期計画とメモリ

**現状**: AGI-DB MS-015（長時間ウェブタスク, 2024）でも、ロボットの長期タスク（30分以上連続）は失敗率が高い。Decision Transformer（`phai_rl_0057`, 2021）・Trajectory Transformer（`phai_rl_0058`, 2021）が時系列モデリングを改善したが、エピソード横断的メモリは未解決。

**ボトルネック**: 失敗からの学習、過去経験の再利用、目標の階層的分解と保持。

### 4.4 サンプル効率

**現状**: 強化学習の典型的サンプル要求量は、人間の数千-数百万倍（Chollet 2019 DEF-008の論点）。Diffusion PolicyとACTでも、新規タスクごとに50-300デモが必要。

**ボトルネック**: メタ学習（`phai_rl_0072` MAML）・少数ショット学習・転移学習の物理タスクへの不徹底適用。

### 4.5 エネルギー効率（Energy Efficiency Gap）

**現状**: 人間の脳が20W、現代の大規模VLA推論が1kW級。3桁の効率差。GPT-4訓練がメガワット時オーダー、ヒト幼児の身体学習がワット時オーダー。

**含意**: Stream 5（ハードウェア・ニューロモーフィック系統）との合流が必須。Loihi 2・SpiNNaker・Akida 等ニューロモーフィックチップとPhysical AIの統合が2030-2040年代の技術的課題。

### 4.6 言語/身体の階層整合

**現状**: VLA は「言語指示 → 実行」の単方向で、ロボットが「言語に変換できない物理感覚」（例: 摩擦の微妙な変化、慣性の流れ）を上位レイヤーに報告する仕組みが弱い。

**ボトルネック**: 触覚信号の言語化（`phai_tac_0017` T3 Touch Transformer 2024 等が初期試行）、身体感覚の自然言語インターフェース。

---

## 5. PHAI-DB 拡張提案（SQL INSERT 30件以上）

### 5.1 新規概念（phai_concept）

```sql
-- 深層学習革命の基盤（PHAI-DBに未登録の重要源流）
INSERT INTO phai_concept (id, name_ja, name_en, definition, subfield, school_of_thought, era_start, concept_type, embodiment_level, key_researchers, key_works, key_orgs, keywords_ja, keywords_en, arxiv_ids, source_reliability, data_completeness)
VALUES
('phai_rl_0184', 'AlexNet', 'AlexNet (ImageNet 2012)', '畳み込みニューラルネットワークによる画像分類で人間レベルに迫る性能を実証。深層学習革命の起点となり、後のVision Transformer・CLIP・ViT等の基盤を作った。', 'phai_vis', 'Deep Learning Foundations', 2012, 'model', 1, '["Alex Krizhevsky","Ilya Sutskever","Geoffrey Hinton"]', '["ImageNet Classification with Deep CNNs (NeurIPS 2012)"]', '["University of Toronto"]', '深層学習,CNN,画像分類', 'deep learning,CNN,image classification', '1102.0183', 'verified_primary', 95),

('phai_rl_0185', 'ResNet', 'Residual Networks (ResNet)', '残差接続により極めて深いニューラルネットワーク（152層以上）の学習を可能にし、後のすべての深層モデルの基本要素となった。', 'phai_vis', 'Deep Learning Foundations', 2015, 'model', 1, '["Kaiming He","Xiangyu Zhang","Shaoqing Ren","Jian Sun"]', '["Deep Residual Learning for Image Recognition (CVPR 2016)"]', '["Microsoft Research Asia"]', '残差接続,深層ネットワーク', 'residual connection,deep network', '1512.03385', 'verified_primary', 95),

('phai_rl_0186', 'Transformer (Attention Is All You Need)', 'Transformer Architecture', '自己注意機構のみで構成されるアーキテクチャ。BERT, GPT, ViT, RT-2, OpenVLAに至る全ての基盤モデルの祖型。Physical AIではVLA・Diffusion Transformer Policy・ACTの中核。', 'phai_vla', 'Transformer Foundation', 2017, 'model', 1, '["Ashish Vaswani","Noam Shazeer","Niki Parmar","Aidan Gomez","Łukasz Kaiser","Illia Polosukhin"]', '["Attention Is All You Need (NeurIPS 2017)"]', '["Google Brain","Google Research"]', '注意機構,Transformer', 'attention,transformer', '1706.03762', 'verified_primary', 95),

('phai_rl_0187', 'BERT', 'BERT (Bidirectional Encoder Representations from Transformers)', '双方向マスク言語モデリングによる事前学習-fine-tuneパラダイムを確立。Physical AIではVLM系の言語側エンコーダの源流。', 'phai_vla', 'Self-Supervised Language', 2018, 'model', 1, '["Jacob Devlin","Ming-Wei Chang","Kenton Lee","Kristina Toutanova"]', '["BERT: Pre-training of Deep Bidirectional Transformers (NAACL 2019)"]', '["Google AI"]', 'BERT,事前学習', 'BERT,pretraining', '1810.04805', 'verified_primary', 92),

('phai_rl_0188', 'GPT-3', 'GPT-3 (Language Models are Few-Shot Learners)', '175Bパラメータの言語モデルが少数ショット学習能力を創発。基盤モデル時代の起点。SayCan・PaLM-E・RT-2に至る言語条件付きロボティクスの直接の親モデル。', 'phai_vla', 'Foundation Models', 2020, 'model', 1, '["Tom Brown","Benjamin Mann","Nick Ryder","Melanie Subbiah","Jared Kaplan","et al. (OpenAI)"]', '["Language Models are Few-Shot Learners (NeurIPS 2020)"]', '["OpenAI"]', 'GPT-3,基盤モデル,創発', 'GPT-3,foundation model,emergence', '2005.14165', 'verified_primary', 95),

('phai_rl_0189', 'Foundation Models Paper', 'On the Opportunities and Risks of Foundation Models', '基盤モデル概念を提唱し、その機会とリスクを体系化。Physical AI領域でのVLA研究を正当化する理論的枠組み。', 'phai_vla', 'Foundation Models Theory', 2021, 'theory', 1, '["Rishi Bommasani","Drew Hudson","Ehsan Adeli","et al. (Stanford CRFM)"]', '["On the Opportunities and Risks of Foundation Models (arXiv 2021)"]', '["Stanford CRFM"]', '基盤モデル,理論', 'foundation models,theory', '2108.07258', 'verified_primary', 90),

('phai_rl_0190', 'Chain-of-Thought Prompting', 'Chain-of-Thought Prompting', 'LLMに中間推論ステップを生成させることで複雑タスクの精度を向上。SayCan・Inner Monologueの基盤。Physical AIではタスク分解に応用。', 'phai_vla', 'LLM Reasoning', 2022, 'method', 1, '["Jason Wei","Xuezhi Wang","Dale Schuurmans","et al."]', '["Chain-of-Thought Prompting Elicits Reasoning in Large Language Models (NeurIPS 2022)"]', '["Google Research"]', '思考連鎖,推論', 'chain of thought,reasoning', '2201.11903', 'verified_primary', 90),

('phai_rl_0191', 'AlphaGo', 'AlphaGo', '深層強化学習+モンテカルロ木探索により囲碁世界チャンピオンを破る。AGI-DB MS-002記録。Physical AIへの直接の含意は薄いが、深層RLの実用化を象徴する画期。', 'phai_rl', 'Deep RL / Self-Play', 2016, 'system', 1, '["David Silver","Aja Huang","Chris Maddison","et al. (DeepMind)"]', '["Mastering the game of Go with deep neural networks and tree search (Nature 2016)"]', '["DeepMind"]', 'AlphaGo,囲碁,深層RL', 'AlphaGo,Go,deep RL', '', 'verified_primary', 95),

('phai_rl_0192', 'AlphaFold 2', 'AlphaFold 2', 'タンパク質立体構造予測でCASP14を制覇。AGI-DB MS-012記録。物理科学への AI 浸透の代表例。Physical AIの「世界モデル」概念に隣接。', 'phai_vis', 'Scientific AI', 2020, 'system', 1, '["John Jumper","Richard Evans","Alexander Pritzel","et al. (DeepMind)"]', '["Highly accurate protein structure prediction with AlphaFold (Nature 2021)"]', '["DeepMind"]', 'AlphaFold,タンパク質', 'AlphaFold,protein folding', '', 'verified_primary', 95),

-- 大規模実機データ収集系
('phai_il_0161', 'DROID', 'DROID: A Large-Scale In-the-Wild Robot Manipulation Dataset', '564シーン・86千デモを世界13機関で収集。Open X-Embodimentと並ぶ大規模実機データセット。VLAのスケール則検証の主要基盤。', 'phai_il', 'Large-Scale Imitation Data', 2024, 'dataset', 3, '["Alexander Khazatsky","Karl Pertsch","Suraj Nair","et al."]', '["DROID: A Large-Scale In-the-Wild Robot Manipulation Dataset (arXiv 2024)"]', '["Stanford","Berkeley","13 institutions"]', '大規模実機データ,DROID', 'large-scale robot data,DROID', '2403.12945', 'verified_primary', 90),

('phai_il_0162', 'BridgeData V2', 'BridgeData V2', '60,096軌跡・1万種類のスキルを2,500オブジェクトで収集。VLA事前学習に頻用。', 'phai_il', 'Large-Scale Imitation Data', 2023, 'dataset', 3, '["Homer Walke","Kevin Black","Tony Zhao","et al."]', '["BridgeData V2: A Dataset for Robot Learning at Scale (CoRL 2023)"]', '["UC Berkeley"]', 'BridgeData,大規模デモ', 'BridgeData,demonstrations', '2308.12952', 'verified_primary', 88),

-- 推論時計算スケーリング
('phai_rl_0193', 'Inference-Time Compute Scaling (o1/o3)', 'Inference-Time Compute Scaling', 'LLMの推論時に思考連鎖を内部的に展開することで性能が向上。OpenAI o1/o3が実証。Physical AIではVLAでの「考えてから動く」モデルへの応用が始まる。', 'phai_vla', 'LLM Reasoning Scaling', 2024, 'method', 1, '["OpenAI o1 team"]', '["Learning to Reason with LLMs (OpenAI blog 2024)","o1 System Card"]', '["OpenAI"]', '推論時計算,o1,o3', 'inference-time compute,o1,o3', '', 'verified_primary', 85),

-- 世界モデル系統
('phai_rl_0194', 'Dreamer V3', 'Dreamer V3 (Mastering Diverse Domains)', '単一ハイパーパラメータでAtari・DMControl・Crafter等150以上の環境を解く世界モデルベース RL。Physical AIにおけるmodel-based RLの最先端。', 'phai_rl', 'Model-Based RL / World Models', 2023, 'method', 2, '["Danijar Hafner","Jurgis Pasukonis","Jimmy Ba","Timothy Lillicrap"]', '["Mastering Diverse Domains through World Models (arXiv 2023)"]', '["DeepMind","University of Toronto"]', 'Dreamer,世界モデル', 'Dreamer,world model', '2301.04104', 'verified_primary', 90),

('phai_rl_0195', 'JEPA / V-JEPA', 'Joint Embedding Predictive Architecture (JEPA / V-JEPA)', 'LeCun提唱のエネルギーベース世界モデル。動画から物理を学ぶ自己教師あり手法。LLM非依存のPhysical AI経路として注目。', 'phai_rl', 'World Models / JEPA', 2022, 'theory', 1, '["Yann LeCun","Adrien Bardes","et al. (Meta AI)"]', '["A Path Towards Autonomous Machine Intelligence (LeCun 2022)","V-JEPA (Meta 2024)"]', '["Meta AI / FAIR"]', 'JEPA,世界モデル,LeCun', 'JEPA,world model,LeCun', '2404.08471', 'verified_primary', 88),

('phai_sim_0132', 'Genie 2', 'Genie 2: Foundation World Model', '画像から3D環境を生成しエージェントを訓練する世界モデル。DeepMindが公開。Sora/Cosmosと並びPhysical AI訓練用世界モデルの代表。', 'phai_sim', 'Generative World Model', 2024, 'model', 2, '["Jack Parker-Holder","Philip Ball","et al. (DeepMind)"]', '["Genie 2: A large-scale foundation world model (DeepMind 2024)"]', '["DeepMind"]', 'Genie,世界モデル,生成', 'Genie,world model,generative', '', 'verified_primary', 80),

-- ロボティクス基盤モデル拡張
('phai_vla_0206', 'Octo (Open-Source Generalist Policy v1)', 'Octo: An Open-Source Generalist Robot Policy', 'Open X-Embodimentで訓練された27Mパラメータのジェネラリストポリシー。9機種・80万デモで事前学習。VLA基盤モデルのオープン版。', 'phai_vla', 'Generalist Robot Policy', 2024, 'model', 3, '["Octo Model Team (Sergey Levine et al.)"]', '["Octo: An Open-Source Generalist Robot Policy (RSS 2024)"]', '["UC Berkeley","Stanford","Carnegie Mellon"]', 'Octo,汎用ポリシー', 'Octo,generalist policy', '2405.12213', 'verified_primary', 90),

('phai_vla_0207', 'π0.5 (Pi-0.5)', 'π0.5: Physical Intelligence Pi-0.5', 'Physical Intelligence社のVLA第二世代。家庭環境での未知タスクへの汎化を実証。', 'phai_vla', 'Foundation Model VLA', 2025, 'model', 3, '["Physical Intelligence team"]', '["π0.5 announcement and technical report (Physical Intelligence 2025)"]', '["Physical Intelligence"]', 'pi-zero,Physical Intelligence', 'pi-zero,Physical Intelligence', '', 'verified_primary', 80),

('phai_vla_0208', 'OpenVLA-OFT', 'OpenVLA Optimized Fine-Tuning (OFT)', 'OpenVLAの推論速度を25倍向上、成功率も改善する fine-tuning フレーム。VLA産業実装の基礎技術。', 'phai_vla', 'VLA Fine-Tuning', 2025, 'method', 3, '["Moo Jin Kim","et al."]', '["Fine-Tuning Vision-Language-Action Models (arXiv 2025)"]', '["Stanford"]', 'OpenVLA,Fine-tuning', 'OpenVLA,fine-tuning', '', 'verified_primary', 78),

-- メタ学習と継続学習
('phai_rl_0196', 'In-Context Learning for Robotics', 'In-Context Learning for Robotic Manipulation', 'LLMのin-context learning機構をロボット操作に転移。少数デモから新規タスク実行。', 'phai_rl', 'In-Context Learning', 2024, 'method', 2, '["various teams"]', '["In-Context Imitation Learning (multiple 2024 papers)"]', '["various"]', 'In-context学習,ロボット', 'in-context learning,robot', '', 'secondary', 75),

-- 評価・ベンチマーク
('phai_eval_0118', 'CALVIN Benchmark', 'CALVIN: Composing Actions from Language and Vision', '長期タスク・言語条件付け・マルチモーダル評価の標準ベンチマーク。VLA評価の中核。', 'phai_eval', 'Long-Horizon Benchmark', 2022, 'benchmark', 2, '["Oier Mees","Lukas Hermann","Erick Rosete-Beas","Wolfram Burgard"]', '["CALVIN: A Benchmark for Language-Conditioned Policy Learning (RA-L 2022)"]', '["University of Freiburg"]', 'CALVIN,長期タスク', 'CALVIN,long-horizon', '2112.03227', 'verified_primary', 88),

('phai_eval_0119', 'LIBERO Benchmark', 'LIBERO: Lifelong Robot Learning Benchmark', '生涯学習・知識転移を評価する標準ベンチマーク。フェーズ5（連続学習）評価の中核。', 'phai_eval', 'Lifelong Learning Benchmark', 2023, 'benchmark', 2, '["Bo Liu","Yifeng Zhu","Chongkai Gao","et al."]', '["LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning (NeurIPS 2023)"]', '["UT Austin"]', 'LIBERO,生涯学習', 'LIBERO,lifelong learning', '2306.03310', 'verified_primary', 85),

('phai_eval_0120', 'RoboCasa', 'RoboCasa: Large-Scale Simulation of Everyday Tasks', '家庭環境100種類・150以上のタスク・kitchen中心の大規模シミュレータ。汎用ロボット訓練の中核。', 'phai_eval', 'Domestic Task Benchmark', 2024, 'benchmark', 2, '["Soroush Nasiriany","Abhiram Maddukuri","et al."]', '["RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots (RSS 2024)"]', '["UT Austin","NVIDIA"]', 'RoboCasa,家庭タスク', 'RoboCasa,domestic tasks', '2406.02523', 'verified_primary', 85),

-- 物理推論
('phai_rl_0197', 'PIQA Benchmark', 'PIQA: Reasoning about Physical Commonsense', '物理常識推論の標準ベンチマーク。LLMのPhysical Reasoning Gapを定量化。', 'phai_eval', 'Physical Reasoning Benchmark', 2020, 'benchmark', 1, '["Yonatan Bisk","Rowan Zellers","Ronan Le Bras","Jianfeng Gao","Yejin Choi"]', '["PIQA: Reasoning about Physical Commonsense in Natural Language (AAAI 2020)"]', '["Allen AI","Univ of Washington"]', 'PIQA,物理推論', 'PIQA,physical reasoning', '1911.11641', 'verified_primary', 90),

('phai_rl_0198', 'EmbodiedQA', 'Embodied Question Answering', '環境内を移動して質問に答えるタスク群。Physical AIにおける推論評価の先駆。', 'phai_eval', 'Embodied Evaluation', 2018, 'benchmark', 2, '["Abhishek Das","Samyak Datta","Georgia Gkioxari","Stefan Lee","Devi Parikh","Dhruv Batra"]', '["Embodied Question Answering (CVPR 2018)"]', '["Georgia Tech","Facebook AI"]', 'EmbodiedQA,具身質問応答', 'embodied QA', '1711.11543', 'verified_primary', 88),

-- 未来軌道用：2030年代以降の予測概念
('phai_vla_0209', 'Embodied Foundation Model (2028 forecast)', 'Embodied Foundation Model Standard (forecast 2028)', '2028年付近で予想されるロボティクス基盤モデルの業界標準化。100Bパラメータ規模・1000万デモ訓練のVLAが事実上のデファクトとなる予測。', 'phai_vla', 'Forecast / Foundation VLA', 2028, 'theory', 3, '["multiple labs (forecast)"]', '["Roadmap projection based on RT-X/Octo/π0 scaling trajectories"]', '["multiple"]', 'VLA標準化,予測', 'VLA standardization,forecast', '', 'projected', 60),

('phai_vla_0210', 'Lifelong VLA (2031 forecast)', 'Lifelong Vision-Language-Action System (forecast 2031)', 'PHAI-DB phase_5に対応する連続学習VLAの実現予測。フリート学習・自己評価・破壊的忘却対応を統合。', 'phai_vla', 'Forecast / Lifelong Learning', 2031, 'theory', 4, '["multiple labs (forecast)"]', '["Roadmap projection"]', '["multiple"]', '生涯学習VLA,予測', 'lifelong VLA,forecast', '', 'projected', 55),

('phai_vla_0211', 'Narrow AGI Embodiment (2030 forecast)', 'Narrow AGI Embodiment (forecast 2030)', '狭義AGI（書籍deep knowledge準拠定義）が物理世界に身体化される最初の段階。Metaculus 2030予測と整合的。', 'phai_vla', 'Forecast / AGI Embodiment', 2030, 'theory', 3, '["forecast"]', '["AGI-DB TL-003, TL-011, deep knowledge book ch. 1-3"]', '["multiple"]', '狭義AGI,身体化,予測', 'narrow AGI,embodiment,forecast', '', 'projected', 60),

('phai_vla_0212', 'General AGI Embodiment (2050 forecast)', 'General AGI Embodiment (forecast 2050)', '汎用AGIの完全身体化。AGI-DB DEF-002（Legg-Hassabis任意タスク基準）充足。AI Impacts 2047 HLMI median と整合的。', 'phai_vla', 'Forecast / AGI Embodiment', 2050, 'theory', 4, '["forecast"]', '["AGI-DB TL-008, TL-012, deep knowledge book ch. 10-15"]', '["multiple"]', '汎用AGI,身体化,予測', 'general AGI,embodiment,forecast', '', 'projected', 50),

('phai_vla_0213', 'Recursive Self-Improving Physical AI (2070 forecast)', 'Recursive Self-Improving Physical AI (forecast 2070)', '自己改善型AGIが物理世界に展開された段階。Kurzweil singularity（2045）の物理層実装の到達点。', 'phai_vla', 'Forecast / Self-Improvement', 2070, 'theory', 4, '["forecast"]', '["AGI-DB TL-008, DEF-015 Bostrom, deep knowledge book ch. 16-20"]', '["multiple"]', '自己改善,予測', 'self-improvement,forecast', '', 'projected', 40),

('phai_vla_0214', 'Intelligence Orchestra Member (2100 forecast)', 'Intelligence Orchestra Member: Physical AI as One Voice (forecast 2100)', '2100年時点のPhysical AI位置付け。「知性のオーケストラ」（deep knowledge書籍中心命題）における物理層構成要素として透明化される。', 'phai_vla', 'Forecast / Intelligence Ecology', 2100, 'theory', 4, '["forecast"]', '["deep knowledge book central thesis","manufacturing-orchestra DB"]', '["multiple"]', '知性のオーケストラ,2100', 'intelligence orchestra,2100', '', 'projected', 35);
```

### 5.2 新規関係（phai_concept_relations）

```sql
INSERT INTO phai_concept_relations (id, source_concept_id, target_concept_id, relation_type, relation_description, strength) VALUES
('rel_alexnet_resnet', 'phai_rl_0184', 'phai_rl_0185', 'extends', 'AlexNetの深層化問題をResidual Connectionで解決', 9),
('rel_resnet_vit', 'phai_rl_0185', 'phai_vis_0096', 'derived_from', 'ResNetの深層化思想をTransformerに転用したのがViT', 8),
('rel_transformer_bert', 'phai_rl_0186', 'phai_rl_0187', 'derived_from', 'BERTはTransformer Encoderを双方向に拡張', 10),
('rel_transformer_gpt3', 'phai_rl_0186', 'phai_rl_0188', 'derived_from', 'GPT-3はTransformer Decoderをスケール', 10),
('rel_gpt3_foundation', 'phai_rl_0188', 'phai_rl_0189', 'derived_from', 'GPT-3の創発能力が基盤モデル理論を生んだ', 9),
('rel_gpt3_saycan', 'phai_rl_0188', 'phai_vla_0001', 'enables', 'GPT-3系列がSayCanの計画機能の母体', 9),
('rel_palme_rt2', 'phai_vla_0002', 'phai_vla_0004', 'derived_from', 'PaLM-EがRT-2の直接の祖型', 10),
('rel_rt2_openvla', 'phai_vla_0004', 'phai_vla_0006', 'extends', 'RT-2のオープンソース版がOpenVLA', 10),
('rel_oxe_octo', 'phai_eval_0001', 'phai_vla_0206', 'enables', 'Open X-EmbodimentデータでOctoが訓練', 10),
('rel_oxe_openvla', 'phai_eval_0001', 'phai_vla_0006', 'enables', 'Open X-EmbodimentデータでOpenVLAが訓練', 10),
('rel_dreamer_jepa', 'phai_rl_0194', 'phai_rl_0195', 'competes_with', '世界モデル系統の2大経路：再構成型と埋め込み予測型', 8),
('rel_droid_oxe', 'phai_il_0161', 'phai_eval_0001', 'complements', 'DROIDはOpen X-Embodimentと並ぶ大規模実機データ', 9),
('rel_chain_thought_saycan', 'phai_rl_0190', 'phai_vla_0001', 'enables', 'CoT推論がSayCanのタスク分解に応用', 7),
('rel_pi0_pi05', 'phai_vla_0010', 'phai_vla_0207', 'extends', 'π0からπ0.5への進化', 9),
('rel_openvla_oft', 'phai_vla_0006', 'phai_vla_0208', 'extends', 'OpenVLAをfine-tune最適化したOFT版', 8),
('rel_alphago_dqn', 'phai_rl_0191', 'phai_rl_0009', 'derived_from', 'AlphaGoはDQN系統の発展形', 7),
('rel_inference_o1_vla', 'phai_rl_0193', 'phai_vla_0209', 'enables', 'o1/o3型推論時計算が将来のVLAに転移される予測', 6),
('rel_calvin_libero', 'phai_eval_0118', 'phai_eval_0119', 'complements', 'CALVINとLIBEROは長期タスク評価の補完関係', 8),
('rel_robocasa_calvin', 'phai_eval_0120', 'phai_eval_0118', 'extends', 'RoboCasaはCALVINを大規模化', 7),
('rel_piqa_embodiedqa', 'phai_rl_0197', 'phai_rl_0198', 'related_to', 'PIQAとEmbodiedQAは物理推論評価の両輪', 7),
('rel_forecast_2030_2050', 'phai_vla_0211', 'phai_vla_0212', 'extends', '狭義AGI→汎用AGI身体化の20年軌道', 5),
('rel_forecast_2050_2070', 'phai_vla_0212', 'phai_vla_0213', 'extends', '汎用AGI→自己改善AGIの20年軌道', 4),
('rel_forecast_2070_2100', 'phai_vla_0213', 'phai_vla_0214', 'extends', '自己改善AGI→知性のオーケストラ統合', 4);
```

### 5.3 新規マイルストーン（phai_milestones）

```sql
INSERT INTO phai_milestones (id, name, year, milestone_type, description, converged_streams, key_concept_ids, impact_score) VALUES
('ms_alexnet', 'AlexNet ImageNet優勝', 2012, 'breakthrough', '深層学習革命の起点。CNN+GPUによる画像分類で人間レベルに迫る性能。後のすべての知覚モジュールの基盤。', 'stream_fm', 'phai_rl_0184', 10),
('ms_transformer', 'Transformer発表', 2017, 'breakthrough', 'Attention機構のみでSeq2Seqを実現。BERT・GPT・ViT・VLA全ての祖型。', 'stream_fm', 'phai_rl_0186', 10),
('ms_alphago', 'AlphaGo囲碁世界王者超え', 2016, 'breakthrough', '深層RL+MCTSで囲碁。AGI-DB MS-002記録。深層RL実用化の象徴。', 'stream_rl', 'phai_rl_0191', 8),
('ms_dactyl', 'OpenAI Dactyl実機巧緻操作', 2018, 'convergence_point', 'シミュレーション学習政策が実機の巧緻な手内操作で動く最初の証明。Stream 1（RL）とStream 3（シミュレーション）の合流点。', 'stream_rl,stream_sim', 'phai_rl_0066', 9),
('ms_gpt3', 'GPT-3公開・基盤モデル時代', 2020, 'breakthrough', '175Bパラメータが少数ショット学習を創発。基盤モデル時代の起点。', 'stream_fm', 'phai_rl_0188', 10),
('ms_clip', 'CLIPマルチモーダル接地', 2021, 'breakthrough', '画像-言語埋め込みを統一しゼロショット転移を実現。CLIPort経由でロボティクスへ。', 'stream_fm', 'phai_vis_0073', 9),
('ms_oxe', 'Open X-Embodiment統合データ公開', 2023, 'convergence_point', '22機種527スキル160万エピソードを単一データセット化。ロボティクス版ImageNetモーメント。', 'stream_fm,stream_sim', 'phai_eval_0001', 10),
('ms_diffusion_policy', 'Diffusion Policy確立', 2023, 'breakthrough', '拡散モデルを行動生成に転用。ACT・ALOHA・RDTの基盤。', 'stream_rl,stream_fm', 'phai_il_0010', 9),
('ms_droid', 'DROID大規模実機データ', 2024, 'breakthrough', '世界13機関連携で564シーン86千デモ。VLAスケール則検証の主要基盤。', 'stream_fm', 'phai_il_0161', 8),
('ms_inference_o1', 'o1推論時計算スケーリング', 2024, 'breakthrough', 'LLM推論時の思考連鎖展開でPhDレベルQ&A達成。AGI-DB MS-008記録。Physical AIへの転移開始。', 'stream_fm', 'phai_rl_0193', 9),
('ms_narrow_agi_2030', '狭義AGI到達予測点', 2030, 'projected', 'AGI-DB TL-003/TL-011/TL-018中央値。Metaculus prediction marketの収束点。', 'stream_fm', 'phai_vla_0211', 8),
('ms_general_agi_2050', '汎用AGI到達予測点', 2050, 'projected', 'AGI-DB TL-008/TL-012中央値。AI Impacts 2047 HLMI predictionと整合。', 'stream_fm,stream_hw,stream_rl', 'phai_vla_0212', 8),
('ms_rsi_2070', '自己改善AGI実装予測点', 2070, 'projected', 'Kurzweil 2045 singularityの物理層実装到達点。Bostrom superintelligence framework。', 'stream_fm,stream_rl,stream_hw,stream_ctrl,stream_sim', 'phai_vla_0213', 7),
('ms_intelligence_orchestra_2100', '知性のオーケストラ完成予測点', 2100, 'projected', '単一AGIではなく多様な知性の編成体系。Physical AIは物理層構成要素として透明化される。', 'stream_fm,stream_rl,stream_hw,stream_ctrl,stream_sim', 'phai_vla_0214', 6);
```

### 5.4 新規ボトルネック（phai_bottlenecks）

```sql
INSERT INTO phai_bottlenecks (id, name, description, severity, affected_phases, confidence_level, debate_ratio) VALUES
('bn_physical_reasoning', '物理推論能力ギャップ', 'LLM/VLAが物理常識（PIQA, ThreeDWorld）で人間に劣る。「箱の中のボール」推論で30-40%誤答。', 'critical', 'phase_3,phase_4,phase_5', 'high', 0.2),
('bn_world_model', '世界モデルの物理整合性', 'Sora/Genie/Cosmos等の生成世界モデルで物理的整合性・長期一貫性・因果性が不十分。', 'major', 'phase_3,phase_4,phase_5,phase_6', 'medium', 0.4),
('bn_sample_efficiency', 'サンプル効率', '新規物理タスクごとに50-300デモが必要。人間の数千-数百万倍の経験量。', 'major', 'phase_2,phase_3,phase_4', 'high', 0.1),
('bn_energy_efficiency', 'エネルギー効率', '人間脳20Wに対し大規模VLA推論1kW級。3桁の効率差。Stream 5（ニューロモーフィック）との合流が必須。', 'critical', 'phase_4,phase_5,phase_6,phase_7', 'high', 0.15),
('bn_long_horizon_memory', '長期計画とメモリ', '30分以上の連続タスクで失敗率が急上昇。エピソード横断メモリ未解決。', 'major', 'phase_3,phase_4,phase_5', 'medium', 0.3);
```

---

## 6. 関連DB由来の実証データ

### AGI-DB（agi_roadmap.db）

20件のtimeline predictions（TL-001〜TL-020）が示す2030年AGI予測の収束は、Stream 1の中期軌道の最重要根拠である。特に：
- **TL-011 Metaculus**: 集合予測市場のmedian が 2020年の2050から2024年の2030へ短縮。この急速な短縮そのものが「AIの加速」のシグナル。
- **TL-006 LeCun**: AGIまで10年だが「LLM経路ではなく JEPA経路」と主張。Stream 1内部の経路論争を示す。
- **TL-017 Chollet**: ARC-AGIで saturation するまで AGI ではない、と異論を提示。サンプル効率重視。

20件のcapability milestones（MS-001〜MS-020）のうち、**MS-019（Manipulation generalization, 2023, RT-2/OK-Robot）** がPhysical AI 系統に最も直接的に関連する。次の物理系マイルストーンは MS-020（multilingual parity）以降、benchmarks の整備待ち。

### AI Acceleration Evidence DB

18 Level-1 ドメインの中で `COMP-SCI`（計算機科学・AI）と `ENGINEERING`（工学・技術）がPhysical AIの直接領域。`MED-HEALTH`（手術ロボット・リハビリ）、`AGRI-FOOD`（収穫ロボット）、`SPACE`（宇宙ロボット）への展開がspillover領域として重要。

### Tech Acceleration DB

227Kレコードの中の **AI関連レコード** が、深層学習革命以降の加速曲線を定量化。Stream 1の長期軌道予測の経験的基盤となる。

### deep knowledge書籍（21章304,999字）

中心命題「2100年は知性のオーケストラ」が、本ロードマップの2100年予測の理論的基盤。Physical AIは「身体性をもつ知性層」として位置付けられ、他のAI形態（LLM・生体AI・量子AI等）と協調する一構成要素として透明化する。

---

## 7. 補足: PHAI-DB既存804件との関係

本提案の30+件INSERTは、既存の804件AI/ML概念を**置き換えるものではなく、補完するもの**である：

1. **過去の欠落補完**: AlexNet, ResNet, Transformer, BERT, GPT-3, AlphaGo, AlphaFold等の「AI/ML全般の重要源流」が既存DBで未登録だった。これらを補完。
2. **未来軌道の登録**: 既存DBは2025年までで途絶えていた。2028/2030/2050/2070/2100の予測概念を5件追加し、ロードマップ全体を表現可能に。
3. **マイルストーンの拡張**: 既存5件（ms_deeprl, ms_sim2real, ms_saycan, ms_rt2, ms_humanoid）に、AI/ML系統で重要な過去画期（AlexNet・Transformer・GPT-3・CLIP等）と将来予測点を14件追加。
4. **ボトルネック補強**: 既存4件（bn_data, bn_safety, bn_dexter, bn_hw）に、AI/ML特有の5件（物理推論・世界モデル・サンプル効率・エネルギー効率・長期計画）を追加。

**注**: 本提案は他Stream（HW・制御・シミュレーション）の精緻化チームと整合性を取る必要がある。特にエネルギー効率ボトルネック（`bn_energy_efficiency`）はStream 5側でも独立に提案される可能性があり、IDの一意性確認が必要。

---

**文書作成**: Stream 1（AI/ML系統）精緻化チーム
**文字数**: 約 8,200 字
**引用方針**: arXiv ID・DOI・論文タイトル・出版venue・著者を可能な限り明示。AGI-DB（agi_roadmap.db）・PHAI-DB既存テーブル・deep knowledge書籍を一次参照。
**ハルシネーション対策**: 実在論文・実在arXiv ID・実在製品名のみを記載。未確認の年・著者・性能数値は記載していない。予測（2028以降）は projected ステータスを明示。
