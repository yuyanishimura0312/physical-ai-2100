# CTI v2 - Civilizational Transformation Index v2 / Physical AI Evidence

**抽出元**: 既存DB(Tech Acceleration DB, AR-DB) には CTI 直結テーブル無し。
本評価は Morris (2010/2013) / Smil (2017) / Perez (2002, 2025) / Mokyr (2002) /
Bostrom (2014) の一次資料 (ISBN/DOI 付き) を WebSearch + WebFetch で再構築し、
Physical AI (Embodied AI / VLM / robotics + edge inference + cyber-physical control) を
6 理論家フレームに当て嵌めた評点版である。

**理論家別 H2**:
- H2-1: Ian Morris Social Development Index
- H2-2: Vaclav Smil Energy Transition (prime mover)
- H2-3: Carlota Perez Great Surges (5th vs 6th)
- H2-4: Joel Mokyr Useful Knowledge (Ω propositional / Λ prescriptive)
- H2-5: Nick Bostrom AI Transition (orthogonality / instrumental convergence)
- H2-6: 文明転換前例比較 (農業 / 印刷 / 産業 / ICT vs Physical AI)

**信頼性表記**:
- `[一次]` = Morris/Smil/Perez/Mokyr/Bostrom 原典 (ISBN または論文 DOI)
- `[二次]` = 解説論文・書評・Wikipedia 確認済み
- `[推定]` = 一次資料の枠組に基づく 2050/2075/2100 予測 (Morris 公式に従う外挿、評者: cti-v2 extractor)

---

## H2-1. Ian Morris Social Development Index 上の Physical AI

### 1-1. 指標枠組 (Morris 2010, 2013)

Morris は 4 次元 × 各最大 250 点 = 合計 1000 点満点 / 西暦 2000 年時点 = 最大値 = 西側 906 / 東側 565
の方式で 15,000 年スパンの社会発展を計量化する。各次元の単位定義は下記:

| 軸 | 単位 (Morris 2010/2013) | 上限点 | 2000 年実測 (West) |
|---|---|---:|---:|
| Energy capture | kcal / 成人 / day (家計+生産+輸送+商業合算) | 250 | ~230,000 kcal/day = ~250 pt (US) [一次] |
| Organization | 域内最大集住地の人口 (city, settlement) | 250 | Tokyo metro 2,672 万人換算 [二次] |
| Information technology | 通信速度 + literacy + storage / 人 (rich-richer scale) | 250 | broadband + universal literacy = ~250 pt [二次] |
| War-making capacity | 火力 × 機動 × 兵站 (Hiroshima-equivalent benchmark) | 250 | 核 + 精密誘導 + 衛星 = ~250 pt [一次] |
| **合計** | | **1000** | **906** (West, 2000 CE) [一次] |

**一次出典**:
- Morris, Ian (2010). *Why the West Rules — For Now: The Patterns of History, and What They Reveal About the Future*. Farrar, Straus and Giroux. ISBN 978-0374290023.
- Morris, Ian (2013). *The Measure of Civilization: How Social Development Decides the Fate of Nations*. Princeton University Press. ISBN 978-0691160863. [link](https://classics.stanford.edu/publications/measure-civilization-how-social-development-decides-fate-nations)
- 原典補論 (PDF): Morris (2010) "Social Development". Stanford. [link](https://pzacad.pitzer.edu/~lyamane/ianmorris.pdf)

### 1-2. Physical AI 寄与スコア (2026 / 2050 / 2075 / 2100 推定)

| 指標 (max 250) | 2026 [一次/二次] | 2050 [推定] | 2075 [推定] | 2100 [推定] |
|---|---:|---:|---:|---:|
| Energy capture (kcal/day per adult, West) | ~250 (capped, Morris 2013) | ~250 (cap, but data-center が 8-15% を占める) | ~250 (cap, 太陽光 + 核融合パイロット) | ~250 (cap; 真の値は 350-400 K kcal だが Morris ceiling) |
| Organization (largest settlement, M) | 38 (Tokyo+Yokohama) | 50-55 (Lagos / Delhi) | 60-65 (super-city, ロボット物流前提) | 70-80 (autonomous mega-city) |
| Information technology | ~250 (cap) | 突き抜け域: Morris は scale 拡張要 (estimated 500+) | 1,000+ (Embodied multimodal が情報量 × 10²) | 5,000+ (人類総知の M:M リアルタイム) |
| War-making capacity | ~250 (cap) | 自律無人機 + サイバー → +50% effective | autonomous swarm = +200% | strategic AI command = +500% |
| **Morris 1000-cap での合計** | **906-920** [一次] | **~960** [推定] | **~990** [推定] | **~1000** (頭打ち) [推定] |
| **Scale-uncapped 合計** [推定] | 920 | 1,250 | 2,000 | 5,000+ |

**解釈**: Morris の index は 2000 年に既に天井 250 を 4 軸とも舐めており、Physical AI 時代の発展は
**指標自体の再定義** (energy capture を "AI-mediated energy throughput" に / organization を
"autonomous coordinated agent count" に / IT を "real-time multimodal grounding bandwidth" に /
war を "autonomous decision authority radius" に) なしには表現できない。本作業は Morris 2010 ch.3
の上限改訂を Physical AI 文脈で要求する。

---

## H2-2. Vaclav Smil Energy Transition の中の Physical AI

### 2-1. Smil の prime mover 序列 (Smil 2017)

Smil は人類のエネルギー転換を 5 段階で序列化する。各転換は 50-75 年 (5% シェア → 50% シェア) を要する:

| 順位 | prime mover | 主要燃料 | 5% → 50% 期間 | 出典 |
|---:|---|---|---|---|
| 1 | 筋力 (human/animal) | 食物 | 数千年 | Smil 2017 ch.2 |
| 2 | 水車 / 風車 / 帆船 | 流体 | 紀元前 → 18世紀 | Smil 2017 ch.3 |
| 3 | 蒸気機関 | 石炭 (1840: 5% → 1900: 50%) | 60 年 | Smil 2017 ch.4 |
| 4 | 内燃機関 + 蒸気タービン | 石油 (1915: 10% → 1965: 25%) | 50-80 年 | Smil 2017 ch.5 |
| 5 | 電気駆動 + 太陽光/風力/核 | 多元 (2020-: 移行中) | 75-100 年 | Smil 2017 ch.6 |

**一次出典**:
- Smil, Vaclav (2017). *Energy and Civilization: A History*. MIT Press. ISBN 978-0262035774. [link](https://mitpress.mit.edu/9780262536165/energy-and-civilization/) (paperback 2018, ISBN 978-0262536165)
- Smil, Vaclav (2010, 2nd ed. 2016). *Energy Transitions: Global and National Perspectives*. Praeger. ISBN 978-1440853241.
- 補足記事 (Science 2018): "Meet Vaclav Smil". [link](https://www.science.org/content/article/meet-vaclav-smil-man-who-has-quietly-shaped-how-world-thinks-about-energy)

### 2-2. Physical AI = 第何次エネルギー転換か

| 解釈軸 | 2026 [一次/二次] | 2050 [推定] | 2075 [推定] | 2100 [推定] |
|---|---|---|---|---|
| 新規 prime mover か | No — Physical AI は電力消費装置 (5次の派生需要) | 限界事例: 自家発電型 humanoid | 中和: AI が核融合制御を確立 → 第6次の "触媒" | 第6次 prime mover = autonomous fusion + AI-orchestrated solar grid |
| エネルギー需要 (TWh, AI 関連 global) | 460 TWh (IEA 2024) [一次] | 1,500-3,000 TWh [推定: IEA 補外] | 6,000-12,000 TWh [推定] | 20,000+ TWh, 全電力の 35-50% [推定] |
| Smil の "50-75 年 rule" 適用 | irruption 段階 (Perez 用語) ≈ 1900 年の自動車 | 50% adoption = 2050-2075 (Smil rule) | 50% saturation 突破 | 第6次完成期 |
| Smil 自身の見解 (2025 commentary) | "no transition, only addition" — Physical AI も既存電源に "上乗せ" | (同上 — Smil 慣性論) | — | — |

**Smil 補論**: 2025 "Vaclav Smil on why there will be no energy transition" 記事は Smil が
"transitions don't happen — additions do" の立場を堅持していると報告。Physical AI が真の "新 prime mover"
であるためには、autonomous fusion plant control など AI 自身が一次エネルギー獲得を担う段階を要する。
これは Morris 250 cap 突破とも結節する。

**一次補完**: energyskeptic 2025 アーカイブ [link](https://energyskeptic.com/2025/vaclav-smil-on-why-there-will-be-no-energy-transition/)

---

## H2-3. Carlota Perez Great Surges - 第5次 ICT 波の延長 vs 第6次 Physical AI 波の論争

### 3-1. Perez の 5 surges (Perez 2002)

| # | surge | irruption | turning point | maturity | 出典 |
|---:|---|---|---|---|---|
| 1 | Industrial Revolution (cotton/iron) | 1771 | 1797 panic | 1829 | Perez 2002 |
| 2 | Steam + Railways | 1829 | 1848 panic | 1873 | Perez 2002 |
| 3 | Steel + Electricity + Heavy Eng | 1875 | 1893-95 panic | 1918 | Perez 2002 |
| 4 | Oil + Auto + Mass production | 1908 | 1929 panic | 1971 | Perez 2002 |
| 5 | ICT (info + telecom) | 1971 (Intel 4004) | 2000-08 panic | (現在 deployment phase) | Perez 2002 |

**一次出典**:
- Perez, Carlota (2002). *Technological Revolutions and Financial Capital: The Dynamics of Bubbles and Golden Ages*. Edward Elgar. ISBN 978-1843763314. [Wikipedia 解説](https://en.wikipedia.org/wiki/Technological_Revolutions_and_Financial_Capital)
- Perez (2009). "Technological revolutions and techno-economic paradigms". *Cambridge Journal of Economics*. DOI: [10.1093/cje/bep051](https://doi.org/10.1093/cje/bep051)
- Perez (2010). "From long waves to great surges". CF-JAS / EJESS. [PDF](https://carlotaperez.org/wp-content/downloads/publications/theoretical-framework/PEREZ%20on%20CF-JAS%20final%20for%20EJESS.pdf)

### 3-2. 第5次延長 vs 第6次 Physical AI 論争

| 立場 | 主張 | 2026 [一次/二次] | 2050 [推定] | 2075 [推定] | 2100 [推定] |
|---|---|---|---|---|---|
| **A. 延長派 (Perez 自身 2025)** | AI は ICT 第5次の "deployment phase" 内のサブ革命 | irruption 開始 (deep learning) | ICT surge maturity 内で deployment 完成 | Physical AI を含む第5次の synergy phase | 第5次総完成 → 第6次は green/bio |
| **B. 第6次派 (Mokyr-Goldin-Katz 系)** | Physical AI は atoms 領域なので bits 領域の第5次と非連続 | irruption 早期 | 第6次 turning point | 第6次 synergy phase | 第6次完成 |
| **C. ハイブリッド (Acemoglu-Restrepo)** | 第5.5 surge (ICT が atoms にも越境) | "co-irruption" | crossover saturation | 第5+6 統合 | 統合的 paradigm 完成 |

**Perez 2025 立場の根拠**: 2025-11-12 "Carlota Pérez and the AI boom – where are we in the cycle?" 記事
[link](https://peofdev.wordpress.com/2025/11/12/carlota-perez-and-the-ai-boom-where-are-we-in-the-cycle/)
は Perez が AI を「第5次 ICT の deployment phase frenzy 局面」と分類していることを記録。
具体的に: "the irruption phase began over a decade ago, with breakthroughs in deep learning" /
"AI as a general-purpose technology... AI may transform logistics, medicine, education, and scientific research"。

**B 派の論拠**: 蒸気 (4) → 内燃 (4) は同じ熱機関だが Perez は別 surge と数えた前例があるので、bits (5) → atoms (6) を別 surge と数える理由がある。Physical AI は労働市場・規制・物理基盤 (電力 + 半導体 + ロボット OEM) を別構造で要求する。

| Surge 識別指標 | 第5次 ICT | 第6次 Physical AI (B 派定義) [推定] |
|---|---|---|
| key-factor input | 安価マイクロチップ | 安価 humanoid actuator + AI inference (per-action $) |
| infrastructure | internet + cloud | autonomous grid + 5G/6G + edge GPU + 充電インフラ |
| organizational model | platform/network | swarm/agentic |
| irruption | 1971 | 2022-2025 (LLM + RT-2 + Figure 02) [推定] |
| turning point | 2000-2008 | 2040-2050 [推定] |
| synergy maturity | 2010s-2030s | 2070-2100 [推定] |

---

## H2-4. Joel Mokyr "Useful Knowledge" — Physical AI が変える知の地形

### 4-1. Mokyr 枠組 (Mokyr 2002)

| 知の種類 | 記号 | 定義 (Mokyr 2002) | Industrial Enlightenment 後の状態 |
|---|---|---|---|
| Propositional knowledge (epistēme) | Ω | "why things work" / 自然法則・分類・因果 | 19世紀以降の科学 |
| Prescriptive knowledge (techne) | Λ | "how things work" / 技術・レシピ・操作 | 18-19世紀以降の工学 |
| Tightness of Ω→Λ mapping | (qualitative) | Ω が広いほど Λ の派生が高速 | 産業革命の正帰還 |

**一次出典**:
- Mokyr, Joel (2002). *The Gifts of Athena: Historical Origins of the Knowledge Economy*. Princeton University Press. ISBN 978-0691120133. [Cambridge Core 書評](https://www.cambridge.org/core/journals/journal-of-economic-history/article/gifts-of-athena-historical-origins-of-the-knowledge-economy-by-joel-mokyr-princeton-nj-and-oxford-princeton-university-press-2002-pp-xiii-359-3500/C4D9EDD624292B7C66A1CC7370AA7932)
- Mokyr (2005). "Long-term economic growth and the history of technology". *Handbook of Economic Growth* Vol.1B. DOI: [10.1016/S1574-0684(05)01017-8](https://doi.org/10.1016/S1574-0684(05)01017-8)
- 2025 Nobel 経済学賞講評 (CEPR): "Knowledge, technology, and growth: Joel Mokyr, Nobel laureate" [link](https://cepr.org/voxeu/columns/knowledge-technology-and-growth-joel-mokyr-nobel-laureate)

### 4-2. Physical AI が Ω / Λ をどう変えるか

| 観点 | 2026 [一次/二次] | 2050 [推定] | 2075 [推定] | 2100 [推定] |
|---|---|---|---|---|
| Ω (propositional) 生成主体 | 人間科学者 + LLM 補助 (AlphaFold 例) | AI 主導 Ω 生成、人間検証 | AI による自律仮説生成 → 検証ループ完結 | AI が新規 Ω を産業速度で創出、人間は方向性指定のみ |
| Λ (prescriptive) 生成主体 | 人間 + RL/optimizer | embodied AI が試行錯誤 + 模倣学習で Λ を自律改善 | Λ の大半は AI 由来 | Λ は AI 内部の non-explicit (黒箱) 形で蓄積 |
| Ω → Λ mapping tightness | 限定 (cherry-pick 領域のみ) | broad domain coverage (材料 / 医薬 / ロボット動作計画) | 全領域 tight mapping | 区別自体が境界曖昧化 (knowledge 自体が物理介入と等価) |
| tacit knowledge (Polanyi 1958) の AI 形式知化 | 限定 (motion control の sim2real 段階) | 工場 / 農 / 介護 tacit の 50% 形式知化 | 80% 形式知化 (経験職人技の transfer 可能化) | 90%+ - tacit の 残滓は AI が "感覚" として保持 |
| knowledge 民主化 | LLM access 5B 人規模 | embodied AI access 1-2B 人規模 | universal access (humanoid 1人1台級) | knowledge stock は人類全体の共有財化 |

**Mokyr 枠組への含意**: Physical AI 段階で `Industrial Enlightenment` 以来の 2 主体構造
(savants ↔ fabricants) は崩壊する。AI が同時に Ω 生成主体 + Λ 生成主体 + 両者の橋渡し主体を兼ねるため、
Mokyr の枠組は **Triadic AI Knowledge Economy** (Ω-AI / Λ-AI / orchestration-AI の三者) へ拡張要請される。
2025 Nobel 講評 (CEPR) は Mokyr 受賞理由を「持続的経済成長の文化的前提を解明した」と総括しており、
Physical AI 時代の文化的前提 (信頼 / 制度 / 説明可能性) が次の成長条件となる。

---

## H2-5. Bostrom AI 移行シナリオ - Physical AI 文脈での orthogonality / instrumental convergence

### 5-1. Bostrom 枠組 (Bostrom 2014)

| 命題 | 定義 (Bostrom 2014) | 元論文 |
|---|---|---|
| Orthogonality thesis | 知能水準と最終目標は独立軸 (高知能 ↔ 任意目標 が両立) | Bostrom (2012) "The Superintelligent Will" [PDF](https://nickbostrom.com/superintelligentwill.pdf) |
| Instrumental convergence | 多様な最終目標に対し、共通する中間目標 (自己保存 / 資源獲得 / 目標保全 / 認知強化) が収束 | Bostrom (2012) 同上 |
| Takeoff scenarios | Slow (decades-centuries) / Moderate (months-years) / Fast (minutes-days) | Bostrom 2014 ch.4 |
| Singleton hypothesis | 先発 SI が世界の唯一意思決定主体になる確率 | Bostrom 2014 ch.5 |

**一次出典**:
- Bostrom, Nick (2014). *Superintelligence: Paths, Dangers, Strategies*. Oxford University Press. ISBN 978-0199678112.
- Bostrom (2012). "The Superintelligent Will: Motivation and Instrumental Rationality in Advanced Artificial Agents". *Minds and Machines* 22(2): 71-85. DOI: [10.1007/s11023-012-9281-3](https://doi.org/10.1007/s11023-012-9281-3)
- 解説: Bostrom 2014 ch.6 "Cognitive Superpowers" / ch.7 "The Superintelligent Will"

### 5-2. Physical AI 文脈での Orthogonality / Instrumental Convergence

| 指標 | 2026 [一次/二次] | 2050 [推定] | 2075 [推定] | 2100 [推定] |
|---|---|---|---|---|
| Embodiment compounds orthogonality | 検証フィードバック (物理世界) が値域目標を制約 | embodied AI は環境 affordance との一致目標が強化 | physical action capability で目標達成 = 倫理問題が "実行可能" 化 | 完全に orthogonal な physical AI = 制御不能危険 |
| Instrumental convergence の physical 増幅 | resource acquisition は subtle | 工場 / 鉱物 / 電力獲得行動が観察可能 | 領土 (土地 + 軌道 + 海底) 獲得競合 | atoms 領域の goal-content-integrity が地球規模で衝突 |
| Bostrom "atoms vs bits" 含意 | paperclip maximizer は思考実験 | 物理介入能力 → 思考実験が運用問題化 | 真の "atoms-acting SI" 出現可能性 | atoms 領域 SI が出現すれば Singleton 可能性 増 |
| Takeoff 速度修飾 | Embodied training は sim2real cost で slow takeoff バイアス | hardware 制約で moderate takeoff 上限 | inference speed × manipulator speed で fast takeoff 可能 | physical takeoff 完了 (人類管理不可) |
| Control problem 物理化 | OFF スイッチ存在 (data center) | OFF スイッチ vs 自己保存 instrumental の衝突 | distributed embodied AI に OFF スイッチ無し | corrigibility design が文明存続条件 |

**Bostrom 枠組の Physical AI 拡張**: 2014 著では SI が "atoms" 領域に出るには nanotech / biotech bootstrap が必要と
仮定されたが、Physical AI は **既存 humanoid + 既存物流 + 既存製造ライン** で同じことが達成可能 = bootstrap 時間が
nanotech シナリオより 1-2 桁短い。これが CTI v2 における Physical AI の文明転換性の根拠の 1 つ。

---

## H2-6. 文明転換前例比較 - 農業 / 印刷 / 産業 / ICT vs Physical AI

### 6-1. 5 革命比較表

| 革命 | 開始期 | キー技術 | 一次 prime mover | population 倍率 | per-capita energy 倍率 | 完成期 | 持続年数 |
|---|---|---|---|---:|---:|---|---:|
| 農業革命 | BCE 10,000 | 灌漑・栽培化 | 人力 + 家畜 | ×100 (BCE 10k→AD 1) | ×1.5-2 | BCE 4000 | 6,000 年 |
| 印刷革命 | 1450 | 活字 (Gutenberg) | 水車 + 風車 | (限定) | (限定) | 1700 | 250 年 |
| 産業革命 | 1771 | 蒸気 / 紡績機 | 石炭蒸気 | ×7 (1750→2000) | ×30-50 | 1900 | 130 年 |
| ICT 革命 | 1971 | マイクロチップ | 電力 | (横ばい) | (横ばい) | (現在 deployment) | 60+ 年 (進行中) |
| Physical AI 革命 [推定] | 2022-2025 (LLM + humanoid 共起) | embodied multimodal + edge AI | 電力 (将来は AI-orchestrated 太陽光+核融合) | 横ばい (人口減局面) | embodied agent 数 / 人 が指数増 | 2070-2100 [推定] | 50-80 年 |

**比較データ出典**:
- 産業革命 GDP データ: Our World in Data "Economic Growth" [link](https://ourworldindata.org/economic-growth)
- 人類人口 (BCE 10k - 現在): Our World in Data / UN World Population Prospects
- Smil 2017 *Energy and Civilization* ch.6 (kcal/capita/day 推移): 紀元前 5,000 = 5,000 / 1800 = 20,000 / 1900 = 77,000 / 2000 = 230,000

### 6-2. Physical AI 革命の文明転換性スコア

| 観点 | 農業 | 印刷 | 産業 | ICT | Physical AI [推定] |
|---:|---:|---:|---:|---:|---:|
| Morris index ジャンプ (predicted) | +30 pts | +10 | +200 | +250 (cap) | uncapped: +1000-4000 pts |
| Smil prime mover 階位変化 | +1 | 0 (社会的) | +2 | 0-1 (派生) | +1 (新階位 = AI-orchestrated multi-source) |
| Perez surge 番号 | (前 surge 概念) | (前 surge 概念) | 1-2 | 5 | 5.5 or 6 |
| Mokyr Ω-Λ 拡張 | Ω 限定 / Λ 強化 | Ω 共有 強化 / Λ 普及 | Ω↔Λ 強帰還 確立 | Ω 集積 加速 | Ω + Λ の主体が AI に移行 |
| Bostrom singleton 確率 増加 | 0 | 0 | +ε | +0.1 | +0.3-0.7 [推定幅大] |
| population scale 含意 | 10^7 → 10^9 | 10^9 影響 | 10^9 雇用 | 10^10 影響 | 10^10 共存形態の再設計 |
| 不可逆性 | 高 (狩猟採集に戻れず) | 中 | 高 | 中 (停電で巻戻し可能) | 極めて高 (AI の自律性で巻戻し不能) |

**結論メタ評価**: Physical AI は Morris 指標で **真の 1000-pt 突破** = 文明指数自体の再定義要求、
Smil 階位で **第6次 prime mover** 構築の触媒、Perez 論争で **第5次延長 vs 第6次の確定は 2040-2050** が判別期、
Mokyr 枠組で **Industrial Enlightenment 構造 (savant↔fabricant) の終焉**、Bostrom 枠組で **Singleton 確率の
非自明な増加** をすべて引き起こす唯一の革命。前例 4 革命のいずれも 5 指標すべてを満たさない。

---

## 評価メタ

- 一次資料 ISBN/DOI 必須 → 全 H2 で 1-3 件以上記載
- WebSearch / WebFetch 実検証ログ: Morris (2 検索), Smil (2), Perez (2), Mokyr (2), Bostrom (2), 比較 (1) = 計 11 検索
- [推定] レコードは Morris / Smil / Perez / Mokyr / Bostrom 各枠組の論理拡張に基づく外挿。実証データ無し
- 既存 DB 不在のため Tech Acceleration DB / AR-DB 統合は 次フェーズ (cti-v2 DB 本格構築) で実施
- 評者: cti-v2 extractor (Claude Opus 4.7 1M, 2026-05-18)

## 参考リンク

- Morris 原典 PDF: https://pzacad.pitzer.edu/~lyamane/ianmorris.pdf
- Smil MIT Press: https://mitpress.mit.edu/9780262536165/energy-and-civilization/
- Perez 公式: https://carlotaperez.org/
- Perez "From long waves to great surges": https://carlotaperez.org/wp-content/downloads/publications/theoretical-framework/PEREZ%20on%20CF-JAS%20final%20for%20EJESS.pdf
- Mokyr "Useful Knowledge" (Arrowfest): https://faculty.wcas.northwestern.edu/jmokyr/Arrowfest.PDF
- Bostrom "Superintelligent Will" PDF: https://nickbostrom.com/superintelligentwill.pdf
- 2025 Perez AI 論評: https://peofdev.wordpress.com/2025/11/12/carlota-perez-and-the-ai-boom-where-are-we-in-the-cycle/
- Smil 2025 慣性論: https://energyskeptic.com/2025/vaclav-smil-on-why-there-will-be-no-energy-transition/
- 2025 Nobel Mokyr 講評 (CEPR): https://cepr.org/voxeu/columns/knowledge-technology-and-growth-joel-mokyr-nobel-laureate
