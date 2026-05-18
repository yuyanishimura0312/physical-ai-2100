# World Model AI / Physical World Foundation Models調査報告（2024-2026）

調査日: 2026-05-18。以下では、公開論文、企業ブログ、モデルカード、ベンチマークリーダーボードで確認できる情報のみを用いる。パラメータ数、学習データ、物理一貫性スコアが公開されていない場合は「未公表」と明記する。なお、ユーザー指定の「Genie 3 rumored 2025」は、2026年5月時点では噂ではなく、Google DeepMindが2025年8月に公式発表済みである。

## 1. World Modelパラダイム概観

World Modelとは、観測された世界の状態、行為、時間発展を内部表現として持ち、未来の状態を予測・生成・評価するAIである。従来の画像生成や動画生成が「見た目のもっともらしさ」を主目的にしていたのに対し、World Modelは「次に何が起こるか」「この行為をしたら状態がどう変わるか」「複数の未来のうちどれが目的達成に近いか」を扱う。MetaはV-JEPA 2の説明で、World Modelに必要な能力を理解、予測、計画の3つに整理している。Google DeepMindはGenie 2/3を、行為入力に応答して仮想環境を展開する「foundation world model」と位置づける。NVIDIAはCosmosをPhysical AI向けのWorld Foundation Model群と呼び、ロボットや自動運転のための合成データ生成、未来状態予測、シミュレーションに使う基盤として設計している。

アーキテクチャ上は、JEPA系、自己回帰系、拡散系の三つが重要である。JEPAはYann LeCunが推すJoint Embedding Predictive Architectureで、ピクセルをそのまま再構成するのではなく、潜在表現の中で未来や欠損部分を予測する。V-JEPA/V-JEPA 2はこの系譜にあり、生成動画の美しさよりも、行為理解、将来予測、ロボット計画のための表現学習を重視する。自己回帰系は、動画や潜在トークンを時系列として扱い、過去フレームと行為から次状態を逐次予測する。Genie 2、GAIA-1、Cosmos Predictの一部はこの方向である。拡散系は、Sora、Veo、Runway、HunyuanVideo、Lumiere、DIAMOND、GameNGenなどで中心的に使われ、視覚品質と運動の滑らかさに強いが、長期の状態保存や因果整合性はまだ弱い。NVIDIA Cosmosのように、拡散と自己回帰を用途別に併用する構成が2025年以降のPhysical AI基盤では増えている。

評価ベンチマークも、従来のFID/FVDや人間選好から、物理・因果・行為条件付き予測へ移っている。VBenchは動画生成を16次元で評価し、subject consistency、background consistency、motion smoothness、overall consistencyなどを測る。Physics-IQは、流体、固体力学、光学、熱、磁性などの物理原理を問う。WorldModelBenchは、動画生成モデルをWorld Modelとして評価するため、instruction following、common sense、physics adherenceを分け、Newton法則、質量保存、流体、貫通、重力などを採点する。これらは「動画が綺麗か」ではなく、「生成された世界が行為と物理法則を守るか」を測る点で、Physical AI 2100の文脈に直結する。

最大の未解決問題はphysics consistencyである。OpenAIはSoraの技術報告で「物理世界のシミュレータへの有望な道」と述べる一方、Soraには物理シミュレータとしての限界が多いとも明記した。Physics-IQでは、Sora初期版のI2Vスコアは10.0%、Runway Gen-3は22.8%、LumiereはI2V 19.0%またはmultiframe 23.0%にとどまる。これは、動画モデルが見た目のリアリズムを急速に高めても、接触、剛体、流体、保存則、隠れた物体の持続性を一貫して扱う能力は別問題であることを示す。World Modelをロボットの内部シミュレータとして使うには、単なる動画補間ではなく、状態、行為、物理量、失敗可能性を保持する必要がある。

## 2. 主要モデル深掘り（30 entries）

| # | Model / Institution | Release | Params | Training data | 物理一貫性スコア / Bench | URL |
|---|---|---:|---:|---|---|---|
| 1 | NVIDIA Cosmos / NVIDIA | CES 2025 | 4B-14B群 | 大規模動画、Physical AI向けデータ、Omniverse連携 | 未公表。Physical AI用WFMとして合成データ・未来予測を主目的化 | https://blogs.nvidia.com/blog/cosmos-world-foundation-models/ |
| 2 | Cosmos-Predict1 Text2World / NVIDIA | 2025 | 7B, 14B | 動画・テキスト条件 | 未公表。拡散型text-to-world | https://docs.nvidia.com/cosmos/latest/predict1/model_matrix.html |
| 3 | Cosmos-Predict1 Video2World diffusion / NVIDIA | 2025 | 7B, 14B | 動画・テキスト条件 | 未公表。動画から未来世界を生成 | https://research.nvidia.com/labs/cosmos-lab/cosmos-predict1/ |
| 4 | Cosmos-Predict1 AR Video2World / NVIDIA | 2025 | 4B, 5B, 12B, 13B | 動画・画像・テキスト | 未公表。自己回帰型未来状態予測 | https://docs.nvidia.com/cosmos/latest/predict1/model_matrix.html |
| 5 | Cosmos Transfer / NVIDIA | GTC 2025 | 未公表 | depth, lidar, segmentation, pose, trajectory等の構造化入力 | 未公表。3Dシミュレーションをフォトリアル動画へ変換 | https://nvidianews.nvidia.com/news/nvidia-announces-major-release-of-cosmos-world-foundation-models-and-physical-ai-data-tools |
| 6 | Cosmos Reason / NVIDIA | GTC 2025 | 未公表 | 動画・時空間データ | 未公表。箱が棚から落ちる等の相互作用を自然言語推論 | 同上 |
| 7 | Genie 2 / Google DeepMind | 2024-12-04 | 未公表 | 大規模動画データ | 公開物理スコアなし。最大1分程度、典型10-20秒の一貫世界 | https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/ |
| 8 | Genie 3 / Google DeepMind | 2025-08 | 未公表 | 未公表 | 公開物理スコアなし。リアルタイム相互作用、Genie 2より長期一貫性 | https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/ |
| 9 | V-JEPA / Meta | 2024 | 未公表 | 動画。特徴予測のみ、テキストや再構成なし | 生成モデルではないためPhysics-IQなし | https://arxiv.org/abs/2404.08471 |
| 10 | V-JEPA 2 / Meta | 2025-06 | 1.2B、LLM整合時8B | 100万時間超の動画、100万画像 | Meta新ベンチで人間85-95%に対しギャップあり。ロボットpick/place 65-80% | https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/ |
| 11 | V-JEPA 2-AC / Meta | 2025 | 1.2B基盤 | 62時間未満のDROIDロボット動画 | ロボット計画用。公開Physics-IQなし | https://arxiv.org/abs/2506.09985 |
| 12 | OpenAI Sora / OpenAI | 2024-02 preview, 2024-12 product | 未公表 | 動画・画像をspacetime patchesへ統一 | Physics-IQ I2V 10.0%。限界をOpenAI自身が記述 | https://openai.com/index/video-generation-models-as-world-simulators |
| 13 | Sora 2 / OpenAI | 2025 | 未公表 | 未公表 | Physics-IQ I2V 42.3%、WMReward BoNで46.4% | https://github.com/google-deepmind/physics-IQ-benchmark |
| 14 | Lumiere / Google Research | 2024-01 | 未公表 | 動画・テキスト | Physics-IQ multiframe 23.0%、I2V 19.0% | https://arxiv.org/abs/2401.12945 |
| 15 | Veo 2 / Google DeepMind | 2024-12 | 未公表 | 未公表 | 公開Physics-IQなし。Googleは物理・運動理解を強調 | https://deepmind.google/discover/blog/state-of-the-art-video-and-image-generation-with-veo-2-and-imagen-3/ |
| 16 | Veo 3 / Google DeepMind | 2025-05-20 | 未公表 | audio, video, image。Geminiで多段階caption付与、重複除去 | 公開Physics-IQなし。モデルカードで物理・運動の改善と複雑運動の限界を併記 | https://storage.googleapis.com/deepmind-media/Model-Cards/Veo-3-Model-Card.pdf |
| 17 | Runway Gen-3 Alpha / Runway | 2024-06-17 | 未公表 | videos and images、密な時間caption | Physics-IQ I2V 22.8%。Video-Bench overall rank 1.78 | https://runwayml.com/research/introducing-gen-3-alpha |
| 18 | Runway Gen-4 / Runway | 2025-03-31 | 未公表 | 未公表 | 公開Physics-IQなし。World consistency、物理シミュレーションを主張 | https://runwayml.com/research/introducing-runway-gen-4 |
| 19 | HunyuanVideo / Tencent | 2024-12-03 | 13B超 | 大規模キュレーション動画、progressive scaling | VBench 1.0 launchでopen-source SOTA、Physics-IQ未掲載 | https://arxiv.org/abs/2412.03603 |
| 20 | Vidu / Shengshu + Tsinghua | 2024-05 | 未公表 | 未公表 | 公開Physics-IQなし。1080p、最大16秒、U-ViT backbone | https://arxiv.org/abs/2405.04233 |
| 21 | Kling 1.0 / Kuaishou | 2024-06 | 未公表 | 未公表 | WorldModelBench total 8.82/10、最上位 | https://ir.kuaishou.com/news-releases/news-release-details/kuaishou-unveils-proprietary-video-generation-model-kling |
| 22 | Kling 1.6 / Kuaishou | 2024-Q4 | 未公表 | 未公表 | 公開Physics-IQなし。Kuaishou決算でアップグレード言及 | https://ir.kuaishou.com/news-releases/news-release-details/kuaishou-technology-announces-fourth-quarter-and-full-year-2024 |
| 23 | World Labs Generating Worlds / World Labs | 2024-12 | 未公表 | 未公表 | 公開物理スコアなし。単一画像から探索可能3D空間 | https://www.worldlabs.ai/blog |
| 24 | World Labs RTFM / World Labs | 2025-09 | 未公表 | 未公表 | 公開物理スコアなし。リアルタイムframe model研究preview | https://www.worldlabs.ai/blog |
| 25 | 1X World Model / 1X | 2025-2026 | 未公表 | web-scale video + 1X robot data | 1XWM Challengeあり。公開汎用Physics-IQなし | https://www.1x.tech/1x-world-model.pdf |
| 26 | GAIA-1 / Wayve | 2023, 9B scaling | 9B | 4,700時間のLondon運転データ | 公開Physics-IQなし。自動運転用生成World Model | https://wayve.ai/thinking/scaling-gaia-1/ |
| 27 | GAIA-2 / Wayve | 2025 | 未公表 | multi-view driving data | 公開物理スコアなし。controllable multi-view driving | https://arxiv.org/abs/2503.20523 |
| 28 | DreamerV3 / DeepMind | 2023 | 8M-200M級実験 | RL環境経験 | Atari/Minecraft等150超タスク。動画物理ベンチではない | https://arxiv.org/abs/2301.04104 |
| 29 | GameNGen / Google | 2024-08 | Stable Diffusion系、詳細未公表 | DOOM gameplay | 20fps超、単一TPUでDoomをニューラルゲームエンジン化 | https://arxiv.org/abs/2408.14837 |
| 30 | DIAMOND / Microsoft Research等 | 2024-05 | 未公表 | Atari、CS:GO gameplay | Atari 100k mean human normalized score 1.46 | https://arxiv.org/abs/2405.12399 |
| 31 | Sony AI / Sony | 2024-2025 | 未公表 | GT Sophy、AMR、ロボット研究 | 専用World Foundation Modelの公開確認なし。物理シミュレータ・モデルベース制御研究は確認 | https://www.sony.com/en/SonyInfo/News/Press/202410/24-035E/ |
| 32 | PFN / Preferred Networks | 2024-2026 | 未公表 | 未公表 | 公開World Modelベンチ確認なし。ロボティクス・実世界AI事業は確認 | https://www.preferred.jp/en/projects/robotics/ |

## 3. ベンチマーク数値比較

Physics-IQは最も直接的に「動画生成モデルは物理を理解しているか」を問う。Google DeepMindの公開leaderboardでは、理想的な物理現実動画を100%とし、Sora初期版I2Vは10.0%、Pika 1.0は13.0%、Stable Video Diffusionは14.8%、Lumiere I2Vは19.0%、VideoPoet I2Vは20.3%、Runway Gen-3 I2Vは22.8%、Lumiere multiframeは23.0%、VideoPoet multiframeは29.5%、Sora 2 I2Vは42.3%、Sora 2 + WMReward BoNは46.4%、Magi-1 multiframeは56.0%、Magi-1 + WMReward BoNは62.6%である。初期Soraは視覚的には衝撃的だったが、Physics-IQでは低く、Sora 2世代で大幅に改善している。

WorldModelBenchは10点満点で、Instruction最大3、Common Sense最大2、Physics Adherence最大5として採点する。Table 3では、Klingが8.82、Minimaxが8.59、Mochi-officialが8.37、Runwayが8.08、Lumaが7.72である。Open modelではMochi 7.62、OpenSoraPlan-T2V 7.61、CogVideoX-T2V 7.31、CogVideoX-I2V 6.75、OpenSora-I2V 5.83となる。重要なのは、上位のKlingでも、タスク完了率や質量保存、物体貫通にまだ失敗が残る点である。World Modelとしては「高得点」でも「物理的に信頼できる内部シミュレータ」には達していない。

VBenchはsubject consistency、background consistency、temporal flickering、motion smoothness、dynamic degree、aesthetic quality、object class、spatial relationship、overall consistencyなど16次元を評価する。公式GitHubはleaderboardへのリンクと評価次元を公開しているが、動的Hugging Face Spaceのため、ここでは確認可能な補助数値としてVideo-Benchの公開表も併記する。Video-BenchではGen3がimaging quality 4.66、aesthetic 4.44、temporal consistency 4.74、overall avg rank 1.78で、Klingはimaging 4.26、temporal 4.38、overall avg rank 3.78である。VBench系は視覚・時間品質に強いが、Physics-IQやWorldModelBenchほど物理法則を直接には問わない。

## 4. 物理理解の限界

Object permanenceでは、キャラクターや物体が一時的に画面外へ出た後、形状、数、位置、同一性が変わる。Runway Gen-4やVeo 3は一貫性を強く改善したが、GoogleのVeo 3モデルカードも、複雑なシーンや複雑運動で完全な一貫性維持が課題と述べる。World LabsやGenie 3は探索可能世界を目指すが、長時間・任意視点の幾何的記憶はまだ研究段階である。

Gravityでは、落下、跳ね返り、接触後の停止、斜面上の滑りが破綻しやすい。MetaのV-JEPA 2ブログは、空中のテニスボールが突然方向転換したりリンゴに変わる例を、World Modelが避けるべき失敗として説明している。WorldModelBenchでもgravitation、Newton法則が独立採点されるのは、この失敗が現行モデルで頻出するからである。

Fluidでは、見た目の水面や煙は得意になったが、体積保存、粘性、容器との相互作用、流入・流出の連続性は弱い。Physics-IQは流体、熱、磁性、光学、固体を分けて評価し、流体は相対的にうまくいく例もあるが、視覚的リアリズムが物理理解を意味しないと結論している。

Contact dynamicsでは、手が物体を掴む、布を畳む、箱を押す、ドアを開けるなどの接触豊富な操作が難しい。1XWMやV-JEPA 2-ACがロボットデータを後段学習に入れる理由はここにある。Web動画だけでは、接触力、摩擦、関節状態、失敗時の反力が観測できない。ロボット用World Modelでは、視覚だけでなくproprioception、action token、軌道、深度、接触イベントを条件にする必要がある。

## 5. Robotics統合

World ModelをVLAの内部シミュレータとして使う方向は、2025年から明確に加速した。VLAは視覚・言語から直接行動を出すが、そのままでは「行動候補を頭の中で試す」能力が弱い。V-JEPA 2-ACは、現在状態と目標画像を潜在空間に写し、候補行動の結果をpredictorで想像し、モデル予測制御で次行動を選ぶ。Metaは62時間未満のロボット動画で、未知物体のpick-and-placeに65-80%の成功率を報告している。

NVIDIA Cosmosは、ロボットや自動運転のVLA/Policy modelに対して、外部・内部の両方のシミュレータとして働く。Cosmos Predictは未来世界状態を生成し、Cosmos TransferはOmniverseや構造化センサー入力をフォトリアル動画へ変換し、Cosmos Reasonは動画内相互作用を自然言語で推論する。NVIDIAは1X、Agility Robotics、Figure AI、Skild AI、Uberなどの採用を発表している。

1X World Modelは、NEO humanoidのために、web-scale videoで事前学習し、1Xロボットデータで後段学習する。論文では、full-body humanoidのcontact-rich futuresを予測することを主張し、1X World Model Challengeではsamplingとcompressionの2トラックを設ける。これは、World Modelを単なる動画生成器ではなく、ロボット行動評価器、失敗予測器、データ生成器として使う流れである。

自動運転ではWayve GAIA-1/GAIA-2が代表例である。GAIA-1は動画、テキスト、行動入力から運転シナリオを生成し、9B版はLondonの4,700時間データで訓練された。GAIA-2はmulti-view制御を加え、車載カメラ群に近い世界予測へ進む。GameNGenやDIAMONDはゲーム環境で、UniSimやInteractive World Simulator系は実世界相互作用で、同じ発想を異なる安全な環境に展開している。

## 6. 2026-2030 outlook

2026-2030年のWorld Model研究は、第一に「動画生成」から「状態生成」へ移る。高品質動画は入口にすぎず、ロボットや自動運転では、見た目よりも、物体ID、3D幾何、接触、速度、力、摩擦、失敗確率が必要になる。したがって、VeoやRunwayのようなクリエイティブ動画モデルと、Cosmos、1XWM、GAIA、V-JEPA系のPhysical AIモデルは分岐しつつ連携する。

第二に、評価はより厳しくなる。VBench的な視覚品質、Physics-IQ的な物理原理、WorldModelBench的な行為条件付き整合性、さらにロボット実機成功率を組み合わせなければ、World Modelの有用性は測れない。現状の数値を見る限り、Sora 2やMagi-1系は初期Soraより大きく改善したが、100%の物理現実性には遠い。

第三に、シミュレータと学習モデルは融合する。Omniverse、MuJoCo、Isaac、MPMなどの明示的物理シミュレータは、ニューラルWorld Modelに教師信号や構造制約を与える。一方、ニューラルWorld Modelは、手作業で作れない多様な環境、外観、失敗例、レアイベントを生成する。2026年以降のPhysical AIでは、純粋なデータ駆動でも純粋な物理エンジンでもなく、両者のハイブリッドが主流になる。

第四に、日本勢は、公開された「World Foundation Model」では米中大手に遅れるが、Sony AIの高忠実度シミュレーション、ロボティクス、GT Sophy系の強化学習、PFNのロボティクス・エッジAI・製造業接続には接続点がある。重要なのは、汎用動画モデルを後追いすることより、製造、モビリティ、家庭ロボット、材料、サービス現場の高品質な実世界データと評価環境を握ることである。

結論として、2024-2026年のWorld Model AIは、Soraの「world simulator」論から、Cosmos/Genie/V-JEPA/1XWM/GAIAの「Physical AIの内部シミュレータ」へと重心を移した。2030年までの勝負は、長時間一貫性、接触物理、3D記憶、行為条件付き予測、実機閉ループ評価をどこまで統合できるかにかかっている。
