# エグゼクティブサマリ

ソフトロボット材料は2026年時点で、空気圧・ゴム材料の量産実装、DEA/HASEL/LCEの高性能化、自己修復・リサイクル材料の耐久化、バイオハイブリッド筋肉の力伝達改善が同時進行している。実用化は食品把持・触覚ハンド・外骨格が先行し、ヒューマノイド全身筋肉への置換は未到達である。2030年までの主戦場は「材料単体性能」ではなく、触覚センサー、制御、製造歩留まり、修理可能性を含む統合設計になる。

## 材料カテゴリ別技術成熟度 TRL マトリクス

| 材料・アクチュエータ | 2026 TRL | 到達点 | 未解決課題 | source_url |
|---|---:|---|---|---|
| McKibben / PAM | 7-9 | 食品把持、外骨格、研究用筋骨格ロボットで実装済み。2025年レビューは高出力重量比・安全な人接触を主要利点と整理。 | コンプレッサ、バルブ、ヒステリシス、精密制御。 | https://www.mdpi.com/2076-0825/14/12/582 |
| ゴム空気圧ソフトグリッパ | 8-9 | Soft Robotics Inc. mGripAI、Bridgestone Tetoteなどで商用ライン投入。 | 寿命、洗浄、食品別チューニング。 | https://www.softroboticsinc.com/aboutus/ , https://www.japanrubberweekly.com/2025/02/bridgestone-soft-robotics-ventures-debuts-moving-soft-robotics-using-tetote/ |
| SMA NiTi | 5-7 | 2025-2026年にSMAソフトアーム、空気圧+SMA閉ループ、NiTiワイヤ多形態ロボットが報告。 | 冷却律速、熱管理、疲労、効率。 | https://www.sciencedirect.com/science/article/abs/pii/S259023852600024X , https://arxiv.org/abs/2506.05741 |
| Cu-Al-Ni / Cu系SMA | 3-5 | 高温・低温・宇宙用途向け材料研究が中心。Cu-Al-Niは高変態温度系として研究されるが、ロボット量産応用はNiTiより遅い。 | 脆性、粒界破壊、加工性、疲労。 | https://www.reddit.com/r/materials/comments/1ozm9kn/superelasticshape_memory_alloy/ , https://phys.org/news/2025-07-copper-alloy-memory-effect-200c.pdf |
| HASEL | 4-6 | Peano-HASELは10%収縮、900%/s、50Hz、200倍自重リフトを実証。2025年は多チャンネル高電圧駆動で16.057Hz駆動を報告。 | kV級電圧、封止、誘電液、量産安全規格。 | https://pubmed.ncbi.nlm.nih.gov/33141696/ , https://www.mdpi.com/2076-0825/14/12/601 |
| DEA | 4-6 | 2025年に自己修復ポリイオン液体電極で切断後96%面ひずみ回復、2026年に自己修復DEA人工筋肉。 | 高電界、絶縁破壊、薄膜量産、湿度耐性。 | https://www.nature.com/articles/s41467-025-62796-6 , https://www.nature.com/articles/s41467-026-72611-5 |
| Electrostrictive PVDF / P(VDF-TrFE-CFE) | 3-5 | センサー・薄膜駆動・ウェアラブル向け。高周波・薄型に強いが大変位筋肉用途は限定。 | 低ひずみ、駆動電圧、機械仕事密度。 | https://www.nature.com/articles/s44182-025-00030-7 |
| LCE | 3-6 | 2025年に幾何非依存LCE、RF選択駆動、液体金属統合LCEなどが進展。 | 熱応答速度、放熱、繰返し安定性、電気直駆動。 | https://www.nature.com/articles/s41467-025-62883-8 , https://www.nature.com/articles/s41467-025-62313-9 |
| 自己修復・リサイクル材料 | 3-6 | 2025年レビューは自己修復ポリマー、センサー、統合ロボットを整理。ETHは動的共有結合ポリマーで自己修復・リサイクルを研究。 | 実環境損傷、修復時間、機械強度との両立。 | https://link.springer.com/article/10.1007/s12541-025-01272-z , https://robotic.mat.ethz.ch/research/sustainable-robotics.html |
| バイオハイブリッド筋肉 | 2-4 | MITは2025年に多方向収縮組織、人工腱で3倍高速・30倍力の指動作。ETHは筋肉-腱界面を3Dバイオプリント。 | 栄養供給、寿命、滅菌、標準化、屋外運用。 | https://news.mit.edu/2025/artificial-muscle-flexes-multiple-directions-offering-path-soft-wiggly-robots-0317 , https://news.mit.edu/2025/artificial-tendons-give-muscle-powered-robots-boost-1201 , https://mavt.ethz.ch/news-and-events/d-mavt-news/2025/09/biohybrid-robotics-muscles-and-tendons-for-robots.html |

## 主要研究機関・企業の最新成果 2025-2026

### Self-healing materials

自己修復ソフトロボットは、2025年レビューで「材料、損傷検知センサー、統合システム」の3層に整理された。少損傷は約9分で封止、大損傷は70℃・30分加熱という例が示され、自己修復だけでなく損傷位置検出と再処理性が評価軸になっている。source_url: https://link.springer.com/article/10.1007/s12541-025-01272-z

Stanfordは2025年にBao LabがNatureで高密度ソフト生体電子ファイバーを発表し、皮膚様材料・スマート繊維・ソフトロボット応用を示した。自己修復そのものの2025-2026論文は今回確認できた一次資料内では特定できず、Bao Labの自己修復多層電子皮膚は既存成果として継続参照されている。source_url: https://neuroscience.stanford.edu/publications/high-density-soft-bioelectronic-fibres-multimodal-sensing-and-stimulation , https://baogroup.stanford.edu/news/layers-self-healing-electronic-skin-realign-autonomously-when-cut

MITは2026年に光で導電率が400倍変化するソフト光イオントロニクスゲルをNature Communicationsで報告した。これは自己修復ではないが、ソフト材料内で情報処理・刺激応答を担わせる方向で、ソフトロボット材料の「感覚と制御の材料内統合」を進める成果である。source_url: https://news.mit.edu/2026/light-activated-gel-could-impact-wearables-soft-robotics-more-0416

EPFLは2025年に300V級の微細zipping electrohydraulic actuatorを報告し、従来の1-5kV級から低電圧化したミリロボット向け製造に進んだ。自己修復を主題にしたEPFL 2025-2026一次論文は今回の確認範囲では限定的で、同校では可変剛性・スマート材料・ソフトマシン製造が主軸である。source_url: https://graphsearch.epfl.ch/fr/publication/3d520532-77da-4e51-aaad-4018f137663e

ETH Zürichは2025年に自己修復・リサイクル可能な動的共有結合ポリマーをロボティック材料として展開し、動的シリコーンの自己修復ロボットスキンも報告している。持続可能ロボットを「損傷に賢い、自己修復、破局故障後も復帰、終末期にリサイクル可能」と定義している点が重要である。source_url: https://robotic.mat.ethz.ch/research/sustainable-robotics.html , https://www.research-collection.ethz.ch/items/55294347-06b4-4091-b491-383107b1b053

### 人工筋肉

MIT Media LabとPolitecnico di Bariは2026年Science RoboticsでElectrofluidic Fiber Musclesを報告した。4kgを持ち上げ、これは筋肉束自重の200倍、30mmストローク、180mm/sの高速レバー、40度曲げロボットアームを実証した。source_url: https://www.science.org/doi/10.1126/scirobotics.ady6438 , https://news.mit.edu/2026/new-type-electrically-driven-artificial-muscle-fiber-0409

HASELはBoulder Keplinger Lab起源の電気油圧人工筋肉で、2018年Peano-HASELが基準性能を示した。2025年には低コスト多チャンネル高電圧電源で平均16.057Hz駆動が報告され、ロボット実装時の電源・制御ボトルネックが焦点になっている。source_url: https://pubmed.ncbi.nlm.nih.gov/33141696/ , https://www.mdpi.com/2076-0825/14/12/601

DEAは2025-2026年に自己修復材料が明確に進展した。2025年Nature Communicationsは自己修復ポリイオン液体電極により切断・修復後も32V/μmで元の面ひずみの約96%を維持し、水中グリッパを実証した。2026年Nature Communicationsは自己修復DEA人工筋肉を発表した。source_url: https://www.nature.com/articles/s41467-025-62796-6 , https://www.nature.com/articles/s41467-026-72611-5

LCEは2025年に、幾何依存性を下げるdeform-and-go設計、RF周波数選択駆動、液体金属統合LCEが報告された。LCEの強みは材料内に変形プログラムを埋め込める点で、弱みは熱駆動の応答と冷却である。source_url: https://www.nature.com/articles/s41467-025-62883-8 , https://www.nature.com/articles/s41467-025-62313-9

## 人工筋肉ベンチマーク

| 技術 | 出力/重量比・力 | 応答速度 | サイクル寿命 | 2026評価 | source_url |
|---|---|---|---|---|---|
| McKibben PAM | 高い。2025年pouch PAMは70kPaで51.09%収縮、243.94N。 | バルブ・空圧系依存。2025年TLVで収縮応答約300倍、排気約230倍改善。 | ゴム・繊維疲労依存。産業用途では交換前提。 | 量産最有力だが空圧インフラが重い。 | https://www.sciencedirect.com/science/article/pii/S1000934525000884 , https://colab.ws/articles/10.1109%2Fsii59315.2025.10871086 |
| HASEL | 200倍自重リフト、10%収縮。 | 900%/s、50Hz。2025電源系で16.057Hz。 | 封止・絶縁破壊が寿命要因。 | 電気直駆動の有力候補だがkV安全設計が必要。 | https://pubmed.ncbi.nlm.nih.gov/33141696/ , https://www.mdpi.com/2076-0825/14/12/601 |
| Electrofluidic Fiber Muscle | 4kg、200倍自重、30mmストローク。 | 180mm/s、0.3秒未満の投射デモ。 | 2026時点で長期量産寿命は未公表。 | 繊維状・外部ポンプ不要でウェアラブル向け有望。 | https://www.science.org/doi/10.1126/scirobotics.ady6438 |
| DEA | 高速・軽量。2025年自己修復電極で96%性能回復。 | ms-10ms級が可能な方式だが実装依存。 | 絶縁破壊、電極劣化が支配。 | 薄膜・触覚・光学素子に近い用途が先行。 | https://www.nature.com/articles/s41467-025-62796-6 |
| SMA NiTi | 高力密度、静音、小型。 | 冷却律速。2025年AI制御レビューは精密制御の課題を整理。 | 熱機械疲労が支配。 | 小型グリッパ、医療、航空軽量アーム向け。 | https://pubmed.ncbi.nlm.nih.gov/40731688/ , https://journals.sagepub.com/doi/abs/10.1177/1045389X251356103 |
| LCE | 大ひずみ・プログラム変形。 | 熱・光・RF駆動で応答は設計依存。 | 光熱疲労・配向安定性が課題。 | 微小ロボット、折紙、医療挿入具に適合。 | https://www.nature.com/articles/s41467-025-62883-8 |
| 生体筋肉 | ATP駆動で自己修復・高効率の潜在性。 | 組織成熟・刺激設計依存。MIT人工腱で3倍高速化。 | 培養維持が制約。 | 研究TRL。医療・生物模倣で突破口。 | https://news.mit.edu/2025/artificial-tendons-give-muscle-powered-robots-boost-1201 |

## バイオハイブリッドの突破口

Harvard Parker Labは2025年Science Roboticsで、機械学習により組織工学rayの設計を最適化した。非線形最適化より高性能形状を選べることを示し、バイオハイブリッドの設計が経験則からデータ駆動へ移行した。source_url: https://diseasebiophysics.seas.harvard.edu/publication/bioinspired-design-tissue-engineered-ray-machine-learning

MIT Raman Labは2025年3月に、筋細胞を溝付きハイドロゲルに成長させ、同心円方向と半径方向の両方へ収縮できる人工筋肉組織を示した。さらに2025年12月には人工腱を導入し、同じ筋肉駆動ロボット指で3倍速く、30倍大きな力でピンチ動作を行った。source_url: https://news.mit.edu/2025/artificial-muscle-flexes-multiple-directions-offering-path-soft-wiggly-robots-0317 , https://news.mit.edu/2025/artificial-tendons-give-muscle-powered-robots-boost-1201

ETH Zürich Soft Robotics Labは2025年に、3Dバイオプリントされた筋肉-腱-骨格界面を用い、筋肉と人工骨格の力伝達ロスを下げるbiohybrid actuatorをScience Advancesで報告した。source_url: https://mavt.ethz.ch/news-and-events/d-mavt-news/2025/09/biohybrid-robotics-muscles-and-tendons-for-robots.html

バイオハイブリッドの現在の限界は明確である。栄養供給、培養環境、滅菌、個体差、長時間動作が未解決で、2030年以前の大規模産業ロボット筋肉には不適である。一方、医療デバイス、薬物送達、心筋モデル、微小泳動ロボットでは研究価値が高い。source_url: https://www.nature.com/articles/s44182-025-00049-w

## 日本機関の独自貢献

東大・鈴森系の流れは、空気圧ゴム人工筋肉、タフロボティクス、細径人工筋肉の実装志向にある。JST ImPACTタフ・ロボティクス・チャレンジでは、5MPa駆動で1万回以上の繰返し耐久性を持つ高出力人工筋肉プロトタイプが報告された。source_url: https://www.jst.go.jp/impact/report/data/program07/h28/trc_2813.pdf

早稲田・高西研は、ヒューマノイドで身体内保存力学的エネルギーを活用する研究を2021-2025年度科研費で進め、筋肉・腱・骨格を含む人型運動の機械設計に強みを持つ。ソフト材料単体より、ヒューマノイド全身統合が貢献領域である。source_url: https://www.waseda.jp/inst/fro/assets/uploads/2022/02/kaken.nii_.ac_.jp_21H05055_saitaku_shoken_ja.pdf

産総研は2025-2026年、AIRoAロボット基盤モデル開発コンペで優勝し、ロボットデータ品質評価と基盤モデル構築を進めた。材料研究単独ではなく、ソフトロボットを含む実世界作業自動化のデータ・評価基盤として重要である。source_url: https://www.aist.go.jp/aist_j/news/prz20260512 , https://www.aist.go.jp/aist_j/news/announce/pr20250123_2.html

MITSUBAは自動車用アクチュエータ・モータ・制御部品の量産基盤を持つため、ソフトロボット材料そのものより、バルブ、ポンプ、センサ、車載品質のアクチュエータ量産で関与余地が大きい。今回確認した一次資料では、2025-2026年のMITSUBA名義ソフトロボット材料論文は特定できなかった。

ブリヂストンは必須注目企業である。2025年RoboDexで、ゴムアクチュエータを使うソフトロボットハンドTetoteと吸着パッド併用のTetote andを展示した。日本勢では材料、ゴム加工、耐久、量産の接続が最も明確である。source_url: https://www.japanrubberweekly.com/2025/02/bridgestone-soft-robotics-ventures-debuts-moving-soft-robotics-using-tetote/

## 触覚センサーとの統合

GelSightはエラストマー表面の変形をカメラで読む高解像度3D触覚で、2025年以降GelSight Mini Robotics Packageは耐久性を高めた標準ゲルを出荷している。ソフトグリッパ統合ではGelSight Fin RayやEndoFlexが代表で、柔らかい把持と高密度触覚の両立を狙う。source_url: https://www.gelsight.com/product/gelsight-mini-robotics-package/ , https://arxiv.org/abs/2204.07146 , https://arxiv.org/abs/2303.17935

DIGITは低コスト・小型・高解像度の視覚触覚センサーで、果実や軟物体把持に使われる。2025年のソフトフルーツ研究ではRobotiq 2F-85にDIGITを装着し、軟らかい果実の扱い改善を狙った。source_url: https://digit.ml/digit.html , https://strathprints.strath.ac.uk/92619/

ReSkinはMeta AIとCMUが開発した磁気式触覚皮膚で、低コスト、交換可能、長期利用を特徴とする。ソフトロボット材料との相性は、表面材を消耗品として交換できる点にある。source_url: https://reskin.dev/ , https://www.cmu.edu/news/stories/archives/2021/november/reskin.html

Sanctuary AIは2025年2月、Phoenixの指腹に7セルのマイクロバロメータ触覚センサーを統合した。2026年には油圧ハンドでゼロショットin-hand manipulationを示し、量産ヒューマノイドでは「柔らかい材料」より先に「触覚付き高性能ハンド」が先行している。source_url: https://www.therobotreport.com/sanctuary-ai-integrates-tactile-sensors-into-phoenix-general-purpose-robots/ , https://www.sanctuary.ai/

## 量産化ロードマップ 2026-2035

| 年 | 到達点 | 主要プレイヤー | 根拠 |
|---|---|---|---|
| 2026-2027 | 食品・物流でソフトグリッパ継続拡大。Soft Robotics Inc.は2024年にグリッパ事業資産をSchmalzへ売却し、視覚検査・AIへ集中。 | Soft Robotics Inc., Schmalz, Bridgestone | https://softroboticsinc.com/ |
| 2026-2028 | 触覚ハンド付きヒューマノイドの工場実証。Boston Dynamics Atlasは2026年に生産対応Atlasを発表、触覚指・掌を仕様化。 | Boston Dynamics, Hyundai | https://bostondynamics.com/blog/atlas-evolution-from-research-robot-to-industrial-humanoid/ , https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf |
| 2025-2028 | Apolloの製造実証。Apptronikは2025年2月にJabilとApollo量産・製造現場導入で提携し、同月350MドルSeries Aを発表。 | Apptronik, Jabil, Google DeepMind | https://apptronik.com/news-collection/apptronik-and-jabil-collaborate-to-scale-production , https://www.axios.com/2025/02/13/apptronik-350-millionhumanoid-robots |
| 2027-2030 | PAM・ゴムアクチュエータは食品、農業、介護補助、軽物流で標準部品化。 | Bridgestone, Schmalz, OnRobot, Piab | https://www.softroboticsinc.com/meat-and-poultry-automation-solutions/ |
| 2028-2032 | DEA/HASEL/LCEは小型ハンド、触覚皮膚、医療器具、ウェアラブルへ限定採用。高電圧安全規格と封止が通れば拡大。 | MIT, CU Boulder, EPFL, ETH | https://www.nature.com/articles/s41467-025-62796-6 , https://graphsearch.epfl.ch/fr/publication/3d520532-77da-4e51-aaad-4018f137663e |
| 2030-2035 | 自己修復・リサイクル材料はメンテナンス費削減のため、交換式スキン、触覚表皮、ケーブル、シール材から採用。全身筋肉の自己修復化は後半。 | ETH, Stanford, MIT, 産業ゴム企業 | https://robotic.mat.ethz.ch/research/sustainable-robotics.html |
| 2032-2035 | バイオハイブリッドは医療・研究デバイス中心。汎用ロボット筋肉としての量産は、培養維持と規制のため限定的。 | MIT Raman, Harvard Parker, ETH Katzschmann | https://www.nature.com/articles/s44182-025-00049-w |

## 主要論文・一次資料

1. Jeong, Majidi, Ko, “Self-Healing Soft Robots: Materials, Sensors and Integrated Systems,” 2025. source_url: https://link.springer.com/article/10.1007/s12541-025-01272-z  
2. “Ultrasoft and fast self-healing poly(ionic liquid) electrode for dielectric elastomer actuators,” Nature Communications, 2025. source_url: https://www.nature.com/articles/s41467-025-62796-6  
3. “A self healable dielectric elastomer artificial muscle,” Nature Communications, 2026. source_url: https://www.nature.com/articles/s41467-026-72611-5  
4. MIT Media Lab, “Electrofluidic fiber muscles,” Science Robotics, 2026. source_url: https://www.science.org/doi/10.1126/scirobotics.ady6438  
5. MIT News, “A new type of electrically driven artificial muscle fiber,” 2026. source_url: https://news.mit.edu/2026/new-type-electrically-driven-artificial-muscle-fiber-0409  
6. Kellaris et al., “Peano-HASEL actuators,” Science Robotics, 2018. source_url: https://pubmed.ncbi.nlm.nih.gov/33141696/  
7. “HASEL Actuators Activated with a Multi-Channel Low-Cost High Voltage Power Supply,” Actuators, 2025. source_url: https://www.mdpi.com/2076-0825/14/12/601  
8. “Geometrically insensitive deform-and-go liquid crystal elastomer actuators,” Nature Communications, 2025. source_url: https://www.nature.com/articles/s41467-025-62883-8  
9. “Frequency-selective actuation of liquid crystalline elastomer actuators with radio-frequency,” Nature Communications, 2025. source_url: https://www.nature.com/articles/s41467-025-62313-9  
10. “Fiber-type artificial muscles for robotic actuation,” npj Robotics, 2025. source_url: https://www.nature.com/articles/s44182-025-00059-8  
11. MIT Raman Lab, multidirectional artificial muscle, 2025. source_url: https://news.mit.edu/2025/artificial-muscle-flexes-multiple-directions-offering-path-soft-wiggly-robots-0317  
12. MIT Raman Lab, artificial tendons for muscle-powered robots, 2025. source_url: https://news.mit.edu/2025/artificial-tendons-give-muscle-powered-robots-boost-1201  
13. Harvard Parker Lab, ML-designed tissue-engineered ray, Science Robotics, 2025. source_url: https://diseasebiophysics.seas.harvard.edu/publication/bioinspired-design-tissue-engineered-ray-machine-learning  
14. ETH Zürich, biohybrid muscle-tendon interface, 2025. source_url: https://mavt.ethz.ch/news-and-events/d-mavt-news/2025/09/biohybrid-robotics-muscles-and-tendons-for-robots.html  
15. EPFL, wafer-level zipping electrohydraulic actuators, 2025. source_url: https://graphsearch.epfl.ch/fr/publication/3d520532-77da-4e51-aaad-4018f137663e  
16. Bridgestone Soft Robotics Ventures Tetote, 2025. source_url: https://www.japanrubberweekly.com/2025/02/bridgestone-soft-robotics-ventures-debuts-moving-soft-robotics-using-tetote/
