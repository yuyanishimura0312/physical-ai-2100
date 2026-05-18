# VLA / VLMモデル調査レポート 2025-2026  
Physical AI 2100 / NPO Miratuku / esse-sense

## 1. VLAパラダイム概観

Vision-Language-Action（VLA）は、視覚入力、自然言語指示、ロボット行動を単一または密結合したモデルに統合するロボット基盤モデルの設計思想である。従来のロボット学習では、認識、タスク計画、軌道生成、制御を別々のモジュールとして設計することが多かったが、VLAではカメラ画像と指示文を入力し、関節角、エンドエフェクタ変位、グリッパ開閉、行動チャンクなどを直接出力する。Google DeepMindのRT-2は、WebスケールのVision-Language Modelをロボット行動へ転移する実験としてVLAという語を前面化し、PaLM-Eは562Bパラメータ級のEmbodied Multimodal Language Modelとして、言語・画像・ロボット状態を同一系列で扱う方向を示した（https://arxiv.org/abs/2307.15818, https://arxiv.org/abs/2303.03378）。この流れはOpen X-Embodiment / RT-Xで、22種類のロボット、21機関、527スキル、160,266タスクというクロス・エンボディメント学習に拡張された（https://arxiv.org/abs/2310.08864）。

2024年から2025年にかけての転換点は、VLAが「巨大企業の閉じたデモ」から「研究コミュニティが再現・微調整・評価できる対象」へ移ったことである。OpenVLAは7Bパラメータ級のオープンVLAとして、Open X-Embodimentの970Kロボットエピソードで訓練され、RT-2-X 55Bより少ないパラメータで29タスク横断の成功率を上回ると報告した（https://arxiv.org/abs/2406.09246, https://huggingface.co/openvla/openvla-7b）。Octoは800K軌道を用いたオープンなgeneralist robot policyを提示し、UC Berkeley、Stanford、CMU、Google DeepMindが関与する共同研究として、言語指示とゴール画像の両方に対応した（https://arxiv.org/abs/2405.12213）。Physical Intelligenceのπ0は、PaliGemma系VLMにflow matchingのaction expertを重ね、連続制御をVLAの中心課題に戻した（https://arxiv.org/abs/2410.24164）。

2025年から2026年にかけては、単に「大きいVLA」を作るだけでなく、実時間性、ロバスト性、安全性、データ生成、世界モデルとの統合が主題になった。OpenVLA-OFTはLIBERO平均成功率を76.5%から97.1%へ上げ、action generation throughputを26倍にしたと報告した（https://openvla-oft.github.io, https://arxiv.org/abs/2502.19645）。Figure AIのHelixはヒューマノイド上半身の連続制御をVLAとして提示し、Google DeepMindのGemini RoboticsはGemini 2.0系のVLAを物理世界へ展開した（https://www.figure.ai/news/helix, https://arxiv.org/abs/2503.20020）。一方でLIBERO-Plusは、標準ベンチマークで95%級に見えるVLAが、視点や初期姿勢の小さな摂動で30%未満へ落ちることを示し、2026年以降の争点が「ベンチマーク成功率」から「外乱、分布外、説明可能性、現場安全」へ移ることを明確にした（https://arxiv.org/abs/2510.13626）。

## 2. モデルカタログ：主要論文・モデル 35件

1. **RT-1: Robotics Transformer for Real-World Control at Scale**。筆頭著者はAnthony Brohan、Google Robotics / Google Research、2022年、arXiv:2212.06817、モデルサイズは約35Mパラメータ、訓練データは実ロボット13万エピソード級、ベンチマークはGoogle社内実ロボット700タスク以上で評価された。source: https://arxiv.org/abs/2212.06817

2. **PaLM-E: An Embodied Multimodal Language Model**。Danny Driess、Google / TU Berlinほか、2023年、arXiv:2303.03378、最大モデルはPaLM-E-562B、ロボット・視覚・言語データを混合、OK-VQAなどVQAベンチマークとロボット計画で評価。source: https://arxiv.org/abs/2303.03378

3. **RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control**。Anthony Brohan、Google DeepMind、2023年、arXiv:2307.15818、PaLI-X / PaLM-Eベースで最大55B級、Web-scale VLMデータとロボットデータを混合、未見命令のセマンティック推論と実ロボット操作で評価。source: https://arxiv.org/abs/2307.15818

4. **Open X-Embodiment: Robotic Learning Datasets and RT-X Models**。Open X-Embodiment Collaboration / Abby O’Neillほか、Google DeepMindほか21機関、2023/2024年、arXiv:2310.08864、RT-1-X / RT-2-Xを含み、22ロボット・527スキル・160,266タスクを報告。source: https://arxiv.org/abs/2310.08864

5. **RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation**。Scott Reedほか、DeepMind、2023年、arXiv:2306.11706、モデルサイズは論文内で詳細限定、データは自己改善を含む多ロボットデータ、評価は多タスク操作。source: https://arxiv.org/abs/2306.11706

6. **Vision-Language Foundation Models as Effective Robot Imitators**。Moo Jin Kimほか、Stanford系、2023年、arXiv:2311.01378、既存VLMをロボット模倣へ転用、モデルサイズはバックボーン依存、評価はロボット模倣学習。source: https://arxiv.org/abs/2311.01378

7. **Octo: An Open-Source Generalist Robot Policy**。Dibya Ghoshほか、UC Berkeley / Stanford / CMU / Google DeepMind、2024年、arXiv:2405.12213、Transformer policy、800K軌道のOpen X-Embodiment訓練、9ロボットプラットフォームで評価。source: https://arxiv.org/abs/2405.12213

8. **OpenVLA: An Open-Source Vision-Language-Action Model**。Moo Jin Kim、Stanford / UC Berkeley / Google DeepMind / TRI、2024年、arXiv:2406.09246、7B級、970K実ロボットエピソード、RT-2-X 55Bを29タスクで16.5ポイント上回ると報告。source: https://arxiv.org/abs/2406.09246

9. **RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics**。Wentao Yuanほか、2024年、arXiv:2406.10721、VLMベース、データセットはRoboPoint / Where2Place系、空間アフォーダンス評価。source: https://huggingface.co/papers/2406.10721

10. **LLARVA: Vision-Action Instruction Tuning Enhances Robot Learning**。筆頭著者は論文ページ参照、2024年、arXiv:2406.11815、8.5M image-visual-trace pairsをOpen X-Embodimentから生成、RLBench 12タスクとFranka実機で評価。source: https://huggingface.co/papers/2406.11815

11. **π0: A Vision-Language-Action Flow Model for General Robot Control**。Kevin Black、Physical Intelligence、2024年、arXiv:2410.24164、PaliGemma系VLM + flow matching action head、複数ロボット実機タスクで評価、モデルサイズ詳細は一部未公開。source: https://arxiv.org/abs/2410.24164

12. **TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies**。筆頭著者はarXivページ参照、2024年、arXiv:2412.10345、OpenVLA微調整、150Kロボット操作軌道、4B Phi-3-Vision版も報告。source: https://arxiv.org/abs/2412.10345

13. **FAST: Efficient Action Tokenization for Vision-Language-Action Models**。Karl Pertsch、Physical Intelligence、2025年、arXiv:2501.09747、π0-FASTのaction tokenizer、1M real robot action sequencesで汎用トークナイザを訓練。source: https://arxiv.org/abs/2501.09747, https://www.physicalintelligence.company/research/fast

14. **OpenVLA-OFT: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success**。Moo Jin Kim、Stanford、2025年、arXiv:2502.19645、OpenVLA 7BのOFT、LIBERO平均97.1%、OpenVLA 76.5%、π0 94.2%、action generation 26倍高速化。source: https://arxiv.org/abs/2502.19645, https://openvla-oft.github.io

15. **Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models**。筆頭著者はHugging Faceページ参照、2025年、arXiv:2502.19417、階層VLA、データとサイズは論文参照、open-ended instruction followingで評価。source: https://huggingface.co/papers/2502.19417

16. **DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control**。筆頭著者はarXiv参照、2025年、arXiv:2502.05855、VLM + diffusion expert、データ・サイズは論文参照、実ロボット制御で評価。source: https://arxiv.org/abs/2502.05855

17. **Gemini Robotics: Bringing AI into the Physical World**。Google DeepMind、2025年、arXiv:2503.20020、Gemini 2.0系VLA、モデルサイズと訓練データ量は未公開、複数ロボット制御と物理推論で評価。source: https://arxiv.org/abs/2503.20020, https://deepmind.google/models/gemini-robotics/gemini-robotics/

18. **GR00T N1: An Open Foundation Model for Generalist Humanoid Robots**。NVIDIA、2025年、arXiv:2503.14734、Eagle VLMを用いるヒューマノイド基盤モデル、実・シミュレーション・合成データを混合、Fourier GR-1で言語条件付き双腕操作を評価。source: https://arxiv.org/abs/2503.14734

19. **π0.5: a Vision-Language-Action Model with Open-World Generalization**。Kevin Black / Physical Intelligence、2025年、arXiv:2504.16054、π0系列、Web・ロボット・実世界環境データを統合、未知家庭環境でのmobile manipulator操作を評価。source: https://arxiv.org/abs/2504.16054

20. **GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data**。筆頭著者はarXiv参照、2025年、arXiv:2505.03233、billion-scale synthetic action dataを用いる把持VLA、ベンチマークは把持タスク中心。source: https://arxiv.org/abs/2505.03233

21. **SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics**。Hugging Face LeRobotチーム、2025年、arXiv:2506.01844、約450M級として公開情報あり、LeRobot community dataを利用、LIBERO / LeRobot系評価。source: https://arxiv.org/abs/2506.01844, https://huggingface.co/papers/2506.01844

22. **BitVLA: 1-bit Vision-Language-Action Models for Robotics Manipulation**。Hongyu Wang、中国科学院計算技術研究所、2025年、arXiv:2506.07530、1-bit / ternary parameter VLA、OpenVLA-OFT相当のLIBERO性能と29.8%メモリ削減を報告。source: https://huggingface.co/papers/2506.07530

23. **CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models**。Zhaoほか、2025年、CVPR 2025、arXiv IDは論文参照、CoT-VLA-7B、45Kロボットデモ、LIBEROで評価。source: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf

24. **SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model**。筆頭著者はarXiv参照、2025年、arXiv:2501.15830、空間表現とAdaptive Action Grids、シミュレーション・実機で評価。source: https://arxiv.org/abs/2501.15830

25. **InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation**。筆頭著者はHFページ参照、2025年、arXiv:2507.17520、VLA-IT、650KサンプルのVLA-IT dataset、視覚言語理解と操作性能を同時評価。source: https://huggingface.co/papers/2507.17520

26. **EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos**。筆頭著者はHFページ参照、2025年、arXiv:2507.12440、人間一人称動画とロボットデモを利用、ロボット操作で評価。source: https://huggingface.co/papers/2507.12440

27. **CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification**。Wei Li、2025年、arXiv:2508.21046、モデルサイズは論文参照、LIBERO 97.4%、実ロボット70.0%、訓練コスト2.5倍削減、推論遅延2.8倍削減を報告。source: https://huggingface.co/papers/2508.21046

28. **VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model**。Yihao Wang、2025年、arXiv:2509.09372、1B級モデルが公開、LIBERO全スイートと22ベースライン比較、軽量Policy module + Bridge Attention。source: https://huggingface.co/papers/2509.09372

29. **dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought**。Junjie Wen、2025年、arXiv:2509.25681、diffusion VLA、LIBERO平均96.4%、Franka実機でbin-pickingを含む評価。source: https://huggingface.co/papers/2509.25681

30. **Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process**。Jiayi Chen、HKUST(GZ)、2025年、arXiv:2511.01718、8B級チェックポイントあり、CALVIN / LIBERO / SimplerEnvで評価、autoregressive方式より4倍高速と報告。source: https://huggingface.co/papers/2511.01718

31. **Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight**。Yi Yang、2025年、arXiv:2511.16175、6B級LIBEROチェックポイントあり、visual foresight + diffusion Transformer、LIBERO系で評価。source: https://huggingface.co/papers/2511.16175

32. **RynnVLA-002: A Unified Vision-Language-Action and World Model**。Jun Cen、DAMO Academy、2025年、arXiv:2511.17502、VLA + world model、LIBERO 97.4%、LeRobot実験でworld modelにより全体成功率50%向上と報告。source: https://huggingface.co/papers/2511.17502

33. **EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation**。Samarth Chopra、2025年、arXiv:2511.05397、低価格6-DOF manipulatorと統合、300ドル未満のハード構成、LIBEROでSOTA相当、実機でID 49%、OOD 34.9%改善。source: https://arxiv.org/abs/2511.05397

34. **LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models**。Senyu Fei、OpenMOSS、2025年、arXiv:2510.13626、評価ベンチマーク論文、7摂動軸、標準95%級性能が30%未満へ低下するケースを報告。source: https://arxiv.org/abs/2510.13626

35. **LeRobot: An Open-Source Library for End-to-End Robot Learning**。Hugging Face LeRobot team、2026年、arXiv:2602.22818、ライブラリ論文であり単一VLAではないが、データ収集・保存・ストリーミング・学習を統合、π0 / π0-FAST / SmolVLAなどの実装基盤として重要。source: https://huggingface.co/papers/2602.22818, https://huggingface.co/lerobot

## 3. 日本の研究機関・企業

日本勢のVLA関連活動は、米国のOpenVLA、Physical Intelligence、Google DeepMind、Figure AIのように「VLAモデル名を掲げた大規模公開モデル」が中心ではなく、視覚言語モデル、ロボットSI、産業応用、基盤モデル開発支援、実機ロボット研究が分散して存在する構図である。

PFN / Preferred Networksについては、ユーザー指定の「PFN PLaMo-Embedded」という名称そのものは、公開検索で一次情報を確認できなかった。一方で確認できる近接プロジェクトとして、PFNはGENIAC第3期で自律稼働デバイス向けの軽量VLM **PLaMo 2.1-8B-VL** を開発し、モニター企業募集を2025年12月16日に発表している（https://www.preferred.jp/news/pr20251216）。これはロボットVLAではなくVLMであるが、自律稼働デバイス向けという点で、将来のVLAバックボーンまたはオンデバイス認識・言語理解基盤になり得る。PFNグループのPreferred Roboticsも、掃除ロボット等の実機開発経験を持つが、2026年5月時点でOpenVLA型の公開VLAモデルは確認できない。

Sony AIの **Gran Turismo Sophy** は、VLAではなく強化学習ベースのレースAIである。ただし、2025年のSony AIはGran Turismo 7 Power Pack DLCで **Gran Turismo Sophy 3.0** に言及し、GT Sophyの学習基盤を拡張している（https://ai.sony/blog/sony-ai-2025-year-in-review）。また、2025年論文 **Automated Reward Design for Gran Turismo** では、LLMによる報酬関数生成、VLMによる選好評価、人間フィードバックを組み合わせ、GT Sophy級のエージェント生成を目指すと説明している（https://arxiv.org/abs/2511.02094）。これは物理ロボットではないが、シミュレーション内の視覚・言語・行動・報酬設計を接続する研究であり、Physical AI教材では「VLAそのもの」ではなく「VLA時代の報酬設計・評価自動化」と位置づけるのが正確である。

TRI / Toyota Research Instituteは、日本企業トヨタの米国研究拠点として、VLA周辺で最も直接的に世界水準の動きを示している。TRIは **Large Behavior Models（LBM）** を、ロボット動作を直接指令するAI foundation modelとして説明している（https://www.tri.global/our-work/large-behavior-models）。2025年8月20日にはBoston DynamicsとTRIが、AtlasヒューマノイドにLBMを載せ、移動と物体操作を含む長い連続タスクを実行したと発表した（https://pressroom.toyota.com/ai-powered-robot-by-boston-dynamics-and-toyota-research-institute-takes-a-key-step-towards-general-purpose-humanoids/）。OpenVLAの著者にもToyota Research Institute関係者が含まれており、TRIはVLA / diffusion policy / behavior cloningを統合する実機ロボット基盤モデルの重要プレイヤーである。

産総研 / AISTとNEDOについては、2025年度以降、日本国内でロボティクス分野の生成AI基盤モデルに向けた制度整備が進んでいる。NEDOは「ポスト5G情報通信システム基盤強化研究開発事業／ロボティクス分野の生成AI基盤モデルの開発に向けたデータプラットフォームに係る開発」の実施体制決定を公表し、AIロボット協会が関与する（https://www.nedo.go.jp/koubo/CD3_100398.html）。産総研は第94回人工知能セミナー「フィジカル領域の生成AI基盤モデル」で、言語・視覚・音声音響等の多様なモダリティを対象とする基盤モデルと、ロボット・ライフサイエンス等のフィジカル領域応用を説明している（https://www.ai-japan.go.jp/menu/events/94ai/）。また、産総研の調達情報には「生成AI基盤モデル実験用双腕移動ロボット」や「汎用ヒューマノイドロボット」が確認でき、VLA研究基盤の実機整備が進んでいる（https://www.aist.go.jp/aist_j/procure/supplyinfo/pub/detail/Z4Z4K8OR, https://www.aist.go.jp/aist_j/procure/supplyinfo/pub/detail/SEE35HA7/TZWRUK0RB2JPKIO2EGL8.pdf）。

東京大学JSK系については、2025年時点で「JSK発の大規模公開VLAモデル」は確認できない。一方で、JSK関係者の河原塚健人氏らによるVLAサーベイ **Vision-Language-Action Models for Robotics** が公開されており、VLA研究の体系化に貢献している（https://vla-survey.github.io/data/paper.pdf）。東京大学全体では、RCASTの日本語特化マルチモーダルモデル14.2Bパラメータの公開、JST/J-GLOBALに見られる「遠隔操作および基盤モデルによる人型研究支援ロボットシステム」など、VLM・遠隔操作・基盤モデルとロボットを接続する研究がある（https://www.rcast.u-tokyo.ac.jp/ja/news/release/20250225.html, https://jglobal.jst.go.jp/en/public/202604018793315551）。教材上は、東大JSKを「VLA実装モデルの提供者」ではなく、「ロボット身体・遠隔操作・実世界タスク・VLAサーベイの橋渡し拠点」と記述するのが安全である。

## 4. 2024→2025→2026の変化

2024年の中心語は「オープン化」だった。OpenVLAは7B級モデル、970Kエピソード、MITライセンスのチェックポイントとコードを公開し、VLA研究を閉じた企業デモから実験可能な研究対象に変えた（https://huggingface.co/openvla/openvla-7b）。Octoは800K軌道のgeneralist policyを公開し、ロボットプラットフォーム差、観測差、行動空間差に対応する設計を示した（https://arxiv.org/abs/2405.12213）。この段階の争点は「VLMをロボットデータで微調整すれば、本当に汎化するのか」だった。

2025年の中心語は「効率化、連続制御、ヒューマノイド、ロバスト性」である。π0はflow matchingにより連続アクションを扱い、FASTはaction chunkを周波数空間トークン化することでautoregressive VLAの実行効率を改善した（https://arxiv.org/abs/2410.24164, https://arxiv.org/abs/2501.09747）。OpenVLA-OFT、CogVLA、VLA-Adapter、BitVLA、SmolVLAは、VLAを巨大GPUクラスタ専用から、より軽量・高速・微調整可能な方向へ動かした（https://arxiv.org/abs/2502.19645, https://huggingface.co/papers/2508.21046, https://huggingface.co/papers/2509.09372, https://huggingface.co/papers/2506.07530, https://arxiv.org/abs/2506.01844）。一方でHelix、GR00T N1、Gemini Roboticsはヒューマノイドや汎用ロボットへスケールし、VLAが研究室の卓上操作を超えて、倉庫、家庭、移動操作、全身制御へ入ったことを示した（https://www.figure.ai/news/helix, https://arxiv.org/abs/2503.14734, https://arxiv.org/abs/2503.20020）。

2026年の入口では、VLAは「単体ポリシー」から「エージェント・世界モデル・データエンジン」へ広がっている。LeRobot論文は、モデルそのものより、収集、保存、ストリーミング、学習、評価のスタックを整える方向を示す（https://huggingface.co/papers/2602.22818）。RynnVLA-002やUnified Diffusion VLAは、行動生成と未来予測・世界モデルを統合する（https://huggingface.co/papers/2511.17502, https://huggingface.co/papers/2511.01718）。LIBERO-Plusやadversarial / backdoor研究は、VLAが現場投入されるほど、攻撃、摂動、言語無視、位置バイアスが深刻な評価課題になることを示している（https://arxiv.org/abs/2510.13626, https://huggingface.co/papers/2510.13237, https://huggingface.co/papers/2510.10932）。

## 5. 未解決問題と2026-2030展望

最大の未解決問題は、ベンチマーク成功率と現実性能の乖離である。LIBEROで97%級の数字が出ても、視点、照明、背景、初期姿勢、物体配置、言語言い換えで性能が崩れるなら、家庭・工場・介護現場では使えない。LIBERO-Plusが示した「95%から30%未満への低下」は、VLAがまだ意味理解より視覚的ショートカットや位置バイアスに依存している可能性を示す（https://arxiv.org/abs/2510.13626）。2026-2030年の評価は、平均成功率より、摂動耐性、失敗検知、自己修正、動作停止、安全余裕、説明可能性を含む方向へ移る。

第二の問題は、データである。Open X-Embodimentは22ロボット、527スキル、160,266タスクを集めたが、実世界の物理タスク空間から見ればまだ薄い（https://arxiv.org/abs/2310.08864）。π0.5やHelixが家庭・物流へ向かい、GR00Tがヒューマノイドへ向かうほど、データは「軌道数」だけでなく、接触、失敗、回復、力覚、長期タスク、人間との共同作業を含む必要がある。NVIDIAのGR00T N1.5やGR00T-Dreamsのように、合成軌道とworld foundation modelでデータ生成を短縮する方向は重要だが、合成データが現実の摩擦、柔軟物、破損、安全制約をどこまで再現できるかは未解決である（https://developer.nvidia.com/blog/enhance-robot-learning-with-synthetic-trajectory-data-generated-by-world-foundation-models/）。

第三の問題は、アーキテクチャである。RT-2型のautoregressive action token、π0型のflow matching、OpenVLA-OFT型の連続action regression、dVLA / UD-VLA型のdiffusion、RynnVLA型のworld model統合は、それぞれ遅延、滑らかさ、長期計画、説明可能性、安全停止で長短が異なる（https://arxiv.org/abs/2307.15818, https://arxiv.org/abs/2410.24164, https://arxiv.org/abs/2502.19645, https://huggingface.co/papers/2509.25681, https://huggingface.co/papers/2511.17502）。2030年までには、単一巨大VLAよりも、VLM/ERモデルが計画し、VLAが短期制御し、world modelが予測し、critic/reward modelが安全性を監視する複合システムが主流になる可能性が高い。

第四の問題は、日本のポジションである。日本にはロボットハード、産業現場、SI、精密制御、製造業データがあるが、2026年5月時点でOpenVLAやπ0に相当する公開VLAモデルは限定的である。PFNのPLaMo 2.1-8B-VL、TRIのLBM、産総研/NEDOのロボティクス生成AI基盤モデル事業、東大JSK系のVLAサーベイと実機研究は、それぞれ部品としては重要である（https://www.preferred.jp/news/pr20251216, https://www.tri.global/our-work/large-behavior-models, https://www.nedo.go.jp/koubo/CD3_100398.html, https://vla-survey.github.io/data/paper.pdf）。2030年に向けて日本が勝てる領域は、基盤モデル単体のパラメータ競争ではなく、現場データ、失敗データ、安全規格、ロボットSI、ヒューマノイド量産、ドメイン特化VLA評価基盤を結びつけることだろう。
