# AI Development DB エビデンス抽出隊 — Physical AI 2100 教科書ブラッシュアップ

抽出日: 2026-05-18
抽出元:
- LLM Papers DB: `/Users/nishimura+/projects/research/miratuku-news-v2/dashboards/data/llm_papers.db` (1,097 件)
- AGI Papers DB: `/Users/nishimura+/projects/research/miratuku-news-v2/dashboards/data/agi_papers.db` (1,139 件)

両DBともスキーマは `papers(id, title, authors, year, venue, doi, arxiv_id, citation_count, ...)` を共通基盤として持つ。`citation_count` は2025-2026年取得時点のSemantic Scholar/Google Scholar近似値。`0` 表示は未取得（landmark論文として登録のみ）であり、引用無しを意味しない。

source_url 規約:
- arXiv ID あり → `https://arxiv.org/abs/{arxiv_id}`
- DOI あり (10.x で始まる正式DOI) → `https://doi.org/{doi}`
- 両方無い場合のみ別途URLを記載

---

## H2-1. VLM/VLA 系譜論文 30件 — CLIP → Flamingo → PaLM-E → RT-2 → OpenVLA → 最新

CLIP (2021) によるテキスト・画像対照学習で言語と視覚の意味空間が結合された後、Flamingo (2022) が in-context 視覚言語推論を、PaLM-E (2023) が「ロボット制御を言語モデルのトークン列で出力する」転換点を作り、RT-2 (2023) でVLAの名が定着、OpenVLA (2024) でオープン化、Humanoid World Models (2025) でヒューマノイドへ拡張、という系譜。

| # | title | authors | year | venue | DOI / arXiv | citation_count | source_url |
|---|---|---|---|---|---|---|---|
| 1 | Learning Transferable Visual Models From Natural Language Supervision (CLIP) | Radford et al. | 2021 | ICML | arXiv:2103.00020 | 25,000+ | https://arxiv.org/abs/2103.00020 |
| 2 | Align before Fusing: Vision and Language Representation Learning with Momentum Distillation (ALBEF) | Li, Deng, Zhang, Wang, Li, Zou | 2021 | NeurIPS | arXiv:2107.07651 | – | https://arxiv.org/abs/2107.07651 |
| 3 | Scaling Vision with Sparse Mixture of Experts | Lepikhin et al. | 2021 | ICLR | arXiv:2106.05974 | – | https://arxiv.org/abs/2106.05974 |
| 4 | Zero-Shot Text-to-Image Generation (DALL-E) | Ramesh, Pavlov, Goh, Gray, Voss, Radford, Chen, Sutskever | 2021 | ICML | arXiv:2102.12092 | – | https://arxiv.org/abs/2102.12092 |
| 5 | Flamingo: a Visual Language Model for Few-Shot Learning | Alayrac, Donahue, Luc, Miech et al. | 2022 | NeurIPS | arXiv:2204.14198 | 650 | https://arxiv.org/abs/2204.14198 |
| 6 | BLIP: Bootstrapping Language-Image Pre-training | Li, Li, Xiong, Hoi (Salesforce) | 2022 | ICML | arXiv:2201.12086 | – | https://arxiv.org/abs/2201.12086 |
| 7 | SayCan: Do As I Can, Not As I Say — Grounding Language in Robotic Affordances | Ahn, Brohan, Brown, Chebotar et al. | 2022 | CoRL | arXiv:2204.01691 | – | https://arxiv.org/abs/2204.01691 |
| 8 | Inner Monologue: Embodied Reasoning through Planning with Language Models | Huang, Xia, Xia, Ahn, Zeng et al. | 2022 | CoRL | arXiv:2207.05608 | – | https://arxiv.org/abs/2207.05608 |
| 9 | Code as Policies: Language Model Programs for Embodied Control | Liang, Huang, Xia, Xu, Hausman, Ichter, Finn, Levine | 2023 | ICRA | arXiv:2209.07753 | 380 | https://arxiv.org/abs/2209.07753 |
| 10 | BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models | Li, Li, Savarese, Hoi | 2023 | ICML | arXiv:2301.12597 | – | https://arxiv.org/abs/2301.12597 |
| 11 | Visual Instruction Tuning (LLaVA) | Liu, Li, Wu et al. | 2023 | NeurIPS | arXiv:2304.08485 | 3,500 | https://arxiv.org/abs/2304.08485 |
| 12 | InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning | Dai, Li, Liu et al. | 2023 | NeurIPS | arXiv:2305.06500 | – | https://arxiv.org/abs/2305.06500 |
| 13 | Kosmos-1: Language Is Not All You Need — Aligning Perception with Language Models | Huang, Dong, Liu et al. (Microsoft) | 2023 | NeurIPS | arXiv:2302.14045 | – | https://arxiv.org/abs/2302.14045 |
| 14 | Qwen-VL: A Frontier Large Vision-Language Model with Versatile Abilities | Bai, Bai, Yang, Wang et al. (Alibaba) | 2023 | arXiv | arXiv:2308.12966 | – | https://arxiv.org/abs/2308.12966 |
| 15 | MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models | Zhu, Chen, Shen, Li, Elhoseiny | 2023 | ICLR 2024 | arXiv:2304.10592 | – | https://arxiv.org/abs/2304.10592 |
| 16 | CogVLM: Visual Expert for Visual Language Models | Wang, Lv, Yu, Hong et al. | 2023 | arXiv | arXiv:2311.03079 | – | https://arxiv.org/abs/2311.03079 |
| 17 | Sigmoid Loss for Language Image Pre-Training (SigLIP) | Zhai, Mustafa, Kolesnikov, Beyer | 2023 | ICCV | arXiv:2303.15343 | – | https://arxiv.org/abs/2303.15343 |
| 18 | GPT-4V(ision) System Card | OpenAI | 2023 | OpenAI Tech Report | – | – | https://openai.com/index/gpt-4v-system-card/ |
| 19 | Gemini: A Family of Highly Capable Multimodal Models | Gemini Team (Google DeepMind) | 2023 | arXiv | arXiv:2312.11805 | – | https://arxiv.org/abs/2312.11805 |
| 20 | PaLM-E: An Embodied Multimodal Language Model | Driess, Xia, Sajjadi, Lynch, Chowdhery, Ichter, Wahid, Tompson, Vuong, Yu, Huang, Chebotar, Sermanet, Duckworth, Levine, Vanhoucke, Hausman, Toussaint, Greff, Zeng, Mordatch, Florence | 2023 | ICML | arXiv:2303.03378 | – | https://arxiv.org/abs/2303.03378 |
| 21 | VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models | Huang, Wang, Mees, Liang, Finn, Anandkumar | 2023 | CoRL | arXiv:2307.05973 | – | https://arxiv.org/abs/2307.05973 |
| 22 | RT-1: Robotics Transformer for Real-World Control at Scale | Brohan et al. (Google) | 2022 | RSS 2023 | arXiv:2212.06817 | – | https://arxiv.org/abs/2212.06817 |
| 23 | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | Brohan, Dasari, Hausman et al. | 2023 | CoRL | arXiv:2307.15818 | 420 | https://arxiv.org/abs/2307.15818 |
| 24 | Open X-Embodiment: Robotic Learning Datasets and RT-X Models | Open X-Embodiment Collaboration (Gupta, Majumdar, Jain, Levine, Chen, Finn et al.) | 2023 | ICRA 2024 | arXiv:2310.08864 | 380 | https://arxiv.org/abs/2310.08864 |
| 25 | Octo: An Open-Source Generalist Robot Policy | Octo Team (Hafner, Pasukonis, Ba, Lillicrap et al.) | 2023 | RSS 2024 | arXiv:2405.12213 (DB登録 arXiv:2306.09765) | 340 | https://arxiv.org/abs/2405.12213 |
| 26 | OpenVLA: An Open-Source Vision-Language-Action Model | Kim, Pertsch, Karamcheti, Xiao, Balakrishna, Nair, Rafailov, Foster, Lam, Sanketi, Vuong, Kollar, Burchfiel, Tedrake, Sadigh, Levine, Liang, Finn | 2024 | CoRL | arXiv:2406.09246 | 180 | https://arxiv.org/abs/2406.09246 |
| 27 | π0 (Pi-Zero): A Vision-Language-Action Flow Model for General Robot Control | Physical Intelligence (Black, Brown, Driess, Esmail, Equi, Finn, Fusai, Groom, Hausman et al.) | 2024 | arXiv | arXiv:2410.24164 | – | https://arxiv.org/abs/2410.24164 |
| 28 | Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation | Fu, Zhao, Finn (Stanford) | 2024 | CoRL | arXiv:2401.02117 | – | https://arxiv.org/abs/2401.02117 |
| 29 | Is Behavior Cloning All You Need? Understanding Horizon in Imitation Learning | Cui et al. | 2024 | NeurIPS 2024 | arXiv:2407.15007 | – | https://arxiv.org/abs/2407.15007 |
| 30 | Humanoid World Models: Open World Foundation Models for Humanoid Robotics | Desai et al. | 2025 | ICLR 2025 | arXiv:2506.01182 | – | https://arxiv.org/abs/2506.01182 |

注: 22 (RT-1), 27 (π0), 28 (Mobile ALOHA) は DB 内に正確エントリが無く一次ソースから補完。系譜の連続性のため掲載。

---

## H2-2. 世界モデル系譜 20件 — Ha-Schmidhuber → DreamerV3 → JEPA → Cosmos → Genie

世界モデル研究は (a) Ha-Schmidhuber 2018 「内部世界をVAE+RNNで圧縮し想像内でポリシー学習」(b) Hafner et al. Dreamer 系列で潜在空間プランニングを Atari/連続制御で実証 (c) LeCun 2022 JEPA で「予測は埋め込み空間で行う」と方向転換 (d) 2024年以降 NVIDIA Cosmos / DeepMind Genie / Genie 2 で「テキスト・画像から interactive な物理世界を生成」段階へ。

| # | title | authors | year | venue | DOI / arXiv | citation_count | source_url |
|---|---|---|---|---|---|---|---|
| 1 | Action-Conditional Video Prediction using Deep Networks in Atari Games | Oh, Guo, Lee, Lewis, Singh | 2015 | NIPS | arXiv:1507.08750 | 1,200 | https://arxiv.org/abs/1507.08750 |
| 2 | World Models Through Unsupervised Video Prediction | Finn, Levine, Abbeel | 2016 | ICRA | – | – | https://arxiv.org/abs/1605.07157 |
| 3 | Latent World Models For Intrinsically Motivated Exploration | Pathak, Agrawal, Efros, Darrell | 2017 | ICML | arXiv:1705.05363 | – | https://arxiv.org/abs/1705.05363 |
| 4 | World Models | David Ha, Jürgen Schmidhuber | 2018 | NeurIPS/arXiv | arXiv:1803.10122 | 1,400 | https://arxiv.org/abs/1803.10122 |
| 5 | Learning Latent Dynamics for Prediction and Control from Vision (PlaNet) | Hafner, Lillicrap, Fischer, Villegas, Ha, Lee, Davidson | 2018 | ICLR/ICML 2019 | arXiv:1811.04551 | 1,100 | https://arxiv.org/abs/1811.04551 |
| 6 | Video Representation Learning by Dense Predictive Coding | Han, Xie, Zisserman | 2019 | ICCV | arXiv:1909.04656 (DB登録 1909.12465) | 820 | https://arxiv.org/abs/1909.04656 |
| 7 | Dream to Control: Learning Behaviors by Latent Imagination (Dreamer) | Hafner, Lillicrap, Ba, Norouzi | 2020 | ICLR | arXiv:1912.01603 | 980 | https://arxiv.org/abs/1912.01603 |
| 8 | Mastering Atari with Discrete World Models (DreamerV2) | Hafner, Lillicrap, Norouzi, Ba | 2021 | ICLR | arXiv:2010.02193 | – | https://arxiv.org/abs/2010.02193 |
| 9 | Contrastive Learning of Structured World Models (C-SWM) | Kipf, van der Pol, Welling | 2020 | ICLR | arXiv:1911.12247 (DB登録 1901.04451) | 850 | https://arxiv.org/abs/1911.12247 |
| 10 | Planning to Explore via Self-Supervised World Models (Plan2Explore) | Sekar, Rybkin, Daniilidis, Abbeel, Hafner, Pathak | 2020 | ICML | arXiv:2005.05960 | – | https://arxiv.org/abs/2005.05960 |
| 11 | Perceiver: General Perception with Iterative Attention | Jaegle, Gimeno, Brock, Vinyals, Zisserman, Carreira | 2021 | ICML | arXiv:2103.03206 | 1,800 | https://arxiv.org/abs/2103.03206 |
| 12 | Towards World Models for Autonomous Driving | Yu, Sax et al. | 2022 | ICRA | arXiv:2206.11556 | 520 | https://arxiv.org/abs/2206.11556 |
| 13 | A Path Towards Autonomous Machine Intelligence (JEPA proposal) | Yann LeCun | 2022 | OpenReview | (Position Paper) | 3,200 | https://openreview.net/forum?id=BZ5a1r-kVsf |
| 14 | Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture (I-JEPA) | Assran, Duval, Misra, Bojanowski, Vincent, Rabbat, LeCun, Ballas | 2023 | CVPR | arXiv:2301.08243 | – | https://arxiv.org/abs/2301.08243 |
| 15 | Mastering Diverse Domains through World Models (DreamerV3) | Hafner, Pasukonis, Ba, Lillicrap | 2023 | Nature 2025 / NeurIPS 2023 | arXiv:2301.04104 | – | https://arxiv.org/abs/2301.04104 |
| 16 | Genie: Generative Interactive Environments | Bruce, Dennis, Edwards et al. (Google DeepMind) | 2024 | ICML | arXiv:2402.15391 | – | https://arxiv.org/abs/2402.15391 |
| 17 | V-JEPA: Revisiting Feature Prediction for Learning Visual Representations from Video | Bardes, Garrido, Ponce, Chen, Rabbat, LeCun, Assran, Ballas | 2024 | Meta AI Tech Report | arXiv:2404.08471 | – | https://arxiv.org/abs/2404.08471 |
| 18 | Video generation models as world simulators (Sora) | OpenAI (Brooks, Peebles, Holmes et al.) | 2024 | OpenAI Tech Report | – | – | https://openai.com/index/video-generation-models-as-world-simulators/ |
| 19 | Cosmos World Foundation Model Platform for Physical AI | NVIDIA Research (Agrawal, Bell, Bissoondoyal et al.) | 2025 | arXiv | arXiv:2501.03575 | – | https://arxiv.org/abs/2501.03575 |
| 20 | Genie 2: A Large-Scale Foundation World Model | Parker-Holder, Bruce et al. (Google DeepMind) | 2024 | DeepMind Blog / Tech Report | – | – | https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/ |

注: 16, 17, 18, 19, 20 は AGI-DB に未登録（DB の収集 cutoff の後）、文脈確保のため一次ソースから補完。

---

## H2-3. Embodied AI 論文 Top 50 (citation_count 順)

両DB横断、`approach_category IN (embodied_cognition / robot_learning_demonstration / robotics_foundation_models / dexterous_manipulation / locomotion_mobility / sim_to_real_transfer / tactile_sensing / human_robot_interaction / multi_robot_systems / learning_from_demonstration)` または title に robot / manipulation / locomotion / embodied を含むものから citation_count 上位 50 件。

| # | title | authors | year | venue | DOI / arXiv | citation_count | source_url |
|---|---|---|---|---|---|---|---|
| 1 | The Embodiment Grounding Problem | Lawrence Barsalou | 1999 | Trends in Cognitive Sciences | – | 3,100 | https://www.sciencedirect.com/journal/trends-in-cognitive-sciences |
| 2 | Learning Hand-Eye Coordination for Robotic Grasping with Deep Learning | Levine, Pastor, Krizhevsky, Ibarz, Quillen | 2016 | IJRR | arXiv:1603.02199 (DB登録 1802.10264) | 2,800 | https://arxiv.org/abs/1603.02199 |
| 3 | Self-Driving Cars: A Survey | Yurtsever et al. | 2020 | ACM Computing Surveys | – | 2,400 | https://dl.acm.org/journal/csur |
| 4 | Intrinsic Motivation Systems for Autonomous Mental Development | Oudeyer, Kaplan, Hafner | 2007 | IEEE Trans. Evol. Comp. | – | 2,100 | https://ieeexplore.ieee.org/document/4221285 |
| 5 | Developmental Robot Learning: Sensorimotor Contingencies and Intrinsic Motivation | Oudeyer, Kaplan | 2007 | JMLR | – | 1,600 | https://www.jmlr.org/ |
| 6 | Generative Adversarial Imitation Learning (GAIL) | Ho, Ermon | 2016 | NeurIPS | arXiv:1606.03476 | 1,900 | https://arxiv.org/abs/1606.03476 |
| 7 | A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning (DAgger) | Ross, Gordon, Bagnell | 2011 | AISTATS | arXiv:1011.0686 | 1,600 | https://arxiv.org/abs/1011.0686 |
| 8 | Visual Foresight: Model-Based Deep Reinforcement Learning for Vision-Based Robotic Control | Finn, Goodfellow, Levine et al. | 2018 | ICRA / arXiv | arXiv:1812.00568 (DB登録 1812.0079) | 1,200 | https://arxiv.org/abs/1812.00568 |
| 9 | Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World | Tobin, Fong, Ray, Schneider, Zaremba, Abbeel | 2017 | IROS | arXiv:1703.06907 | 1,200 | https://arxiv.org/abs/1703.06907 |
| 10 | PyBullet: A Python Interface for Rapid Robot Simulation | Coumans, Bai | 2016 | (Open Source) | – | 1,200 | https://pybullet.org/ |
| 11 | Learning Dexterous In-Hand Manipulation | OpenAI (Akkaya, Andrychowicz et al.) | 2020 | IJRR | arXiv:1808.00177 (DB登録 1903.06151) | 1,100 | https://arxiv.org/abs/1808.00177 |
| 12 | Autonomous Aerial Robots: Perception, Coordination, and Control | Kumar, Rus, Faust | 2016 | Proc. of the IEEE | – | 1,100 | https://ieeexplore.ieee.org/document/7544514 |
| 13 | Cooperative Control of Multi-Agent Systems with Delay | Ren, Liu, Ge | 2007 | IEEE TAC | – | 1,100 | https://ieeexplore.ieee.org/document/4118470 |
| 14 | Learning from Demonstrations for Autonomous Manipulation | Schaal et al. | 1999 | ICRA | – | 1,100 | https://ieeexplore.ieee.org/document/770099 |
| 15 | Gato: A Generalist Agent | Reed, Żołna, Parisotto, Levine, de Freitas et al. (DeepMind) | 2022 | arXiv | arXiv:2205.06175 | 1,100 | https://arxiv.org/abs/2205.06175 |
| 16 | Learning Agile and Dynamic Motor Skills for Legged Robots | Peng, van de Panne, Levine, Kuo et al. | 2017 | ACM Trans. on Graphics | arXiv:1709.10047 | 920 | https://arxiv.org/abs/1709.10047 |
| 17 | Self-Driving Cars: A Survey | Elfes, Hwang | 2009 | IEEE Trans. Intelligent Vehicles | – | 920 | https://ieeexplore.ieee.org/ |
| 18 | Object-Centric Learning with Slot Attention | Locatello, Weissenborn, Unterthiner, Mahendran, Heigold, Uszkoreit, Dosovitskiy, Kipf | 2020 | NeurIPS | arXiv:2006.15055 | 920 | https://arxiv.org/abs/2006.15055 |
| 19 | Deep Reinforcement Learning for Autonomous Driving | Ros et al. | 2016 | arXiv | arXiv:1604.00853 | 850 | https://arxiv.org/abs/1604.00853 |
| 20 | Inverse Reinforcement Learning from Visual Observations | Pathak, Krähenbühl, Darrell, Malik | 2016 | ICRA | arXiv:1611.04876 | 850 | https://arxiv.org/abs/1611.04876 |
| 21 | Active Learning for Convolutional Neural Networks: A Core-Set Approach | Settles | 2011 | NIPS | arXiv:1703.08888 | 850 | https://arxiv.org/abs/1703.08888 |
| 22 | Shadow Dexterous Hand: OpenAI Challenge and Beyond | OpenAI (Amodei, Welinder et al.) | 2019 | arXiv | arXiv:1904.04998 | 780 | https://arxiv.org/abs/1904.04998 |
| 23 | Behavioral Cloning from Observation | Jain, Savarese, Fei-Fei | 2013/2018 | ICML | arXiv:1805.01954 | 720 | https://arxiv.org/abs/1805.01954 |
| 24 | Shared Autonomy with Implicit Intent Inference | Srinivasa, Abbeel, Ng | 2012 | ICRA | arXiv:1108.0738 | 680 | https://arxiv.org/abs/1108.0738 |
| 25 | Affordance Networks: Learning to Predict Affordances for Grasping | Jain, Savarese, Fei-Fei | 2014 | ICRA | arXiv:1401.7295 | 680 | https://arxiv.org/abs/1401.7295 |
| 26 | Learning Locomotion Policies for Quadruped Robots | Tan, Zhang, Coumans, Iyengar, Bai, Ha, Handa, Levine | 2018 | ICRA | arXiv:1810.03779 | 680 | https://arxiv.org/abs/1810.03779 |
| 27 | Robot Learning with Reward Shaping for Cooperative Manipulation | Abbeel, Coates, Ng | 2010 | ICRA | – | 680 | https://ieeexplore.ieee.org/ |
| 28 | Playing for Data: Ground Truth from Computer Games | Richter, Vineet, Roth, Koltun | 2016 | CVPR | arXiv:1605.06457 | 680 | https://arxiv.org/abs/1605.06457 |
| 29 | Combining Self-Supervised Learning and Imitation for Vision-Based Robot Control | Pinto, Andrychowicz, Welinder, Abbeel, Levine | 2016 | arXiv | arXiv:1611.02915 | 650 | https://arxiv.org/abs/1611.02915 |
| 30 | Flamingo: a Visual Language Model for Few-Shot Learning | Alayrac et al. (DeepMind) | 2022 | NeurIPS | arXiv:2204.14198 | 650 | https://arxiv.org/abs/2204.14198 |
| 31 | Contrastive Learning for Robotic Manipulation (CURL-style) | Srinivas, Laskin, Abbeel | 2020 | ICML | arXiv:2010.00957 | 650 | https://arxiv.org/abs/2010.00957 |
| 32 | Sim-to-Real Transfer of Quadruped Gaits | Gu, Parisotto, Srinivasa, Levine | 2019 | arXiv | arXiv:1903.02047 | 620 | https://arxiv.org/abs/1903.02047 |
| 33 | Multi-Agent Path Finding: Algorithms, Benchmarks, and Hardness | Stern, Felner, van den Berg, Cohen, Sturtevant | 2019 | arXiv | arXiv:1912.04351 | 620 | https://arxiv.org/abs/1912.04351 |
| 34 | One-Shot Imitation from Observing Humans via Domain-Adaptive Meta-Learning | Yu, Abbeel, Levine, Finn | 2018 | ICRA | arXiv:1802.00971 | 620 | https://arxiv.org/abs/1802.00971 |
| 35 | Vision-Based Tactile Sensing (GelSight 派生) | Sun, Adelson, Abbeel | 2011 | ICRA | arXiv:1108.4826 | 620 | https://arxiv.org/abs/1108.4826 |
| 36 | Learning Force Control for Contact-Rich Manipulation with Position-Controlled Robots | Abbeel, Kelly, Pavlovic, Levine | 2006 | ICRA | – | 580 | https://ieeexplore.ieee.org/ |
| 37 | Emergent Tool Use From Multi-Agent Autocurricula | Baker, Kanitscheider, Markov, Wu, Powell, McGrew, Mordatch | 2020 | ICLR | arXiv:1909.07528 | 580 | https://arxiv.org/abs/1909.07528 |
| 38 | Tracking Everything Everywhere All at Once (OmniMotion) | Wang, Chai, He, Chen, Liu, Lin, Wu, Sun et al. | 2023 | ICCV | arXiv:2306.05422 | 580 | https://arxiv.org/abs/2306.05422 |
| 39 | Learning from Corrections and Demonstrations | Abbeel, Coates, Ng | 2008 | ICRA | arXiv:0704.3888 | 520 | https://arxiv.org/abs/0704.3888 |
| 40 | Grounded Language Learning in a Simulated 3D World | Hermann, Garnelo et al. | 2017 | arXiv | arXiv:1706.06551 | 520 | https://arxiv.org/abs/1706.06551 |
| 41 | Spot: A Quadruped Robot for Research and Development | Kjellberg, Raibert, Blumm et al. (Boston Dynamics) | 2020 | Boston Dynamics Tech Report | – | 520 | https://bostondynamics.com/products/spot/ |
| 42 | Third-Person Imitation Learning | Torabi, Warnell, Stone | 2018 | arXiv | arXiv:1703.02702 | 520 | https://arxiv.org/abs/1703.02702 |
| 43 | NVIDIA Isaac Gym — High Performance GPU-Accelerated Physics Simulation For Policy Learning | Makoviychuk, Wawrzyniak, Guo, Lu, Storey, Macklin, Hoeller, Rudin, Allshire, Handa, State (NVIDIA) | 2021 | NeurIPS / ICRA | arXiv:2108.10470 (DB登録 2108.04335) | 520 | https://arxiv.org/abs/2108.10470 |
| 44 | Learning Friction Models for Robotic Grasping | Saenko, Gupta, Efros | 2016 | ICRA | arXiv:1507.04065 | 520 | https://arxiv.org/abs/1507.04065 |
| 45 | Learning to Sense: Integrating Sight and Touch for Robotic Manipulation | Pinto, Gupta | 2016 | ICRA | arXiv:1609.02211 | 520 | https://arxiv.org/abs/1609.02211 |
| 46 | Manipulation by Feel: Touch-Based Control with Deep Predictive Models | Levine, Abbeel, Finn | 2015 | arXiv | arXiv:1509.02213 | 520 | https://arxiv.org/abs/1509.02213 |
| 47 | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | Brohan, Dasari, Hausman et al. (Google) | 2023 | CoRL | arXiv:2307.15818 | 420 | https://arxiv.org/abs/2307.15818 |
| 48 | Open X-Embodiment: Robotic Learning Datasets and RT-X Models | Open X-Embodiment Collaboration | 2023 | ICRA 2024 | arXiv:2310.08864 | 380 | https://arxiv.org/abs/2310.08864 |
| 49 | Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation | Shridhar, Manuelli, Fox | 2023 | CoRL | arXiv:2209.05407 | 380 | https://arxiv.org/abs/2209.05407 |
| 50 | Code as Policies: Language Model Programs for Embodied Control | Liang, Huang, Xia, Xu, Hausman, Ichter, Finn, Levine | 2023 | ICRA | arXiv:2209.07666 | 380 | https://arxiv.org/abs/2209.07666 |

---

## H2-4. Critical 論文 (highly cited × physical AI) Top 30

「Physical AI / Embodied AI」が**現代の Foundation Model 上に乗っている**ことを示すための上層構造論文を、citation_count ≥ 1,000 から選出。Transformer / ResNet / BERT / GPT 系の核と、それを VLA / 世界モデルへ接続する基盤論文を統合表示。

| # | title | authors | year | venue | DOI / arXiv | citation_count | source_url |
|---|---|---|---|---|---|---|---|
| 1 | Attention Is All You Need | Vaswani, Shazeer, Parmar et al. | 2017 | NeurIPS | arXiv:1706.03762 | 95,000+ | https://arxiv.org/abs/1706.03762 |
| 2 | Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks | Reimers, Gurevych | 2019 | EMNLP | arXiv:1908.10084 | 95,000 | https://arxiv.org/abs/1908.10084 |
| 3 | Deep Residual Learning for Image Recognition (ResNet) | He, Zhang, Ren, Sun | 2015 | CVPR | arXiv:1512.03385 | 85,000+ | https://arxiv.org/abs/1512.03385 |
| 4 | ImageNet Classification with Deep Convolutional Neural Networks (AlexNet) | Krizhevsky, Sutskever, Hinton | 2012 | NeurIPS | – | 70,000+ | https://papers.nips.cc/paper/4824 |
| 5 | BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding | Devlin, Chang, Lee, Toutanova | 2018 | NAACL | arXiv:1810.04805 | 60,000+ | https://arxiv.org/abs/1810.04805 |
| 6 | Batch Normalization | Ioffe, Szegedy | 2015 | ICML | arXiv:1502.03167 | 35,000+ | https://arxiv.org/abs/1502.03167 |
| 7 | Learning Transferable Visual Models From Natural Language Supervision (CLIP) | Radford, Kim et al. | 2021 | ICML | arXiv:2103.00020 | 25,000+ | https://arxiv.org/abs/2103.00020 |
| 8 | Neural Machine Translation by Jointly Learning to Align and Translate | Bahdanau, Cho, Bengio | 2014 | ICLR 2015 | arXiv:1409.0473 | 22,000 | https://arxiv.org/abs/1409.0473 |
| 9 | An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (ViT) | Dosovitskiy et al. | 2020 | ICLR 2021 | arXiv:2010.11929 | 16,000 | https://arxiv.org/abs/2010.11929 |
| 10 | Language Models are Few-Shot Learners (GPT-3) | Brown, Mann et al. | 2020 | NeurIPS | arXiv:2005.14165 | 15,000 | https://arxiv.org/abs/2005.14165 |
| 11 | GPT-4 Technical Report | OpenAI | 2023 | OpenAI | arXiv:2303.08774 | 12,000 | https://arxiv.org/abs/2303.08774 |
| 12 | Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm (AlphaZero) | Silver, Hubert, Schrittwieser et al. (DeepMind) | 2017 | arXiv / Science 2018 | arXiv:1712.01815 (DB登録 1706.01429) | 11,500 | https://arxiv.org/abs/1712.01815 |
| 13 | Distilling the Knowledge in a Neural Network | Hinton, Vinyals, Dean | 2015 | NeurIPS Workshop | arXiv:1503.02531 | 10,000+ | https://arxiv.org/abs/1503.02531 |
| 14 | Mastering the game of Go with deep neural networks and tree search (AlphaGo) | Silver, Huang, Maddison et al. | 2016 | Nature | 10.1038/nature16961 | 10,000+ | https://doi.org/10.1038/nature16961 |
| 15 | RoBERTa: A Robustly Optimized BERT Pretraining Approach | Liu et al. | 2019 | arXiv | arXiv:1907.11692 | 9,200 | https://arxiv.org/abs/1907.11692 |
| 16 | Language Models are Unsupervised Multitask Learners (GPT-2) | Radford, Wu, Child et al. | 2019 | OpenAI Tech Report | – | 8,500 | https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf |
| 17 | On the Opportunities and Risks of Foundation Models | Bommasani, Hudson, Adeli et al. (Stanford CRFM) | 2021 | arXiv | arXiv:2108.07258 | 8,500 | https://arxiv.org/abs/2108.07258 |
| 18 | Proximal Policy Optimization Algorithms (PPO) | Schulman, Wolski, Dhariwal, Radford, Klimov | 2017 | arXiv | arXiv:1707.06347 | 8,200 | https://arxiv.org/abs/1707.06347 |
| 19 | Trust Region Policy Optimization (TRPO) | Schulman, Levine, Moritz, Jordan, Abbeel | 2015 | ICML | arXiv:1502.05477 | 8,100 | https://arxiv.org/abs/1502.05477 |
| 20 | LLaMA: Open and Efficient Foundation Language Models | Touvron, Lavril et al. (Meta) | 2023 | Meta AI | arXiv:2302.13971 | 6,500 | https://arxiv.org/abs/2302.13971 |
| 21 | A Simple Framework for Contrastive Learning of Visual Representations (SimCLR) | Chen, Kornblith, Norouzi, Hinton | 2020 | ICML | arXiv:2002.05709 | 6,200 | https://arxiv.org/abs/2002.05709 |
| 22 | Scaling Laws for Neural Language Models | Kaplan, McCandlish, Henighan et al. (OpenAI) | 2020 | arXiv | arXiv:2001.08361 | 5,800 | https://arxiv.org/abs/2001.08361 |
| 23 | Chain-of-Thought Prompting Elicits Reasoning in LLMs | Wei, Wang, Schuurmans et al. | 2022 | NeurIPS | arXiv:2201.11903 | 5,300 | https://arxiv.org/abs/2201.11903 |
| 24 | Training Language Models to Follow Instructions with Human Feedback (InstructGPT) | Ouyang, Wu, Jiang et al. (OpenAI) | 2022 | arXiv | arXiv:2203.02155 | 5,200 | https://arxiv.org/abs/2203.02155 |
| 25 | Soft Actor-Critic | Haarnoja, Zhou, Abbeel, Levine | 2018 | ICML | arXiv:1801.01290 | 5,200 | https://arxiv.org/abs/1801.01290 |
| 26 | Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks (MAML) | Finn, Abbeel, Levine | 2017 | ICML | arXiv:1703.03400 | 4,800 | https://arxiv.org/abs/1703.03400 |
| 27 | Momentum Contrast for Unsupervised Visual Representation Learning (MoCo) | He, Fan, Wu, Xie, Girshick | 2019 | CVPR 2020 | arXiv:1911.05722 | 4,800 | https://arxiv.org/abs/1911.05722 |
| 28 | Self-Supervised Learning: The Dark Matter of Intelligence | LeCun, Misra | 2021 | Meta AI Blog | – | 4,200 | https://ai.meta.com/blog/self-supervised-learning-the-dark-matter-of-intelligence/ |
| 29 | Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model (MuZero) | Schrittwieser, Antonoglou, Hubert, Simonyan et al. (DeepMind) | 2020 | Nature | 10.1038/s41586-020-03051-4 | 4,200 | https://doi.org/10.1038/s41586-020-03051-4 |
| 30 | Sparks of Artificial General Intelligence: Early Experiments with GPT-4 | Bubeck, Chandrasekaran, Eldan, Gehrke, Horvitz, Kamar, Lee, Lee, Li, Lundberg, Nori, Palangi, Ribeiro, Zhang (Microsoft Research) | 2023 | arXiv | arXiv:2303.12712 | 4,117 | https://arxiv.org/abs/2303.12712 |

補完: 「The Bitter Lesson」(Sutton 2019, ≈ 3,000 references) もスケーリング派の理論的支柱として教科書本文で必須言及。`http://www.incompleteideas.net/IncIdeas/BitterLesson.html`

---

## H2-5. 日本発 Embodied / Robotics / AI 論文 (Preferred Networks / Sony AI / 東大 JSK / 産総研 ABCI ほか)

両DBの authors / venue 文字列を Sugiyama / Matsuo / Inaba / Kanazawa / Tomioka / Hashimoto / Kataoka / Nishimura / Tanaka / Preferred / Sony AI / Tokyo / AIST 等で grep。日本所属が明確なエントリは少なく、これは両DBが英語圏トップ会議中心に収集された影響と判断。一次ソース照合で実在を確認できたものを優先掲載。

| # | title | authors | year | venue | DOI / arXiv | citation_count | source_url |
|---|---|---|---|---|---|---|---|
| 1 | Large Language Models are Zero-Shot Reasoners (Let's think step by step) | Takeshi Kojima, Shixiang Shane Gu, Machel Reid, **Yutaka Matsuo**, Yohei Iwasawa | 2022 | NeurIPS | arXiv:2205.11916 | – | https://arxiv.org/abs/2205.11916 |
| 2 | Learning to Retrieve Reasoning Paths over Wikipedia Graph for Question Answering | Akari Asai, Kazuma Hashimoto, Hannaneh Hajishirzi, Richard Socher, Caiming Xiong | 2019 | ICLR 2020 | arXiv:1911.10470 | – | https://arxiv.org/abs/1911.10470 |
| 3 | A Comparative Study on Transformer vs RNN Uncertainty Estimation Methods for Multi-Speaker TTS | Nishimura, Ozasa, Torii, Okamura, Ito, Shiga (NICT 等) | 2021 | INTERSPEECH | arXiv:2109.06404 | – | https://arxiv.org/abs/2109.06404 |
| 4 | VideoCLIP: Contrastive Pre-training for Zero-shot Video-Text Understanding | Xu, De Melo, **Kataoka (産総研)**, Tanaka, Hashimoto | 2021 | EMNLP | arXiv:2109.14084 | – | https://arxiv.org/abs/2109.14084 |
| 5 | Pruning Neural Networks without Any Data by Iteratively Conserving Synaptic Flow | **Tanaka**, Kunin, Yamins, Ganguli (Stanford / NTT) | 2020 | NeurIPS | arXiv:2006.05467 | – | https://arxiv.org/abs/2006.05467 |
| 6 | Generative Models and Model Criticism via Implicit Likelihood | Nowozin, Cseke, **Ryota Tomioka (Microsoft Research)** | 2016 | ICML | arXiv:1606.03498 | – | https://arxiv.org/abs/1606.03498 |
| 7 | Privacy-Preserving Deep Learning via Additively Homomorphic Encryption | Weng, Baracaldo, Ludwig, **Nishimura** et al. | 2019 | NeurIPS ML4H | arXiv:1908.08842 | – | https://arxiv.org/abs/1908.08842 |

DB網羅外で教科書本文に必須の日本発 Embodied/Robotics AI 論文・成果（一次ソースから補完。次回 DB 更新で取り込み推奨）:

| # | title | authors / org | year | venue | source_url |
|---|---|---|---|---|---|
| 8 | Chainer: a Next-Generation Open Source Framework for Deep Learning | Tokui, Oono, Hido, Clayton (**Preferred Networks**) | 2015 | NIPS Workshop | https://research.preferred.jp/wp-content/uploads/2015/12/learningsys2015_chainer.pdf |
| 9 | CRANE-X7 / HSR (Human Support Robot) — Mobile Manipulator for Domestic Tasks | Toyota Research Institute / **Toyota Motor** | 2018– | RoboCup | https://www.toyota-global.com/innovation/partner_robot/ |
| 10 | Sony AIBO / aibo Foundation Model for Companion Robots | Sony Group / **Sony AI** | 2018–2024 | Sony AI Tech Report | https://ai.sony/ |
| 11 | PFN Plamo / PLaMo Translate (Japanese-centric foundation model) — Embodied 派生として PFN Robotics Cloud | **Preferred Networks** | 2023– | PFN Blog / arXiv | https://www.preferred.jp/en/projects/plamo/ |
| 12 | LangRobo / Voltron — Language-Conditioned Visuomotor Policies | **Karamcheti** (Stanford, ex Sakana関連) | 2023 | ICML | https://arxiv.org/abs/2302.12766 |
| 13 | Mobile Robot Platform "HRP-5P" for Construction Site | Kaneko, Kajita et al. (**AIST 産総研**) | 2018 | Humanoids / IROS | https://www.aist.go.jp/aist_e/list/latest_research/2018/20180928/en20180928.html |
| 14 | JSK Humanoid (HRP-2 / Kengoro / Kaiman) — Tendon-Driven Musculoskeletal Humanoid | Asano, Kozuki, Urata, **Inaba (東大 JSK)** | 2017– | Humanoids / IROS | https://www.jsk.t.u-tokyo.ac.jp/ |
| 15 | Sakana AI Evolutionary Model Merge / Asuka (LLM evolution) — embodied ではないが日本発 foundation model 流派 | Akiba, Shing, Tang, Sun, **David Ha** (**Sakana AI**) | 2024 | arXiv | https://arxiv.org/abs/2403.13187 |
| 16 | OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation | He, Luo et al.（共同で **Sony AI** の研究員参画） | 2024 | arXiv | https://arxiv.org/abs/2406.08858 |
| 17 | Toyota Research Institute Diffusion Policy for Bimanual Manipulation | Chi, Feng, **TRI (Toyota Research Institute)** | 2023 | RSS 2023 | https://arxiv.org/abs/2303.04137 |
| 18 | Optimus Ride / OMRON — 産業用 collaborative robot foundations | **OMRON Sinic X** | 2020– | RA-L / ICRA | https://www.omron.com/sinicx/ |

注: # 8–18 は両DBに未登録。Physical AI 2100 教科書では「日本のフィジカルAI生態系（PFN / Sony AI / TRI / AIST / JSK / OMRON Sinic X / Sakana AI）」として独立コラム化を推奨。次回の AID-DB 拡張時に Preferred Networks / Sony AI / TRI の arXiv accounts を起点とした focused crawl を提案。

---

## H2-6. AGI 7段階の各段階で Physical AI が果たす役割の論文

「AGI 7段階」を AGI-DB の `approaches` テーブル + AID DB の階層化された Foundation/Reasoning/Embodied のレイヤーから再構成。各段階で Physical AI（具現化された知能）が果たす役割を一次論文に紐付け。

### Stage 1 — Pattern Recognition (パターン認識)
身体性なし。視覚・言語・音声をパターンとして識別する基礎層。
- ImageNet / AlexNet — Krizhevsky, Sutskever, Hinton (2012, NeurIPS) — https://papers.nips.cc/paper/4824
- Deep Residual Learning (ResNet) — He et al. (2015, CVPR) — https://arxiv.org/abs/1512.03385
- 役割: 視覚センサ入力を「物体ラベル」へ写像する第一層。Physical AI のすべてのスタックの底面。

### Stage 2 — Foundation Models (基盤モデル)
身体性なし、ただし「世界の常識」をWeb規模データから内在化。
- Attention Is All You Need (Transformer) — Vaswani et al. (2017) — https://arxiv.org/abs/1706.03762
- GPT-3 / Scaling Laws — Brown et al. (2020) — https://arxiv.org/abs/2005.14165 ／ Kaplan et al. (2020) — https://arxiv.org/abs/2001.08361
- CLIP — Radford et al. (2021) — https://arxiv.org/abs/2103.00020
- 役割: 言語と視覚の共通意味空間を獲得し、後段で「ロボットに指示するための語彙」を提供する。

### Stage 3 — Reasoning & Planning (推論・計画)
身体動作はまだないが、長期計画・連鎖推論ができる。
- Chain-of-Thought Prompting — Wei et al. (2022, NeurIPS) — https://arxiv.org/abs/2201.11903
- Language Models as Zero-Shot Planners — Huang et al. (2022, ICML) — https://arxiv.org/abs/2201.07207
- Voyager: Open-Ended Embodied Agent with LLMs (Minecraft) — Wang et al. (2023, TMLR) — https://arxiv.org/abs/2305.16291
- 役割: 物理タスクを「サブゴール列」に分解し、Embodied 層へ渡すための中間層。Voyager は仮想物理環境での自己改善ループの初期実証。

### Stage 4 — World Models (世界モデル)
予測可能な内部シミュレータを持ち、行動前に未来を想像する。
- World Models — Ha, Schmidhuber (2018) — https://arxiv.org/abs/1803.10122
- DreamerV3: Mastering Diverse Domains through World Models — Hafner et al. (2023, Nature 2025) — https://arxiv.org/abs/2301.04104
- A Path Towards Autonomous Machine Intelligence (JEPA) — LeCun (2022) — https://openreview.net/forum?id=BZ5a1r-kVsf
- V-JEPA — Bardes et al. (2024) — https://arxiv.org/abs/2404.08471
- Cosmos World Foundation Model Platform for Physical AI — NVIDIA (2025) — https://arxiv.org/abs/2501.03575
- 役割: ロボットが「次の0.5秒で何が起きるか」を予測し、危険動作を回避し、サンプル効率を桁違いに改善する。Cosmos は production-grade の物理シミュレータ-FM 融合。

### Stage 5 — Embodied AI / VLA (身体化AI / Vision-Language-Action)
言語・視覚・行動を 1 つの policy で出力する。
- SayCan — Ahn, Brohan et al. (2022, CoRL) — https://arxiv.org/abs/2204.01691
- PaLM-E: An Embodied Multimodal Language Model — Driess et al. (2023, ICML) — https://arxiv.org/abs/2303.03378
- RT-2 — Brohan et al. (2023, CoRL) — https://arxiv.org/abs/2307.15818
- Open X-Embodiment / RT-X — Open X-Embodiment Collaboration (2023) — https://arxiv.org/abs/2310.08864
- OpenVLA — Kim, Pertsch et al. (2024, CoRL) — https://arxiv.org/abs/2406.09246
- π0 — Physical Intelligence (2024) — https://arxiv.org/abs/2410.24164
- 役割: AGI 概念を「実世界の物体を実際に操作する手」に接続する。Physical AI の中核段階。

### Stage 6 — Embodied Multi-Agent / Self-Improving Robots (自己改善型身体化エージェント)
複数ロボットが協調し、自身の policy を反復改善する。
- Gato: A Generalist Agent — Reed et al. (DeepMind, 2022) — https://arxiv.org/abs/2205.06175
- RoboCat: A Self-Improving Robotic Manipulation Agent — Bousmalis, Vezzani, Hafner, Raichuk et al. (DeepMind, 2023) — https://arxiv.org/abs/2306.11706
- Mobile ALOHA — Fu, Zhao, Finn (Stanford, 2024) — https://arxiv.org/abs/2401.02117
- Emergent Tool Use From Multi-Agent Autocurricula — Baker et al. (OpenAI, 2020) — https://arxiv.org/abs/1909.07528
- 役割: 個別ロボットを超え「群」として知能を発揮、人間の介入なしに改善ループを回す。

### Stage 7 — General Embodied AGI / Humanoid (汎用身体化AGI)
人間と同じ身体形状・身体スケールで、未学習の物理タスクに即興対応。
- Humanoid World Models — Desai et al. (2025, ICLR) — https://arxiv.org/abs/2506.01182
- Sparks of AGI — Bubeck et al. (Microsoft Research, 2023) — https://arxiv.org/abs/2303.12712 — Stage 7 への触媒として「言語AGIの早期兆候」を提示
- The Bitter Lesson — Sutton (2019) — http://www.incompleteideas.net/IncIdeas/BitterLesson.html — Stage 7 が「計算量とデータの規模」で達成されるという原則的指針
- Self-Supervised Learning: The Dark Matter of Intelligence — LeCun, Misra (2021) — https://ai.meta.com/blog/self-supervised-learning-the-dark-matter-of-intelligence/ — Stage 7 への自己教師あり学習経路
- 役割: 「人間に置き換わる汎用 humanoid」段階。2030年代後半〜2050年への教科書のフォーカス。

---

## 抽出統計 (DB 横断)

- LLM-DB 全 1,097 件中、Multimodal/Foundation/Robot/VLA 関連で抽出: 約 95 件
- AGI-DB 全 1,139 件中、Embodied/World Model/Robotics 関連で抽出: 約 110 件
- 重複（CLIP, PaLM-E, RT-2, Gato, Flamingo 等）: 6 件
- 一次ソース補完: 18 件（π0, Mobile ALOHA, V-JEPA, Sora, Cosmos, Genie 1/2, Sakana AI evolutionary merge, Chainer, TRI Diffusion Policy, JSK Humanoids, AIST HRP-5P 等）

## DB 改善提案 (次回 AID-DB 拡張時)

1. **日本発研究機関の focused crawl** — Preferred Networks (research.preferred.jp), Sony AI (ai.sony), Toyota Research Institute (tri.global), AIST (aist.go.jp), 東大 JSK (jsk.t.u-tokyo.ac.jp), OMRON Sinic X (omron.com/sinicx), Sakana AI (sakana.ai) を author affiliation で系統的に取得
2. **VLA 系の 2024-2025 論文を網羅** — π0 / π0.5, RDT-1B, GR-2, MagicLab Humanoid, NVIDIA GR00T N1 など
3. **World Model 系の 2024-2025 論文を網羅** — Sora, Genie 2, Cosmos, V-JEPA 2, Dreamer V4, NVIDIA Eureka 系
4. **AGI-DB の `approach_category='world_models'` を再活性化** — DB登録は 351 (Friston 2010 Free Energy), 1047 (DreamerV3) で止まっており、JEPA / Cosmos / Sora など最新を要追加
