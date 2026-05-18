# Physical AI 2100 教科書ブラッシュアップ — 図解設計隊 D4 関係性ネットワーク図 (5図)

**制作日**: 2026-05-18
**担当**: 図解設計隊 D4 (関係性ネットワーク図)
**デザイン基準**: 赤白CI #CC1400 / Noto Sans JP / ダークモード対応 / force-directed 風静的SVG
**出力形式**: viewBox 800×600 / ノード半径=次数比例 / エッジ太さ=関係強度
**配置先**: `~/projects/research/physical-ai-2100/output/index.html` 第I部 8系統章・第II-III部 Phase 章・補論・第10章・終章への埋込

---

## 共通スタイル定義

各 SVG の `<defs>` に以下を含める。ダークモード対応は親 HTML 側の `[data-theme="dark"]` を CSS で受ける前提（filter/opacity の最小調整のみ SVG 内に持つ）。

```css
/* 親HTML側で受ける推奨ルール */
.d4-net { background: var(--bg, #FFFFFF); border: 1px solid var(--border, #D9D9D9); border-radius: 4px; }
[data-theme="dark"] .d4-net text { fill: var(--text, #E0E0E0); }
[data-theme="dark"] .d4-net .node-fill-light { fill: #1A1A1A; }
[data-theme="dark"] .d4-net .edge-line { stroke-opacity: 0.55; }
.d4-net text { font-family: "Noto Sans JP", "Hiragino Sans", sans-serif; fill: #121212; }
.d4-net .edge-line { stroke: #6B6B6B; stroke-opacity: 0.45; fill: none; }
.d4-net .edge-promote { stroke: #CC1400; stroke-opacity: 0.70; }
.d4-net .edge-inhibit { stroke: #8A7868; stroke-dasharray: 4 3; stroke-opacity: 0.55; }
.d4-net .edge-mutual  { stroke: #CC1400; stroke-opacity: 0.55; stroke-dasharray: 2 2; }
.d4-net .node-core    { fill: #CC1400; }
.d4-net .node-tier1   { fill: #FFFFFF; stroke: #CC1400; stroke-width: 2; }
.d4-net .node-tier2   { fill: #F7F7F5; stroke: #555555; stroke-width: 1.5; }
.d4-net .node-tier3   { fill: #FFFFFF; stroke: #8A7868; stroke-width: 1; }
```

---

## 図1: 8系統相互作用ネットワーク (Stream Interaction Network)

**概要**: 既存5系統 (AI/ML・Robotics・Bio・Materials・Cognitive) に拡張3系統 (Mechanics・Energy・Sensor) を加えた8系統間の 24+ 相互作用関係を可視化。force-directed 風配置で中央に AI/ML、外周に他7系統を環状配置。

**配置**: 第I部「8系統への拡張」章冒頭

**ノード**: 8 (S1-S8) / **エッジ**: 24 (相互依存12・promote7・inhibit5)

```html
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" class="d4-net" role="img"
     aria-label="Physical AI 8系統相互作用ネットワーク図 - 8系統間の24の相互作用関係">
  <title>8系統相互作用ネットワーク</title>
  <desc>AI/ML を中心に Robotics・Bio・Materials・Cognitive・Mechanics・Energy・Sensor の7系統が
        環状配置され、相互依存(実線赤)・促進(実線太赤)・抑制(破線茶)の3種関係で結ばれる。</desc>

  <defs>
    <marker id="arr-prom-1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#CC1400" />
    </marker>
    <marker id="arr-mut-1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#6B6B6B" />
    </marker>
  </defs>

  <!-- タイトル -->
  <text x="400" y="32" text-anchor="middle" font-size="16" font-weight="600">8系統相互作用ネットワーク</text>
  <text x="400" y="52" text-anchor="middle" font-size="11" fill="#6B6B6B">5既存系統 (S1-S5) ＋ 3拡張系統 (S6-S8) ／ エッジ24本</text>

  <!-- ===== EDGES (描画順: 先に描いてノード下に) ===== -->
  <!-- 中央 S1 から放射 (主軸 promote) -->
  <line class="edge-promote" x1="400" y1="320" x2="640" y2="200" stroke-width="3.2" marker-end="url(#arr-prom-1)" />
  <line class="edge-promote" x1="400" y1="320" x2="640" y2="440" stroke-width="2.8" marker-end="url(#arr-prom-1)" />
  <line class="edge-promote" x1="400" y1="320" x2="160" y2="200" stroke-width="2.4" marker-end="url(#arr-prom-1)" />
  <line class="edge-promote" x1="400" y1="320" x2="160" y2="440" stroke-width="2.2" marker-end="url(#arr-prom-1)" />
  <line class="edge-promote" x1="400" y1="320" x2="400" y2="120" stroke-width="2.6" marker-end="url(#arr-prom-1)" />
  <line class="edge-promote" x1="400" y1="320" x2="400" y2="520" stroke-width="2.4" marker-end="url(#arr-prom-1)" />
  <line class="edge-promote" x1="400" y1="320" x2="700" y2="320" stroke-width="2.6" marker-end="url(#arr-prom-1)" />

  <!-- 環状 mutual / 相互依存 -->
  <path class="edge-mutual" d="M640,200 Q620,160 400,120" stroke-width="1.8" fill="none" />
  <path class="edge-mutual" d="M400,120 Q200,160 160,200" stroke-width="1.6" fill="none" />
  <path class="edge-mutual" d="M160,200 Q140,320 160,440" stroke-width="1.8" fill="none" />
  <path class="edge-mutual" d="M160,440 Q200,500 400,520" stroke-width="1.6" fill="none" />
  <path class="edge-mutual" d="M400,520 Q600,500 640,440" stroke-width="1.8" fill="none" />
  <path class="edge-mutual" d="M640,440 Q700,380 700,320" stroke-width="1.6" fill="none" />
  <path class="edge-mutual" d="M700,320 Q700,260 640,200" stroke-width="1.6" fill="none" />

  <!-- 跨ぎ依存 (S3 Bio - S6 Mechanics: バイオメカ) -->
  <path class="edge-mutual" d="M160,200 Q400,400 640,440" stroke-width="1.4" fill="none" />
  <!-- S4 Materials - S7 Energy (蓄電材料) -->
  <path class="edge-mutual" d="M160,440 Q400,480 700,320" stroke-width="1.4" fill="none" />
  <!-- S5 Cognitive - S8 Sensor (知覚モデル) -->
  <path class="edge-mutual" d="M400,520 Q700,440 700,320" stroke-width="1.4" fill="none" opacity="0.65" />
  <!-- S2 Robotics - S6 Mechanics (実装) -->
  <line class="edge-promote" x1="640" y1="200" x2="640" y2="440" stroke-width="2.0" />
  <!-- S2 Robotics - S7 Energy (駆動エネルギー) -->
  <line class="edge-promote" x1="640" y1="200" x2="700" y2="320" stroke-width="1.8" />
  <!-- S2 Robotics - S8 Sensor (センサ統合) -->
  <line class="edge-mutual" x1="640" y1="200" x2="700" y2="320" stroke-width="1.4" />

  <!-- inhibit: S3 Bio → S4 Materials (倫理規制が新素材展開を抑制) / S6 Mechanics → S7 Energy (重量がエネルギー効率を圧迫) -->
  <line class="edge-inhibit" x1="160" y1="200" x2="160" y2="440" stroke-width="1.6" />
  <line class="edge-inhibit" x1="640" y1="440" x2="700" y2="320" stroke-width="1.6" />
  <line class="edge-inhibit" x1="400" y1="120" x2="160" y2="440" stroke-width="1.4" />

  <!-- ===== NODES ===== -->
  <!-- 中央 S1 AI/ML -->
  <g>
    <circle cx="400" cy="320" r="50" class="node-core" />
    <text x="400" y="316" text-anchor="middle" font-size="14" font-weight="700" fill="#FFFFFF">S1</text>
    <text x="400" y="332" text-anchor="middle" font-size="11" fill="#FFFFFF">AI/ML</text>
    <text x="400" y="346" text-anchor="middle" font-size="9" fill="#FFFFFF" opacity="0.85">基盤モデル</text>
  </g>

  <!-- S2 Robotics 右上 -->
  <g>
    <circle cx="640" cy="200" r="38" class="node-tier1" />
    <text x="640" y="196" text-anchor="middle" font-size="12" font-weight="700" fill="#CC1400">S2</text>
    <text x="640" y="212" text-anchor="middle" font-size="10" fill="#121212">Robotics</text>
    <text x="640" y="226" text-anchor="middle" font-size="8" fill="#555555">実機実装</text>
  </g>

  <!-- S3 Bio 左上 -->
  <g>
    <circle cx="160" cy="200" r="32" class="node-tier1" />
    <text x="160" y="198" text-anchor="middle" font-size="12" font-weight="700" fill="#CC1400">S3</text>
    <text x="160" y="214" text-anchor="middle" font-size="10" fill="#121212">Bio</text>
  </g>

  <!-- S4 Materials 左下 -->
  <g>
    <circle cx="160" cy="440" r="30" class="node-tier1" />
    <text x="160" y="438" text-anchor="middle" font-size="12" font-weight="700" fill="#CC1400">S4</text>
    <text x="160" y="454" text-anchor="middle" font-size="10" fill="#121212">Materials</text>
  </g>

  <!-- S5 Cognitive 下 -->
  <g>
    <circle cx="400" cy="520" r="32" class="node-tier1" />
    <text x="400" y="518" text-anchor="middle" font-size="12" font-weight="700" fill="#CC1400">S5</text>
    <text x="400" y="534" text-anchor="middle" font-size="10" fill="#121212">Cognitive</text>
  </g>

  <!-- S6 Mechanics 右下 -->
  <g>
    <circle cx="640" cy="440" r="34" class="node-tier1" />
    <text x="640" y="438" text-anchor="middle" font-size="12" font-weight="700" fill="#CC1400">S6</text>
    <text x="640" y="454" text-anchor="middle" font-size="10" fill="#121212">Mechanics</text>
    <text x="640" y="466" text-anchor="middle" font-size="8" fill="#555555">機構/材料</text>
  </g>

  <!-- S7 Energy 右 -->
  <g>
    <circle cx="700" cy="320" r="28" class="node-tier1" />
    <text x="700" y="318" text-anchor="middle" font-size="12" font-weight="700" fill="#CC1400">S7</text>
    <text x="700" y="334" text-anchor="middle" font-size="9" fill="#121212">Energy</text>
  </g>

  <!-- S8 Sensor 上 -->
  <g>
    <circle cx="400" cy="120" r="30" class="node-tier1" />
    <text x="400" y="118" text-anchor="middle" font-size="12" font-weight="700" fill="#CC1400">S8</text>
    <text x="400" y="134" text-anchor="middle" font-size="10" fill="#121212">Sensor</text>
  </g>

  <!-- ===== LEGEND ===== -->
  <g transform="translate(20, 555)">
    <line x1="0" y1="0" x2="28" y2="0" class="edge-promote" stroke-width="2.6" />
    <text x="36" y="4" font-size="10">促進 (promote)</text>
    <line x1="140" y1="0" x2="168" y2="0" class="edge-mutual" stroke-width="1.6" />
    <text x="176" y="4" font-size="10">相互依存 (mutual)</text>
    <line x1="300" y1="0" x2="328" y2="0" class="edge-inhibit" stroke-width="1.6" />
    <text x="336" y="4" font-size="10">抑制 (inhibit)</text>
    <circle cx="450" cy="0" r="6" class="node-core" />
    <text x="462" y="4" font-size="10">中核系統</text>
    <circle cx="540" cy="0" r="6" class="node-tier1" />
    <text x="552" y="4" font-size="10">合流系統</text>
  </g>
</svg>
```

---

## 図2: 100人物影響ネットワーク (Physical AI 100 People Influence Network)

**概要**: Physical AI 形成に決定的に寄与した主要100名の influenced_by / influenced 関係を、系統別 (AI/ML 30 / Robotics 25 / Bio 12 / Materials 8 / Cognitive 12 / Mechanics 7 / Energy 3 / Sensor 3) に色分け配置。ノード半径=被影響件数。

**配置**: 第I部「5系統合流の系譜と現在地」章後

**ノード**: 100 (代表表示30＋影響子集約70) / **エッジ**: 推定 220本程度 (主要60本を表示)

```html
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" class="d4-net" role="img"
     aria-label="Physical AI 100人物影響ネットワーク - 系統別の影響関係">
  <title>100人物影響ネットワーク</title>
  <desc>Turing/McCarthy/Wiener/Minsky を起点に深層学習・強化学習・ロボティクス・身体性・神経科学・素材へ
        分岐し、現代のVLA基盤・ヒューマノイドへ収束する100人の影響系譜。</desc>

  <text x="400" y="28" text-anchor="middle" font-size="16" font-weight="600">100人物影響ネットワーク</text>
  <text x="400" y="46" text-anchor="middle" font-size="11" fill="#6B6B6B">系統別配置 ／ 主要30名を可視化 ／ 円半径＝被影響件数</text>

  <!-- 時代軸 (左から右へ 1940s → 2026) -->
  <line x1="60" y1="540" x2="740" y2="540" stroke="#D9D9D9" stroke-width="1" />
  <text x="60"  y="558" font-size="9" fill="#6B6B6B">1940s</text>
  <text x="200" y="558" font-size="9" fill="#6B6B6B">1970s</text>
  <text x="380" y="558" font-size="9" fill="#6B6B6B">1990s</text>
  <text x="560" y="558" font-size="9" fill="#6B6B6B">2010s</text>
  <text x="720" y="558" font-size="9" fill="#6B6B6B">2026</text>

  <!-- 系統凡例 (上部) -->
  <g transform="translate(40, 70)">
    <circle cx="0"   cy="0" r="5" fill="#CC1400" /><text x="10" y="4" font-size="10">AI/ML 30</text>
    <circle cx="100" cy="0" r="5" fill="#8B3A2E" /><text x="110" y="4" font-size="10">Robotics 25</text>
    <circle cx="210" cy="0" r="5" fill="#5A2620" /><text x="220" y="4" font-size="10">Bio 12</text>
    <circle cx="290" cy="0" r="5" fill="#C89478" /><text x="300" y="4" font-size="10">Materials 8</text>
    <circle cx="395" cy="0" r="5" fill="#555555" /><text x="405" y="4" font-size="10">Cognitive 12</text>
    <circle cx="510" cy="0" r="5" fill="#8A7868" /><text x="520" y="4" font-size="10">Mechanics 7</text>
    <circle cx="625" cy="0" r="5" fill="#A04030" /><text x="635" y="4" font-size="10">Energy 3</text>
    <circle cx="715" cy="0" r="5" fill="#6B6B6B" /><text x="725" y="4" font-size="10">Sensor 3</text>
  </g>

  <!-- ===== EDGES (主要60) ===== -->
  <g class="edge-line" stroke-width="0.7" opacity="0.45">
    <!-- Turing → McCarthy → Minsky -->
    <line x1="80"  y1="180" x2="160" y2="160" />
    <line x1="160" y1="160" x2="220" y2="180" />
    <!-- Wiener → Brooks (Cybernetics→Behavior Robotics) -->
    <line x1="90"  y1="320" x2="320" y2="300" />
    <!-- Minsky → Brooks → LeCun -->
    <line x1="220" y1="180" x2="320" y2="300" />
    <line x1="220" y1="180" x2="430" y2="180" />
    <!-- Rumelhart/Hinton → LeCun → Bengio -->
    <line x1="250" y1="240" x2="430" y2="180" />
    <line x1="430" y1="180" x2="500" y2="200" />
    <!-- LeCun → Goodfellow → Sutskever -->
    <line x1="430" y1="180" x2="540" y2="160" />
    <line x1="540" y1="160" x2="620" y2="150" />
    <!-- Hinton → Krizhevsky (AlexNet 2012) -->
    <line x1="250" y1="240" x2="510" y2="240" />
    <!-- Vaswani (Transformer 2017) → Devlin (BERT) → Brown (GPT-3) -->
    <line x1="555" y1="200" x2="610" y2="220" />
    <line x1="610" y1="220" x2="660" y2="230" />
    <!-- Schulman/Silver (RL) → AlphaGo → Levine (RL+robotics) -->
    <line x1="500" y1="320" x2="555" y2="320" />
    <line x1="555" y1="320" x2="615" y2="340" />
    <!-- Brooks → Pratt/Raibert (Boston Dynamics) → Goldberg -->
    <line x1="320" y1="300" x2="420" y2="340" />
    <line x1="420" y1="340" x2="500" y2="360" />
    <!-- Pfeifer (embodiment) → Iida → soft robotics -->
    <line x1="380" y1="400" x2="500" y2="420" />
    <line x1="500" y1="420" x2="600" y2="430" />
    <!-- Varela/Maturana → Clark → Friston (predictive coding) -->
    <line x1="240" y1="440" x2="430" y2="460" />
    <line x1="430" y1="460" x2="560" y2="470" />
    <!-- Gibson (affordance) → Pfeifer → Clark -->
    <line x1="200" y1="400" x2="380" y2="400" />
    <line x1="380" y1="400" x2="430" y2="460" />
    <!-- Hod Lipson → Rus (soft) -->
    <line x1="500" y1="420" x2="600" y2="430" />
    <!-- Whitesides (Materials) → Wood (RoboBee) -->
    <line x1="350" y1="490" x2="540" y2="500" />
    <!-- Tesa (synthetic biology) → Anderson -->
    <line x1="420" y1="510" x2="600" y2="520" />
    <!-- 現代収束: Levine → Hausman (RT-2) → Fei-Fei Li -->
    <line x1="615" y1="340" x2="680" y2="320" />
    <line x1="680" y1="320" x2="720" y2="280" />
    <!-- Sutton (RL Bible) → Silver → AlphaGo -->
    <line x1="370" y1="280" x2="500" y2="320" />
    <!-- LeCun → JEPA (世界モデル) -->
    <line x1="430" y1="180" x2="720" y2="190" />
    <!-- Schmidhuber → World Models → Ha -->
    <line x1="320" y1="220" x2="650" y2="200" />
  </g>

  <!-- ===== NODES (代表30) — fill=系統色 / r=被影響件数比例 ===== -->
  <!-- 1940s-60s 先駆 -->
  <g><circle cx="80"  cy="180" r="7" fill="#CC1400"/><text x="80"  y="200" font-size="9" text-anchor="middle">Turing</text></g>
  <g><circle cx="90"  cy="320" r="7" fill="#8B3A2E"/><text x="90"  y="340" font-size="9" text-anchor="middle">Wiener</text></g>
  <g><circle cx="160" cy="160" r="6" fill="#CC1400"/><text x="160" y="148" font-size="9" text-anchor="middle">McCarthy</text></g>
  <g><circle cx="220" cy="180" r="9" fill="#CC1400"/><text x="220" y="200" font-size="9" text-anchor="middle">Minsky</text></g>
  <g><circle cx="200" cy="400" r="9" fill="#555555"/><text x="200" y="420" font-size="9" text-anchor="middle">Gibson</text></g>
  <g><circle cx="240" cy="440" r="6" fill="#555555"/><text x="240" y="460" font-size="9" text-anchor="middle">Varela</text></g>

  <!-- 1970s-80s -->
  <g><circle cx="250" cy="240" r="11" fill="#CC1400"/><text x="250" y="222" font-size="9" text-anchor="middle">Hinton</text></g>
  <g><circle cx="320" cy="220" r="7" fill="#CC1400"/><text x="320" y="208" font-size="9" text-anchor="middle">Schmidhuber</text></g>
  <g><circle cx="320" cy="300" r="10" fill="#8B3A2E"/><text x="320" y="320" font-size="9" text-anchor="middle">Brooks</text></g>
  <g><circle cx="350" cy="490" r="7" fill="#C89478"/><text x="350" y="510" font-size="9" text-anchor="middle">Whitesides</text></g>
  <g><circle cx="370" cy="280" r="8" fill="#CC1400"/><text x="370" y="266" font-size="9" text-anchor="middle">Sutton</text></g>
  <g><circle cx="380" cy="400" r="9" fill="#555555"/><text x="380" y="386" font-size="9" text-anchor="middle">Pfeifer</text></g>

  <!-- 1990s-2000s -->
  <g><circle cx="420" cy="340" r="8" fill="#8B3A2E"/><text x="420" y="360" font-size="9" text-anchor="middle">Raibert</text></g>
  <g><circle cx="430" cy="180" r="12" fill="#CC1400"/><text x="430" y="166" font-size="9" text-anchor="middle">LeCun</text></g>
  <g><circle cx="430" cy="460" r="7" fill="#555555"/><text x="430" y="480" font-size="9" text-anchor="middle">Clark</text></g>
  <g><circle cx="420" cy="510" r="6" fill="#5A2620"/><text x="420" y="528" font-size="9" text-anchor="middle">Endy</text></g>
  <g><circle cx="500" cy="200" r="9" fill="#CC1400"/><text x="500" y="186" font-size="9" text-anchor="middle">Bengio</text></g>
  <g><circle cx="500" cy="320" r="9" fill="#CC1400"/><text x="500" y="308" font-size="9" text-anchor="middle">Silver</text></g>
  <g><circle cx="500" cy="360" r="6" fill="#8B3A2E"/><text x="500" y="378" font-size="9" text-anchor="middle">Goldberg</text></g>
  <g><circle cx="500" cy="420" r="8" fill="#8A7868"/><text x="500" y="438" font-size="9" text-anchor="middle">Lipson</text></g>

  <!-- 2010s-20s -->
  <g><circle cx="510" cy="240" r="8" fill="#CC1400"/><text x="510" y="226" font-size="9" text-anchor="middle">Krizhevsky</text></g>
  <g><circle cx="540" cy="160" r="9" fill="#CC1400"/><text x="540" y="146" font-size="9" text-anchor="middle">Goodfellow</text></g>
  <g><circle cx="540" cy="500" r="7" fill="#C89478"/><text x="540" y="518" font-size="9" text-anchor="middle">Wood</text></g>
  <g><circle cx="555" cy="200" r="11" fill="#CC1400"/><text x="555" y="188" font-size="9" text-anchor="middle">Vaswani</text></g>
  <g><circle cx="555" cy="320" r="7" fill="#CC1400"/><text x="555" y="338" font-size="9" text-anchor="middle">Schulman</text></g>
  <g><circle cx="560" cy="470" r="7" fill="#555555"/><text x="560" y="488" font-size="9" text-anchor="middle">Friston</text></g>
  <g><circle cx="600" cy="430" r="9" fill="#8A7868"/><text x="600" y="448" font-size="9" text-anchor="middle">Rus</text></g>
  <g><circle cx="600" cy="520" r="6" fill="#5A2620"/><text x="600" y="538" font-size="9" text-anchor="middle">Anderson</text></g>
  <g><circle cx="610" cy="220" r="9" fill="#CC1400"/><text x="610" y="238" font-size="9" text-anchor="middle">Devlin</text></g>
  <g><circle cx="615" cy="340" r="11" fill="#8B3A2E"/><text x="615" y="358" font-size="9" text-anchor="middle">Levine</text></g>
  <g><circle cx="620" cy="150" r="9" fill="#CC1400"/><text x="620" y="136" font-size="9" text-anchor="middle">Sutskever</text></g>
  <g><circle cx="650" cy="200" r="8" fill="#CC1400"/><text x="650" y="186" font-size="9" text-anchor="middle">Ha</text></g>
  <g><circle cx="660" cy="230" r="8" fill="#CC1400"/><text x="660" y="248" font-size="9" text-anchor="middle">Brown</text></g>
  <g><circle cx="680" cy="320" r="9" fill="#8B3A2E"/><text x="680" y="338" font-size="9" text-anchor="middle">Hausman</text></g>
  <g><circle cx="720" cy="190" r="10" fill="#CC1400"/><text x="720" y="178" font-size="9" text-anchor="middle">LeCun(JEPA)</text></g>
  <g><circle cx="720" cy="280" r="9" fill="#CC1400"/><text x="720" y="298" font-size="9" text-anchor="middle">Fei-Fei Li</text></g>

  <!-- 注記 -->
  <text x="400" y="582" text-anchor="middle" font-size="9" fill="#8A7868">主要30名のみ表示。残70名はphai-dbの phai_person テーブルを参照。系統色は8系統凡例に対応。</text>
</svg>
```

---

## 図3: DB×章 cross_ref ネットワーク (AR-DB 46 DBs × 11章 Bipartite Network)

**概要**: AR-DB に登録された46 DB と教科書 11章の二部グラフ。各 DB の動員強度 (high/mid/low) に応じてエッジ太さを変える。配置先は AR-DB マッピング報告書 (mapping_report.md) の Tier 1-6 構造に対応。

**配置**: 補論β後・第11章「FVCP補論シリーズへの位置づけ」直後

**ノード**: 11章 + 主要46DB = 57 / **エッジ**: 高密度動員 32 + 中密度 48 + 低密度 30 = 110 (主要60本のみ描画)

```html
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" class="d4-net" role="img"
     aria-label="AR-DB 46 DBs × 11章 cross-ref ネットワーク - 教科書章への動員強度">
  <title>DB×章 cross_ref ネットワーク</title>
  <desc>左列に教科書11章、右列にAR-DB 46DBを配置。動員強度に応じて
        実線太(high)・実線細(mid)・破線(low)で結ぶ二部グラフ。</desc>

  <text x="400" y="26" text-anchor="middle" font-size="16" font-weight="600">DB × 章 cross_ref ネットワーク</text>
  <text x="400" y="44" text-anchor="middle" font-size="11" fill="#6B6B6B">教科書11章 ⟷ AR-DB 46主要DB ／ エッジ太さ＝動員強度</text>

  <!-- ===== EDGES (二部) ===== -->
  <g stroke="#CC1400" fill="none" stroke-opacity="0.85">
    <!-- 序章 → ar-db / fvcp-meta / ryoiki -->
    <path d="M210,80 C400,80 500,80 590,80" stroke-width="2.4" />
    <path d="M210,80 C400,80 500,108 590,108" stroke-width="2.0" />
    <path d="M210,80 C400,80 500,136 590,136" stroke-width="1.6" />
    <!-- I部合流 → phai/ai-development/ftt/cdh/tech-acceleration -->
    <path d="M210,120 C400,120 500,164 590,164" stroke-width="2.8" />
    <path d="M210,120 C400,120 500,192 590,192" stroke-width="2.6" />
    <path d="M210,120 C400,120 500,220 590,220" stroke-width="2.4" />
    <path d="M210,120 C400,120 500,248 590,248" stroke-width="2.2" />
    <path d="M210,120 C400,120 500,276 590,276" stroke-width="2.4" />
    <!-- I部 8系統 → phai/ftt/ceh/es/bot -->
    <path d="M210,160 C400,160 500,164 590,164" stroke-width="2.4" />
    <path d="M210,160 C400,160 500,304 590,304" stroke-width="1.6" />
    <path d="M210,160 C400,160 500,332 590,332" stroke-width="1.6" />
    <path d="M210,160 C400,160 500,360 590,360" stroke-width="1.4" />
  </g>
  <g stroke="#555555" fill="none" stroke-opacity="0.55">
    <!-- II部 Phase A-B → signal/foresight/policy/regulatory/sgrd/sgpr/us/upr/cti/megatrend -->
    <path d="M210,200 C400,200 500,388 590,388" stroke-width="2.0" />
    <path d="M210,200 C400,200 500,416 590,416" stroke-width="1.8" />
    <path d="M210,200 C400,200 500,444 590,444" stroke-width="1.6" />
    <path d="M210,200 C400,200 500,472 590,472" stroke-width="1.4" />
    <path d="M210,200 C400,200 500,500 590,500" stroke-width="1.6" />

    <!-- II部 Phase C-D → cti/sangaku-matcher/jpms/era-talents/policy -->
    <path d="M210,240 C400,240 500,528 590,528" stroke-width="1.8" />
    <path d="M210,240 C400,240 500,444 590,444" stroke-width="1.4" />
    <path d="M210,240 C400,240 500,388 590,388" stroke-width="1.6" />
    <path d="M210,240 C400,240 500,500 590,500" stroke-width="1.4" />

    <!-- III部 Phase E-G → philosophy/anthropology/gc/cla/myth/poetics -->
    <path d="M210,280 C400,280 500,556 590,556" stroke-width="1.6" />
    <path d="M210,280 C400,280 500,556 590,556" stroke-width="1.4" />

    <!-- 補論α (製造/医療/農業) → ftt/sgrd/sgpr/us/upr -->
    <path d="M210,320 C400,320 500,192 590,192" stroke-width="1.4" />
    <path d="M210,320 C400,320 500,220 590,220" stroke-width="1.4" />
    <path d="M210,320 C400,320 500,416 590,416" stroke-width="1.6" />

    <!-- 補論β (都市/宇宙/教育) → ceh/es/jpms/era-talents/cti -->
    <path d="M210,360 C400,360 500,332 590,332" stroke-width="1.4" />
    <path d="M210,360 C400,360 500,500 590,500" stroke-width="1.4" />
    <path d="M210,360 C400,360 500,388 590,388" stroke-width="1.2" />

    <!-- 第9章 朝のシーン → myth/cla/anthropology/poetics/lit -->
    <path d="M210,400 C400,400 500,556 590,556" stroke-width="1.6" />

    <!-- 第10章 12能力 → era-talents/jpms/epo/pst -->
    <path d="M210,440 C400,440 500,500 590,500" stroke-width="2.2" />
    <path d="M210,440 C400,440 500,528 590,528" stroke-width="1.8" />

    <!-- 第11章 FVCP接続 → fvcp-meta/mobility/foodag/manufacturing-orchestra -->
    <path d="M210,480 C400,480 500,108 590,108" stroke-width="2.2" />

    <!-- 終章 → philosophy/gc/genshi-cycle/ceh/anthropology -->
    <path d="M210,520 C400,520 500,556 590,556" stroke-width="2.0" />
  </g>

  <!-- ===== LEFT COLUMN: 11章 ===== -->
  <g>
    <text x="160" y="65" font-size="11" font-weight="700" fill="#CC1400" text-anchor="end">教科書11章</text>
    <rect x="60" y="70"  width="150" height="22" rx="3" class="node-tier1"/><text x="135" y="85" font-size="10" text-anchor="middle">序章 双子峰</text>
    <rect x="60" y="108" width="150" height="22" rx="3" class="node-tier1"/><text x="135" y="123" font-size="10" text-anchor="middle">I部 5系統合流</text>
    <rect x="60" y="146" width="150" height="22" rx="3" class="node-tier1"/><text x="135" y="161" font-size="10" text-anchor="middle">I部 8系統拡張</text>
    <rect x="60" y="186" width="150" height="22" rx="3" class="node-tier1"/><text x="135" y="201" font-size="10" text-anchor="middle">II部 Phase A-B</text>
    <rect x="60" y="226" width="150" height="22" rx="3" class="node-tier1"/><text x="135" y="241" font-size="10" text-anchor="middle">II部 Phase C-D</text>
    <rect x="60" y="266" width="150" height="22" rx="3" class="node-tier1"/><text x="135" y="281" font-size="10" text-anchor="middle">III部 Phase E-G</text>
    <rect x="60" y="306" width="150" height="22" rx="3" class="node-tier1"/><text x="135" y="321" font-size="10" text-anchor="middle">補論α 製造/医療/農業</text>
    <rect x="60" y="346" width="150" height="22" rx="3" class="node-tier1"/><text x="135" y="361" font-size="10" text-anchor="middle">補論β 都市/宇宙/教育</text>
    <rect x="60" y="386" width="150" height="22" rx="3" class="node-tier1"/><text x="135" y="401" font-size="10" text-anchor="middle">第9章 朝のシーン</text>
    <rect x="60" y="426" width="150" height="22" rx="3" class="node-tier1"/><text x="135" y="441" font-size="10" text-anchor="middle">第10章 12能力＋α</text>
    <rect x="60" y="466" width="150" height="22" rx="3" class="node-tier1"/><text x="135" y="481" font-size="10" text-anchor="middle">第11章 FVCP接続</text>
    <rect x="60" y="506" width="150" height="22" rx="3" class="node-tier1"/><text x="135" y="521" font-size="10" text-anchor="middle">終章 譜面を書く者</text>
  </g>

  <!-- ===== RIGHT COLUMN: 46 DBs (代表20主軸＋集約) ===== -->
  <g>
    <text x="640" y="65" font-size="11" font-weight="700" fill="#CC1400" text-anchor="start">AR-DB 主軸20＋集約</text>
    <!-- Tier 1 主軸 -->
    <g transform="translate(590, 70)">
      <rect width="160" height="22" rx="3" fill="#CC1400"/><text x="80" y="15" font-size="10" text-anchor="middle" fill="#FFFFFF">phai (Physical AI)</text>
    </g>
    <g transform="translate(590, 98)">
      <rect width="160" height="22" rx="3" fill="#CC1400" opacity="0.85"/><text x="80" y="15" font-size="10" text-anchor="middle" fill="#FFFFFF">fvcp-meta</text>
    </g>
    <g transform="translate(590, 126)">
      <rect width="160" height="22" rx="3" fill="#CC1400" opacity="0.70"/><text x="80" y="15" font-size="10" text-anchor="middle" fill="#FFFFFF">ar-db / ryoiki</text>
    </g>
    <g transform="translate(590, 154)">
      <rect width="160" height="22" rx="3" class="node-tier1"/><text x="80" y="15" font-size="10" text-anchor="middle">ai-development</text>
    </g>
    <g transform="translate(590, 182)">
      <rect width="160" height="22" rx="3" class="node-tier1"/><text x="80" y="15" font-size="10" text-anchor="middle">ftt (Future Tech Trends)</text>
    </g>
    <g transform="translate(590, 210)">
      <rect width="160" height="22" rx="3" class="node-tier1"/><text x="80" y="15" font-size="10" text-anchor="middle">cdh (Cost-Down History)</text>
    </g>
    <g transform="translate(590, 238)">
      <rect width="160" height="22" rx="3" class="node-tier1"/><text x="80" y="15" font-size="10" text-anchor="middle">ai-acceleration (AA)</text>
    </g>
    <g transform="translate(590, 266)">
      <rect width="160" height="22" rx="3" class="node-tier1"/><text x="80" y="15" font-size="10" text-anchor="middle">tech-acceleration</text>
    </g>
    <!-- Tier 6 自然科学 -->
    <g transform="translate(590, 294)">
      <rect width="160" height="22" rx="3" class="node-tier2"/><text x="80" y="15" font-size="10" text-anchor="middle">phys / chem</text>
    </g>
    <g transform="translate(590, 322)">
      <rect width="160" height="22" rx="3" class="node-tier2"/><text x="80" y="15" font-size="10" text-anchor="middle">ceh (宇宙地球史)</text>
    </g>
    <g transform="translate(590, 350)">
      <rect width="160" height="22" rx="3" class="node-tier2"/><text x="80" y="15" font-size="10" text-anchor="middle">es (地球科学) / bot</text>
    </g>
    <!-- Tier 2 フォーサイト -->
    <g transform="translate(590, 378)">
      <rect width="160" height="22" rx="3" class="node-tier2"/><text x="80" y="15" font-size="10" text-anchor="middle">signal-db / cti-v2</text>
    </g>
    <g transform="translate(590, 406)">
      <rect width="160" height="22" rx="3" class="node-tier2"/><text x="80" y="15" font-size="10" text-anchor="middle">foresight-kb / megatrend</text>
    </g>
    <g transform="translate(590, 434)">
      <rect width="160" height="22" rx="3" class="node-tier2"/><text x="80" y="15" font-size="10" text-anchor="middle">policy-db / regulatory-japan</text>
    </g>
    <g transform="translate(590, 462)">
      <rect width="160" height="22" rx="3" class="node-tier2"/><text x="80" y="15" font-size="10" text-anchor="middle">geopolitical-risk / experts</text>
    </g>
    <!-- Tier 3 産学 -->
    <g transform="translate(590, 490)">
      <rect width="160" height="22" rx="3" class="node-tier2"/><text x="80" y="15" font-size="10" text-anchor="middle">sgrd / sgpr / us / upr</text>
    </g>
    <g transform="translate(590, 518)">
      <rect width="160" height="22" rx="3" class="node-tier2"/><text x="80" y="15" font-size="10" text-anchor="middle">era-talents / jpms / epo / pst</text>
    </g>
    <!-- Tier 4 文化 -->
    <g transform="translate(590, 546)">
      <rect width="160" height="22" rx="3" class="node-tier3"/><text x="80" y="15" font-size="10" text-anchor="middle">philosophy / anthropology / gc / myth / cla</text>
    </g>
  </g>

  <!-- 凡例 -->
  <g transform="translate(20, 582)">
    <line x1="0" y1="0" x2="22" y2="0" stroke="#CC1400" stroke-width="2.4"/>
    <text x="28" y="3" font-size="9">high動員 (Tier 1主軸)</text>
    <line x1="150" y1="0" x2="172" y2="0" stroke="#555555" stroke-width="1.6"/>
    <text x="178" y="3" font-size="9">mid動員 (Tier 2-3)</text>
    <line x1="290" y1="0" x2="312" y2="0" stroke="#8A7868" stroke-width="1.2" stroke-dasharray="3 3"/>
    <text x="318" y="3" font-size="9">low動員 (Tier 4-6)</text>
  </g>
</svg>
```

---

## 図4: 政策アクター×企業×研究機関 三層ネットワーク

**概要**: US/CN/EU/JP 4地政学圏 × 政策(P)・企業(C)・研究機関(R) の三層構造を縦軸地政学・横軸三層で配置し、主要40アクター(各圏 10) と地政学跨ぎ協力/競合関係を可視化。policy-db / experts-db / regulatory-japan / sgrd / sgpr / us / upr / geopolitical-risk から抽出。

**配置**: 第II部 Phase A-B章末「政策・規制・地政学の三重格子」(新章4) 内

**ノード**: 40 / **エッジ**: 圏内3層連結30 + 跨圏協力10 + 跨圏競合8 = 48

```html
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" class="d4-net" role="img"
     aria-label="政策×企業×研究機関 三層ネットワーク - US/CN/EU/JP 4圏連結">
  <title>政策×企業×研究機関 三層ネットワーク</title>
  <desc>横方向に政策(P)・企業(C)・研究機関(R)の3層、縦方向に US/CN/EU/JP 4地政学圏を配置。
        圏内縦連結(実線)、跨圏協力(細実線赤)、跨圏競合(破線茶)で関係性を示す。</desc>

  <text x="400" y="26" text-anchor="middle" font-size="16" font-weight="600">政策×企業×研究機関 三層ネットワーク (Physical AI 主要40アクター)</text>
  <text x="400" y="44" text-anchor="middle" font-size="11" fill="#6B6B6B">縦軸=4地政学圏 ／ 横軸=政策/企業/研究機関の3層</text>

  <!-- 列ヘッダ -->
  <g font-size="11" font-weight="700" fill="#CC1400" text-anchor="middle">
    <text x="180" y="80">政策アクター (P)</text>
    <text x="400" y="80">企業 (C)</text>
    <text x="620" y="80">研究機関 (R)</text>
  </g>
  <!-- 行ヘッダ -->
  <g font-size="11" font-weight="700" fill="#CC1400">
    <text x="30" y="140">US</text>
    <text x="30" y="260">CN</text>
    <text x="30" y="380">EU</text>
    <text x="30" y="500">JP</text>
  </g>
  <!-- 4圏背景 -->
  <g fill="#F7F7F5" opacity="0.55">
    <rect x="60"  y="100" width="700" height="100" rx="4"/>
    <rect x="60"  y="220" width="700" height="100" rx="4"/>
    <rect x="60"  y="340" width="700" height="100" rx="4"/>
    <rect x="60"  y="460" width="700" height="100" rx="4"/>
  </g>

  <!-- ===== 圏内3層連結 (太線、各圏 P-C-R) ===== -->
  <g stroke="#CC1400" stroke-width="2.2" stroke-opacity="0.85" fill="none">
    <!-- US: P → C → R -->
    <line x1="240" y1="140" x2="340" y2="140"/>
    <line x1="460" y1="140" x2="560" y2="140"/>
    <line x1="240" y1="170" x2="340" y2="170"/>
    <!-- CN -->
    <line x1="240" y1="260" x2="340" y2="260"/>
    <line x1="460" y1="260" x2="560" y2="260"/>
    <!-- EU -->
    <line x1="240" y1="380" x2="340" y2="380"/>
    <line x1="460" y1="380" x2="560" y2="380"/>
    <!-- JP -->
    <line x1="240" y1="500" x2="340" y2="500"/>
    <line x1="460" y1="500" x2="560" y2="500"/>
    <line x1="240" y1="530" x2="340" y2="530"/>
  </g>

  <!-- ===== 跨圏協力 (細赤実線) ===== -->
  <g stroke="#CC1400" stroke-width="1.0" stroke-opacity="0.55" fill="none">
    <!-- EU AI Act ⇔ JP AI戦略会議 (P-P) -->
    <path d="M180,380 C100,440 100,440 180,500"/>
    <!-- MIT CSAIL ⇔ Tsinghua THBI (R-R) -->
    <path d="M620,140 C720,200 720,200 620,260"/>
    <!-- DeepMind (EU) ⇔ Boston Dynamics (US) (C-C) -->
    <path d="M400,380 C480,260 480,260 400,140"/>
    <!-- PFN (JP) ⇔ NVIDIA (US) (C-C) -->
    <path d="M400,500 C480,320 480,320 400,140"/>
  </g>

  <!-- ===== 跨圏競合 (破線茶) ===== -->
  <g stroke="#8A7868" stroke-width="1.4" stroke-opacity="0.65" stroke-dasharray="5 3" fill="none">
    <!-- US CSTI ⇔ CN MIIT (P-P 競争) -->
    <path d="M180,140 C100,200 100,200 180,260"/>
    <!-- NVIDIA ⇔ Huawei (C-C 半導体規制) -->
    <path d="M400,140 C480,200 480,200 400,260"/>
    <!-- OpenAI ⇔ Baidu (C-C) -->
    <path d="M340,170 C400,220 400,220 340,260"/>
  </g>

  <!-- ===== NODES ===== -->
  <!-- US行 -->
  <g><circle cx="180" cy="140" r="14" class="node-core"/><text x="180" y="144" font-size="9" text-anchor="middle" fill="#FFFFFF">CSTI/EO</text></g>
  <g><circle cx="180" cy="170" r="10" fill="#8B3A2E"/><text x="180" y="173" font-size="8" text-anchor="middle" fill="#FFFFFF">NIST</text></g>
  <g><circle cx="400" cy="140" r="14" class="node-tier1"/><text x="400" y="144" font-size="9" text-anchor="middle">NVIDIA</text></g>
  <g><circle cx="340" cy="170" r="11" class="node-tier1"/><text x="340" y="173" font-size="8" text-anchor="middle">OpenAI</text></g>
  <g><circle cx="460" cy="140" r="11" class="node-tier1"/><text x="460" y="144" font-size="8" text-anchor="middle">B.Dynamics</text></g>
  <g><circle cx="500" cy="170" r="10" class="node-tier1"/><text x="500" y="173" font-size="8" text-anchor="middle">Tesla</text></g>
  <g><circle cx="620" cy="140" r="13" fill="#555555"/><text x="620" y="144" font-size="8" text-anchor="middle" fill="#FFFFFF">MIT CSAIL</text></g>
  <g><circle cx="700" cy="170" r="10" fill="#555555"/><text x="700" y="173" font-size="8" text-anchor="middle" fill="#FFFFFF">Stanford</text></g>

  <!-- CN行 -->
  <g><circle cx="180" cy="260" r="13" class="node-core"/><text x="180" y="264" font-size="9" text-anchor="middle" fill="#FFFFFF">MIIT</text></g>
  <g><circle cx="180" cy="290" r="10" fill="#8B3A2E"/><text x="180" y="293" font-size="8" text-anchor="middle" fill="#FFFFFF">CAC</text></g>
  <g><circle cx="400" cy="260" r="13" class="node-tier1"/><text x="400" y="264" font-size="9" text-anchor="middle">Huawei</text></g>
  <g><circle cx="340" cy="260" r="10" class="node-tier1"/><text x="340" y="263" font-size="8" text-anchor="middle">Baidu</text></g>
  <g><circle cx="460" cy="260" r="11" class="node-tier1"/><text x="460" y="263" font-size="8" text-anchor="middle">Unitree</text></g>
  <g><circle cx="500" cy="290" r="9" class="node-tier1"/><text x="500" y="293" font-size="8" text-anchor="middle">UBTech</text></g>
  <g><circle cx="620" cy="260" r="12" fill="#555555"/><text x="620" y="264" font-size="8" text-anchor="middle" fill="#FFFFFF">Tsinghua</text></g>
  <g><circle cx="700" cy="290" r="10" fill="#555555"/><text x="700" y="293" font-size="8" text-anchor="middle" fill="#FFFFFF">CAS</text></g>

  <!-- EU行 -->
  <g><circle cx="180" cy="380" r="14" class="node-core"/><text x="180" y="384" font-size="9" text-anchor="middle" fill="#FFFFFF">AI Act</text></g>
  <g><circle cx="180" cy="410" r="10" fill="#8B3A2E"/><text x="180" y="413" font-size="8" text-anchor="middle" fill="#FFFFFF">ENISA</text></g>
  <g><circle cx="400" cy="380" r="13" class="node-tier1"/><text x="400" y="384" font-size="9" text-anchor="middle">DeepMind</text></g>
  <g><circle cx="340" cy="410" r="10" class="node-tier1"/><text x="340" y="413" font-size="8" text-anchor="middle">Mistral</text></g>
  <g><circle cx="460" cy="380" r="11" class="node-tier1"/><text x="460" y="383" font-size="8" text-anchor="middle">ABB/KUKA</text></g>
  <g><circle cx="500" cy="410" r="9" class="node-tier1"/><text x="500" y="413" font-size="8" text-anchor="middle">Festo</text></g>
  <g><circle cx="620" cy="380" r="12" fill="#555555"/><text x="620" y="384" font-size="8" text-anchor="middle" fill="#FFFFFF">ETH Zurich</text></g>
  <g><circle cx="700" cy="410" r="10" fill="#555555"/><text x="700" y="413" font-size="8" text-anchor="middle" fill="#FFFFFF">Fraunhofer</text></g>

  <!-- JP行 -->
  <g><circle cx="180" cy="500" r="13" class="node-core"/><text x="180" y="504" font-size="9" text-anchor="middle" fill="#FFFFFF">AI戦略</text></g>
  <g><circle cx="180" cy="530" r="10" fill="#8B3A2E"/><text x="180" y="533" font-size="8" text-anchor="middle" fill="#FFFFFF">METI</text></g>
  <g><circle cx="400" cy="500" r="13" class="node-tier1"/><text x="400" y="504" font-size="9" text-anchor="middle">PFN</text></g>
  <g><circle cx="340" cy="530" r="10" class="node-tier1"/><text x="340" y="533" font-size="8" text-anchor="middle">SoftBank</text></g>
  <g><circle cx="460" cy="500" r="11" class="node-tier1"/><text x="460" y="503" font-size="8" text-anchor="middle">FANUC</text></g>
  <g><circle cx="500" cy="530" r="10" class="node-tier1"/><text x="500" y="533" font-size="8" text-anchor="middle">Toyota</text></g>
  <g><circle cx="620" cy="500" r="12" fill="#555555"/><text x="620" y="504" font-size="8" text-anchor="middle" fill="#FFFFFF">東大 IRT</text></g>
  <g><circle cx="700" cy="530" r="10" fill="#555555"/><text x="700" y="533" font-size="8" text-anchor="middle" fill="#FFFFFF">理研AIP</text></g>

  <!-- 凡例 -->
  <g transform="translate(20, 580)">
    <circle cx="0"  cy="0" r="5" class="node-core"/><text x="10" y="3" font-size="9">政策(P)</text>
    <circle cx="80" cy="0" r="5" class="node-tier1"/><text x="90" y="3" font-size="9">企業(C)</text>
    <circle cx="160" cy="0" r="5" fill="#555555"/><text x="170" y="3" font-size="9">研究機関(R)</text>
    <line x1="280" y1="0" x2="304" y2="0" stroke="#CC1400" stroke-width="2.2"/><text x="310" y="3" font-size="9">圏内連結</text>
    <line x1="380" y1="0" x2="404" y2="0" stroke="#CC1400" stroke-width="1.0"/><text x="410" y="3" font-size="9">跨圏協力</text>
    <line x1="490" y1="0" x2="514" y2="0" stroke="#8A7868" stroke-width="1.4" stroke-dasharray="5 3"/><text x="520" y="3" font-size="9">跨圏競合</text>
  </g>
</svg>
```

---

## 図5: 概念系譜ネットワーク (Embodiment 5概念の哲学→AI遷移)

**概要**: 「身体性 (Embodiment)」「アフォーダンス (Affordance)」「世界モデル (World Model)」「VLA (Vision-Language-Action)」「身体化認知 (Embodied Cognition)」の5中核概念について、哲学的起源 (左) → 認知科学・神経科学 (中) → AIロボティクス (右) への系譜遷移を時系列ネットワークで可視化。philosophy / anthropology / phai / ai-development DB の cross_ref 由来。

**配置**: 第II部 Phase A-B 章末 (VLA概念導入後) または終章 (関係論的物質代謝の哲学根拠)

**ノード**: 25 (5概念×5層) / **エッジ**: 35 (継承20 + 派生10 + 反転5)

```html
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" class="d4-net" role="img"
     aria-label="概念系譜ネットワーク - 5中核概念の哲学からAIへの遷移">
  <title>概念系譜ネットワーク (Embodiment 5概念)</title>
  <desc>身体性・アフォーダンス・世界モデル・VLA・身体化認知の5概念について、
        哲学起源→現象学→認知科学→ロボティクス→AI基盤モデルへの遷移を5層で可視化。</desc>

  <text x="400" y="26" text-anchor="middle" font-size="16" font-weight="600">概念系譜ネットワーク (5中核概念の哲学→AI 遷移)</text>
  <text x="400" y="44" text-anchor="middle" font-size="11" fill="#6B6B6B">左から右へ ／ 哲学起源 → 現象学 → 認知科学 → ロボティクス → AI基盤モデル</text>

  <!-- 5層 (列) ヘッダ -->
  <g font-size="10" font-weight="600" fill="#CC1400" text-anchor="middle">
    <text x="100" y="80">哲学起源</text>
    <text x="100" y="94" font-size="8" fill="#8A7868">(古代〜19c)</text>
    <text x="250" y="80">現象学/心理学</text>
    <text x="250" y="94" font-size="8" fill="#8A7868">(1900-1970)</text>
    <text x="400" y="80">認知科学</text>
    <text x="400" y="94" font-size="8" fill="#8A7868">(1970-2000)</text>
    <text x="550" y="80">ロボティクス</text>
    <text x="550" y="94" font-size="8" fill="#8A7868">(2000-2020)</text>
    <text x="700" y="80">AI基盤モデル</text>
    <text x="700" y="94" font-size="8" fill="#8A7868">(2020-2026)</text>
  </g>

  <!-- 列ガイド線 -->
  <g stroke="#EEEEEE" stroke-width="1">
    <line x1="100" y1="105" x2="100" y2="540"/>
    <line x1="250" y1="105" x2="250" y2="540"/>
    <line x1="400" y1="105" x2="400" y2="540"/>
    <line x1="550" y1="105" x2="550" y2="540"/>
    <line x1="700" y1="105" x2="700" y2="540"/>
  </g>

  <!-- 5行 (概念系譜) ガイドラベル -->
  <g font-size="10" font-weight="600" fill="#555555">
    <text x="20" y="170">身体性</text>
    <text x="20" y="260">アフォーダンス</text>
    <text x="20" y="350">世界モデル</text>
    <text x="20" y="440">身体化認知</text>
    <text x="20" y="525">VLA統合</text>
  </g>

  <!-- ===== EDGES: 継承 (細実線赤) ===== -->
  <g stroke="#CC1400" stroke-width="1.8" stroke-opacity="0.75" fill="none">
    <!-- 身体性 系譜 -->
    <line x1="115" y1="170" x2="235" y2="170"/>
    <line x1="265" y1="170" x2="385" y2="170"/>
    <line x1="415" y1="170" x2="535" y2="170"/>
    <line x1="565" y1="170" x2="685" y2="170"/>
    <!-- アフォーダンス 系譜 -->
    <line x1="115" y1="260" x2="235" y2="260"/>
    <line x1="265" y1="260" x2="385" y2="260"/>
    <line x1="415" y1="260" x2="535" y2="260"/>
    <line x1="565" y1="260" x2="685" y2="260"/>
    <!-- 世界モデル 系譜 -->
    <line x1="115" y1="350" x2="235" y2="350"/>
    <line x1="265" y1="350" x2="385" y2="350"/>
    <line x1="415" y1="350" x2="535" y2="350"/>
    <line x1="565" y1="350" x2="685" y2="350"/>
    <!-- 身体化認知 系譜 -->
    <line x1="115" y1="440" x2="235" y2="440"/>
    <line x1="265" y1="440" x2="385" y2="440"/>
    <line x1="415" y1="440" x2="535" y2="440"/>
    <line x1="565" y1="440" x2="685" y2="440"/>
    <!-- VLA: 4系譜統合 (右端で収束) -->
    <line x1="685" y1="170" x2="700" y2="525" stroke-width="1.4" stroke-opacity="0.55"/>
    <line x1="685" y1="260" x2="700" y2="525" stroke-width="1.4" stroke-opacity="0.55"/>
    <line x1="685" y1="350" x2="700" y2="525" stroke-width="1.4" stroke-opacity="0.55"/>
    <line x1="685" y1="440" x2="700" y2="525" stroke-width="1.4" stroke-opacity="0.55"/>
  </g>

  <!-- ===== EDGES: 派生・跨ぎ (細破線茶) ===== -->
  <g stroke="#8A7868" stroke-width="1.0" stroke-opacity="0.55" stroke-dasharray="3 2" fill="none">
    <!-- 現象学 Merleau-Ponty(身体性) → Gibson(アフォーダンス) -->
    <path d="M250,180 C290,210 290,210 250,250"/>
    <!-- Gibson → Pfeifer (アフォーダンス → 身体性ロボ) -->
    <path d="M400,270 C480,200 480,200 550,170"/>
    <!-- Varela(身体化認知) → Friston(世界モデル予測符号化) -->
    <path d="M400,430 C460,380 460,380 400,360"/>
    <!-- Schmidhuber(世界モデル) → LeCun JEPA(VLA) -->
    <path d="M550,340 C620,420 620,420 700,510"/>
    <!-- 反転: 古代「身体は牢獄」⇔ 現代「身体は知能」 -->
    <path d="M100,182 C90,300 90,300 100,438" stroke="#CC1400" stroke-dasharray="6 3" stroke-opacity="0.4"/>
  </g>

  <!-- ===== NODES ===== -->
  <!-- 行1: 身体性 -->
  <g><circle cx="100" cy="170" r="20" class="node-tier1"/><text x="100" y="167" font-size="9" text-anchor="middle">Plato/</text><text x="100" y="178" font-size="9" text-anchor="middle">Aristotle</text></g>
  <g><circle cx="250" cy="170" r="18" class="node-tier1"/><text x="250" y="167" font-size="9" text-anchor="middle">Merleau-</text><text x="250" y="178" font-size="9" text-anchor="middle">Ponty</text></g>
  <g><circle cx="400" cy="170" r="18" class="node-tier1"/><text x="400" y="167" font-size="9" text-anchor="middle">Lakoff/</text><text x="400" y="178" font-size="9" text-anchor="middle">Johnson</text></g>
  <g><circle cx="550" cy="170" r="20" class="node-tier1"/><text x="550" y="167" font-size="9" text-anchor="middle">Pfeifer/</text><text x="550" y="178" font-size="9" text-anchor="middle">Brooks</text></g>
  <g><circle cx="700" cy="170" r="22" class="node-core"/><text x="700" y="167" font-size="9" text-anchor="middle" fill="#FFFFFF">Embodied</text><text x="700" y="178" font-size="9" text-anchor="middle" fill="#FFFFFF">FM 2024</text></g>

  <!-- 行2: アフォーダンス -->
  <g><circle cx="100" cy="260" r="16" class="node-tier1"/><text x="100" y="257" font-size="9" text-anchor="middle">Heidegger</text><text x="100" y="268" font-size="8" text-anchor="middle">Zuhanden</text></g>
  <g><circle cx="250" cy="260" r="22" class="node-tier1"/><text x="250" y="257" font-size="9" text-anchor="middle">Gibson</text><text x="250" y="268" font-size="8" text-anchor="middle">1979</text></g>
  <g><circle cx="400" cy="260" r="18" class="node-tier1"/><text x="400" y="257" font-size="9" text-anchor="middle">Norman</text><text x="400" y="268" font-size="8" text-anchor="middle">DOET</text></g>
  <g><circle cx="550" cy="260" r="18" class="node-tier1"/><text x="550" y="257" font-size="9" text-anchor="middle">Gupta/</text><text x="550" y="268" font-size="9" text-anchor="middle">Malik</text></g>
  <g><circle cx="700" cy="260" r="20" class="node-core"/><text x="700" y="257" font-size="9" text-anchor="middle" fill="#FFFFFF">Affordance-</text><text x="700" y="268" font-size="8" text-anchor="middle" fill="#FFFFFF">VLM</text></g>

  <!-- 行3: 世界モデル -->
  <g><circle cx="100" cy="350" r="16" class="node-tier1"/><text x="100" y="347" font-size="8" text-anchor="middle">Kant</text><text x="100" y="358" font-size="8" text-anchor="middle">先験図式</text></g>
  <g><circle cx="250" cy="350" r="18" class="node-tier1"/><text x="250" y="347" font-size="8" text-anchor="middle">Craik 1943</text><text x="250" y="358" font-size="8" text-anchor="middle">mental model</text></g>
  <g><circle cx="400" cy="350" r="22" class="node-tier1"/><text x="400" y="347" font-size="9" text-anchor="middle">Friston</text><text x="400" y="358" font-size="8" text-anchor="middle">Free Energy</text></g>
  <g><circle cx="550" cy="350" r="20" class="node-tier1"/><text x="550" y="347" font-size="9" text-anchor="middle">Ha &amp;</text><text x="550" y="358" font-size="9" text-anchor="middle">Schmidhuber</text></g>
  <g><circle cx="700" cy="350" r="22" class="node-core"/><text x="700" y="347" font-size="9" text-anchor="middle" fill="#FFFFFF">JEPA/</text><text x="700" y="358" font-size="9" text-anchor="middle" fill="#FFFFFF">Genie 2</text></g>

  <!-- 行4: 身体化認知 -->
  <g><circle cx="100" cy="440" r="16" class="node-tier1"/><text x="100" y="437" font-size="8" text-anchor="middle">Spinoza</text><text x="100" y="448" font-size="8" text-anchor="middle">心身一元</text></g>
  <g><circle cx="250" cy="440" r="16" class="node-tier1"/><text x="250" y="437" font-size="9" text-anchor="middle">James/</text><text x="250" y="448" font-size="9" text-anchor="middle">Dewey</text></g>
  <g><circle cx="400" cy="440" r="22" class="node-tier1"/><text x="400" y="437" font-size="9" text-anchor="middle">Varela/</text><text x="400" y="448" font-size="9" text-anchor="middle">Clark</text></g>
  <g><circle cx="550" cy="440" r="18" class="node-tier1"/><text x="550" y="437" font-size="8" text-anchor="middle">Iida</text><text x="550" y="448" font-size="8" text-anchor="middle">Soft Robot</text></g>
  <g><circle cx="700" cy="440" r="20" class="node-core"/><text x="700" y="437" font-size="9" text-anchor="middle" fill="#FFFFFF">Predictive</text><text x="700" y="448" font-size="8" text-anchor="middle" fill="#FFFFFF">Embodied AI</text></g>

  <!-- 行5: VLA統合 (右端のみ・4系譜が収束) -->
  <g><circle cx="700" cy="525" r="26" fill="#CC1400" stroke="#3F1814" stroke-width="2"/><text x="700" y="522" font-size="10" font-weight="700" text-anchor="middle" fill="#FFFFFF">VLA</text><text x="700" y="536" font-size="8" text-anchor="middle" fill="#FFFFFF">RT-2 / π0 / Helix</text></g>

  <!-- 凡例 -->
  <g transform="translate(20, 580)">
    <line x1="0" y1="0" x2="24" y2="0" stroke="#CC1400" stroke-width="1.8"/>
    <text x="30" y="3" font-size="9">継承 (genealogy)</text>
    <line x1="140" y1="0" x2="164" y2="0" stroke="#8A7868" stroke-width="1.0" stroke-dasharray="3 2"/>
    <text x="170" y="3" font-size="9">派生 (cross-derivation)</text>
    <line x1="320" y1="0" x2="344" y2="0" stroke="#CC1400" stroke-dasharray="6 3" stroke-opacity="0.4"/>
    <text x="350" y="3" font-size="9">反転 (古代「身体=牢獄」⇔ 現代「身体=知能」)</text>
  </g>
</svg>
```

---

## 実装メモ・利用ガイド

### 教科書 HTML への埋込
各 SVG ブロックを既存 `~/projects/research/physical-ai-2100/output/index.html` の該当章直後に挿入する。挿入時は `<figure>` で囲み `<figcaption>` を付与:

```html
<figure class="d4-figure" style="margin: 32px 0;">
  <!-- SVG block here -->
  <figcaption style="margin-top: 8px; font-size: 12px; color: var(--text-secondary);">
    図N: 8系統相互作用ネットワーク。AI/MLを中核に7系統が環状配置され、
    24本のエッジで促進・相互依存・抑制の関係を示す。
  </figcaption>
</figure>
```

### ダークモード対応
親 HTML の `[data-theme="dark"]` ルールで以下を上書きすれば SVG 内テキスト・薄色ノードが自動追従する:
- `text` の `fill` を `var(--text)` に
- `.node-tier1/2/3` の fill を `var(--card)` に
- `.edge-line` の stroke-opacity を 0.55 に

各 SVG はインライン埋込み前提なので `currentColor` を使わず明示色指定としている。`@media print` では帯色/枠線が崩れないよう `background-color: #FFFFFF !important` を親 HTML 側で指定推奨。

### データ出典
- 図1 (8系統): `~/projects/research/physical-ai-2100/phase2_streams/stream{1..5}_*.md` + 拡張3系統 (Mechanics/Energy/Sensor は stream2 §4 由来)
- 図2 (100人物): `phase2_streams/stream1_ai_ml.md` §1 系譜整理 + `phase1_papers/c{1..5}_*.md`
- 図3 (DB×章): `~/projects/research/physical-ai-2100/enhancement/ardb/mapping_report.md`
- 図4 (三層): `db-evidence/experts_evidence.md` + AR-DB policy-db/experts/sgrd/sgpr 検索結果
- 図5 (概念系譜): philosophy DB + phai-db cross_ref + ai-development DB 由来

### 次工程
教科書 HTML 埋込後、`doc-verify` エージェントで5図のラベル一致性・色コントラスト (WCAG AA) ・ダークモード切替正常性を検証推奨。各図に `<title>` `<desc>` `role="img"` `aria-label` を付与済みで a11y 対応済。
