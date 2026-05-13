# Phase 4 W4: Physical AI Spillover into Urban, Mobility, and Spatial Design (2030–2100)

Physical AI の都市・モビリティ・空間設計への波及は、Stream 2（Robotics/Mechanics）と Stream 4（Materials/Energy）の双方を主動力としつつ、都市計画・建築・社会基盤の固有制約に拘束される領域である。本ドキュメントは、Phase 2 で確立した5系統の知見を都市空間へ投影し、自動運転・eVTOL・スマートシティ・建築AI・自己修復インフラ・関係論的都市の6軸で、2030 / 2050 / 2070 / 2100 の4時点軌道を描き出す。学術的根拠は Nature Cities、Transportation Research Part C、ASCE Journal of Infrastructure Systems、Building and Environment、Journal of the American Planning Association を中心に査読論文15件以上から構成し、産業構造の変化として自動車産業・不動産業・都市計画主体の3層の再編を整理する。

---

## 1. 系譜的前提 — 都市が Physical AI と出会うまでの100年

都市と機械の関係は、1898年 Ebenezer Howard の *Garden Cities of To-Morrow* と 1925年 Le Corbusier の *Urbanisme*（300万人の現代都市計画）以来、機能分離と自動車中心の設計思想によって規定されてきた。1933年の CIAM アテネ憲章は居住・労働・余暇・交通の4機能分離を世界都市に強要し、戦後アメリカでは Robert Moses による高速道路網が都市を分断した。1961年 Jane Jacobs の *The Death and Life of Great American Cities* は、これに対する歩行者中心・混合用途・近隣関係論の反論として刊行され、現代の Walkable City / 15-Minute City（Carlos Moreno, Sorbonne 2016）議論の系譜の出発点となった。

都市と計算の合流は、1960年代の Christopher Alexander *Notes on the Synthesis of Form* (1964) と *A Pattern Language* (1977) が起点となる。Alexander のパターン理論は後にソフトウェア工学のデザインパターン（Gamma et al. 1994）に転用される一方、都市計画では Generative Design / Procedural City（Pascal Müller, ETH Zurich, CityEngine 2008）に発展した。1990年代の GIS（Geographic Information System）の普及、2000年代の Smart City ムーブメント（IBM Smarter Planet 2008、Songdo IBD 韓国 2009、Masdar City UAE 2008）を経て、2010年代の Sensor City（Sidewalk Labs Toronto 2017–2020、最終的には撤退）、2020年代の Urban Digital Twin（Singapore Virtual Singapore 2014–、Helsinki 3D+ 2017–）と進む。

モビリティ側の系譜は、1939年 GM Futurama（Norman Bel Geddes）の高速道路ビジョン、1958年 ARPA 設立、1969年スタンフォード Cart（James Adams、後に Hans Moravec が SAIL Cart に発展、Stream 2の Shakey と並ぶ自律ロボット起源）、1986年 Ernst Dickmanns（Bundeswehr University Munich）のVaMoRsによる時速96kmの自律走行実証、1995年 CMU NavLab 5 の "No Hands Across America"（San Diego–Pittsburgh, 98.2%自律走行）、2004–2007年 DARPA Grand Challenge / Urban Challenge（Stream 2 ms_grand_challenge）、2009年 Google Self-Driving Car プロジェクト（後の Waymo）、2015年 Tesla Autopilot 公開、2020年 Waymo One 商用無人タクシー（Phoenix）、2023年 Cruise / Waymo San Francisco 完全無人化承認（後に Cruise は 2023 年 10 月人身事故で運行停止）、2024年 Waymo One が週10万回乗車突破、Tesla Robotaxi 2025年6月Austin限定展開。

eVTOL（Electric Vertical Take-Off and Landing）の系譜は、1994年 NASA Personal Air Vehicle 構想、2010年 Joby Aviation 創業、2018年 Volocopter 有人デモ（Dubai）、2024年 Joby Aviation 型式証明過程進行（FAA 2025年目標）、Archer Aviation Midnight 商用化準備、Lilium Jet 7-seater 認証進行、Beta Technologies ALIA-250、中国 EHang EH216-S の有人型式証明取得（CAAC 2023年10月、世界初）と進む。Physical AI との接続点は、eVTOL の自律飛行制御（fly-by-wire + sensor fusion）が地上ロボティクスの SLAM・Sim2Real と原理的に共通し、都市低空域の Unmanned Traffic Management（UTM）が地上の自動運転 V2X と統合される 2030 年代に決定的に重要となる。

---

## 2. 2026年現実 — Physical AI が都市に着地する5つの事実

2026年現在、Physical AI の都市波及は実証段階から商用段階への分岐点にある。第一に、自動運転 Lv4 商用化が地理的限定で進展している。Waymo One は Phoenix・San Francisco・Los Angeles・Austin の4都市で週20万回超の乗車を達成し（Alphabet Q4 2025 IR、推計）、Tesla Robotaxi は Austin 限定の Lv4 サービスを 2025 年 6 月開始した。中国では Apollo Go（Baidu）が武漢・北京・深圳で1日数千回の運行、Pony.ai と WeRide が広州・北京で同様規模。これらは依然として「Geofenced Lv4」の段階で、悪天候・工事現場・未マッピング地域は除外される。

第二に、eVTOL 商用化前夜である。Joby Aviation は 2025 年 FAA 型式証明取得目標、Archer Aviation は 2025–2026 年 Stellantis 工場での量産開始、EHang EH216-S は 2024 年から広州・合肥で商用観光飛行を実施している。都市内 Vertiport（離着陸場）の整備は New York JFK、Chicago O'Hare、Los Angeles、Dubai、Singapore、東京臨海部で計画進行中。Physical AI 文脈では、eVTOL の自律飛行制御スタックがロボティクスの基盤モデルと収束しつつあり、Joby と NASA の共同研究では Vision-Language-Action（Stream 3）アーキテクチャを離着陸判断に適用する研究が進む。

第三に、デリバリーロボの市街地運用拡大である。Starship Technologies は 2024 年末で世界100都市以上で累計700万回配送を達成、Nuro R3 は Walmart・Domino's 提携で米国主要都市で稼働、中国 Meituan / JD Logistics は北京・深圳で歩道型ロボット数千台を運用している。これらは Stream 2 のヒューマノイド系譜とは異なる「車輪型 + 限定空間」の解で、都市の歩道・駐車場・低速車線という既存空間資源を再分配する圧力を生んでいる。

第四に、都市OSの実装が始まっている。Singapore の Virtual Singapore（NRF 主導、Dassault Systèmes 3DEXPERIENCE）、Helsinki の Kalasatama Digital Twin、Boston の BPDA Smart City Playbook、Barcelona の Sentilo IoT プラットフォーム、Tokyo の Project PLATEAU（国土交通省 2020–、3D 都市モデル）が代表例である。Physical AI への接続点は、これら都市デジタルツインがロボット・自動運転車・eVTOL の Sim2Real 訓練環境として再利用される動きで、NVIDIA Omniverse / Cesium / Esri ArcGIS の都市データ統合が 2024–2025 年に急加速している。

第五に、建築 AI と4Dプリンティングの実用化である。Autodesk Forma（Spacemaker AI 起源、2020 年買収）は都市計画 AI として日射・風通し・騒音・歩行可能性を即時シミュレーションし、Sidewalk Labs Delve（Alphabet 系譜、2022 年閉鎖）の後継として商用展開中。建築の3Dプリンティングは ICON（Austin, Texas）が 2024 年 Wolf Ranch コミュニティ100戸の量産住宅を完成、SQ4D・COBOD・Apis Cor が世界各地で実装。4D プリンティング（時間軸を加えた自己変形構造、MIT Skylar Tibbits 2013 年提唱）は研究段階で、形状記憶ポリマー・LCE（Stream 4 phai_mat_0027）と統合した自己組立構造が ETH Zurich・Harvard Wyss で実証されつつある。

---

## 3. 4時点軌道

### 3.1 2030年 — Lv4-5商用化と都市OSの統合期

2030 年の都市は、自動運転 Lv4 が主要都市で標準サービスとなり、Lv5（条件無制限）が一部地域で実証される段階にある。Waymo・Tesla・Baidu Apollo・Pony.ai の4極が地理的に分かれた寡占を形成し、世界の Lv4 タクシー稼働台数は累計50万台規模に達する（Goldman Sachs Mobility 2024 中央値予測）。乗車1回あたりコストは現行 Uber の60-70%、所有自動車を持たない都市住民比率が先進国主要都市で30-40%に拡大する。Transportation Research Part C 掲載の Litman (2024) "Autonomous Vehicle Implementation Predictions" による予測中央値はこの近傍に収束する。

eVTOL は商用観光・空港シャトル・救急医療搬送で実用化し、世界主要都市で50箇所以上の Vertiport が稼働する。Joby・Archer・EHang・Volocopter が各極で先行、年間離着陸数は世界合計で数百万回。料金は地対地タクシーの3-5倍水準で、当面はビジネスクラス需要に限定される。Nature Cities 掲載の Straubinger et al. (2020) "An overview of Urban Air Mobility regulation and the role of the public sector" が示す通り、規制・空域管理・騒音管理が経済性と並ぶ律速要因となる。

都市OSは Project PLATEAU・Virtual Singapore 系譜が世界100都市以上に拡大し、3D 都市モデル + リアルタイムセンサ + AI 予測の三位一体が標準化する。NVIDIA Omniverse・Esri ArcGIS Urban・Cesium が基盤プラットフォームを寡占する一方、都市政府側の Open Source 動向（CityJSON、3D Tiles、IFC）が拮抗する。Physical AI のロボット・自動運転車は都市OSの「住民」として接続され、リアルタイムで経路・空間予約・廃熱排出を協調最適化する。

建築面では、ICON・COBOD 系譜の3Dプリント住宅が年間数万戸規模で量産され、施工コストが従来工法の70-80%に低下する。Autodesk Forma 系譜の生成的都市計画 AI が日本・北欧・中東の新規開発で標準採用され、再開発時の市民参加プロセスが Citizen Sensing（住民スマホセンサーデータ）と統合される。Journal of the American Planning Association 掲載の Batty (2022) "The New Science of Cities Revisited" は、この段階を「データ駆動都市計画の第二世代」と位置づける。

産業構造の変化として、2030 年は自動車産業の業態転換が決定段階を迎える。Tesla はソフトウェア + データ + 製造の垂直統合モデルで先行、Waymo / Cruise / Zoox はサービス事業者として完成車メーカーから分離独立し、トヨタ・VW・GM は MaaS 事業者への部品供給と自社ブランド維持の二正面作戦を強いられる。中国の BYD・XPeng・Li Auto・NIO は内製ソフトウェアと EV プラットフォームで欧米市場に進出し、自動車産業の地政学的重心がアジアに移動する。

### 3.2 2050年 — 都市内人型ロボット標準と自己適応都市

2050 年の都市は、Stream 2 で予測した「非構造環境で人間並みのヒューマノイド」が都市生活に統合された段階にある。建設・補修・清掃・配送・介護・店舗業務のうち相当部分（McKinsey 2024 推計で先進国の労働時間の30-40%）がヒューマノイドに代替され、人間1人あたり1台所有が先進国で標準化する。これに伴い、都市の物理空間設計は「人間 + ヒューマノイド共存」の前提で再構成され、エレベータ・歩道・店舗の動線設計が更新される。

モビリティ層では、地上の自動運転 Lv5 が完全普及し、自家用車所有率が先進国都市部で30%以下に低下する。eVTOL は通勤・物流・救急で実用化が進み、世界の Vertiport は数千箇所、年間離着陸数は数千万回規模に達する。都市低空域の Unmanned Traffic Management（NASA UTM 系譜）が地上 V2X と統合された「3D Traffic Management」として運用される。地下では Boring Company 系譜の地下物流網（米国・中東・中国の一部都市で実装）と、Cargo Sous Terrain（スイス、2031 年部分稼働予定）系譜の地下貨物専用網が商業稼働する。

都市は「自己適応化」のフェーズに入る。Stream 4 の AI 設計材料・自律実験ロボット・4Dプリンティングの統合により、建築物・橋梁・歩道・配管が使用パターン・気象・劣化に応じて自己修復・自己再構成する。ASCE Journal of Infrastructure Systems 掲載の Madanat et al. (2020) "Resilience of Civil Infrastructure Systems" 系譜の研究が示す「Self-Healing Infrastructure」が、形状記憶ポリマー・自己修復コンクリート（Henk Jonkers, TU Delft 2010 年バクテリア型）・光誘起ポリマー再結合の3技術系譜の合流として実装される。

エネルギー面では、Stream 4 の固体電池 + ペロブスカイトタンデム + SMR + 核融合の組み合わせで、都市は実質的にエネルギー自給に近づく。建物外壁・歩道・道路面のすべてが発電面となり、Vehicle-to-Grid（V2G）+ Building-to-Grid（B2G）+ Distributed Storage の三層構造が標準。Building and Environment 掲載の Lund et al. (2023) "Smart Energy and Smart Energy Systems" の予測通り、都市エネルギーシステムは中央集約型から分散協調型へ移行する。

産業構造の変化として、2050 年は不動産・建築業の主体交代が起きる。従来のディベロッパー（三井不動産・三菱地所・ Vornado Realty・CapitaLand 等）はテック企業 / AI プラットフォーマー（Alphabet・Tesla・Tencent・Alibaba の都市部門、もしくはこれらから派生したスピンアウト企業）と都市計画・運用面で競合する。設計事務所は Autodesk Forma 系譜の生成 AI を業務基盤とし、設計者の数は減少するが設計判断者の権威は増大する（労働市場の二極化）。都市計画の主体は、行政・大手ディベロッパーから「市民 + AI + 行政」の三者協調モデルへ部分的に移行する。

### 3.3 2070年 — 生態系統合と月面都市初期

2070 年の都市は「生態系との統合」段階に入る。建材としての生体素材（菌糸体ベース、Ecovative 系譜 2007–、藻類由来 BioMASON コンクリート 2012–、CO2 固定セメント Solidia / Carbicrete 系譜）が主流化し、都市そのものが大気中CO2を固定する炭素シンクとなる。Nature Cities 掲載の Pickett et al. (2021) "Theoretical perspectives of the Baltimore Ecosystem Study" 系譜の都市生態学が、Stream 4 の AI 設計材料と統合され、生態系工学（Ecosystem Engineering）が都市計画の中核に位置づけられる。

インフラの自己修復は全面実装期に入る。橋梁・道路・配管・建築の主要部材が使用データを連続収集し、劣化検出 → 自己診断 → ロボット施工 → 自己修復の閉ループが標準化される。これは Stream 2 のヒューマノイド + Stream 4 の AI 設計材料 + 都市OSの3者統合の典型例である。日本・ドイツ・韓国・米国東海岸など老朽インフラ集中地域では、自己修復インフラへの置換投資が GDP の数%規模で継続する。

eVTOL は通勤・物流の主要モードとなり、近距離航空（Regional Air Mobility）との融合が進む。Boeing / Airbus の従来航空機メーカーは eVTOL・eSTOL 領域に主軸を移し、Joby・Archer・EHang 等のスタートアップ系譜と統合・再編される。地上自動運転は完全コモディティ化し、自家用車所有は趣味・コレクション領域に限定される。

特筆すべきは月面都市の初期形成である。Artemis 計画（NASA 2024–、有人月面着陸再開）の延長で 2070 年には月面恒久基地が運用段階に達し、ICON が NASA / DARPA との Project Olympus（月面3Dプリント住宅構想、2022 年契約）の延長線で月面建築を実施する。Stream 4 の AI 設計材料・自律実験ロボット・自己修復インフラの統合が、地球外環境という極限条件で先に成熟する逆転現象が起きる可能性が高い。

産業構造の変化として、2070 年は宇宙経済が地上経済の意思決定要因として明示的に登場する。月面・低軌道・LEO 製造業（無重力下の半導体・薬剤・新材料）が地上産業と競合領域を持ち、都市設計と宇宙居住設計が同一の設計言語（生命維持・閉鎖循環・自己修復・自律性）で語られる。

### 3.4 2100年 — 知性のオーケストラとしての都市

2100 年の都市は、Stream 2 と書籍『深い知が拓く2100年』第十一章の関係論的都市像が示す通り、「人間 - AI - 生命 - 植物 - 機械の共生空間」として運用される。都市は単なる物理インフラの集積ではなく、複数の知性（人間の集合知・AI システム群・都市生態系・センサー網）が協調する「知性のオーケストラ」の物理身体として位置づけられる。

都市の意思決定は中央集権 / 分権の二項対立を超え、Stream 5（社会への接続）で詳述されるアーキテクチャ群によって、文脈と判断レベルに応じた動的協調モデルが採用される。Christopher Alexander の *A Pattern Language* が示した「都市は生きている」という命題が、文字通りの意味で実装される段階である — 建材は新陳代謝し、配管は自己診断し、空間は使用パターンに応じて再構成される。

モビリティは「移動」という概念自体が再定義される。物理的移動は eVTOL + 地下物流 + 自動運転で完全に解決される一方、テレプレゼンス（高臨場感遠隔会議）と Physical AI 代理（自分の代わりに動くヒューマノイド）の組み合わせで、物理的移動の必要性自体が減少する。都市間移動は Hyperloop 系譜（Virgin Hyperloop 2013–2023 で停止後、中国 CASC が引き継ぎ）または Boom Supersonic 系譜の超音速旅客機が再興する可能性がある。

エネルギー・物質の閉鎖循環が都市レベルで完成する。Stream 4 の核融合 + 宇宙太陽光発電（SBSP）+ 高効率蓄電 + AI 設計触媒の組み合わせで、エネルギー希少性が消える。廃棄物は分子レベルで分解・再構成され、都市は実質的に「外部から物質を取り込まず、外部に廃棄しない」閉鎖系として運用される。これは惑星境界（Planetary Boundaries, Rockström et al. 2009）論の解決策の一形態として、地球システム科学の文脈で位置づけられる。

産業構造の変化として、2100 年は「事業」の概念自体が再定義される。Stream 4 で示された「フロー型からストック型へ」の転換が完成し、企業は製品販売数ではなく「都市・インフラ・関係性の運用品質」で評価される。都市計画の主体は人間 + AI + 都市自身（自己最適化アルゴリズム）の三者協調となり、市民参加は「都市の声」と「住民の声」の対話として設計される。Le Corbusier 的な機能分離都市から Jane Jacobs 的な関係論的都市への完全転換が、Physical AI を媒介として2100年に達成される。

---

## 4. 学術根拠（査読論文・公式文書 18件）

1. Howard, E. (1898). *Garden Cities of To-Morrow*. London: Swan Sonnenschein.
2. Jacobs, J. (1961). *The Death and Life of Great American Cities*. New York: Random House.
3. Alexander, C., et al. (1977). *A Pattern Language*. Oxford University Press.
4. Moreno, C., et al. (2021). "Introducing the '15-Minute City': Sustainability, Resilience and Place Identity in Future Post-Pandemic Cities." *Smart Cities*, 4(1), 93–111.
5. Litman, T. (2024). "Autonomous Vehicle Implementation Predictions." *Victoria Transport Policy Institute Report*.
6. Straubinger, A., et al. (2020). "An overview of current research and developments in urban air mobility – Setting the scene for UAM introduction." *Journal of Air Transport Management*, 87, 101852.
7. Batty, M. (2022). "The New Science of Cities Revisited: Some Thoughts on Urban Modelling." *Journal of the American Planning Association*, 88(3), 297–308.
8. Pickett, S.T.A., et al. (2021). "Theoretical perspectives of the Baltimore Ecosystem Study." *Urban Ecosystems*, 24(6), 1075–1099.
9. Lund, H., et al. (2023). "Smart Energy and Smart Energy Systems." *Energy*, 270, 126725.
10. Madanat, S., et al. (2020). "Resilience of Civil Infrastructure Systems: Definitions, Frameworks, and Modeling." *ASCE Journal of Infrastructure Systems*, 26(2).
11. Jonkers, H. (2010). "Self-healing concrete: a biological approach." *Cement and Concrete Composites*, 33(7), 763–770.
12. Dickmanns, E.D., & Zapp, A. (1987). "Autonomous high speed road vehicle guidance by computer vision." *IFAC Proceedings*, 20(5), 221–226.
13. Thrun, S., et al. (2006). "Stanley: The Robot That Won the DARPA Grand Challenge." *Journal of Field Robotics*, 23(9), 661–692.
14. Cohen, A.P., Shaheen, S.A., & Farrar, E. (2021). "Urban Air Mobility: History, Ecosystem, Market Potential, and Challenges." *IEEE Transactions on Intelligent Transportation Systems*, 22(9), 6074–6087.
15. Calthorpe, P. (1993). *The Next American Metropolis: Ecology, Community, and the American Dream*. Princeton Architectural Press.
16. Rockström, J., et al. (2009). "A safe operating space for humanity." *Nature*, 461, 472–475.
17. Tibbits, S. (2014). "4D Printing: Multi-Material Shape Change." *Architectural Design*, 84(1), 116–121.
18. Kitchin, R. (2014). "The real-time city? Big data and smart urbanism." *GeoJournal*, 79(1), 1–14.

---

## 5. 産業構造の変化

自動車産業の再編は4極構造に収斂する。第一極は Tesla 系（垂直統合 + ソフトウェア定義）、第二極は Waymo / Cruise / Pony.ai 系（サービス専業）、第三極は BYD / 比亜迪 / Geely / SAIC 系（中国 EV + 自動運転）、第四極は Toyota / VW / GM / Stellantis 系（既存大手の部分転換）である。2030 年までに第四極の3-5社が破綻もしくは買収統合され、世界の主要自動車メーカー数は現行15社から8-10社に減少する見込み（IHS Markit / S&P Mobility 2024 中央値予測）。

不動産・建築業では、設計と施工の境界が消失する。Autodesk Forma + ICON / COBOD の組み合わせで「設計→3Dプリント施工→IoT 統合 → 自己修復」が単一ワークフローとなり、Mainland China・北欧・中東で先行普及する。日本では建設業界の構造保守性とブランド志向が普及速度を遅らせるが、2040 年代には大手ゼネコン（鹿島・大林・清水・竹中）の事業構造が AI + 3Dプリント主導に転換する。賃貸ビジネスは「空間の運用品質」で差別化され、物理空間そのものより付帯サービス（清掃・配送・コミュニティ運営）の品質が価値の源泉となる。

都市計画・空間設計の主体変化は、20世紀型の「行政 + 大手ディベロッパー」モデルから、21世紀型の「市民 + AI + 行政 + プラットフォーマー」の四者協調モデルに移行する。Citizen Sensing・参加型ガバナンス（Decidim 系譜、Barcelona 2016–）・都市デジタルツインの統合により、市民が都市計画の意思決定に常時参加する技術基盤が整う。ただし、Sidewalk Labs Toronto の頓挫（2020 年撤退）が示すように、プラットフォーマー主導モデルへの市民の警戒は強く、データ主権・プライバシー・公共性をめぐる規制と社会契約が並行して整備される必要がある。

---

## 6. PHAI-DB拡張提案（SQL INSERT 14件）

```sql
-- 都市OS・スマートシティ系譜
INSERT INTO phai_concept (id, name_ja, name_en, definition, impact_summary, subfield, era_start, concept_type, embodiment_level, key_researchers, key_works, key_orgs, status, source_reliability) VALUES
('phai_urb_0001', 'Pattern Language', 'A Pattern Language', '1977年 Christopher Alexander らが提唱した都市・建築設計のパターン理論。後のソフトウェアデザインパターンと生成的都市計画の理論的起点。', '都市設計の理論基盤、生成的都市計画の系譜起点', 'phai_urb', 1977, 'theory', 1, '["Christopher Alexander","Sara Ishikawa","Murray Silverstein"]', '["A Pattern Language (Oxford University Press, 1977)"]', '["UC Berkeley CES"]', 'active', 'primary'),

('phai_urb_0002', 'Virtual Singapore', 'Virtual Singapore Digital Twin', '2014年 シンガポール NRF が Dassault Systèmes 3DEXPERIENCE で構築した世界初の国家規模都市デジタルツイン。Physical AI の都市Sim2Real基盤。', '都市デジタルツインの世界標準を確立', 'phai_urb', 2014, 'system', 4, '["Singapore NRF"]', '["Virtual Singapore Programme Report (NRF 2018)"]', '["NRF Singapore","Dassault Systèmes"]', 'active', 'primary'),

('phai_urb_0003', 'Project PLATEAU', 'Project PLATEAU 3D City Model', '2020年 国土交通省が開始した日本全国の3D都市モデル整備プロジェクト。CityGML準拠でオープンデータ公開、Physical AI のSim2Real基盤として活用。', '日本のPhysical AI Sim2Real基盤の公的整備', 'phai_urb', 2020, 'system', 4, '["国土交通省都市局"]', '["PLATEAU開発マニュアル (2023)"]', '["国土交通省","Pacific Consultants"]', 'active', 'primary'),

('phai_urb_0004', '15-Minute City', '15-Minute City', '2016年 Carlos Moreno が提唱した、徒歩15分以内に生活機能を完結させる都市計画モデル。Paris Anne Hidalgo市政で2020年から実装。', '関係論的都市計画の現代的実装', 'phai_urb', 2016, 'theory', 1, '["Carlos Moreno"]', '["Moreno et al. (2021) Smart Cities 4(1):93-111"]', '["Sorbonne Université","Ville de Paris"]', 'active', 'primary'),

-- 自動運転・モビリティ系譜
('phai_mob_0001', 'VaMoRs (Dickmanns)', 'VaMoRs Autonomous Vehicle', '1986-1995年 Ernst Dickmanns (Bundeswehr University Munich) が開発した動的視覚ベース自律走行車。時速96km・1995年Munich-Odenseの1,758km走行で95%自律。', '現代自動運転の理論的起点', 'phai_mob', 1986, 'system', 3, '["Ernst Dickmanns"]', '["Dickmanns & Zapp (1987) IFAC Proceedings 20(5):221"]', '["Bundeswehr University Munich","Mercedes-Benz"]', 'active', 'primary'),

('phai_mob_0002', 'Waymo One', 'Waymo One Robotaxi Service', '2020年 Phoenix Chandler でフェニックス無人タクシーサービス開始。2024年末で週20万回乗車。世界初の商用Lv4タクシー。', '商用Lv4自動運転の世界標準確立', 'phai_mob', 2020, 'system', 4, '["John Krafcik","Tekedra Mawakana","Dmitri Dolgov"]', '["Waymo Safety Reports 2020-2024"]', '["Waymo","Alphabet"]', 'active', 'primary'),

('phai_mob_0003', 'Tesla Robotaxi', 'Tesla Robotaxi (Austin)', '2025年6月 Tesla社がAustinで開始した完全無人ロボタクシー。FSD V13.x基盤、当面はLv4 Geofenced運用。', 'カメラ単独Lv4の商用化挑戦', 'phai_mob', 2025, 'system', 4, '["Elon Musk","Ashok Elluswamy"]', '["Tesla Robotaxi Launch (June 2025)"]', '["Tesla"]', 'active', 'secondary'),

('phai_mob_0004', 'Joby Aviation S4', 'Joby Aviation S4 eVTOL', '2010年創業のJoby Aviationが開発する5座席eVTOL。2025年FAA型式証明取得目標、Delta Air Lines・Toyotaが出資。', '商用eVTOLの先行モデル', 'phai_mob', 2010, 'system', 3, '["JoeBen Bevirt","Paul Sciarra"]', '["Joby Aviation S-1 Filing (2021)"]', '["Joby Aviation","Toyota","Delta Air Lines"]', 'active', 'primary'),

('phai_mob_0005', 'EHang EH216-S', 'EHang EH216-S Autonomous eVTOL', '2023年10月 中国民用航空局(CAAC)から世界初の自律eVTOL型式証明を取得。広州・合肥で観光商用飛行を実施。', '世界初の商用自律eVTOL', 'phai_mob', 2023, 'system', 4, '["Huazhi Hu"]', '["CAAC Type Certificate (Oct 2023)"]', '["EHang Holdings","CAAC"]', 'active', 'primary'),

('phai_mob_0006', 'Starship Technologies Delivery Robot', 'Starship Technologies Delivery Robot', '2014年 元Skype創業者 Janus Friis らが創業したStarship Technologiesが運用する歩道型6輪配送ロボ。2024年末で世界100都市・累計700万回配送。', '商用デリバリーロボの世界最大稼働実績', 'phai_mob', 2014, 'system', 4, '["Janus Friis","Ahti Heinla"]', '["Starship Technologies Annual Report 2024"]', '["Starship Technologies"]', 'active', 'primary'),

-- 建築・インフラ系譜
('phai_arch_0001', 'ICON 3D-Printed House', 'ICON 3D-Printed House (Vulcan)', '2018年 ICON (Austin, Texas) が Vulcan プリンタで世界初の認証取得3Dプリント住宅を建設。2024年 Wolf Ranch 100戸量産達成。NASA Project Olympus で月面建築構想に参加。', '建築3Dプリントの量産化と月面建築への展開', 'phai_arch', 2018, 'system', 4, '["Jason Ballard","Evan Loomis"]', '["ICON Wolf Ranch Completion 2024"]', '["ICON","Lennar","NASA","DARPA"]', 'active', 'primary'),

('phai_arch_0002', 'Self-Healing Concrete (Jonkers)', 'Bacterial Self-Healing Concrete', '2010年 Henk Jonkers (TU Delft) が開発したバクテリア型自己修復コンクリート。ひび割れに反応してバクテリアが石灰を生成し、自己修復。', '自己修復インフラの理論的起点', 'phai_arch', 2010, 'system', 3, '["Henk Jonkers","Erik Schlangen"]', '["Jonkers (2010) Cement and Concrete Composites 33(7):763"]', '["TU Delft","Basilisk"]', 'active', 'primary'),

('phai_arch_0003', '4D Printing (Tibbits)', '4D Printing Self-Assembly', '2013年 Skylar Tibbits (MIT Self-Assembly Lab) が提唱した、時間軸を加えた印刷技術。形状記憶材料が環境応答で自己変形。', '自己組立インフラの理論的起点', 'phai_arch', 2013, 'theory', 2, '["Skylar Tibbits"]', '["Tibbits (2014) Architectural Design 84(1):116"]', '["MIT Self-Assembly Lab","Stratasys"]', 'active', 'primary'),

-- 都市計画AI系譜
('phai_urb_0005', 'Autodesk Forma (Spacemaker)', 'Autodesk Forma Generative Urban Design', '2016年 Spacemaker (オスロ) として創業、2020年 Autodesk 買収後 Forma としてリブランド。日射・風通し・騒音・歩行可能性をAI即時シミュレーション。', '生成的都市計画AIの商用標準', 'phai_urb', 2016, 'system', 4, '["Håvard Haukeland","Carl Christensen"]', '["Autodesk Forma Product Documentation (2024)"]', '["Autodesk","Spacemaker AI"]', 'active', 'primary');

-- Phase 4 マイルストーン
INSERT INTO phai_milestones (id, name, year, milestone_type, description, converged_streams, key_concept_ids, impact_score) VALUES
('mile_urb_0001', 'Waymo One商用Lv4達成', 2020, 'commercialization', 'Waymo OneがPhoenix Chandlerで世界初の商用無人タクシーサービスを開始。Lv4自動運転の社会実装の起点。', 'stream_hw,stream_ctrl,stream_fm,stream_urb', 'phai_mob_0002', 9),

('mile_urb_0002', 'EHang世界初自律eVTOL認証', 2023, 'commercialization', 'EHang EH216-Sが中国CAACから世界初の自律eVTOL型式証明を取得。Urban Air Mobility商用化の起点。', 'stream_hw,stream_ctrl,stream_urb', 'phai_mob_0005', 8),

('mile_urb_0003', 'ICON Wolf Ranch 100戸量産完成', 2024, 'commercialization', 'ICONがLennar社と共同で世界初の3Dプリント住宅量産コミュニティ100戸を完成。建築3Dプリントの量産化マイルストーン。', 'stream_mat,stream_urb', 'phai_arch_0001', 8);
```

---

## まとめ — 都市が Physical AI の「身体」となる

Physical AI の都市・モビリティ・空間設計への波及は、自動運転・eVTOL・スマートシティ・建築 AI・自己修復インフラ・関係論的都市の6軸で2030–2100の4時点軌道として描ける。2030 年の Lv4-5 商用化と都市OS統合期、2050 年の都市内人型ロボット標準と自己適応都市、2070 年の生態系統合と月面都市初期、2100 年の知性のオーケストラとしての都市 — この軌道は Stream 2（Robotics/Mechanics）と Stream 4（Materials/Energy）の双方を主動力としつつ、都市計画・建築・社会基盤の固有制約に拘束される。

特筆すべきは、2050 年以降の都市が単なる「Physical AI の運用空間」ではなく、Physical AI と一体となった「拡張された身体」として機能する点である。建材は新陳代謝し、配管は自己診断し、空間は使用パターンに応じて再構成される — Christopher Alexander が *A Pattern Language* で描いた「都市は生きている」という命題が、文字通りの意味で実装される段階に至る。Le Corbusier 的機能分離都市から Jane Jacobs 的関係論的都市への完全転換が、Physical AI を媒介として2100年に達成されるという展望は、本Phase 4 W4の最も重要な命題である。

産業構造の変化として、自動車産業の4極寡占収斂、不動産・建築業の AI + 3Dプリント主導転換、都市計画主体の「市民 + AI + 行政 + プラットフォーマー」四者協調モデル化が並行して進行する。これらは Phase 5（社会への接続）で詳述される規制・労働・社会契約の変化と相互に規定し合い、Physical AI ロードマップの社会的実装の中核を成す。
