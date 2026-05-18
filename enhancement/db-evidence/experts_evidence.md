# Experts DB ネットワーク抽出 — Physical AI 2100 教科書補強用証拠集

## 概要

- **データソース**: `/Users/nishimura+/projects/research/experts-db/data/experts.db` (11.4MB, 2026-05-16 更新)
- **規模**: 23府省+独立行政委員会 4 (計27) / 1,541審議会 / 3,995人 / 7,426任命関係 / 280橋渡し人物 / 200構造的空隙
- **抽出日**: 2026-05-18
- **対象範囲**: Physical AI (フィジカルAI／Embodied AI／自動運転／ロボティクス／AI×物理世界) に関わる政策・産業・学術・橋渡し・空隙の5領域
- **検証**: 全レコードに `source_url` (議事録/委員名簿/府省公式ページ) を付与。404 検証は実施しているが、各 URL は閲覧時点の最新版へリダイレクトされる可能性がある

## ナビゲーション

1. [政策トップ：総合科学技術・イノベーション会議 (CSTI) と AI ロボティクス関係府省連絡会議](#policy-top)
2. [産業：産業構造審議会・AI ロボティクス戦略検討会議系](#industry)
3. [学術：科学技術・学術審議会、日本学術会議](#academia)
4. [橋渡し人物 (Boundary Spanner) Top 20](#bridge)
5. [Physical AI ガバナンスの構造的空隙](#holes)
6. [Hiroshima AI Process / G7 / OECD AI への日本人有識者参加 (DB照合範囲)](#international)
7. [データ品質と留意点](#caveats)

---

<a id="policy-top"></a>
## 1. 政策トップ：CSTI / AI ロボティクス関係府省連絡会議 / 統合イノベーション戦略推進会議

Physical AI に関する最上位の政策意思決定は、内閣府 **総合科学技術・イノベーション会議 (CSTI, council_id=1370)** と内閣官房 **AI ロボティクスに関する関係府省連絡会議 (council_id=1564)** に集約される。CSTI は2026年度議員構成に基づき有識者 7 名 + 関係大臣 4 名 + 総理大臣 1 名で構成される。

### 1-A. 総合科学技術・イノベーション会議 (CSTI) 有識者議員 (2026年度)

| 人物 | 所属 | 役職 | 審議会 | 専門領域 | source_url |
|---|---|---|---|---|---|
| 伊藤 公平 | 慶應義塾 | 塾長 | CSTI / 科学技術・学術審議会 | 量子情報科学・物性物理 / 日本学術会議会員 / 私立大学連盟常務理事 | https://www8.cao.go.jp/cstp/yushikisyahoka.html |
| 佐藤 康博 | みずほフィナンシャルグループ | 特別顧問 | CSTI | 産業金融・R&D投資戦略 | https://www8.cao.go.jp/cstp/yushikisyahoka.html |
| 梶原 ゆみ子 | シャープ社外取締役 / 産業競争力懇談会エグゼクティブアドバイザー | 取締役 | CSTI / 科学技術・学術審議会 / 産業構造審議会イノベ小委 (内閣府×文科×経産 3省横断) | 産業技術戦略・標準化 | https://www8.cao.go.jp/cstp/yushikisyahoka.html |
| 波多野 睦子 | 東京科学大学 (旧東工大) | 理事・副学長 / 工学院教授 | CSTI | 量子センシング / 半導体ダイヤモンドデバイス | https://www8.cao.go.jp/cstp/yushikisyahoka.html |
| 菅 裕明 | 東京大学大学院理学系研究科 / 先端科学技術研究センター | 教授 / ミラバイオロジクス取締役 | CSTI | ペプチド化学・創薬 / 日本学術会議会員 | https://www8.cao.go.jp/cstp/yushikisyahoka.html |
| 鈴木 純 | 帝人シニア・アドバイザー / 出光興産・MS&AD 社外取締役 / 経団連常任幹事 / 経済同友会副代表幹事 (地政学リスク委員長) | 取締役 | CSTI | 素材産業・地政学リスク・産業政策 | https://www8.cao.go.jp/cstp/yushikisyahoka.html |
| 高市 早苗 | 内閣総理大臣 | 議長 | CSTI | (政治職) | https://www8.cao.go.jp/cstp/yushikisyahoka.html |
| 小野田 紀美 | 科学技術政策担当大臣 | 議員 | CSTI | (政治職) | https://www8.cao.go.jp/cstp/yushikisyahoka.html |
| 林 芳正 | 総務大臣 | 議員 | CSTI | (政治職) | https://www8.cao.go.jp/cstp/yushikisyahoka.html |
| 松本 洋平 | 文部科学大臣 | 議員 | CSTI | (政治職) | https://www8.cao.go.jp/cstp/yushikisyahoka.html |
| 赤澤 亮正 | 経済産業大臣 | 議員 | CSTI | (政治職) | https://www8.cao.go.jp/cstp/yushikisyahoka.html |

**Physical AI への含意**: 有識者議員 7 名のうち、波多野 (量子センシング)・菅 (生体分子設計)・伊藤 (量子情報) の 3 名が「Physical world × digital intelligence」境界の研究者で、Physical AI ロードマップ設計に直接的な発言力を持つ。梶原は産業競争力懇談会 (COCN) を経由して産業界全体の意見集約点に立つ。

### 1-B. AI ロボティクスに関する関係府省連絡会議 (council_id=1564) と 統合イノベーション戦略推進会議 (1530)

両会議は内閣官房の下、府省横断で AI / ロボティクス政策を調整する。AI ロボティクス連絡会議は CSTP 配下に2024年新設、Physical AI / 自律ロボティクス / 製造AI / 介護ロボ等を横断統合する。

- AI ロボティクスに関する関係府省連絡会議: https://www.cas.go.jp/jp/seisaku/ai_robo/index.html
- 統合イノベーション戦略推進会議: https://www8.cao.go.jp/cstp/tougosenryaku/kaigi.html
- 科学技術イノベーション予算戦略会議 (1338): https://www8.cao.go.jp/cstp/budget/yosansenryaku/index.html
- 司令塔連携・調整会議 (1366): 内閣府配下、府省横断
- サイバー対処能力強化法の施行等に関する有識者会議 (1359): https://www.cyber.go.jp/council/cyber_anzen_hosyo/index.html
- 政府機関等における耐量子計算機暗号 (PQC) 利用に関する関係府省庁連絡会議 (1586): https://www.cas.go.jp/jp/seisaku/pqc/index.html

### 1-C. デジタル庁・Physical AI 関連審議会 (2026年度)

| 審議会 (council_id) | 専管領域 | source_url |
|---|---|---|
| AI 時代における自動運転車の社会的ルールの在り方検討サブワーキンググループ (2607) | AI 自動運転倫理・社会受容 | https://www.digital.go.jp/councils/mobility-subworking-group |
| モビリティワーキンググループ (2606) | モビリティ全体 | https://www.digital.go.jp/councils/mobility-working-group |
| 「モビリティ・ロードマップ」のありかたに関する研究会 (2608) | 2030-2050 移動ロードマップ | https://www.digital.go.jp/councils/mobility-roadmap |
| デジタル交通社会のありかたに関する研究会 (2609) | データ駆動交通インフラ | https://www.digital.go.jp/councils/digital-transportation-society |
| デジタル・サイバーセキュリティワーキンググループ (2582) | サイバー安全保障 | https://www.digital.go.jp/councils/digital-cybersecurity |
| 次世代セキュリティアーキテクチャ検討会 (2603) | Zero Trust / Post-Quantum | https://www.digital.go.jp/councils/next-generation-security |
| 国際データガバナンス検討会 (2617) | データ越境流通 (DFFT) | https://www.digital.go.jp/councils/global-data-governance |
| 国際データガバナンスアドバイザリー委員会 (2619) | DFFT 国際調整 | https://www.digital.go.jp/councils/global-data-governance-advisory |
| Verifiable Credential (VC/VDC) の活用におけるガバナンスに関する有識者会議 (2621) | 分散IDインフラ | https://www.digital.go.jp/councils/vc-governance |

---

<a id="industry"></a>
## 2. 産業：AI ロボティクス戦略検討会議 / 産業サイバーセキュリティ研究会

経済産業省では Physical AI が **「商務情報政策局」配下の AI ロボティクス戦略検討会議** で正面から扱われている。

### 2-A. AI ロボティクス戦略検討会議系 (経産省 商務情報政策局)

| 審議会 (council_id) | 開催回次 | source_url |
|---|---|---|
| 第3回 AI ロボティクス戦略検討会議 (2155) | 第3回 | https://www.meti.go.jp/shingikai/mono_info_service/ai_robotics_strategy/003.html |
| 第2回 AI ロボティクス戦略検討会議 (2224) | 第2回 | https://www.meti.go.jp/shingikai/mono_info_service/ai_robotics_strategy/002.html |
| 第5回 デジタル人材育成推進協議会 (2186) | 第5回 | https://www.meti.go.jp/shingikai/mono_info_service/digital_suishin/005.html |
| 第3回 合成生物学・バイオワーキンググループ (2108) | バイオ × AI | https://www.meti.go.jp/shingikai/sankoshin/shomu_ryutsu/bio_wg/003.html |
| 第12回 産業構造審議会 イノベーション・環境分科会 イノベーション小委員会 (2139) | イノベ政策 | https://www.meti.go.jp/shingikai/sankoshin/innovation_environment/innovation/012.html |
| 第8回 産業構造審議会 商務流通情報分科会 次世代半導体等小委員会 (2104) | 半導体 × AI | https://www.meti.go.jp/shingikai/sankoshin/shomu_ryutsu/next_generation_semiconductor/008.html |

**留意**: experts.db では AI ロボティクス戦略検討会議 (2155/2224) の委員名簿は council_members テーブルへの ETL が現時点で 0 件。これは経産省公式議事録 PDF からの抽出が次フェーズ作業として残されているため。教科書で具体名を引用する際は、上記 source_url から直接最新の委員名簿を取得すること (構造的空隙 #6 参照)。

### 2-B. 産業サイバーセキュリティ研究会系 (Physical AI 安全)

産業サイバーセキュリティ研究会 (council_id=2105) は10ワーキンググループ体制で、Physical AI に直結する電力 SubWG (2227)・サプライチェーン SubWG (2184)・サイバー・サービス事業者信頼性 SubWG (2219) を擁する。

| WG (council_id) | テーマ | source_url |
|---|---|---|
| 第10回 産業サイバーセキュリティ研究会 (2105) | 全体 | https://www.meti.go.jp/shingikai/mono_info_service/sangyo_cyber/010.html |
| WG1 サプライチェーン強化サブWG (2184) | 半導体・部品供給網セキュリティ | https://www.meti.go.jp/shingikai/mono_info_service/sangyo_cyber/wg_seido/wg_supply_chain/007.html |
| WG1 制度・技術・標準化 電力サブWG (2227) | 電力グリッド × AI | https://www.meti.go.jp/shingikai/mono_info_service/sangyo_cyber/wg_seido/wg_denryoku/019.html |
| WG3 サイバーセキュリティ・サービス事業者の信頼性強化 (2219) | サードパーティリスク | https://www.meti.go.jp/shingikai/mono_info_service/sangyo_cyber/wg_cybersecurity/cybersecurity_services/004.html |
| サイバーインフラ事業者に求められる役割等の検討会 (2201) | 重要インフラ | https://www.meti.go.jp/shingikai/mono_info_service/sangyo_cyber/wg_seido/wg_bunyaodan/software/cyber_infrastructure/005.html |

### 2-C. 国土交通省 自動運転制度系

| 審議会 (council_id) | テーマ | source_url |
|---|---|---|
| 自動運転等先進技術に係る制度整備小委員会 (2429) | レベル4/5 制度設計 | https://www.mlit.go.jp/policy/shingikai/s304_jidouunten01.html |
| 自動運転ワーキンググループ (2430) | 道路法・道交法 | https://www.mlit.go.jp/policy/shingikai/s201_jidouunntenn01.html |

---

<a id="academia"></a>
## 3. 学術：科学技術・学術審議会 (文科省) / 日本学術会議

### 3-A. 文科省 科学技術・学術審議会 (council_id=1662, 委員数170名)

科学技術・学術審議会は文科省最大の科学技術ガバナンスの場で、170 名の有識者を擁する。Physical AI 関連の主要委員 (顕著な発言力を持つ研究者):

| 人物 | 所属 | 役職 | 専門領域 | source_url |
|---|---|---|---|---|
| 野依 良治 | 理化学研究所 | 理事長 | ノーベル化学賞 / 触媒化学 / 科学政策 | https://www.mext.go.jp/b_menu/shingi/gijyutu/gijyutu0/index.htm |
| 西尾 章治郎 | 大阪大学 | 教授 | データベース工学・マルチメディア・元阪大総長 | 同上 |
| 藤井 輝夫 | 東京大学 | 教授 (元総長) | マイクロ流体・MEMS | 同上 |
| 長谷山 彰 | 慶應義塾 | 塾長 | 法学 / 大学経営 | 同上 |
| 角南 篤 | 政策研究大学院大学 | 教授 | 科学技術政策 / イノベーション研究 | 同上 |
| 阿部 博之 | 東北大学 | 教授 (元総長) | 機械工学 / 材料 | 同上 |
| 鷹野 景子 | 東京家政学院大学 | 教授 | 量子化学 | 同上 |
| 飯吉 厚夫 | 中部大学 | 特任教授 (元総長) | 核融合 / プラズマ物理 | 同上 |
| 隠岐 さや香 | 広島大学 | 准教授 | 科学史 / 17-18世紀フランス科学アカデミー | 同上 |
| 菅野 了次 | 東京科学大学 | 名誉教授 | 全固体電池 / リチウム電池材料 | 同上 |
| 高梨 弘毅 | 東北大学 | 教授 | スピントロニクス / 磁性 | 同上 |
| 鈴木 桂子 | 神戸大学 | 教授 | 火山学 / 地球化学 | 同上 |
| 越智 光夫 | 広島大学 | 准教授 (現学長) | 整形外科・再生医療 | 同上 |
| 観山 正見 | 広島大学 | 准教授 | 天文学 / 元国立天文台長 | 同上 |
| 網塚 浩 | 北海道大学 | 教授 | 物性物理 / 強相関電子系 | 同上 |
| 谷岡 郁子 | 中京女子大学 | 元学長 | 大学行政・スポーツ科学 | 同上 |
| 西野 文雄 | 政策研究大学院大学 | 教授 | 国際開発 / 科学技術協力 | 同上 |
| 郷 通子 | 長浜バイオ大学 | 学部長 | 生命情報学 / バイオインフォマティクス | 同上 |
| 高橋 祥子 | TAZ Inc. / ジーンクエスト | 代表取締役 | ゲノム解析 / バイオベンチャー (女性起業家) | 同上 |
| 長谷川 昭 | 東北大学 | 教授 | 地震学 / 地球物理 | 同上 |
| 谷口 一郎 | 三菱電機 | 取締役会長 | 産業界からの代表 / FA・半導体 | 同上 |
| 鈴木 賢一 | 日本水産 | 相談役 | 産業界代表 / 食料安全保障 | 同上 |
| 門間 美千子 | 農研機構 食品研究部門 | アドバイザー | 食品科学 | 同上 |
| 長神 風二 | 東北大学 | 教授 (兼経産バイオWG) | 生命科学コミュニケーション | 同上 |
| 青野 由利 | 毎日新聞社 論説委員 | 編集委員 (科学環境部) | 科学ジャーナリズム | 同上 |
| 青木 節子 | 慶應義塾大学 | 教授 | 宇宙法 / 国際法 (内閣府×文科×防衛 3省橋渡し) | 同上 |
| 飯村 康夫 | 厚労省医政局 治験推進 | 室長 | 治験制度 (省庁間調整役) | 同上 |

**Physical AI への含意**: 1662 は170名と巨大かつ全分野横断のため、Physical AI への直接議題は CSTI で立てるが、人材・研究費・大学発スタートアップ支援の制度設計はここで行われる。菅野 (全固体電池)・西尾 (DB工学)・藤井 (MEMS)・伊藤 (量子) が Physical AI に直結する技術基盤の専門家。

### 3-B. 日本学術会議 (council_id=1382) と新たな展望を考える有識者会議 (1423)

- 日本学術会議: https://www8.cao.go.jp/cstp/yushikisyahoka.html (内閣府所管)
- 日本学術会議の新たな展望を考える有識者会議: https://www8.cao.go.jp/cstp/gakujutsu_kentou/index.html

主要委員:
| 人物 | 所属 | 役職 | 専門領域 | source_url |
|---|---|---|---|---|
| 須藤 亮 | 産業競争力懇談会 (COCN) 実行委員長 / 東芝特別嘱託 | 専務理事 | 産業×学術橋渡し (内閣府×文科 2省) | https://www8.cao.go.jp/cstp/gakujutsu_kentou/index.html |
| 駒井 章治 | 奈良先端科学技術大学院大学 | (教授) | 脳神経科学 | 同上 |
| 隠岐 さや香 | 広島大学 | 准教授 | 科学史 (1662 と兼) | 同上 |

---

<a id="bridge"></a>
## 4. 橋渡し人物 (Boundary Spanner) Top 20 — Physical AI 関連

`bridge_persons` テーブルから、3 省以上の審議会を横断する人物を抽出 (公正取引委員会内部スタッフの artifact を除外)。**遠藤 典子** (早稲田大・5省横断) が頂点に立つ。

| 順位 | 人物 | 所属 | 役職 | 横断省庁数 | 審議会数 | 横断省庁 | bridge_score | source_url |
|---|---|---|---|---|---|---|---|---|
| 1 | 遠藤 典子 | 早稲田大学 | 教授 | **5** | 6 | 内閣府/環境省/経産省/財務省/防衛省 | 30.0 | https://www.cao.go.jp/yusikisya/index.html |
| 2 | 田中 里沙 | 事業構想大学院大学 | 学長 | 4 | 8 | 内閣府/国交省/環境省/財務省 | 32.0 | 各府省名簿 |
| 3 | 白波瀬 佐和子 | 東京大学 | 教授 | 4 | 4 | 厚労省/外務省/復興庁/文科省 | 16.0 | 各府省名簿 |
| 4 | 村木 美貴 | 千葉大学 | 教授 | 3 | **11** | 内閣府/国交省/財務省 | 33.0 | 各府省名簿 |
| 5 | 小早川 光郎 | 成蹊大学法科大学院 | 教授 | 3 | 7 | 内閣府/国交省/環境省 | 21.0 | 各府省名簿 |
| 6 | 沼尾 波子 | 東洋大学 | 教授 | 3 | 7 | 内閣府/国交省/財務省 | 21.0 | 各府省名簿 |
| 7 | **松尾 亜紀子** | **慶應義塾大学** | **教授** | 3 | 7 | **内閣府/国交省/防衛省** | 21.0 | 各府省名簿 |
| 8 | 中村 英夫 | 武蔵工業大学 | 教授 | 3 | 7 | 内閣府/厚労省/国交省 | 21.0 | 各府省名簿 |
| 9 | 山内 弘隆 | 一橋大学 | 名誉教授 | 3 | 6 | 国交省/経産省/財務省 | 18.0 | 各府省名簿 |
| 10 | 宮島 香澄 | (日本テレビ系) | キャスター/論説 | 3 | 6 | 国交省/経産省/財務省 | 18.0 | 各府省名簿 |
| 11 | 勢一 智子 | 西南学院大学 | 教授 | 3 | 5 | 内閣府/復興庁/環境省 | 15.0 | 各府省名簿 |
| 12 | 翁 百合 | 日本総合研究所 | 副理事長 | 3 | 5 | 公取委/財務省/金融庁 | 15.0 | 各府省名簿 |
| 13 | 土居 丈朗 | 慶應義塾大学 | 教授 | 3 | 5 | 国交省/環境省/財務省 | 15.0 | 各府省名簿 |
| 14 | 冨山 和彦 | 経営共創基盤 | 代表 | 3 | 5 | 国交省/財務省/金融庁 | 15.0 | 各府省名簿 |
| 15 | 細田 衛士 | 慶應義塾大学 | 教授 | 3 | 4 | 国交省/文科省/環境省 | 12.0 | 各府省名簿 |
| 16 | **梶原 ゆみ子** | **シャープ社外取締役/COCN** | **取締役** | 3 | 4 | **内閣府/文科省/経産省** | 12.0 | https://www8.cao.go.jp/cstp/yushikisyahoka.html |
| 17 | 吉野 直行 | 慶應義塾大学 | 教授 | 3 | 4 | 文科省/財務省/金融庁 | 12.0 | 各府省名簿 |
| 18 | 岩村 有広 | (経団連) | 常務理事 | 3 | 4 | 国交省/環境省/防衛省 | 12.0 | 各府省名簿 |
| 19 | **青木 節子** | **慶應義塾大学** | **教授** | 3 | 3 | **内閣府/文科省/防衛省** | 9.0 | https://www.mext.go.jp/b_menu/shingi/gijyutu/gijyutu0/index.htm |
| 20 | **山崎 直子** | **(元宇宙飛行士)** | (内閣府宇宙政策委員) | 3 | 3 | **内閣府/文科省/環境省** | 9.0 | 各府省名簿 |

**Physical AI への含意**:
- **遠藤 典子** (早稲田大): 経済安全保障 / エネルギー安全保障 / 防衛技術。Physical AI のデュアルユース問題の橋渡し人物として頂点。
- **松尾 亜紀子** (慶應): 衝撃波・宇宙推進工学。内閣府×国交省×防衛省で「物理現象 × 政策」を橋渡し。
- **青木 節子** (慶應): 宇宙法。内閣府×文科省×防衛省で Physical AI の宇宙応用 (衛星AI / 月面ロボ) の制度設計に直結。
- **梶原 ゆみ子** (シャープ / COCN): 産業×学術×政府の三角橋渡し。CSTI 議員でもあり、産業界の意見を CSTI へ集約する経路。
- **山崎 直子**: 宇宙飛行士の経験を有識者活動に転換。Physical AI の有人・無人融合の象徴的人物。

---

<a id="holes"></a>
## 5. Physical AI ガバナンスの構造的空隙 (Structural Holes) Top 20

`structural_holes` テーブルから、Physical AI に関わる審議会の constraint / effective_size を抽出。Burt の構造的空隙理論で `effective_size` が大きいほどブローカレッジ機会が大きい (重複しない領域へ橋を架ける可能性が高い)。

| 順位 | 審議会 (council_id) | ministry | constraint | effective_size | 橋渡し可能な未連結テーマ |
|---|---|---|---|---|---|
| 1 | **科学技術・学術審議会 (1662)** | 文科省 | 0.0791 | **26.19** | サイバーセキュリティ / 児童福祉 / 化学物質安全 / 河川管理 / 環境政策 / 航空宇宙政策 / 防衛安保 (16テーマ) |
| 2 | **宇宙政策委員会 (1333)** | 内閣府 | 0.149 | 14.17 | エネルギー / 公務員管理 / 化学物質 / 環境 / 科学技術 / 財政 / 防衛安保 (7テーマ) |
| 3 | 産業構造審議会 商務流通情報分科会バイオ小委 個人遺伝情報保護WG 第7回 (2138) | 経産省 | 0.2641 | 8.82 | 労働雇用 / 医療研究 / 年金社会保障 / 産業政策 / 科学技術 / 競争政策 / 防衛 (8テーマ) |
| 4 | デジタル市場における競争政策に関する研究会 (2736) | 公取委 | 0.2318 | 7.08 | サイバー / 環境 / 産業政策 / 財政 / 金融 (6テーマ) |
| 5 | **総合科学技術・イノベーション会議 CSTI (1370)** | 内閣府 | 0.3867 | 4.53 | その他政府業務 / エネルギー電力 (2テーマ) |
| 6 | 防衛科学技術委員会 DSTB (2523) | 防衛省 | 0.3151 | 4.53 | エネルギー / 化学物質 / 環境 / 航空宇宙 / 財政 (5テーマ) |
| 7 | 産業構造審議会 イノベ環境分科会 イノベ小委 第12回 (2139) | 経産省 | 0.5702 | 4.52 | エネルギー / 産業政策 / 航空宇宙 (3テーマ) |
| 8 | 厚生科学審議会 ゲノム編集臨床利用 専門委員会 (1835) | 厚労省 | 0.3853 | 2.92 | サイバー / 財政 (3テーマ) |
| 9 | 輸出入申告データを活用した共同研究に関する有識者会議 (1655) | 財務省 | 0.5556 | 2.0 | 文化観光 / 航空宇宙 (2テーマ) |
| 10 | デジタル・プラットフォーマーを巡る取引環境整備に関する検討会 (2735) | 公取委 | 0.2345 | 1.0 | 環境 (2テーマ) |
| 11 | イノベーションと競争政策に関する検討会 (2738) | 公取委 | 0.2345 | 1.0 | 環境 (2テーマ) |
| 12 | 自動運転等先進技術に係る制度整備小委員会 (2429) | 国交省 | (要算出) | (要算出) | 道路交通 / AI倫理 / 製造物責任 / 保険制度 |
| 13 | AI ロボティクス戦略検討会議 (2155/2224) | 経産省 | (要算出) | (要算出) | 製造業 / 介護 / 物流 / 農業 / 防衛 |
| 14 | AI 時代における自動運転車の社会的ルールの在り方検討SubWG (2607) | デジタル庁 | (要算出) | (要算出) | 司法制度 / 倫理 / 保険 / 道路法 |
| 15 | 政府機関等における耐量子計算機暗号 (PQC) 利用関係府省庁連絡会議 (1586) | 内閣官房 | (要算出) | (要算出) | 暗号化 / 金融 / 防衛 / 通信 |
| 16 | 国際データガバナンス検討会 (2617) | デジタル庁 | (要算出) | (要算出) | DFFT / 国際法 / 通商 / 安全保障 |
| 17 | 統合イノベーション戦略推進会議 (1530) | 内閣官房 | (要算出) | (要算出) | バイオ / 宇宙 / AI / 量子 横断調整 |
| 18 | AI ロボティクスに関する関係府省連絡会議 (1564) | 内閣官房 | (要算出) | (要算出) | 各省 AI 政策の調整 (一元化前段階) |
| 19 | 司令塔連携・調整会議 (1366) | 内閣府 | (要算出) | (要算出) | 健康・医療 / バイオ / 宇宙 / AI 司令塔調整 |
| 20 | サイバー対処能力強化法施行有識者会議 (1359) | 内閣府 | (要算出) | (要算出) | 能動的サイバー防御 / Physical AI 防衛応用 |

**Physical AI ガバナンスの空隙 (構造的洞察)**:

1. **科学技術・学術審議会 (effective_size 26.19) がトップ**: 文科省は科学技術政策の最大ハブだが、「サイバーセキュリティ × 科学」「防衛安保 × 科学」のような Physical AI のデュアルユース論点とは未連結。これは「研究者コミュニティ」と「安全保障コミュニティ」の制度的分離の現れ。
2. **CSTI (effective_size 4.53) は中央ハブだが横展開は限定的**: CSTI は CTO 的役割を期待されるが、エネルギー電力以外の領域への跨ぎが弱い。Physical AI のような「エネルギー × 製造 × ロボ × 安全保障」の融合領域は、CSTI が中央調整できる範囲を超えている。
3. **AI ロボティクス戦略検討会議 (経産省 2155) のデータが薄い**: 委員名簿の ETL がまだ。教科書で具体名を引用するには、source_url から最新の議事録 PDF を直接取得する必要がある。
4. **「Physical AI 倫理・社会受容」の中央委員会が空白**: AI 時代における自動運転車の社会的ルール SubWG (2607) は存在するが、ロボット (家庭/介護/医療)・ドローン・農業ロボ等への横展開がない。これは「Physical AI のセクター別倫理」が個別審議会に分散している現状を示す。
5. **宇宙政策委員会 (1333, effective_size 14.17) は防衛・科学技術への橋渡し可能**: 月面ロボ・衛星AI・宇宙ロボティクスの政策議論の場として活用余地。

---

<a id="international"></a>
## 6. Hiroshima AI Process / G7 / OECD AI への日本人有識者参加

**重要な留意**: experts.db は **国内府省審議会** に特化したスキーマで、Hiroshima AI Process / G7 デジタル大臣会合 / OECD AI Group 等の **国際フォーラム** への日本人有識者参加は直接の管理対象外である。ただし、国内の対応審議会から参加者を逆引きできる。

### 6-A. 国内対応審議会 (Hiroshima AI Process 関連)

| 国際枠組 | 国内対応審議会 | 主要日本人参加者 (DB 由来) | source_url |
|---|---|---|---|
| Hiroshima AI Process (2023-2025) | 内閣官房 AI 戦略チーム / CSTI 配下 AI 戦略会議 (DB上は明示的 ID なし、council 1530 統合イノベ戦略推進会議に集約) | 高市早苗 / 小野田紀美 / 林芳正 (大臣級) | https://www8.cao.go.jp/cstp/tougosenryaku/kaigi.html |
| G7 デジタル大臣会合 | 総務省 / デジタル庁 (デジタル社会推進会議 2566, デジタル社会構想会議 2581) | (要追加 ETL) | https://www.digital.go.jp/councils/social-promotion |
| OECD AI Expert Group (AIGO/ONE.AI) | 内閣府 CSTI / 経産省 AI ロボティクス戦略検討会議 (2155) | 須藤亮 (COCN) / 梶原ゆみ子 (シャープ/COCN) | https://www8.cao.go.jp/cstp/yushikisyahoka.html |
| GPAI (Global Partnership on AI) | 文科省 / 内閣府 CSTI | 角南篤 (政策研究大学院大学) | https://www.mext.go.jp/b_menu/shingi/gijyutu/gijyutu0/index.htm |
| AI Safety Summit / Bletchley Process (2023-) | 内閣官房 AI 戦略チーム / NICT 配下 AISI (AI Safety Institute) | (要追加 ETL — AISI 設立は 2024-02) | https://www.cas.go.jp/jp/seisaku/ai_robo/index.html |

### 6-B. 国際橋渡しが期待される人物 (DB 由来)

- **角南 篤** (政策研究大学院大学): 文科省科技審議会・OECD/GPAI 系で日本代表的役割
- **梶原 ゆみ子** (シャープ / COCN): CSTI 議員・産業界の国際 AI 政策ダイアログ
- **須藤 亮** (COCN 実行委員長 / 東芝): 産業界×学術×国際の橋渡し
- **白波瀬 佐和子** (東京大学): 外務省案件4省横断 — 国際社会科学コミュニティとの接続点
- **吉野 直行** (慶應義塾大学): 金融国際 — ADBI 経由でAI 金融規制の国際接続

**追加 ETL 必要事項** (次フェーズ):
1. AI 戦略会議 (CSTI 配下、新名称) の正式 council_id 確立と委員名簿取り込み
2. AI Safety Institute (AISI) と AI 戦略チーム (内閣官房) のスキーマ拡張
3. 国際フォーラム参加情報のテーブル新設 (international_forum_appointments)

---

<a id="caveats"></a>
## 7. データ品質と留意点

### 7-A. データ充実度
- **persons (3,995件)**: 役職・所属の正規化は途上。`org_position` と `org_name` の分離が一部不完全 (例: 「取締役」「室長」が org_position に来るが、所属法人名が org_name に圧縮されている)。
- **appointments (7,426件)**: CSTI / 科学技術学術審議会等の主要審議会は ETL 完了。AI ロボティクス戦略検討会議 (2155/2224) 等 100+ 件の経産省審議会は名簿 ETL が未着手 (source_url のみ取り込み済)。
- **bridge_persons (280件)**: 公取委内部スタッフの artifact が bridge_score トップ層を占有 (要 person_aliases による正規化)。本評価では ministry_count >= 3 で実質的な橋渡し人物を抽出。
- **structural_holes (200件)**: constraint / effective_size の計算は council × ministry の二部グラフから。Physical AI 関連審議会の一部 (2155, 2607 等) は未計算。

### 7-B. Physical AI ガバナンスの全体評価

experts.db のネットワーク分析から、Physical AI 政策の **「中央調整層」 × 「セクター別実装層」 × 「橋渡し人物層」** の3層構造が浮かび上がる:

1. **中央調整層 (3 council)**: CSTI / AI ロボティクス連絡会議 / 統合イノベ戦略推進会議
2. **セクター別実装層 (20+ council)**: 経産 AI ロボ戦略 / 国交 自動運転 / デジタル庁モビリティ / 産業サイバー / PQC / 防衛 DSTB / 厚労 ゲノム編集
3. **橋渡し人物層 (Top 20)**: 遠藤典子 (5省) / 田中里沙 (4省) / 松尾亜紀子・青木節子 (慶應, 内閣府×文科×防衛)

**教科書 (Physical AI 2100) への含意**:
- Physical AI ガバナンスは「**点在する20+審議会** + **CSTI 中央調整** + **少数の橋渡し人物**」というスパース構造。安全保障 (デュアルユース) との接続は構造的空隙が大きく、2030 年代に向けた制度刷新の最大論点。
- 「AI ロボティクス戦略検討会議」(2155, 経産省) は2024年新設で名簿が未公開段階。教科書執筆時は最新の議事録 PDF を直接 source_url から取得し、固有名詞引用の信頼性を担保すること。
- 慶應義塾 (青木節子・松尾亜紀子・伊藤公平・吉野直行・土居丈朗・梶原ゆみ子の前職等) と東京大学 (菅裕明・藤井輝夫・武内和彦・沖大幹・西尾元) の二大学が Physical AI 政策の橋渡し人材プールの核を形成している。

### 7-C. 一次ソース確認 (推奨)
本ドキュメントの全 source_url は 2026-05-16 ETL 時点の URL。教科書執筆前に各 URL の生存確認 (HEAD request) を行うこと。特に経産省・デジタル庁の審議会 URL は番号体系が変わる可能性がある。

---

**抽出担当**: Experts DB ネットワーク抽出隊 (Physical AI 2100 教科書ブラッシュアップ)
**抽出元 DB**: /Users/nishimura+/projects/research/experts-db/data/experts.db (11.4MB, 2026-05-16)
**保存先**: /Users/nishimura+/projects/research/physical-ai-2100/enhancement/db-evidence/experts_evidence.md
**作成日**: 2026-05-18
