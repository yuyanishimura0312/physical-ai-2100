# エグゼクティブサマリ

2026年5月時点の宇宙ロボティクスは、「探査機」から「作業員・建設機械・保守要員」へ役割が拡張している。Artemis IIは2026年4月に有人月周回を実施済みで、NASAはArtemis IIIを2027年の地球低軌道ランダー試験へ再設計し、月面着陸を2028年以降へ段階化した（source_url: https://www.nasa.gov/news-release/nasa-adds-mission-to-artemis-lunar-program-updates-architecture/）。中国は嫦娥6号で2024年に月裏側サンプルリターンを達成し、嫦娥7/8で南極資源・ISRU・基地ロボットへ進む。日本はJAXA/ToyotaのLunar Cruiser、ispace、GITAI、Astroscaleが月面移動・作業・軌道保守の中核を担う。

## ミッション別ロボット要件マトリクス

| 領域 | 主要ミッション | 必須ロボット機能 | 2025-2026の状態 |
|---|---|---|---|
| 月面 | Artemis、嫦娥7/8、CLPS、HAKUTO-R | 高信頼着陸、極域走行、掘削、サンプル採取、夜間耐性、遠隔/自律作業 | Artemis IIIは2027年LEOランダー試験、月面着陸は2028年以降へ再構成（source_url: https://www.nasa.gov/artemis-iii-news-and-updates/）。嫦娥6号は2024年6月25日に月裏側サンプルを地球帰還（source_url: https://english.cas.cn/newsroom/cas_media/202406/t20240628_666011_2.shtml）。 |
| 火星 | SpaceX Starship/Optimus構想、将来NASA Mars | 長距離自律、粉塵耐性、通信遅延下の判断、建設・点検 | Musk発言として「2026年末にStarshipでOptimusを火星へ」という構想が報じられたが、NASA/SpaceXの正式ミッション計画としては未確定（source_url: https://www.gmanetwork.com/news/scitech/technology/939421/starship-carrying-tesla-s-bot-set-for-mars-by-end-2026-elon-musk/story/）。 |
| 軌道上 | Gateway、ISS後継、ISAM、デブリ除去 | ロボットアーム、ランデブ・近傍運用、捕獲、点検、組立、補給 | GatewayはCanadarm3を外部点検・ペイロード操作に使う計画で、CSAは2025-26に詳細設計を継続（source_url: https://www.csa-asc.gc.ca/eng/publications/dp-2025-2026.asp）。NASAは商業LEOステーションPhase 2を2026年に複数選定予定（source_url: https://www.nasa.gov/humans-in-space/commercial-space/commercial-space-stations/）。 |

## Artemis プログラムにおけるロボット役割

Artemis Iは2022年11月16日にSLS/Orion無人統合試験として打ち上げられ、2022年12月11日に太平洋へ帰還した。これは有人深宇宙ロボット・生命維持・地上回収系の基盤試験であり、Orionを月帰還速度で検証した（source_url: https://www.nasa.gov/blogs/artemis/2022/12/11/artemis-i-flight-day-26-orion-splashes-down-concluding-historic-artemis-i-mission/）。

Artemis IIは、ユーザー指定の「2026春予定」から進み、NASA公式ページ上では「乗員が月を周回した」と記述されている。NASA+の公式放送ページは打上げ日を2026年4月1日としており、2026年5月18日時点では実施済み扱いで整理する必要がある（source_url: https://plus.nasa.gov/scheduled-video/nasas-artemis-ii-crew-launches-to-the-moon-official-broadcast/、https://www.nasa.gov/mission/artemis-ii/）。

Artemis IIIは大きく変更された。NASAは2026年2月27日発表で、Artemis IIIを2027年の地球低軌道デモに再設計し、SpaceXまたはBlue Originの商業月着陸船とのランデブ・ドッキング、生命維持、通信、推進、xEVAスーツ試験を実施するとした。有人月面着陸はArtemis IVの2028年以降へ後ろ倒しされた（source_url: https://www.nasa.gov/news-release/nasa-adds-mission-to-artemis-lunar-program-updates-architecture/）。

月面ローバーでは二層構造が明確である。第一層はCLPSによる小型・無人ローバーで、NASAはVIPERを2024年7月に中止し、2025年5月に代替輸送手段を検討すると発表した（source_url: https://science.nasa.gov/mission/viper/、https://www.nasa.gov/blogs/missions/2025/05/07/nasa-to-explore-additional-methods-to-send-viper-to-moon/）。第二層はArtemisのLunar Terrain Vehicleで、NASAはIntuitive Machines、Lunar Outpost、Venturi AstrolabをLTVベンダーとして進め、2025年に科学機器を選定した（source_url: https://www.nasa.gov/news-release/nasa-selects-instruments-for-artemis-lunar-terrain-vehicle/）。

Lunar OutpostのMAPPは、商業月面ローバーとして極域調査・通信実証・資源探査を狙う。IM-2ではLunar Outpost MAPPとIntuitive MachinesのMicro-Nova Hopper、Nokia通信実証が組み合わされたが、NASAはIM-2が2025年3月6日に月南極付近のクレーターへ着陸後、限定的なデータ取得で終了したと発表した（source_url: https://www.nasa.gov/news-release/nasa-receives-some-data-before-intuitive-machines-ends-lunar-mission、https://www.nasa.gov/wp-content/uploads/2025/02/np-2025-02-005-jsc-clps-intuitive-machines-press-kit-508-2-25-25.pdf）。

Astrobotic Peregrineは2024年1月8日に打ち上げられたが、推進系異常により月面軟着陸を断念し、2024年1月18日に南太平洋上空で制御再突入した。Astroboticはヘリウム加圧系と酸化剤間のバルブ再シール不良を有力仮説として公表した（source_url: https://www.nasa.gov/?p=597122、https://www.astrobotic.com/update-8-for-peregrine-mission-one/）。

## 中国月面・嫦娥プログラム vs Artemis

嫦娥6号は2024年5月3日に打上げ、2024年6月2日に月裏側の南極エイトケン盆地へ着陸し、2024年6月25日に帰還カプセルが内モンゴルへ着陸した。CAS報道では回収サンプル量は1,935.3gとされ、月裏側サンプルリターンとして世界初である（source_url: https://english.cas.cn/newsroom/cas_media/202406/t20240628_666011_2.shtml、https://english.cas.cn/newsroom/news--archives/2024/news-updates/202406/t20240625_1129636.shtml）。

嫦娥7号は2026年に月南極を調査する計画で、CNSA発表として2026年打上げ、南極資源・水氷探索を行うと報じられている。構成はオービター、ランダー、ローバー、ホッピング探査機とされ、従来ローバーが入りにくい永久影・急峻地形に対応する設計思想である（source_url: https://www.cislunarspace.cn/en/space-news/2026/04/2026-04-24-chang-e7-launch/）。

嫦娥8号は2028年前後にISRU、月面環境、基地建設技術を試験する位置づけで、ILRSのロボット先遣隊に近い。公開情報ではレゴリス利用、3Dプリント、ローバー/脚式ロボット等の実証が示されているが、個別機体仕様は公式確定情報と二次情報を分けて扱う必要がある（source_url: https://www.cnsa.gov.cn/english/n6465652/n6465653/c6812150/content.html、参考: https://www.ida.org/-/media/feature/publications/p/pe/peoples-republic-of-china-in-cislunar-space-activities-motivations-and-implications/3002255.ashx）。

Artemisとの違いは、米国が有人安全性・商業分担・国際標準化を重視するのに対し、中国は嫦娥4/5/6でロボット探査を連続成功させ、嫦娥7/8で月南極とILRSへ段階的に進む点である。Artemisは2026年に有人周回を達成したが、月面着陸は2028年以降へ再設計されたため、2026-2028の月面ロボット実績では中国の連続性が強い（source_url: https://www.nasa.gov/news-release/nasa-adds-mission-to-artemis-lunar-program-updates-architecture/、https://english.cas.cn/newsroom/cas_media/202406/t20240628_666011_2.shtml）。

## 日本機関の独自貢献

JAXA/ToyotaのLunar Cruiserは、2019年から共同研究されている有人与圧ローバーで、JAXAは2020年代後半の打上げを目指すと発表していた。Toyotaは月面環境を「1/6重力、-170から120℃、真空、放射線、レゴリス」と整理し、燃料電池・耐久性・走行制御をローバー技術へ移植する（source_url: https://global.jaxa.jp/press/2020/08/20200828-1_e.html、https://global.toyota/en/mobility/technology/lunarcruiser/）。

GITAIは2025年3月31日、JAXAから有人与圧ローバー用ロボットアームの概念検討契約を受けたと発表した。これはLunar Cruiserが単なる移動体ではなく、船外作業、サンプル操作、設備点検、基地建設のロボット作業プラットフォームになることを示す（source_url: https://gitai.tech/2025/03/31/gitai-awarded-jaxa-contract-for-concept-study-of-robotic-arm-for-crewed-pressurized-lunar-rover/）。

GITAIのR1月面作業ローバーは、2021年12月にJAXA相模原キャンパスの模擬月面環境で走行・作業試験を完了した。公表タスクは探査、採掘、点検、保守、組立などで、月面基地建設の「労働力」をロボット化する方向性が明確である（source_url: https://gitai.tech/2022/02/10/gitai-develops-lunar-robotic-rover-r1/）。

ispaceはHAKUTO-R Mission 1で2023年4月に着陸に失敗した後、Mission 2 RESILIENCEを2025年1月15日に打ち上げ、2025年6月6日JSTの着陸を設定した。ESAもRESILIENCEを欧州初ローバー搭載の月ミッションとして支援したが、2025年6月の着陸時に通信を喪失し、ミッション終了となった（source_url: https://ispace-inc.com/wp-content/uploads/2025/01/20250109_M2-Launch-Date.pdf、https://www.esa.int/Enabling_Support/Operations/ESA_Ground_Stations/ESA_supports_Moon_mission_carrying_first_European_rover、https://ispace-inc.com/wp-content/uploads/2025/06/20250606-Update-1.pdf）。

AstroscaleはJAXA CRD2 Phase Iの契約先としてADRAS-Jを開発し、2024年7月に大型デブリの周回観測画像を公開した。JAXAは2024年8月にCRD2 Phase IIのパートナーシップ型契約を結び、観測から捕獲・除去へ進める構造である（source_url: https://global.jaxa.jp/press/2024/07/20240730-1_e.html、https://www.kenkai.jaxa.jp/eng/crd2/）。

ALEはロボット企業ではないが、日本の宇宙産業として、2025年4月に東京大学UTOPSと小惑星アポフィス探査ミッションの共同研究契約を締結した。宇宙ロボティクス教科書では、ALEは「宇宙環境・小天体ミッションを民間が設計する」事例として扱うのが適切で、月面作業ロボット企業として分類してはならない（source_url: https://prtimes.jp/main/html/rd/p/000000026.000042372.html）。

HRP-5Pについては注意が必要である。HRP-5PはJAXAではなく産総研AISTが2018年に発表した大型構造物組立向けヒューマノイドで、公式発表は建設、航空機、船舶など危険・重労働現場を対象としている。公開情報上、JAXAがHRP-5Pを月面適応した公式計画は確認できないため、本教科書では「月面基地建設に転用可能な地上ヒューマノイド技術」と限定して扱う（source_url: https://www.aist.go.jp/aist_e/list/latest_research/2018/20181116/en20181116.html）。

## 商業宇宙ロボット市場

商業LEO市場では、NASAがISS退役後の2030年前後を見据え、Axiom、Blue Origin/Orbital Reef、Starlab、Sierra Space、Vast等を支援している。NASAは2025年後半にPhase 2提案募集、2026年初に複数の資金付きSpace Act Agreementを予定する（source_url: https://www.nasa.gov/humans-in-space/commercial-space/commercial-space-stations/）。

Axiom SpaceはISSに接続する商業モジュールから独立ステーションへ移行する計画で、NASAは2020年に少なくとも1つの居住商業モジュールをISSに接続する契約を授与した。Axiomは軌道上データセンターも進め、AI/ML処理を宇宙で行う基盤を商業化しつつある（source_url: https://www.nasa.gov/humans-in-space/commercial-space/commercial-space-stations/、https://axiomspace.com/release/axiom-space-spacebilt-announce-orbital-data-center-node）。

VastのHaven-1は単一モジュール商業ステーションで、NASAは2025年5月に空気フィルター試験進捗を紹介した。Vastは2026年後半に環境試験を行う統合段階へ進めるとしており、Haven-1は研究・製造・短期滞在の自律運用実証になる（source_url: https://www.nasa.gov/?p=870336、https://www.vastspace.com/updates/vast-advances-haven-1-into-integration-phase）。

Sierra SpaceのLIFEは膨張式大型居住モジュールで、NASAは商業ステーション技術として扱う。LIFEはロボットそのものではないが、商業ステーションでは保守、点検、実験交換、船外作業を人だけで行うのは非効率なため、AMUやロボットアーム、自由飛行ロボットが運用費を決める（source_url: https://www.nasa.gov/humans-in-space/commercial-space/commercial-space-stations/、https://www.nasa.gov/general/nasas-commercial-partners-make-progress-on-low-earth-orbit-projects/）。

宇宙ステーションロボットでは、Canadarm3がGateway外部点検・ペイロード移設・車両支援の中核である。NASA Gatewayページは、CSAが大型アーム、小型器用アーム、専用ツール、地上管制セグメントを含む詳細設計・試験へ進んだと説明する（source_url: https://www.nasa.gov/reference/gateway-about/）。

Robonaut 2は2011年にISSへ送られた初の宇宙ヒューマノイドで、2018年まで滞在した。NASA公式の「Robonaut 3」運用後継は確認できないが、NASA SpinoffはApptronikのApolloをNASAのヒューマノイド研究の継続成果として紹介しているため、現状の後継軸はNASA直営機ではなく商業ヒューマノイド技術移転である（source_url: https://www.nasa.gov/robonaut2/、https://spinoff.nasa.gov/Humanoid_Robots_Assist_Assembly_Lines）。

ESA CIMONはISSで使われたAI支援ロボットで、2025年7月にはJAXA宇宙飛行士大西卓哉が「きぼう」でCIMONをセットアップしたとNASAが報じた。Int-Ball2はJAXAの「きぼう」内自由飛行カメラロボットで、2023年6月から機能実証されている（source_url: https://www.nasa.gov/blogs/spacestation/2025/07/29/muscles-ai-robotics-research-assisting-astronauts-as-next-crew-nears-launch/、https://corporate.epson/en/news/2024/240409.html）。

## スペースデブリ除去

デブリ除去の要件は、非協力ターゲットへの接近、相対航法、形状推定、タンブリング推定、捕獲、減速、再突入である。Astroscale ADRAS-JはH-IIA上段という実デブリに接近し、JAXA安全基準下でフライアラウンド観測を実施したため、商業デブリ除去の重要な前段実証である（source_url: https://global.jaxa.jp/press/2024/07/20240730-1_e.html）。

ClearSpace-1はESAが購入した世界初級の能動的デブリ除去ミッションで、対象デブリにランデブし、捕獲して大気圏再突入させる。ESAはClearSpace-1を「軌道上からデブリを除去する初のミッション」と位置づけ、アクティブデブリ除去市場の形成を狙う（source_url: https://www.esa.int/Space_Safety/ClearSpace-1）。

DARPA RSGSは静止軌道で協力衛星の点検・修理・寿命延長を行うロボットサービスである。DARPAは2022年時点で部品レベル試験完了、2025年に軌道上サービス開始見込みとしていたが、実運用スケジュールは防衛・商業契約に依存する（source_url: https://www.darpa.mil/news/2022/in-space-robot-mechanic、https://www.darpa.mil/program/robotic-servicing-of-geosynchronous-satellites）。

NASA OSAM-1はMaxarの衛星バスとSPIDERを含む軌道上給油・組立実証だったが、2024年に技術・コスト・スケジュール問題で停止された。OSAM-2/Archinaut Oneも2023年に飛行実証前に終了しており、NASAのISAMは大型単発デモから技術移転・商業連携へ比重を移している（source_url: https://www.nasa.gov/mission_pages/tdm/satellite-servicing.html、https://www.nasa.gov/mission/on-orbit-servicing-assembly-and-manufacturing-2-osam-2/）。

## 主要論文・公式資料

1. NASA Artemis I splashdown, 2022年12月11日（source_url: https://www.nasa.gov/blogs/artemis/2022/12/11/artemis-i-flight-day-26-orion-splashes-down-concluding-historic-artemis-i-mission/）
2. NASA Artemis II mission page, 2026年有人月周回（source_url: https://www.nasa.gov/mission/artemis-ii/）
3. NASA Artemis architecture update, 2026年2月27日（source_url: https://www.nasa.gov/news-release/nasa-adds-mission-to-artemis-lunar-program-updates-architecture/）
4. NASA Artemis III updates, 2027年LEOデモ（source_url: https://www.nasa.gov/artemis-iii-news-and-updates/）
5. NASA VIPER cancellation and alternatives（source_url: https://science.nasa.gov/mission/viper/、https://www.nasa.gov/blogs/missions/2025/05/07/nasa-to-explore-additional-methods-to-send-viper-to-moon/）
6. CNSA/CAS Chang’e-6 sample return, 1,935.3g（source_url: https://english.cas.cn/newsroom/cas_media/202406/t20240628_666011_2.shtml）
7. JAXA/Toyota Lunar Cruiser公式発表（source_url: https://global.jaxa.jp/press/2020/08/20200828-1_e.html）
8. GITAI JAXA lunar rover arm concept study, 2025年（source_url: https://gitai.tech/2025/03/31/gitai-awarded-jaxa-contract-for-concept-study-of-robotic-arm-for-crewed-pressurized-lunar-rover/）
9. JAXA CRD2 / ADRAS-J fly-around images（source_url: https://global.jaxa.jp/press/2024/07/20240730-1_e.html）
10. ESA ClearSpace-1（source_url: https://www.esa.int/Space_Safety/ClearSpace-1）
11. NASA Gateway / Canadarm3（source_url: https://www.nasa.gov/reference/gateway-about/）
12. NASA OSAM-1 cancellation and SPIDER（source_url: https://www.nasa.gov/mission_pages/tdm/satellite-servicing.html）
13. NASA OSAM-2 / Archinaut One conclusion（source_url: https://www.nasa.gov/mission/on-orbit-servicing-assembly-and-manufacturing-2-osam-2/）
14. NASA Commercial Space Stations strategy（source_url: https://www.nasa.gov/humans-in-space/commercial-space/commercial-space-stations/）
15. AIST HRP-5P公式発表（source_url: https://www.aist.go.jp/aist_e/list/latest_research/2018/20181116/en20181116.html）

## 2030-2050 宇宙ロボティクス景観予測

2030年までに、月面ロボットは「探査」から「基地準備」へ移る。Artemisは2028年以降の有人月面着陸と年次着陸を目標に再構成され、中国は嫦娥7/8とILRS先行技術で月南極資源へ進むため、月面ロボットの競争軸は水氷探査、電力敷設、通信塔設置、レゴリス処理になる（source_url: https://www.nasa.gov/artemis-iii-news-and-updates/、https://www.cnsa.gov.cn/english/n6465652/n6465653/c6812150/content.html）。

2030年代前半には、JAXA/Toyota Lunar Cruiser型の与圧ローバーと、GITAI型の作業アーム/ローバーが組み合わさり、有人滞在の前後にロボットが基地を点検・準備する運用が標準化する。日本の勝ち筋は大型ローバー、器用作業、デブリ除去、安全基準対応の組合せである（source_url: https://global.toyota/en/mobility/technology/lunarcruiser/、https://gitai.tech/2025/03/31/gitai-awarded-jaxa-contract-for-concept-study-of-robotic-arm-for-crewed-pressurized-lunar-rover/、https://www.kenkai.jaxa.jp/eng/crd2/）。

2040年までに、軌道上サービスは保険・規制・標準インターフェースと結びつき、非協力デブリ除去よりも、協力ターゲットの給油・姿勢回復・モジュール交換が先に市場化する。NASA OSAM-1/2の中止は失敗ではなく、実証機一発主義から商業ISAMエコシステムへ移る転換点である（source_url: https://www.nasa.gov/nexis/isam/）。

2050年には、月・火星・軌道上でロボットの設計思想が分化する。月面は建設機械型、火星は通信遅延に耐える自律作業員型、軌道上は軽量高精度アーム型が主流になる。ヒューマノイドはSpaceX/Tesla Optimusのような象徴的構想だけでなく、宇宙服・工具・施設を人間互換に保つ場合に価値を持つが、2026年時点で火星投入はCEO発言レベルであり、公式ミッション実証とは区別して記述すべきである（source_url: https://www.gmanetwork.com/news/scitech/technology/939421/starship-carrying-tesla-s-bot-set-for-mars-by-end-2026-elon-musk/story/）。
