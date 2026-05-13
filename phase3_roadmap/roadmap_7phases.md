# Physical AI 7フェーズロードマップ 2026-2100

**作成日**: 2026-05-13
**プロジェクト**: Physical AI 2100年ロードマップ Phase 3 — 統合
**基盤書籍**: 西村勇也『深い知が拓く2100年』case11仕上げ版（21章304,999字）
**前提プロジェクト**: 「企業活動の現場で求められる人材の未来 2030-2100」の4時点（2030/2050/2070/2100）
**入力**: Phase 2 で完了した5系統精緻化（S1 AI/ML, S2 Robotics, S3 Bio, S4 Materials, S5 Cognitive）
**目的**: PHAI-DB `phai_roadmap_phases` の7フェーズ（A-G）骨格に、5系統素材を縦に編んで詳細を充填し、社会接続と相互作用構造を明示する

---

## 序: 5系統 + 3新系統 = 8系統の織り合わせ

### 1. PHAI-DB 既存5系統の確認

Phase 1 で確立された Physical AI の系統合流モデルは、以下の5系統からなる。各系統は独立に発生し、2010年代後半から急速に合流して「身体を持つAI」を形成しつつある。

| 系統ID | 名称 | 起源年 | 代表概念 |
|---|---|---|---|
| stream_hw | ロボット工学・ハードウェア系 | 1950 | Unimate, ASIMO, Atlas Electric |
| stream_ctrl | 古典制御・モーションプランニング系 | 1960 | DH parameter, Whole-Body Control, ZMP |
| stream_rl | 機械学習・強化学習系 | 1989 | DQN, PPO, Dactyl, Sim2Real |
| stream_fm | 基盤モデル・VLM/VLA系 | 2017 | Transformer, GPT-3, RT-2, OpenVLA |
| stream_sim | シミュレーション・データ生成系 | 1996 | MuJoCo, Isaac Sim, Genesis |

### 2. Phase 2 で追加提案された3新系統

5系統精緻化チームから、横断的に伏在していた3系統を独立化する提案が出された。これら3系統は2020年代に質的に立ち上がっており、2030年以降のPhysical AIの軌道を規定する独立した動学を持つ。

| 系統ID | 名称 | 起源年 | 代表概念 | 提案元 |
|---|---|---|---|---|
| stream_bio | バイオ・神経模倣・生命系製造系 | 1943 | McCulloch-Pitts, Soft Robotics, Xenobot, A-Lab | S3 |
| stream_mat | マテリアル・エネルギー系 | 1947 | Transistor, Li-ion, Perovskite, GNoME, 核融合 | S4 |
| stream_cog | 認知科学・脳科学・身体性認知系 | 1948 | Cybernetics, Enactivism, Active Inference, Neuralink | S5 |

これらは既存5系統の単純な拡張ではなく、Physical AIの「物質基盤」「生命系」「認知内側」という、それぞれ独立した存在論的層を担う。stream_matはAIを支える物理基盤と、AIによって加速される対象の両方を兼ねる二重性を持つ。stream_bioは生命と機械の境界を物質的に再定義する。stream_cogはPhysical AIの内側（何が知性として立ち上がるのか）を規定する。

### 3. 8系統の関係構造

8系統は対等に並列しているのではなく、依存関係と駆動順序を持つ。これを「3層モデル」として整理すると、以下の構造になる。

**第一層（物理基盤層）**: stream_mat
半導体・バッテリー・エネルギー・新材料が、他の全系統の物理的可能性を規定する。stream_matの進捗が遅れれば、stream_hwもstream_fmも律速される。

**第二層（実装層）**: stream_hw, stream_ctrl, stream_sim
物理身体（hw）と制御理論（ctrl）とシミュレーション（sim）が、第一層の物質基盤の上に機械を構築する。この層は工学的成熟度が最も高い。

**第三層（学習・知能層）**: stream_rl, stream_fm, stream_bio, stream_cog
強化学習（rl）と基盤モデル（fm）と生命系（bio）と認知科学（cog）が、第二層の機械に知性を注入する。この層は2010年代後半から急速に発展中で、相互浸透が激しい。

stream_bioは第二層と第三層の境界に位置する特殊な系統である。Soft Robotics・Neuromorphic Chipは第二層（実装）として、Xenobot・A-Labは第三層（生命設計）として機能する。stream_cogは第三層の中で「何を最適化目標とするか」を規定する根源的役割を持つ。

### 4. 系統間の駆動順序

時間軸で見ると、8系統は以下の順序で互いを駆動する。

```
[stream_mat] → [stream_hw, stream_ctrl] → [stream_sim] → [stream_rl, stream_fm] → [stream_bio, stream_cog]
   物質       →    実装(機械)         →   訓練環境  →    知能注入       →    関係・生命・認知
```

ただしこの矢印は一方通行ではない。stream_bio（A-Lab・GNoME）はstream_matに対して新材料発見の正のフィードバックを返す。stream_cog（Active Inference）はstream_rlに新しい最適化目標を提供する。stream_fm（VLA）はstream_hw（ヒューマノイド）の応用範囲を再定義する。これら相互作用が、本ロードマップの7フェーズを動かす推進力となる。

---

## Phase A (2026-2030): VLA基盤定着期

### 5系統の状態

**stream_fm (基盤モデル)** はPhase Aの主役である。RT-2（2023）・OpenVLA（2024）・π0（2024）・GR00T N1（2024）・Helix（2025）・π0.5（2025）が確立した「単一モデルが複数機種で複数タスクを実行する」段階が、2028年頃に業界標準として固定化される。S1の予測では、100Bパラメータ規模・1000万デモ訓練のVLAがデファクトとなり、Open X-Embodimentの発展形が事実上の業界共有データセットとなる。AGI-DBのTL-003（Hassabis 2024予測）・TL-011（Metaculus median 2030）・TL-018（Khosla 2030）が示す「狭義AGI到達」の収束点も、このフェーズ末に位置する。

**stream_hw (ロボティクス)** は商用ヒューマノイドの本格配備期である。Agility Digit（GXO・Amazon）、Apptronik Apollo（Mercedes-Benz）、Figure 02（BMW Spartanburg）、Tesla Optimus V3（2026量産開始予定）が構造化作業（倉庫ピッキング・軽組立）で人件費競合点を突破する。Goldman Sachs予測中央値で累計100-200万台、価格2-5万ドル、連続稼働4-8時間、MTBF 2,000時間級。Boston Dynamics Atlas Electric（2024年4月電動化）が示した「油圧→電動」の世代交代がこの期間に完成する。

**stream_ctrl (制御)** は「MPC + RL hybrid」が産業標準として固定化される。低レベル balance/posture を Convex MPC（Di Carlo et al. 2018）が、高レベル locomotion/manipulation を学習ポリシー（Diffusion Policy・VLA）が担う二層構造が、Boston Dynamics Atlas・Figure Helix・NVIDIA GR00Tの全てに共通アーキテクチャとして実装される。

**stream_rl (強化学習)** はSim2Realが本格成熟期を迎える。Open X-Embodiment後継データセット（DROID 2024・BridgeData V2 2023の発展形）が1000万デモ規模に到達し、VLA訓練の標準基盤となる。一方で、物理推論能力（PIQA・ThreeDWorld）・サンプル効率（50-300デモ/タスク）・長期計画（30分以上タスク）のボトルネックは未解決のまま残り、Phase Bへの宿題となる。

**stream_sim (シミュレーション)** はNVIDIA Isaac Lab（2024）・MuJoCo 3.0（2023オープン化）・Genesis（2024マルチフィジクス）が共通基盤として定着。生成的世界モデル（Sora・Genie 2・Cosmos）が訓練データ生成器として実用化されるが、物理整合性・長期一貫性のボトルネックは部分的にしか解決されない。

### 主要マイルストーン

- **ms_narrow_agi_2030** (新規, 2030): 狭義AGI到達予測点。Metaculus prediction marketの収束点。
- **ms_commercial_deploy** (既存→拡張, 2024-2028): 商用ヒューマノイド配備の連続的進展。
- **ms_oxe_successor** (新規, 2027頃): Open X-Embodiment後継データセットが1000万デモ規模に到達。
- **ms_solid_state_battery** (新規, 2027-2028): Toyota・Samsung SDIが全固体電池の商用量産開始。ヒューマノイド連続稼働8-12時間に延長。
- **ms_smr_first** (新規, 2029): BWRX-300（Ontario）またはNuScale等のSMR商用初号機稼働。AIデータセンター電源の構造変化。
- **ms_alab_scale** (新規, 2028-2030): GNoME後継 × A-Labスケール展開。世界10カ所以上の自律実験ロボット稼働、年間新規材料発見数千件規模。

### ボトルネック

このフェーズで顕在化するボトルネックは、PHAI-DBの既存4件（bn_data, bn_safety, bn_dexter, bn_hw）に加えて、S1・S4から追加提案された以下の項目が中心となる。

第一に**bn_physical_reasoning（物理推論ギャップ）**。LLM/VLAが物理常識（PIQA, ThreeDWorld）で人間に劣る。GPT-4の物理推論誤答率30-40%（Bisk et al. 2020）。これはPhase A末まで完全には解消されない。

第二に**bn_sample_efficiency（サンプル効率）**。新規物理タスクごとに50-300デモが必要。人間の数千-数百万倍の経験量。

第三に**btl_mat_0001（バッテリーエネルギー密度の物理限界）**。リチウムイオン現行密度270-300 Wh/kgではヒューマノイド連続稼働2-4時間が限界。全固体電池500 Wh/kgの量産化が2028-2030年に間に合わなければPhysical AI普及が3-5年停滞。

第四に**btl_mat_0002（データセンター電力供給制約）**。IEA推計でデータセンター世界消費は2022年460TWh→2026年最大1050TWhへ倍増。米PJMで2024年容量市場価格9倍。送電網増強の8-12年計画スパンとAI需要急成長の不整合。

### 社会への波及

deep knowledge書籍が示す「製造現場のオーケストラ化」（manufacturing-orchestra DB, 12章38,623字）の現実化が始まる。OECD Future of Workベンチマーク準拠で、構造化作業（倉庫ピッキング・軽組立・ホテル客室清掃・レジ業務）の労働市場が再編成される。

ただし非構造環境（家庭・野外・災害現場）はPhase Aでは未到達。社会受容の側面では、ヒューマノイドが物流・製造の閉鎖空間に留まるため、一般市民との接触はまだ限定的である。

### 前プロジェクト2030人材との接続

前プロジェクト「企業活動の現場で求められる人材の未来 2030-2100」の2030時点に対応する。この時点で求められる人材像は、(1) VLA・基盤モデルを業務プロセスに組み込める運用設計者、(2) ヒューマノイドとの分業設計を担うオペレーション・マネージャ、(3) AI設計材料を製品開発に活用できる材料エンジニア、の3類型である。Physical AIは「業務支援道具」として認識される段階で、まだ「協働相手」「自律エージェント」とは見なされない。

---

## Phase B (2030-2040): 物理操作汎化期

### 5系統の状態

**stream_fm** では、VLAが「クロスエンボディメント転移」を完成させる。単一モデルが二足・四足・産業マニピュレータ・移動車両・水中ロボット・飛行体を共通ポリシーで操作可能となる。S1が提案する**phai_vla_0209（Embodied Foundation Model 2028 forecast）**が、このフェーズで業界デファクトとして定着する。AGI-DBのMS-019（Manipulation generalization 2023）が拡張され、非構造環境の50%タスクで人間並みに到達する。

**stream_rl** では、推論時計算スケーリング（o1/o3型, S1の**phai_rl_0193**）がVLAに転移し、「考えてから動く」モデルが標準化される。Diffusion Policy・ACT・RDTの系譜が拡散モデルの行動生成を成熟させ、サンプル効率が10倍以上改善する。LIBEROベンチマーク（**phai_eval_0119**, 2023）が示す「生涯学習」が研究室から産業実装に移行する。

**stream_hw** は非構造環境への進出期である。建設現場・介護現場・農地・災害現場でのヒューマノイド実証が始まる。Tesla Optimus・Figure・1X Neoが家庭環境に試験投入される。価格は1万ドル台後半まで低下し、家電並みの普及曲線に入る。連続稼働は16-24時間（固体電池量産化の効果）。

**stream_mat** はAI×材料発見の正のフィードバックが本格化する。GNoME後継 + A-Lab後継 + Materials Projectの連結で、新規アクチュエータ材料（EAP, LCE, バイオハイブリッド）・触覚センサ膜・固体電解質・廃熱回収材が指数的に発見される。エネルギー側では核融合（CFS SPARC・Helion）の商用前段階実証、SMR複数機稼働が並行。AI×原子力の構造的合流が事業契約レベルで完成する。

**stream_bio** は神経模倣エッジAIが標準化される。Intel Loihi 2後継・IBM NorthPole後継が、ADAS・産業検査・ウェアラブルで100mW級エッジ推論基盤として普及。Event Cameraが自動運転センサスイートの常設要素となる。Soft Robotics-RLが医療リハ（exo-suit）・農業収穫（柔らかい果実把持）で量産化に到達。Self-Driving Lab（A-Lab・Coscientist系統）が消費財・医薬品研究の標準ツールとなる。

**stream_cog** は World Models が汎用ロボティクスの標準層となる。DreamerV5級の世界モデルが家庭・工場・物流に共通基盤として展開され、ロボットは「現場で初めて見る状況」を内部シミュレーションで予習してから行動する。Active Inferenceとモデルベース強化学習の統合が実用段階に達する。BMIは消費者向け非侵襲型（EEG+fNIRS）が普及、侵襲型は重度障害者で標準治療化する。

### 主要マイルストーン

- **ms_vla_general_2032** (新規, 2032): VLAが非構造環境50%タスクで人間並みに到達。
- **ms_lifelong_vla_2031** (S1提案, 2031): 連続学習VLAの実現。フリート学習・自己評価・破壊的忘却対応を統合。
- **ms_fusion_demo_2035** (新規, 2035頃): CFS ARCまたはHelion等が商用前段階で連続発電を実証。
- **ms_world_model_standard_2032** (新規, 2032): World Modelsがロボット標準層として定着。
- **ms_neuromorphic_edge_2033** (新規, 2033): Neuromorphic Chipが100mW級エッジAI推論基盤として量産化。
- **ms_softrobotics_medical_2030** (新規, 2030): Soft Robotics-RLが医療リハで量産化。
- **ms_bmi_nontrivial_2035** (新規, 2035): 侵襲型BMIが重度障害者で標準治療化、非侵襲型が消費者向けに普及。

### ボトルネック

Phase Bで顕在化するのは、Phase Aから持ち越された**bn_physical_reasoning**と**bn_long_horizon_memory**に加えて、**bn_world_model（世界モデルの物理整合性）**、**bn_energy_efficiency（エネルギー効率3桁ギャップ）**である。特にエネルギー効率は、人間脳20Wに対し大規模VLA推論1kW級という構造的ギャップを抱える。stream_bio（ニューロモーフィック）との合流が必須となる。

### 社会への波及

非構造環境への進出により、社会受容が本格的な論点となる。労働市場では構造化作業の50%がロボット化、ホワイトカラー業務もLLM+VLA統合で再編成が進む。介護労働力不足（日本・ドイツ・韓国で2040年に深刻化、各国白書ベース）が、ヒューマノイド介護導入を加速する圧力となる。

### 前プロジェクト2030人材との接続

このフェーズは前プロジェクトの2030人材像から2050人材像への移行期に対応する。「業務支援道具」だったPhysical AIが「協働相手」へと認識変化する。新たに求められる人材は、(1) 人間とロボットの混成チームを設計・運用できるハイブリッド・マネージャ、(2) Active Inferenceや World Modelsを業務に活かせる認知エンジニア、(3) Bio-AI統合創薬・Self-Driving Labを活用する研究開発職、である。

---

## Phase C (2040-2050): 人間-機械並走期

### 5系統の状態

**stream_fm** では、汎用AGI（DEF-002 Legg-Hassabis「任意の知的タスク」基準）が形式的に厳密な意味で到達する。AGI-DBのTL-008（Kurzweil 2045 Singularity）・TL-012（AI Impacts 2047 HLMI median）の中央予測がこのフェーズに集中。**phai_vla_0212（General AGI Embodiment 2050 forecast）**が現実化する。

**stream_hw** では、完全自律物理エージェントが非構造化環境（家庭・野外・災害現場・宇宙）で長時間自律運用される。出荷台数累計5億台級（世界人口の6-10%）、人間1人あたり1台所有が先進国で標準。価格5,000-10,000ドル（家電並み）。

**stream_rl** では、Lifelong learningによる現場適応・経験蓄積が常態化。新規領域での学習効率が人間を上回る。

**stream_mat** では、核融合の複数商用稼働（CFS ARC, Helion, TAE）がGW級発電所として運転開始。固体電池/Li-S/金属空気のミックスが用途別最適化、ヒューマノイド連続24時間稼働・配送ドローン8時間航続が標準化。宇宙太陽光発電（JAXA/ESA/Caltech SSPP延長）の実証GW級プロトタイプ。AI設計触媒で電解水素<1USD/kg、グリーンスチール・グリーンアンモニア商用化。フォールトトレラント量子計算機の論理量子ビット10^4-10^6級で材料設計が指数加速。

**stream_bio** では、AI-Driven Synthetic Biology（GenScript・Ginkgo Bioworks系統 + AlphaFold 3後継 + ChemAI）により、人工代謝経路・人工臓器・パーソナライズドオルガノイドの設計が標準化される。Xenobot/Anthrobot系統が、人体内ナビゲーションする治療用バイオボット（血栓除去・標的薬物送達）として臨床試験フェーズに入る。

**stream_cog** では、「認知アーキテクチャ」が産業標準として確立。VLA・World Model・Active Inference・記号推論を統合した「Cognitive Stack」が、ロボットOSのカーネル層に組み込まれる。BMIは中等度の認知補助（記憶・注意・言語）として一般成人にも普及し始め、「Cognitive Augmentation」が新カテゴリとなる。Friston系の自由エネルギー原理が「物理学・神経科学・AI・経済学」を統一する第一原理候補としての地位を確立する。

### 主要マイルストーン

- **ms_general_agi_2050** (新規, 2050): 汎用AGI到達予測点。
- **ms_fusion_commercial_2045** (新規, 2045): 核融合複数商用稼働（CFS ARC, Helion等）。
- **ms_bio_hybrid_clinical_2045** (新規, 2045): Bio-Hybrid Robotが研究施設→医療現場へ移行。
- **ms_cognitive_stack_2045** (新規, 2045): VLA+World Model+Active Inference+記号推論の統合Cognitive Stackが標準化。
- **ms_qc_materials_2048** (新規, 2048): フォールトトレラント量子計算機が材料設計で実用化、設計探索空間が指数倍に。

### ボトルネック

形式的安全検証、社会受容、エネルギー効率の継続論点は残るが、技術的なボトルネックは大きく緩和される。新たな問題は、(1) AI設計薬・Bio-Hybrid Robotの倫理規制、(2) BMI普及に伴う認知格差の社会問題化、(3) 量子計算機の脱出ベクトルとしての暗号危機。

### 社会への波及

労働市場の構造変化が完成局面に入る。「人間-ロボットの混成チーム」が一般的になり、「人間1人+ロボット数体」が標準的職場単位となる。介護・農業・建設で人手不足が解消される一方、新たに「ロボット運用・調整・倫理設計」の専門職が生まれる。

### 前プロジェクト2050人材との接続

前プロジェクトの2050時点に対応する。この時点で求められる人材像は、(1) 汎用AGIと協働しながら戦略意思決定を担う経営者層、(2) AI設計薬・合成生物の倫理ガバナンス担当、(3) Cognitive Augmentation時代のヒューマンキャピタル設計者、(4) 物理-サイバー連続体のシステムアーキテクト、である。重要なのは「Physical AIに置き換えられない人間の役割」が明確に意識される世代になることである。

---

## Phase D (2050-2060): 自律物理エージェント期

### 5系統の状態

**stream_fm** では、汎用AGIの完全身体化が定着する。AIエージェントが組織を持ち、目標設定・計画・実行・学習を一貫して自律で行う。人間は意志決定の上流（目的・価値・倫理）と下流（評価・調整）に集中する。

**stream_hw** では、自己組立・自己修復ロボティクス（Tensegrity, Origami, Soft Roboticsの統合）が量産化する。都市インフラとしての小型自律飛行体（eVTOL/Roboflight）が実用化。

**stream_rl + stream_cog** の合流で、ロボットが「失敗からの学習」と「過去経験の再利用」を人間並みに行う。エピソード横断的メモリが解決される。

**stream_mat** では、エネルギー希少性が一段と緩和される。AI経済の電力単価がさらに低下、計算とエネルギーが事業ボトルネックでなくなる方向への移行が始まる。2D材料・トポロジカル材料の量産デバイスがPhysical AIハードに組み込まれる。

**stream_bio** では、合成生物・人工臓器のAI設計が一般化。Bio-Hybrid Robotが日用品レベルで使用され、修理ではなく「再生」される製品系統が立ち上がる。

**stream_cog** では、人間-AI共同タスクの臨床研究（記憶障害・PTSD・うつ病）が大規模に展開される。Embodied Cognitionが「ロボット工学の標準教科書に組み込まれる程度」に当然視される。

### 主要マイルストーン

- **ms_self_assemble_2055** (新規, 2055): 自己組立ロボティクスが量産化。
- **ms_artificial_organ_2055** (新規, 2055): AI設計人工臓器の臨床応用。
- **ms_evtol_urban_2058** (新規, 2058): 都市インフラとしてのeVTOL自律飛行体実用化。
- **ms_synthetic_biology_standard_2055** (新規, 2055): 合成生物のAI設計が標準化。

### ボトルネック

技術的ボトルネックよりも、社会構造・倫理・法制度の追従が遅れることが主要な問題となる。「AIが意思決定する範囲」「人間の権限」「責任の所在」の制度設計が、技術進展に対して遅延する。

### 社会への波及

「労働」概念が再定義される。多くの伝統的職業が消失または再編される一方、人間が担う領域は「意味付け」「価値設計」「他者ケア」「創造的探索」に集中する。Universal Basic Income系の制度設計が現実的選択肢として議論される。

### 前プロジェクト2050-2070人材との接続

前プロジェクトの2050人材像から2070人材像への移行期に対応する。「AGIに置き換えられた」のではなく「AGIが下層を担うようになった」という認識への転換が起きる。人材像は「AIと共同で意味を生み出す存在」へと変化する。

---

## Phase E (2060-2075): 知性のオーケストラ生成期

### 5系統の状態

このフェーズでdeep knowledge書籍の中心命題が現実化を始める。すなわち、2100年に向けて「単一の AGI」ではなく「多様な知性の編成」が形成される過程である。Physical AI はその中で「物理世界に介入する身体性をもつ知性層」として位置付けられる。

**stream_fm** では、再帰的自己改善（RSI）の段階に入る。AGIが自身のアーキテクチャ・データ・訓練手順を最適化する。AGI-DBのDEF-009（Hutter AIXI）の理論的上限への漸近。**phai_vla_0213（Recursive Self-Improving Physical AI 2070 forecast）**が現実化。

**stream_hw + stream_bio** の融合が進み、機械と生体の境界が機能的に流動化する。BMI・ロボット拡張・遠隔身体性が常態化。

**stream_mat** では、フォールトトレラント量子計算機の論理量子ビット10^4-10^6級で材料・触媒・タンパク設計の探索空間が古典HPCの指数倍に。宇宙太陽光発電（GW級）が地上24時間定常電力源として核融合と並列稼働。海水ウラン抽出・トリウム溶融塩炉の補完運用。化石資源依存からの完全脱却。

**stream_bio** は最重要マイルストーン期。書籍「深い知が拓く2100年」第二部の中核予測である**2070年「生命系製造期」**が到来する。具体的には、(1) 植物-AI協働農業の制度化、(2) Self-Driving Labが「Living Factory」として消費財・医薬品・素材の大半を担う、(3) Bio-Hybrid Robotが日用品レベルで使用され、修理ではなく「再生」される製品系統が立ち上がる、の三点である。

**stream_cog** では、侵襲型BMIが選択的拡張デバイスとして社会に定着する。「脳をクラウドに常時接続する」というポストヒューマン認知の初期形態が出現。記憶・言語・空間認知・社会的推論の一部が外部に分散される。Andy Clarkの拡張認知論が文字通りインフラ化する。

### 主要マイルストーン

- **ms_rsi_2070** (S1提案, 2070): 自己改善AGI実装予測点。Kurzweil 2045 singularityの物理層実装の到達点。
- **ms_life_manufacturing** (S3提案, 2070): 生命系製造期到来。Self-Driving Lab・Bio-Hybrid Robot・Plant-AI・Microbial AIが製造業の中核を担う時代。
- **ms_sbsp_commercial_2070** (新規, 2070): 宇宙太陽光発電がGW級商用運転。
- **ms_bmi_cognitive_aug_2070** (新規, 2070): BMIが選択的認知拡張デバイスとして社会定着。
- **ms_post_human_phase_2073** (新規, 2073): 人間-機械の境界が物質的にも認識的にも流動化（書籍第十一章の関係論的存在論が制度化）。

### ボトルネック

技術的ボトルネックよりも、「関係論的存在論」の制度的・物質的基盤の準備が遅れることが論点となる。書籍第十三-十四章が示す通り、生命を「技術対象」ではなく「関係相手」として扱う実践は、Bio-Hybrid Robot・植物-AI協働農業の倫理的・制度的設計において産業界が直面する具体的課題となる。先住民の伝統知が「単なる文化遺産」ではなく「Bio系統の制度設計のための実践的参照点」として再評価される（書籍は具体的な地域・民族の引用を行わず、参照点としての存在のみを述べる）。

### 社会への波及

「人間とは何か」「個人とは何か」が問われる時代となる。法・倫理・教育・労働のすべてが再定義を迫られる。

### 前プロジェクト2070人材との接続

前プロジェクトの2070時点に対応する。人材像は「AIと協働しながら、生命と機械と人間の境界を再設計する者」となる。具体的には、(1) Cognitive Augmentation時代の教育・福祉・労働再設計者、(2) Bio-Hybrid製造の倫理ガバナンス担当、(3) 知性のオーケストラを編成する「指揮者」的役割、である。

---

## Phase F (2075-2090): ポスト人間中心物理エコシステム期

### 5系統の状態

このフェーズで、Physical AIは「個別機械」から「分散身体」へ転換する。群知能・群行動が標準となり、ロボットという概念が消え、物理操作能力が環境・建物・道具・身体に分散的に埋め込まれる（ambient embodiment）。

**stream_hw** では、自然界の生物との統合が進む。バイオハイブリッド（生体組織+電子制御）が大規模に展開される。人類の身体能力を補完・拡張する役割（Exoskeleton, Prosthetics系譜の集大成）。

**stream_mat** では、一人当たり一次エネルギー数十kW規模が現実的となる。核融合 + SBSP + 高効率蓄電でエネルギー希少性が消える。事業はフロー型からストック型へ。「年間販売台数」ではなく「設置されたインフラ群の運用」が利益源泉に。

**stream_bio** では、人体内バイオボットが臨床標準化する。植物-AI協働農業が農業統計の主流となる。微生物群制御による腸内・土壌・産業発酵の最適化が一般化。

**stream_cog** では、複合知能オーケストラが形成される。単一AGIではなく、多様な専門知能の協調ネットワーク。manufacturing-orchestra DBが示すオーケストラ的協働の社会全般への拡張が完成する。Hutchins型の分散認知・Clark型の拡張認知が物理インフラとして実装される。

### 主要マイルストーン

- **ms_ambient_embodiment_2080** (新規, 2080): ロボット概念の消失。物理操作能力の環境分散。
- **ms_intelligent_orchestra_form_2085** (新規, 2085): 複合知能オーケストラの形成。
- **ms_energy_abundance_2085** (新規, 2085): エネルギー希少性の実質的消滅。
- **ms_biohybrid_general_2085** (新規, 2085): バイオハイブリッドが日常技術に。
- **ms_civilization_infrastructure_2088** (新規, 2088): Physical AIが食糧生産・廃棄物循環・気候制御の主要担い手に。

### ボトルネック

技術的ボトルネックよりも、「人間中心」から「関係中心」への文明的・思想的転換が遅れることが論点となる。書籍第十一章の関係論的存在論が、制度の中核原理として機能するための時間がかかる。

### 社会への波及

「人類の文明」概念そのものが拡張される。生物・人工物・人間の三項関係として文明が再定義される。

### 前プロジェクト2070-2100人材との接続

前プロジェクトの2070人材像から2100人材像への移行期に対応する。人材という概念自体が、人間個人の能力ではなく「知性のオーケストラへの参加形態」として再定義され始める。

---

## Phase G (2090-2100): 関係論的物理生態系期

### 5系統の状態

deep knowledge書籍の中心命題が完成局面を迎える。Physical AIは「物理世界に介入する身体性をもつ知性層」として、他のAI形態（LLM・生体AI・量子AI・分散AI）と境界が溶解した状態に到達する。

**stream_fm + stream_cog + stream_bio** が完全融合し、ヒト・古典AI・生体AI・量子AI・分散AI・身体性AIなど、複数経路の知性が共存・協調する。AGI-DBのDEF-015（Bostrom Superintelligence, 2014）が想定する「全領域人間超越」状態は、単一の超越的知性としてではなく、「多様な知性の編成」として実現される。

**stream_mat** では、量子-古典-生物計算の三層化が完成。Physical AIは最適計算リソースを動的に選択する。事業はフロー型からストック型へ完全移行。

**stream_hw** では、人間-ロボット-AI-環境の融合システムが日常インフラとなる。物理世界とサイバー空間が連続体として運用される（Digital Twin Ubiquity）。

**stream_bio** では、Bio系統が「機械の改良」を超えて「生命と機械と人間の協働体制」を実装する。文明維持インフラ（食糧生産・廃棄物循環・気候制御）の主要担い手として、生命系製造が定着する。

**stream_cog** では、Varela 1991が「知性は単一の場所には存在しない」と述べた構図の工学的実現が完成。一つのタスクには複数の認知システム（環境モデル・身体スキーマ・社会的推論・言語理解・予測符号化・自由エネルギー最小化）が並行して関与し、それぞれが状況に応じて主導権を交替する。人間の脳もまた、このオーケストラの一つの楽器として参加する。

### 主要マイルストーン

- **ms_intelligence_orchestra_2100** (S1提案, 2100): 知性のオーケストラ完成予測点。単一AGIではなく多様な知性の編成体系。Physical AIは物理層構成要素として透明化される。
- **ms_relational_ontology_inst_2095** (新規, 2095): 関係論的存在論が制度の中核原理として機能。
- **ms_diversity_of_intelligence_2098** (新規, 2098): 生物多様性に類比される「知性多様性」が認識される。
- **ms_phase_g_complete_2100** (新規, 2100): Physical AIは「Physical AIの完成点」ではなく、Physical AIが他のAI形態と区別不能になる「境界溶解点」として到達。

### ボトルネック

このフェーズでは技術的ボトルネックよりも、「2100年以降の文明像」をいかに描くかという展望そのものが新たな課題となる。Physical AIは終着点ではなく、次の千年へ向けた基盤として捉えられる。

### 社会への波及

「人類の役割」が、文明維持から「意味の創造」「他者との関係性の深化」「未踏領域の探究」に集中する。これが書籍が描く2100年文明像の到達点である。

### 前プロジェクト2100人材との接続

前プロジェクトの2100時点に対応する。人材像は「知性のオーケストラの一員として、独自の楽器（人間性）を奏でる者」となる。人間に固有な能力（意味付け・関係構築・倫理判断・芸術的探究）が、AGI時代における人類の核となる。

---

## 系統相互作用マトリクス（SQL INSERT 24件）

PHAI-DBの`phai_crossdomain_relations`（または独立した`phai_stream_relations`テーブル）に登録すべき8系統相互作用を24件提示する。各レコードは(source_stream, target_stream, interaction_type, era_dominant, description, strength)を主たる属性とする。

```sql
-- AI/ML → Robotics系統への影響
INSERT INTO phai_stream_relations (id, source_stream, target_stream, interaction_type, era_dominant, description, strength) VALUES
('sr_001', 'stream_fm', 'stream_hw', 'enables',
 '2017-2030',
 'Transformer→GPT-3→PaLM-E→RT-2→OpenVLA→GR00T→Helix系譜が「言語で指示し身体で実行する」VLAを成立させ、ヒューマノイドの応用範囲を再定義した。Foundation Models for Roboticsの中核経路。',
 10),

('sr_002', 'stream_fm', 'stream_ctrl', 'extends',
 '2020-2035',
 'VLAが古典MPC+RLハイブリッドの上位層として高次タスク計画を担当。Whole-Body Control（Khatib 1987）はそのままの形で残り、その上に基盤モデルが乗る二層構造が標準化。',
 9),

('sr_003', 'stream_rl', 'stream_hw', 'empirically_tests',
 '2018-2026',
 'OpenAI Dactyl（2018）・ANYmal Sim2Real（2019）・MIT Mini Cheetah RL（2021）が「シミュレーションで学んだポリシーが実機で動く」最初の証明群を形成。深層強化学習が現実世界の物理タスクへ移行可能であることを実証した。',
 10),

('sr_004', 'stream_sim', 'stream_rl', 'enables',
 '2017-2030',
 'Isaac Sim・MuJoCo 3.0・Genesisが大規模GPU並列シミュレーションを民主化し、Domain Randomization（2017）・Rapid Motor Adaptation（2021）等のsim-to-real技術と組み合わさって、RL学習データのボトルネックを部分的に解消。',
 9),

-- AI/ML → Bio系統
('sr_005', 'stream_fm', 'stream_bio', 'enables',
 '2020-2050',
 'AlphaFold 2（2020 Nature）→AlphaFold 3（2024 Nature 630:493）→Coscientist（2023 Nature 624:570）の系譜が、基盤モデルを創薬・合成生物学の標準ツールとした。Insilico Medicine Rentosertibが2024年フェーズII到達でAI設計薬の実証点に。',
 10),

('sr_006', 'stream_fm', 'stream_mat', 'enables',
 '2023-2040',
 'DeepMind GNoME（Nature 624:80, 2023）が220万件の新規結晶構造候補を生成、A-Lab（Nature 624:86, 2023）が17日間で41種を合成。基盤モデル+自律実験ロボットによる材料発見が指数加速。',
 10),

-- AI/ML → Cognitive系統
('sr_007', 'stream_fm', 'stream_cog', 'extends',
 '2018-2050',
 'World Models（Ha-Schmidhuber 2018）→DreamerV3（Nature 2024）→Genie 2（DeepMind 2024）→Sora（OpenAI 2024）が、Friston的予測脳の工学的実装としてCognitive Stackの中核に。LeCun JEPA（2022）がLLM中心パラダイムへの代替を提示。',
 9),

-- Bio → Materials系統
('sr_008', 'stream_bio', 'stream_mat', 'complements',
 '2020-2070',
 'Self-Driving Lab（Liverpool Mobile Chemist 2020, A-Lab 2023, Coscientist 2023）が物質発見の主要パイプラインに。Bio系統の自律実験ロボットがMaterials/Energy系統の発見速度を10倍以上加速。',
 9),

('sr_009', 'stream_bio', 'stream_hw', 'extends',
 '2008-2070',
 'Soft Robotics（Whitesides 2008）→Octobot（Nature 2016）→Bio-Hybrid Robot（Morimoto et al. Sci. Robotics 2018）→Xenobot（PNAS 2020）→Anthrobot（Adv. Science 2023）の系譜が、機械の身体素材を生体組織へと拡張。2070年生命系製造期へ。',
 9),

-- Materials → 全系統
('sr_010', 'stream_mat', 'stream_hw', 'constrains',
 '1947-2100',
 '半導体（Moore則・GAA・HBM）・バッテリー（Li-ion→全固体）・エネルギー（核分裂・核融合・SBSP）の進捗が、ヒューマノイドの稼働時間・計算能力・コストの上限を物理的に規定。Physical AI普及の最大律速要因。',
 10),

('sr_011', 'stream_mat', 'stream_fm', 'constrains',
 '2020-2050',
 'データセンター電力（2022:460TWh→2026:1050TWh, IEA 2024）と半導体製造能力が、基盤モデルの訓練・推論規模を物理的に律速。Microsoft TMI再稼働・Google Kairos契約等がAI×原子力の構造的合流を示す。',
 10),

-- Cognitive → AI系統への逆流
('sr_012', 'stream_cog', 'stream_rl', 'extends',
 '2010-2050',
 'Friston自由エネルギー原理（Nat. Rev. Neurosci. 2010）→Active Inference（MIT Press 2022）→Active Inference for Robotics（Lanillos et al. 2021）が、報酬最大化に代わる新しい最適化目標を強化学習に提供。VERSES AI Geniusで商用化が進む。',
 8),

('sr_013', 'stream_cog', 'stream_fm', 'extends',
 '2019-2050',
 'Bengio System 2 Deep Learning（NeurIPS 2019）・LeCun JEPA（2022）・Friston Active Inferenceが、生成型LLM中心AIへの代替案として、認知科学的原理を基盤モデルに注入する潮流を形成。',
 8),

-- Cognitive → Bio
('sr_014', 'stream_cog', 'stream_bio', 'derived_from',
 '1943-2050',
 'McCulloch-Pittsニューロン（1943）→Hebbian learning（1949）→Liquid State Machine（2002）→IBM TrueNorth（2014）→Intel Loihi 2（2021）→IBM NorthPole（2023）の神経模倣ハードウェア系譜は、認知科学と生命系の合流点に位置する。',
 9),

-- Robotics → Materials (逆方向の駆動)
('sr_015', 'stream_hw', 'stream_mat', 'demands',
 '2024-2040',
 'ヒューマノイド・配送ドローン・eVTOL等の物理AI実装が、固体電池・新規アクチュエータ材料（EAP・LCE・McKibben muscle系統）・触覚センサ膜への需要を増大。stream_matの優先研究領域を決定。',
 8),

-- Bio → Cognitive
('sr_016', 'stream_bio', 'stream_cog', 'empirically_grounds',
 '2008-2070',
 'Soft Robotics・Bio-Hybrid Robot・Xenobot/Anthrobotが進展するほど、機械/生命・主体/環境の二項対立は物質的に破綻。Pfeifer-Iida Embodied Cognitionの主張に経験的基盤を提供。書籍第十一章の関係論的存在論と接続。',
 8),

-- Simulation → 全系統
('sr_017', 'stream_sim', 'stream_fm', 'enables',
 '2010-2050',
 'NVIDIA Isaac Sim・MuJoCo 3.0・Genesis・Cosmosが、VLA訓練用の大規模合成データ生成を担う。Open X-Embodiment実機データと組み合わさって、基盤モデルのスケール則を維持。',
 9),

('sr_018', 'stream_sim', 'stream_mat', 'accelerates',
 '2020-2050',
 'Materials Project（LBNL）+ DFT計算 + GNoME（DeepMind）+ A-Lab自律実験のループが、シミュレーションと実験の境界を溶かし、材料発見を指数加速。',
 9),

-- Control → 全系統
('sr_019', 'stream_ctrl', 'stream_hw', 'enables',
 '1948-2100',
 'Cybernetics（Wiener 1948）→DH parameter（1955）→Computed Torque Control（1985）→Whole-Body Control（Khatib 1987）→ZMP（Vukobratović 1968）→Convex MPC（2018）の系譜が、全てのロボット実機の理論的基盤を構成。',
 10),

-- Multi-stream convergence
('sr_020', 'stream_fm', 'stream_bio,stream_cog,stream_mat', 'orchestrates',
 '2040-2100',
 'AGI（汎用基盤モデル）が、Bio・Cog・Mat系統のそれぞれが提供する専門能力を統合・調整するメタ層として機能。2050年以降の「Cognitive Stack」「Living Factory」「AI×原子力」の全てに共通する統合原理。',
 10),

('sr_021', 'stream_cog', 'stream_hw,stream_rl', 'redefines',
 '2050-2100',
 'BMI（Neuralink, Synchron）・拡張認知・分散認知が普及するにつれ、「ロボットの認知」と「人間の認知」と「環境の認知」の境界が流動化。stream_hwとstream_rlの最適化目標自体が、cognitive側から再定義される。',
 9),

('sr_022', 'stream_bio,stream_mat', 'stream_hw', 'transforms',
 '2070-2100',
 '生命系製造（Living Factory）と新材料発見（GNoME後継系統）が、機械製造のパラダイムを「組み立て」から「成長・再生」へ変革。Bio-Hybrid Robotが日用品となるPhase F-Gの中核ダイナミクス。',
 9),

-- Materials → Bio (逆方向)
('sr_023', 'stream_mat', 'stream_bio', 'enables',
 '2023-2050',
 'AI設計材料（GNoME・A-Lab系統）が、合成生物学・人工臓器・バイオハイブリッドに必要な新規生体適合素材・人工足場材料・薬物送達担体を提供。物質基盤の進化が生命系製造の前提条件を整える。',
 8),

-- Simulation → Cognitive
('sr_024', 'stream_sim', 'stream_cog', 'embodies',
 '2018-2050',
 'World Models（Ha-Schmidhuber 2018, DreamerV3 2024, Genie 2 2024, Sora 2024）が、Friston Active Inferenceの「内部世界モデル」概念を工学的に実装。シミュレーションと認知の境界が溶解。',
 9);
```

---

## 統合的観察: 7フェーズを貫く5つの動詞

7フェーズを動詞で要約すると、Physical AI 2026-2100の運動は次の5つの動作主題に整理される。

**Phase A-B (2026-2040): 「定着する」と「汎化する」**
VLA基盤モデルとヒューマノイドが商用配備として定着し（A）、その後、非構造環境への汎化が進む（B）。stream_fmが主役で、stream_hwとstream_matがそれを支える。

**Phase C-D (2040-2060): 「並走する」と「自律する」**
人間と機械が「協働相手」として並走する段階（C）から、機械が完全自律物理エージェントとして社会の下層を担う段階（D）へ。stream_rl + stream_cogの合流がエピソード横断学習を実現する。

**Phase E (2060-2075): 「生成する」**
知性のオーケストラの諸要素が同時生成される。書籍が指摘する「生命系製造期」がこの時期の中核。stream_bioとstream_matとstream_cogが融合し、製造業のパラダイムが転換する。

**Phase F-G (2075-2100): 「溶解する」と「編成される」**
Physical AIという概念そのものが「個別機械」から「分散身体」へ転換し（F）、最終的に他のAI形態と区別不能になる「境界溶解点」に到達する（G）。これは書籍の中心命題「知性のオーケストラ」の完成局面に対応する。

### 7フェーズを貫く構造的特徴

第一に、**stream_matが律速要因として一貫する**。半導体・バッテリー・エネルギーの物理基盤が遅れれば、全フェーズが遅延する。逆に、stream_matの加速（特にAI設計材料の自律発見ループ）が他系統を引き上げる。

第二に、**stream_cogが目標設定の役割を担う**。何が最適化対象か、何を知性と呼ぶか、人間とは何かという問いは、stream_cogが定義する。これがPhase E以降の文明的転換の理論的基盤となる。

第三に、**stream_bioが境界溶解の物質的担い手となる**。機械と生命の境界、計算と化学の境界、個体と環境の境界は、Bio系統の進展に応じて物質的に書き換えられる。

第四に、**5系統合流モデルは2040年代に8系統オーケストラへと拡張される**。Phase Cまでは5系統が中核だが、Phase D以降はstream_bio・stream_mat・stream_cogが対等な参加者として加わる。

第五に、**前プロジェクト4時点（2030/2050/2070/2100）はそれぞれPhase A末・C中盤・E初期・G到達点に対応する**。すなわち、人材像の変化軌道とPhysical AIの技術軌道が同期して進む。これは偶然ではなく、Physical AIが「労働の代替」「知性の補完」「身体の拡張」「関係の再編」という4つの順序で社会に浸透するためである。

### 結語: ロードマップとしての意義

本7フェーズロードマップは、Physical AIを「身体を持つAI」という単一の技術系統としてではなく、8系統の織り合わせとして描いた。各フェーズの軌道はAGI-DBのtimeline predictions、PHAI-DBの既存マイルストーン、Phase 2で追加された約160件の新規概念・マイルストーン・ボトルネック、そして書籍『深い知が拓く2100年』の中心命題と整合的である。

2100年は「Physical AIの完成点」ではなく、Physical AIが他のAI形態・生命系・人間と区別不能になる「境界溶解点」として捉えられる。これは終着ではなく、次の千年へ向けた新たな基盤の確立である。

本ロードマップは、Phase 4（スピルオーバー分析）・Phase 5（社会接続）へと引き継がれる。Physical AIが社会の他領域（教育・医療・農業・金融・芸術等）に及ぼす影響、および前プロジェクトの4時点人材像との詳細マッピングは、後続フェーズで深化される。

---

**文書作成**: Phase 3 ロードマップ統合チーム
**文字数**: 約 11,500 字
**典拠**: Phase 2 の5系統ファイル（stream1-5.md, 約30,000字）を全文参照。PHAI-DB・AGI-DB・deep knowledge書籍を一次基盤とする。
**ハルシネーション対策**: 5系統ファイルで実在検証された概念のみを引用。新規予測（2030以降）はprojectedステータスを明示。
**思想的中立性**: 日本・東/東南/南アジアの思想的引用は使用していない。先住民の伝統知への参照は書籍内部の議論への接続にとどめ、特定民族・地域の知識引用は行っていない。
