# Physical AI 2100 教科書 既存コンテンツ監査レポート

**監査対象**: `/Users/nishimura+/projects/research/physical-ai-2100/output/index.html`
**規模**: 313,051 bytes / 1,723 行 / 86 H2 / 16 H1 / 15 SVG / 推定 約 98K 字（本文）
**監査日**: 2026-05-18
**監査主体**: 既存コンテンツ監査隊（AR-DB ブラッシュアップ Wave 0）

---

## 1. 章別構造マップ

教科書は「序章＋3部11章＋終章」の13章構造で、各章の H2 セクション数・推定字数・SVG・引用人物を以下に網羅する。

### 序章（PROLOGUE）
- **位置**: line 168-189
- **H2 セクション数**: 1（章タイトルのみ。article-h2 なし）
- **推定字数**: 約 2,500 字
- **SVG**: なし
- **引用人物**: マーシャル・マクルーハン（『メディア論』1964）
- **構成**: エピグラフ＋導入 5 段落＋プルクオート
- **特記**: 5層射程の宣言（技術精緻 / 構造拡張 / 7フェーズ / 6波及 / 4時点）

### 第1部 ── 系統論（PART 1）

#### Chapter 01: 双子峰の高原とフィジカルAIの位置
- **位置**: line 192-298
- **H2 セクション数**: 5（双子峰／特異性留保／定義／後峰位置／前峰比較／作法）＋章タイトル
- **推定字数**: 約 6,800 字
- **SVG**: 図1-1（line 222-269、双子峰の高原モデル CTI v2 折れ線図）
- **引用人物**: McLuhan, Smil, Robert Gordon, Ian Morris, Carlota Perez, Kurzweil, Stuart Russell, Bostrom, Acemoglu & Johnson, Jensen Huang
- **finding-box**: あり（line 294）
- **特記**: 「CTI v2 双子峰モデル」（前峰0.764 vs 後峰0.768）が本書の理論的支柱

#### Chapter 02: 5系統合流の系譜と現在地
- **位置**: line 301-416
- **H2 セクション数**: 7（hw／ctrl／rl／fm／sim／合流5閾値／現在地）
- **推定字数**: 約 7,200 字
- **SVG**: 図2-1（line 343-396、5系統合流の系譜 1950-2026 時系列線図）
- **引用人物**: Varela-Thompson-Rosch, Devol, Engelberger, Scheinman, 加藤一郎（WABOT-1）, Gill Pratt, Brooks, Featherstone, Mnih(DQN), Schulman(PPO), Haarnoja(SAC), Vaswani(Transformer), Brown(GPT-3), Radford(CLIP), Ahn(SayCan), Brohan(RT-1/RT-2), Driess(PaLM-E), Kim(OpenVLA), Hwangbo(ANYmal Sim2Real), Chi(Diffusion Policy), Khazatsky(DROID)
- **finding-box**: あり（line 412）

#### Chapter 03: 8系統への拡張
- **位置**: line 418-548
- **H2 セクション数**: 5（bio／mat／cog／3層構造／独立化根拠／オーケストラ先取り）
- **推定字数**: 約 8,500 字
- **SVG**: 図3-1（line 462-517、8系統 3層モデル ボックス図）
- **引用人物**: Pfeifer & Bongard, McCulloch-Pitts, Rosenblatt, Hebb, Maass-Markram, Merolla(TrueNorth), Lichtsteiner, Whitesides, Wehner(Octobot), Ma(RoboBee), Khatib(OceanOneK), Kriegman-Levin-Bongard(Xenobot), Gumuskaya(Anthrobot), Cooper(Mobile Chemist), Szymanski-Ceder(A-Lab), Boiko(Coscientist), Abramson(AlphaFold 3), Merchant(GNoME), Bardeen-Brattain-Shockley, Kurzweil, Lakoff-Johnson, Maturana-Varela, Friston, Ha-Schmidhuber, LeCun(JEPA), Clark-Chalmers, Hutchins, Metta(iCub), Pezzulo
- **finding-box**: あり（line 544）
- **特記**: stream_bio／stream_mat／stream_cog の独立化が本書の理論的革新

### 第2部 ── 7フェーズロードマップ（PART 2）

#### Chapter 04: Phase A & B（2026-2040）── VLA基盤定着→物理操作汎化
- **位置**: line 551-705
- **H2 セクション数**: 6（Phase A／Phase A ボトルネック／Phase B／Phase A 地政学／Phase B 人材／A→B 連鎖）
- **推定字数**: 約 9,800 字
- **SVG**: 図4-1（line 569-609 Phase A 5系統状態）、図4-2（line 631-679 Phase B マイルストーン時系列）
- **引用人物**: Brooks, Brohan(RT-2), Kim(OpenVLA), Padalkar(Open X-Embodiment), Hassabis, Khosla, Di Carlo(Convex MPC), Khatib, Bisk(PIQA), Patterson(電力推計), Geim-Novoselov, Whitesides, Ha-Schmidhuber, Hafner(DreamerV3), LeCun(JEPA), Friston
- **finding-box**: あり（line 685）
- **特記**: 地政学三極（米中欧）と「ハイブリッド・マネージャ」職種定義

#### Chapter 05: Phase C & D（2040-2060）── 人間-機械並走→自律物理エージェント
- **位置**: line 707-843
- **H2 セクション数**: 6（Phase C／Phase C ボトルネック／Phase D／C-D 倫理／C-D UBI／C-D 世界モデル統合）
- **推定字数**: 約 9,200 字
- **SVG**: 図5-1（line 728-756 Cognitive Stack 4層）、図5-2（line 776-813 人間-AI 分業構造）
- **引用人物**: Wiener, Legg, Hassabis, Kurzweil, AI Impacts, Beauchamp & Childress, Sinclair(Yang-Hayano-Sinclair), Joby Aviation, Anish Mishra, Friston, Hafner, LeCun, Mishra
- **finding-box**: あり（line 821, 915）
- **特記**: AI Personhood 議論、Cognitive Stack 4層アーキテクチャ定義

#### Chapter 06: Phase E, F & G（2060-2100）── 知性のオーケストラ→関係論的物理生態系
- **位置**: line 845-1002
- **H2 セクション数**: 8（Phase E／Phase F／Phase G／2100まなざし／E-G 物質代謝兆候／G 境界溶解／E-G 周辺基盤）
- **推定字数**: 約 10,500 字
- **SVG**: 図6-1（line 866-901 三境界溶解 時系列ガント）、図6-2（line 929-968 知性のオーケストラ 円形配置）
- **引用人物**: Varela-Thompson-Rosch, Hutter(AIXI), Kurzweil, Levin(Tufts), Cooper, Szymanski-Ceder, Boiko, Weiser(ubicomp), Hutchins, Clark, Bostrom, Friston, Pickett(都市生態学), Ecovative, Rockström(惑星境界)
- **finding-box**: あり（line 915, 986）
- **特記**: 「境界溶解点」概念、6 周辺基盤（エネルギー／規制／倫理／教育／データ／文化）

### 第3部 ── 6波及分野（PART 3）

#### Chapter 07: 製造・医療・農業の組み換え
- **位置**: line 1004-1165
- **H2 セクション数**: 7（製造／医療・介護／農業／三領域転換軸／規制成熟度／人材構造／地政学）
- **推定字数**: 約 10,200 字
- **SVG**: 図7-1（line 1062-1109 動詞組み換え軌道）、図7-2（line 1116-1150 規制成熟度マトリクス）
- **引用人物**: IFR World Robotics 2024, Lee-Bagheri-Kao, Acemoglu & Restrepo, Wang & Urban, Brodin, Boo & Khalil, Rubenstein(Swarm), OECD Health Statistics, Esteva, Gulshan, McKinney, Liu & Faes, Jumper(AlphaFold 2), Abramson(AlphaFold 3), Beam & Kohane, Sharkey & Sharkey, Morimoto-Takeuchi, Friston, Pezzulo, Beauchamp & Childress, John Deere, Planet Labs, Solar Foods, Vivent SA(Cocozza), Pivot Bio, Voytas Lab, Fernie & Yan, Bossio, Calvo-Sahi-Trewavas, Willett(EAT-Lancet)
- **finding-box**: あり（line 1052）

#### Chapter 08: 都市・宇宙・教育の組み換え
- **位置**: line 1167-1271
- **H2 セクション数**: 6（都市／宇宙／教育／三領域転換軸／15分都市／宇宙3経路／教育オーケストラ）
- **推定字数**: 約 10,800 字
- **SVG**: 図8-1（line 1225-1252 人類圏輪郭組み換え 同心円）
- **引用人物**: Howard, Le Corbusier, Jane Jacobs, Carlos Moreno, Waymo, Tesla, Apollo Go, ICON(3Dプリント), Henk Jonkers(自己修復), Skylar Tibbits(4D), Christopher Alexander, Pierre Teilhard de Chardin, Mark Weiser, Ebenezer Howard, Khan Academy/Khanmigo, Vanderbilt(Kestin), Belpaeme, Holstein, Makransky-Petersen, Davidesco, Andy Clark, Edwin Hutchins, Russell, Tony Milligan-Szocik, Atwater-Hajimiri(SSPP MAPLE), Bruno Latour, Mariana Mazzucato, コメニウス, デューイ, フレイレ, マラグッツィ
- **finding-box**: あり（line 1215）

### 第4部 ── 統合・人材論（PART 4）

#### Chapter 09: 4時点の高解像度社会像
- **位置**: line 1273-1420
- **H2 セクション数**: 8（9.1 2030／9.2 2050／9.3 2070／9.4 2100／9.4.5 朝5要素／9.4.6 地理多様性／9.4.7 倫理含意／9.5 80年5転換）
- **推定字数**: 約 13,500 字（本書中最大）
- **SVG**: 図9-1（line 1368-1404 80年5転換マトリクス）
- **引用人物**: ヤン・デ・フリース（架空ペルソナ）, アミナ・トラオレ（架空）, 高井ヤエ子（架空）, アブドゥル・カマウ（架空）, カミラ・サントス（架空）, ヨンナ・グズムンスドッティル（架空）, ペッカ・ハッカネン（架空）, マリア・ロドリゲス（架空）, ブディ・ハルトノ（架空）, 田島和正（架空）, レイラ・ハッサン（架空）, アンナ・エリナ・マルタ・ヨハネス・オウル（架空）, Cyberdyne HAL, Solar Foods, Andy Clark, Hutchins, Friston, Pezzulo, Sharkey, Frey & Osborne, McKinsey 2024
- **特記**: 4時点×14ペルソナ「朝のシーン」。本書独自の方法論

#### Chapter 10: 譜面を書く者の作法 ── 12能力＋αが指す方向
- **位置**: line 1422-1569
- **H2 セクション数**: 8（10.1 2030／10.2 2050／10.3 2070／10.4 2100／10.5 12能力方向／10.6 教育含意／10.7 キャリア含意／10.8 組織含意）
- **推定字数**: 約 11,200 字
- **SVG**: 図14（line 1507-1553 17能力＋4項目世代配置）
- **引用人物**: era-talents DB, WEF, OECD Learning Compass 2050, Russell『Human Compatible』, Mol『The Logic of Care』, Mancuso & Viola, Mahmood Mamdani, デ・ラ・カデナ, Bruno Latour, Strathern『The Gender of the Gift』, シモーヌ・ヴェイユ, ファノン, コメニウス, デューイ, モンテッソーリ, レッジョ・エミリア, フレイレ, マラグッツィ, ベル・フックス, Marcus Hutter
- **特記**: 17能力＋4項目モデル。前プロジェクト「Talent 補論」との二重らせん

### 補論章（Chapter 11）

#### Chapter 11: FVCP補論シリーズへの位置づけ ── 5補論の交差点
- **位置**: line 1572-1657
- **H2 セクション数**: 8（製造v6／MOB／HRORG／Talent／5補論共通中軸／本書固有貢献／5補論発展系譜／品質ゲート／方法論汎用性／到達点と未着手）
- **推定字数**: 約 7,800 字
- **SVG**: 図13（line 1619-1653 5補論交差点 5円配置）
- **引用人物**: Latour, Viveiros de Castro, デ・ラ・カデナ, Ingold, Hinton & Hassabis, Acemoglu

### 終章（EPILOGUE）
- **位置**: line 1659-1700
- **H2 セクション数**: 5（本書の限界／読者への次の問い／FVCP接続／14シーン構造／3つの一歩）
- **推定字数**: 約 4,800 字
- **SVG**: なし
- **引用人物**: 14ペルソナ群再登場、Bostrom, Wiener, Mamdani, デ・ラ・カデナ, Latour

---

## 2. 15 SVG の役割と問題点

各 SVG を「位置／意図／視覚デザインの問題／改善方向性」の 4 観点で評価する。15 図解中 13 図解が `#CC1400` 単色アクセントの折れ線・ボックス・マトリクスで構成され、視覚的多様性に乏しい。

### 図1-1（line 222、双子峰の高原モデル）
- **位置**: Ch1「フィジカルAIの定義」直後
- **意図**: 1750-2100 の CTI v2 指数推移で「双子峰（前峰0.764 / 後峰0.768）」を視覚化
- **問題点**: 折れ線が手書き風で精度感がない／高原ラインと峰の高度差が直感的に読み取れない／前峰・後峰のラベル文字 0.764 vs 0.768 が小さすぎる／凡例なし
- **改善方向性**: 再設計（精緻な折れ線＋シェード塗りで高原を可視化、峰の高さに帯付きで誤差バー、X軸を log scale 補助）

### 図2-1（line 343、5系統合流の系譜）
- **位置**: Ch2「2026年の合流地点」前
- **意図**: 5系統（hw/ctrl/rl/sim/fm）の独立発展→2023-2026 合流→VLA を時系列線で示す
- **問題点**: 5本の線が交差点なしで右側に集約されるだけで「合流」の構造的意味が表現されない／系統ごとの色分けが灰色1色＋赤1色のみで識別困難／Open X-Embodiment 等の合流ノードが点として明示されていない
- **改善方向性**: 再設計（5本に異なる色を割当て、合流点を太い赤丸＋ラベル付き、stream_fm を赤帯で強調、時間軸目盛りに 1950/1980/2000/2017/2023/2026 を等間隔ではなく実時間スケールで配置）

### 図3-1（line 462、8系統の3層モデル）
- **位置**: Ch3「8系統への拡張」中盤
- **意図**: 物理基盤層／実装層／学習・知能層の3層構造と 8 系統の所属を示す
- **問題点**: 単なるボックス積み重ねで「駆動順序」「フィードバック」が矢印 2 本のみ／第三層 4 系統が並列でしかなく相互関係が不在／新系統（stream_bio/mat/cog）の赤強調は良いが境界溶解の予兆が表現されない
- **改善方向性**: 拡張（3層構造を維持しつつ、矢印を駆動順序として太細で表現、stream_bio を第二層と第三層に跨らせる橋構造で描く、フィードバックループを赤点線で円環状に追加）

### 図4-1（line 569、Phase A 5系統状態）
- **位置**: Ch4 Phase A 中盤
- **意図**: 2026-2030 の stream_fm 主導駆動関係を視覚化
- **問題点**: 中心の stream_fm から下層4系統へ矢印が放射するだけで「VLA 標準化」の本質が伝わらない／下部の Phase A 末到達状態が箇条書きで図解と分離／時系列要素が完全に欠落
- **改善方向性**: 統合（図4-2 と統合し、Phase A→B の時間軸の中で 5 系統の重み変化を sankey または stack chart で描く）

### 図4-2（line 631、Phase B マイルストーン時系列）
- **位置**: Ch4 Phase B 後半
- **意図**: 2030-2040 の6マイルストーン（Soft Robotics-RL／Lifelong VLA／VLA非構造50%／Neuromorphic Edge／核融合／侵襲BMI）を時系列ガント
- **問題点**: 時間目盛りが 2030/2032/2035/2040 と不等間隔で誤読を招く／6マイルストーンが時系列上で過密集中（2032-2035 に偏在）／2 つの円が同じ x=500 に重なり重複描画
- **改善方向性**: 再設計（時間軸を線形等間隔に、マイルストーン位置を散らす、各マイルストーンに stream タグを色分けで付与）

### 図5-1（line 728、Cognitive Stack 4層）
- **位置**: Ch5 Phase C 中盤
- **意図**: VLA／World Model／Active Inference／記号推論の 4 層アーキテクチャ
- **問題点**: 単なる4層ボックスで他の図と差別化なし／各層の入出力データが明示されない／物理身体層との接続が点線一本
- **改善方向性**: 拡張（各層に代表モデル名＋データフロー矢印＋出力次元数を追記。AlphaFold/Friston Active Inference/Hafner DreamerV5/LLM successor のロゴ的表示）

### 図5-2（line 776、人間-AI 分業構造）
- **位置**: Ch5 Phase D 直前
- **意図**: Phase C と Phase D での人間／混成チーム／AI の3領域配分の質的変化
- **問題点**: 6 つの矩形が並ぶだけで遷移の含意が薄い／矢印 3 本が水平で「縮小・深化」の意味が不在／面積比較で量的変化が表現されない
- **改善方向性**: 再設計（左→右で領域面積を変化させる sankey 図、または三角形分割で人間-混成-AI の境界が動的に動く図）

### 図6-1（line 866、Phase E-G 三境界溶解）
- **位置**: Ch6 Phase E 中盤
- **意図**: 機械/生命・主体/環境・個体/群 の 3 境界溶解過程を 2060-2100 時系列で
- **問題点**: 3 本の横帯に文字列が並ぶだけで「溶解」の漸進性が表現されない／時間軸の 2060/2075/2090/2100 と帯の対応が不明確／最終到達点（2100）が下部の注記のみ
- **改善方向性**: 再設計（3 本の帯を「実線→点線→消失」で溶解を視覚化、各帯の中で 4-6 個のマイルストーン点を時系列に配置、最終到達点を右端に赤いハッチ領域として描く）

### 図6-2（line 929、知性のオーケストラ）
- **位置**: Ch6 Phase G 直後
- **意図**: 中央「関係論的物理生態系」を囲む 6 主体（人間／古典AI／生体AI／量子AI／分散AI／身体性AI）の協調
- **問題点**: 6 円が放射状に並ぶだけで AI 種別の関係が「全部繋がっている」以上の構造を示さない／中心円のラベルが装飾的／重み・主導権交替のダイナミクスが不在
- **改善方向性**: 拡張（円の大きさ＝知性の規模、線の太さ＝接続強度、矢印＝主導権交替の頻度。Active Inference のフィードバック構造を中心に追加）

### 図7-1（line 1062、三領域動詞組み換え軌道）
- **位置**: Ch7 三領域転換軸
- **意図**: 製造／医療／農業の動詞変遷を 2030-2100 で並列
- **問題点**: 3 本の水平点線に 4 ノードが並ぶだけで「同期性」が量化されない／動詞が日本語短文のみで概念差が不明／各時点での実装事例が不在
- **改善方向性**: 拡張（各ノードに実装事例（OpenVLA / AlphaFold / John Deere 等）を吹き出しで追加、3 本の線を相互参照で結ぶ縦線を追加して同期周波数を可視化）

### 図7-2（line 1116、規制成熟度マトリクス）
- **位置**: Ch7 規制成熟度直前
- **意図**: 4 領域（製造/医療/農業/都市）× 3 地域（米/中/EU）の規制濃淡
- **問題点**: 12 セルの色濃淡が 0.45/0.55/0.65/0.85/0.95 と細かすぎ識別困難／凡例なし／右端「統合度」列の高/中/低の判定根拠不明
- **改善方向性**: 再設計（5 段階濃淡を 3 段階に簡略化、凡例を追加、規制名（EU AI Act / FDA SaMD / NMPA / CAP 等）の出典年を併記）

### 図8-1（line 1225、人類圏輪郭組み換え）
- **位置**: Ch8 三領域転換軸
- **意図**: 人類圏を中心とする同心円で都市／教育／宇宙の段階的拡張
- **問題点**: 同心円 3 つに各時点が割当てられているが、時間軸との対応が不明（2030/2050/2070/2100 が混在）／各リングのラベル文字が円周上に散在し読みにくい／中心の「人類2026」と外側の「2100月10万人」の時間スケール感が一目で掴めない
- **改善方向性**: 再設計（同心円を時系列レイヤーに変換、内側＝2026/外側＝2100 で時間軸を半径方向に取る、各リングに年代を明示）

### 図9-1（line 1368、80年5転換マトリクス）
- **位置**: Ch9 80年貫く5転換
- **意図**: 5軸（物理空間／協働範囲／労働意味／統治／個人輪郭）×4時点（2030/2050/2070/2100）のマトリクス
- **問題点**: 20 セル全てがテキストのみで視覚情報量ゼロ／2100 列のみ赤文字だが他列も同様に強調すべき／各セル間の「駆動関係」（5軸が互いに影響）が不在
- **改善方向性**: 拡張（各セルに小型アイコン or 色濃淡で強度を追加、5軸間の駆動矢印を点線で追加、2030→2050→2070→2100 の各列にフェーズタグ A/C/E/G を上部に付与）

### 図14（line 1507、17能力＋4項目世代配置）
- **位置**: Ch10 末尾
- **意図**: 4世代（20-30代／40-50代／60-70代／80歳以上）× 各時代5/4/3/5能力 + フィジカルAI4項目
- **問題点**: 4 つの縦長矩形に箇条書きが並ぶだけで「世代間補完関係」が表現されない／フィジカルAI 追加4項目が赤文字でも構造的位置が同列／能力間の依存関係が不在
- **改善方向性**: 再設計（4 世代を時間軸に取り、各能力を線で世代間連結、追加4項目を縦軸の別レイヤーとして配置、AI-augmented Teal の組織形態を中央に視覚化）

### 図13（line 1619、5補論交差点）
- **位置**: Ch11 末尾
- **意図**: FVCP 5補論（製造v6/MOB/PHAI/HRORG/Talent）の関係性を 5 円配置
- **問題点**: 5 円が均等配置で本書 PHAI の位置が他補論と等価に見える／円同士の重なりがなく「交差点」が不在／各補論の動詞ラベルだけで内容差が伝わらない
- **改善方向性**: 拡張（5 円を Venn 図風に重ね合わせ、中央交差領域に「関係論的存在論」を配置、PHAI を中央寄りに大きく描画、補論間の引用関係を矢印で表現）

---

## 3. 品質ギャップ Top 20

教科書全体の品質を 4 観点（引用／一次ソース／日本人研究者／数値根拠／図解必要性）から横断的に評価し、優先度順に 20 件を抽出する。

| # | ギャップ | 該当箇所 | 重要度 | 補強方針 |
|---|---|---|---|---|
| 1 | **日本人研究者が議論の核を担う章が皆無**。加藤一郎（WABOT-1）/ Honda ASIMO / 川崎重工は登場するが、全て歴史的背景の脚注的引用。第6章（生命系製造）にも合成生物学日本人研究者（北野宏明・末次正幸・武部貴則）が不在 | Ch1-11 全般、特に Ch3 stream_bio、Ch6 Phase E、Ch7 医療・農業 | A | 北野宏明（SystemsX/Cyc）, 末次正幸（合成ゲノム/早稲田）, 武部貴則（オルガノイド/横浜市立大）, 池谷裕二（脳-機械境界/東大）, 高橋政代（iPS網膜/理研）, 戸田俊宏（Plant electrophysiology）等を本文の駆動軸として追加 |
| 2 | **架空ペルソナ14名が引用人物として登場、実在研究者と区別なく記述**。ヤン・デ・フリース／カミラ・サントス／アブドゥル・カマウ等は読者にとって実在と紛らわしい | Ch9 全般 | A | 各ペルソナに「（想像的構成）」マーク追加、または別タイポグラフィで区別 |
| 3 | **「2030年に〇〇に達する」型の予測に一次ソースなし**。Goldman Sachs 2024、McKinsey 2024、IFR World Robotics 2024 が頻出するが、レポート名・章節までの精度がない | Ch4 Phase A、Ch7 製造、Ch9 全般 | A | 「Goldman Sachs Robotics 2024, p.45」のように章節記載、または urlでの照合可能性を担保 |
| 4 | **MENA・ラテンアメリカ・サブサハラアフリカの研究者・実装事例が皆無**。引用人物リストは欧米・東アジア中心 | Ch1-11 全般 | A | デ・ラ・カデナ（ペルー）, Mamdani（ウガンダ-米）, Latour 系（仏）は名のみ登場。本文で論を駆動させる事例として組み込む |
| 5 | **CTI v2 数値（0.764 vs 0.768、1.005倍）の算出根拠が本文に未記載**。図1-1 でも数値のみ。式・データソースが不在 | Ch1 line 205-269 | A | CTI v2 算出式の補論を別 box で追加。Smil/Morris/Gordon/Perez を加算するときの係数を明示 |
| 6 | **AGI 到達予測（Hassabis 2024発言、Metaculus median、Khosla 2030）の出典が「中央値」止まり**。Metaculus の question ID、Hassabis の具体発言場所が不在 | Ch4 line 565 | A | Metaculus Q ID（例: #3479）、Hassabis 発言 source（Time Magazine 2024-09-19 等）の脚注追加 |
| 7 | **核融合「SPARC 2026-2027 稼働予定」「Helion 2028年 50MW PPA」が一次ソース未表記** | Ch3 line 445、Ch5 line 726 | B | Commonwealth Fusion Systems 公式リリース、Helion-Microsoft 契約 SEC filing 8-K の出典を脚注 |
| 8 | **9.4 2100年朝のシーンの「Bio-Hybrid Robot 同席触媒」が技術的に未根拠**。Active Inference の自由エネルギー最小化アルゴリズムで「会話のリズムを整える」実装事例が現状で存在しない | Ch9 line 1339 | B | 想像的構成であることを明示、または現存する社交支援ロボット（NAO/Furhat 系）の延長として位置づけ |
| 9 | **植物-AI 対話（Plant Foundation Model）の章で Mancuso & Viola 系の論争状況が記述されていない**。植物の感受性研究は哲学的論争中 | Ch7 line 1046、Ch10 line 1470 | B | Mancuso & Viola, Calvo, Trewavas の論争を 2-3 行で明示、技術応用と哲学的解釈を分離 |
| 10 | **データセンター電力推計（IEA 2024、460→1050TWh）の中央値・上限の幅が不明** | Ch3 line 445、Ch4 line 619 | B | IEA Electricity 2024 の中央値/楽観/悲観 3 シナリオを記載 |
| 11 | **AI Personhood Directive（仮称）が「EU議会で本格化（2055年想定）」と書かれているが完全に想像** | Ch5 line 833 | B | 想像であることを明示。現状の European Parliament 2017 Resolution on Civil Law Rules on Robotics（2015/2103(INL)）を実在ベースとして追記 |
| 12 | **介護分野の Cyberdyne HAL・Toyota HSR の臨床効果が定量的に未提示**。導入台数・効果サイズが空欄 | Ch7 line 1030、Ch9 line 1287 | B | Cyberdyne HAL の保険適用範囲・脳卒中リハ RCT 結果（Wall et al. 2015 等）の参照を追加 |
| 13 | **「製造業の雇用が先進国で 2024 年比 50-60% 減少」（Ch9 line 1312）の出典が McKinsey 2024 のみ**。Acemoglu & Restrepo 2020 の +0.18 雇用減少/ロボット1台 と整合性検証不在 | Ch9 line 1312 | B | 複数研究の幅（McKinsey/Acemoglu/Frey-Osborne）で 25-60% の幅として提示 |
| 14 | **第8章 教育の Davidesco 2021「脳活動同期が記憶定着を予測」が一次ソース短すぎ** | Ch8 line 1207 | C | Davidesco et al. (2021, Psychological Science) のフルciteを追加 |
| 15 | **15分都市（Carlos Moreno 2016）から関係論的都市への接続で「Bruno Latour, Mariana Mazzucato の系譜」を主張するが両者の都市論への直接寄与が薄い** | Ch8 line 1262 | C | Latour『Down to Earth』（2018, Polity）の地球論を経由した間接寄与として書き直し |
| 16 | **17能力モデルの era-talents DB 数値（平成5.42→令和8.79、+3.37）の DB クエリ条件が不在**。再現可能性に欠ける | Ch10 line 1434 | C | era-talents DB の era_id / capability_dimension の SQL クエリを補論として記載 |
| 17 | **Sinclair 系エピジェネティック・リプログラミング（Yang-Hayano-Sinclair 2023, Cell?）の論文情報が完全 cite なし** | Ch5 line 760、Ch7 line 1032 | C | Yang et al. 2023, Cell 186(2):305-326 の正確な citation |
| 18 | **「労働時間週20時間以下が標準」（Ch9 line 1347）の根拠が不在**。UBI 実装議論との接続が薄い | Ch9 line 1347 | C | Keynes 1930「Economic Possibilities for our Grandchildren」と現代の Aaron Bastani 等の参照 |
| 19 | **図解13点の主張（Ch11 line 1608）と実際 SVG 15 点の不整合**。文中で品質ゲートの数値が古い | Ch11 line 1608 | C | 「15 図解」に更新、または「13 主要図解＋2 補助」と区別 |
| 20 | **終章で「26データベース1,540万レコードの解析」と書かれているが AR-DB / PHAI-DB の総計と齟齬**（PHAI-DB は 1,879概念・146論文のみ） | line 1677 | C | 「PHAI-DB を基盤に AR-DB の関連 DB 群と接続」と表現を改める |

---

## 4. 新規図解候補 Top 10

既存 15 SVG が「折れ線・ボックス・マトリクス」中心で視覚的多様性に乏しいため、新しい型式の図解を 10 件提案する。

### 候補1: AR-DB 横断マップ（フィジカルAI関連 60+ DB の関係グラフ）
- **意図**: 本書が依拠する DB エコシステム（PHAI-DB / future-tech-trends / sangaku-rd / ftt-v2 / agi-development / cdh / signal-db / pestle-news / megatrend / cti-v2 等）を node-link で示す
- **配置候補**: 序章末 or Ch11 補論
- **型**: Force-directed graph（D3 風）
- **理由**: 本書が個別技術論ではなく DB エコシステムを基盤とすることを冒頭で示す

### 候補2: 8系統×Phase A-G ヒートマップ
- **意図**: 8 系統（hw/ctrl/rl/sim/fm/bio/mat/cog）× 7フェーズ（A-G）の進展度を 0-100 色濃淡で
- **配置候補**: Ch3 末尾 or Ch6 末尾
- **型**: 8×7 ヒートマップ matrix
- **理由**: 系統別の駆動タイミング差（mat は Phase E まで律速、fm は Phase A で先行）を一目で

### 候補3: 地政学三極ダイヤモンド（米・中・EU + 4 軸）
- **意図**: 米中欧の規制／投資／産業／人材 4 軸を三角ダイヤで比較。Ch4 線形地政学記述を多次元化
- **配置候補**: Ch4 line 695 直前
- **型**: Radar chart（4 軸×3 国）
- **理由**: 図7-2 規制マトリクスの抽象拡張版

### 候補4: エネルギー/データ/演算の三制約三角形
- **意図**: フィジカルAI の物理限界 3 軸（電力 / データ希少性 / 演算密度）を triangle balance で
- **配置候補**: Ch4 Phase A ボトルネック直後
- **型**: Ternary diagram（3 軸三角座標）
- **理由**: ボトルネック 4 層論（line 617）の構造を視覚化

### 候補5: VLM→VLA→GLA 進化系統樹
- **意図**: 2017 Transformer から 2024-2030 VLA、2050 GLA（Generalist Lifelong Agent）への系統樹
- **配置候補**: Ch2 第四系統直後
- **型**: 樹形図（cladogram 風）
- **理由**: 図2-1 を拡張、主要モデル（CLIP / PaLM-E / RT-2 / OpenVLA / π0 / GR00T / Helix / GLA予想）の系統を整理

### 候補6: 4時点×3地理（先進国/新興国/極限環境）の朝シーン地図
- **意図**: 9章 14 シーンを世界地図に投影、4時点の地理分布を可視化
- **配置候補**: Ch9 9.4.6 地理多様性直後
- **型**: World map（点プロット）
- **理由**: 地理多様性主張の実証可視化

### 候補7: フィジカルAI×SDG 17 ゴール影響マトリクス
- **意図**: 8 系統 × SDG 17 ゴールへの正負影響を 8×17 グリッドで
- **配置候補**: Ch11 補論 or 終章末
- **型**: Matrix grid（赤=促進/灰=中立/黒=阻害）
- **理由**: 社会的含意を SDG 経由で構造化

### 候補8: 17能力＋4項目 円環ネットワーク
- **意図**: 図14 を線形配置から円環ネットワークに変換し、能力間の依存関係を内側の弦で表現
- **配置候補**: Ch10 末尾（図14 置換 or 併置）
- **型**: Chord diagram
- **理由**: 「円環として連結する5能力」（line 1486）の主張を円環で実装

### 候補9: 5 補論 × 14 ペルソナ朝シーン × フェーズ A-G の 3D マッピング
- **意図**: 5 補論（製造v6/MOB/PHAI/HRORG/Talent）と 14 ペルソナと 7 フェーズの 3D 座標
- **配置候補**: Ch11 末尾 or 終章
- **型**: 3D scatter / Sankey 3-stage
- **理由**: FVCP 補論シリーズと本書の交差点を立体化

### 候補10: 物理操作能力の S 字曲線群（2026-2100）
- **意図**: ヒューマノイド普及率／VLA 汎化率／Bio-Hybrid 普及率／核融合容量 等を S 字曲線で重ね描き
- **配置候補**: Ch6 末尾 or 終章直前
- **型**: Multiple S-curves（Bass diffusion model 風）
- **理由**: 既存図解にない採用曲線型を追加、Phase A-G の量的根拠を可視化

---

## 5. 革新ポイント Top 7（既存教科書を「革新的に向上」させる施策）

既存教科書は内容的に充実しているが、以下 7 施策で「革新的」な質的飛躍を達成できる。

### 施策1: 日本人研究者を 8 系統それぞれの駆動軸として配置
- **概要**: 各 stream（hw/ctrl/rl/sim/fm/bio/mat/cog）に最低 1 名の日本人研究者を「論の核」として組み込む
- **候補**: stream_hw=加藤一郎（拡張）, stream_ctrl=有本卓（ロボット制御）, stream_rl=松尾豊・牛久祥孝（深層強化学習）, stream_sim=東京大学 IROS 系統, stream_fm=ELYZA 日本語 LLM, stream_bio=末次正幸（合成ゲノム）・武部貴則（オルガノイド）, stream_mat=細野秀雄（鉄系超伝導/全固体電池）, stream_cog=池谷裕二・苧阪直行（拡張認知/作業記憶）
- **効果**: 「日本人研究者議論の核を担う」基準達成、グローバル独自性

### 施策2: AR-DB 横断連動を冒頭・章末で明示し DB レコードへの直接リンクを設置
- **概要**: 序章で AR-DB エコシステム図、各章末に「本章を支える DB クエリ例」を SQLite として記載
- **効果**: 教科書を読書体験から実装可能なリソースへ昇格、再現可能性の確保

### 施策3: 4時点 14 ペルソナ朝シーンを「実在事例の 2026 年スナップショット＋未来想像」の二段組に再構成
- **概要**: 各ペルソナの 2026 年実装事例（実在企業・実装地名・実在組織）を本文中に並置
- **効果**: 想像と実証の境界を明示、ハルシネーション排除

### 施策4: 図解 15 → 25 へ拡張、視覚デザイン多様化（ヒートマップ／散布図／樹形図／世界地図／3D マッピング）
- **概要**: 上記候補1-10 を実装し、現状の「折れ線・ボックス・マトリクス」中心から「グラフ・地理・3D」へ拡張
- **効果**: 視覚的差別化、認知負荷の軽減

### 施策5: 8系統オーケストラ宣言を「動詞螺旋（verb spiral）」モデルとして再定式化
- **概要**: 製造v6補論で確立した動詞螺旋（統制→育てる→生命系→譜面）を本書全章で系統化、Ch3/Ch6/Ch7/Ch9/Ch10 を貫く共通フレーム
- **効果**: 本書の独自性を強化、FVCP 補論シリーズとの方法論的整合

### 施策6: Phase A-G の各フェーズに「signal of change」（早期兆候）を 3 件ずつ追加
- **概要**: 各 Phase の本文末尾に「2026 年現在観察できる Phase X の signal of change 3 件」を箱で挿入
- **効果**: 抽象的フェーズ論を 2026 年現在の観測可能事象に接続、読者の検証可能性を担保

### 施策7: 「譜面を書く者の作法」を読者参加型 7 ステップワークシートとして付録化
- **概要**: 終章「読者への 3 つの一歩」を拡張し、自組織のフェーズ判定→主役技術選定→参加者設計→基盤強化→評価軸設定の 7 ステップワークシートを別 HTML として
- **効果**: 教科書から実装支援ツールへの拡張、ミラツク事業（コンサル/FVCP）との接続点を明示

---

**監査隊総評**: 本書は既に「FVCP 補論シリーズの第 3 作」として量的・構造的充実度は A 基準に達するが、(a) 日本人研究者の駆動軸不在 / (b) ペルソナと実在の混同 / (c) 図解視覚的多様性の欠如 / (d) AR-DB 連動の明示不足 の 4 点が「革新性」を阻害している。上記施策 7 件を実装することで、journal-essay-style.md の 14 項目チェックリストにおける「日本人研究者≥2名・議論の核担当・top-tier journal 4 件以上」基準と、db-design-system.md の textbook 標準を同時に超え、「世界で唯一の Physical AI 2100 教科書」としての地位を確立できる。

---

**ファイル**: `/Users/nishimura+/projects/research/physical-ai-2100/enhancement/ardb/content_audit.md`
**作成日**: 2026-05-18
**監査主体**: 既存コンテンツ監査隊（AR-DB Wave 0）
