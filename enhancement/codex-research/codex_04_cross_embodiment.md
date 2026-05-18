# Cross-Embodiment Transfer Learning in Robotics, 2023-2026

## 1. なぜ cross-embodiment が重要か

ロボット学習でいう cross-embodiment transfer learning は、ある身体で集めた経験を、別の身体をもつロボットに移すための技術群である。ここでの「身体」は、腕の本数、リンク長、関節数、エンドエフェクタ、移動ベース、カメラ配置、力覚・触覚センサ、制御周期まで含む。2023年以降この問題が急に中心課題になったのは、単一のロボットを大量に動かすだけでは、世界の多様な作業環境に対応できないことが明確になったからである。Franka、WidowX、ALOHA、UR、Google Robot、移動双腕、ヒューマノイド、筋骨格ロボットは、同じ「コップを取る」というタスクでも、可達域、把持姿勢、失敗モードが異なる。したがって、単一ハードウェア上の成功率だけでは、Physical AI 2100 が扱うべき「身体をまたぐ知能」の評価にならない。

データ scalability の観点では、cross-embodiment はロボット版の「Web-scale pretraining」に相当する。言語モデルはインターネット上のテキストを横断的に使えたが、ロボットでは行動ラベル付きデータが高価で、ハードウェアごとにフォーマットが異なる。Open X-Embodiment はこの制約に対する最初の大規模な回答であり、Google DeepMind と多数の研究機関が 22 種類のロボット身体、60 個の個別データセット、100万超の軌道を共通形式で集約した。論文は 21 機関、527 skills、160,266 tasks を報告している（https://arxiv.org/abs/2310.08864）。ここで重要なのは、データが「多い」ことだけではない。別のロボットで起きた接触、失敗、物体操作、言語指示を、ターゲットロボットの方策に役立つ形で使えるかが焦点である。

現状のボトルネックは、データ統合ではなく「身体差をどう表現するか」に移っている。画像と言語は比較的共通化しやすいが、行動空間はロボットごとに違う。あるデータセットは 7-DoF end-effector delta、別のデータセットは joint position、別のデータセットは dual-arm action chunk、さらに別のものは mobile base velocity を含む。センサも、外部RGB、手首カメラ、深度、触覚、力覚、proprioception が混在する。RT-X、Octo、OpenVLA、RDT-1B、π0 以降の研究は、まさにこの異質性を、shared tokenizer、latent action、unified action space、hardware abstraction、fine-tuning recipe によって吸収しようとしている。

## 2. Dataset catalog

| Dataset / system | 主な貢献者 | 身体数 | 規模 | Source URL |
|---|---:|---:|---:|---|
| Open X-Embodiment / OXE | Google DeepMind + Open X-Embodiment Collaboration、21機関 | 22 embodiments | 60 datasets、100万超 trajectories、527 skills、160,266 tasks | https://arxiv.org/abs/2310.08864 / https://robotics-transformer-x.github.io |
| DROID | Stanford, UC Berkeley ほか | 主に標準化された Franka 系マニピュレータ | 76k demonstration trajectories、350 hours、564 scenes、84 tasks、50 collectors | https://arxiv.org/abs/2403.12945 |
| BridgeData V2 | UC Berkeley RAIL、Stanford、Google DeepMind、CMU 系著者 | 低コスト WidowX 系公開ロボット | 60,096 trajectories、24 environments | https://arxiv.org/abs/2308.12952 / https://rail-berkeley.github.io/bridgedata |
| RoboMimic | ARISE Initiative / Mandlekar et al. | robosuite sim + real robot datasets | 複数タスク。v0.1 docs では Lift 1,500 trajectories、Can 3,900 trajectories などを含む | https://arxiv.org/abs/2108.03298 / https://robomimic.github.io |
| RoboCasa | UT Austin / NVIDIA / RoboCasa team | 主にキッチン内操作用ロボット設定、シミュレーション | 100 tasks、150+ object categories、数千3D assets。docs は pretraining demonstrations 約2,000 hours を報告 | https://arxiv.org/abs/2406.02523 / https://robocasa.ai |
| Mobile ALOHA | Stanford / Google DeepMind 系 | mobile bimanual ALOHA | 低コスト全身遠隔操作。既存 static ALOHA data との co-training で性能向上を報告 | https://arxiv.org/abs/2401.02117 / https://mobile-aloha.github.io |
| UMI / FastUMI | Columbia, Toyota Research Institute, MIT 系 / FastUMI team | 人間の handheld gripper から複数ロボットへ | UMI は robot-free human demos、FastUMI は 10,000+ trajectories、22 everyday tasks | https://arxiv.org/abs/2402.10329 / https://umi-gripper.github.io / https://arxiv.org/abs/2409.19499 |
| Galaxea Open-World Dataset | Galaxea Dynamics / Tsinghua 周辺著者 | 一貫した Galaxea embodiment + cross-embodiment pretraining stage | open-world household / workplace behaviors、G0 VLA の三段階 curriculum | https://arxiv.org/abs/2509.00576 / https://galaxea-dynamics.com |
| ManiSkill3 | UCSD / Meta / Stanford など | 12 domains、arms, humanoids, dexterous hands, mobile manipulation | millions of demonstration frames、GPU parallel simulation、最大 30,000+ FPS | https://arxiv.org/abs/2410.00425 |
| Isaac Lab | NVIDIA | 多様なロボット、GR00T 基盤にも接続 | GPU-accelerated multimodal robot learning framework | https://arxiv.org/abs/2511.04831 / https://developer.nvidia.com/isaac/lab |
| MuJoCo Playground | Google DeepMind / Berkeley ほか | quadrupeds, humanoids, dexterous hands, arms | MJX ベース、zero-shot sim-to-real を重視 | https://arxiv.org/abs/2502.08844 / https://playground.mujoco.org |

この表から見える傾向は、2023年は「実ロボットデータを統合する」年、2024年は「in-the-wild 収集と open VLA が出る」年、2025年は「foundation model と sim-to-real をつなぐ」年だったということである。Open X-Embodiment は横断データのハブであり、DROID は標準ハードウェアで実環境の多様性を押し上げ、RoboCasa・ManiSkill3・Isaac Lab・MuJoCo Playground は現実データ不足をシミュレーション側から補う。

## 3. Methods deep dive

RT-X 系列は、Open X-Embodiment の中心的な実証である。RT-1-X は RT-1 architecture を OXE 上で訓練したモデルで、RT-2-X は RT-2 の vision-language-action backbone を cross-embodiment data で訓練したものだ。Google DeepMind は、RT-1-X を 5 つの研究室・5 種類の一般的ロボットで評価し、各ロボット専用に作られた元手法より平均 50% 高い success rate を得たと報告している（https://deepmind.google/discover/blog/scaling-up-learning-across-many-different-robot-types/）。強みは、多機関データを同じ model family に流し込む単純さと、実ロボット評価で positive transfer を示した点である。弱みは、行動表現が end-effector action に寄りやすく、全身制御、触覚依存作業、ロボット固有の力制御にはまだ粗いことである。

Octo は、Open X-Embodiment の約 800k trajectories で訓練された open-source generalist robot policy である（https://arxiv.org/abs/2405.12213）。Octo の意義は、RT-X よりも研究コミュニティが触りやすい形で、画像・言語・行動の統合アーキテクチャを公開した点にある。多様な observation / action space を扱う設計になっており、下流ロボットへの fine-tuning を前提にしている。長所は、オープンな ablation と再利用性である。短所は、完全な zero-shot cross-embodiment というより、pretraining + adaptation の土台であり、未知の身体にそのまま入れて安定に動くわけではない。

RDT-1B は中国・清華大学系の Robotics Diffusion Transformer で、1.2B parameter diffusion foundation model として、1M+ multi-robot episodes による pretraining を行う（https://arxiv.org/abs/2410.07864 / https://rdt-robotics.github.io/rdt-robotics/）。Hugging Face の model card は、RGB 最大3視点、言語指示、proprioception、control frequency を入力し、次の 64 actions を予測すると説明する（https://huggingface.co/robotics-diffusion-transformer/rdt-1b）。重要なのは physically interpretable unified action space である。joint、EEF、position、velocity、mobile base locomotion などを統一ベクトルに埋め、各ロボットが対応する成分だけを使う。長所は、dual-arm / bimanual 操作や高周波 action chunk に強いこと。短所は、model card 自身が述べる通り、pretraining dataset に含まれない新規 robot platform へは fine-tuning が推奨される点である。

latent action representation は、2025年以降の最重要路線の一つである。Latent Action Diffusion for Cross-Embodiment Manipulation は、anthropomorphic hand、人間の手、parallel jaw gripper の end-effector action を contrastive learning で意味的に対応する latent action space に写し、co-training によって最大 13% の manipulation success rate 改善を報告している（https://arxiv.org/abs/2506.14608）。この方法の長所は、行動空間を直接そろえず、物体に対する「操作の意味」を潜在空間で共有できることである。短所は、latent space の品質がデータ対応・タスク分布に依存し、力制御や接触遷移のような微細な身体差を潰してしまう危険があることだ。

OpenVLA と OpenVLA-OFT は、VLA fine-tuning の実用面を前進させた。OpenVLA は 7B parameter open-source VLA で、970k real-world robot demonstrations に訓練された（https://arxiv.org/abs/2406.09246 / https://github.com/openvla/openvla）。OpenVLA-OFT は 2025年に、parallel decoding、action chunking、continuous action representation、L1 regression objective を組み合わせ、LIBERO の平均 success rate を 76.5% から 97.1% に上げ、action generation throughput を 26倍にしたと報告する（https://arxiv.org/abs/2502.19645 / https://openvla-oft.github.io/）。さらに実ロボットでは bimanual ALOHA 上で π0、RDT-1B、Diffusion Policy、ACT を最大 15 percentage points 上回るとされる。長所は、既存 VLA をターゲットロボットに高速・高成功率で合わせる recipe を示したこと。短所は、fine-tuning 前提であり、未知身体への完全な zero-shot generalization ではないことだ。

π0 と π0.5 は、Physical Intelligence が提示した cross-embodiment foundation model の代表例である。π0 は vision-language-action flow model で、flow matching action head により高周波連続 action を生成する（https://arxiv.org/abs/2410.24164）。π0.5 は 2025年に、複数ロボット、semantic prediction、web data、language instruction、low-level actions を co-training し、未知の家庭で掃除や片付けのような長時間タスクを実演した（https://arxiv.org/abs/2504.16054）。長所は、単なる tabletop manipulation から household long-horizon manipulation へ射程を広げた点である。短所は、公開評価の多くが Physical Intelligence 側の環境・データ・ロボットに依存し、研究者が同条件で再現しにくいことだ。

AnyBody / AnyTask / AnySkill 系の「any body, any task, any skill」という発想は、2025年時点では完全な単一手法というより、複数研究に分散している。AnyBody は Princeton の cross-embodiment manipulation benchmark で、reach / push を 18 robot variations、interpolation / extrapolation / composition splits で評価する（https://arxiv.org/abs/2505.14986）。AnySkill は open-vocabulary physical skill を扱う interactive agents の研究で、ロボット操作というより身体化エージェントの skill abstraction に近い（https://arxiv.org/abs/2403.12835）。task-agnostic / skill-agnostic の実装例としては、XSkill が human and robot manipulation videos から skill prototypes を発見する（https://xskill.cs.columbia.edu/）、UniSkill が cross-embodiment video data から embodiment-agnostic skill representations を学ぶ（https://arxiv.org/abs/2505.08787）。厳密な “AnyTask” という名の主要ロボット論文は確認できなかったため、ここでは「任意タスク化」を task-agnostic skill representation の流れとして扱うのが安全である。

hardware abstraction の代表は UMI である。UMI はロボットそのものではなく handheld gripper で人間の実演を集め、relative-trajectory action representation と latency matching により、ハードウェア非依存の方策へ変換する（https://arxiv.org/abs/2402.10329）。FastUMI はこれを簡素化し、10,000+ trajectories、22 tasks のデータセットを公開した（https://arxiv.org/abs/2409.19499）。この方向の長所は、ロボットを現場に持ち込まずに現場データを集められること。短所は、人間の gripper interface が robot gripper と一致する範囲では強いが、柔軟手、触覚、全身バランス、脚移動を伴う作業には追加変換が必要なことだ。

## 4. Benchmarks: 異身体間 transfer success rate の実測値

最も引用しやすい実測値は RT-X である。RT-1-X は、5 研究室の実ロボット評価で、各ロボット専用の元手法に対して平均 50% success rate improvement を示した（https://deepmind.google/discover/blog/scaling-up-learning-across-many-different-robot-types/）。第三者整理では、平均成功率が約 63% 対 41% とされるが、一次的には DeepMind blog と OXE paper の “50% higher mean success rate” を使うのが確実である。RT-2-X では、評価ロボット自身の訓練データにはないが、他ロボットの OXE data には存在する emergent skills で、RT-2-X が 75.8%、standard RT-2 が 27.3% と報告されている整理がある。これは「別身体から見た skill が、同一ロボット上の新能力として出る」ことを示す重要な数字である。

OpenVLA-OFT は、cross-embodiment そのものの zero-shot 評価というより、VLA adaptation benchmark として重要である。LIBERO simulation で 76.5% から 97.1% に改善し、real bimanual ALOHA で π0、RDT-1B、Diffusion Policy、ACT を最大 15% absolute 上回る（https://arxiv.org/abs/2502.19645）。これは「多様データで事前学習された VLA を、別のロボットセットアップへどう適応するか」という現実的な cross-embodiment 問題に対する評価である。

Latent Action Diffusion は、end-effector の違うロボット・人間手・gripper 間で、共通 latent action を使うことで最大 13% success rate improvement を報告する（https://arxiv.org/abs/2506.14608）。AnyBody は、benchmark として単一成功率を売るというより、multi-embodiment RL が簡単な interpolation では改善しても、extrapolation / composition ではまだ single-embodiment baseline に届かないことを示す。つまり 2025年時点で、cross-embodiment は「平均では効く」が、「未知形態へのゼロショット」はまだ難しい。

sim-to-real では、X-Sim が human video から object-centric reward を構成し、real-to-sim-to-real で 5 manipulation tasks / 2 environments において、hand-tracking や sim-to-real baseline より平均 30% task progress を改善し、10倍少ない data collection time で behavior cloning に匹敵すると報告する（https://arxiv.org/abs/2505.07096）。MuJoCo Playground は zero-shot sim-to-real を掲げ、quadrupeds、humanoids、dexterous hands、robot arms を同一フレームワークで扱う（https://arxiv.org/abs/2502.08844）。ManiSkill3 は 10-1000x faster rendering/simulation、最大 30,000+ FPS を報告し、学習環境のスループットそのものを benchmark にしている（https://arxiv.org/abs/2410.00425）。

## 5. 制約

第一の制約は physical morphology gap である。parallel gripper と five-finger hand、single arm と bimanual、固定台と mobile manipulator、剛体関節と筋骨格駆動は、同じ言語指示に対して必要な制御戦略が異なる。リンク長が違えば可達姿勢が変わり、手先形状が違えば把持可能性が変わる。AnyBody の結果が示すように、同一カテゴリ内の interpolation より、異なるリンク構造への extrapolation が難しい。latent action はこの gap を緩和するが、身体固有の affordance を完全に消すことはできない。

第二の制約は sensor diversity である。Open X-Embodiment は多様なセンサ設定を統合したが、それは同時に問題でもある。外部カメラ、wrist camera、depth、force/torque、tactile、joint proprioception の有無がばらつく。VLA はRGBと言語には強いが、接触豊富な作業では力覚・触覚が欠けると限界が出る。UMI のような相対軌道表現は視覚主導の transfer には有効だが、嵌合、布操作、ケーブル、食品、工具使用では、非視覚センサの統一が次の課題になる。

第三の制約は control frequency mismatch である。データセットごとに 5Hz、10Hz、20Hz、50Hz、あるいは action chunking の長さが異なる。RDT-1B は control frequency を入力に含め、64 action chunk を出力する。π0 は flow matching により高周波連続 action を扱う。OpenVLA-OFT は parallel decoding と action chunking で速度を改善する。だが、データの timestamp jitter、camera-action synchronization、latency は、単に token を共通化するだけでは解けない。UMI が latency matching を明示したのは、この問題が実機性能に直結するからである。

## 6. 日本機関の cross-embodiment 研究

日本では、明示的に “cross-embodiment VLA” を前面に出す研究は米中ほど多くないが、身体差・技能転写・ロボット基盤モデルに関わる蓄積は厚い。産総研 AIST は 2025年1月、実世界の困難作業自動化を目指したロボット基盤モデル研究を本格始動したと発表している（https://www.aist.go.jp/aist_j/news/announce/pr20250123_2.html）。Nature Index の紹介でも、AIST の室岡雅樹氏らが製造現場向けの robotic foundation model を三年計画で構築する狙いが述べられている（https://www.nature.com/articles/d42473-024-00203-2）。また CNRS-AIST JRL は、模倣学習による難作業実現と robotics foundation models の開発を掲げている（https://unit.aist.go.jp/isri/isri-jrl/en/projects/project-foundation.html）。2026年5月の AIST 記事では、双腕ロボットAI研究開発を支援する 1万エピソードの AIST Bimanual Manipulation Dataset の無償公開にも触れている（https://www.aist.go.jp/aist_j/magazine/20260513.html）。

東京大学 JSK 系では、Kento Kawaharazuka 氏の EVARL が、筋骨格ヒューマノイド、ワイヤ駆動ロボット、open-source robotic platforms を通じて、embodiment、biomechanics、sensorimotor learning を研究対象にしている（https://www.eva.ai.u-tokyo.ac.jp/）。JST AIP の資料では、Kawaharazuka 氏の「情報化身体モデル」が、センサとアクチュエータの因果・空間関係を大量データから自己組織化し、軸駆動、車輪型、筋骨格型を含む多様なロボットが内部システムを形成・成長させる構想として説明されている（https://www.jst.go.jp/kisoken/aip/colab/image/researchers/pdf/111F003_db7930_en.pdf）。これは OXE 型の VLA とは違うが、身体構造の差を内部モデルとして学習するという意味で、cross-embodiment の基礎研究に近い。

東大松尾研系の TRAIL も robot learning from offline data を研究テーマに掲げ、Open X-Embodiment 論文を研究リストに含めている（https://trail.t.u-tokyo.ac.jp/）。日本の強みは、長年のヒューマノイド、筋骨格、産業ロボット、RT middleware、実生産現場との接続にある。一方で、2023-2026 の世界的潮流である「大規模公開ロボットデータ + open VLA + cross-embodiment benchmark」という形では、米中の大規模公開データに比べて存在感はまだ限定的である。AIST の 1万エピソード級データ公開と基盤モデル計画は、このギャップを埋める重要な動きである。

## 7. 2026-2030 outlook

2026-2030年の第一の焦点は、共通行動表現の勝ち筋である。RT-X は 7-DoF action に寄せ、Octo は open generalist policy として多様 I/O を扱い、RDT-1B は physically interpretable unified action space、π0 は flow matching action head、OpenVLA-OFT は continuous action chunking、latent action 系は意味的潜在空間を使う。おそらく単一方式には収束しない。実用上は、低レベル制御は robot-specific adapter、高レベル操作意図は embodiment-agnostic latent、データ形式は RLDS / LeRobot / OpenVLA 系で相互変換、という三層構造になる可能性が高い。

第二の焦点は、sim-to-real と real-to-sim-to-real の統合である。Isaac Lab、MuJoCo Playground、ManiSkill3、RoboCasa365 のような高速・大規模シミュレーションは、データ不足を補うだけでなく、未知身体を安全に試す場所になる。X-Sim のように human video から object-centric reward を作る方法は、cross-embodiment の「身体ではなく物体変化を共有する」方向を示す。2030年までには、実ロボット軌道、human video、simulation rollout、synthetic demonstration が同じ training mixture に入り、robot-specific calibration だけを実機で行う流れが標準化すると考えられる。

第三の焦点は、評価である。2025年時点の success rate は、個別タスク・個別ロボットで比較されることが多く、家庭・工場・物流・介護の現実タスクに対する横断指標は未成熟である。AnyBody のように interpolation / extrapolation / composition を分ける benchmark は重要だが、reach / push だけでは足りない。今後は、未知ロボット、未知物体、未知部屋、未知センサ、未知制御周期を分離して評価する必要がある。OpenVLA-OFT のような fine-tuning benchmark、π0.5 のような household long-horizon benchmark、Galaxea G0 のような dual-system benchmark が統合されていくはずである。

第四の焦点は、日本の役割である。日本は高品質な産業ロボット、ヒューマノイド、双腕、筋骨格ロボットの実体を持っている。AIST、東大 JSK / EVARL、松尾研 TRAIL、早稲田、東北大、奈良先端大、産業界のロボットメーカーが、公開可能な実データ、標準化されたタスク、基盤モデル評価環境を出せるかが鍵になる。Physical AI 2100 の観点では、cross-embodiment は単なる AI benchmark ではなく、「身体の違いを前提にした社会実装」の基礎である。2030年までに本当に必要なのは、万能な単一ロボットではなく、異なる身体をもつロボット群が、経験・技能・失敗知を共有できる学習基盤である。
