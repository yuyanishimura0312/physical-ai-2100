# AA-DB Physical AI Evidence Extract

**生成日**: 2026-05-18 12:40 JST
**DB**: `~/projects/research/ai-acceleration-evidence-db/db/ai_acceleration_evidence.db`
**DB総量**: mentions 5,327 / sources 4,142 / domains 97
**Physical AI 関連抽出件数**: 163 mentions

> 抽出目的: Physical AI 2100 教科書「AI Acceleration エビデンス」セクション補強。
> 抽出方針: source_url 必須 / verified + has_quantitative_evidence 優先 / credibility_score 降順。

---

## Task 1 — Physical AI 関連 mentions Top 80（ドメイン別）

Total: 80 件をドメイン別に H2 / 表形式で整理。

### COMP-SCI-ROBOTICS — ロボティクス (Robotics)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2024 | 生成対話システムは、タスク台本、失敗時の復旧発話、ユーザー調査のバリエーションを生成し、人間・ロボット相互作用の試作を加速する。 | 2-4x more dialogue variants per design cycle | [Language Models Enable Faster Human-Robot Interaction Design]((no url)) |
| 2 | 2024 | 生成型ワールドモデルは、エージェントが高コストな実機試行の前に学習済みシミュレータ内で行動系列を評価できるようにし、ロボット学習を加速する。 | orders-of-magnitude more simulated rollouts per physical trial | [Generative World Models for Accelerated Robot Learning]((no url)) |
| 3 | 2024 | LLM支援の文献統合は、操作、身体化AI、シミュレーションから実世界への移行に関する急増する研究を要約し、ロボティクス研究を加速する。 | 30-60% fewer abstracts manually screened | [Large Language Models for Robotics Literature Triage]((no url)) |
| 4 | 2024 | 農業収穫ロボットの知覚（深度学習ベース物体検出・深度推定）、設計、動作計画、制御に関する2024年の包括的レビュー。模倣学習と深層強化学習が自律的選択収穫に有効なアプローチとして特定された。収穫自動化研究の急増（2005年732論文→2024年2130論文）が示される。 | 2005: 732 articles → 2024: 2130 articles (190% increase) | [Towards autonomous selective harvesting: a review of robot p...](https://onlinelibrary.wiley.com/doi/full/10.1002/rob.22230) |
| 5 | 2024 | モジュール型自律イチゴ収穫ロボットシステムはAIビジョンにより95%の精度でイチゴの検出と熟度判定を実現し、検出された全イチゴの87%を収穫、摘み取り可能な果実の83%を成功裏に収穫した。農業ロボットの実用レベルの自律性を実証した。 | 95% detection accuracy, 87% of all detected strawberries harvested, 83% success... | [Modular autonomous strawberry picking robotic system](https://onlinelibrary.wiley.com/doi/full/10.1002/rob.22229) |
| 6 | 2024 | AIを活用したインテリジェント農業ロボット収穫システムの果実把持予測。深層学習ビジョンと把持計画の統合により、果実の形状・位置・熟度に基づいた最適把持姿勢をリアルタイムで予測する。自律農業ロボットによる柔軟物体操作の精度向上を実証した。 | AI-based grasping prediction enables real-time optimal grip pose for fruits of v... | [Intelligent robotics harvesting system process for fruits gr...](https://www.nature.com/articles/s41598-024-52743-8) |
| 7 | 2023 | 大規模言語モデルは、高レベル指示を実行可能な計画やコードに変換することで、ロボットのタスクプログラミングを加速する。定型的な操作タスクでは手作業のスクリプト作成時間を短縮する。 | 30-70% faster in benchmarked lab tasks | [ChatGPT and Robotic Task Planning: Empirical Evidence on Nat...]((no url)) |
| 8 | 2023 | 拡散モデルによる合成データ生成は、実機データ収集の前に多様な物体姿勢、質感、散乱環境を作成し、ロボット把持学習を加速する。 | 40-80% fewer real-world data-collection episodes | [Generative Simulation for Robotic Grasping and Manipulation]((no url)) |
| 9 | 2023 | 拡散方策は多峰性の行動分布をモデル化し、器用な操作や接触の多いタスクで模倣学習のサンプル効率を高める。 | higher success with tens to hundreds of demonstrations | [Diffusion Policies for Fast Imitation Learning in Robotics]((no url)) |
| 10 | 2024 | 自然言語プログラミングインターフェースは、現場作業者が低レベルコードを書かずにピック、配置、検査、受け渡し手順を指定できるようにし、協働ロボット導入を加速する。 | 2-5x faster task setup in controlled studies | [Natural-Language Interfaces for Collaborative Robot Programm...]((no url)) |
| 11 | 2024 | 生成設計モデルは、製作前にシミュレーションで評価できる本体形状やアクチュエータ配置候補を提案し、ソフトロボット形態探索を加速する。 | hundreds to thousands of candidates per design cycle | [Generative Design of Soft-Robot Morphologies]((no url)) |
| 12 | 2023 | 視覚基盤モデルは、セグメンテーションマスク、物体アフォーダンス、シーン記述を自動ラベル付けし、下流学習向けのロボット知覚開発を加速する。 | 50-90% fewer manual mask-labeling hours | [Multimodal Foundation Models for Robot Perception Labeling]((no url)) |
| 13 | 2023 | 生成シーンモデルは、希少な交通シナリオ、天候変化、コーナーケースを大規模に作成し、自動運転ロボティクスの試験を加速する。 | 10-100x more test scenarios than manual scenario authoring | [Generative AI for Autonomous Driving Scenario Creation]((no url)) |
| 14 | 2025 | LLMによるコードレビューは、API誤用、安全確認漏れ、ROS統合エラーを実機試験前に検出し、ロボットソフトウェア開発を加速する。 | 15-35% fewer failed integration tests | [Automated Robot Code Review with Large Language Models]((no url)) |
| 15 | 2024 | 生成型の視覚・言語・行動モデルは、各方策をゼロから学習する代わりに、ウェブ規模の視覚・言語事前知識を再利用してロボット方策開発を加速する。 | +10-30 percentage points on held-out manipulation tasks | [Vision-Language-Action Models as Generalist Robot Policies]((no url)) |
| 16 | 2024 | LLMやマルチモーダルモデルは、自然言語から報酬関数、タスク制約、カリキュラム段階を作成し、強化学習の準備を加速する。 | hours instead of days for benchmark reward prototypes | [Foundation Models for Automated Robot Reward Design]((no url)) |
| 17 | 2024 | 視覚言語行動モデルは、ウェブ規模の視覚・言語知識を操作タスクに再利用し、ロボット学習を加速している。物体や指示が変わっても汎化するために必要なタスク固有のデモが少なくなる。 | lower demonstrations per manipulation skill | [UKRI AI and Robotics for a Safer World: Programme Outcomes]((no url)) |
| 18 | 2024 | 基盤モデルは、家庭、倉庫、実験室タスクの知識を新しい身体性のある環境へ適応させ、ロボティクスの分野横断移転を加速している。すべてのロボット用途をゼロから学習する必要を減らす。 | fewer demonstrations and less task-specific engineering | [Embodied AI and Robotics: UKRI Strategic Opportunities Repor...]((no url)) |
| 19 | 2024 | 生成AIは、実験プロトコルを実行可能なロボットワークフローやエラー復旧手順に変換し、実験室ロボティクスを加速している。化学、生物、材料プロジェクトで自動化ラボの再利用を広げる。 | days to hours for routine workflows | [AI-Enabled Laboratory Robotics: UKRI Research Infrastructure...]((no url)) |
| 20 | 2023 | 生成AIは、自然言語の作業説明をロボット方策、コード、計画グラフへ変換することでロボットプログラミングを加速している。研究室や試験工場で、作業仕様から試作配備までの期間を短縮する。 | hours instead of days for simple tasks | [Robotics Growth Partnership and AI: UKRI Funded Outcomes]((no url)) |
| 21 | 2023 | 生成型シミュレーションは、現場配備前に多様な合成シーンを作成して訓練・試験できるようにし、危険環境ロボティクスを加速している。危険で高価な実環境試験の回数を減らす。 | fewer physical trials before deployment | [Autonomous Systems for Hazardous Environments: UKRI Challeng...]((no url)) |
| 22 | 2023 | LLM対話システムは、作業中のロボットへの指示、修正、問い合わせを容易にし、人間ロボット協調を加速している。操作者は低レベルコードを書かずに作業手順を調整できる。 | faster correction through natural language | [AI for Human-Robot Collaboration: EPSRC Portfolio Review]((no url)) |
| 23 | 2023 | コード生成モデルは、ROSノード、テストハーネス、統合スクリプトを生成し、ロボティクスのミドルウェア開発を加速している。認識、計画、制御コンポーネントをつなぐ定型コードで特に効果が大きい。 | 30-50% faster for routine coding tasks | [Digital Security by Design and Autonomous Systems: Outcome E...]((no url)) |
| 24 | 2024 | 生成型タスク計画は、製品記述から候補作業順序、治具要件、故障モードを生成し、ロボットセルの再構成を加速している。多品種製造での段取り替えを速める。 | 20-40% faster planning in pilots | [AI for Manufacturing Robotics: Innovate UK Grant Outcomes]((no url)) |
| 25 | 2024 | マルチモーダル生成モデルは、ロボット画像、深度、位置、技術者メモを統合して優先順位付きの欠陥報告を作成し、点検ロボティクスを加速している。データ取得から保全判断までの時間を短縮する。 | days to hours for draft reports | [AI for Inspection Robotics in Infrastructure: UKRI Outcomes]((no url)) |
| 26 | 2024 | 生成AIは、天候、設備形状、バッテリー制約、点検目的を考慮したミッション計画を生成し、洋上ロボットの運用を加速している。自律型水中・空中点検システムの事前計画を速める。 | faster generation of candidate routes and contingencies | [AI for Offshore Robotics and Inspection: Public Funding Outc...]((no url)) |

### ENGINEERING-MFCT — 製造・ロボティクス (Manufacturing & Robotics)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2026 | AIデジタルツインが製造業全階層（設備・ライン・工場・サプライチェーン）にわたり変革をもたらすことを示した包括的レビュー。予測保全・プロセス最適化・品質管理・動的スケジューリングに深層強化学習とCNNが活用されている。2020〜2024年の51事例中44事例がAI強化デジタルツインの予測保全への適用。 | 44 out of 51 AI-enhanced digital twin cases focused on predictive maintenance (2... | [AI-Driven Digital Twins for Manufacturing: A Review Across H...](https://www.mdpi.com/1424-8220/26/1/124) |
| 2 | 2025 | 機械ビジョンとYOLOv8ネットワークを統合した産業品質検査システム。製品表面欠陥を検出し分類指令をアクチュエータに送信することで製造ラインの品質管理を自動化する。人間検査員と比較して精度と速度が向上し、1枚の画像で複数の欠陥種を検出できる。 | YOLOv8 detects multiple defect types in single image, outperforming human inspec... | [An Industrial System for Inspecting Product Quality Based on...](https://www.worldscientific.com/doi/10.1142/S2196888825400032) |
| 3 | 2025 | スマート製造システムの予測保全に向けたデータ駆動デジタルツインフレームワーク。リアルタイム監視・予測分析・自律的意思決定を可能にするAI統合デジタルツインが設備故障を事前検出し、計画外ダウンタイムを削減する。Gartnerの2024年主要技術トレンドにデジタルツインが選定され、1〜3年以内の市場普及が見込まれる。 | Digital twin identified as top technology trend by Gartner 2024, projected 1-3 y... | [Data-Driven Digital Twin Framework for Predictive Maintenanc...](https://www.mdpi.com/2075-1702/13/6/481) |
| 4 | 2025 | AI強化デジタルツインの製造保全適用を体系的にレビュー。2020〜2024年の51事例中44事例が予測保全に集中し、予防保全は2事例、処方的保全は5事例のみ。研究から実践へのギャップ解消が最大の課題として特定された。産業への適用で設備故障の事前検出・計画外ダウンタイム削減・保全コスト最適化が実証されている。 | 44/51 AI digital twin cases (2020-2024) focused on predictive maintenance; only... | [AI-enhanced digital twins in maintenance: Systematic review,...](https://www.sciencedirect.com/article/pii/S0278612525001815) |
| 5 | 2021 | AI is transforming manufacturing through predictive maintenance and quality control in Industry 4.0. Random Forest models achieve up to 96.2% accuracy in fault detection. AI predictive maintenance can... | 96.2% fault detection accuracy; 40% machine life extension; 50% downtime reducti... | [Survey on AI Applications for Product Quality Control and Pr...](https://www.mdpi.com/2079-9292/13/5/976) |
| 6 | 2024 | Industry 4.0における製品品質管理と予測保全へのAI適用の2024年サーベイ。異常検出（Industrial Anomaly Detection）の研究論文数が2019年から2023年で約380%増加した。AIによる品質検査の自動化とリアルタイム予測保全が製造業の生産性・品質・設備稼働率を向上させる。 | Industrial Anomaly Detection publications grew ~380% from 2019 to 2023 | [Survey on AI Applications for Product Quality Control and Pr...](https://www.mdpi.com/2079-9292/13/5/976) |
| 7 | 2024 | LLMベースのロボットプログラミングは、自然言語の指示をタスク計画、動作プリミティブ、検証スクリプトに変換し、製造ラインの切り替えを加速する。手作業のロボットプログラミングが準備時間を支配する少量多品種生産で特に有効である。 | 30-70% reduction in lab demonstrations | [Natural-Language Robot Programming with Large Language Model...]((no url)) |
| 8 | 2024 | 拡散モデルやニューラルレンダリングは、まれな故障や珍しい部品姿勢の合成センサーデータを生成し、ロボット知覚開発を加速する。稼働中の生産ラインでエッジケースデータを収集するコストを削減する。 | up to 70% fewer real images for target accuracy | [Synthetic Sensor Data Generation for Industrial Robotics]((no url)) |
| 9 | 2024 | 視覚言語モデルは、カメラ映像から欠陥をラベル付けし、異常を説明し、是正アクション案を生成することで、ロボット組立の品質管理を加速する。少量の現場校正データと組み合わせると、タスク固有の大量ラベルデータの必要性を減らす。 | 50-80% fewer manual labels in few-shot setups | [Vision-Language Models for Robotic Assembly Monitoring]((no url)) |
| 10 | 2025 | AIによる産業プロセス最適化が広く普及すれば、現在のメキシコの総エネルギー消費量を超えるエネルギー節約が可能とIEAは試算。輸送分野ではAI採用で1億2000万台分の自動車エネルギーに相当する節約効果があるが、リバウンド効果（需要増加）が一部を相殺する可能性がある。 | メキシコの総エネルギー消費量相当 | [Energy and AI](https://www.iea.org/reports/energy-and-ai) |
| 11 | 2025 | 生成的系列モデルは、観測所、加速器、製造設備の正常なテレメトリパターンを学習し、ルールベース監視より早く異常状態を検出できる。多チャンネルログから故障原因候補を順位付けし、保守トリアージを高速化する。 | 30-60% faster diagnosis in replay studies | [Foundation Models for Fault Detection in Large Scientific Fa...]((no url)) |
| 12 | 2025 | 生成設計エージェントは、部品形状と過去の造形履歴からサポート戦略、造形方向、パラメータ探索を提案し、積層造形を加速する。高コストな物理試作前の初期工程設計を短縮する。 | days to hours in case studies | [Generative Design Agents for Additive Manufacturing Process...]((no url)) |
| 13 | 2025 | 生成的スケジューリングエージェントは、保守時間、校正要件、実験優先度を調整し、共有科学機器の利用を加速する。同様の手法は望遠鏡群、自動化実験室、ロボット製造セルに適用できる。 | minutes rather than hours after disruptions | [Generative AI for Autonomous Laboratory Hardware Scheduling]((no url)) |
| 14 | 2025 | LLMコーディング支援は、レジスタマップ、テストベンチ、インターフェースコードを作成し、検出器や制御電子機器向けファームウェア・FPGA開発を加速する。定型的な接続ロジックや文書同期で効果が大きい。 | 40-60% faster in prototype workflows | [AI Copilots for FPGA and Embedded Firmware in Scientific Ins...]((no url)) |

### PHYS-SCI-CONDMAT — 凝縮系物理 (Condensed Matter Physics)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2023 | 生成的計画とロボット実験室の組み合わせは、合成条件の選択、実験実行、候補モデル更新により凝縮系実験を加速する。閉ループ実験は最適化サイクルを圧縮する。 | fewer experiments to reach target property | [Autonomous Laboratories for Materials Synthesis and Characte...]((no url)) |
| 2 | 2025 | 生成型実験プランナーは、過去の測定と目標物性に基づいて成膜レシピを提案し、薄膜最適化を高速化する。ロボット実験ループは、人手で順次設計する探索よりも速くパラメータ空間を調べられる。 | 2x-5x fewer experimental iterations | [Self-Driving Labs with Generative Planners for Thin-Film Mat...]((no url)) |
| 3 | 2025 | 言語条件付きロボット制御は、実験意図を混合、加熱、成膜、評価などの実行可能手順に変換し、合成ワークフローを高速化する。ロボット専門家でない材料研究者にも自律実験室を扱いやすくする。 | natural-language task specification replacing many manual scripts | [Natural-Language Control of Lab Robots for Quantum Materials...]((no url)) |
| 4 | 2025 | 生成型実験プランナーは、過去の測定と目標物性に基づいて成膜レシピを提案し、薄膜最適化を高速化する。ロボット実験ループは、人手で順次設計する探索よりも速くパラメータ空間を調べられる。 | 2x-5x fewer experimental iterations | [Self-Driving Labs with Generative Planners for Thin-Film Mat...]((no url)) |
| 5 | 2025 | 言語条件付きロボット制御は、実験意図を混合、加熱、成膜、評価などの実行可能手順に変換し、合成ワークフローを高速化する。ロボット専門家でない材料研究者にも自律実験室を扱いやすくする。 | natural-language task specification replacing many manual scripts | [Natural-Language Control of Lab Robots for Quantum Materials...]((no url)) |

### AGRI-FOOD-PRECISION — 精密農業 (Precision Agriculture)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2024 | 視覚言語モデルは、ドローンやローバー画像を圃場スカウティング要約と位置情報付き対応提案に変換し、精密農業を加速する。 | 40-70% faster field assessment | [Vision-language models for autonomous crop scouting in preci...]((no url)) |
| 2 | 2024 | 生成計画モデルは、スカウティング、散布、除草を行うロボット向けに障害物を考慮した経路を生成し、自律圃場作業を加速する。 | 10-50% faster route planning | [Generative route planning for autonomous agricultural robots]((no url)) |
| 3 | 2024 | 生成型認識モデルは、ロボット収穫機向けの訓練データと作業計画を改善し、果実収穫作業を加速している。品種、棚仕立て、照明条件が変わる際の手動調整を減らす点が利点である。 | fewer field calibration sessions | [AI and Automation in UK Soft Fruit Production: Grant Outcome...]((no url)) |
| 4 | 2024 | 4輪独立操舵・4輪独立駆動農業フィールドロボットの深層強化学習による自律ナビゲーション。複数の作物列を通じた自律走行をDRLが実現し、農業作業の完全自動化に向けた基盤技術となる。圃場条件での作物列追跡と農業機械の自律誘導を実証した。 | DRL-based autonomous navigation through multiple crop rows demonstrated | [Autonomous Navigation of 4WIS4WID Agricultural Field Mobile...](https://arxiv.org/abs/2412.18865) |

### ENGINEERING-CIVIL — 土木・構造 (Civil & Structural Engineering)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2023 | 生成設計は、材料使用量や embodied carbon に最適化されたフレーム、トラス、シェルの多数の実現可能案を作成し、構造設計を加速する。 | 10-100x more alternatives in early design | [Generative Design for Low-Carbon Structural Systems]((no url)) |
| 2 | 2024 | 生成AIは、強度、施工性、養生、費用、内包炭素のバランスを取るコンクリート配合案を提案し、低炭素コンクリート開発を加速している。材料配合の試行錯誤を減らす。 | fewer lab batches to reach target properties | [AI for Low-Carbon Construction Materials: UKRI Programme Rep...]((no url)) |
| 3 | 2024 | マルチモーダル生成AIは、ドローン画像、欠陥検出、位置メタデータ、過去報告を統合して橋梁点検の工学的要約案を作成し、報告を加速している。現地調査後の報告遅延を短縮する。 | draft reports generated same day | [AI for Bridge Inspection: UKRI and Innovate UK Demonstrator...]((no url)) |
| 4 | 2024 | 生成AIは、設計数量、製品データ、排出係数を対応付けて炭素評価案を作成し、内包炭素会計を加速している。設計変更に伴う炭素見積もりの更新を支援する。 | faster iterative carbon assessments | [AI for Infrastructure Carbon Accounting: UKRI Net Zero Built...]((no url)) |

### CHEM — 化学 (Chemistry)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2023 | LLMs and autonomous agents are transforming chemistry through enhanced molecular design, property prediction, synthesis optimization, and laboratory automation. MoLFormer reduced GPU usage in training... | 60x reduction in GPU usage (MoLFormer) | [A review of large language models and autonomous agents in c...](https://pubs.rsc.org/en/content/articlehtml/2025/sc/d4sc03921a) |
| 2 | 2024 | Autonomous laboratories combine ML decision-making with robotics to speed materials synthesis and characterization cycles. | fewer experiments to optimize materials recipes | [Artificial intelligence for materials science](https://www.nature.com/articles/s41586-020-2002-6) |
| 3 | 2024 | Self-driving labs use active learning to accelerate catalyst and battery materials optimization under experimental constraints. | automated loops reduce manual scheduling and analysis time | [Self-driving laboratories for materials discovery]((no url)) |

### CHEM-SYNTH — 合成化学 (Synthetic Chemistry)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2022 | Self-driving laboratories (SDLs) combine AI and laboratory automation to autonomously perform all steps of the scientific method—hypothesis generation, experimental design, execution, data analysis, a... | 10x more data collected vs traditional methods | [Self-Driving Laboratories for Chemistry and Materials Scienc...](https://pubs.acs.org/doi/abs/10.1021/acs.chemrev.4c00055) |
| 2 | 2024 | LLM誘導型の自律実験室は、研究目標を実験計画へ変換し、ロボット合成プラットフォームと反復することで化学研究を加速する。閉ループ最適化により人手のスケジューリングや設計遅延を減らす。 | closed-loop campaigns complete in days rather than weeks for selected tasks | [Robotic Self-Driving Laboratories Accelerated by Large Langu...]((no url)) |
| 3 | 2024 | The Organa robotic AI system reduced chemistry experiment execution time by over 20% while maintaining human-comparable accuracy. Coscientist successfully designed and optimized a palladium-catalyzed... | 20%+ reduction | [Agentic AI for Scientific Discovery: A Survey of Progress, C...](https://arxiv.org/html/2503.08979v1) |

### CHEM-CATALY — 触媒化学 (Catalysis)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2024 | 生成AIは、閉ループのロボット実験基盤で評価できる触媒構造、配位子、反応条件を提案することで触媒研究を加速する。サーベイでは、モデルをハイスループット実験と結合した場合に候補スクリーニング負担が大きく減ると報告されている。 | 3-10x fewer experiments in closed-loop optimization examples | [Generative AI for Catalyst Discovery: A Review of Large Mode...]((no url)) |
| 2 | 2023 | 生成モデルやベイズ型の閉ループシステムは、測定された性能から次の実験を自動選択し、触媒発見を加速する。自律実験室では、格子探索よりはるかに少ない実験数で活性の高い触媒組成を見つけられる。 | 5-20x fewer experiments than exhaustive composition screening in examples | [Autonomous Discovery of Catalysts in a Self-Driving Laborato...]((no url)) |
| 3 | 2023 | 生成AIとロボット実験を組み合わせることで、実験提案、実行、モデル更新を閉ループ化し、触媒最適化を高速化する。触媒発見サイクルを数か月から数日または数週間に短縮できる。 | months to days or weeks in robotic campaigns | [Self-Driving Laboratories for Accelerated Catalyst Optimizat...]((no url)) |

### AGRI-FOOD-CROP — 作物科学 (Crop Science)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2025 | 植物病害抵抗性育種へのAI活用を論じた総説。CNNと関連深層学習手法による植物病害検出・オミクス予測が概説され、高スループットフェノタイピングのフィールドロボット（LiDARと高分光センサー）が葉角分布・草高・バイオマスを測定しつつ、専門家目視評価と比較して90–95%の精度で病害症状を検出することが示された。 | 90-95% accuracy compared to expert visual ratings | [Artificial Intelligence-Assisted Breeding for Plant Disease...](https://www.mdpi.com/1422-0067/26/11/5324) |
| 2 | 2024 | 生成AIは、農学的目標を偵察、除草、散布、収穫ロボットのタスク計画に変換することで、ロボットによる作物作業を加速する。自然言語による計画は、農家や技術者のプログラミング負担を減らせる。 | task plans generated from natural-language instructions | [CORDIS Results Pack on Robotics and AI for Agriculture]((no url)) |

### EARTH-SCI-OCEAN — 海洋学 (Oceanography)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2025 | 生成モデルは、グライダーや水中ロボットの観測を圧縮、要約、優先順位付けし、自律海洋ロボット運用を高速化する。帯域幅が限られる任務でも、科学的に重要なデータをより早く送信できる。 | 2-5x more high-priority observations | [NIH Outcome Report: AI for Autonomous Marine Robotics Data T...]((no url)) |
| 2 | 2024 | 生成計画モデルは、不確実な海流、バッテリー制約、目標特徴に応じてAUV経路を適応できる。配備ごとのデータ収量を増やし、海洋調査を高速化する。 | +10-30% target coverage | [Generative Models for Autonomous Underwater Vehicle Mission...]((no url)) |

### ENERGY-GRID — 電力網 (Grid Optimization)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2023 | 視覚言語モデルは、ドローン画像、熱画像、保守記録を要約し、変電所や送電設備の点検を加速する。現場技術者はすべてのメディアを手作業で確認する代わりに、優先順位付きの欠陥候補を受け取る。 | 30-70% reduction in image review time | [JST Report on AI-Enhanced Power Equipment Maintenance]((no url)) |
| 2 | 2024 | 視覚言語モデルは赤外線画像、ドローン画像、保守記録を統合してラベル付けし、変電所点検の優先順位付けと設備リスク評価を高速化できる。 | 2x-5x faster review of image batches | [Vision-Language Models for Substation Inspection and Asset M...]((no url)) |

### COMP-SCI-CV — コンピュータビジョン (Computer Vision)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2023 | 生成的ニューラルレンダリングは、限られた画像から視点合成を学習し、3Dアセットやシーン再構築を高速化する。ロボティクス、シミュレーション、デジタルツインの手作業モデリング時間を減らす。 | minutes to hours instead of days of manual modeling | [Generative AI for 3D Scene Reconstruction and Neural Renderi...]((no url)) |

### SOC-SCI-PSYCH — 心理学 (Psychology)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2023 | LLMベースの合成参加者は、人間のデータ収集前に調査文言や実験操作を検証し、心理学研究の初期段階を加速する。 | near-zero marginal cost for thousands of simulated responses | [Large Language Models as Synthetic Participants in Social Ps...]((no url)) |

### CHEM-COMPHEM — 計算化学 (Computational Chemistry)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2023 | 生成AIは、自律実験室と接続されることで分子や反応条件を提案し、実験を行い、モデルを更新して化学研究を加速する。閉ループシステムは特定課題で設計・構築・試験・学習の周期を数カ月から数日に近づける。 | days rather than weeks or months in selected demonstrations | [Self-Driving Laboratories and Generative Design in Chemistry]((no url)) |

### EARTH-SCI-SEISMO — 地震学 (Seismology)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2024 | マルチモーダル生成モデルは、衛星、ドローン、街路画像を被害カテゴリに要約し、解析者の確認に回すことで地震後の現地把握を加速する。 | 2x-4x faster image triage | [Vision-Language Models for Rapid Earthquake Damage Interpret...]((no url)) |

### ECON-BIZ-SUPPLY — サプライチェーン (Supply Chain & Logistics)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2024 | 視覚言語モデルや言語モデルは、画像やWMSイベントからピッキング経路の説明、ロボット作業計画、例外報告を生成し、倉庫業務を高速化する。人と自動化設備が混在する環境で管理者の負担を減らす。 | 15-35% reduction in pilot settings | [Generative AI for Warehouse Operations: Human-Robot Task Pla...]((no url)) |

### MATH-STAT-THEOREM — 定理証明 (Theorem Proving)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2024 | 生成モデルは、記号エンジンが検証する変換、置換、正規形を提案し、代数的定理証明を高速化する。記号操作の選択が重要な恒等式や漸化式証明で探索を改善する。 | fewer transformation steps explored in selected tasks | [Neural-Symbolic Systems for Algebraic Identity Proving]((no url)) |

### LAW-POLICY-IP — 知的財産 (Intellectual Property)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2024 | 生成AIは、出願ドラフト内の用語不一致、裏付けのない請求項要素、不足する実施形態を検出し、特許品質レビューを加速する。出願前に回避可能な拒絶理由を減らし得る。 | higher first-pass consistency checks | [JST Policy Brief on AI-Assisted Patent Quality Metrics]((no url)) |

### ENERGY-BATTERY — バッテリー (Battery & Energy Storage)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2023 | 生成AIは、過去の合成、評価、サイクル試験結果に基づいて次の実験を提案し、自律型電池ラボを加速している。設計・作製・試験・学習のループを手動計画よりも速く回す。 | fewer experiments to identify promising conditions | [Self-Driving Labs for Energy Materials: UKRI Infrastructure...]((no url)) |

### ENERGY-FUSION — 核融合 (Fusion Energy)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2024 | 生成AIは、CAD、センサーデータ、手順書をロボット作業計画へ変換することで、核融合施設の遠隔保守計画を加速する。危険またはアクセス困難な炉内部品の計画周期を短縮できる。 | 30%-60% reduction in draft procedure time | [NEDO Outcome Documents on Robotics and Remote Maintenance fo...]((no url)) |

### MATH-STAT-OPTIM — 最適化 (Optimization)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2024 | 世界モデルは、制御方策のためのシミュレーション軌跡を生成し、強化学習による最適化を加速する。ロボットや産業制御で必要な高コストの実システム相互作用を減らす。 | 5x-50x fewer real interactions | [NEDO Outcome Summary on Reinforcement Learning and Generativ...]((no url)) |

### LIFE-SCI-SYNBIO — 合成生物学 (Synthetic Biology)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2025 | 生成的実験計画モデルは、ロボット試験に有益な構築物や条件を選び、DNAアセンブリ最適化を加速する。閉ループシステムは失敗したアセンブリから学習し、総当たり実験なしにプロトコル選択を改善できる。 | 50-80% fewer experiments than grid search | [Closed-Loop Self-Driving Labs for DNA Assembly Optimization]((no url)) |

### LIFE-SCI-PROTEIN — タンパク質科学 (Protein Science)

| # | 年 | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|
| 1 | 2025 | 自律型タンパク質工学プラットフォームは、生成設計、ロボット合成、ハイスループットアッセイ、能動学習を統合し、発見を加速する。モデル提案から実験フィードバックまでの閉ループを数週間ではなく数日で回せる。 | days instead of weeks in automated platforms | [Self-Driving Protein Engineering Platforms with Generative D...]((no url)) |

---

## Task 2 — 加速曲線（cost-down / performance / speedup）30 件

`has_quantitative_evidence=1` かつ key_metric_value に倍率・削減・コスト・加速語を含むもの。credibility 降順。

| # | 年 | ドメイン | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|---|
| 1 | 2023 | バッテリー | ML potentials enable quantum-accurate atomistic simulations with 2-4 orders of magnitude speedup over density functional theory, and ML-driven screening efficiently navigates vast... | 2-4 orders of magnitude speedup; 75% discovery time reduction for solar cells (15-year acceleration) | [Machine learning for accelerating energy materials...](https://advanced.onlinelibrary.wiley.com/doi/10.1002/aenm.202503356) |
| 2 | 2024 | バッテリー | AI is driving a battery revolution from material discovery through smart manufacturing. Argonne National Laboratory is building AI foundation models to accelerate discovery of new... | 2-4 orders of magnitude speedup | [Accelerating the Battery Revolution: AI-Driven Mul...](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adfm.202514830) |
| 3 | 2024 | 炭素回収 | CCS分野のAI文献が2021-2024年で急速に成長（12.1%→21.6%）。GNNとCIF構造情報によるMOFスクリーニング、炭素回収効率20%向上・エネルギー消費15%削減を実現。 | 炭素回収効率20%向上、エネルギー消費15%削減 | [AI-driven Carbon Capture and Storage: emerging tec...](https://www.sciencedirect.com/science/article/pii/S2772656826000096) |
| 4 | 2021 | 分子生成 | Rentosertib (ISM001-055), a first-in-class AI-generated small-molecule TNIK inhibitor for idiopathic pulmonary fibrosis, showed safety and efficacy in a randomized Phase 2a trial o... | 18 months, <$2.6 million (vs years and hundreds of millions traditionally) | [A generative AI-discovered TNIK inhibitor for idio...](https://www.nature.com/articles/s41591-025-03743-2) |
| 5 | 2023 | 化学 | LLMs and autonomous agents are transforming chemistry through enhanced molecular design, property prediction, synthesis optimization, and laboratory automation. MoLFormer reduced G... | 60x reduction in GPU usage (MoLFormer) | [A review of large language models and autonomous a...](https://pubs.rsc.org/en/content/articlehtml/2025/sc/d4sc03921a) |
| 6 | 2024 | 計算機科学・AI | Analysis of 41.3 million papers shows AI adoption enables scientists to publish 3.02 times more papers and receive 4.84 times more citations, while achieving research leadership 1.... | 3.02x papers, 4.84x citations, 1.37 years earlier leadership; -4.63% topic volume, -22% collaboratio... | [Artificial Intelligence Tools Expand Scientists' I...](https://www.nature.com/articles/s41586-025-09922-y) |
| 7 | 2023 | バッテリー | AI significantly reduces the time and cost of conventional trial-and-error experimentation and density functional theory calculations for electrocatalyst discovery. Research shows... | up to 20x acceleration vs random acquisition | [AI-Accelerated Discovery of Electrocatalyst Materi...](https://pubs.acs.org/doi/10.1021/acsmaterialsau.5c00135) |
| 8 | 2023 | タンパク質構造予測 | AI has reduced time and costs for antibody design by minimizing failures and increasing success rates. Language-model-guided affinity maturation achieved improved binding affinitie... | up to 7x for mature antibodies; up to 160x for unmatured antibodies | [Artificial intelligence in therapeutic antibody de...](https://www.sciencedirect.com/science/article/abs/pii/S0959440X25001022) |
| 9 | 2025 | タンパク質科学 | AI×LLM×バイオファウンドリー自動化統合プラットフォームが人間の介在なく酵素工学を実行。1酵素で基質選択性90倍向上・エチル転移活性16倍向上を達成。別の酵素では中性pH活性26倍向上。 | 90倍向上 | [A generalized platform for artificial intelligence...](https://www.nature.com/articles/s41467-025-61209-y) |
| 10 | 2025 | 電力網 | DRL最適化データセンターエネルギー管理システムが従来手法比でエネルギーコスト38%削減・エネルギー効率82%向上・炭素排出45%削減を達成。 | エネルギーコスト38%削減、CO2排出45%削減 | [Deep reinforcement learning for data center green...](https://arxiv.org/html/2507.21153v1) |
| 11 | 2024 | 政治学 | 機械学習・ディープラーニング・NLPによる誤情報検出が政治科学に普及。BERT・GPTアーキテクチャがフェイクニュース・ボット検出・政治的操作コンテンツの識別に有効。NewsGuardによれば2023年にAI生成フェイクニュースサイトが10倍増加 | 2023年に10倍増（NewsGuard） | [AI in Disinformation Detection — Frontiers in Poli...](https://www.frontiersin.org/journals/political-science/articles/10.3389/fpos.2025.1517726/full) |
| 12 | 2025 | 経済・ビジネス | S&Pグローバルの調査では、2024年にほとんどのAI取り組みを放棄した企業が42%に達し、前年の17%から急増した | 17%→42%（1年で2.5倍増） | [S&P Global: 42% of companies abandoned most AI ini...](https://www.directual.com/blog/ai-agents-in-2025-why-95-of-corporate-projects-fail) |
| 13 | 2025 | メンタルヘルス | LLMは面接記録の共感、反映、CBT忠実度を評価し、手作業のスーパービジョンだけの場合より頻繁なフィードバックを可能にして療法士訓練を加速する。 | 5-10x more reviewed sessions | [Generative AI supervision aids for therapist train...]((no url)) |
| 14 | 2025 | 精密農業 | 生成最適化は、分散と労力を減らす区画配置や適応的サンプリング計画を提案し、精密圃場試験を加速する。 | 10-30% fewer plots for similar power | [Generative AI for field experiment layout and adap...]((no url)) |
| 15 | 2025 | 人事・組織 | LLMは、コミュニケーションのメタデータやテキストから協働テーマ、調整ボトルネック、役割シグナルを抽出し、組織ネットワーク分析を加速する。組織摩擦の迅速な診断を可能にする。 | large communication samples coded faster than manual qualitative analysis | [Generative AI for Organizational Network Analysis...]((no url)) |
| 16 | 2025 | 定理証明 | 生成AIを用いた自然言語インターフェースは、証明支援系の構文を知らない数学者の形式的定理証明への参入障壁を下げる。主な定量的利得は、非形式的な問題文から検査済みの形式的試行までの時間短縮である。 | roughly 2x faster completion of introductory formalization tasks in user studies | [Natural Language Interfaces to Formal Proof Assist...]((no url)) |
| 17 | 2025 | 触媒化学 | 生成AIは、合成前に目標酸化還元電位、吸収プロファイル、三重項エネルギーを持つ候補を提案し、光触媒発見を加速できる。閉ループのケーススタディでは、利用可能な光触媒を見つけるまでの合成・スクリーニングサイクルが減ると報告されている。 | 2-4x fewer cycles in reported photocatalyst optimization studies | [Generative AI for Photocatalyst Discovery in Organ...]((no url)) |
| 18 | 2025 | 触媒化学 | タンパク質基盤モデルは、標的反応向けの酵素足場や活性部位変異体を生成し、生体触媒設計を加速する。定量報告では、測定可能な触媒活性を得るために必要な実験ライブラリサイズが大きく削減されることが示されている。 | 10-100x fewer variants screened to find active designs in selected enzyme-design tasks | [Generative Design of Enzyme-Like Catalysts with Pr...]((no url)) |
| 19 | 2025 | ビジュアルアート | デザインチームの制御研究では、AI画像生成が曖昧性の低い視覚タスクを速める一方、多くの利用者が似たプロンプトに頼ると差別化が低下しうることが示されている。スループット面の加速は実在するが、独創性の向上は専門的なキュレーションに依存する。 | 20-40% faster completion but lower inter-team distinctiveness in some tasks | [Human Preference and Productivity Effects of AI Im...]((no url)) |
| 20 | 2025 | ビジュアルアート | 視覚デザイン教育の研究は、生成AIが学生の反復案数を増やし、視覚フィードバックを速めることを示している。加速は探索を改善するが、制約なしに使うと基礎的なスケッチ練習を弱める可能性がある。 | 2-3x more iterations; mixed effects on originality ratings | [Generative AI and Visual Design Education: Product...]((no url)) |
| 21 | 2024 | ロボティクス | 生成対話システムは、タスク台本、失敗時の復旧発話、ユーザー調査のバリエーションを生成し、人間・ロボット相互作用の試作を加速する。 | 2-4x more dialogue variants per design cycle | [Language Models Enable Faster Human-Robot Interact...]((no url)) |
| 22 | 2025 | バッテリー | 生成的な組成探索は、電圧、安定性、原材料制約を両立する置換候補を提案し、低コバルト正極開発を加速する。 | 2-4x higher hit rate for target property windows | [AI-Guided Discovery of Low-Cobalt Cathode Composit...]((no url)) |
| 23 | 2025 | 土木・構造 | 生成サロゲートモデルは、多数の地震動や設計案に対する非線形動的シミュレーションを近似し、耐震設計を加速する。 | 100-1000x faster scenario evaluation | [Generative Surrogate Models for Seismic Structural...]((no url)) |
| 24 | 2025 | 土木・構造 | 生成サロゲートモデルは、多数の降雨、土地利用、排水対策シナリオの水理シミュレーションをエミュレートし、雨水計画を加速する。 | 100x faster screening of intervention portfolios | [Generative Urban Drainage Models for Rapid Flood-R...]((no url)) |
| 25 | 2025 | 医用画像 | 生成型マルチモーダル支援は、リアルタイムのプローブ誘導、解剖ラベル付け、動画からのフィードバック生成により、超音波トレーニングを加速する。 | 20-40% faster acquisition of standard views in simulations | [Generative AI for Ultrasound Guidance and Skill Tr...]((no url)) |
| 26 | 2024 | 心理学 | LLMは、項目プール、言い換え、読みやすさを調整した版を生成し、後続の実証検証に向けた心理尺度開発を加速する。 | 10-50x more candidate items per hour | [LLMs for Psychological Scale Development and Item...]((no url)) |
| 27 | 2025 | 心理学 | 生成AIは、利用者の目標や症状プロファイルに合わせてワークシート、リマインダー、心理教育テキストを調整し、デジタルCBT提供を加速する。 | minutes instead of clinician-hours for draft materials | [Generative AI for Personalized Digital Cognitive B...]((no url)) |
| 28 | 2025 | 心理学 | LLMエージェントは、多様なエージェントのプロフィール、意思決定ルール、会話的相互作用を生成し、社会・心理シミュレーションを加速する。 | days to hours for prototype agent models | [Generative AI for Social-Science Agent-Based Model...]((no url)) |
| 29 | 2024 | 教育コンテンツ | 教師とAIの共同制作ワークフローは、検索、要約、書き換え、ライセンス情報作成を組み合わせ、オープン教材制作を加速する。ワークシート、短い授業、解説ページのようなモジュール型教材で効果が特に見えやすい。 | 2-5x more draft modules per authoring session | [Teacher-AI Co-Creation of Open Educational Resourc...]((no url)) |
| 30 | 2024 | 炭素回収 | 生成AIは低濃度CO2吸着、湿度耐性、再生エネルギーに最適化された吸着材を設計し、直接空気回収材料の探索を加速する。手作業だけでは大きすぎる化学設計空間の探索を支援する。 | fewer lab tests per high-capacity candidate | [Generative AI for Direct Air Capture Material Disc...]((no url)) |

---

## Task 3 — 2025-2026 決定的瞬間 20 件

claim_emerged_year / claim_year_start / published_year のいずれかが 2025-2026 で、verified もしくは credibility ≥ 0.85。

| # | 年 | ドメイン | 出来事 | 数値 | コンセンサス | 出典URL |
|---|---|---|---|---|---|---|
| 1 | 2026 | 触媒化学 | 不均一系触媒のAI変革ロードマップが、AIレディデータエコシステム・マルチモーダル基盤モデル・自律実験室の3段階で触媒技術の加速を提示。 | データエコシステム→基盤モデル→自律実験室の3段階 | GROWING | [Roadmap for transforming heterogeneous catalysis w...](https://www.nature.com/articles/s41929-026-01479-x) |
| 2 | 2026 | 社会科学 | 一般市民はAI生成コンテンツを尤もらしいと感じても懐疑的なままであり、AI補助研究の受容に課題がある。AIは社会科学研究者が行う人間認知の種類の過程をまだ実行していない |  | GROWING | [How social science academics use AI: Activities an...](https://journals.sagepub.com/doi/10.1177/01655515251396892) |
| 3 | 2026 | ゲノム医療 | AI駆動ゲノム医学の包括的レビュー。Mayo ClinicのAI+薬理ゲノミクスが関節リウマチ薬（メトトレキサート）への反応をゲノム・臨床データで予測し、CYP2C9・VKORC1変異からワルファリン投与量をガイドするAIモデルが臨床実装済み。NGSによる精密医療市場は2024年の62.1億ドルから2034年には320.1億ドルへ成長見込み。 | NGS precision medicine market USD 6.21B (2024) → USD 32.01B (2034) | GROWING | [AI-driven genomic medicine: A comprehensive review...](https://www.sciencedirect.com/science/article/pii/S2666521226000232) |
| 4 | 2026 | 製造・ロボティクス | AIデジタルツインが製造業全階層（設備・ライン・工場・サプライチェーン）にわたり変革をもたらすことを示した包括的レビュー。予測保全・プロセス最適化・品質管理・動的スケジューリングに深層強化学習とCNNが活用されている。2020〜2024年の51事例中44事例がAI強化デジタルツインの予測保全への適用。 | 44 out of 51 AI-enhanced digital twin cases focused on predictive maintenance (2... | GROWING | [AI-Driven Digital Twins for Manufacturing: A Revie...](https://www.mdpi.com/1424-8220/26/1/124) |
| 5 | 2026 | 作物科学 | ゲノム技術・AI・CRISPRゲノム編集・高スループットフェノタイピングの統合により病害抵抗性作物の工学的育種を加速することを論じた最新レビュー。AIがCRISPR標的設計・ゲノム予測・フェノタイプ解析を統合し、これまでの育種期間を大幅短縮する可能性を示す。 | AI+CRISPR+genomics+HTP integration enables accelerated disease-resistant crop de... | EMERGING | [Integrating genomic technologies with artificial i...](https://www.sciencedirect.com/science/article/pii/S2667064X26001004) |
| 6 | 2026 | 医用画像 | EU加盟27か国中74%がAI支援診断（医療画像・疾患検出・臨床意思決定支援）をすでに活用。63%がチャットボットによる患者エンゲージメント支援を導入。全27か国が「患者ケアの改善」をAI導入の主要動機として挙げた。 | EU27か国中74% | GROWING | [Artificial Intelligence is Reshaping Health System...](https://www.who.int/europe/publications/i/item/WHO-EURO-2025-12707-52481-81028) |
| 7 | 2026 | 医療・健康 | EU加盟国の半数近くがAI・データサイエンス専門職を医療分野に新設。多くの国がAI研修プログラムの導入・拡充を計画している。AIが保健システムの主要機能（普遍的医療保障・緊急対応・健康増進）全体にわたって活用されていることが調査で確認された。 | EU加盟国の半数近く | GROWING | [Artificial Intelligence is Reshaping Health System...](https://www.who.int/europe/publications/i/item/WHO-EURO-2025-12707-52481-81028) |
| 8 | 2026 | 材料設計 | AI for Scienceの材料科学分野では「ユーザー所望の特性を実現する材料構造とその製造方法の提案」が主要AIアプリケーションとして確認。広大な材料データで学習した基盤モデルが従来の限界を超えた革命的材料の迅速発見・開発を可能にするとCRDSは評価。 |  | CONTESTED | [AI for Scienceの動向2026 ─ AIトランスフォーメーションに伴う科学技術・イノベー...](https://www.jst.go.jp/crds/report/CRDS-FY2025-RR-05.html) |
| 9 | 2026 | 生命科学 | 生命科学分野では薬物候補探索・細胞刺激応答予測・疾患適応予測がAIの主要応用として特定。生物AI基盤モデルが複雑な生命現象の解明・高精度バイオ分子構造予測・代謝・合成プロセス予測を可能にし、バイオ製造・創薬研究の速度を向上。 |  | GROWING | [AI for Scienceの動向2026 ─ AIトランスフォーメーションに伴う科学技術・イノベー...](https://www.jst.go.jp/crds/report/CRDS-FY2025-RR-05.html) |
| 10 | 2026 | 気象学 | CRDSは気象・宇宙を材料発見・生命科学とともに日本がAI特化基盤モデルで競争優位を狙える分野として特定。AIが科学研究の「第5のパラダイム」（経験科学・理論科学・計算科学・データ駆動科学を統合する新パラダイム）を形成するとする概念を提示。 |  | GROWING | [AI for Scienceの動向2026 ─ AIトランスフォーメーションに伴う科学技術・イノベー...](https://www.jst.go.jp/crds/report/CRDS-FY2025-RR-05.html) |
| 11 | 2025 | 気候モデリング | AI-driven weather forecast models can accelerate climate change attribution studies for heatwaves, enabling rapid estimation of how climate change altered the probability and inten... |  | EMERGING | [AI-driven weather forecasts to accelerate climate...](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025EF006453) |
| 12 | 2025 | 分子生成 | 生成AI設計薬剤ISM001-055がIPF Phase 2a試験でプラセボ比FVC+98.4mLの改善を達成。ターゲット同定〜Phase1完了まで30ヶ月（従来4〜6年） | +98.4 mL (60mg群) vs −62.3 mL (プラセボ群) | GROWING | [A generative AI-discovered TNIK inhibitor for idio...](https://www.nature.com/articles/s41591-025-03743-2) |
| 13 | 2025 | 生命科学 | AlphaGenomeが26のバリアント効果予測評価中24で既存最良モデルと同等以上の精度を示し、sQTL予測でAUC 0.80、ipaQTL予測でAUC 0.86を記録 | sQTL: AUC=0.80、ipaQTL: AUC=0.86；26評価中24で最高水準達成 | GROWING | [AlphaGenome: advancing regulatory variant effect p...](https://www.nature.com/articles/s41586-025-10014-0) |
| 14 | 2025 | 分子生成 | RSGPTは100億データポイントで事前訓練した生成トランスフォーマーモデルで逆合成計画を実行。創薬向けの反応クラスでTop-10ラウンドトリップ精度0.97以上を達成。大規模事前訓練が合成計画精度を劇的に向上。 | 0.97以上 | GROWING | [RSGPT: a generative transformer model for retrosyn...](https://www.nature.com/articles/s41467-025-62308-6) |
| 15 | 2025 | 合成生物学 | AIが単にCRISPRガイドRNA設計を改善するだけでなく、新たなCRISPRシステム自体の発見・設計を可能にしつつある。AIによるCRISPRと合成生物学の収束が遺伝子治療・作物改良・基礎研究を加速。 |  | GROWING | [Revolutionizing CRISPR technology with artificial...](https://www.nature.com/articles/s12276-025-01462-9) |
| 16 | 2025 | 創薬 | 世界初の生成AIによる完全設計薬Rentosertib（INS018_055）が特発性肺線維症フェーズ2a試験を完了。薬剤投与群はFVCが平均98.4ml改善、プラセボ群は20.3ml低下。ターゲット発見からPhase 2まで通常の半分以下の30ヶ月以内で到達。 | 薬剤群+98.4ml vs プラセボ群-20.3ml | EMERGING | [A generative AI-discovered TNIK inhibitor for idio...](https://www.nature.com/articles/s41591-025-03743-2) |
| 17 | 2025 | ゲノミクス | Evo 2は9兆塩基対のDNAデータで訓練した基盤モデルで、生命の全ドメインにまたがるゲノムをモデル化。BRCA1の臨床的に重要な変異を含む病原性変異の機能的影響を微調整なしに予測。 | 9兆塩基対（生命の全ドメイン） | GROWING | [Genome modelling and design across all domains of...](https://www.nature.com/articles/s41586-026-10176-5) |
| 18 | 2025 | 神経科学 | AIコパイロット（共有自律性）をBCIに統合することで運動BCIのパフォーマンスを大幅向上。CNNとReFIT-likeカルマンフィルタのハイブリッドアダプティブデコーディングにより、健常者と麻痺患者が脳波信号でカーソルとロボットアームを制御。 |  | GROWING | [Brain–computer interface control with artificial i...](https://www.nature.com/articles/s42256-025-01090-y) |
| 19 | 2025 | 合成生物学 | CRISPR-GPTはLLMエージェントシステムとしてCRISPRベースの遺伝子編集設計・データ解析を自動化。CRISPRシステム選択、実験計画、gRNA設計、デリバリー手法選択、プロトコル作成、データ解析まで一気通貫で支援。 |  | GROWING | [CRISPR-GPT for agentic automation of gene-editing...](https://www.nature.com/articles/s41551-025-01463-z) |
| 20 | 2025 | 合成生物学 | AI配列モデリングにより高機能なCRISPR-Casゲノム編集ツールをde novoで設計。天然CRISPRシステムの配列空間を超えた新規編集ツールを設計・機能的に検証。 |  | GROWING | [Design of highly functional genome editors by mode...](https://www.nature.com/articles/s41586-025-09298-z) |

---

## Task 4 — 97 ドメインのうち Physical AI 関連ドメイン全列挙

AA-DB の 97 ドメインを Physical AI への関連度で 3 階層に分類。括弧内は mention 件数。

### A. 中核 (Primary) — Physical AI ど真ん中

| ID | 和名 | 英名 | level | mentions |
|---|---|---|---|---|
| COMP-SCI-ROBOTICS | ロボティクス | Robotics | L2 | 50 |
| ENGINEERING-MFCT | 製造・ロボティクス | Manufacturing & Robotics | L2 | 42 |

### B. 周縁 (Periphery) — Physical AI の感覚器・基盤技術・応用先

| ID | 和名 | 英名 | level | mentions |
|---|---|---|---|---|
| PHYS-SCI | 物理・材料科学 | Physical & Materials Sciences | L1 | 55 |
| AGRI-FOOD-CROP | 作物科学 | Crop Science | L2 | 53 |
| AGRI-FOOD-PRECISION | 精密農業 | Precision Agriculture | L2 | 52 |
| CHEM-CATALY | 触媒化学 | Catalysis | L2 | 56 |
| CHEM-SYNTH | 合成化学 | Synthetic Chemistry | L2 | 54 |
| CLIMATE-ENV-CARBON | 炭素回収 | Carbon Capture & Sequestration | L2 | 49 |
| CLIMATE-ENV-REMOTE | リモートセンシング | Remote Sensing & Earth Observation | L2 | 54 |
| COMP-SCI-CV | コンピュータビジョン | Computer Vision | L2 | 52 |
| COMP-SCI-NLP | 自然言語処理 | Natural Language Processing | L2 | 59 |
| EARTH-SCI-OCEAN | 海洋学 | Oceanography | L2 | 50 |
| EARTH-SCI-SEISMO | 地震学 | Seismology | L2 | 49 |
| EARTH-SCI-WEATHER | 気象学 | Weather Forecasting | L2 | 53 |
| ENERGY-BATTERY | バッテリー | Battery & Energy Storage | L2 | 51 |
| ENERGY-FUSION | 核融合 | Fusion Energy | L2 | 50 |
| ENERGY-GRID | 電力網 | Grid Optimization | L2 | 48 |
| ENGINEERING-CHEM | 化学工学 | Chemical Engineering | L2 | 52 |
| ENGINEERING-CIVIL | 土木・構造 | Civil & Structural Engineering | L2 | 54 |
| ENGINEERING-ELEC | 電気・電子 | Electrical & Electronic Engineering | L2 | 52 |
| LIFE-SCI-DRUG | 創薬 | Drug Discovery | L2 | 53 |
| LIFE-SCI-ECOLOGY | 生態学 | Ecology & Biodiversity | L2 | 55 |
| LIFE-SCI-SYNBIO | 合成生物学 | Synthetic Biology | L2 | 43 |
| MED-HEALTH-IMAGING | 医用画像 | Medical Imaging | L2 | 53 |
| PHYS-SCI-MATDESIGN | 材料設計 | Materials Design & Discovery | L2 | 52 |
| SPACE-ASTRO | 天文学 | Astronomy & Astrophysics | L2 | 66 |
| SPACE-EXOPLANET | 系外惑星 | Exoplanet Detection | L2 | 47 |
| EARTH-SCI-WEATHER-NOWCAST | ナウキャスト | Nowcasting | L3 | 2 |
| MED-HEALTH-IMAGING-PATH | 病理画像 | Pathology Image Analysis | L3 | 1 |
| MED-HEALTH-IMAGING-RADIOL | 放射線AI | Radiology AI | L3 | 3 |
| PHYS-SCI-MATDESIGN-BATTERY | バッテリー材料 | Battery Materials Discovery | L3 | 2 |
| PHYS-SCI-MATDESIGN-CATALYST | 触媒材料 | Catalyst Materials | L3 | 0 |
| PHYS-SCI-MATDESIGN-POLYMER | 高分子材料 | Polymer Design | L3 | 1 |

### C. 他全 97 ドメイン（参考リスト）

| ID | 和名 | 英名 | level | mentions |
|---|---|---|---|---|
| AGRI-FOOD | 農業・食料 | Agriculture & Food | L1 | 6 |
| CHEM | 化学 | Chemistry | L1 | 260 |
| CLIMATE-ENV | 気候・環境科学 | Climate & Environmental Sciences | L1 | 3 |
| COMP-SCI | 計算機科学・AI | Computer Science & AI | L1 | 501 |
| CREATIVE | 創造的芸術・メディア | Creative Arts & Media | L1 | 1 |
| EARTH-SCI | 地球科学 | Earth Sciences | L1 | 3 |
| ECON-BIZ | 経済・ビジネス | Economics & Business | L1 | 371 |
| EDUCATION | 教育 | Education | L1 | 13 |
| ENERGY | エネルギー | Energy | L1 | 6 |
| ENGINEERING | 工学・技術 | Engineering & Technology | L1 | 10 |
| HUMANITIES | 人文学 | Humanities | L1 | 24 |
| LAW-POLICY | 法・政策 | Law & Policy | L1 | 9 |
| LIFE-SCI | 生命科学 | Life Sciences | L1 | 8 |
| MATH-STAT | 数学・統計学 | Mathematics & Statistics | L1 | 5 |
| MED-HEALTH | 医療・健康 | Medicine & Health | L1 | 288 |
| SOC-SCI | 社会科学 | Social Sciences | L1 | 81 |
| SPACE | 宇宙科学 | Space Sciences | L1 | 10 |
| CHEM-COMPHEM | 計算化学 | Computational Chemistry | L2 | 48 |
| CLIMATE-ENV-MODEL | 気候モデリング | Climate Modeling | L2 | 271 |
| COMP-SCI-CYBERSEC | サイバーセキュリティ | Cybersecurity | L2 | 55 |
| COMP-SCI-SE | ソフトウェア工学 | Software Engineering | L2 | 54 |
| CREATIVE-FILM | 映像 | Film & Video Production | L2 | 45 |
| CREATIVE-GAME | ゲーム | Game Development | L2 | 49 |
| CREATIVE-MUSIC | 音楽 | Music Composition | L2 | 50 |
| CREATIVE-VISUAL | ビジュアルアート | Visual Arts & Design | L2 | 52 |
| CREATIVE-WRITING | 創作文章 | Creative Writing | L2 | 54 |
| ECON-BIZ-FINANCE | 金融 | Finance & Investment | L2 | 42 |
| ECON-BIZ-HR | 人事・組織 | HR & Organizational Science | L2 | 58 |
| ECON-BIZ-MARKET | マーケティング | Marketing & CRM | L2 | 54 |
| ECON-BIZ-SUPPLY | サプライチェーン | Supply Chain & Logistics | L2 | 51 |
| EDUCATION-ASSESS | 評価・アセスメント | Assessment & Evaluation | L2 | 59 |
| EDUCATION-CONTENT | 教育コンテンツ | Educational Content Creation | L2 | 55 |
| EDUCATION-TUTOR | 個別指導 | Intelligent Tutoring | L2 | 45 |
| LAW-POLICY-COMPLIANCE | 規制コンプライアンス | Regulatory Compliance | L2 | 56 |
| LAW-POLICY-CONTRACT | 契約分析 | Contract Analysis | L2 | 48 |
| LAW-POLICY-IP | 知的財産 | Intellectual Property | L2 | 49 |
| LIFE-SCI-GENOMICS | ゲノミクス | Genomics & Sequencing | L2 | 57 |
| LIFE-SCI-NEUROSCI | 神経科学 | Neuroscience | L2 | 51 |
| LIFE-SCI-PROTEIN | タンパク質科学 | Protein Science | L2 | 54 |
| MATH-STAT-OPTIM | 最適化 | Optimization | L2 | 49 |
| MATH-STAT-THEOREM | 定理証明 | Theorem Proving | L2 | 52 |
| MED-HEALTH-CLINICAL | 臨床意思決定支援 | Clinical Decision Support | L2 | 50 |
| MED-HEALTH-EPIDEM | 疫学 | Epidemiology & Public Health | L2 | 47 |
| MED-HEALTH-GENOMICMED | ゲノム医療 | Genomic Medicine | L2 | 55 |
| MED-HEALTH-MENTAL | メンタルヘルス | Mental Health | L2 | 50 |
| PHYS-SCI-CONDMAT | 凝縮系物理 | Condensed Matter Physics | L2 | 63 |
| PHYS-SCI-PARTICLE | 素粒子物理 | Particle & High-Energy Physics | L2 | 65 |
| PHYS-SCI-QUANTUM | 量子コンピューティング | Quantum Computing | L2 | 53 |
| SOC-SCI-ANTHRO | 文化人類学 | Anthropology | L2 | 66 |
| SOC-SCI-POLSCI | 政治学 | Political Science | L2 | 54 |
| SOC-SCI-PSYCH | 心理学 | Psychology | L2 | 52 |
| SOC-SCI-SOCIOL | 社会学 | Sociology | L2 | 66 |
| CLIMATE-ENV-MODEL-DOWNSCALE | 気候ダウンスケーリング | Climate Downscaling | L3 | 1 |
| COMP-SCI-SE-CODEGEN | コード生成 | Code Generation | L3 | 8 |
| COMP-SCI-SE-TESTING | テスト自動化 | Automated Testing | L3 | 0 |
| ECON-BIZ-FINANCE-QUANT | 定量取引 | Quantitative Trading | L3 | 191 |
| ECON-BIZ-FINANCE-RISK | リスクモデリング | Credit & Risk Modeling | L3 | 1 |
| LIFE-SCI-DRUG-ADMET | ADMET予測 | ADMET Property Prediction | L3 | 5 |
| LIFE-SCI-DRUG-MOLGEN | 分子生成 | Molecular Generation / De Novo Design | L3 | 6 |
| LIFE-SCI-DRUG-PROTEIN | タンパク質構造予測 | Protein Structure Prediction | L3 | 10 |
| LIFE-SCI-DRUG-REPURPOSE | 薬剤リパーポジング | Drug Repurposing | L3 | 3 |
| LIFE-SCI-DRUG-TARGET | 標的同定 | Target Identification | L3 | 2 |
| LIFE-SCI-GENOMICS-SINGLECELL | シングルセル解析 | Single-Cell Analysis | L3 | 6 |
| LIFE-SCI-GENOMICS-VARIANT | 変異解釈 | Variant Interpretation | L3 | 3 |

---

## Task 5 — 連鎖加速 (cascade acceleration) パターン

AA-DB の taxonomy_mechanisms に直接 `cascade` ラベルは無いが、近接概念として **CROSS_DOMAIN_TRANSFER / SIMULATION_EMULATION / WORKFLOW_AUTOMATION / MULTIMODAL_ANALYSIS** の 4 メカニズムが Physical AI 領域に紐付くケースを抽出。これらは「他分野→ロボティクスへの知識・データ・モデル流入」「シミュレーションから実機への転移」「マルチモーダル統合による能力連鎖」を表す。

| # | 年 | ドメイン | メカニズム | 出来事 | 数値 | 出典URL |
|---|---|---|---|---|---|---|
| 1 | 2026 | 製造・ロボティクス | シミュレーション代替 (Simulation & Surrogate Modeling) | AIデジタルツインが製造業全階層（設備・ライン・工場・サプライチェーン）にわたり変革をもたらすことを示した包括的レビュー。予測保全・プロセス最適化・品質管理・動的スケジューリングに深層強化学習とCNNが活用されている。2020〜2024年の51事例中44事例がAI強化デジタルツインの予測保全への適用。 | 44 out of 51 AI-enhanced digital twin cases focused on predictive main... | [AI-Driven Digital Twins for Manufacturing: A...](https://www.mdpi.com/1424-8220/26/1/124) |
| 2 | 2026 | 製造・ロボティクス | 研究ワークフロー自動化 (Research Workflow Automation) | AIデジタルツインが製造業全階層（設備・ライン・工場・サプライチェーン）にわたり変革をもたらすことを示した包括的レビュー。予測保全・プロセス最適化・品質管理・動的スケジューリングに深層強化学習とCNNが活用されている。2020〜2024年の51事例中44事例がAI強化デジタルツインの予測保全への適用。 | 44 out of 51 AI-enhanced digital twin cases focused on predictive main... | [AI-Driven Digital Twins for Manufacturing: A...](https://www.mdpi.com/1424-8220/26/1/124) |
| 3 | 2025 | 作物科学 | マルチモーダル解析 (Multimodal Data Analysis) | 植物病害抵抗性育種へのAI活用を論じた総説。CNNと関連深層学習手法による植物病害検出・オミクス予測が概説され、高スループットフェノタイピングのフィールドロボット（LiDARと高分光センサー）が葉角分布・草高・バイオマスを測定しつつ、専門家目視評価と比較して90–95%の精度で病害症状を検出することが示された。 | 90-95% accuracy compared to expert visual ratings | [Artificial Intelligence-Assisted Breeding for...](https://www.mdpi.com/1422-0067/26/11/5324) |
| 4 | 2025 | 製造・ロボティクス | マルチモーダル解析 (Multimodal Data Analysis) | 機械ビジョンとYOLOv8ネットワークを統合した産業品質検査システム。製品表面欠陥を検出し分類指令をアクチュエータに送信することで製造ラインの品質管理を自動化する。人間検査員と比較して精度と速度が向上し、1枚の画像で複数の欠陥種を検出できる。 | YOLOv8 detects multiple defect types in single image, outperforming hu... | [An Industrial System for Inspecting Product Q...](https://www.worldscientific.com/doi/10.1142/S2196888825400032) |
| 5 | 2025 | 生態学 | マルチモーダル解析 (Multimodal Data Analysis) | 生成AIは、介入前後のドローン画像を比較し進捗要約を作成することで、生態系回復のモニタリングを加速する。回復チームは植生回復や侵食問題をより速く検出できる。 | faster post-intervention reporting | [Artificial Intelligence Index Report 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report) |
| 6 | 2024 | ロボティクス | シミュレーション代替 (Simulation & Surrogate Modeling) | 自己駆動型実験室（SDL）はAIと実験室ロボティクスを組み合わせ、科学的方法の全ステップ（物理的・知的）を自律的に実行する。NovartisのMicroCycleプラットフォームはSDLの最先端事例であり、新化合物の自律合成・精製・評価・データ解析・次サイクル設計を実行できる。Level-3自律性では複数の科学的方法サイクルを自律実行する。 | Level 3 SDLs can autonomously perform multiple cycles of scientific me... | [Self-driving laboratories with artificial int...](https://www.sciencedirect.com/science/article/abs/pii/S0098135425002698) |
| 7 | 2025 | 製造・ロボティクス | シミュレーション代替 (Simulation & Surrogate Modeling) | スマート製造システムの予測保全に向けたデータ駆動デジタルツインフレームワーク。リアルタイム監視・予測分析・自律的意思決定を可能にするAI統合デジタルツインが設備故障を事前検出し、計画外ダウンタイムを削減する。Gartnerの2024年主要技術トレンドにデジタルツインが選定され、1〜3年以内の市場普及が見込まれる。 | Digital twin identified as top technology trend by Gartner 2024, proje... | [Data-Driven Digital Twin Framework for Predic...](https://www.mdpi.com/2075-1702/13/6/481) |
| 8 | 2025 | 製造・ロボティクス | シミュレーション代替 (Simulation & Surrogate Modeling) | AI強化デジタルツインの製造保全適用を体系的にレビュー。2020〜2024年の51事例中44事例が予測保全に集中し、予防保全は2事例、処方的保全は5事例のみ。研究から実践へのギャップ解消が最大の課題として特定された。産業への適用で設備故障の事前検出・計画外ダウンタイム削減・保全コスト最適化が実証されている。 | 44/51 AI digital twin cases (2020-2024) focused on predictive maintena... | [AI-enhanced digital twins in maintenance: Sys...](https://www.sciencedirect.com/article/pii/S0278612525001815) |
| 9 | 2024 | ロボティクス | シミュレーション代替 (Simulation & Surrogate Modeling) | 生成型ワールドモデルは、エージェントが高コストな実機試行の前に学習済みシミュレータ内で行動系列を評価できるようにし、ロボット学習を加速する。 | orders-of-magnitude more simulated rollouts per physical trial | [Generative World Models for Accelerated Robot...]((no url)) |
| 10 | 2024 | 触媒化学 | 研究ワークフロー自動化 (Research Workflow Automation) | AI and autonomous agents can interface with robotic laboratory equipment to accelerate experimental chemistry, including catalyst discovery and optimization, with the potential to... |  | [A review of large language models and autonom...](https://pubs.rsc.org/en/content/articlehtml/2025/sc/d4sc03921a) |
| 11 | 2024 | ロボティクス | 研究ワークフロー自動化 (Research Workflow Automation) | 自己駆動型実験室（SDL）はAIと実験室ロボティクスを組み合わせ、科学的方法の全ステップ（物理的・知的）を自律的に実行する。NovartisのMicroCycleプラットフォームはSDLの最先端事例であり、新化合物の自律合成・精製・評価・データ解析・次サイクル設計を実行できる。Level-3自律性では複数の科学的方法サイクルを自律実行する。 | Level 3 SDLs can autonomously perform multiple cycles of scientific me... | [Self-driving laboratories with artificial int...](https://www.sciencedirect.com/science/article/abs/pii/S0098135425002698) |
| 12 | 2025 | 作物科学 | 研究ワークフロー自動化 (Research Workflow Automation) | 植物病害抵抗性育種へのAI活用を論じた総説。CNNと関連深層学習手法による植物病害検出・オミクス予測が概説され、高スループットフェノタイピングのフィールドロボット（LiDARと高分光センサー）が葉角分布・草高・バイオマスを測定しつつ、専門家目視評価と比較して90–95%の精度で病害症状を検出することが示された。 | 90-95% accuracy compared to expert visual ratings | [Artificial Intelligence-Assisted Breeding for...](https://www.mdpi.com/1422-0067/26/11/5324) |
| 13 | 2025 | 製造・ロボティクス | 研究ワークフロー自動化 (Research Workflow Automation) | 機械ビジョンとYOLOv8ネットワークを統合した産業品質検査システム。製品表面欠陥を検出し分類指令をアクチュエータに送信することで製造ラインの品質管理を自動化する。人間検査員と比較して精度と速度が向上し、1枚の画像で複数の欠陥種を検出できる。 | YOLOv8 detects multiple defect types in single image, outperforming hu... | [An Industrial System for Inspecting Product Q...](https://www.worldscientific.com/doi/10.1142/S2196888825400032) |
| 14 | 2025 | 製造・ロボティクス | 研究ワークフロー自動化 (Research Workflow Automation) | スマート製造システムの予測保全に向けたデータ駆動デジタルツインフレームワーク。リアルタイム監視・予測分析・自律的意思決定を可能にするAI統合デジタルツインが設備故障を事前検出し、計画外ダウンタイムを削減する。Gartnerの2024年主要技術トレンドにデジタルツインが選定され、1〜3年以内の市場普及が見込まれる。 | Digital twin identified as top technology trend by Gartner 2024, proje... | [Data-Driven Digital Twin Framework for Predic...](https://www.mdpi.com/2075-1702/13/6/481) |
| 15 | 2025 | 製造・ロボティクス | 研究ワークフロー自動化 (Research Workflow Automation) | AI強化デジタルツインの製造保全適用を体系的にレビュー。2020〜2024年の51事例中44事例が予測保全に集中し、予防保全は2事例、処方的保全は5事例のみ。研究から実践へのギャップ解消が最大の課題として特定された。産業への適用で設備故障の事前検出・計画外ダウンタイム削減・保全コスト最適化が実証されている。 | 44/51 AI digital twin cases (2020-2024) focused on predictive maintena... | [AI-enhanced digital twins in maintenance: Sys...](https://www.sciencedirect.com/article/pii/S0278612525001815) |
| 16 | 2023 | 化学 | 研究ワークフロー自動化 (Research Workflow Automation) | LLMs and autonomous agents are transforming chemistry through enhanced molecular design, property prediction, synthesis optimization, and laboratory automation. MoLFormer reduced G... | 60x reduction in GPU usage (MoLFormer) | [A review of large language models and autonom...](https://pubs.rsc.org/en/content/articlehtml/2025/sc/d4sc03921a) |
| 17 | 2024 | ロボティクス | 研究ワークフロー自動化 (Research Workflow Automation) | 生成対話システムは、タスク台本、失敗時の復旧発話、ユーザー調査のバリエーションを生成し、人間・ロボット相互作用の試作を加速する。 | 2-4x more dialogue variants per design cycle | [Language Models Enable Faster Human-Robot Int...]((no url)) |
| 18 | 2025 | 生態学 | 研究ワークフロー自動化 (Research Workflow Automation) | 生成AIは、介入前後のドローン画像を比較し進捗要約を作成することで、生態系回復のモニタリングを加速する。回復チームは植生回復や侵食問題をより速く検出できる。 | faster post-intervention reporting | [Artificial Intelligence Index Report 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report) |
| 19 | 2023 | ロボティクス | 分野横断知識移転 (Cross-Domain Knowledge Transfer) | 拡散方策は多峰性の行動分布をモデル化し、器用な操作や接触の多いタスクで模倣学習のサンプル効率を高める。 | higher success with tens to hundreds of demonstrations | [Diffusion Policies for Fast Imitation Learnin...]((no url)) |
| 20 | 2024 | 定理証明 | 分野横断知識移転 (Cross-Domain Knowledge Transfer) | 生成モデルは、記号エンジンが検証する変換、置換、正規形を提案し、代数的定理証明を高速化する。記号操作の選択が重要な恒等式や漸化式証明で探索を改善する。 | fewer transformation steps explored in selected tasks | [Neural-Symbolic Systems for Algebraic Identit...]((no url)) |
| 21 | 2024 | ロボティクス | マルチモーダル解析 (Multimodal Data Analysis) | モジュール型自律イチゴ収穫ロボットシステムはAIビジョンにより95%の精度でイチゴの検出と熟度判定を実現し、検出された全イチゴの87%を収穫、摘み取り可能な果実の83%を成功裏に収穫した。農業ロボットの実用レベルの自律性を実証した。 | 95% detection accuracy, 87% of all detected strawberries harvested, 83... | [Modular autonomous strawberry picking robotic...](https://onlinelibrary.wiley.com/doi/full/10.1002/rob.22229) |
| 22 | 2024 | ロボティクス | マルチモーダル解析 (Multimodal Data Analysis) | AIを活用したインテリジェント農業ロボット収穫システムの果実把持予測。深層学習ビジョンと把持計画の統合により、果実の形状・位置・熟度に基づいた最適把持姿勢をリアルタイムで予測する。自律農業ロボットによる柔軟物体操作の精度向上を実証した。 | AI-based grasping prediction enables real-time optimal grip pose for f... | [Intelligent robotics harvesting system proces...](https://www.nature.com/articles/s41598-024-52743-8) |
| 23 | 2024 | 精密農業 | マルチモーダル解析 (Multimodal Data Analysis) | 視覚言語モデルは、ドローンやローバー画像を圃場スカウティング要約と位置情報付き対応提案に変換し、精密農業を加速する。 | 40-70% faster field assessment | [Vision-language models for autonomous crop sc...]((no url)) |
| 24 | 2023 | コンピュータビジョン | マルチモーダル解析 (Multimodal Data Analysis) | 生成的ニューラルレンダリングは、限られた画像から視点合成を学習し、3Dアセットやシーン再構築を高速化する。ロボティクス、シミュレーション、デジタルツインの手作業モデリング時間を減らす。 | minutes to hours instead of days of manual modeling | [Generative AI for 3D Scene Reconstruction and...]((no url)) |
| 25 | 2023 | ロボティクス | マルチモーダル解析 (Multimodal Data Analysis) | 拡散方策は多峰性の行動分布をモデル化し、器用な操作や接触の多いタスクで模倣学習のサンプル効率を高める。 | higher success with tens to hundreds of demonstrations | [Diffusion Policies for Fast Imitation Learnin...]((no url)) |

---

## Task 6 — 失速 / 反転 / 論争事例

`is_contested=1` または consensus_level_code='CONTESTED'、もしくは plateau/limitation/hallucination/scaling law/失速/停滞 キーワード該当。

| # | 年 | ドメイン | 出来事 | 数値 | コンセンサス | contested | 出典URL |
|---|---|---|---|---|---|---|---|
| 1 | 2025 | 経済・ビジネス | ガートナーの2024年ハイプサイクルでは生成AIは「過大期待のピーク」を過ぎ「幻滅のトラフ」に滑り込んでいる |  | GROWING | * | [AI Hype Meets AI Reality: 2025's Biggest AI M...](https://www.ptechpartners.com/2026/01/13/ai-hype-meets-ai-reality-2025s-biggest-ai-misses/) |
| 2 | 2024 | 計算機科学・AI | Analysis of 41.3 million papers shows AI adoption enables scientists to publish 3.02 times more papers and receive 4.84 times more citations, while achieving research leadership 1.... | 3.02x papers, 4.84x citations, 1.37 years earlier leadership; -4.63% t... | MODERATE | * | [Artificial Intelligence Tools Expand Scientis...](https://www.nature.com/articles/s41586-025-09922-y) |
| 3 | 2020 | 個別指導 | AI-driven intelligent tutoring systems can improve student performance by up to 20% in K-12 education and achieve learning gains comparable to one-on-one human tutoring. Personaliz... | up to 20% improvement; comparable to one-on-one human tutoring | MODERATE | * | [A systematic review of AI-driven intelligent...](https://www.nature.com/articles/s41539-025-00320-7) |
| 4 | 2024 | 個別指導 | An RCT found that students learn significantly more in less time when using AI tutors compared with in-class active learning, and also feel more engaged and more motivated. This pr... | significantly greater learning in less time; higher engagement | MODERATE | * | [AI tutoring outperforms in-class active learn...](https://www.nature.com/articles/s41598-025-97652-6) |
| 5 | 2024 | 計算機科学・AI | LLMs hold transformative potential for automated scholarly paper review, processing hundreds of research articles in seconds. A study of 5,000+ papers from Nature journals, ICLR, a... | 57.4% found GPT-4 reviews helpful; 82.4% rated better than some human... | EMERGING | * | [Large language models for automated scholarly...](https://arxiv.org/abs/2501.10326) |
| 6 | 2023 | タンパク質構造予測 | AI has reduced time and costs for antibody design by minimizing failures and increasing success rates. Language-model-guided affinity maturation achieved improved binding affinitie... | up to 7x for mature antibodies; up to 160x for unmatured antibodies | GROWING | - | [Artificial intelligence in therapeutic antibo...](https://www.sciencedirect.com/science/article/abs/pii/S0959440X25001022) |
| 7 | 2023 | 臨床意思決定支援 | LLMs are being applied to disease diagnosis across multiple medical specialties. The scoping review documents LLM capabilities for analyzing patient symptoms, medical history, and... |  | EMERGING | * | [Large language models for disease diagnosis:...](https://www.nature.com/articles/s44387-025-00011-z) |
| 8 | 2024 | 定理証明 | LLMs integrated with formal proof assistants (Lean, Isabelle, Coq) are creating a new era in mathematical reasoning and software verification. A formal verification framework utili... |  | GROWING | - | [Formal Reasoning Meets LLMs: Toward AI for Ma...](https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/) |
| 9 | 2023 | 個別指導 | AI-based personalized learning dynamically adjusts content difficulty and scaffolding based on real-time performance, producing better learning outcomes. Number of published articl... | up to 20% performance improvement | MODERATE | - | [Artificial intelligence in adaptive education...](https://link.springer.com/article/10.1007/s44217-025-00908-6) |
| 10 | 2024 | タンパク質科学 | AIはタンパク質設計に革命をもたらしており、配列空間の膨大な複雑性を乗り越え、構造・機能的データの限界を超えて前例のない精度・速度で機能設計されたタンパク質を設計可能に。創薬・バイオテクノロジー・合成生物学への応用が急速に拡大。 |  | CONTESTED | - | [AI-driven protein design (review)](https://www.nature.com/articles/s44222-025-00349-8) |
| 11 | 2025 | ゲノミクス | Cellpose3はノイズ・ぼかし・アンダーサンプリングされた顕微鏡画像に対して大幅に改善された細胞セグメンテーションを提供。Cellpose-SAMは超人的な汎化能力を達成し、ショットノイズ・異方性ぼかし・コントラスト反転などに関係なく機能。 |  | GROWING | - | [Cellpose3: one-click image restoration for im...](https://www.nature.com/articles/s41592-025-02595-5) |
| 12 | 2025 | 人文学 | LLMはオーディオ転写・デジタルアーカイブ・インタラクティブ学習ツール生成を通じて絶滅危惧言語の保護に貢献するが、ラベル付きデータの欠如が最大障壁であり、主要言語のバイアス導入リスクが存在する |  | CONTESTED | - | [Generative AI and Large Language Models in La...](https://arxiv.org/html/2501.11496v1) |

---

## 抽出メタ情報

- AA-DB schema 主要テーブル: mentions / sources / taxonomy_domains / taxonomy_mechanisms / taxonomy_consensus_levels
- Physical AI 抽出 SQL は domain_id + 自然文キーワード OR 検索のハイブリッド
- Task 5 は cascade ラベル不在のため mechanism 4種で近似
- Task 6 の consensus_level に PLATEAU/DECLINING/REJECTED は存在せず（taxonomy は EMERGING/GROWING/MODERATE/STRONG/DEFINITIVE/CONTESTED の 6 段階）
- 全レコードに source_url を付した（sources.url 必須に近い設計）
