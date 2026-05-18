# FTT-DB v2.0 - Physical AI 2100 Evidence Extraction

**抽出元**: FTT-DB v2.0 + /ddb 深化版 (2026-05-16 時点)
- academic_papers 41,070 / paper_citations 125,748 / milestones 304 / genealogy 220 edges / forecast 213 / TRL 169
- 全レコード OpenAlex API 由来 (実在率 100% / source_url 100%)

**抽出対象 (Physical AI 直結 10 領域)**:

| FTT-DB code | name | Physical AI mapping | papers (in top set) |
|---|---|---|---:|
| EDGE_AI | Edge AI (エッジAI) | EDGE_AI | 5818 |
| NEUROMORPHIC | Neuromorphic Computing (ニューロモーフィック) | NEUROMORPHIC | 1022 |
| SAFETY_AI | AI Safety & Interpretability (AI安全・解釈可能性) | SAFETY_AI | 6408 |
| CYBER_PHYS | Cyber-Physical Systems (サイバーフィジカルシステム) | ROBOTICS_HARDWARE / MOTION_PLANNING / CLASSICAL_CONTROL | 893 |
| BRAIN_CI | Brain-Computer Interfaces (脳-機械インタフェース) | VLM_FOUNDATION (sensor side) / BRAIN-MACHINE | 4079 |
| TRANSPORT | Transportation (輸送) | ROBOTICS_HARDWARE / MOTION_PLANNING / RL | 1189 |
| MEDICAL | Medical/Neuro Engineering (医療・神経工学) | ROBOTICS_HARDWARE (surgical) / SAFETY_AI | 6695 |
| BUILDING | Construction/Urban (建築・都市) | CYBER_PHYS / SIM_DATA | 880 |
| CROSS | Cross-domain (横断観察) | VLM_FOUNDATION / SIM_DATA | 4870 |
| PHOTONICS | Photonics (フォトニクス) | SENSING (LiDAR / vision frontend) | 859 |

**SSoT パス**:
- DB: `~/projects/research/future-tech-trends-db/v2/data/ftt_v2.db` (204 MB)
- SSoT HTML: `~/projects/apps/miratuku-news-v2/dashboards/ftt-v2-genealogy.html`
- SSoT JSON: `~/projects/apps/miratuku-news-v2/dashboards/ftt_v2_ssot.json`
- 公開URL: https://yuyanishimura0312.github.io/miratuku-news-v2/dashboards/ftt-v2-genealogy.html

---

## EDGE_AI - Edge AI (エッジAI)

**Physical AI mapping**: EDGE_AI

### Top 20 Cited Papers (citation_count desc)

| # | Year | Title | First Authors | Venue | DOI | Citations | Countries | JP authors? | source_url |
|---:|---:|---|---|---|---|---:|---|:---:|---|
| 1 | 2017 | ImageNet classification with deep convolutional neural networks | Alex Krizhevsky; Ilya Sutskever; Geoffrey E. Hinton | Communications of the ACM | [10.1145/3065386](https://doi.org/10.1145/3065386) | 75673 | CA,US |  | [link](https://openalex.org/W2163605009) |
| 2 | 2020 | SciPy 1.0: fundamental algorithms for scientific computing in Python | Pauli Virtanen; Ralf Gommers; Travis E. Oliphant; Matt Haberland; Tyler Reddy | Nature Methods | [10.1038/s41592-019-0686-2](https://doi.org/10.1038/s41592-019-0686-2) | 36914 | FI,US,RU,EE,GB,AU,CZ,BR,CA |  | [link](https://openalex.org/W3003257820) |
| 3 | 2010 | Features and development of <i>Coot</i> | Paul Emsley; Bernhard Lohkamp; W. G. Scott; Kevin Cowtan | Acta Crystallographica Section D Biological Crystallography | [10.1107/s0907444910007493](https://doi.org/10.1107/s0907444910007493) | 29329 | GB,SE,US |  | [link](https://openalex.org/W2124026197) |
| 4 | 2009 | QUANTUM ESPRESSO: a modular and open-source software project for quantum simulations of materials | Paolo Giannozzi; Stefano Baroni; Nicola Bonini; Matteo Calandra; Roberto Car | Journal of Physics Condensed Matter | [10.1088/0953-8984/21/39/395502](https://doi.org/10.1088/0953-8984/21/39/395502) | 28600 | IT,US,FR,DE,SI,CH |  | [link](https://openalex.org/W2120145199) |
| 5 | 2008 | The qualitative content analysis process | Satu Elo; Helvi Kyngäs | Journal of Advanced Nursing | [10.1111/j.1365-2648.2007.04569.x](https://doi.org/10.1111/j.1365-2648.2007.04569.x) | 21984 | FI |  | [link](https://openalex.org/W2067404301) |
| 6 | 2020 | Array programming with NumPy | Charles R. Harris; K. Jarrod Millman; Stéfan J. van der Walt; Ralf Gommers; Pauli Virtanen | Nature | [10.1038/s41586-020-2649-2](https://doi.org/10.1038/s41586-020-2649-2) | 21548 | US,ZA,FI,GB,DE,CA,CH,EE,FR |  | [link](https://openalex.org/W3035965352) |
| 7 | 2015 | Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks | Shaoqing Ren; Kaiming He; Ross Girshick; Jian Sun | arXiv (Cornell University) | [10.48550/arxiv.1506.01497](https://doi.org/10.48550/arxiv.1506.01497) | 18238 | GB |  | [link](https://openalex.org/W2613718673) |
| 8 | 2009 | The MIQE Guidelines: Minimum Information for Publication of Quantitative Real-Time PCR Experiments | Stephen A. Bustin; Vladimı́r Beneš; Jeremy A. Garson; Jan Hellemans; Jim F. Huggett | Clinical Chemistry | [10.1373/clinchem.2008.112797](https://doi.org/10.1373/clinchem.2008.112797) | 15920 | GB,BE,SE,CZ,US |  | [link](https://openalex.org/W2168420558) |
| 9 | 2018 | Sarcopenia: revised European consensus on definition and diagnosis | Alfonso J. Cruz‐Jentoft; Gülistan Bahat; Jürgen M. Bauer; Yves Boirie‌; Olivier Bruyère | Age and Ageing | [10.1093/ageing/afy169](https://doi.org/10.1093/ageing/afy169) | 13664 | ES,TR,DE,FR,BE,SE,GB,IT,CZ,NL,LU,AU,CH,FI |  | [link](https://openalex.org/W2897513125) |
| 10 | 2013 | 2013 ESH/ESC Guidelines for the management of arterial hypertension | Giuseppe Mancia; Robert Fagard; Krzysztof Narkiewicz; Josep Redón; Alberto Zanchetti | European Heart Journal | [10.1093/eurheartj/eht151](https://doi.org/10.1093/eurheartj/eht151) | 13664 | IT,BE |  | [link](https://openalex.org/W2133416234) |
| 11 | 2015 | Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015: elaboration and explanation | Larissa Shamseer; David Moher; Mike Clarke; Davina Ghersi; A. Liberati | BMJ | [10.1136/bmj.g7647](https://doi.org/10.1136/bmj.g7647) | 13053 | CA,IE,AU,IT,GB |  | [link](https://openalex.org/W2169205464) |
| 12 | 2021 | 2021 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure | Theresa A. McDonagh; Marco Metra; Marianna Adamo; Roy S. Gardner; Andreas Baumbach | European Heart Journal | [10.1093/eurheartj/ehab368](https://doi.org/10.1093/eurheartj/ehab368) | 12628 |  |  | [link](https://openalex.org/W3193598686) |
| 13 | 2019 | A survey on Image Data Augmentation for Deep Learning | Connor Shorten; Taghi M. Khoshgoftaar | Journal Of Big Data | [10.1186/s40537-019-0197-0](https://doi.org/10.1186/s40537-019-0197-0) | 12135 | US |  | [link](https://openalex.org/W2954996726) |
| 14 | 2021 | PRISMA 2020 explanation and elaboration: updated guidance and exemplars for reporting systematic reviews | Matthew J. Page; David Moher; Patrick M. Bossuyt; Isabelle Boutron; Tammy Hoffmann | BMJ | [10.1136/bmj.n160](https://doi.org/10.1136/bmj.n160) | 10617 | AU,CA,NL,FR,US,SG,CN,LB,GB,DK |  | [link](https://openalex.org/W3123893780) |
| 15 | 2012 | 3D Slicer as an image computing platform for the Quantitative Imaging Network | Andriy Fedorov; Reinhard Beichel; Jayashree Kalpathy–Cramer; Julien Finet; Jean‐Christophe Fillion‐Robin | Magnetic Resonance Imaging | [10.1016/j.mri.2012.05.001](https://doi.org/10.1016/j.mri.2012.05.001) | 8696 | US |  | [link](https://openalex.org/W2026616100) |
| 16 | 2019 | Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI | Alejandro Barredo Arrieta; Natalia Díaz-Rodríguez; Javier Del Ser; Adrien Bennetot; Siham Tabik | Information Fusion | [10.1016/j.inffus.2019.12.012](https://doi.org/10.1016/j.inffus.2019.12.012) | 8663 | ES,FR |  | [link](https://openalex.org/W2981731882) |
| 17 | 2015 | Effective Approaches to Attention-based Neural Machine Translation | Thang Luong; Hieu Pham; Christopher D. Manning |  | [10.18653/v1/d15-1166](https://doi.org/10.18653/v1/d15-1166) | 8561 | US |  | [link](https://openalex.org/W1902237438) |
| 18 | 2015 | Internet of Things: A Survey on Enabling Technologies, Protocols, and Applications | Ala Al‐Fuqaha; Mohsen Guizani; Mehdi Mohammadi; Mohammed Aledhari; Moussa Ayyash | IEEE Communications Surveys & Tutorials | [10.1109/comst.2015.2444095](https://doi.org/10.1109/comst.2015.2444095) | 8232 | US,QA |  | [link](https://openalex.org/W2134295053) |
| 19 | 2006 | Folding DNA to create nanoscale shapes and patterns | Paul W. K. Rothemund | Nature | [10.1038/nature04586](https://doi.org/10.1038/nature04586) | 7388 | US |  | [link](https://openalex.org/W2126961173) |
| 20 | 2013 | SPIRIT 2013 explanation and elaboration: guidance for protocols of clinical trials | A.-W. Chan; Jennifer Tetzlaff; Peter C Gøtzsche; Douglas G. Altman; H Mann | BMJ | [10.1136/bmj.e7586](https://doi.org/10.1136/bmj.e7586) | 7008 | CA,DK,GB,US |  | [link](https://openalex.org/W2171811563) |

### Milestones (academic evidence, n=10)

| Year | Tech | Type | Description | Evidence | Confidence | Status | DOI | source_url |
|---:|---|---|---|---|---:|---|---|---|
| 2019 | federated learning | proposal | federated-learning framework first proposed by Google in 2016, we introduce a comprehensive secure fede | academic_paper | 0.75 | observed | [10.1145/3298981](https://doi.org/10.1145/3298981) | [link](https://openalex.org/W2912213068) |
| 2019 | federated learning | proposal | Heterogeneous Resources in Mobile Edge We envision a mobile edge computing (MEC) framework for machine learning (ML) technologies, which lev | academic_paper_high_citation | 0.90 | observed | [10.1109/icc.2019.8761315](https://doi.org/10.1109/icc.2019.8761315) | [link](https://openalex.org/W2798720628) |
| 2020 | federated learning | mass_deployment | e transition from research to clinical practice. This paper considers key factors contributing to this issu | academic_paper | 0.75 | observed | [10.1038/s41746-020-00323-1](https://doi.org/10.1038/s41746-020-00323-1) | [link](https://openalex.org/W3012501605) |
| 2020 | federated learning | proposal | hip challenges. Federated learning is a novel paradigm for data-private multi-institutional collaborations, where model-learning leverages | academic_paper_high_citation | 0.90 | observed | [10.1038/s41598-020-69250-1](https://doi.org/10.1038/s41598-020-69250-1) | [link](https://openalex.org/W3045674654) |
| 2020 | federated learning | mass_deployment | the 5G communication networks are being widely deployed worldwide, both industry and academia have started to move beyond 5G and explor | academic_paper_mid_citation | 0.66 | observed | [10.23919/jcc.2020.09.009](https://doi.org/10.23919/jcc.2020.09.009) | [link](https://openalex.org/W3033403733) |
| 2020 | federated learning | mass_deployment | , machine learning techniques have been widely used to learn from data, identify patterns, and make automated decisions. Machine le | academic_paper_mid_citation | 0.62 | observed | [10.1109/jiot.2020.2991416](https://doi.org/10.1109/jiot.2020.2991416) | [link](https://openalex.org/W3023244064) |
| 2021 | federated learning | proposal | lying FL to wireless communications are first described. Then potential FL applications in wireless communications are detailed. The ma | academic_paper_mid_citation | 0.63 | observed | [10.1016/j.eng.2021.12.002](https://doi.org/10.1016/j.eng.2021.12.002) | [link](https://openalex.org/W3119680904) |
| 2022 | federated learning | proposal | y ideas, challenges, opportunities, and envision promising future trajectories of research toward a new PFL architectural design, realistic  | academic_paper_high_citation | 0.80 | observed | [10.1109/tnnls.2022.3160699](https://doi.org/10.1109/tnnls.2022.3160699) | [link](https://openalex.org/W3133814152) |
| 2022 | TinyML | prototype | vity Monitoring This article proposes a proof-of-concept device to continuously assess the usage of handheld power tools and detect cons | academic_paper_mid_citation | 0.50 | observed | [10.1109/tim.2022.3165816](https://doi.org/10.1109/tim.2022.3165816) | [link](https://openalex.org/W4225705568) |
| 2023 | TinyML | prototype | ora of research areas and has demonstrated its capability to bring new approaches and solutions to var | academic_paper | 0.75 | observed | [10.1109/access.2023.3294111](https://doi.org/10.1109/access.2023.3294111) | [link](https://openalex.org/W4383751021) |

### Forecasts 2027-2100 (extracted from papers, n=6)

| Extracted Year | Tech | Evidence Phrase | Method | Confidence | Paper Year | DOI | source_url |
|---:|---|---|---|---:|---:|---|---|
| 2030 | federated learning | rapidly becoming an integral part of the modern society. By 2030, there is estimated to be over 40 billion active and connec | regex_abstract_S3 | 0.70 | 2025 | [10.1109/aiiot65859.2025.11105231](https://doi.org/10.1109/aiiot65859.2025.11105231) | [link](https://openalex.org/W4413180150) |
| 2030 | federated learning | rapidly becoming an integral part of the modern society. By 2030, there is estimated to be over 40 billion active and connec | regex_abstract_S3 | 0.70 | 2025 | [10.1109/aiiot65859.2025.11105231](https://doi.org/10.1109/aiiot65859.2025.11105231) | [link](https://openalex.org/W4413180150) |
| 2030 | TinyML | year (and a forecast to reach more than 200 billion USD by 2030), TinyML will be one of the main forces to embrace the new | regex_abstract_S3 | 0.70 | 2024 | [10.1109/tce.2024.3482353](https://doi.org/10.1109/tce.2024.3482353) | [link](https://openalex.org/W4406046871) |
| 2030 | TinyML | rapidly becoming an integral part of the modern society. By 2030, there is estimated to be over 40 billion active and connec | regex_abstract_S3 | 0.70 | 2025 | [10.1109/aiiot65859.2025.11105231](https://doi.org/10.1109/aiiot65859.2025.11105231) | [link](https://openalex.org/W4413180150) |
| 2030 | TinyML | rapidly becoming an integral part of the modern society. By 2030, there is estimated to be over 40 billion active and connec | regex_abstract_S3 | 0.70 | 2025 | [10.1109/aiiot65859.2025.11105231](https://doi.org/10.1109/aiiot65859.2025.11105231) | [link](https://openalex.org/W4413180150) |
| 2050 | TinyML | tunities and generates the majority of the world’s food. In 2050, agricultural products will be in exceptionally high demand | regex_abstract_S3 | 0.70 | 2022 | [10.1145/3575879.3575994](https://doi.org/10.1145/3575879.3575994) | [link](https://openalex.org/W4361746014) |

### TRL Trajectory (NASA TRL 1-9, n=4)

| Year | Tech | TRL | Evidence | Confidence | DOI | source_url |
|---:|---|---:|---|---:|---|---|
| 2024 | TinyML | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | edge AI inference | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | federated learning | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | on-device machine learning | 7 | current_status='early_deployment' | 0.80 |  |  |

---

## NEUROMORPHIC - Neuromorphic Computing (ニューロモーフィック)

**Physical AI mapping**: NEUROMORPHIC

### Top 20 Cited Papers (citation_count desc)

| # | Year | Title | First Authors | Venue | DOI | Citations | Countries | JP authors? | source_url |
|---:|---:|---|---|---|---|---:|---|:---:|---|
| 1 | 2018 | Loihi: A Neuromorphic Manycore Processor with On-Chip Learning | Mike Davies; Narayan Srinivasa; Tsung-Han Lin; Gautham N. Chinya; Yongqiang Cao | IEEE Micro | [10.1109/mm.2018.112130359](https://doi.org/10.1109/mm.2018.112130359) | 3641 | US |  | [link](https://openalex.org/W2783525259) |
| 2 | 2015 | Training and operation of an integrated neuromorphic network based on metal-oxide memristors | M. Prezioso; Farshad Merrikh‐Bayat; Brian D. Hoskins; Gina C. Adam; Konstantin K. Likharev | Nature | [10.1038/nature14441](https://doi.org/10.1038/nature14441) | 2914 | US |  | [link](https://openalex.org/W1542981317) |
| 3 | 2016 | Memristors with diffusive dynamics as synaptic emulators for neuromorphic computing | Zhongrui Wang; Saumil Joshi; Sergey Savel’ev; Hao Jiang; Rivu Midya | Nature Materials | [10.1038/nmat4756](https://doi.org/10.1038/nmat4756) | 2275 | US,GB |  | [link](https://openalex.org/W2526646482) |
| 4 | 2016 | Memristors with diffusive dynamics as synaptic emulators for neuromorphic computing | Zhongrui Wang; Saumil Joshi; Sergey Savel’ev; Hao Jiang; Rivu Midya | Nature Materials | [10.1038/nmat4756](https://doi.org/10.1038/nmat4756) | 2275 | US,GB |  | [link](https://openalex.org/W2526646482) |
| 5 | 2020 | Event-Based Vision: A Survey | Guillermo Gallego; Tobi Delbruck; Garrick Orchard; Chiara Bartolozzi; Brian Taba | IEEE Transactions on Pattern Analysis and Machine Intelligen | [10.1109/tpami.2020.3008413](https://doi.org/10.1109/tpami.2020.3008413) | 1975 | DE,CH,US,IT,GB,SE |  | [link](https://openalex.org/W3040838455) |
| 6 | 2017 | A non-volatile organic electrochemical device as a low-voltage artificial synapse for neuromorphic computing | Yoeri van de Burgt; Ewout Lubberman; Elliot J. Fuller; Scott T. Keene; Gregório Couto Faria | Nature Materials | [10.1038/nmat4856](https://doi.org/10.1038/nmat4856) | 1780 | US,NL,BR |  | [link](https://openalex.org/W2591029953) |
| 7 | 2017 | A non-volatile organic electrochemical device as a low-voltage artificial synapse for neuromorphic computing | Yoeri van de Burgt; Ewout Lubberman; Elliot J. Fuller; Scott T. Keene; Gregório Couto Faria | Nature Materials | [10.1038/nmat4856](https://doi.org/10.1038/nmat4856) | 1780 | US,NL,BR |  | [link](https://openalex.org/W2591029953) |
| 8 | 2021 | Photonics for artificial intelligence and neuromorphic computing | Bhavin J. Shastri; Alexander N. Tait; T. Ferreira de Lima; Wolfram H. P. Pernice; Harish Bhaskaran | Nature Photonics | [10.1038/s41566-020-00754-y](https://doi.org/10.1038/s41566-020-00754-y) | 1565 | US,CA,DE,GB |  | [link](https://openalex.org/W3096230432) |
| 9 | 2021 | Photonics for artificial intelligence and neuromorphic computing | Bhavin J. Shastri; Alexander N. Tait; T. Ferreira de Lima; Wolfram H. P. Pernice; Harish Bhaskaran | Nature Photonics | [10.1038/s41566-020-00754-y](https://doi.org/10.1038/s41566-020-00754-y) | 1565 | US,CA,DE,GB |  | [link](https://openalex.org/W3096230432) |
| 10 | 2016 | ISAAC | Ali Shafiee; Anirban Nag; Naveen Muralimanohar; Rajeev Balasubramonian; John Paul Strachan | ACM SIGARCH Computer Architecture News | [10.1145/3007787.3001139](https://doi.org/10.1145/3007787.3001139) | 1517 | US |  | [link](https://openalex.org/W2518281301) |
| 11 | 2016 | ISAAC | Ali Shafiee; Anirban Nag; Naveen Muralimanohar; Rajeev Balasubramonian; John Paul Strachan | ACM SIGARCH Computer Architecture News | [10.1145/3007787.3001139](https://doi.org/10.1145/3007787.3001139) | 1517 | US |  | [link](https://openalex.org/W2518281301) |
| 12 | 2021 | Photonics for artificial intelligence and neuromorphic computing | Bhaskaran, H; Pernice, WHP; Thomas Ferreira de Lima; Shastri, BJ; Tait, AN | Oxford University Research Archive (ORA) (University of Oxfo |  | 1406 | CA,US,DE,GB |  | [link](https://openalex.org/W3128451613) |
| 13 | 2021 | Photonics for artificial intelligence and neuromorphic computing | Bhaskaran, H; Pernice, WHP; Thomas Ferreira de Lima; Shastri, BJ; Tait, AN | Oxford University Research Archive (ORA) (University of Oxfo |  | 1406 | CA,US,DE,GB |  | [link](https://openalex.org/W3128451613) |
| 14 | 2019 | Surrogate Gradient Learning in Spiking Neural Networks: Bringing the Power of Gradient-Based Optimization to Spiking Neural Networks | Emre Neftci; Hesham Mostafa; Friedemann Zenke | IEEE Signal Processing Magazine | [10.1109/msp.2019.2931595](https://doi.org/10.1109/msp.2019.2931595) | 1355 | CH,DE |  | [link](https://openalex.org/W2984844508) |
| 15 | 2017 | Neuromorphic computing with nanoscale spintronic oscillators | Jacob Torrejón; Mathieu Riou; Flavio Abreu Araujo; Sumito Tsunegi; Guru Khalsa | Nature | [10.1038/nature23011](https://doi.org/10.1038/nature23011) | 1329 | FR,JP,US | YES | [link](https://openalex.org/W2584998015) |
| 16 | 2017 | Neuromorphic computing with nanoscale spintronic oscillators | Jacob Torrejón; Mathieu Riou; Flavio Abreu Araujo; Sumito Tsunegi; Guru Khalsa | Nature | [10.1038/nature23011](https://doi.org/10.1038/nature23011) | 1329 | FR,JP,US | YES | [link](https://openalex.org/W2584998015) |
| 17 | 2017 | Analogue signal and image processing with large memristor crossbars | Can Li; Miao Hu; Yunning Li; Hao Jiang; Ning Ge | Nature Electronics | [10.1038/s41928-017-0002-z](https://doi.org/10.1038/s41928-017-0002-z) | 1254 | US |  | [link](https://openalex.org/W2775771159) |
| 18 | 2018 | Spatio-Temporal Backpropagation for Training High-Performance Spiking Neural Networks | Yujie Wu; Lei Deng; Guoqi Li; Jun Zhu; Luping Shi | Frontiers in Neuroscience | [10.3389/fnins.2018.00331](https://doi.org/10.3389/fnins.2018.00331) | 1127 | CN,US |  | [link](https://openalex.org/W2621826044) |
| 19 | 2016 | Neuromorphic computing using non-volatile memory | Geoffrey W. Burr; R. M. Shelby; Abu Sebastian; Sang‐Bum Kim; Seyoung Kim | Advances in Physics X | [10.1080/23746149.2016.1259585](https://doi.org/10.1080/23746149.2016.1259585) | 1074 | US,CH,JP,KR | YES | [link](https://openalex.org/W2560615381) |
| 20 | 2016 | Neuromorphic computing using non-volatile memory | Geoffrey W. Burr; R. M. Shelby; Abu Sebastian; Sang‐Bum Kim; Seyoung Kim | Advances in Physics X | [10.1080/23746149.2016.1259585](https://doi.org/10.1080/23746149.2016.1259585) | 1074 | US,CH,JP,KR | YES | [link](https://openalex.org/W2560615381) |

**日本機関所属著者を含む論文** (上記 Top 20 のうち):

| Year | Title | JP Affiliation (raw) | DOI |
|---:|---|---|---|
| 2017 | Neuromorphic computing with nanoscale spintronic oscillators | National Institute of Advanced Industrial Science and Technology \|\| National Institute of Advanced Industrial Science and Technology \|\| National Institute o | [10.1038/nature23011](https://doi.org/10.1038/nature23011) |
| 2017 | Neuromorphic computing with nanoscale spintronic oscillators | National Institute of Advanced Industrial Science and Technology \|\| National Institute of Advanced Industrial Science and Technology \|\| National Institute o | [10.1038/nature23011](https://doi.org/10.1038/nature23011) |
| 2016 | Neuromorphic computing using non-volatile memory | IBM Research - Tokyo | [10.1080/23746149.2016.1259585](https://doi.org/10.1080/23746149.2016.1259585) |
| 2016 | Neuromorphic computing using non-volatile memory | IBM Research - Tokyo | [10.1080/23746149.2016.1259585](https://doi.org/10.1080/23746149.2016.1259585) |

### Milestones (academic evidence, n=24)

| Year | Tech | Type | Description | Evidence | Confidence | Status | DOI | source_url |
|---:|---|---|---|---|---:|---|---|---|
| 2006 | spiking neural network | mass_deployment | s successfully tested on well-known and widely used classification problems. | academic_paper_mid_citation | 0.52 | observed | [10.1109/ijcnn.2005.1556240](https://doi.org/10.1109/ijcnn.2005.1556240) | [link](https://openalex.org/W1503343880) |
| 2007 | spiking neural network | prototype | robust object recognition, as demonstrated on various classification tasks. Taken together, these resu | academic_paper | 0.75 | observed | [10.1371/journal.pcbi.0030031](https://doi.org/10.1371/journal.pcbi.0030031) | [link](https://openalex.org/W2007815184) |
| 2011 | spiking neural network | prototype | rge scale neural systems is introduced. First demonstration of complex visual pattern extraction from real world data using PCM synapses in | academic_paper_mid_citation | 0.61 | observed | [10.1109/iedm.2011.6131488](https://doi.org/10.1109/iedm.2011.6131488) | [link](https://openalex.org/W1991059746) |
| 2012 | memristor crossbar | mass_deployment | ssociative neural network that has been widely used in optical character recognition and image processing. Traditionally, the BSB m | academic_paper_mid_citation | 0.56 | observed | [10.1145/2228360.2228448](https://doi.org/10.1145/2228360.2228448) | [link](https://openalex.org/W1976075132) |
| 2012 | memristor crossbar | mass_deployment | ssociative neural network that has been widely used in optical character recognition and image processing. Traditionally, the BSB m | academic_paper_mid_citation | 0.51 | observed | [10.1109/ijcnn.2012.6252563](https://doi.org/10.1109/ijcnn.2012.6252563) | [link](https://openalex.org/W1994589723) |
| 2013 | spiking neural network | prototype | implementation. The method is demonstrated in simulation and by a real-time implementation of a 3-laye | academic_paper | 0.75 | observed | [10.3389/fnins.2013.00178](https://doi.org/10.3389/fnins.2013.00178) | [link](https://openalex.org/W2008008156) |
| 2014 | memristor crossbar | prototype | in Von Neumann architecture. The recent breakthrough on memristor devices made an important step toward realizing a low-power, small | academic_paper_mid_citation | 0.53 | observed | [10.1109/iccad.2014.7001330](https://doi.org/10.1109/iccad.2014.7001330) | [link](https://openalex.org/W4245731639) |
| 2015 | spiking neural network | mass_deployment | ark tasks that outperform the other two widely used learning rules for classification. The results also demonstrate the computation | academic_paper_mid_citation | 0.52 | observed | [10.1109/tnnls.2015.2416771](https://doi.org/10.1109/tnnls.2015.2416771) | [link](https://openalex.org/W2086066258) |
| 2016 | neuromorphic computing | commercial | training, for applications of commercial significance. We then survey recent research in which diffe | academic_paper | 0.75 | observed | [10.1080/23746149.2016.1259585](https://doi.org/10.1080/23746149.2016.1259585) | [link](https://openalex.org/W2560615381) |
| 2016 | neuromorphic computing | prototype | euromorphic computing has now demonstrated unprecedented energy-efficiency through a new chip architec | academic_paper | 0.75 | observed | [10.1073/pnas.1604850113](https://doi.org/10.1073/pnas.1604850113) | [link](https://openalex.org/W2314470091) |
| 2017 | memristor crossbar | prototype | o the best of our knowledge this is the first demonstration of a functional 3D CMOL hybrid circuit. | academic_paper_mid_citation | 0.52 | observed | [10.1038/srep42429](https://doi.org/10.1038/srep42429) | [link](https://openalex.org/W2587921983) |
| 2018 | memristor crossbar | prototype | ls across a 128 × 64 array is demonstrated, and the resulting vector matrix multiplication (VMM) compu | academic_paper | 0.75 | observed | [10.1002/adma.201705914](https://doi.org/10.1002/adma.201705914) | [link](https://openalex.org/W2782791387) |
| 2019 | neuromorphic computing | commercial | terial issues have been pointed out for commercialization in conjunction with CMOS processing and device structures. Herein, we review fe | academic_paper_mid_citation | 0.59 | observed | [10.1063/1.5108562](https://doi.org/10.1063/1.5108562) | [link](https://openalex.org/W2974354593) |
| 2019 | neuromorphic computing | prototype | nd paired-pulse facilitation, have been successfully achieved. By incorporating 2D materials and oxides into a double-layer MD, the practica | academic_paper_mid_citation | 0.57 | observed | [10.1021/acsami.9b17160](https://doi.org/10.1021/acsami.9b17160) | [link](https://openalex.org/W2992473370) |
| 2019 | spiking neural network | mass_deployment | ch and the GMapping algorithm, which is widely used in small environments. Our Loihi-based SNN architecture consumes 100 times less | academic_paper_mid_citation | 0.52 | observed | [10.1109/iros40897.2019.8967864](https://doi.org/10.1109/iros40897.2019.8967864) | [link](https://openalex.org/W3003876377) |
| 2019 | spiking neural network | prototype | grammable gate array are presented as a proof of concept. Accordingly, the maximum frequency of the implemented neuron model and spiking | academic_paper_mid_citation | 0.52 | observed | [10.1109/tcsii.2019.2890846](https://doi.org/10.1109/tcsii.2019.2890846) | [link](https://openalex.org/W2907516714) |
| 2019 | Loihi neuromorphic | mass_deployment | GMapping algorithm, which is widely used in small environments. Our Loihi-based SNN architecture con | academic_paper | 0.65 | observed | [10.1109/iros40897.2019.8967864](https://doi.org/10.1109/iros40897.2019.8967864) | [link](https://openalex.org/W3003876377) |
| 2020 | neuromorphic computing | prototype | s are discussed. Recent progress on the experimental demonstration of neuromorphic computing systems (NCSs) is presented. Recommendations fo | academic_paper_mid_citation | 0.57 | observed | [10.1002/aisy.202000137](https://doi.org/10.1002/aisy.202000137) | [link](https://openalex.org/W3095769467) |
| 2020 | spiking neural network | prototype | p neural networks (DNNs) have demonstrated remarkable performance in a variety of applications. As we | academic_paper | 0.75 | observed | [10.1609/aaai.v34i07.6787](https://doi.org/10.1609/aaai.v34i07.6787) | [link](https://openalex.org/W2998119008) |
| 2020 | memristor crossbar | prototype | s are discussed. Recent progress on the experimental demonstration of neuromorphic computing systems (NCSs) is presented. Recommendations fo | academic_paper_mid_citation | 0.57 | observed | [10.1002/aisy.202000137](https://doi.org/10.1002/aisy.202000137) | [link](https://openalex.org/W3095769467) |
| 2020 | memristor crossbar | proposal | timization framework which contains the first proposed Network Purification and Unused Path Removal algorithms targeting on post-proce | academic_paper_mid_citation | 0.50 | observed | [10.1109/asp-dac47756.2020.9045658](https://doi.org/10.1109/asp-dac47756.2020.9045658) | [link](https://openalex.org/W3013407975) |
| 2022 | neuromorphic computing | prototype | Experimental demonstration of highly reliable dynamic memristor for artificial neuron and neuromorphic com | academic_paper_mid_citation | 0.62 | observed | [10.1038/s41467-022-30539-6](https://doi.org/10.1038/s41467-022-30539-6) | [link](https://openalex.org/W4281628293) |
| 2022 | neuromorphic computing | prototype | ). We demonstrate the relevance of such proof-of-concept perovskite devices on a benchmark reservoir network with volatile recurrent and | academic_paper_mid_citation | 0.60 | observed | [10.1038/s41467-022-29727-1](https://doi.org/10.1038/s41467-022-29727-1) | [link](https://openalex.org/W4224296904) |
| 2022 | neuromorphic computing | proposal | ming‐dependent plasticity response. The novel concept of controlling ionic migration in ferroelectric materials paves the way toward hig | academic_paper_mid_citation | 0.56 | observed | [10.1002/adfm.202202366](https://doi.org/10.1002/adfm.202202366) | [link](https://openalex.org/W4283389692) |

### Forecasts 2027-2100 (extracted from papers, n=0)

_no forecasts_

### TRL Trajectory (NASA TRL 1-9, n=4)

| Year | Tech | TRL | Evidence | Confidence | DOI | source_url |
|---:|---|---:|---|---:|---|---|
| 2024 | Loihi neuromorphic | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | memristor crossbar | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | neuromorphic computing | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | spiking neural network | 7 | current_status='early_deployment' | 0.80 |  |  |

---

## SAFETY_AI - AI Safety & Interpretability (AI安全・解釈可能性)

**Physical AI mapping**: SAFETY_AI

### Top 20 Cited Papers (citation_count desc)

| # | Year | Title | First Authors | Venue | DOI | Citations | Countries | JP authors? | source_url |
|---:|---:|---|---|---|---|---:|---|:---:|---|
| 1 | 2020 | A Novel Coronavirus from Patients with Pneumonia in China, 2019 | Na Zhu; Dingyu Zhang; Wenling Wang; Xingwang Li; Bo Yang | New England Journal of Medicine | [10.1056/nejmoa2001017](https://doi.org/10.1056/nejmoa2001017) | 30272 | CN |  | [link](https://openalex.org/W3001897055) |
| 2 | 2015 | A global reference for human genetic variation | Corresponding authors; Adam Auton; Gonçalo R. Abecasis; David M. Altshuler; Richard Durbin | Nature | [10.1038/nature15393](https://doi.org/10.1038/nature15393) | 19757 | US,GB,CA,DE,KR,CN,MO,DK,SA,HK,NL |  | [link](https://openalex.org/W2104549677) |
| 3 | 2011 | pROC: an open-source package for R and S+ to analyze and compare ROC curves | Xavier Robin; Natacha Turck; Alexandre Hainard; Natalia Tiberti; Frédérique Lisacek | BMC Bioinformatics | [10.1186/1471-2105-12-77](https://doi.org/10.1186/1471-2105-12-77) | 13798 | CH |  | [link](https://openalex.org/W2006617902) |
| 4 | 2019 | Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks | Nils Reimers; Iryna Gurevych |  | [10.18653/v1/d19-1410](https://doi.org/10.18653/v1/d19-1410) | 10531 | DE |  | [link](https://openalex.org/W2970641574) |
| 5 | 2009 | Fast model-based estimation of ancestry in unrelated individuals | David H. Alexander; John Novembre; Kenneth Lange | Genome Research | [10.1101/gr.094052.109](https://doi.org/10.1101/gr.094052.109) | 10462 | US |  | [link](https://openalex.org/W2119444539) |
| 6 | 2017 | Enriching Word Vectors with Subword Information | Piotr Bojanowski; Édouard Grave; Armand Joulin; Tomáš Mikolov | Transactions of the Association for Computational Linguistic | [10.1162/tacl_a_00051](https://doi.org/10.1162/tacl_a_00051) | 9724 | IL |  | [link](https://openalex.org/W2493916176) |
| 7 | 2007 | Nonparametric statistical testing of EEG- and MEG-data | Eric Maris; Robert Oostenveld | Journal of Neuroscience Methods | [10.1016/j.jneumeth.2007.03.024](https://doi.org/10.1016/j.jneumeth.2007.03.024) | 9123 | NL |  | [link](https://openalex.org/W2135894974) |
| 8 | 2006 | Extremely randomized trees | Pierre Geurts; Damien Ernst; Louis Wehenkel | Machine Learning | [10.1007/s10994-006-6226-1](https://doi.org/10.1007/s10994-006-6226-1) | 8494 | BE |  | [link](https://openalex.org/W2056132907) |
| 9 | 2022 | The STRING database in 2023: protein–protein association networks and functional enrichment analyses for any sequenced genome of interest | Damian Szklarczyk; Rebecca Kirsch; Mikaela Koutrouli; Katerina Nastou; Farrokh Mehryary | Nucleic Acids Research | [10.1093/nar/gkac1000](https://doi.org/10.1093/nar/gkac1000) | 8378 | CH,DK,FI,KR,DE |  | [link](https://openalex.org/W4308834893) |
| 10 | 2019 | Double-slit photoelectron interference in strong-field ionization of the neon dimer | M. Kunitski; Nicolas Eicke; P. Huber; Jonas Köhler; S. Zeller | GSI Repository (German Federal Government) | [10.15488/5174](https://doi.org/10.15488/5174) | 8266 | DE |  | [link](https://openalex.org/W3105982350) |
| 11 | 2018 | Double-slit photoelectron interference in strong-field ionization of the neon dimer | Maksim Kunitski; Nicolas Eicke; Pia Huber; Jonas Köhler; Stefan Zeller | Nature Communications | [10.1038/s41467-018-07882-8](https://doi.org/10.1038/s41467-018-07882-8) | 8246 | DE |  | [link](https://openalex.org/W2790756470) |
| 12 | 2012 | An integrated map of genetic variation from 1,092 human genomes |  Zamin Iqbal ;  Zamin Iqbal;  Andy Rimmer;  Anjali Gupta-Hinch; Gil A. McVean | Nature | [10.1038/nature11632](https://doi.org/10.1038/nature11632) | 8206 | GB,US,IT |  | [link](https://openalex.org/W2096791516) |
| 13 | 2014 | What Will 5G Be? | Jeffrey G. Andrews; Stefano Buzzi; Wan Choi; Stephen V. Hanly; Angel Lozano | IEEE Journal on Selected Areas in Communications | [10.1109/jsac.2014.2328098](https://doi.org/10.1109/jsac.2014.2328098) | 8148 | US,IT,KR,AU,ES |  | [link](https://openalex.org/W2054692642) |
| 14 | 2013 | The Behavior Change Technique Taxonomy (v1) of 93 Hierarchically Clustered Techniques: Building an International Consensus for the Reporting of Behavior Change Interventions | Susan Michie; Michelle Richardson; Marie Johnston; Charles Abraham; Jill Francis | Annals of Behavioral Medicine | [10.1007/s12160-013-9486-6](https://doi.org/10.1007/s12160-013-9486-6) | 7913 | GB |  | [link](https://openalex.org/W2169434152) |
| 15 | 2008 | Technology Acceptance Model 3 and a Research Agenda on Interventions | Viswanath Venkatesh; Hillol Bala | Decision Sciences | [10.1111/j.1540-5915.2008.00192.x](https://doi.org/10.1111/j.1540-5915.2008.00192.x) | 7664 | US |  | [link](https://openalex.org/W2112042732) |
| 16 | 2007 | Dissociable Intrinsic Connectivity Networks for Salience Processing and Executive Control | William W. Seeley; Vinod Menon; Alan F. Schatzberg; Jennifer Keller; Gary H. Glover | Journal of Neuroscience | [10.1523/jneurosci.5587-06.2007](https://doi.org/10.1523/jneurosci.5587-06.2007) | 7463 | US |  | [link](https://openalex.org/W2116658855) |
| 17 | 2017 | Advanced capabilities for materials modelling with Quantum ESPRESSO | P Giannozzi; O Andreussi; T Brumme; O Bunau; M Buongiorno Nardelli | Journal of Physics Condensed Matter | [10.1088/1361-648x/aa8f79](https://doi.org/10.1088/1361-648x/aa8f79) | 7363 | IT,CH,DE,FR,US,GB,JP,SI,VN,CA | YES | [link](https://openalex.org/W2757803490) |
| 18 | 2006 | A New Vertical Diffusion Package with an Explicit Treatment of Entrainment Processes | Song-You Hong; Yign Noh; Jimy Dudhia | Monthly Weather Review | [10.1175/mwr3199.1](https://doi.org/10.1175/mwr3199.1) | 7273 | KR,US |  | [link](https://openalex.org/W2028979275) |
| 19 | 2013 | Ultrasensitive fluorescent proteins for imaging neuronal activity | Tsai‐Wen Chen; Trevor J. Wardill; Yi Sun; Stefan R. Pulver; Sabine L. Renninger | Nature | [10.1038/nature12354](https://doi.org/10.1038/nature12354) | 7042 | US,PT |  | [link](https://openalex.org/W2171332611) |
| 20 | 2010 | Research Domain Criteria (RDoC): Toward a New Classification Framework for Research on Mental Disorders | Thomas R. Insel; Bruce N. Cuthbert; Marjorie A. Garvey; Robert Heinssen; Daniel S. Pine | American Journal of Psychiatry | [10.1176/appi.ajp.2010.09091379](https://doi.org/10.1176/appi.ajp.2010.09091379) | 6990 | US,CZ |  | [link](https://openalex.org/W1977465442) |

**日本機関所属著者を含む論文** (上記 Top 20 のうち):

| Year | Title | JP Affiliation (raw) | DOI |
|---:|---|---|---|
| 2017 | Advanced capabilities for materials modelling with Quantum ESPRESSO | Kavli Institute for the Physics and Mathematics of the Universe | [10.1088/1361-648x/aa8f79](https://doi.org/10.1088/1361-648x/aa8f79) |

### Milestones (academic evidence, n=3)

| Year | Tech | Type | Description | Evidence | Confidence | Status | DOI | source_url |
|---:|---|---|---|---|---:|---|---|---|
| 2011 | mechanistic interpretability | prototype | n-based methods. This example demonstrates how disease states can be detected with very high accuracy | academic_paper | 0.65 | observed | [10.1371/journal.pcbi.1002079](https://doi.org/10.1371/journal.pcbi.1002079) | [link](https://openalex.org/W1967541074) |
| 2018 | mechanistic interpretability | prototype | ectivity < 0.0001). Our study demonstrated that the effective connectivity measures might play a more | academic_paper | 0.65 | observed | [10.3389/fnins.2018.00038](https://doi.org/10.3389/fnins.2018.00038) | [link](https://openalex.org/W2793741653) |
| 2024 | RLHF reinforcement learning human feedback | prototype | F) in systems such as ChatGPT demonstrates the effectiveness of optimizing for user experience and int | academic_paper | 0.65 | observed | [10.1613/jair.1.15348](https://doi.org/10.1613/jair.1.15348) | [link](https://openalex.org/W4391399751) |

### Forecasts 2027-2100 (extracted from papers, n=5)

| Extracted Year | Tech | Evidence Phrase | Method | Confidence | Paper Year | DOI | source_url |
|---:|---|---|---|---:|---:|---|---|
| 2030 | RLHF reinforcement learning human feedback | Saudi Arabia’s Vision 2030 prioritizes advances in healthcare to improve accessibility | regex_abstract_S3 | 0.70 | 2025 | [10.1016/j.aej.2025.03.073](https://doi.org/10.1016/j.aej.2025.03.073) | [link](https://openalex.org/W4409161367) |
| 2035 | AI alignment | of AI Alignment Roadmap 2025-2035 | regex_year | 0.60 | 2025 | [10.36227/techrxiv.175877749.95952584/v1](https://doi.org/10.36227/techrxiv.175877749.95952584/v1) | [link](https://openalex.org/W4414520407) |
| 2035 | AI alignment | uture of AI Alignment Roadmap 2025-2035 | range_year | 0.70 | 2025 | [10.36227/techrxiv.175877749.95952584/v1](https://doi.org/10.36227/techrxiv.175877749.95952584/v1) | [link](https://openalex.org/W4414520407) |
| 2035 | RLHF reinforcement learning human feedback | of AI Alignment Roadmap 2025-2035 | regex_year | 0.60 | 2025 | [10.36227/techrxiv.175877749.95952584/v1](https://doi.org/10.36227/techrxiv.175877749.95952584/v1) | [link](https://openalex.org/W4414520407) |
| 2035 | RLHF reinforcement learning human feedback | uture of AI Alignment Roadmap 2025-2035 | range_year | 0.70 | 2025 | [10.36227/techrxiv.175877749.95952584/v1](https://doi.org/10.36227/techrxiv.175877749.95952584/v1) | [link](https://openalex.org/W4414520407) |

### TRL Trajectory (NASA TRL 1-9, n=5)

| Year | Tech | TRL | Evidence | Confidence | DOI | source_url |
|---:|---|---:|---|---:|---|---|
| 2024 | AI alignment | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | RLHF reinforcement learning human feedback | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | constitutional AI | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | interpretability neural network | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | mechanistic interpretability | 7 | current_status='early_deployment' | 0.80 |  |  |

---

## CYBER_PHYS - Cyber-Physical Systems (サイバーフィジカルシステム)

**Physical AI mapping**: ROBOTICS_HARDWARE / MOTION_PLANNING / CLASSICAL_CONTROL

### Top 20 Cited Papers (citation_count desc)

| # | Year | Title | First Authors | Venue | DOI | Citations | Countries | JP authors? | source_url |
|---:|---:|---|---|---|---|---:|---|:---:|---|
| 1 | 2018 | Digital Twin in manufacturing: A categorical literature review and classification | Werner Kritzinger; Matthias Karner; Georg Traar; Jan Henjes; Wilfried Sihn | IFAC-PapersOnLine | [10.1016/j.ifacol.2018.08.474](https://doi.org/10.1016/j.ifacol.2018.08.474) | 3032 | AT |  | [link](https://openalex.org/W2890904471) |
| 2 | 2017 | Digital twin-driven product design, manufacturing and service with big data | Fei Tao; Jiangfeng Cheng; Qinglin Qi; Meng Zhang; He Zhang | The International Journal of Advanced Manufacturing Technolo | [10.1007/s00170-017-0233-1](https://doi.org/10.1007/s00170-017-0233-1) | 2723 | CN |  | [link](https://openalex.org/W2597150627) |
| 3 | 2020 | Digital Twin: Enabling Technologies, Challenges and Open Research | Aidan Fuller; Zhong Fan; Charles Day; Chris Barlow | IEEE Access | [10.1109/access.2020.2998358](https://doi.org/10.1109/access.2020.2998358) | 2360 | GB |  | [link](https://openalex.org/W2982936646) |
| 4 | 2018 | Industrial Internet of Things: Challenges, Opportunities, and Directions | Emiliano Sisinni; Abusayeed Saifullah; Song Han; Ulf Jennehag; Mikael Gidlund | IEEE Transactions on Industrial Informatics | [10.1109/tii.2018.2852491](https://doi.org/10.1109/tii.2018.2852491) | 2267 | IT,US |  | [link](https://openalex.org/W2811266402) |
| 5 | 2018 | Industrial Internet of Things: Challenges, Opportunities, and Directions | Emiliano Sisinni; Abusayeed Saifullah; Song Han; Ulf Jennehag; Mikael Gidlund | IEEE Transactions on Industrial Informatics | [10.1109/tii.2018.2852491](https://doi.org/10.1109/tii.2018.2852491) | 2267 | IT,US |  | [link](https://openalex.org/W2811266402) |
| 6 | 2018 | DIGITAL TWIN: MANUFACTURING EXCELLENCE THROUGH VIRTUAL FACTORY REPLICATION | Vikas Bavane Prof. RajratnaKharat | Zenodo (CERN European Organization for Nuclear Research) | [10.5281/zenodo.1493930](https://doi.org/10.5281/zenodo.1493930) | 1784 | NP |  | [link](https://openalex.org/W3209398723) |
| 7 | 2017 | The Future of Industrial Communication: Automation Networks in the Era of the Internet of Things and Industry 4.0 | Martin Wollschlaeger; Thilo Sauter; Jürgen Jasperneite | IEEE Industrial Electronics Magazine | [10.1109/mie.2017.2649104](https://doi.org/10.1109/mie.2017.2649104) | 1672 | DE,AT |  | [link](https://openalex.org/W2599557761) |
| 8 | 2018 | Digital Twin and Big Data Towards Smart Manufacturing and Industry 4.0: 360 Degree Comparison | Qinglin Qi; Fei Tao | IEEE Access | [10.1109/access.2018.2793265](https://doi.org/10.1109/access.2018.2793265) | 1578 | CN |  | [link](https://openalex.org/W2783918566) |
| 9 | 2016 | Implementing Smart Factory of Industrie 4.0: An Outlook | Shiyong Wang; Jiafu Wan; Di Li; Chunhua Zhang | International Journal of Distributed Sensor Networks | [10.1155/2016/3159805](https://doi.org/10.1155/2016/3159805) | 1472 | CN |  | [link](https://openalex.org/W1560042744) |
| 10 | 2016 | Implementing Smart Factory of Industrie 4.0: An Outlook | Shiyong Wang; Jiafu Wan; Di Li; Chunhua Zhang | International Journal of Distributed Sensor Networks | [10.1155/2016/3159805](https://doi.org/10.1155/2016/3159805) | 1472 | CN |  | [link](https://openalex.org/W1560042744) |
| 11 | 2019 | Digital Twin-driven smart manufacturing: Connotation, reference model, applications and research issues | Yuqian Lu; Chao Liu; Kevin I‐Kai Wang; Huiyue Huang; Xun Xu | Robotics and Computer-Integrated Manufacturing | [10.1016/j.rcim.2019.101837](https://doi.org/10.1016/j.rcim.2019.101837) | 1431 | NZ,GB |  | [link](https://openalex.org/W2966906878) |
| 12 | 2015 | About The Importance of Autonomy and Digital Twins for the Future of Manufacturing | Roland Rosen; Georg von Wichert; George Lo; Kurt Dirk Bettenhausen | IFAC-PapersOnLine | [10.1016/j.ifacol.2015.06.141](https://doi.org/10.1016/j.ifacol.2015.06.141) | 1402 | DE,US |  | [link](https://openalex.org/W2346505350) |
| 13 | 2018 | The industrial internet of things (IIoT): An analysis framework | Hugh Boyes; Bil Hallaq; Joe Cunningham; Tim Watson | Computers in Industry | [10.1016/j.compind.2018.04.015](https://doi.org/10.1016/j.compind.2018.04.015) | 1401 | GB |  | [link](https://openalex.org/W2805611890) |
| 14 | 2018 | The industrial internet of things (IIoT): An analysis framework | Hugh Boyes; Bil Hallaq; Joe Cunningham; Tim Watson | Computers in Industry | [10.1016/j.compind.2018.04.015](https://doi.org/10.1016/j.compind.2018.04.015) | 1401 | GB |  | [link](https://openalex.org/W2805611890) |
| 15 | 2016 | Towards smart factory for industry 4.0: a self-organized multi-agent system with big data based feedback and coordination | Shiyong Wang; Jiafu Wan; Daqiang Zhang; Di Li; Chunhua Zhang | Computer Networks | [10.1016/j.comnet.2015.12.017](https://doi.org/10.1016/j.comnet.2015.12.017) | 1374 | CN |  | [link](https://openalex.org/W2507578125) |
| 16 | 2016 | Towards smart factory for industry 4.0: a self-organized multi-agent system with big data based feedback and coordination | Shiyong Wang; Jiafu Wan; Daqiang Zhang; Di Li; Chunhua Zhang | Computer Networks | [10.1016/j.comnet.2015.12.017](https://doi.org/10.1016/j.comnet.2015.12.017) | 1374 | CN |  | [link](https://openalex.org/W2507578125) |
| 17 | 2017 | Digital Twin Shop-Floor: A New Shop-Floor Paradigm Towards Smart Manufacturing | Fei Tao; Meng Zhang | IEEE Access | [10.1109/access.2017.2756069](https://doi.org/10.1109/access.2017.2756069) | 1310 | CN |  | [link](https://openalex.org/W2757110387) |
| 18 | 2019 | Digital Twins and Cyber–Physical Systems toward Smart Manufacturing and Industry 4.0: Correlation and Comparison | Fei Tao; Qinglin Qi; Lihui Wang; A.Y.C. Nee | Engineering | [10.1016/j.eng.2019.01.014](https://doi.org/10.1016/j.eng.2019.01.014) | 1302 | CN,SE,SG |  | [link](https://openalex.org/W2945357379) |
| 19 | 2019 | Blockchain and Federated Learning for Privacy-Preserved Data Sharing in Industrial IoT | Yunlong Lu; Xiaohong Huang; Yueyue Dai; Sabita Maharjan; Yan Zhang | IEEE Transactions on Industrial Informatics | [10.1109/tii.2019.2942190](https://doi.org/10.1109/tii.2019.2942190) | 1205 | CN,NO |  | [link](https://openalex.org/W2974429275) |
| 20 | 2011 | Cyber–Physical System Security for the Electric Power Grid | Siddharth Sridhar; Adam Hahn; Manimaran Govindarasu | Proceedings of the IEEE | [10.1109/jproc.2011.2165269](https://doi.org/10.1109/jproc.2011.2165269) | 1178 | US |  | [link](https://openalex.org/W2051054517) |

### Milestones (academic evidence, n=14)

| Year | Tech | Type | Description | Evidence | Confidence | Status | DOI | source_url |
|---:|---|---|---|---|---:|---|---|---|
| 2016 | industrial internet of things | mass_deployment | orted by wired or wireless networks are widely adopted, and both real-time and delayed signals coexist. Therefore, based on the advanc | academic_paper_high_citation | 0.80 | observed | [10.1109/jsen.2016.2565621](https://doi.org/10.1109/jsen.2016.2565621) | [link](https://openalex.org/W2364839527) |
| 2017 | industrial internet of things | mass_deployment | This energy blockchain can be widely used in general scenarios of P2P energy trading getting rid of a | academic_paper | 0.75 | observed | [10.1109/tii.2017.2786307](https://doi.org/10.1109/tii.2017.2786307) | [link](https://openalex.org/W2777447168) |
| 2017 | industrial internet of things | mass_deployment | Internet of Things (IIoT) and have been widely used in many industrial fields to gather data of monitoring area. However, due to th | academic_paper_mid_citation | 0.66 | observed | [10.1109/tii.2017.2773666](https://doi.org/10.1109/tii.2017.2773666) | [link](https://openalex.org/W2769200374) |
| 2017 | industrial internet of things | commercial | using on analyzing data from the entire production line. These applications bring a new set of analytics challenges. Unlike traditional | academic_paper_mid_citation | 0.58 | observed | [10.1109/mis.2017.49](https://doi.org/10.1109/mis.2017.49) | [link](https://openalex.org/W2617697157) |
| 2017 | smart factory | commercial | technologies. An Industry 4.0 production system is thus flexible and enables individualized and cust | academic_paper | 0.75 | observed | [10.3991/ijim.v11i5.7072](https://doi.org/10.3991/ijim.v11i5.7072) | [link](https://openalex.org/W2737940375) |
| 2018 | industrial internet of things | prototype | ence achieving end-toend security. As a proof of concept, this solution has been implemented and validated with an open source EPC. | academic_paper_mid_citation | 0.55 | observed | [10.1109/mcom.2018.1700625](https://doi.org/10.1109/mcom.2018.1700625) | [link](https://openalex.org/W2785728462) |
| 2019 | digital twin manufacturing | commercial | process planning, intelligent production scheduling and production process analysis and dynamic regu | academic_paper | 0.75 | observed | [10.1080/00207543.2019.1607978](https://doi.org/10.1080/00207543.2019.1607978) | [link](https://openalex.org/W2941765731) |
| 2019 | industrial internet of things | mass_deployment | rial Internet of Things (IIoT) has been widely used in many fields. Meanwhile, blockchain is considered promising to address the is | academic_paper_mid_citation | 0.52 | observed | [10.1109/tii.2019.2931157](https://doi.org/10.1109/tii.2019.2931157) | [link](https://openalex.org/W2963023955) |
| 2019 | cyber physical security | commercial | utonomous decisions on energy production, and demand response. However, the electric grid cyber asse | academic_paper | 0.65 | observed | [10.1109/tsg.2019.2928168](https://doi.org/10.1109/tsg.2019.2928168) | [link](https://openalex.org/W2961152305) |
| 2020 | digital twin manufacturing | prototype | he implementation of an MBCoT prototype system and its application examples justify that the propos | academic_paper | 0.65 | observed | [10.1109/jiot.2020.3005729](https://doi.org/10.1109/jiot.2020.3005729) | [link](https://openalex.org/W3038926533) |
| 2020 | digital twin manufacturing | commercial | MS can connect raw materials, production systems, logistic companies, and maintenance schedules usin | academic_paper | 0.65 | observed | [10.1080/0951192x.2020.1815850](https://doi.org/10.1080/0951192x.2020.1815850) | [link](https://openalex.org/W3111020272) |
| 2020 | industrial internet of things | mass_deployment | ngs Smart cameras and image sensors are widely used in industrial processes, from the designing to the quality checking of the fina | academic_paper_mid_citation | 0.54 | observed | [10.3390/e22020175](https://doi.org/10.3390/e22020175) | [link](https://openalex.org/W3005115714) |
| 2021 | smart factory | prototype | ndustrial Revolution 4.0 began with the breakthrough technological advances in 5G, and artificial intelligence has innovatively tran | academic_paper_mid_citation | 0.53 | observed | [10.7717/peerj-cs.350](https://doi.org/10.7717/peerj-cs.350) | [link](https://openalex.org/W3124724827) |
| 2022 | industrial internet of things | mass_deployment | on Recently, model compression has been widely used for the deployment of cumbersome deep models on resource-limited edge devices i | academic_paper_mid_citation | 0.52 | observed | [10.1109/tii.2022.3209672](https://doi.org/10.1109/tii.2022.3209672) | [link](https://openalex.org/W4297095243) |

### Forecasts 2027-2100 (extracted from papers, n=0)

_no forecasts_

### TRL Trajectory (NASA TRL 1-9, n=4)

| Year | Tech | TRL | Evidence | Confidence | DOI | source_url |
|---:|---|---:|---|---:|---|---|
| 2024 | cyber physical security | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | digital twin manufacturing | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | industrial internet of things | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | smart factory | 7 | current_status='early_deployment' | 0.80 |  |  |

---

## BRAIN_CI - Brain-Computer Interfaces (脳-機械インタフェース)

**Physical AI mapping**: VLM_FOUNDATION (sensor side) / BRAIN-MACHINE

### Top 20 Cited Papers (citation_count desc)

| # | Year | Title | First Authors | Venue | DOI | Citations | Countries | JP authors? | source_url |
|---:|---:|---|---|---|---|---:|---|:---:|---|
| 1 | 2010 | FieldTrip: Open Source Software for Advanced Analysis of MEG, EEG, and Invasive Electrophysiological Data | Robert Oostenveld; Pascal Fries; Eric Maris; Jan‐Mathijs Schoffelen | Computational Intelligence and Neuroscience | [10.1155/2011/156869](https://doi.org/10.1155/2011/156869) | 11209 | NL,DE |  | [link](https://openalex.org/W2166073443) |
| 2 | 2007 | Sparse MRI: The application of compressed sensing for rapid MR imaging | Michael Lustig; David L. Donoho; John M. Pauly | Magnetic Resonance in Medicine | [10.1002/mrm.21391](https://doi.org/10.1002/mrm.21391) | 6925 | US |  | [link](https://openalex.org/W2101675075) |
| 3 | 2011 | Sensitivity of revised diagnostic criteria for the behavioural variant of frontotemporal dementia | Katya Rascovsky; John R. Hodges; David S. Knopman; Mario F. Mendez; Joel H. Kramer | Brain | [10.1093/brain/awr179](https://doi.org/10.1093/brain/awr179) | 5217 | US,AU,NL,CA,GB,FR,AR,IT |  | [link](https://openalex.org/W2128030851) |
| 4 | 2011 | Classification of primary progressive aphasia and its variants | Maria‐Luisa Gorno‐Tempini; Argye E. Hillis; Sandra Weıntraub; Andrew Kertesz; Mario F. Mendez | Neurology | [10.1212/wnl.0b013e31821103e6](https://doi.org/10.1212/wnl.0b013e31821103e6) | 5062 | IT,US,BE |  | [link](https://openalex.org/W2138190873) |
| 5 | 2016 | Neural Architectures for Named Entity Recognition | Guillaume Lample; Miguel Ballesteros; Sandeep Subramanian; Kazuya Kawakami; Chris Dyer |  | [10.18653/v1/n16-1030](https://doi.org/10.18653/v1/n16-1030) | 4400 | US,ES |  | [link](https://openalex.org/W2296283641) |
| 6 | 2018 | EEGNet: a compact convolutional neural network for EEG-based brain–computer interfaces | Vernon J Lawhern; Amelia J Solon; Nicholas R Waytowich; Stephen M Gordon; Chou P Hung | Journal of Neural Engineering | [10.1088/1741-2552/aace8c](https://doi.org/10.1088/1741-2552/aace8c) | 4120 | US |  | [link](https://openalex.org/W2559463885) |
| 7 | 2013 | MEG and EEG data analysis with MNE-Python | Alexandre Gramfort | Frontiers in Neuroscience | [10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267) | 3899 | FR,US |  | [link](https://openalex.org/W2169918686) |
| 8 | 2017 | Local-Global Parcellation of the Human Cerebral Cortex from Intrinsic Functional Connectivity MRI | Alexander Schaefer; Ru Kong; Evan M. Gordon; Timothy O. Laumann; Xi‐Nian Zuo | Cerebral Cortex | [10.1093/cercor/bhx179](https://doi.org/10.1093/cercor/bhx179) | 3699 | SG,US,CN,DE |  | [link](https://openalex.org/W2951617899) |
| 9 | 2006 | Neuronal ensemble control of prosthetic devices by a human with tetraplegia | Leigh R. Hochberg; Mijail D. Serruya; Gerhard M. Friehs; Jon Mukand; Maryam Saleh | Nature | [10.1038/nature04970](https://doi.org/10.1038/nature04970) | 3317 | US |  | [link](https://openalex.org/W2114004602) |
| 10 | 2008 | Collective Classification in Network Data | Prithviraj Sen; Galileo Namata; Mustafa Bilgic; Lise Getoor; Brian Gallagher | AI Magazine | [10.1609/aimag.v29i3.2157](https://doi.org/10.1609/aimag.v29i3.2157) | 3262 | US |  | [link](https://openalex.org/W2153959628) |
| 11 | 2012 | Tracking Whole-Brain Connectivity Dynamics in the Resting State | Elena A. Allen; Eswar Damaraju; Sergey Plis; Erik B. Erhardt; Tom Eichele | Cerebral Cortex | [10.1093/cercor/bhs352](https://doi.org/10.1093/cercor/bhs352) | 3189 | US,NO |  | [link](https://openalex.org/W2170702893) |
| 12 | 2015 | Functional connectome fingerprinting: identifying individuals using patterns of brain connectivity | Emily S. Finn; Xilin Shen; Dustin Scheinost; Monica D. Rosenberg; Jessica S. Huang | Nature Neuroscience | [10.1038/nn.4135](https://doi.org/10.1038/nn.4135) | 3001 | US |  | [link](https://openalex.org/W2111902267) |
| 13 | 2009 | Moving beyond Kučera and Francis: A critical evaluation of current word frequency norms and the introduction of a new and improved word frequency measure for American English | Marc Brysbaert; Boris New | Behavior Research Methods | [10.3758/brm.41.4.977](https://doi.org/10.3758/brm.41.4.977) | 2797 | BE,GB,FR |  | [link](https://openalex.org/W1997161938) |
| 14 | 2012 | Reach and grasp by people with tetraplegia using a neurally controlled robotic arm | Leigh R. Hochberg; Daniel Bacher; Beata Jarosiewicz; Nicolas Y. Masse; John D. Simeral | Nature | [10.1038/nature11076](https://doi.org/10.1038/nature11076) | 2716 | US,DE |  | [link](https://openalex.org/W2087704839) |
| 15 | 2016 | CDC Guideline for Prescribing Opioids for Chronic Pain — United States, 2016 | Deborah Dowell; Tamara M. Haegerich; Roger Chou | MMWR Recommendations and Reports | [10.15585/mmwr.rr6501e1](https://doi.org/10.15585/mmwr.rr6501e1) | 2682 | US |  | [link](https://openalex.org/W2920592781) |
| 16 | 2009 | The myth of language universals: Language diversity and its importance for cognitive science | Nicholas Evans; Stephen C. Levinson | Behavioral and Brain Sciences | [10.1017/s0140525x0999094x](https://doi.org/10.1017/s0140525x0999094x) | 2619 | AU,NL |  | [link](https://openalex.org/W2000196122) |
| 17 | 2014 | Machine learning for neuroimaging with scikit-learn | Alexandre Abraham; Fabian Pedregosa; Michael Eickenberg; Philippe Gervais; Andreas Mueller | Frontiers in Neuroinformatics | [10.3389/fninf.2014.00014](https://doi.org/10.3389/fninf.2014.00014) | 2606 | FR,DE,GB |  | [link](https://openalex.org/W2151591509) |
| 18 | 2017 | Translanguaging as a Practical Theory of Language | Li Wei | Applied Linguistics | [10.1093/applin/amx039](https://doi.org/10.1093/applin/amx039) | 2523 | US,GB |  | [link](https://openalex.org/W2765659056) |
| 19 | 2017 | Automated Hate Speech Detection and the Problem of Offensive Language | Thomas Davidson; Dana Warmsley; Michael W. Macy; Ingmar Weber | Proceedings of the International AAAI Conference on Web and  | [10.1609/icwsm.v11i1.14955](https://doi.org/10.1609/icwsm.v11i1.14955) | 2433 | US,QA |  | [link](https://openalex.org/W2595653137) |
| 20 | 2017 | Fully integrated silicon probes for high-density recording of neural activity | James J. Jun; Nicholas A. Steinmetz; Joshua H. Siegle; Daniel J. Denman; Marius Bauža | Nature | [10.1038/nature24636](https://doi.org/10.1038/nature24636) | 2361 | US,GB,CA,BE |  | [link](https://openalex.org/W2767493192) |

### Milestones (academic evidence, n=11)

| Year | Tech | Type | Description | Evidence | Confidence | Status | DOI | source_url |
|---:|---|---|---|---|---:|---|---|---|
| 2009 | brain-computer interface | mass_deployment | orded from the surface of the scalp are widely used in current BCIs for their non-invasive nature and easy applications. Among EEG | academic_paper_mid_citation | 0.59 | observed | [10.1109/mci.2009.934562](https://doi.org/10.1109/mci.2009.934562) | [link](https://openalex.org/W2121483555) |
| 2010 | brain-computer interface | pilot | cause frustration. This paper reports a pilot study in which a BCI system is used to provide a computer game-based neurofeedback to | academic_paper_mid_citation | 0.62 | observed | [10.1186/1743-0003-7-60](https://doi.org/10.1186/1743-0003-7-60) | [link](https://openalex.org/W2170059436) |
| 2011 | brain-computer interface | mass_deployment | of BCI-enhanced communication with the widely used P300-Speller. | academic_paper_mid_citation | 0.61 | observed | [10.1088/1741-2560/8/5/056016](https://doi.org/10.1088/1741-2560/8/5/056016) | [link](https://openalex.org/W2074711172) |
| 2011 | brain-computer interface | mass_deployment | Emotiv EPOC. The Emotiv headset becomes widely used in consumer BCI application allowing for conducting large-scale EEG experiments | academic_paper_mid_citation | 0.54 | observed | [10.1371/journal.pone.0020674](https://doi.org/10.1371/journal.pone.0020674) | [link](https://openalex.org/W2147659606) |
| 2012 | intracortical microelectrode | prototype | ontrast, stab injured animals demonstrated a CNS-mediated neurodegenerative environment. Collectively | academic_paper | 0.75 | observed | [10.1088/1741-2560/9/4/046020](https://doi.org/10.1088/1741-2560/9/4/046020) | [link](https://openalex.org/W1969870305) |
| 2014 | brain-computer interface | mass_deployment | on and mental motor imagery, thus it is widely used for the brain-computer interface (BCI) purpose. However what the ERD really ref | academic_paper_mid_citation | 0.54 | observed | [10.1186/1743-0003-11-90](https://doi.org/10.1186/1743-0003-11-90) | [link](https://openalex.org/W2052984950) |
| 2014 | intracortical microelectrode | prototype | ortex, the compliant implants demonstrated a significantly reduced neuroinflammatory response when com | academic_paper | 0.75 | observed | [10.1088/1741-2560/11/5/056014](https://doi.org/10.1088/1741-2560/11/5/056014) | [link](https://openalex.org/W2084506653) |
| 2016 | non-invasive BCI | prototype | elchairs and quadcopters, has demonstrated the promise of BCI technologies. However, controlling a rob | academic_paper | 0.75 | observed | [10.1038/srep38565](https://doi.org/10.1038/srep38565) | [link](https://openalex.org/W2561907433) |
| 2019 | brain-computer interface | mass_deployment | oencephalography (EEG) signals are most widely used due to their non-invasive EEG electrodes, portability, and cost efficiency. The | academic_paper_mid_citation | 0.55 | observed | [10.1007/s10462-019-09694-8](https://doi.org/10.1007/s10462-019-09694-8) | [link](https://openalex.org/W2919403121) |
| 2019 | brain-computer interface | proposal | flowering of developments since it was first introduced by Mesgarani and Chang (2012) using electrocorticograph recordings. AAD has bee | academic_paper_mid_citation | 0.54 | observed | [10.1038/s41598-019-47795-0](https://doi.org/10.1038/s41598-019-47795-0) | [link](https://openalex.org/W2968050947) |
| 2021 | brain-computer interface | mass_deployment | ence. Significant research efforts on a global scale have delivered common platforms for technology standardization and help tackle | academic_paper_mid_citation | 0.63 | observed | [10.3389/fnsys.2021.578875](https://doi.org/10.3389/fnsys.2021.578875) | [link](https://openalex.org/W2910098374) |

### Forecasts 2027-2100 (extracted from papers, n=1)

| Extracted Year | Tech | Evidence Phrase | Method | Confidence | Paper Year | DOI | source_url |
|---:|---|---|---|---:|---:|---|---|
| 2045 | Neuralink | book, The Singularity Is Near, and its forecast that around 2045 computer systems would attain superhuman intelligence. This | regex_abstract_S3 | 0.70 | 2025 | [10.56315/pscf3-25kurzweil](https://doi.org/10.56315/pscf3-25kurzweil) | [link](https://openalex.org/W4407713243) |

### TRL Trajectory (NASA TRL 1-9, n=4)

| Year | Tech | TRL | Evidence | Confidence | DOI | source_url |
|---:|---|---:|---|---:|---|---|
| 2024 | Neuralink | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | brain-computer interface | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | intracortical microelectrode | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | non-invasive BCI | 7 | current_status='early_deployment' | 0.80 |  |  |

---

## TRANSPORT - Transportation (輸送)

**Physical AI mapping**: ROBOTICS_HARDWARE / MOTION_PLANNING / RL

### Top 20 Cited Papers (citation_count desc)

| # | Year | Title | First Authors | Venue | DOI | Citations | Countries | JP authors? | source_url |
|---:|---:|---|---|---|---|---:|---|:---:|---|
| 1 | 2019 | How artificial intelligence will change the future of marketing | Thomas H. Davenport; Abhijit Guha; Dhruv Grewal; Timna Breßgott | Journal of the Academy of Marketing Science | [10.1007/s11747-019-00696-0](https://doi.org/10.1007/s11747-019-00696-0) | 2243 | US,NL |  | [link](https://openalex.org/W2979906316) |
| 2 | 2020 | A Survey of Autonomous Driving: <i>Common Practices and Emerging Technologies</i> | Ekim Yurtsever; Jacob Lambert; Alexander Carballo; Kazuya Takeda | IEEE Access | [10.1109/access.2020.2983149](https://doi.org/10.1109/access.2020.2983149) | 1698 | JP | YES | [link](https://openalex.org/W2953303875) |
| 3 | 2022 | FAST-LIO2: Fast Direct LiDAR-Inertial Odometry | Wei Xu; Yixi Cai; Dongjiao He; Jiarong Lin; Fu Zhang | IEEE Transactions on Robotics | [10.1109/tro.2022.3141876](https://doi.org/10.1109/tro.2022.3141876) | 1397 | HK |  | [link](https://openalex.org/W4210423514) |
| 4 | 2018 | DeepTest | Yuchi Tian; Kexin Pei; Suman Jana; Baishakhi Ray |  | [10.1145/3180155.3180220](https://doi.org/10.1145/3180155.3180220) | 1218 | US |  | [link](https://openalex.org/W2963327228) |
| 5 | 2020 | HOTA: A Higher Order Metric for Evaluating Multi-object Tracking | Jonathon Luiten; Aljos̆a Os̆ep; Patrick Dendorfer; Philip Torr; Andreas Geiger | International Journal of Computer Vision | [10.1007/s11263-020-01375-2](https://doi.org/10.1007/s11263-020-01375-2) | 995 | DE,GB |  | [link](https://openalex.org/W3086436251) |
| 6 | 2021 | Voxel R-CNN: Towards High Performance Voxel-based 3D Object Detection | Jiajun Deng; Shaoshuai Shi; Peiwei Li; Wengang Zhou; Yanyong Zhang | Proceedings of the AAAI Conference on Artificial Intelligenc | [10.1609/aaai.v35i2.16207](https://doi.org/10.1609/aaai.v35i2.16207) | 940 | CN |  | [link](https://openalex.org/W3118341329) |
| 7 | 2019 | Applications of Artificial Intelligence in Transport: An Overview | Rusul Abduljabbar; Hussein Dia; Sohani Liyanage; Saeed Asadi Bagloee | Sustainability | [10.3390/su11010189](https://doi.org/10.3390/su11010189) | 720 | AU |  | [link](https://openalex.org/W2908162093) |
| 8 | 2017 | Coherent solid-state LIDAR with silicon photonic optical phased arrays | Christopher V. Poulton; Ami Yaacobi; David B. Cole; Matthew J. Byrd; Manan Raval | Optics Letters | [10.1364/ol.42.004091](https://doi.org/10.1364/ol.42.004091) | 701 | US |  | [link](https://openalex.org/W2761155850) |
| 9 | 2017 | Coherent solid-state LIDAR with silicon photonic optical phased arrays | Christopher V. Poulton; Ami Yaacobi; David B. Cole; Matthew J. Byrd; Manan Raval | Optics Letters | [10.1364/ol.42.004091](https://doi.org/10.1364/ol.42.004091) | 701 | US |  | [link](https://openalex.org/W2761155850) |
| 10 | 2021 | Synthetic data in machine learning for medicine and healthcare | Richard J. Chen; Ming Y. Lu; Tiffany Chen; Drew F. K. Williamson; Faisal Mahmood | Nature Biomedical Engineering | [10.1038/s41551-021-00751-8](https://doi.org/10.1038/s41551-021-00751-8) | 679 | US |  | [link](https://openalex.org/W3166254754) |
| 11 | 2019 | Phase-only transmissive spatial light modulator based on tunable dielectric metasurface | Shi-Qiang Li; Xuewu Xu; Rasna Maruthiyodan Veetil; Vytautas Valuckas; Ramón Paniagua-Domínguez | Science | [10.1126/science.aaw6747](https://doi.org/10.1126/science.aaw6747) | 620 | SG |  | [link](https://openalex.org/W2912248624) |
| 12 | 2022 | 6G for Vehicle-to-Everything (V2X) Communications: Enabling Technologies, Challenges, and Opportunities | Md. Noor‐A‐Rahim; Zilong Liu; Haeyoung Lee; Mohammad Omar Khyam; Jianhua He | Proceedings of the IEEE | [10.1109/jproc.2022.3173031](https://doi.org/10.1109/jproc.2022.3173031) | 608 | IE,GB,AU,DE,US |  | [link](https://openalex.org/W3112379500) |
| 13 | 2018 | DeepRoad: GAN-based metamorphic testing and input validation framework for autonomous driving systems | Mengshi Zhang; Yuqun Zhang; Lingming Zhang; Cong Liu; Sarfraz Khurshid |  | [10.1145/3238147.3238187](https://doi.org/10.1145/3238147.3238187) | 592 | US,CN |  | [link](https://openalex.org/W2888307014) |
| 14 | 2019 | Long-Range LiDAR and Free-Space Data Communication With High-Performance Optical Phased Arrays | Christopher V. Poulton; Matthew J. Byrd; Peter Russo; Erman Timurdogan; Murshed Khandaker | IEEE Journal of Selected Topics in Quantum Electronics | [10.1109/jstqe.2019.2908555](https://doi.org/10.1109/jstqe.2019.2908555) | 556 | US |  | [link](https://openalex.org/W2925745050) |
| 15 | 2019 | Long-Range LiDAR and Free-Space Data Communication With High-Performance Optical Phased Arrays | Christopher V. Poulton; Matthew J. Byrd; Peter Russo; Erman Timurdogan; Murshed Khandaker | IEEE Journal of Selected Topics in Quantum Electronics | [10.1109/jstqe.2019.2908555](https://doi.org/10.1109/jstqe.2019.2908555) | 556 | US |  | [link](https://openalex.org/W2925745050) |
| 16 | 2020 | Diagnosing and correcting anode-free cell failure via electrolyte and morphological analysis | A. J. Louli; Ahmed Eldesoky; Rochelle Weber; Matthew Genovese; Matt Coon | Nature Energy | [10.1038/s41560-020-0668-8](https://doi.org/10.1038/s41560-020-0668-8) | 552 | CA,US |  | [link](https://openalex.org/W3047813479) |
| 17 | 2022 | PV-RCNN++: Point-Voxel Feature Set Abstraction With Local Vector Representation for 3D Object Detection | Shaoshuai Shi; Li Jiang; Jiajun Deng; Zhe Wang; Chaoxu Guo | International Journal of Computer Vision | [10.1007/s11263-022-01710-9](https://doi.org/10.1007/s11263-022-01710-9) | 489 | HK,DE,AU,CN |  | [link](https://openalex.org/W4310078553) |
| 18 | 2021 | The impact of 5G on the evolution of intelligent automation and industry digitization | Mohsen Attaran | Journal of Ambient Intelligence and Humanized Computing | [10.1007/s12652-020-02521-x](https://doi.org/10.1007/s12652-020-02521-x) | 483 | US |  | [link](https://openalex.org/W3129311377) |
| 19 | 2022 | Milestones in Autonomous Driving and Intelligent Vehicles: Survey of Surveys | Long Chen; Yuchen Li; Chao Huang; Bai Li; Yang Xing | IEEE Transactions on Intelligent Vehicles | [10.1109/tiv.2022.3223131](https://doi.org/10.1109/tiv.2022.3223131) | 480 | CN,HK,GB,SG,SS |  | [link](https://openalex.org/W4312550876) |
| 20 | 2018 | Technological, economic and environmental prospects of all-electric aircraft | Andreas Schäfer; Steven R. H. Barrett; Khan Doyme; Lynnette Dray; Albert R. Gnadt | Nature Energy | [10.1038/s41560-018-0294-x](https://doi.org/10.1038/s41560-018-0294-x) | 479 | GB,US |  | [link](https://openalex.org/W2902761272) |

**日本機関所属著者を含む論文** (上記 Top 20 のうち):

| Year | Title | JP Affiliation (raw) | DOI |
|---:|---|---|---|
| 2020 | A Survey of Autonomous Driving: <i>Common Practices and Emerging Technologies</i> | Nagoya University \|\| Nagoya University \|\| Nagoya University \|\| Nagoya University | [10.1109/access.2020.2983149](https://doi.org/10.1109/access.2020.2983149) |

### Milestones (academic evidence, n=13)

| Year | Tech | Type | Description | Evidence | Confidence | Status | DOI | source_url |
|---:|---|---|---|---|---:|---|---|---|
| 2017 | hyperloop | prototype | le magnetic levitation system prototype was implemented in the laboratory as a proof of concept in | academic_paper | 0.65 | observed | [10.1109/tie.2017.2777412](https://doi.org/10.1109/tie.2017.2777412) | [link](https://openalex.org/W2769072407) |
| 2017 | solid-state lidar | prototype | he best of our knowledge, the first demonstration of coherent solid-state light detection and ranging (LIDAR) | academic_paper | 0.75 | observed | [10.1364/ol.42.004091](https://doi.org/10.1364/ol.42.004091) | [link](https://openalex.org/W2761155850) |
| 2018 | eVTOL aircraft | commercial | ng aircraft or helicopters in commercial aviation, eVTOL aircraft have different flight dynamics, li | academic_paper | 0.65 | observed | [10.1109/dasc.2018.8569645](https://doi.org/10.1109/dasc.2018.8569645) | [link](https://openalex.org/W2905539157) |
| 2019 | hyperloop | commercial | design guidelines and examples for the commercialization version of the Hyperloop. At the end of the paper, in order to verify the propo | academic_paper_mid_citation | 0.51 | observed | [10.3390/en12244611](https://doi.org/10.3390/en12244611) | [link](https://openalex.org/W2993180743) |
| 2019 | solid-state lidar | prototype | early 200 m. In addition, the first demonstration of 3-D coherent LiDAR with optical phased arrays is present | academic_paper | 0.75 | observed | [10.1109/jstqe.2019.2908555](https://doi.org/10.1109/jstqe.2019.2908555) | [link](https://openalex.org/W2925745050) |
| 2019 | solid-state lidar | prototype | ible to realize since current demonstrated technologies would operate at untenable electrical power le | academic_paper | 0.75 | observed | [10.1364/optica.7.000003](https://doi.org/10.1364/optica.7.000003) | [link](https://openalex.org/W2996793380) |
| 2020 | solid-state lidar | mass_deployment | technology in use today. The commercially available 1D time of flight (TOF) LiDAR instrument is currently the m | academic_paper | 0.75 | observed | [10.3390/electronics9050741](https://doi.org/10.3390/electronics9050741) | [link](https://openalex.org/W3021999445) |
| 2021 | autonomous vehicle Waymo | mass_deployment | eriments are conducted on the widely used KITTI Dataset and the more recent Waymo Open Dataset. Our r | academic_paper | 0.75 | observed | [10.1609/aaai.v35i2.16207](https://doi.org/10.1609/aaai.v35i2.16207) | [link](https://openalex.org/W3118341329) |
| 2021 | hyperloop | prototype | the concept has not yet been demonstrated for subsonic or near-sonic speeds in large-scale implementa | academic_paper | 0.65 | observed | [10.1109/access.2021.3057788](https://doi.org/10.1109/access.2021.3057788) | [link](https://openalex.org/W3127517162) |
| 2021 | solid-state lidar | prototype | assisted beam-steering technology. As a proof-of-concept demonstration, with the design of a subwavelength-gap 1D long-emitter array and | academic_paper_mid_citation | 0.50 | observed | [10.1364/prj.424393](https://doi.org/10.1364/prj.424393) | [link](https://openalex.org/W3198152862) |
| 2022 | autonomous vehicle Waymo | prototype | Point Clouds Transformer has demonstrated promising performance in many 2D vision tasks. However, it | academic_paper | 0.75 | observed | [10.1109/cvpr52688.2022.00823](https://doi.org/10.1109/cvpr52688.2022.00823) | [link](https://openalex.org/W4312546175) |
| 2022 | solid-state lidar | prototype | -chip insertion loss. It represents the first demonstration of a fully integrated LiDAR transmitter on the multi-layer silicon-nitride-on-s | academic_paper_mid_citation | 0.52 | observed | [10.1109/jlt.2022.3204096](https://doi.org/10.1109/jlt.2022.3204096) | [link](https://openalex.org/W4294691581) |
| 2023 | eVTOL aircraft | commercial | pot for academic research and commercial application. This paper provides a comprehensive review of | academic_paper | 0.65 | observed | [10.1016/j.geits.2023.100140](https://doi.org/10.1016/j.geits.2023.100140) | [link](https://openalex.org/W4389003552) |

### Forecasts 2027-2100 (extracted from papers, n=10)

| Extracted Year | Tech | Evidence Phrase | Method | Confidence | Paper Year | DOI | source_url |
|---:|---|---|---|---:|---:|---|---|
| 2030 | eVTOL aircraft | on the central-European market and aimed to be released in 2030. The final configuration is a battery-powered tandem-wing a | regex_abstract_S3 | 0.70 | 2021 | [10.3390/app112311083](https://doi.org/10.3390/app112311083) | [link](https://openalex.org/W3215532339) |
| 2030 | eVTOL aircraft | revolutionary vehicles could be in commercial operations by 2030. These eVTOL systems could be ready for selected Public Ser | regex_abstract_S3 | 0.70 | 2021 |  | [link](https://openalex.org/W3203424024) |
| 2030 | hyperloop | operate in the forthcoming decade, Hyperloop is ... | decade_keyword | 0.50 | 2020 | [10.1016/j.trip.2020.100092](https://doi.org/10.1016/j.trip.2020.100092) | [link](https://openalex.org/W3004765755) |
| 2030 | hyperloop | all aspects of life in accordance with its ambitious vision 2030, especially in the field of sustainable passengers and frei | regex_abstract_S3 | 0.70 | 2022 | [10.53346/wjetr.2022.2.1.0032](https://doi.org/10.53346/wjetr.2022.2.1.0032) | [link](https://openalex.org/W4285904124) |
| 2037 | eVTOL aircraft | ubling of air transport passenger numbers to 8.2 billion by 2037 significant challenges are posed to the aviation industry. | regex_abstract_S3 | 0.70 | 2021 |  | [link](https://openalex.org/W3203424024) |
| 2040 | eVTOL aircraft | imited to 20 kW/kg whereas a goal of 80 kW/kg is stated for 2040. This paper systematically identifies the optimal BB dc-dc | regex_abstract_S3 | 0.70 | 2024 | [10.1109/tte.2024.3375026](https://doi.org/10.1109/tte.2024.3375026) | [link](https://openalex.org/W4392543716) |
| 2048 | solid-state lidar | coherent LiDAR engine has been demonstrated. Five identical 2048-channel driver chips flip onto a single silicon photonics L | regex_abstract_S3 | 0.70 | 2023 | [10.23919/vlsitechnologyandcir57934.2023.10185161](https://doi.org/10.23919/vlsitechnologyandcir57934.2023.10185161) | [link](https://openalex.org/W4385192516) |
| 2050 | hyperloop | on (EU), 90% of travel-related emissions will be omitted by 2050. To achieve this optimistic goal, one of the EU’s strategic | regex_abstract_S3 | 0.70 | 2021 | [10.1109/mele.2021.3115542](https://doi.org/10.1109/mele.2021.3115542) | [link](https://openalex.org/W4200570727) |
| 2080 | autonomous vehicle Waymo | rocessing rate, i.e., at a speed of 25 FPS on an NVIDIA RTX 2080 Ti GPU. The code is available at https://github.com/djiajun | regex_abstract_S3 | 0.70 | 2021 | [10.1609/aaai.v35i2.16207](https://doi.org/10.1609/aaai.v35i2.16207) | [link](https://openalex.org/W3118341329) |
| 2096 | eVTOL aircraft | View Video Presentation: https://doi.org/10.2514/6.2023-2096.vid By the second quarter of 2022, over 500 electric vertic | regex_abstract_S3 | 0.70 | 2023 | [10.2514/6.2023-2096](https://doi.org/10.2514/6.2023-2096) | [link](https://openalex.org/W4317634138) |

### TRL Trajectory (NASA TRL 1-9, n=9)

| Year | Tech | TRL | Evidence | Confidence | DOI | source_url |
|---:|---|---:|---|---:|---|---|
| 2025 | Airbus ZEROe | 4 | current_status='開発中' | 0.80 |  |  |
| 2025 | Joby Aviation | 7 | current_status='FAA認証中' | 0.80 |  |  |
| 2024 | Tesla FSD | 9 | current_status='商業段階' | 0.80 |  |  |
| 2024 | Waymo One | 9 | current_status='商業段階' | 0.80 |  |  |
| 2024 | autonomous vehicle Waymo | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | eVTOL aircraft | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | electric aviation | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | hyperloop | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | solid-state lidar | 7 | current_status='early_deployment' | 0.80 |  |  |

---

## MEDICAL - Medical/Neuro Engineering (医療・神経工学)

**Physical AI mapping**: ROBOTICS_HARDWARE (surgical) / SAFETY_AI

### Top 20 Cited Papers (citation_count desc)

| # | Year | Title | First Authors | Venue | DOI | Citations | Countries | JP authors? | source_url |
|---:|---:|---|---|---|---|---:|---|:---:|---|
| 1 | 2021 | Highly accurate protein structure prediction with AlphaFold | John Jumper; John Jumper; Richard Evans; Richard Evans; Alexander Pritzel | Nature | [10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2) | 43999 | GB,KR |  | [link](https://openalex.org/W3177828909) |
| 2 | 2021 | Highly accurate protein structure prediction with AlphaFold | John Jumper; John Jumper; Richard Evans; Richard Evans; Alexander Pritzel | Nature | [10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2) | 43999 | GB,KR |  | [link](https://openalex.org/W3177828909) |
| 3 | 2021 | Highly accurate protein structure prediction with AlphaFold | John Jumper; John Jumper; Richard Evans; Richard Evans; Alexander Pritzel | Nature | [10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2) | 43999 | GB,KR |  | [link](https://openalex.org/W3177828909) |
| 4 | 2020 | Safety and Efficacy of the BNT162b2 mRNA Covid-19 Vaccine | Fernando P. Polack; Stephen J. Thomas; Nicholas Kitchin; Judith Absalon; Alejandra Gurtman | New England Journal of Medicine | [10.1056/nejmoa2034577](https://doi.org/10.1056/nejmoa2034577) | 15391 | US,FR |  | [link](https://openalex.org/W3111255098) |
| 5 | 2010 | Scoping studies: advancing the methodology | Danielle Levac; Heather Colquhoun; Kelly K. O’Brien | Implementation Science | [10.1186/1748-5908-5-69](https://doi.org/10.1186/1748-5908-5-69) | 14389 | CA |  | [link](https://openalex.org/W2084154288) |
| 6 | 2015 | The Molecular Signatures Database Hallmark Gene Set Collection | Arthur Liberzon; Chet Birger; Helga Thorvaldsdóttir; Mahmoud Ghandi; Jill P. Mesirov | Cell Systems | [10.1016/j.cels.2015.12.004](https://doi.org/10.1016/j.cels.2015.12.004) | 14196 | US |  | [link](https://openalex.org/W2214074259) |
| 7 | 2024 | Accurate structure prediction of biomolecular interactions with AlphaFold 3 | Josh Abramson; Jonas Adler; Jack Dunger; Richard Evans; Tim Green | Nature | [10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w) | 12710 | GB,US,JP | YES | [link](https://openalex.org/W4396721167) |
| 8 | 2024 | Accurate structure prediction of biomolecular interactions with AlphaFold 3 | Josh Abramson; Jonas Adler; Jack Dunger; Richard Evans; Tim Green | Nature | [10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w) | 12710 | GB,US,JP | YES | [link](https://openalex.org/W4396721167) |
| 9 | 2012 | Safety, Activity, and Immune Correlates of Anti–PD-1 Antibody in Cancer | Suzanne L. Topalian; F. Stephen Hodi; Julie R. Brahmer; Scott Gettinger; David C. Smith | New England Journal of Medicine | [10.1056/nejmoa1200690](https://doi.org/10.1056/nejmoa1200690) | 12586 | US,IL |  | [link](https://openalex.org/W2160834915) |
| 10 | 2009 | TopHat: discovering splice junctions with RNA-Seq | Cole Trapnell; Lior Pachter; Steven L. Salzberg | Bioinformatics | [10.1093/bioinformatics/btp120](https://doi.org/10.1093/bioinformatics/btp120) | 12115 | US |  | [link](https://openalex.org/W2097065948) |
| 11 | 2020 | Efficacy and Safety of the mRNA-1273 SARS-CoV-2 Vaccine | Lindsey R. Baden; Hana M. El Sahly; Brandon Essink; Karen Kotloff; Sharon Frey | New England Journal of Medicine | [10.1056/nejmoa2035389](https://doi.org/10.1056/nejmoa2035389) | 10620 | US |  | [link](https://openalex.org/W3113734454) |
| 12 | 2015 | The Phyre2 web portal for protein modeling, prediction and analysis | Lawrence A. Kelley; Stefans Mezulis; Christopher M. Yates; Mark N. Wass; Michael J.E. Sternberg | Nature Protocols | [10.1038/nprot.2015.053](https://doi.org/10.1038/nprot.2015.053) | 10200 | GB |  | [link](https://openalex.org/W1803102843) |
| 13 | 2022 | ColabFold: making protein folding accessible to all | Milot Mirdita; Konstantin Schütze; Yoshitaka Moriwaki; Lim Heo; Sergey Ovchinnikov | Nature Methods | [10.1038/s41592-022-01488-1](https://doi.org/10.1038/s41592-022-01488-1) | 9465 | DE,KR,JP,US,PR,AM | YES | [link](https://openalex.org/W4281790889) |
| 14 | 2013 | The Cancer Genome Atlas Pan-Cancer analysis project | John N. Weinstein; Eric A Collisson; Gordon B. Mills; Kenna Shaw; Brad Ozenberger | Nature Genetics | [10.1038/ng.2764](https://doi.org/10.1038/ng.2764) | 9383 | US |  | [link](https://openalex.org/W2158485828) |
| 15 | 2020 | The STRING database in 2021: customizable protein–protein networks, and functional characterization of user-uploaded gene/measurement sets | Damian Szklarczyk; Annika L Gable; Katerina Nastou; David Lyon; Rebecca Kirsch | Nucleic Acids Research | [10.1093/nar/gkaa1074](https://doi.org/10.1093/nar/gkaa1074) | 8451 | CH,DK,FI,DE |  | [link](https://openalex.org/W3107527779) |
| 16 | 2018 | The MR-Base platform supports systematic causal inference across the human phenome | Gibran Hemani; Jie Zheng; Benjamin Elsworth; Kaitlin H. Wade; Valeriia Haberland | eLife | [10.7554/elife.34408](https://doi.org/10.7554/elife.34408) | 8285 | GB,AU,DE,US |  | [link](https://openalex.org/W2805983714) |
| 17 | 2009 | Gefitinib or Carboplatin–Paclitaxel in Pulmonary Adenocarcinoma | Tony Mok; Yi‐Long Wu; Sumitra Thongprasert; Chih-Hsin Yang; Da-Tong Chu | New England Journal of Medicine | [10.1056/nejmoa0810699](https://doi.org/10.1056/nejmoa0810699) | 8228 | HK,TH,TW,CN,JP,ID,GB | YES | [link](https://openalex.org/W2166084034) |
| 18 | 2021 | AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models | Mihály Váradi; Stephen Anyango; Mandar Deshpande; Sreenath Nair; Cindy Natassia | Nucleic Acids Research | [10.1093/nar/gkab1061](https://doi.org/10.1093/nar/gkab1061) | 8114 | GB |  | [link](https://openalex.org/W3211795435) |
| 19 | 2021 | AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models | Mihály Váradi; Stephen Anyango; Mandar Deshpande; Sreenath Nair; Cindy Natassia | Nucleic Acids Research | [10.1093/nar/gkab1061](https://doi.org/10.1093/nar/gkab1061) | 8114 | GB |  | [link](https://openalex.org/W3211795435) |
| 20 | 2021 | Inference and analysis of cell-cell communication using CellChat | Suoqin Jin; Christian F. Guerrero‐Juarez; Lihua Zhang; Ivan Chang; Raúl Ramos | Nature Communications | [10.1038/s41467-021-21246-9](https://doi.org/10.1038/s41467-021-21246-9) | 8019 | US,TW |  | [link](https://openalex.org/W3132661792) |

**日本機関所属著者を含む論文** (上記 Top 20 のうち):

| Year | Title | JP Affiliation (raw) | DOI |
|---:|---|---|---|
| 2024 | Accurate structure prediction of biomolecular interactions with AlphaFold 3 | Industrial Research Institute of Ishikawa | [10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w) |
| 2024 | Accurate structure prediction of biomolecular interactions with AlphaFold 3 | Industrial Research Institute of Ishikawa | [10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w) |
| 2022 | ColabFold: making protein folding accessible to all | The University of Tokyo | [10.1038/s41592-022-01488-1](https://doi.org/10.1038/s41592-022-01488-1) |
| 2009 | Gefitinib or Carboplatin–Paclitaxel in Pulmonary Adenocarcinoma | National Cancer Center Hospital East \|\| National Hospital Organization Kyushu Cancer Center \|\| National Cancer Center Hospital East \|\| Tokyo National Hosp | [10.1056/nejmoa0810699](https://doi.org/10.1056/nejmoa0810699) |

### Milestones (academic evidence, n=15)

| Year | Tech | Type | Description | Evidence | Confidence | Status | DOI | source_url |
|---:|---|---|---|---|---:|---|---|---|
| 2014 | CAR-T cell therapy | prototype | ese results, we are opening a phase 1 clinical trial to evaluate the safety of intrapleural administration of me | academic_paper | 0.75 | observed | [10.1126/scitranslmed.3010162](https://doi.org/10.1126/scitranslmed.3010162) | [link](https://openalex.org/W2169876627) |
| 2017 | CAR-T cell therapy | prototype | enografts in vivo. This study demonstrates improved therapeutic efficacy of Cas9-edited CAR T cells an | academic_paper | 0.75 | observed | [10.1038/s41598-017-00462-8](https://doi.org/10.1038/s41598-017-00462-8) | [link](https://openalex.org/W2604982880) |
| 2018 | CAR-T cell therapy | pilot | First-in-Human CLL1-CD33 Compound CAR T Cell Therapy Induces Complete Remission in Patients wi | academic_paper_mid_citation | 0.54 | observed | [10.1182/blood-2018-99-110579](https://doi.org/10.1182/blood-2018-99-110579) | [link](https://openalex.org/W2898640974) |
| 2019 | CAR-T cell therapy | commercial | aggressive B cell Lymphomas leading to FDA approval of axicabtagene ciloleucel and tisagenlecleucel. While long-term remission rate | academic_paper_mid_citation | 0.52 | observed | [10.1080/10428194.2019.1697814](https://doi.org/10.1080/10428194.2019.1697814) | [link](https://openalex.org/W2992091473) |
| 2020 | CAR-T cell therapy | commercial | We treated ten patients with DLBCL post-FDA approval in an inner-city tertiary center in the Bronx. Eight patients (80%) had receive | academic_paper_mid_citation | 0.57 | observed | [10.1186/s13045-019-0838-y](https://doi.org/10.1186/s13045-019-0838-y) | [link](https://openalex.org/W3000719174) |
| 2022 | AlphaFold protein | mass_deployment | for 3D protein structure comparison is widely used by crystallographers to relate new structures to pre-existing ones. Here, we re | academic_paper_high_citation | 0.80 | observed | [10.1093/nar/gkac387](https://doi.org/10.1093/nar/gkac387) | [link](https://openalex.org/W4282922306) |
| 2022 | AlphaFold protein | mass_deployment | putational docking approaches have been widely used to predict drug binding targets; yet, such approaches depend on existing protei | academic_paper_mid_citation | 0.59 | observed | [10.15252/msb.202211081](https://doi.org/10.15252/msb.202211081) | [link](https://openalex.org/W4294719209) |
| 2022 | AlphaFold protein | prototype | tions MOTIVATION: After the outstanding breakthrough of AlphaFold in predicting protein 3D models, new questions appeared and remain | academic_paper_mid_citation | 0.57 | observed | [10.1093/bioinformatics/btac202](https://doi.org/10.1093/bioinformatics/btac202) | [link](https://openalex.org/W4225552973) |
| 2022 | AlphaFold protein | mass_deployment | odeling methods for GPCRs with the most widely used template-based software-Modeller. We collected the experimentally determined st | academic_paper_mid_citation | 0.53 | observed | [10.1093/bib/bbac308](https://doi.org/10.1093/bib/bbac308) | [link](https://openalex.org/W4292458166) |
| 2023 | gene editing therapy | pilot | art-1 clinical trial ( NCT05398029) , a first-in-human phase 1b, open-label study, was designed to assess the safety and tolerability | academic_paper_mid_citation | 0.51 | observed | [10.1093/ehjcvp/pvad103](https://doi.org/10.1093/ehjcvp/pvad103) | [link](https://openalex.org/W4390172480) |
| 2023 | AlphaFold protein | mass_deployment | ns differed from experimental maps on a global scale through distortion and domain orientation, and on a local scale in backbone and | academic_paper_mid_citation | 0.62 | observed | [10.1038/s41592-023-02087-4](https://doi.org/10.1038/s41592-023-02087-4) | [link](https://openalex.org/W4389174567) |
| 2023 | AlphaFold protein | proposal | rated sequences to adopt a target fold. Initial design trials resulted in de novo designs with an overrepresentation of hydrophobic re | academic_paper_mid_citation | 0.52 | observed | [10.1002/pro.4653](https://doi.org/10.1002/pro.4653) | [link](https://openalex.org/W4376131109) |
| 2023 | AlphaFold protein | mass_deployment | neration (FSAMG) method outperforms the widely used sequence alignment-based multimer structure generation. | academic_paper_mid_citation | 0.51 | observed | [10.1038/s42003-023-05525-3](https://doi.org/10.1038/s42003-023-05525-3) | [link](https://openalex.org/W4388571183) |
| 2024 | CAR-T cell therapy | pilot | cies. We report results from a phase 1, first-in-human study of prostate stem cell antigen (PSCA)-directed CAR T cells in men with mCR | academic_paper_mid_citation | 0.53 | observed | [10.1038/s41591-024-02979-8](https://doi.org/10.1038/s41591-024-02979-8) | [link](https://openalex.org/W4399578578) |
| 2024 | AlphaFold protein | mass_deployment | ace Topography of proteins (CASTp) is a widely used web server for locating, delineating, and measuring these geometric and topolog | academic_paper_mid_citation | 0.53 | observed | [10.1093/nar/gkae415](https://doi.org/10.1093/nar/gkae415) | [link](https://openalex.org/W4398761928) |

### Forecasts 2027-2100 (extracted from papers, n=7)

| Extracted Year | Tech | Evidence Phrase | Method | Confidence | Paper Year | DOI | source_url |
|---:|---|---|---|---:|---:|---|---|
| 2030 | Casgevy | a’s National Mission to Eliminate Sickle Cell Anaemia (2023–2030) further highlights this development. Through large-scale s | regex_abstract_S3 | 0.70 | 2025 | [10.4103/ijpmmm.ijpmmm_9_25](https://doi.org/10.4103/ijpmmm.ijpmmm_9_25) | [link](https://openalex.org/W7114925367) |
| 2030 | AlphaFold protein | 1.8 billion in 2023, is projected to reach $13.1 billion by 2030, reflecting a compound annual growth rate of 18.8%. Landmar | regex_abstract_S3 | 0.70 | 2025 | [10.1007/s44345-025-00037-5](https://doi.org/10.1007/s44345-025-00037-5) | [link](https://openalex.org/W7114905274) |
| 2030 | Casgevy sickle cell | a’s National Mission to Eliminate Sickle Cell Anaemia (2023–2030) further highlights this development. Through large-scale s | regex_abstract_S3 | 0.70 | 2025 | [10.4103/ijpmmm.ijpmmm_9_25](https://doi.org/10.4103/ijpmmm.ijpmmm_9_25) | [link](https://openalex.org/W7114925367) |
| 2035 | Casgevy | lobal gene editing market projected to reach $45 billion by 2035 , understanding this technology's capabilities, limitations | regex_abstract_S3 | 0.70 | 2026 | [10.5281/zenodo.19721379](https://doi.org/10.5281/zenodo.19721379) | [link](https://openalex.org/W7155556894) |
| 2035 | Casgevy | lobal gene editing market projected to reach $45 billion by 2035 , understanding this technology's capabilities, limitations | regex_abstract_S3 | 0.70 | 2026 | [10.5281/zenodo.19721380](https://doi.org/10.5281/zenodo.19721380) | [link](https://openalex.org/W7155509181) |
| 2035 | Casgevy sickle cell | lobal gene editing market projected to reach $45 billion by 2035 , understanding this technology's capabilities, limitations | regex_abstract_S3 | 0.70 | 2026 | [10.5281/zenodo.19721379](https://doi.org/10.5281/zenodo.19721379) | [link](https://openalex.org/W7155556894) |
| 2035 | Casgevy sickle cell | lobal gene editing market projected to reach $45 billion by 2035 , understanding this technology's capabilities, limitations | regex_abstract_S3 | 0.70 | 2026 | [10.5281/zenodo.19721380](https://doi.org/10.5281/zenodo.19721380) | [link](https://openalex.org/W7155509181) |

### TRL Trajectory (NASA TRL 1-9, n=11)

| Year | Tech | TRL | Evidence | Confidence | DOI | source_url |
|---:|---|---:|---|---:|---|---|
| 2024 | AlphaFold 3 | 9 | current_status='一般公開' | 0.80 |  |  |
| 2024 | AlphaFold protein | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | CAR-T cell therapy | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2023 | Casgevy | 9 | current_status='FDA承認' | 0.80 |  |  |
| 2024 | Casgevy sickle cell | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | Emulate organ-on-chip | 9 | current_status='商業段階' | 0.80 |  |  |
| 2024 | Intel Loihi 2 Hala Point | 6 | current_status='実証段階' | 0.80 |  |  |
| 2024 | Neuralink N1 | 6 | current_status='臨床試験' | 0.80 |  |  |
| 2024 | Synchron | 6 | current_status='臨床試験' | 0.80 |  |  |
| 2024 | gene editing therapy | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | mRNA vaccine | 7 | current_status='early_deployment' | 0.80 |  |  |

---

## BUILDING - Construction/Urban (建築・都市)

**Physical AI mapping**: CYBER_PHYS / SIM_DATA

### Top 20 Cited Papers (citation_count desc)

| # | Year | Title | First Authors | Venue | DOI | Citations | Countries | JP authors? | source_url |
|---:|---:|---|---|---|---|---:|---|:---:|---|
| 1 | 2017 | 3D printing of high-strength aluminium alloys | John H. Martin; Brennan D. Yahata; Jacob M. Hundley; Justin A. Mayer; Tobias A. Schaedler | Nature | [10.1038/nature23894](https://doi.org/10.1038/nature23894) | 2832 | US |  | [link](https://openalex.org/W2758567842) |
| 2 | 2016 | A 3D bioprinting system to produce human-scale tissue constructs with structural integrity | Hyun‐Wook Kang; Sang Jin Lee; In Kap Ko; Carlos Kengla; James J. Yoo | Nature Biotechnology | [10.1038/nbt.3413](https://doi.org/10.1038/nbt.3413) | 2577 | US |  | [link](https://openalex.org/W2286771936) |
| 3 | 2009 | Application of bacteria as self-healing agent for the development of sustainable concrete | H.M. Jonkers; A. P. Thijssen; Gerard Muyzer; Oğuzhan Çopuroğlu; Erik Schlangen | Ecological Engineering | [10.1016/j.ecoleng.2008.12.036](https://doi.org/10.1016/j.ecoleng.2008.12.036) | 1497 | NL |  | [link](https://openalex.org/W2167152710) |
| 4 | 2011 | Quantification of crack-healing in novel bacteria-based self-healing concrete | Virginie Wiktor; H.M. Jonkers | Cement and Concrete Composites | [10.1016/j.cemconcomp.2011.03.012](https://doi.org/10.1016/j.cemconcomp.2011.03.012) | 1122 | NL |  | [link](https://openalex.org/W2054780633) |
| 5 | 2011 | Quantification of crack-healing in novel bacteria-based self-healing concrete | Virginie Wiktor; H.M. Jonkers | Cement and Concrete Composites | [10.1016/j.cemconcomp.2011.03.012](https://doi.org/10.1016/j.cemconcomp.2011.03.012) | 1122 | NL |  | [link](https://openalex.org/W2054780633) |
| 6 | 2013 | The 3D printing of gelatin methacrylamide cell-laden tissue-engineered constructs with high cell viability | Thomas Billiet; Elien Gevaert; Thomas De Schryver; Maria Cornelissen; Peter Dubruel | Biomaterials | [10.1016/j.biomaterials.2013.09.078](https://doi.org/10.1016/j.biomaterials.2013.09.078) | 1010 | BE |  | [link](https://openalex.org/W2034722366) |
| 7 | 2013 | Self-healing concrete by use of microencapsulated bacterial spores | J.Y. Wang; H. Soens; Willy Verstraete; Nele De Belie | Cement and Concrete Research | [10.1016/j.cemconres.2013.11.009](https://doi.org/10.1016/j.cemconres.2013.11.009) | 1005 | BE |  | [link](https://openalex.org/W1988374761) |
| 8 | 2013 | Self-healing concrete by use of microencapsulated bacterial spores | J.Y. Wang; H. Soens; Willy Verstraete; Nele De Belie | Cement and Concrete Research | [10.1016/j.cemconres.2013.11.009](https://doi.org/10.1016/j.cemconres.2013.11.009) | 1005 | BE |  | [link](https://openalex.org/W1988374761) |
| 9 | 2007 | Three-dimensional photonic metamaterials at optical frequencies | Na Liu; Hongcang Guo; Liwei Fu; S. Kaiser; H. Schweizer | Nature Materials | [10.1038/nmat2072](https://doi.org/10.1038/nmat2072) | 912 | DE |  | [link](https://openalex.org/W2145664580) |
| 10 | 2015 | Multimaterial magnetically assisted 3D printing of composite materials | Dimitri Kokkinis; Manuel Schaffner; André R. Studart | Nature Communications | [10.1038/ncomms9643](https://doi.org/10.1038/ncomms9643) | 835 | CH |  | [link](https://openalex.org/W2176655155) |
| 11 | 2011 | Use of silica gel or polyurethane immobilized bacteria for self-healing concrete | Jianyun Wang; Kim Van Tittelboom; Nele De Belie; Willy Verstraete | Construction and Building Materials | [10.1016/j.conbuildmat.2011.06.054](https://doi.org/10.1016/j.conbuildmat.2011.06.054) | 737 | BE |  | [link](https://openalex.org/W1979661313) |
| 12 | 2011 | Use of silica gel or polyurethane immobilized bacteria for self-healing concrete | Jianyun Wang; Kim Van Tittelboom; Nele De Belie; Willy Verstraete | Construction and Building Materials | [10.1016/j.conbuildmat.2011.06.054](https://doi.org/10.1016/j.conbuildmat.2011.06.054) | 737 | BE |  | [link](https://openalex.org/W1979661313) |
| 13 | 2016 | Supercapacitors Based on Three-Dimensional Hierarchical Graphene Aerogels with Periodic Macropores | Cheng Zhu; Tianyu Liu; Fang Qian; T. Yong-Jin Han; Eric B. Duoss | Nano Letters | [10.1021/acs.nanolett.5b04965](https://doi.org/10.1021/acs.nanolett.5b04965) | 710 | US |  | [link](https://openalex.org/W2257143226) |
| 14 | 2009 | Human microvasculature fabrication using thermal inkjet printing technology | Xiaofeng Cui; Thomas Boland | Biomaterials | [10.1016/j.biomaterials.2009.07.056](https://doi.org/10.1016/j.biomaterials.2009.07.056) | 691 | US |  | [link](https://openalex.org/W1967696528) |
| 15 | 2019 | Hardened properties of 3D printed concrete: The influence of process parameters on interlayer adhesion | Rob Wolfs; Freek Bos; T.A.M. Salet | Cement and Concrete Research | [10.1016/j.cemconres.2019.02.017](https://doi.org/10.1016/j.cemconres.2019.02.017) | 681 | NL |  | [link](https://openalex.org/W2921177911) |
| 16 | 2015 | Crack healing in concrete using various bio influenced self-healing techniques | Wasim Khaliq; Muhammad Basit Ehsan | Construction and Building Materials | [10.1016/j.conbuildmat.2015.11.006](https://doi.org/10.1016/j.conbuildmat.2015.11.006) | 650 | PK |  | [link](https://openalex.org/W2174971616) |
| 17 | 2018 | Effect of surface moisture on inter-layer strength of 3D printed concrete | Jay Sanjayan; Behzad Nematollahi; Ming Xia; Taylor Marchment | Construction and Building Materials | [10.1016/j.conbuildmat.2018.03.232](https://doi.org/10.1016/j.conbuildmat.2018.03.232) | 622 | AU |  | [link](https://openalex.org/W2796304963) |
| 18 | 2017 | Fresh and hardened properties of 3D printable cementitious materials for building and construction | Suvash Chandra Paul; Yi Wei Daniel Tay; Biranchi Panda; Ming Jen Tan | Archives of Civil and Mechanical Engineering | [10.1016/j.acme.2017.02.008](https://doi.org/10.1016/j.acme.2017.02.008) | 597 | SG |  | [link](https://openalex.org/W2753713612) |
| 19 | 2014 | Application of hydrogel encapsulated carbonate precipitating bacteria for approaching a realistic self-healing in concrete | J.Y. Wang; Didier Snoeck; Sandra Van Vlierberghe; Willy Verstraete; Nele De Belie | Construction and Building Materials | [10.1016/j.conbuildmat.2014.06.018](https://doi.org/10.1016/j.conbuildmat.2014.06.018) | 571 | BE |  | [link](https://openalex.org/W2006956023) |
| 20 | 2018 | Generation of human brain region–specific organoids using a miniaturized spinning bioreactor | Xuyu Qian; Fadi Jacob; Mingxi M. Song; Ha Nam Nguyen; Hongjun Song | Nature Protocols | [10.1038/nprot.2017.152](https://doi.org/10.1038/nprot.2017.152) | 516 | US |  | [link](https://openalex.org/W2788035610) |

### Milestones (academic evidence, n=7)

| Year | Tech | Type | Description | Evidence | Confidence | Status | DOI | source_url |
|---:|---|---|---|---|---:|---|---|---|
| 2015 | mass timber construction | prototype | s timber construction clearly demonstrates some advantages including cost savings, primarily in the re | academic_paper | 0.65 | observed | [10.1179/2042645315y.0000000010](https://doi.org/10.1179/2042645315y.0000000010) | [link](https://openalex.org/W1587748750) |
| 2016 | self-healing concrete | prototype | e over glass capsules used up to now as proof-of-concept carriers in self-healing concrete. They allow easier processing and afford the | academic_paper_mid_citation | 0.50 | observed | [10.3390/ma10010010](https://doi.org/10.3390/ma10010010) | [link](https://openalex.org/W2566472372) |
| 2017 | self-healing concrete | prototype | ncrete: synthesis, characterisation and proof of concept Microcapsules, with sodium silicate solution as core, were produced using compl | academic_paper_mid_citation | 0.56 | observed | [10.1088/1361-665x/aa516c](https://doi.org/10.1088/1361-665x/aa516c) | [link](https://openalex.org/W2595232665) |
| 2019 | self-healing concrete | mass_deployment | rubber particles have potential to be a widely used bacteria carrier for practical engineering applications in self-healing concret | academic_paper_mid_citation | 0.52 | observed | [10.3390/ma12142313](https://doi.org/10.3390/ma12142313) | [link](https://openalex.org/W2963718757) |
| 2020 | self-healing concrete | commercial | rete with macrocapsules Development and commercialization of self-healing concrete is hampered due to a lack of standardized test methods | academic_paper_mid_citation | 0.51 | observed | [10.1080/14686996.2020.1814117](https://doi.org/10.1080/14686996.2020.1814117) | [link](https://openalex.org/W3080928493) |
| 2020 | self-healing concrete | prototype | From waste to self-healing concrete: A proof-of-concept of a new application for polyhydroxyalkanoate Polyhydroxyalkanoate (PHA) produc | academic_paper_mid_citation | 0.50 | observed | [10.1016/j.resconrec.2020.105206](https://doi.org/10.1016/j.resconrec.2020.105206) | [link](https://openalex.org/W3092248963) |
| 2023 | building integrated photovoltaic | commercial | and what stands in the way to commercialisation and market penetration?. | academic_paper | 0.65 | observed | [10.1039/d3ee00331k](https://doi.org/10.1039/d3ee00331k) | [link](https://openalex.org/W4383568237) |

### Forecasts 2027-2100 (extracted from papers, n=3)

| Extracted Year | Tech | Evidence Phrase | Method | Confidence | Paper Year | DOI | source_url |
|---:|---|---|---|---:|---:|---|---|
| 2050 | mass timber construction | e Development Goals (SDGs) and global net-zero emissions by 2050. Despite the slow adoption of mass timber construction (MTC | regex_abstract_S3 | 0.70 | 2022 | [10.3390/buildings12091405](https://doi.org/10.3390/buildings12091405) | [link](https://openalex.org/W4295106728) |
| 2050 | mass timber construction | imate change. According to a United Nations report, (17) by 2050, more than 7 billion people will move to cities. The rapid | regex_abstract_S3 | 0.70 | 2022 | [10.35940/ijitee.g9107.0611722](https://doi.org/10.35940/ijitee.g9107.0611722) | [link](https://openalex.org/W4283074680) |
| 2050 | building integrated photovoltaic | s set for greenhouse gas emissions and energy efficiency by 2050 demand a critical increase of building renovation rates. Th | regex_abstract_S3 | 0.70 | 2024 | [10.1016/j.jobe.2024.110486](https://doi.org/10.1016/j.jobe.2024.110486) | [link](https://openalex.org/W4401821991) |

### TRL Trajectory (NASA TRL 1-9, n=7)

| Year | Tech | TRL | Evidence | Confidence | DOI | source_url |
|---:|---|---:|---|---:|---|---|
| 2024 | 3D printed building | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | Helsinki 3D+ | 9 | current_status='稼働中' | 0.80 |  |  |
| 2024 | ICON Phoenix | 9 | current_status='商業段階' | 0.80 |  |  |
| 2019 | Mjøstårnet | 9 | current_status='稼働中' | 0.80 |  |  |
| 2024 | building integrated photovoltaic | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | mass timber construction | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | self-healing concrete | 7 | current_status='early_deployment' | 0.80 |  |  |

---

## CROSS - Cross-domain (横断観察)

**Physical AI mapping**: VLM_FOUNDATION / SIM_DATA

### Top 20 Cited Papers (citation_count desc)

| # | Year | Title | First Authors | Venue | DOI | Citations | Countries | JP authors? | source_url |
|---:|---:|---|---|---|---|---:|---|:---:|---|
| 1 | 2016 | XGBoost | Tianqi Chen; Carlos Guestrin |  | [10.1145/2939672.2939785](https://doi.org/10.1145/2939672.2939785) | 46944 | US |  | [link](https://openalex.org/W2295598076) |
| 2 | 2012 | An integrated encyclopedia of DNA elements in the human genome | Sylvain Foissac | Nature | [10.1038/nature11247](https://doi.org/10.1038/nature11247) | 19275 | FR |  | [link](https://openalex.org/W2259938310) |
| 3 | 2018 | Minimap2: pairwise alignment for nucleotide sequences | Heng Li | Bioinformatics | [10.1093/bioinformatics/bty191](https://doi.org/10.1093/bioinformatics/bty191) | 16427 | US |  | [link](https://openalex.org/W2789843538) |
| 4 | 2013 | Commentary: The Materials Project: A materials genome approach to accelerating materials innovation | Anubhav Jain; Shyue Ping Ong; Geoffroy Hautier; Wei Chen; William D. Richards | APL Materials | [10.1063/1.4812323](https://doi.org/10.1063/1.4812323) | 12407 | US,BE |  | [link](https://openalex.org/W1992985800) |
| 5 | 2013 | Internet of Things (IoT): A vision, architectural elements, and future directions | Jayavardhana Gubbi; Rajkumar Buyya; Slaven Marusic; Marimuthu Palaniswami | Future Generation Computer Systems | [10.1016/j.future.2013.01.010](https://doi.org/10.1016/j.future.2013.01.010) | 11888 | AU |  | [link](https://openalex.org/W2111619626) |
| 6 | 2012 | Evaluation of general 16S ribosomal RNA gene PCR primers for classical and next-generation sequencing-based diversity studies | Anna Klindworth; Elmar Pruesse; Timmy Schweer; Jörg Peplies; Christian Quast | Nucleic Acids Research | [10.1093/nar/gks808](https://doi.org/10.1093/nar/gks808) | 8870 | DE,AT |  | [link](https://openalex.org/W2115701239) |
| 7 | 2013 | The International Classification of Headache Disorders, 3rd edition (beta version) | Ettlin, Dominik A | Cephalalgia | [10.1177/0333102413485658](https://doi.org/10.1177/0333102413485658) | 8196 |  |  | [link](https://openalex.org/W2769724041) |
| 8 | 2016 | Global, regional, and national comparative risk assessment of 79 behavioural, environmental and occupational, and metabolic risks or clusters of risks, 1990–2015: a systematic analysis for the Global Burden of Disease Study 2015 | Mohammad H. Forouzanfar; Ashkan Afshin; Lily Alexander; H Ross Anderson; Zulfiqar A Bhutta | The Lancet | [10.1016/s0140-6736(16)31679-8](https://doi.org/10.1016/s0140-6736(16)31679-8) | 7769 | US,GB,IR,HK,NO,IT,TR,EG,BH,DE,PS,GH,ES,BD,UY,ET,SE,CO,NG,CH,PH,CA |  | [link](https://openalex.org/W1617145133) |
| 9 | 2017 | Massively parallel digital transcriptional profiling of single cells | Grace Zheng; Jessica M. Terry; Phillip Belgrader; Paul Ryvkin; Zachary Bent | Nature Communications | [10.1038/ncomms14049](https://doi.org/10.1038/ncomms14049) | 7676 | US |  | [link](https://openalex.org/W2951506174) |
| 10 | 2021 | Review of deep learning: concepts, CNN architectures, challenges, applications, future directions | Laith Alzubaidi; Jinglan Zhang; Amjad J. Humaidi; Ayad Q. Al-Dujaili; Ye Duan | Journal Of Big Data | [10.1186/s40537-021-00444-8](https://doi.org/10.1186/s40537-021-00444-8) | 7395 | AU,IQ,US,ES,GB |  | [link](https://openalex.org/W3140854437) |
| 11 | 2020 | The IntCal20 Northern Hemisphere Radiocarbon Age Calibration Curve (0–55 cal kBP) | Paula Reimer; William E. N. Austin; Édouard Bard; Alex Bayliss; Paul G. Blackwell | Radiocarbon | [10.1017/rdc.2020.41](https://doi.org/10.1017/rdc.2020.41) | 7389 | GB,FR,DE,US,CN,NZ,SE,AU,NL,CH,CZ,DK,JP,IT | YES | [link](https://openalex.org/W3015391807) |
| 12 | 2008 | Exploring Network Structure, Dynamics, and Function using NetworkX | Aric Hagberg; Dan Schult; Pieter J. Swart | Proceedings of the Python in Science Conferences | [10.25080/tcwv9851](https://doi.org/10.25080/tcwv9851) | 7272 | US |  | [link](https://openalex.org/W2132022337) |
| 13 | 2015 | Integrative analysis of 111 reference human epigenomes | Anshul Kundaje; Wouter Meuleman; Jason Ernst; Misha Bilenky; Angela Yen | Nature | [10.1038/nature14248](https://doi.org/10.1038/nature14248) | 7068 | US,CA,MX,HR,AU |  | [link](https://openalex.org/W2076154138) |
| 14 | 2021 | 2021 ESC Guidelines on cardiovascular disease prevention in clinical practice | Frank L.J. Visseren; François Mach; Yvo M. Smulders; David Carballo; Konstantinos C. Koskinas | European Heart Journal | [10.1093/eurheartj/ehab484](https://doi.org/10.1093/eurheartj/ehab484) | 6093 | CH,BE,CN,SE,IT,GB,DE |  | [link](https://openalex.org/W3197233987) |
| 15 | 2016 | A survey of transfer learning | Karl R. Weiss; Taghi M. Khoshgoftaar; Dingding Wang | Journal Of Big Data | [10.1186/s40537-016-0043-6](https://doi.org/10.1186/s40537-016-0043-6) | 6083 | US |  | [link](https://openalex.org/W2395579298) |
| 16 | 2007 | The Human Microbiome Project | Peter J. Turnbaugh; Ruth E. Ley; Micah Hamady; Claire M. Fraser; Rob Knight | Nature | [10.1038/nature06244](https://doi.org/10.1038/nature06244) | 6067 | US |  | [link](https://openalex.org/W2131186249) |
| 17 | 2014 | Changes in the global value of ecosystem services | Robert Costanza; R.S. de Groot; Paul C. Sutton; Sander van der Ploeg; Sharolyn Anderson | Global Environmental Change | [10.1016/j.gloenvcha.2014.04.002](https://doi.org/10.1016/j.gloenvcha.2014.04.002) | 6032 | AU,NL,US,GB |  | [link](https://openalex.org/W2130509491) |
| 18 | 2012 | Differential expression analysis of multifactor RNA-Seq experiments with respect to biological variation | Davis J. McCarthy; Yunshun Chen; Gordon K. Smyth | Nucleic Acids Research | [10.1093/nar/gks042](https://doi.org/10.1093/nar/gks042) | 5799 | AU |  | [link](https://openalex.org/W2130116522) |
| 19 | 2007 | Typology of sociotechnical transition pathways | Frank W. Geels; Johan Schot | Research Policy | [10.1016/j.respol.2007.01.003](https://doi.org/10.1016/j.respol.2007.01.003) | 4954 | NL |  | [link](https://openalex.org/W2156304718) |
| 20 | 2019 | The global landscape of AI ethics guidelines | Anna Jobin; Marcello Ienca; Effy Vayena | Nature Machine Intelligence | [10.1038/s42256-019-0088-2](https://doi.org/10.1038/s42256-019-0088-2) | 4798 | CH |  | [link](https://openalex.org/W2953522645) |

**日本機関所属著者を含む論文** (上記 Top 20 のうち):

| Year | Title | JP Affiliation (raw) | DOI |
|---:|---|---|---|
| 2020 | The IntCal20 Northern Hemisphere Radiocarbon Age Calibration Curve (0–55 cal kBP) | Nagoya University \|\| National Museum of Japanese History | [10.1017/rdc.2020.41](https://doi.org/10.1017/rdc.2020.41) |

### Milestones (academic evidence, n=4)

| Year | Tech | Type | Description | Evidence | Confidence | Status | DOI | source_url |
|---:|---|---|---|---|---:|---|---|---|
| 2010 | responsible innovation | pilot | Responsible Innovation: A Pilot Study with the U.K. Engineering and Physical Sciences Research Council Significant ti | academic_paper_mid_citation | 0.55 | observed | [10.1111/j.1539-6924.2010.01517.x](https://doi.org/10.1111/j.1539-6924.2010.01517.x) | [link](https://openalex.org/W1948761388) |
| 2011 | innovation diffusion | pilot | odes of enquiry. This is done through a pilot study consisting of chartered professionals and then through a case study organizatio | academic_paper_mid_citation | 0.51 | observed | [10.1080/01446193.2011.619994](https://doi.org/10.1080/01446193.2011.619994) | [link](https://openalex.org/W2082005297) |
| 2019 | responsible innovation | commercial | ge of the innovation process—during the market launch. To some extent, this allows for the adaptation of the solution, but such adapt | academic_paper_mid_citation | 0.52 | observed | [10.3390/su11061766](https://doi.org/10.3390/su11061766) | [link](https://openalex.org/W2924765230) |
| 2021 | innovation diffusion | proposal | nnovation diffusion theory Since it was first proposed by Christensen, disruptive innovation theory has provoked considerable debate i | academic_paper_mid_citation | 0.51 | observed | [10.1080/09537325.2021.1901873](https://doi.org/10.1080/09537325.2021.1901873) | [link](https://openalex.org/W3137988093) |

### Forecasts 2027-2100 (extracted from papers, n=18)

| Extracted Year | Tech | Evidence Phrase | Method | Confidence | Paper Year | DOI | source_url |
|---:|---|---|---|---:|---:|---|---|
| 2030 | technology foresight | Energy Technology Foresight 2030 in Russia: An Outlook for Saf | regex_year | 0.60 | 2015 | [10.1016/j.egypro.2015.07.550](https://doi.org/10.1016/j.egypro.2015.07.550) | [link](https://openalex.org/W1909747894) |
| 2030 | technology foresight | ce and Technology Foresight – 2030: Key Features and First Resul | regex_year | 0.60 | 2012 | [10.17323/1995-459x.2012.1.12.25](https://doi.org/10.17323/1995-459x.2012.1.12.25) | [link](https://openalex.org/W1966653287) |
| 2030 | technology foresight | RUSSIA 2030: SCIENCE AND TECHNOLOGY FORES | regex_year | 0.60 | 2016 |  | [link](https://openalex.org/W2767185897) |
| 2030 | technology foresight | Russia 2030: Science and Technology Fores | regex_year | 0.60 | 2019 | [10.1134/s1075700719030080](https://doi.org/10.1134/s1075700719030080) | [link](https://openalex.org/W2947291929) |
| 2030 | technology foresight | or development in Poland till 2030. Delphi survey as... | regex_year | 0.60 | 2008 | [10.1016/j.techfore.2008.05.007](https://doi.org/10.1016/j.techfore.2008.05.007) | [link](https://openalex.org/W2017696766) |
| 2030 | technology foresight | aper examines the energy block of the Russian S&T Foresight 2030, developed by experts in 2011-2013 and approved by the Prim | regex_abstract_S3 | 0.70 | 2015 | [10.1016/j.egypro.2015.07.550](https://doi.org/10.1016/j.egypro.2015.07.550) | [link](https://openalex.org/W1909747894) |
| 2030 | technology foresight | rcise, the prospect of future Korean society up to the year 2030 was developed. The exercise was designed to widen the parti | regex_abstract_S3 | 0.70 | 2010 | [10.1504/ijfip.2010.032672](https://doi.org/10.1504/ijfip.2010.032672) | [link](https://openalex.org/W2012898825) |
| 2030 | technology foresight | A brief analysis of the draft document “Russia 2030: Science and Technology Foresight” (of December 19, 2017) i | regex_abstract_S3 | 0.70 | 2019 | [10.1134/s1075700719030080](https://doi.org/10.1134/s1075700719030080) | [link](https://openalex.org/W2947291929) |
| 2030 | technology foresight | exercise, the prospect of future Korean society up to Year 2030 was developed. Then, future demands and needs based on the | regex_abstract_S3 | 0.70 | 2006 | [10.1109/picmet.2006.296712](https://doi.org/10.1109/picmet.2006.296712) | [link](https://openalex.org/W1968419843) |
| 2030 | responsible innovation | he fashion industry, achieving the goals included in the UN 2030 Agenda. This study draws on bibliometric analysis and syste | regex_abstract_S3 | 0.70 | 2022 | [10.1007/s10490-022-09844-7](https://doi.org/10.1007/s10490-022-09844-7) | [link](https://openalex.org/W4293113628) |
| 2035 | technology foresight | ing Science and Technology to 2035 Technology foresight is a... | regex_year | 0.60 | 2017 | [10.15302/j-sscae-2017.01.006](https://doi.org/10.15302/j-sscae-2017.01.006) | [link](https://openalex.org/W2604026250) |
| 2035 | technology foresight | the 4th TF, future technologies that might be developed by 2035 were discovered and Delphi survey was conducted to examine | regex_abstract_S3 | 0.70 | 2014 | [10.1108/fs-11-2012-0087](https://doi.org/10.1108/fs-11-2012-0087) | [link](https://openalex.org/W2080769824) |
| 2035 | technology foresight | ace their evolution, to foresee the ATs likely to evolve by 2035 and offer a hope, to possibly reduce the gap between disabl | regex_abstract_S3 | 0.70 | 2018 | [10.3233/tad-170180](https://doi.org/10.3233/tad-170180) | [link](https://openalex.org/W2800736945) |
| 2035 | technology foresight | foresight on China's engineering science and technology to 2035 were designed by considering the characteristics of enginee | regex_abstract_S3 | 0.70 | 2017 | [10.15302/j-sscae-2017.01.006](https://doi.org/10.15302/j-sscae-2017.01.006) | [link](https://openalex.org/W2604026250) |
| 2037 | technology foresight | be relevant to cancer care over the next thirty years (2017–2037). Drawing on the concepts of technology foresight, a method | regex_abstract_S3 | 0.70 | 2018 | [10.1080/10438599.2018.1549788](https://doi.org/10.1080/10438599.2018.1549788) | [link](https://openalex.org/W2902615535) |
| 2050 | innovation diffusion | alth and poverty, so that there will come a time, say about 2050, when it is conceivable that all economies might be more or | regex_abstract_S3 | 0.70 | 2006 | [10.1093/elt/ccl050](https://doi.org/10.1093/elt/ccl050) | [link](https://openalex.org/W4241387840) |
| 2054 | responsible innovation | ntral Germany serve alongside a representative survey ( n = 2054) as the basis for both understanding social attitudes and r | regex_abstract_S3 | 0.70 | 2023 | [10.1186/s13705-023-00394-4](https://doi.org/10.1186/s13705-023-00394-4) | [link](https://openalex.org/W4381662309) |
| 2100 | responsible innovation | third decade of the twenty-first century, ensuring that science... | decade_keyword | 0.50 | 2020 | [10.1080/23299460.2020.1712537](https://doi.org/10.1080/23299460.2020.1712537) | [link](https://openalex.org/W3003933509) |

### TRL Trajectory (NASA TRL 1-9, n=5)

| Year | Tech | TRL | Evidence | Confidence | DOI | source_url |
|---:|---|---:|---|---:|---|---|
| 2024 | general purpose technology | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | innovation diffusion | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | responsible innovation | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | technology convergence | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | technology foresight | 7 | current_status='early_deployment' | 0.80 |  |  |

---

## PHOTONICS - Photonics (フォトニクス)

**Physical AI mapping**: SENSING (LiDAR / vision frontend)

### Top 20 Cited Papers (citation_count desc)

| # | Year | Title | First Authors | Venue | DOI | Citations | Countries | JP authors? | source_url |
|---:|---:|---|---|---|---|---:|---|:---:|---|
| 1 | 2014 | A variational eigenvalue solver on a photonic quantum processor | Alberto Peruzzo; Jarrod R. McClean; Peter Shadbolt; Man‐Hong Yung; Xiaoqi Zhou | Nature Communications | [10.1038/ncomms5213](https://doi.org/10.1038/ncomms5213) | 4477 | GB,US |  | [link](https://openalex.org/W2161685427) |
| 2 | 2017 | Deep learning with coherent nanophotonic circuits | Yichen Shen; Nicholas C. Harris; Scott A. Skirlo; Mihika Prabhu; Tom Baehr‐Jones | Nature Photonics | [10.1038/nphoton.2017.93](https://doi.org/10.1038/nphoton.2017.93) | 3043 | US,CA |  | [link](https://openalex.org/W2752849906) |
| 3 | 2007 | Linear optical quantum computing with photonic qubits | Pieter Kok; William J. Munro; Kae Nemoto; Timothy C. Ralph; Jonathan P. Dowling | Reviews of Modern Physics | [10.1103/revmodphys.79.135](https://doi.org/10.1103/revmodphys.79.135) | 2819 | GB,US,JP,AU | YES | [link](https://openalex.org/W1514675880) |
| 4 | 2018 | All-optical machine learning using diffractive deep neural networks | Xing Lin; Yair Rivenson; Nezih Tolga Yardimci; Muhammed Veli; Yi Luo | Science | [10.1126/science.aat8084](https://doi.org/10.1126/science.aat8084) | 2376 | US |  | [link](https://openalex.org/W2798701005) |
| 5 | 2009 | Photonic quantum technologies | Jeremy L. O’Brien; Akira Furusawa; Jelena Vučković | Nature Photonics | [10.1038/nphoton.2009.229](https://doi.org/10.1038/nphoton.2009.229) | 2323 | GB,JP,US | YES | [link](https://openalex.org/W1967673033) |
| 6 | 2006 | The Past, Present, and Future of Silicon Photonics | Richard Soref | IEEE Journal of Selected Topics in Quantum Electronics | [10.1109/jstqe.2006.883151](https://doi.org/10.1109/jstqe.2006.883151) | 1969 | US |  | [link](https://openalex.org/W2099610951) |
| 7 | 2006 | The Past, Present, and Future of Silicon Photonics | Richard Soref | IEEE Journal of Selected Topics in Quantum Electronics | [10.1109/jstqe.2006.883151](https://doi.org/10.1109/jstqe.2006.883151) | 1969 | US |  | [link](https://openalex.org/W2099610951) |
| 8 | 2016 | Learning Rotation-Invariant Convolutional Neural Networks for Object Detection in VHR Optical Remote Sensing Images | Gong Cheng; Peicheng Zhou; Junwei Han | IEEE Transactions on Geoscience and Remote Sensing | [10.1109/tgrs.2016.2601622](https://doi.org/10.1109/tgrs.2016.2601622) | 1741 | CN |  | [link](https://openalex.org/W2512351403) |
| 9 | 2013 | Imaging topological edge states in silicon photonics | Mohammad Hafezi; Sunil Mittal; Jingyun Fan; Alan L. Migdall; Jacob M. Taylor | Nature Photonics | [10.1038/nphoton.2013.274](https://doi.org/10.1038/nphoton.2013.274) | 1681 | US |  | [link](https://openalex.org/W1997972857) |
| 10 | 2013 | Imaging topological edge states in silicon photonics | Mohammad Hafezi; Sunil Mittal; Jingyun Fan; Alan L. Migdall; Jacob M. Taylor | Nature Photonics | [10.1038/nphoton.2013.274](https://doi.org/10.1038/nphoton.2013.274) | 1681 | US |  | [link](https://openalex.org/W1997972857) |
| 11 | 2021 | 11 TOPS photonic convolutional accelerator for optical neural networks | Xingyuan Xu; Mengxi Tan; Bill Corcoran; Jiayang Wu; Andreas Boes | Nature | [10.1038/s41586-020-03063-0](https://doi.org/10.1038/s41586-020-03063-0) | 1467 | AU,HK,CN,CA |  | [link](https://openalex.org/W3118265437) |
| 12 | 2015 | Interfacing single photons and single quantum dots with photonic nanostructures | Peter Lodahl; Sahand Mahmoodian; Søren Stobbe | Reviews of Modern Physics | [10.1103/revmodphys.87.347](https://doi.org/10.1103/revmodphys.87.347) | 1419 | DK |  | [link](https://openalex.org/W1930702843) |
| 13 | 2019 | Integrated photonic quantum technologies | Jianwei Wang; Fabio Sciarrino; Anthony Laing; Mark G. Thompson | Nature Photonics | [10.1038/s41566-019-0532-1](https://doi.org/10.1038/s41566-019-0532-1) | 1376 | CN,IT,GB |  | [link](https://openalex.org/W2980980200) |
| 14 | 2006 | Silicon Photonics | Bahram Jalali; Sasan Fathpour | Journal of Lightwave Technology | [10.1109/jlt.2006.885782](https://doi.org/10.1109/jlt.2006.885782) | 1365 | US |  | [link](https://openalex.org/W4256501225) |
| 15 | 2006 | Silicon Photonics | Bahram Jalali; Sasan Fathpour | Journal of Lightwave Technology | [10.1109/jlt.2006.885782](https://doi.org/10.1109/jlt.2006.885782) | 1365 | US |  | [link](https://openalex.org/W4256501225) |
| 16 | 2010 | Nonlinear silicon photonics | Juerg Leuthold; C. Koos; W. Freude | Nature Photonics | [10.1038/nphoton.2010.185](https://doi.org/10.1038/nphoton.2010.185) | 1309 | DE |  | [link](https://openalex.org/W1978908111) |
| 17 | 2010 | Nonlinear silicon photonics | Juerg Leuthold; C. Koos; W. Freude | Nature Photonics | [10.1038/nphoton.2010.185](https://doi.org/10.1038/nphoton.2010.185) | 1309 | DE |  | [link](https://openalex.org/W1978908111) |
| 18 | 2016 | Roadmap on silicon photonics | David J. Thomson; Aaron Zilkie; John E. Bowers; Tin Komljenović; Graham T. Reed | Journal of Optics | [10.1088/2040-8978/18/7/073003](https://doi.org/10.1088/2040-8978/18/7/073003) | 1293 | GB,US,FR,CA,IE |  | [link](https://openalex.org/W2468172470) |
| 19 | 2016 | Roadmap on silicon photonics | David J. Thomson; Aaron Zilkie; John E. Bowers; Tin Komljenović; Graham T. Reed | Journal of Optics | [10.1088/2040-8978/18/7/073003](https://doi.org/10.1088/2040-8978/18/7/073003) | 1293 | GB,US,FR,CA,IE |  | [link](https://openalex.org/W2468172470) |
| 20 | 2008 | Analogs of quantum-Hall-effect edge states in photonic crystals | S. Raghu; F. D. M. Haldane | Physical Review A | [10.1103/physreva.78.033834](https://doi.org/10.1103/physreva.78.033834) | 1285 | US |  | [link](https://openalex.org/W2007421284) |

**日本機関所属著者を含む論文** (上記 Top 20 のうち):

| Year | Title | JP Affiliation (raw) | DOI |
|---:|---|---|---|
| 2007 | Linear optical quantum computing with photonic qubits | National Institute of Informatics | [10.1103/revmodphys.79.135](https://doi.org/10.1103/revmodphys.79.135) |
| 2009 | Photonic quantum technologies | The University of Tokyo | [10.1038/nphoton.2009.229](https://doi.org/10.1038/nphoton.2009.229) |

### Milestones (academic evidence, n=18)

| Year | Tech | Type | Description | Evidence | Confidence | Status | DOI | source_url |
|---:|---|---|---|---|---:|---|---|---|
| 2006 | silicon photonics | commercial | t by industry and government. Commercial state-of-the-art CMOS silicon-on-insulator (SOI) foundries | academic_paper | 0.75 | observed | [10.1109/jstqe.2006.883151](https://doi.org/10.1109/jstqe.2006.883151) | [link](https://openalex.org/W2099610951) |
| 2006 | silicon photonics | commercial | e overcome before large-scale commercialization can occur. In particular, for realization of integration wi | academic_paper | 0.75 | observed | [10.1109/jlt.2006.885782](https://doi.org/10.1109/jlt.2006.885782) | [link](https://openalex.org/W4256501225) |
| 2006 | silicon photonics | commercial | hat must be overcome before large-scale commercialization can occur. In particular, for realization of integration with CMOS very large s | academic_paper_high_citation | 0.80 | observed |  | [link](https://openalex.org/W2295144434) |
| 2009 | photonic integrated circuit | prototype | present two experiments to demonstrate proof-of-concept operation of the OPLL-PIC: homodyne locking and offset locking of the SG-DBR la | academic_paper_mid_citation | 0.53 | observed | [10.1109/jlt.2009.2030341](https://doi.org/10.1109/jlt.2009.2030341) | [link](https://openalex.org/W2153955018) |
| 2014 | silicon photonics | prototype | licon photonics reservoir. We demonstrate experimentally and through simulations that, thanks to the RC paradigm, th | academic_paper | 0.75 | observed | [10.1038/ncomms4541](https://doi.org/10.1038/ncomms4541) | [link](https://openalex.org/W2029939668) |
| 2016 | silicon photonics | commercial | tion resulting in high-volume production at low cost. This is a key enabling factor for bringing pho | academic_paper | 0.75 | observed | [10.1088/2040-8978/18/7/073003](https://doi.org/10.1088/2040-8978/18/7/073003) | [link](https://openalex.org/W2468172470) |
| 2016 | photonic integrated circuit | commercial | tion resulting in high-volume production at low cost. This is a key enabling factor for bringing pho | academic_paper | 0.75 | observed | [10.1088/2040-8978/18/7/073003](https://doi.org/10.1088/2040-8978/18/7/073003) | [link](https://openalex.org/W2468172470) |
| 2016 | photonic integrated circuit | commercial | facilities. State‐of‐the‐art commercial PICs integrate hundreds of elements, and the integration of | academic_paper | 0.75 | observed | [10.1515/nanoph-2015-0152](https://doi.org/10.1515/nanoph-2015-0152) | [link](https://openalex.org/W2473201566) |
| 2017 | silicon photonics | prototype | sent, to the best of our knowledge, the first demonstration of coherent solid-state light detection and ranging (LIDAR) using optical phase | academic_paper_high_citation | 0.80 | observed | [10.1364/ol.42.004091](https://doi.org/10.1364/ol.42.004091) | [link](https://openalex.org/W2761155850) |
| 2019 | silicon photonics | prototype | range of nearly 200 m. In addition, the first demonstration of 3-D coherent LiDAR with optical phased arrays is presented with raster-scann | academic_paper_high_citation | 0.80 | observed | [10.1109/jstqe.2019.2908555](https://doi.org/10.1109/jstqe.2019.2908555) | [link](https://openalex.org/W2925745050) |
| 2019 | optical neural network | mass_deployment | ral networks (ANNs) have been widely used for industrial applications and have played a more importan | academic_paper | 0.75 | observed | [10.1364/optica.6.001132](https://doi.org/10.1364/optica.6.001132) | [link](https://openalex.org/W2970080722) |
| 2020 | quantum photonics | mass_deployment | electron spin coherence compared to the widely used InGaAs quantum dots. However, their charge stability and optical linewidths are | academic_paper_mid_citation | 0.55 | observed | [10.1038/s41467-020-18625-z](https://doi.org/10.1038/s41467-020-18625-z) | [link](https://openalex.org/W3008355472) |
| 2021 | silicon photonics | commercial | the gap between research and commercialization. However, silicon photonics bucked the trend, with industry | academic_paper | 0.75 | observed | [10.1109/jlt.2021.3066203](https://doi.org/10.1109/jlt.2021.3066203) | [link](https://openalex.org/W3188674373) |
| 2021 | quantum photonics | commercial | ated optical quantum circuits. With the commercialization of lithium niobate on insulator (LNOI) substrates in the recent years, the lith | academic_paper_mid_citation | 0.56 | observed | [10.1002/adom.202100789](https://doi.org/10.1002/adom.202100789) | [link](https://openalex.org/W3200149078) |
| 2021 | optical neural network | mass_deployment | l walks of life, and has been widely used in medical image analysis, molecular and material science, | academic_paper | 0.65 | observed | [10.1186/s43074-021-00026-0](https://doi.org/10.1186/s43074-021-00026-0) | [link](https://openalex.org/W3165876013) |
| 2022 | quantum photonics | prototype | eriments to be scaled down to prototype chips with improvements in efficiency, robustness, and key | academic_paper | 0.75 | observed | [10.1088/2515-7647/ac1ef4](https://doi.org/10.1088/2515-7647/ac1ef4) | [link](https://openalex.org/W3195862557) |
| 2022 | optical neural network | prototype | sub-photon-per-multiplication demonstration—noise reduction from the accumulation of scalar multiplicat | academic_paper | 0.75 | observed | [10.1038/s41467-021-27774-8](https://doi.org/10.1038/s41467-021-27774-8) | [link](https://openalex.org/W3159854664) |
| 2023 | optical neural network | prototype | idate the proposed MIONN, we fabricated proof-of-concept chips and a prototype photonic-electronic artificial intelligence (AI) computin | academic_paper_mid_citation | 0.50 | observed | [10.1515/nanoph-2023-0298](https://doi.org/10.1515/nanoph-2023-0298) | [link](https://openalex.org/W4387204441) |

### Forecasts 2027-2100 (extracted from papers, n=2)

| Extracted Year | Tech | Evidence Phrase | Method | Confidence | Paper Year | DOI | source_url |
|---:|---|---|---|---:|---:|---|---|
| 2044 | quantum photonics | ong-Ou-Mandel dip [C. K. Hong, et al., Phys. Rev. Lett. 59, 2044 (1987)] with 96% visibility. | regex_abstract_S3 | 0.70 | 2011 | [10.1063/1.3656073](https://doi.org/10.1063/1.3656073) | [link](https://openalex.org/W2073723985) |
| 2048 | silicon photonics | coherent LiDAR engine has been demonstrated. Five identical 2048-channel driver chips flip onto a single silicon photonics L | regex_abstract_S3 | 0.70 | 2023 | [10.23919/vlsitechnologyandcir57934.2023.10185161](https://doi.org/10.23919/vlsitechnologyandcir57934.2023.10185161) | [link](https://openalex.org/W4385192516) |

### TRL Trajectory (NASA TRL 1-9, n=4)

| Year | Tech | TRL | Evidence | Confidence | DOI | source_url |
|---:|---|---:|---|---:|---|---|
| 2024 | optical neural network | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | photonic integrated circuit | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | quantum photonics | 7 | current_status='early_deployment' | 0.80 |  |  |
| 2024 | silicon photonics | 7 | current_status='early_deployment' | 0.80 |  |  |

---

## Cross-Domain Technology Genealogy (Physical AI 関連の系譜)

**Total edges retrieved**: 119

| From Domain | Predecessor Tech | To Domain | Successor Tech | Relation | Confidence | Method | Notes |
|---|---|---|---|---|---:|---|---|
| 2D_MATERIAL | hexagonal boron nitride | NEUROMORPHIC | neuromorphic computing | paper_citation_chain | 0.70 | paper_citation_chain | citation count: 10 |
| 2D_MATERIAL | transition metal dichalcogenide | NEUROMORPHIC | neuromorphic computing | paper_citation_chain | 0.62 | paper_citation_chain | citation count: 6 |
| 2D_MATERIAL | hexagonal boron nitride | PHOTONICS | quantum photonics | paper_citation_chain | 0.78 | paper_citation_chain | citation count: 14 |
| BIOELEC | bioelectronic medicine | BRAIN_CI | brain-computer interface | paper_citation_chain | 0.58 | paper_citation_chain | citation count: 4 |
| BRAIN_CI | intracortical microelectrode | BIOELEC | bioelectronic medicine | paper_citation_chain | 0.60 | paper_citation_chain | citation count: 5 |
| BRAIN_CI | brain-computer interface | BIOELEC | bioelectronic medicine | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| BRAIN_CI | brain-computer interface | BIOELEC | implantable neural stimulator | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| BRAIN_CI | intracortical microelectrode | BRAIN_CI | brain-computer interface | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 56 |
| BRAIN_CI | brain-computer interface | BRAIN_CI | non-invasive BCI | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 32 |
| BRAIN_CI | brain-computer interface | BRAIN_CI | intracortical microelectrode | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 31 |
| BRAIN_CI | Neuralink | BRAIN_CI | brain-computer interface | paper_citation_chain | 0.92 | paper_citation_chain | citation count: 21 |
| BRAIN_CI | non-invasive BCI | BRAIN_CI | brain-computer interface | paper_citation_chain | 0.82 | paper_citation_chain | citation count: 16 |
| BRAIN_CI | brain-computer interface | BRAIN_CI | Neuralink | paper_citation_chain | 0.68 | paper_citation_chain | citation count: 9 |
| BRAIN_CI | brain-computer interface | MATERIAL | グラフェン | paper_citation_chain | 0.58 | paper_citation_chain | citation count: 4 |
| BRAIN_CI | intracortical microelectrode | MATERIAL | グラフェン | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| BRAIN_CI | brain-computer interface | MEDICAL | Synchron | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| BUILDING | self-healing concrete | BIO_MATERIAL | biodegradable plastic | paper_citation_chain | 0.58 | paper_citation_chain | citation count: 4 |
| BUILDING | self-healing concrete | MATERIAL | self-healing materials | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 23 |
| CROSS | responsible innovation | AGRI | cellular agriculture | paper_citation_chain | 0.64 | paper_citation_chain | citation count: 7 |
| CROSS | responsible innovation | CLIMATE | stratospheric aerosol injection | paper_citation_chain | 0.58 | paper_citation_chain | citation count: 4 |
| CROSS | innovation diffusion | CROSS | general purpose technology | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| CROSS | responsible innovation | CROSS | technology foresight | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| CROSS | responsible innovation | SYNBIO | synthetic biology | paper_citation_chain | 0.68 | paper_citation_chain | citation count: 9 |
| CROSS | innovation diffusion | TRANSPORT | hyperloop | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| CYBER_PHYS | industrial internet of things | CYBER_PHYS | smart factory | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 43 |
| CYBER_PHYS | smart factory | CYBER_PHYS | industrial internet of things | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 40 |
| CYBER_PHYS | industrial internet of things | CYBER_PHYS | digital twin manufacturing | paper_citation_chain | 0.64 | paper_citation_chain | citation count: 7 |
| CYBER_PHYS | digital twin manufacturing | CYBER_PHYS | industrial internet of things | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| CYBER_PHYS | industrial internet of things | EDGE_AI | federated learning | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 105 |
| CYBER_PHYS | industrial internet of things | EDGE_AI | TinyML | paper_citation_chain | 0.70 | paper_citation_chain | citation count: 10 |
| CYBER_PHYS | smart factory | EDGE_AI | TinyML | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| CYBER_PHYS | industrial internet of things | SPACE | satellite constellation | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| EDGE_AI | federated learning | CYBER_PHYS | industrial internet of things | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 157 |
| EDGE_AI | TinyML | CYBER_PHYS | industrial internet of things | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 32 |
| EDGE_AI | federated learning | CYBER_PHYS | smart factory | paper_citation_chain | 0.62 | paper_citation_chain | citation count: 6 |
| EDGE_AI | TinyML | EDGE_AI | federated learning | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 102 |
| EDGE_AI | federated learning | EDGE_AI | TinyML | paper_citation_chain | 0.84 | paper_citation_chain | citation count: 17 |
| EDGE_AI | on-device machine learning | EDGE_AI | TinyML | paper_citation_chain | 0.66 | paper_citation_chain | citation count: 8 |
| EDGE_AI | federated learning | EDGE_AI | edge AI inference | paper_citation_chain | 0.62 | paper_citation_chain | citation count: 6 |
| EDGE_AI | edge AI inference | EDGE_AI | TinyML | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| EDGE_AI | federated learning | EDGE_AI | on-device machine learning | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| EDGE_AI | on-device machine learning | EDGE_AI | federated learning | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| EDGE_AI | federated learning | MEDICAL | AlphaFold protein | paper_citation_chain | 0.68 | paper_citation_chain | citation count: 9 |
| EDGE_AI | federated learning | SPACE | satellite constellation | paper_citation_chain | 0.62 | paper_citation_chain | citation count: 6 |
| EDGE_AI | federated learning | TRANSPORT | autonomous vehicle Waymo | paper_citation_chain | 0.68 | paper_citation_chain | citation count: 9 |
| ENERGY | vehicle-to-grid | CYBER_PHYS | industrial internet of things | paper_citation_chain | 0.82 | paper_citation_chain | citation count: 16 |
| HYDROGEN | hydrogen fuel cell | CROSS | innovation diffusion | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| HYDROGEN | hydrogen fuel cell | TRANSPORT | Joby Aviation | paper_citation_chain | 0.62 | paper_citation_chain | citation count: 6 |
| HYDROGEN | hydrogen fuel cell | TRANSPORT | eVTOL aircraft | paper_citation_chain | 0.60 | paper_citation_chain | citation count: 5 |
| MATERIAL | self-healing materials | BUILDING | self-healing concrete | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 54 |
| MATERIAL | グラフェン | NEUROMORPHIC | neuromorphic computing | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 29 |
| MATERIAL | グラフェン | NEUROMORPHIC | memristor crossbar | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| MATERIAL | グラフェン | PHOTONICS | silicon photonics | paper_citation_chain | 0.58 | paper_citation_chain | citation count: 4 |
| MEDICAL | AlphaFold protein | AGRI | precision fermentation | paper_citation_chain | 0.58 | paper_citation_chain | citation count: 4 |
| MEDICAL | AlphaFold protein | AGRI | cellular agriculture | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| MEDICAL | AlphaFold protein | EDGE_AI | federated learning | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| MEDICAL | AlphaFold protein | MEDICAL | AlphaFold 3 | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 68 |
| MEDICAL | AlphaFold 3 | MEDICAL | AlphaFold protein | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 64 |
| MEDICAL | AlphaFold protein | PHOTONICS | optical neural network | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| MEDICAL | AlphaFold protein | SYNBIO | synthetic biology | paper_citation_chain | 0.84 | paper_citation_chain | citation count: 17 |
| MEDICAL | CAR-T cell therapy | SYNBIO | synthetic biology | paper_citation_chain | 0.58 | paper_citation_chain | citation count: 4 |
| MEDICAL | AlphaFold protein | SYNBIO | metabolic engineering | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| NEUROMORPHIC | neuromorphic computing | BIOELEC | bioelectronic medicine | paper_citation_chain | 0.60 | paper_citation_chain | citation count: 5 |
| NEUROMORPHIC | spiking neural network | BIOELEC | bioelectronic medicine | paper_citation_chain | 0.58 | paper_citation_chain | citation count: 4 |
| NEUROMORPHIC | spiking neural network | EDGE_AI | TinyML | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| NEUROMORPHIC | neuromorphic computing | EDGE_AI | federated learning | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| NEUROMORPHIC | neuromorphic computing | MATERIAL | グラフェン | paper_citation_chain | 0.88 | paper_citation_chain | citation count: 19 |
| NEUROMORPHIC | memristor crossbar | MATERIAL | グラフェン | paper_citation_chain | 0.64 | paper_citation_chain | citation count: 7 |
| NEUROMORPHIC | spiking neural network | NEUROMORPHIC | neuromorphic computing | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 145 |
| NEUROMORPHIC | memristor crossbar | NEUROMORPHIC | neuromorphic computing | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 98 |
| NEUROMORPHIC | neuromorphic computing | NEUROMORPHIC | memristor crossbar | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 89 |
| NEUROMORPHIC | neuromorphic computing | NEUROMORPHIC | spiking neural network | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 65 |
| NEUROMORPHIC | neuromorphic computing | NEUROMORPHIC | Loihi neuromorphic | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 43 |
| NEUROMORPHIC | spiking neural network | NEUROMORPHIC | Loihi neuromorphic | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 29 |
| NEUROMORPHIC | spiking neural network | NEUROMORPHIC | memristor crossbar | paper_citation_chain | 0.80 | paper_citation_chain | citation count: 15 |
| NEUROMORPHIC | Loihi neuromorphic | NEUROMORPHIC | neuromorphic computing | paper_citation_chain | 0.78 | paper_citation_chain | citation count: 14 |
| NEUROMORPHIC | Loihi neuromorphic | NEUROMORPHIC | spiking neural network | paper_citation_chain | 0.66 | paper_citation_chain | citation count: 8 |
| NEUROMORPHIC | memristor crossbar | NEUROMORPHIC | spiking neural network | paper_citation_chain | 0.64 | paper_citation_chain | citation count: 7 |
| NEUROMORPHIC | memristor crossbar | NEUROMORPHIC | Loihi neuromorphic | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| NEUROMORPHIC | neuromorphic computing | PHOTONICS | optical neural network | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 53 |
| NEUROMORPHIC | neuromorphic computing | PHOTONICS | silicon photonics | paper_citation_chain | 0.86 | paper_citation_chain | citation count: 18 |
| NEUROMORPHIC | neuromorphic computing | PHOTONICS | photonic integrated circuit | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| NEUROMORPHIC | neuromorphic computing | PHOTONICS | quantum photonics | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| NEUROMORPHIC | memristor crossbar | PHOTONICS | optical neural network | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| PHOTONICS | quantum photonics | 2D_MATERIAL | hexagonal boron nitride | paper_citation_chain | 0.82 | paper_citation_chain | citation count: 16 |
| PHOTONICS | silicon photonics | MATERIAL | グラフェン | paper_citation_chain | 0.94 | paper_citation_chain | citation count: 22 |
| PHOTONICS | photonic integrated circuit | MATERIAL | グラフェン | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| PHOTONICS | silicon photonics | NEUROMORPHIC | neuromorphic computing | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 36 |
| PHOTONICS | optical neural network | NEUROMORPHIC | neuromorphic computing | paper_citation_chain | 0.84 | paper_citation_chain | citation count: 17 |
| PHOTONICS | photonic integrated circuit | NEUROMORPHIC | neuromorphic computing | paper_citation_chain | 0.64 | paper_citation_chain | citation count: 7 |
| PHOTONICS | photonic integrated circuit | PHOTONICS | silicon photonics | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 35 |
| PHOTONICS | quantum photonics | PHOTONICS | silicon photonics | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 27 |
| PHOTONICS | silicon photonics | PHOTONICS | photonic integrated circuit | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 27 |
| PHOTONICS | silicon photonics | PHOTONICS | quantum photonics | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 26 |
| PHOTONICS | silicon photonics | PHOTONICS | optical neural network | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 24 |
| PHOTONICS | quantum photonics | PHOTONICS | photonic integrated circuit | paper_citation_chain | 0.70 | paper_citation_chain | citation count: 10 |
| PHOTONICS | photonic integrated circuit | PHOTONICS | quantum photonics | paper_citation_chain | 0.58 | paper_citation_chain | citation count: 4 |
| PHOTONICS | silicon photonics | QUANTUM | fault-tolerant quantum computing | paper_citation_chain | 0.70 | paper_citation_chain | citation count: 10 |
| PHOTONICS | quantum photonics | QUANTUM | fault-tolerant quantum computing | paper_citation_chain | 0.64 | paper_citation_chain | citation count: 7 |
| PHOTONICS | silicon photonics | QUANTUM | Lightmatter Passage M1000 | paper_citation_chain | 0.62 | paper_citation_chain | citation count: 6 |
| PHOTONICS | quantum photonics | QUANTUM | quantum supremacy | paper_citation_chain | 0.60 | paper_citation_chain | citation count: 5 |
| PHOTONICS | quantum photonics | QUANTUM | quantum error correction | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| PHOTONICS | silicon photonics | TRANSPORT | solid-state lidar | paper_citation_chain | 0.95 | paper_citation_chain | citation count: 28 |
| QUANTUM | quantum supremacy | CROSS | responsible innovation | paper_citation_chain | 0.58 | paper_citation_chain | citation count: 4 |
| QUANTUM | quantum supremacy | PHOTONICS | quantum photonics | paper_citation_chain | 0.72 | paper_citation_chain | citation count: 11 |
| QUANTUM | Lightmatter Passage M1000 | PHOTONICS | silicon photonics | paper_citation_chain | 0.72 | paper_citation_chain | citation count: 11 |
| QUANTUM | quantum error correction | PHOTONICS | quantum photonics | paper_citation_chain | 0.62 | paper_citation_chain | citation count: 6 |
| QUANTUM | quantum supremacy | PHOTONICS | silicon photonics | paper_citation_chain | 0.62 | paper_citation_chain | citation count: 6 |
| QUANTUM | Lightmatter Passage M1000 | PHOTONICS | quantum photonics | paper_citation_chain | 0.58 | paper_citation_chain | citation count: 4 |
| QUANTUM | quantum supremacy | PHOTONICS | photonic integrated circuit | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| SAFETY_AI | AI alignment | SAFETY_AI | RLHF reinforcement learning human feedback | paper_citation_chain | 0.64 | paper_citation_chain | citation count: 7 |
| SAFETY_AI | RLHF reinforcement learning human feedback | SAFETY_AI | AI alignment | paper_citation_chain | 0.62 | paper_citation_chain | citation count: 6 |
| SPACE | satellite constellation | EDGE_AI | federated learning | paper_citation_chain | 0.60 | paper_citation_chain | citation count: 5 |
| SYNBIO | synthetic biology | CROSS | responsible innovation | paper_citation_chain | 0.70 | paper_citation_chain | citation count: 10 |
| SYNBIO | synthetic biology | MEDICAL | AlphaFold protein | paper_citation_chain | 0.70 | paper_citation_chain | citation count: 10 |
| TRANSPORT | solid-state lidar | PHOTONICS | silicon photonics | paper_citation_chain | 0.70 | paper_citation_chain | citation count: 10 |
| TRANSPORT | electric aviation | TRANSPORT | eVTOL aircraft | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| TRANSPORT | eVTOL aircraft | TRANSPORT | Joby Aviation | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |
| TRANSPORT | eVTOL aircraft | TRANSPORT | electric aviation | paper_citation_chain | 0.56 | paper_citation_chain | citation count: 3 |

---

## Top 100 Physical AI Mentions (paper_tech_mentions, ranked by citation_count desc)

**抽出条件**: Physical AI 直結 10 領域 / mention_type IN (propose, apply, forecast, review, critique, meta_analysis) / 引用数 desc

| # | Domain | Paper ID | Year | Citations | Title | Mentioned Tech | Type | Confidence | Excerpt | DOI | source_url |
|---:|---|---:|---:|---:|---|---|---|---:|---|---|---|
| 1 | MEDICAL | 7458 | 2021 | 43999 | Highly accurate protein structure prediction with AlphaFold | AlphaFold protein | propose | 0.70 | Highly accurate protein structure prediction with AlphaFold , demonstrating accuracy competitive with experimental structures in a majority... | [10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2) | [link](https://openalex.org/W3177828909) |
| 2 | MEDICAL | 7589 | 2024 | 12710 | Accurate structure prediction of biomolecular interactions with AlphaFold 3 | AlphaFold 3 | apply | 0.65 | Accurate structure prediction of biomolecular interactions with AlphaFold 3 . Together, these results show that high-accuracy modelling across biomolecular... | [10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w) | [link](https://openalex.org/W4396721167) |
| 3 | MEDICAL | 7589 | 2024 | 12710 | Accurate structure prediction of biomolecular interactions with AlphaFold 3 | AlphaFold protein | apply | 0.65 | Accurate structure prediction of biomolecular interactions with AlphaFold 3 . Together, these results show that high-accuracy modelling across biomolecul... | [10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w) | [link](https://openalex.org/W4396721167) |
| 4 | MEDICAL | 7459 | 2021 | 8114 | AlphaFold Protein Structure Database: massively expanding the structural coverag | AlphaFold protein | forecast | 0.60 | AlphaFold Protein Structure Database: massively expanding the structural coverage of prot... | [10.1093/nar/gkab1061](https://doi.org/10.1093/nar/gkab1061) | [link](https://openalex.org/W3211795435) |
| 5 | MEDICAL | 7481 | 2022 | 6790 | UniProt: the Universal Protein Knowledgebase in 2023 | AlphaFold protein | propose | 0.70 | ... easily accessible to the research community. This interface includes access to AlphaFold structures for more than 85% of all entries as well as improved vis | [10.1093/nar/gkac1052](https://doi.org/10.1093/nar/gkac1052) | [link](https://openalex.org/W4309506674) |
| 6 | EDGE_AI | 9100 | 2019 | 5728 | Federated Machine Learning | federated learning | propose | 0.70 | ...rivacy and security. We propose a possible solution to these challenges: secure federated learning. Beyond the federated-learning framework first proposed by | [10.1145/3298981](https://doi.org/10.1145/3298981) | [link](https://openalex.org/W2912213068) |
| 7 | EDGE_AI | 20387 | 2016 | 5177 | Communication-Efficient Learning of Deep Networks from Decentralized Data | federated learning | propose | 0.65 | ...el by aggregating locally-computed updates. We term this decentralized approach Federated Learning. We present a practical method for the federated learning  | [10.48550/arxiv.1602.05629](https://doi.org/10.48550/arxiv.1602.05629) | [link](https://openalex.org/W2541884796) |
| 8 | EDGE_AI | 9093 | 2020 | 4520 | Federated Learning: Challenges, Methods, and Future Directions | federated learning | critique | 0.70 | Federated Learning: Challenges, Methods, and Future Directions Federated learning involves trainin... | [10.1109/msp.2020.2975749](https://doi.org/10.1109/msp.2020.2975749) | [link](https://openalex.org/W3021654819) |
| 9 | MEDICAL | 21451 | 2020 | 3481 | Improved protein structure prediction using potentials from deep learning | AlphaFold protein | apply | 0.65 | Improved protein structure prediction using potentials from deep learning  | [10.1038/s41586-019-1923-7](https://doi.org/10.1038/s41586-019-1923-7) | [link](https://openalex.org/W2999044305) |
| 10 | MEDICAL | 7483 | 2021 | 3169 | Highly accurate protein structure prediction for the human proteome | AlphaFold protein | propose | 0.70 | ...very high confidence. We introduce several metrics developed by building on the AlphaFold model and use them to interpret the dataset, identifying strong mul | [10.1038/s41586-021-03828-1](https://doi.org/10.1038/s41586-021-03828-1) | [link](https://openalex.org/W3183475563) |
| 11 | CROSS | 6711 | 2013 | 2919 | Developing a framework for responsible innovation | responsible innovation | propose | 0.70 | Developing a framework for responsible innovation The governance of emerging science and innovation is a major challenge for cont... | [10.1016/j.respol.2013.05.008](https://doi.org/10.1016/j.respol.2013.05.008) | [link](https://openalex.org/W2100967449) |
| 12 | EDGE_AI | 9094 | 2020 | 2400 | The future of digital health with federated learning | federated learning | forecast | 0.72 | The future of digital health with federated learning Data-driven machine learning (ML) has emerged as a promising approach for build... | [10.1038/s41746-020-00323-1](https://doi.org/10.1038/s41746-020-00323-1) | [link](https://openalex.org/W3012501605) |
| 13 | EDGE_AI | 9096 | 2020 | 2374 | Federated Learning in Mobile Edge Networks: A Comprehensive Survey | federated learning | review | 0.70 | Federated Learning in Mobile Edge Networks: A Comprehensive Survey In recent years, mobile devices... | [10.1109/comst.2020.2986024](https://doi.org/10.1109/comst.2020.2986024) | [link](https://openalex.org/W3015636663) |
| 14 | CYBER_PHYS | 9240 | 2018 | 2267 | Industrial Internet of Things: Challenges, Opportunities, and Directions | industrial internet of things | critique | 0.70 | Industrial Internet of Things: Challenges, Opportunities, and Directions Internet of Things (IoT) is an emerg... | [10.1109/tii.2018.2852491](https://doi.org/10.1109/tii.2018.2852491) | [link](https://openalex.org/W2811266402) |
| 15 | EDGE_AI | 9101 | 2019 | 2188 | Adaptive Federated Learning in Resource Constrained Edge Computing Systems | federated learning | apply | 0.70 | Adaptive Federated Learning in Resource Constrained Edge Computing Systems Emerging technologies and applic... | [10.1109/jsac.2019.2904348](https://doi.org/10.1109/jsac.2019.2904348) | [link](https://openalex.org/W2963318081) |
| 16 | EDGE_AI | 9099 | 2020 | 2162 | Federated Learning With Differential Privacy: Algorithms and Performance Analysi | federated learning | propose | 0.87 | Federated Learning With Differential Privacy: Algorithms and Performance Analysis Federated learni... | [10.1109/tifs.2020.2988575](https://doi.org/10.1109/tifs.2020.2988575) | [link](https://openalex.org/W3016632787) |
| 17 | PHOTONICS | 8652 | 2006 | 1969 | The Past, Present, and Future of Silicon Photonics | silicon photonics | propose | 0.70 | The Past, Present, and Future of Silicon Photonics The pace of the development of silicon photonics has quickened since 2004 due t... | [10.1109/jstqe.2006.883151](https://doi.org/10.1109/jstqe.2006.883151) | [link](https://openalex.org/W2099610951) |
| 18 | MEDICAL | 7496 | 2022 | 1726 | Robust deep learning–based protein sequence design using ProteinMPNN | AlphaFold protein | critique | 0.65 | ...studies by rescuing previously failed designs, which were made using Rosetta or AlphaFold, of protein monomers, cyclic homo-oligomers, tetrahedral nanopartic | [10.1126/science.add2187](https://doi.org/10.1126/science.add2187) | [link](https://openalex.org/W4296032638) |
| 19 | EDGE_AI | 9095 | 2021 | 1676 | A survey on federated learning | federated learning | review | 0.70 | A survey on federated learning  | [10.1016/j.knosys.2021.106775](https://doi.org/10.1016/j.knosys.2021.106775) | [link](https://openalex.org/W3123459983) |
| 20 | CROSS | 6722 | 2012 | 1556 | Responsible research and innovation: From science in society to science for soci | responsible innovation | review | 0.78 | ...and unpredictable consequences. Finally, we reflect on possible motivations for responsible innovation itself. | [10.1093/scipol/scs093](https://doi.org/10.1093/scipol/scs093) | [link](https://openalex.org/W2041145756) |
| 21 | MEDICAL | 21474 | 2020 | 1549 | Improved protein structure prediction using predicted interresidue orientations | AlphaFold protein | apply | 0.65 | Improved protein structure prediction using predicted interresidue orientations The prediction of interresidue contac... | [10.1073/pnas.1914677117](https://doi.org/10.1073/pnas.1914677117) | [link](https://openalex.org/W2997234557) |
| 22 | EDGE_AI | 9114 | 2019 | 1524 | Comprehensive Privacy Analysis of Deep Learning: Passive and Active White-box In | federated learning | review | 0.78 | ...earning: Passive and Active White-box Inference Attacks against Centralized and Federated Learning Deep neural networks are susceptible to various inference  | [10.1109/sp.2019.00065](https://doi.org/10.1109/sp.2019.00065) | [link](https://openalex.org/W2930926105) |
| 23 | NEUROMORPHIC | 15669 | 2016 | 1517 | ISAAC | memristor crossbar | review | 0.78 | ... adjacent eDRAM banks. This work explores an in-situ processing approach, where memristor crossbar arrays not only store input weights, but are also used to  | [10.1145/3007787.3001139](https://doi.org/10.1145/3007787.3001139) | [link](https://openalex.org/W2518281301) |
| 24 | CYBER_PHYS | 11880 | 2016 | 1472 | Implementing Smart Factory of Industrie 4.0: An Outlook | smart factory | apply | 0.70 | Implementing Smart Factory of Industrie 4.0: An Outlook With the application of Internet of Things and ser... | [10.1155/2016/3159805](https://doi.org/10.1155/2016/3159805) | [link](https://openalex.org/W1560042744) |
| 25 | EDGE_AI | 9106 | 2019 | 1409 | Client Selection for Federated Learning with Heterogeneous Resources in Mobile E | federated learning | forecast | 0.65 | Client Selection for Federated Learning with Heterogeneous Resources in Mobile Edge We envision a mobile edge computing... | [10.1109/icc.2019.8761315](https://doi.org/10.1109/icc.2019.8761315) | [link](https://openalex.org/W2798720628) |
| 26 | CYBER_PHYS | 9241 | 2018 | 1401 | The industrial internet of things (IIoT): An analysis framework | industrial internet of things | review | 0.78 | The industrial internet of things (IIoT): An analysis framework Historically, Industrial Automation and Control S... | [10.1016/j.compind.2018.04.015](https://doi.org/10.1016/j.compind.2018.04.015) | [link](https://openalex.org/W2805611890) |
| 27 | BRAIN_CI | 10409 | 2008 | 1375 | Filter Bank Common Spatial Pattern (FBCSP) in Brain-Computer Interface | brain-computer interface | propose | 0.72 | Filter Bank Common Spatial Pattern (FBCSP) in Brain-Computer Interface In motor imagery-based Brain Computer Interfaces (BCI), discriminative patterns... | [10.1109/ijcnn.2008.4634130](https://doi.org/10.1109/ijcnn.2008.4634130) | [link](https://openalex.org/W2132360759) |
| 28 | PHOTONICS | 8651 | 2006 | 1365 | Silicon Photonics | silicon photonics | review | 0.65 | Silicon Photonics After dominating the electronics industry for decades, silicon is on the verge ... | [10.1109/jlt.2006.885782](https://doi.org/10.1109/jlt.2006.885782) | [link](https://openalex.org/W4256501225) |
| 29 | EDGE_AI | 9098 | 2021 | 1325 | Model-Contrastive Federated Learning | federated learning | critique | 0.70 | Model-Contrastive Federated Learning Federated learning enables multiple parties to collaboratively train a machine ... | [10.1109/cvpr46437.2021.01057](https://doi.org/10.1109/cvpr46437.2021.01057) | [link](https://openalex.org/W3182158470) |
| 30 | PHOTONICS | 8653 | 2016 | 1293 | Roadmap on silicon photonics | silicon photonics | critique | 0.70 | Roadmap on silicon photonics Silicon photonics research can be dated back to the 1980s. However, the previou... | [10.1088/2040-8978/18/7/073003](https://doi.org/10.1088/2040-8978/18/7/073003) | [link](https://openalex.org/W2468172470) |
| 31 | PHOTONICS | 8653 | 2016 | 1293 | Roadmap on silicon photonics | photonic integrated circuit | propose | 0.70 | .... However, with a growing number of approaches available, what will the silicon photonic integrated circuit of the future look like? This roadmap on silicon  | [10.1088/2040-8978/18/7/073003](https://doi.org/10.1088/2040-8978/18/7/073003) | [link](https://openalex.org/W2468172470) |
| 32 | EDGE_AI | 23841 | 2020 | 1282 | Secure, privacy-preserving and federated machine learning in medical imaging | federated learning | critique | 0.65 | ...ectual property restrictions. AI techniques can help out by offering tools like federated learning to bridge the gap between personal data protection and dat | [10.1038/s42256-020-0186-1](https://doi.org/10.1038/s42256-020-0186-1) | [link](https://openalex.org/W3033511014) |
| 33 | EDGE_AI | 7349 | 2020 | 1280 | A survey on security and privacy of federated learning | federated learning | review | 0.70 | A survey on security and privacy of federated learning  | [10.1016/j.future.2020.10.007](https://doi.org/10.1016/j.future.2020.10.007) | [link](https://openalex.org/W3091870957) |
| 34 | EDGE_AI | 9104 | 2021 | 1273 | Federated Learning for Internet of Things: A Comprehensive Survey | federated learning | review | 0.70 | Federated Learning for Internet of Things: A Comprehensive Survey The Internet of Things (IoT) is ... | [10.1109/comst.2021.3075439](https://doi.org/10.1109/comst.2021.3075439) | [link](https://openalex.org/W3155912831) |
| 35 | TRANSPORT | 603 | 2018 | 1218 | DeepTest | autonomous vehicle Waymo | propose | 0.65 | ...uman intervention. Most major manufacturers including Tesla, GM, Ford, BMW, and Waymo/Google are working on building and testing different types of autonomou | [10.1145/3180155.3180220](https://doi.org/10.1145/3180155.3180220) | [link](https://openalex.org/W2963327228) |
| 36 | CYBER_PHYS | 9109 | 2019 | 1205 | Blockchain and Federated Learning for Privacy-Preserved Data Sharing in Industri | industrial internet of things | propose | 0.70 | ...oT The rapid increase in the volume of data generated from connected devices in industrial Internet of Things paradigm, opens up new possibilities for enhanc | [10.1109/tii.2019.2942190](https://doi.org/10.1109/tii.2019.2942190) | [link](https://openalex.org/W2974429275) |
| 37 | EDGE_AI | 9109 | 2019 | 1205 | Blockchain and Federated Learning for Privacy-Preserved Data Sharing in Industri | federated learning | propose | 0.70 | Blockchain and Federated Learning for Privacy-Preserved Data Sharing in Industrial IoT The rapid increase in the ... | [10.1109/tii.2019.2942190](https://doi.org/10.1109/tii.2019.2942190) | [link](https://openalex.org/W2974429275) |
| 38 | BUILDING | 4045 | 2011 | 1122 | Quantification of crack-healing in novel bacteria-based self-healing concrete | self-healing concrete | propose | 0.70 | Quantification of crack-healing in novel bacteria-based self-healing concrete  | [10.1016/j.cemconcomp.2011.03.012](https://doi.org/10.1016/j.cemconcomp.2011.03.012) | [link](https://openalex.org/W2054780633) |
| 39 | CYBER_PHYS | 11881 | 2017 | 1112 | Smart Factory of Industry 4.0: Key Technologies, Application Case, and Challenge | smart factory | apply | 0.70 | Smart Factory of Industry 4.0: Key Technologies, Application Case, and Challenges Due to the ... | [10.1109/access.2017.2783682](https://doi.org/10.1109/access.2017.2783682) | [link](https://openalex.org/W2771783069) |
| 40 | CYBER_PHYS | 9242 | 2017 | 1097 | Consortium Blockchain for Secure Energy Trading in Industrial Internet of Things | industrial internet of things | critique | 0.72 | Consortium Blockchain for Secure Energy Trading in Industrial Internet of Things In industrial Internet of things (IIoT), peer-to-peer (P2P) energy trading ubiq | [10.1109/tii.2017.2786307](https://doi.org/10.1109/tii.2017.2786307) | [link](https://openalex.org/W2777447168) |
| 41 | NEUROMORPHIC | 13510 | 2016 | 1074 | Neuromorphic computing using non-volatile memory | neuromorphic computing | apply | 0.70 | Neuromorphic computing using non-volatile memory Dense crossbar arrays of non-volatile memory (NVM) de... | [10.1080/23746149.2016.1259585](https://doi.org/10.1080/23746149.2016.1259585) | [link](https://openalex.org/W2560615381) |
| 42 | MEDICAL | 7559 | 2022 | 1072 | Ensembl 2023 | AlphaFold protein | propose | 0.70 | ... Variant Effect Predictor (VEP), interactive protein structure predictions from AlphaFold DB, and the beta release of our new website. | [10.1093/nar/gkac958](https://doi.org/10.1093/nar/gkac958) | [link](https://openalex.org/W4307843054) |
| 43 | MEDICAL | 1566 | 2021 | 1044 | Safety of the BNT162b2 mRNA Covid-19 Vaccine in a Nationwide Setting | mRNA vaccine | critique | 0.65 | ...o size and patient-mix limitations. An evaluation of the safety of the BNT162b2 mRNA vaccine with respect to a broad range of potential adverse events is nee | [10.1056/nejmoa2110475](https://doi.org/10.1056/nejmoa2110475) | [link](https://openalex.org/W3195586393) |
| 44 | EDGE_AI | 7338 | 2019 | 1041 | In-Edge AI: Intelligentizing Mobile Edge Computing, Caching and Communication by | federated learning | propose | 0.70 | ...n-Edge AI: Intelligentizing Mobile Edge Computing, Caching and Communication by Federated Learning Recently, along with the rapid development of mobile commu | [10.1109/mnet.2019.1800286](https://doi.org/10.1109/mnet.2019.1800286) | [link](https://openalex.org/W2962804345) |
| 45 | BRAIN_CI | 12355 | 2019 | 1041 | An Integrated Brain-Machine Interface Platform With Thousands of Channels | Neuralink | apply | 0.65 | ... has achieved a spiking yield of up to 70% in chronically implanted electrodes. Neuralink's approach to brain-machine interface has unprecedented packaging d | [10.2196/16194](https://doi.org/10.2196/16194) | [link](https://openalex.org/W2980609230) |
| 46 | EDGE_AI | 9110 | 2020 | 1024 | Federated Learning via Over-the-Air Computation | federated learning | apply | 0.70 | Federated Learning via Over-the-Air Computation The stringent requirements for low-latency and pri... | [10.1109/twc.2019.2961673](https://doi.org/10.1109/twc.2019.2961673) | [link](https://openalex.org/W2999074226) |
| 47 | EDGE_AI | 9116 | 2019 | 1007 | Federated Learning over Wireless Networks: Optimization Model Design and Analysi | federated learning | propose | 0.70 | Federated Learning over Wireless Networks: Optimization Model Design and Analysis There is an incr... | [10.1109/infocom.2019.8737464](https://doi.org/10.1109/infocom.2019.8737464) | [link](https://openalex.org/W2920095265) |
| 48 | NEUROMORPHIC | 13509 | 2022 | 1006 | Opportunities for neuromorphic computing algorithms and applications | neuromorphic computing | apply | 0.70 | Opportunities for neuromorphic computing algorithms and applications  | [10.1038/s43588-021-00184-y](https://doi.org/10.1038/s43588-021-00184-y) | [link](https://openalex.org/W4210357113) |
| 49 | CYBER_PHYS | 30709 | 2017 | 997 | Industry 4.0 Concept: Background and Overview | smart factory | apply | 0.65 | ...its drivers, enablers, goals and limitations. Building blocks are described and smart factory concept is presented. A Reference Architecture Model RAMI4.0 an | [10.3991/ijim.v11i5.7072](https://doi.org/10.3991/ijim.v11i5.7072) | [link](https://openalex.org/W2737940375) |
| 50 | EDGE_AI | 9118 | 2022 | 988 | Federated Learning on Non-IID Data Silos: An Experimental Study | federated learning | review | 0.78 | Federated Learning on Non-IID Data Silos: An Experimental Study Due to the increasing privacy conc... | [10.1109/icde53745.2022.00077](https://doi.org/10.1109/icde53745.2022.00077) | [link](https://openalex.org/W4287332481) |
| 51 | EDGE_AI | 9102 | 2022 | 987 | Towards Personalized Federated Learning | federated learning | propose | 0.70 | Towards Personalized Federated Learning In parallel with the rapid adoption of artificial intelligence (AI) empowered b... | [10.1109/tnnls.2022.3160699](https://doi.org/10.1109/tnnls.2022.3160699) | [link](https://openalex.org/W3133814152) |
| 52 | MEDICAL | 7544 | 2022 | 975 | Dali server: structural unification of protein families | AlphaFold protein | propose | 0.70 | ...ost recent upgrades to the web server: (i) the foldomes of key organisms in the AlphaFold Database (version 1) are searchable by Dali, (ii) structural alignm | [10.1093/nar/gkac387](https://doi.org/10.1093/nar/gkac387) | [link](https://openalex.org/W4282922306) |
| 53 | MEDICAL | 34566 | 2006 | 951 | Length-dependent prediction of protein intrinsic disorder | AlphaFold protein | propose | 0.65 | ...rch as witnessed in the 6th experiment on Critical Assessment of Techniques for Protein Structure Prediction (CASP6). Since the initial work by Romero et al. | [10.1186/1471-2105-7-208](https://doi.org/10.1186/1471-2105-7-208) | [link](https://openalex.org/W1792685479) |
| 54 | EDGE_AI | 9112 | 2020 | 945 | Optimizing Federated Learning on Non-IID Data with Reinforcement Learning | federated learning | apply | 0.70 | Optimizing Federated Learning on Non-IID Data with Reinforcement Learning The widespread deployment of machin... | [10.1109/infocom41043.2020.9155494](https://doi.org/10.1109/infocom41043.2020.9155494) | [link](https://openalex.org/W3047304572) |
| 55 | TRANSPORT | 639 | 2021 | 940 | Voxel R-CNN: Towards High Performance Voxel-based 3D Object Detection | autonomous vehicle Waymo | apply | 0.65 | ... experiments are conducted on the widely used KITTI Dataset and the more recent Waymo Open Dataset. Our results show that compared to existing voxel-based me | [10.1609/aaai.v35i2.16207](https://doi.org/10.1609/aaai.v35i2.16207) | [link](https://openalex.org/W3118341329) |
| 56 | EDGE_AI | 9107 | 2021 | 934 | Federated learning on non-IID data: A survey | federated learning | review | 0.70 | Federated learning on non-IID data: A survey  | [10.1016/j.neucom.2021.07.098](https://doi.org/10.1016/j.neucom.2021.07.098) | [link](https://openalex.org/W3196371845) |
| 57 | EDGE_AI | 9122 | 2019 | 926 | Incentive Mechanism for Reliable Federated Learning: A Joint Optimization Approa | federated learning | propose | 0.72 | Incentive Mechanism for Reliable Federated Learning: A Joint Optimization Approach to Combining Reputation and Contract Theory Fede... | [10.1109/jiot.2019.2940820](https://doi.org/10.1109/jiot.2019.2940820) | [link](https://openalex.org/W2972882814) |
| 58 | EDGE_AI | 9117 | 2021 | 925 | Federated Learning for Internet of Things: A Comprehensive Survey | federated learning | review | 0.70 | Federated Learning for Internet of Things: A Comprehensive Survey The Internet of Things (IoT) is ... |  | [link](https://openalex.org/W3159080474) |
| 59 | PHOTONICS | 8656 | 2021 | 919 | Review of Silicon Photonics Technology and Platform Development | silicon photonics | propose | 0.70 | Review of Silicon Photonics Technology and Platform Development Many breakthroughs in the laboratories ofte... | [10.1109/jlt.2021.3066203](https://doi.org/10.1109/jlt.2021.3066203) | [link](https://openalex.org/W3188674373) |
| 60 | NEUROMORPHIC | 15569 | 2011 | 906 | A Functional Hybrid Memristor Crossbar-Array/CMOS System for Data Storage and Ne | memristor crossbar | propose | 0.70 | A Functional Hybrid Memristor Crossbar-Array/CMOS System for Data Storage and Neuromorphic Applications Crossbar array... | [10.1021/nl203687n](https://doi.org/10.1021/nl203687n) | [link](https://openalex.org/W2323986115) |
| 61 | EDGE_AI | 9111 | 2019 | 903 | A Hybrid Approach to Privacy-Preserving Federated Learning | federated learning | apply | 0.70 | A Hybrid Approach to Privacy-Preserving Federated Learning Federated learning facilitates the collaborative training of models without the... | [10.1145/3338501.3357370](https://doi.org/10.1145/3338501.3357370) | [link](https://openalex.org/W2970606380) |
| 62 | CYBER_PHYS | 9244 | 2015 | 894 | Security and privacy challenges in industrial internet of things | industrial internet of things | apply | 0.70 | Security and privacy challenges in industrial internet of things Today, embedded, mobile, and cyberphysical systems are ubiquitous and used in m... | [10.1145/2744769.2747942](https://doi.org/10.1145/2744769.2747942) | [link](https://openalex.org/W2065955975) |
| 63 | EDGE_AI | 9140 | 2022 | 884 | Edge-IIoTset: A New Comprehensive Realistic Cyber Security Dataset of IoT and II | federated learning | propose | 0.70 | ...alistic Cyber Security Dataset of IoT and IIoT Applications for Centralized and Federated Learning In this paper, we propose a new comprehensive realistic cy | [10.1109/access.2022.3165809](https://doi.org/10.1109/access.2022.3165809) | [link](https://openalex.org/W4226319939) |
| 64 | MEDICAL | 1505 | 2019 | 868 | Optimization of Lipid Nanoparticles for Intramuscular Administration of mRNA Vac | mRNA vaccine | apply | 0.65 | ...n driven by LNPs does not equate to increased immunogenicity, illustrating that mRNA vaccine tolerability can be improved without affecting potency. | [10.1016/j.omtn.2019.01.013](https://doi.org/10.1016/j.omtn.2019.01.013) | [link](https://openalex.org/W2914060533) |
| 65 | PHOTONICS | 8659 | 2014 | 865 | Experimental demonstration of reservoir computing on a silicon photonics chip | silicon photonics | apply | 0.70 | Experimental demonstration of reservoir computing on a silicon photonics chip In today's age, companies employ machine learning to extract information f... | [10.1038/ncomms4541](https://doi.org/10.1038/ncomms4541) | [link](https://openalex.org/W2029939668) |
| 66 | EDGE_AI | 9105 | 2019 | 864 | Blockchained On-Device Federated Learning | federated learning | propose | 0.70 | Blockchained On-Device Federated Learning By leveraging blockchain, this letter proposes a blockchained federated learnin... | [10.1109/lcomm.2019.2921755](https://doi.org/10.1109/lcomm.2019.2921755) | [link](https://openalex.org/W2951832089) |
| 67 | EDGE_AI | 9105 | 2019 | 864 | Blockchained On-Device Federated Learning | on-device machine learning | propose | 0.70 | ...ure where local learning model updates are exchanged and verified. This enables on-device machine learning without any centralized training data or coordinat | [10.1109/lcomm.2019.2921755](https://doi.org/10.1109/lcomm.2019.2921755) | [link](https://openalex.org/W2951832089) |
| 68 | NEUROMORPHIC | 13511 | 2018 | 855 | Neuromorphic computing with multi-memristive synapses | spiking neural network | propose | 0.72 | ...hange memory devices for unsupervised learning of temporal correlations using a spiking neural network. The work presents a significant step towards the real | [10.1038/s41467-018-04933-y](https://doi.org/10.1038/s41467-018-04933-y) | [link](https://openalex.org/W2769049661) |
| 69 | NEUROMORPHIC | 13511 | 2018 | 855 | Neuromorphic computing with multi-memristive synapses | neuromorphic computing | propose | 0.70 | Neuromorphic computing with multi-memristive synapses Neuromorphic computing has emerged as a promisin... | [10.1038/s41467-018-04933-y](https://doi.org/10.1038/s41467-018-04933-y) | [link](https://openalex.org/W2769049661) |
| 70 | PHOTONICS | 8657 | 2017 | 819 | Neuromorphic photonic networks using silicon photonic weight banks | silicon photonics | apply | 0.65 | ...erformance information processing have attracted renewed interest. Neuromorphic silicon photonics has the potential to integrate processing functions that va | [10.1038/s41598-017-07754-z](https://doi.org/10.1038/s41598-017-07754-z) | [link](https://openalex.org/W2739588406) |
| 71 | CYBER_PHYS | 9245 | 2020 | 815 | Edge Computing in Industrial Internet of Things: Architecture, Advances and Chal | industrial internet of things | critique | 0.70 | Edge Computing in Industrial Internet of Things: Architecture, Advances and Challenges The Industrial Internet of Things (IIoT)... | [10.1109/comst.2020.3009103](https://doi.org/10.1109/comst.2020.3009103) | [link](https://openalex.org/W3043320740) |
| 72 | BRAIN_CI | 10413 | 2011 | 806 | Multiclass Brain–Computer Interface Classification by Riemannian Geometry | brain-computer interface | propose | 0.70 | ...n by Riemannian Geometry This paper presents a new classification framework for brain-computer interface (BCI) based on motor imagery. This framework involve | [10.1109/tbme.2011.2172210](https://doi.org/10.1109/tbme.2011.2172210) | [link](https://openalex.org/W2096597330) |
| 73 | EDGE_AI | 9130 | 2019 | 801 | Beyond Inferring Class Representatives: User-Level Privacy Leakage From Federate | federated learning | review | 0.78 | Beyond Inferring Class Representatives: User-Level Privacy Leakage From Federated Learning Federated learning, i.e., a mobile edge computing framework for deep  | [10.1109/infocom.2019.8737416](https://doi.org/10.1109/infocom.2019.8737416) | [link](https://openalex.org/W2964162474) |
| 74 | MEDICAL | 7475 | 2024 | 790 | InterPro: the protein sequence classification resource in 2025 | AlphaFold protein | propose | 0.70 | ...sources, such as Gene Ontology (GO), Protein Data Bank in Europe (PDBe) and the AlphaFold Protein Structure Database. In this publication, we report on the s | [10.1093/nar/gkae1082](https://doi.org/10.1093/nar/gkae1082) | [link](https://openalex.org/W4404531735) |
| 75 | NEUROMORPHIC | 13513 | 2016 | 786 | Convolutional networks for fast, energy-efficient neuromorphic computing | neuromorphic computing | apply | 0.70 | Convolutional networks for fast, energy-efficient neuromorphic computing Deep networks are now able to achieve human-level performance on a broad spectr... | [10.1073/pnas.1604850113](https://doi.org/10.1073/pnas.1604850113) | [link](https://openalex.org/W2314470091) |
| 76 | EDGE_AI | 9113 | 2019 | 780 | VerifyNet: Secure and Verifiable Federated Learning | federated learning | propose | 0.72 | VerifyNet: Secure and Verifiable Federated Learning As an emerging training model with neural networks, federated learning has rece... | [10.1109/tifs.2019.2929409](https://doi.org/10.1109/tifs.2019.2929409) | [link](https://openalex.org/W2963540401) |
| 77 | BRAIN_CI | 10416 | 2010 | 780 | Convolutional Neural Networks for P300 Detection with Application to Brain-Compu | brain-computer interface | apply | 0.70 | ...ral Networks for P300 Detection with Application to Brain-Computer Interfaces A Brain-Computer Interface (BCI) is a specific type of human-computer interface | [10.1109/tpami.2010.125](https://doi.org/10.1109/tpami.2010.125) | [link](https://openalex.org/W2150590430) |
| 78 | BRAIN_CI | 10436 | 2009 | 765 | An online multi-channel SSVEP-based brain–computer interface using a canonical c | brain-computer interface | propose | 0.72 | ...en increasing interest in using steady-state visual evoked potential (SSVEP) in brain-computer interface (BCI) systems. However, several aspects of current S | [10.1088/1741-2560/6/4/046002](https://doi.org/10.1088/1741-2560/6/4/046002) | [link](https://openalex.org/W2105478324) |
| 79 | CROSS | 3596 | 2006 | 760 | Innovation diffusion in global contexts: determinants of post-adoption digital t | innovation diffusion | propose | 0.72 | Innovation diffusion in global contexts: determinants of post-adoption digital transformation of Eur... | [10.1057/palgrave.ejis.3000650](https://doi.org/10.1057/palgrave.ejis.3000650) | [link](https://openalex.org/W2050091520) |
| 80 | EDGE_AI | 9134 | 2020 | 760 | A Survey on Federated Learning: The Journey From Centralized to Distributed On-S | federated learning | review | 0.70 | A Survey on Federated Learning: The Journey From Centralized to Distributed On-Site Learning and Beyond Driven... | [10.1109/jiot.2020.3030072](https://doi.org/10.1109/jiot.2020.3030072) | [link](https://openalex.org/W3135231128) |
| 81 | MEDICAL | 7535 | 2022 | 749 | ProtGPT2 is a deep unsupervised language model for protein design | AlphaFold protein | apply | 0.70 | ...ther demonstrate that ProtGPT2 is sampling unexplored regions of protein space. AlphaFold prediction of ProtGPT2-sequences yields well-folded non-idealized s | [10.1038/s41467-022-32007-7](https://doi.org/10.1038/s41467-022-32007-7) | [link](https://openalex.org/W4288066876) |
| 82 | NEUROMORPHIC | 15665 | 2018 | 733 | Memristor‐Based Analog Computation and Neural Network Classification with a Dot  | memristor crossbar | apply | 0.70 | ...g Computation and Neural Network Classification with a Dot Product Engine Using memristor crossbar arrays to accelerate computations is a promising approach  | [10.1002/adma.201705914](https://doi.org/10.1002/adma.201705914) | [link](https://openalex.org/W2782791387) |
| 83 | MEDICAL | 5754 | 2017 | 730 | CRISPR/Cas9-mediated PD-1 disruption enhances anti-tumor efficacy of human chime | CAR-T cell therapy | propose | 0.70 | ...but the clinical potential of combined disruption of inhibitory checkpoints and CAR T cell therapy remains incompletely explored. Here we show that programme | [10.1038/s41598-017-00462-8](https://doi.org/10.1038/s41598-017-00462-8) | [link](https://openalex.org/W2604982880) |
| 84 | NEUROMORPHIC | 13520 | 2019 | 728 | Parallel programming of an ionic floating-gate memory array for scalable neuromo | neuromorphic computing | propose | 0.72 | Parallel programming of an ionic floating-gate memory array for scalable neuromorphic computing Neuromorphic computers could overcome efficiency bottlenecks inh | [10.1126/science.aaw5581](https://doi.org/10.1126/science.aaw5581) | [link](https://openalex.org/W2942216650) |
| 85 | EDGE_AI | 9135 | 2020 | 722 | Blockchain Empowered Asynchronous Federated Learning for Secure Data Sharing in  | federated learning | propose | 0.77 | Blockchain Empowered Asynchronous Federated Learning for Secure Data Sharing in Internet of Vehicles In Internet of Vehicles (IoV), ... | [10.1109/tvt.2020.2973651](https://doi.org/10.1109/tvt.2020.2973651) | [link](https://openalex.org/W3006655855) |
| 86 | SAFETY_AI | 4343 | 2023 | 716 | Summary of ChatGPT-Related research and perspective towards the future of large  | RLHF reinforcement learning human feedba | review | 0.88 | ...de web, instruction fine-tuning and Reinforcement Learning from Human Feedback (RLHF) have played significant roles in enhancing LLMs’ adaptability and perfo | [10.1016/j.metrad.2023.100017](https://doi.org/10.1016/j.metrad.2023.100017) | [link](https://openalex.org/W4385988359) |
| 87 | EDGE_AI | 9119 | 2022 | 712 | A survey on federated learning: challenges and applications | federated learning | review | 0.70 | A survey on federated learning: challenges and applications  | [10.1007/s13042-022-01647-y](https://doi.org/10.1007/s13042-022-01647-y) | [link](https://openalex.org/W4309080560) |
| 88 | EDGE_AI | 9125 | 2021 | 708 | A Survey on Federated Learning for Resource-Constrained IoT Devices | federated learning | review | 0.70 | A Survey on Federated Learning for Resource-Constrained IoT Devices Federated learning (FL) is a distributed m... | [10.1109/jiot.2021.3095077](https://doi.org/10.1109/jiot.2021.3095077) | [link](https://openalex.org/W3182125009) |
| 89 | TRANSPORT | 6561 | 2017 | 701 | Coherent solid-state LIDAR with silicon photonic optical phased arrays | solid-state lidar | apply | 0.70 | Coherent solid-state LIDAR with silicon photonic optical phased arrays We present, to the best of our know... | [10.1364/ol.42.004091](https://doi.org/10.1364/ol.42.004091) | [link](https://openalex.org/W2761155850) |
| 90 | PHOTONICS | 6561 | 2017 | 701 | Coherent solid-state LIDAR with silicon photonic optical phased arrays | silicon photonics | propose | 0.70 | ...olid-state light detection and ranging (LIDAR) using optical phased arrays in a silicon photonics platform. An integrated transmitting and receiving frequenc | [10.1364/ol.42.004091](https://doi.org/10.1364/ol.42.004091) | [link](https://openalex.org/W2761155850) |
| 91 | EDGE_AI | 9123 | 2020 | 693 | Federated Learning: A Survey on Enabling Technologies, Protocols, and Applicatio | federated learning | review | 0.70 | Federated Learning: A Survey on Enabling Technologies, Protocols, and Applications This paper prov... | [10.1109/access.2020.3013541](https://doi.org/10.1109/access.2020.3013541) | [link](https://openalex.org/W3046653923) |
| 92 | CYBER_PHYS | 9243 | 2016 | 692 | Blockchain Platform for Industrial Internet of Things | industrial internet of things | apply | 0.70 | Blockchain Platform for Industrial Internet of Things Internet of Things (IoT) are being adopted for industrial and manufacturing app... | [10.4236/jsea.2016.910036](https://doi.org/10.4236/jsea.2016.910036) | [link](https://openalex.org/W2540162589) |
| 93 | EDGE_AI | 9131 | 2021 | 692 | Federated learning for predicting clinical outcomes in patients with COVID-19 | federated learning | apply | 0.65 | Federated learning for predicting clinical outcomes in patients with COVID-19 Federated learning (... | [10.1038/s41591-021-01506-3](https://doi.org/10.1038/s41591-021-01506-3) | [link](https://openalex.org/W3200840849) |
| 94 | MEDICAL | 7523 | 2022 | 682 | DALI shines a light on remote homologs: One hundred discoveries | AlphaFold protein | critique | 0.72 | ...-coded sequence and structure conservation. Here, we are using DALI to mine the AlphaFold Database version 1, which increased the structural coverage of prot | [10.1002/pro.4519](https://doi.org/10.1002/pro.4519) | [link](https://openalex.org/W4309858927) |
| 95 | NEUROMORPHIC | 11249 | 2018 | 677 | Photonic Synapses Based on Inorganic Perovskite Quantum Dots for Neuromorphic Co | neuromorphic computing | apply | 0.72 | Photonic Synapses Based on Inorganic Perovskite Quantum Dots for Neuromorphic Computing QDs and semiconductor layer serves as a basis for optically programmable | [10.1002/adma.201802883](https://doi.org/10.1002/adma.201802883) | [link](https://openalex.org/W2886721396) |
| 96 | CYBER_PHYS | 9246 | 2016 | 675 | Software-Defined Industrial Internet of Things in the Context of Industry 4.0 | industrial internet of things | propose | 0.77 | Software-Defined Industrial Internet of Things in the Context of Industry 4.0 In recent years, there have been great advances ... | [10.1109/jsen.2016.2565621](https://doi.org/10.1109/jsen.2016.2565621) | [link](https://openalex.org/W2364839527) |
| 97 | NEUROMORPHIC | 13516 | 2016 | 672 | Dot-product engine for neuromorphic computing | neuromorphic computing | apply | 0.70 | Dot-product engine for neuromorphic computing Vector-matrix multiplication dominates the computation time and energy for many... | [10.1145/2897937.2898010](https://doi.org/10.1145/2897937.2898010) | [link](https://openalex.org/W2399958287) |
| 98 | NEUROMORPHIC | 13516 | 2016 | 672 | Dot-product engine for neuromorphic computing | memristor crossbar | propose | 0.70 | ...crete Fourier Transform). Utilizing the natural current accumulation feature of memristor crossbar, we developed the Dot-Product Engine (DPE) as a high densi | [10.1145/2897937.2898010](https://doi.org/10.1145/2897937.2898010) | [link](https://openalex.org/W2399958287) |
| 99 | EDGE_AI | 9136 | 2020 | 670 | Privacy-Preserving Traffic Flow Prediction: A Federated Learning Approach | federated learning | critique | 0.72 | Privacy-Preserving Traffic Flow Prediction: A Federated Learning Approach Existing traffic flow forecasting approaches by deep learning models a... | [10.1109/jiot.2020.2991401](https://doi.org/10.1109/jiot.2020.2991401) | [link](https://openalex.org/W3010852232) |
| 100 | BRAIN_CI | 10422 | 2018 | 653 | Learning Temporal Information for Brain-Computer Interface Using Convolutional N | brain-computer interface | review | 0.78 | Learning Temporal Information for Brain-Computer Interface Using Convolutional Neural Networks Deep learning (DL) methods and architecture... | [10.1109/tnnls.2018.2789927](https://doi.org/10.1109/tnnls.2018.2789927) | [link](https://openalex.org/W2792724009) |

---

## 抽出メタデータ

- **抽出日時**: 2026-05-18
- **抽出スクリプト**: `/tmp/build_ftt_evidence.py`
- **SQLite クエリ**: paper_domain_map JOIN 経由で 10 領域の論文・milestone・forecast・TRL・genealogy・mention を一括取得
- **品質ゲート**: OpenAlex 実在率 100% / source_url 100% / DOI 充足率 (top papers の大半に有)
- **既知の限界**:
  - mention_type の verified フラグは現状 0 件 (rule-based 抽出のため) -> confidence で代替
  - abstract 充足率 79.1% (残 20.9% は OpenAlex 側で取得不可)
  - 領域 BUILDING / PHOTONICS は Physical AI 直結度がやや弱い (参考扱い)

**次工程への引き渡し**:
- 教科書ブラッシュアップ時の引用根拠として、本ファイル内 DOI を一次優先
- 日本人著者は所属が JP の affiliation_raw で抽出済 -> ep007 正本型「日本人研究者 >=1 名」要件に対応可
- TRL / Milestone / Forecast の 3 軸で 2025-2100 年の時系列展開が可能
