# D5 図解設計隊 — 5新規インフォグラフィック

Physical AI 2100 教科書ブラッシュアップ用の 5 SVG。既存 25 SVG と統一する viewBox / 配色 / フォントを採用。

## 共通仕様
- viewBox: 主要 `680×360〜400`、横長 `760×320〜380`
- フォント: `Noto Sans JP, sans-serif`（ラベル）/ ダーク時は `fill="currentColor"` 派生で text-secondary 連動
- 配色: `#121212` 主軸 / `#CC1400` 赤白CIアクセント / `#555` ラベル / `#6B6B6B` 注釈
- ダーク時: `stroke="currentColor"` で代替する代わりに、 wrapping figure に `style="filter: var(--svg-invert,none)"` を被せず、固定色で十分なコントラストを担保（既存 25 SVG と同方針）
- 凡例: 図下に `<figcaption>` で説明、`font-size:0.78rem;color:#6B6B6B`
- アクセシビリティ: 各 `<svg>` 直下に `<title>` と `<desc>` を必須配置

---

## 図 D5-1: Physical AI の3定義図（知性が物質に降りる / 解像度 / 関係論的存在）

```html
<figure style="margin:36px 0;text-align:center;background:rgba(204,20,0,0.02);border-top:1px solid #CC1400;border-bottom:1px solid #CC1400;padding:32px 16px;">
<svg viewBox="0 0 760 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="d5-1-title d5-1-desc" style="width:100%;max-width:760px;height:auto;">
<title id="d5-1-title">Physical AI の3定義図</title>
<desc id="d5-1-desc">Physical AIを3つの定義で示す3-up図。左から「知性が物質に降りる」「解像度が上がる」「関係論的存在」。</desc>

<!-- パネル1: 知性が物質に降りる -->
<g>
  <rect x="40" y="60" width="200" height="240" fill="none" stroke="#121212" stroke-width="1.2"/>
  <text x="140" y="48" font-family="Noto Sans JP, sans-serif" font-size="12" fill="#CC1400" text-anchor="middle" font-weight="700" letter-spacing="0.08em">DEFINITION 01</text>
  <text x="140" y="88" font-family="Noto Sans JP, sans-serif" font-size="14" fill="#121212" text-anchor="middle" font-weight="700">知性が物質に降りる</text>
  <!-- 降下の矢印 -->
  <circle cx="140" cy="135" r="22" fill="none" stroke="#CC1400" stroke-width="1.5"/>
  <text x="140" y="140" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#CC1400" text-anchor="middle">LLM</text>
  <line x1="140" y1="160" x2="140" y2="220" stroke="#CC1400" stroke-width="2" marker-end="url(#d5arrow)"/>
  <text x="160" y="195" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#6B6B6B">descent</text>
  <rect x="100" y="225" width="80" height="50" fill="none" stroke="#121212" stroke-width="1.5"/>
  <text x="140" y="247" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#121212" text-anchor="middle">物質</text>
  <text x="140" y="262" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#6B6B6B" text-anchor="middle">aktuator + sensor</text>
  <text x="140" y="290" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555" text-anchor="middle">VLA で言語→行為が同階層</text>
</g>

<!-- パネル2: 解像度が上がる -->
<g>
  <rect x="280" y="60" width="200" height="240" fill="none" stroke="#121212" stroke-width="1.2"/>
  <text x="380" y="48" font-family="Noto Sans JP, sans-serif" font-size="12" fill="#CC1400" text-anchor="middle" font-weight="700" letter-spacing="0.08em">DEFINITION 02</text>
  <text x="380" y="88" font-family="Noto Sans JP, sans-serif" font-size="14" fill="#121212" text-anchor="middle" font-weight="700">解像度が上がる</text>
  <!-- 粗い格子 → 細かい格子 -->
  <g stroke="#999" stroke-width="0.8" fill="none">
    <rect x="305" y="120" width="60" height="60"/>
    <line x1="305" y1="150" x2="365" y2="150"/>
    <line x1="335" y1="120" x2="335" y2="180"/>
  </g>
  <text x="335" y="200" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#6B6B6B" text-anchor="middle">2020</text>
  <text x="395" y="155" font-family="Noto Sans JP, sans-serif" font-size="14" fill="#CC1400" text-anchor="middle">→</text>
  <g stroke="#CC1400" stroke-width="0.6" fill="none">
    <rect x="410" y="120" width="60" height="60"/>
    <line x1="410" y1="135" x2="470" y2="135"/>
    <line x1="410" y1="150" x2="470" y2="150"/>
    <line x1="410" y1="165" x2="470" y2="165"/>
    <line x1="425" y1="120" x2="425" y2="180"/>
    <line x1="440" y1="120" x2="440" y2="180"/>
    <line x1="455" y1="120" x2="455" y2="180"/>
  </g>
  <text x="440" y="200" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#CC1400" text-anchor="middle">2026</text>
  <text x="380" y="232" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555" text-anchor="middle">触覚 1mm→0.1mm / 制御 100Hz→1kHz</text>
  <text x="380" y="248" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555" text-anchor="middle">力 1N→0.05N / 6軸統合化</text>
  <text x="380" y="285" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555" text-anchor="middle">物理世界の「見え方」が桁単位で精密化</text>
</g>

<!-- パネル3: 関係論的存在 -->
<g>
  <rect x="520" y="60" width="200" height="240" fill="none" stroke="#121212" stroke-width="1.2"/>
  <text x="620" y="48" font-family="Noto Sans JP, sans-serif" font-size="12" fill="#CC1400" text-anchor="middle" font-weight="700" letter-spacing="0.08em">DEFINITION 03</text>
  <text x="620" y="88" font-family="Noto Sans JP, sans-serif" font-size="14" fill="#121212" text-anchor="middle" font-weight="700">関係論的存在</text>
  <!-- 三点ネットワーク -->
  <circle cx="565" cy="160" r="14" fill="none" stroke="#121212" stroke-width="1.5"/>
  <text x="565" y="164" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#121212" text-anchor="middle">人</text>
  <circle cx="675" cy="160" r="14" fill="none" stroke="#121212" stroke-width="1.5"/>
  <text x="675" y="164" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#121212" text-anchor="middle">環境</text>
  <circle cx="620" cy="225" r="16" fill="none" stroke="#CC1400" stroke-width="2"/>
  <text x="620" y="229" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#CC1400" text-anchor="middle">PhAI</text>
  <line x1="579" y1="160" x2="661" y2="160" stroke="#CC1400" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="570" y1="172" x2="608" y2="212" stroke="#CC1400" stroke-width="1.2"/>
  <line x1="670" y1="172" x2="632" y2="212" stroke="#CC1400" stroke-width="1.2"/>
  <text x="620" y="265" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555" text-anchor="middle">単体ではなく「人-環境-機械」</text>
  <text x="620" y="280" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555" text-anchor="middle">の結節として現れる</text>
</g>

<defs>
  <marker id="d5arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
    <path d="M0,0 L8,4 L0,8 z" fill="#CC1400"/>
  </marker>
</defs>
</svg>
<figcaption style="font-family:var(--font);font-size:0.78rem;color:#6B6B6B;margin-top:12px;text-align:center;">図 D5-1: Physical AI の3定義図。「知性が物質に降りる」「解像度が桁単位で上がる」「関係論的に現れる」── 3つの定義は相互補完的で、いずれか1つで Physical AI を定義することはできない。</figcaption>
</figure>
```

---

## 図 D5-2: 特異性主張への留保 ── シンギュラリティ vs 5系統合流

```html
<figure style="margin:36px 0;text-align:center;background:rgba(204,20,0,0.02);border-top:1px solid #CC1400;border-bottom:1px solid #CC1400;padding:32px 16px;">
<svg viewBox="0 0 760 380" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="d5-2-title d5-2-desc" style="width:100%;max-width:760px;height:auto;">
<title id="d5-2-title">特異性主張への留保 比較表図</title>
<desc id="d5-2-desc">シンギュラリティ説と5系統合流説を6観点で対比する比較表。本書は後者の立場を採る。</desc>

<!-- ヘッダ -->
<text x="380" y="28" font-family="Noto Sans JP, sans-serif" font-size="13" fill="#121212" text-anchor="middle" font-weight="700">フィジカルAIをどう読むか ── 2つの立場の対比</text>

<!-- 列見出し -->
<rect x="40" y="50" width="180" height="36" fill="#F7F7F5" stroke="#121212" stroke-width="1"/>
<text x="130" y="73" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#555" text-anchor="middle" font-weight="700">観点</text>

<rect x="220" y="50" width="270" height="36" fill="#F7F7F5" stroke="#121212" stroke-width="1"/>
<text x="355" y="73" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#6B6B6B" text-anchor="middle" font-weight="700">シンギュラリティ説</text>

<rect x="490" y="50" width="230" height="36" fill="rgba(204,20,0,0.08)" stroke="#CC1400" stroke-width="1.5"/>
<text x="605" y="73" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#CC1400" text-anchor="middle" font-weight="700">5系統合流説（本書）</text>

<!-- 行データ -->
<g font-family="Noto Sans JP, sans-serif" font-size="10.5">
  <!-- row1 -->
  <rect x="40" y="86" width="180" height="42" fill="none" stroke="#D9D9D9" stroke-width="0.8"/>
  <text x="50" y="112" fill="#121212">時間構造</text>
  <rect x="220" y="86" width="270" height="42" fill="none" stroke="#D9D9D9" stroke-width="0.8"/>
  <text x="230" y="105" fill="#555">単一の特異点（垂直の跳躍）</text>
  <text x="230" y="121" fill="#999" font-size="9.5">2045 ± n年に集中</text>
  <rect x="490" y="86" width="230" height="42" fill="none" stroke="#D9D9D9" stroke-width="0.8"/>
  <text x="500" y="105" fill="#121212">5系統が独立に発生→2010s合流</text>
  <text x="500" y="121" fill="#999" font-size="9.5">74年（2026-2100）の漸進</text>

  <!-- row2 -->
  <rect x="40" y="128" width="180" height="42" fill="#F7F7F5" stroke="#D9D9D9" stroke-width="0.8"/>
  <text x="50" y="154" fill="#121212">駆動因子</text>
  <rect x="220" y="128" width="270" height="42" fill="#F7F7F5" stroke="#D9D9D9" stroke-width="0.8"/>
  <text x="230" y="148" fill="#555">計算量の指数的増加 1因子</text>
  <text x="230" y="163" fill="#999" font-size="9.5">ムーアの法則の延長</text>
  <rect x="490" y="128" width="230" height="42" fill="#F7F7F5" stroke="#D9D9D9" stroke-width="0.8"/>
  <text x="500" y="148" fill="#121212">HW/Ctrl/RL/FM/Sim の5因子</text>
  <text x="500" y="163" fill="#999" font-size="9.5">それぞれ別の制約曲線</text>

  <!-- row3 -->
  <rect x="40" y="170" width="180" height="42" fill="none" stroke="#D9D9D9" stroke-width="0.8"/>
  <text x="50" y="196" fill="#121212">予測の粒度</text>
  <rect x="220" y="170" width="270" height="42" fill="none" stroke="#D9D9D9" stroke-width="0.8"/>
  <text x="230" y="189" fill="#555">「AGI到来」の単一イベント</text>
  <text x="230" y="205" fill="#999" font-size="9.5">何が起きるかは予測不能</text>
  <rect x="490" y="170" width="230" height="42" fill="none" stroke="#D9D9D9" stroke-width="0.8"/>
  <text x="500" y="189" fill="#121212">7フェーズ × 8系統で限定</text>
  <text x="500" y="205" fill="#999" font-size="9.5">時期と内容を学術論文で固定</text>

  <!-- row4 -->
  <rect x="40" y="212" width="180" height="42" fill="#F7F7F5" stroke="#D9D9D9" stroke-width="0.8"/>
  <text x="50" y="238" fill="#121212">物質との関係</text>
  <rect x="220" y="212" width="270" height="42" fill="#F7F7F5" stroke="#D9D9D9" stroke-width="0.8"/>
  <text x="230" y="232" fill="#555">情報空間の指数曲線の延長</text>
  <text x="230" y="247" fill="#999" font-size="9.5">物質制約は副次的</text>
  <rect x="490" y="212" width="230" height="42" fill="#F7F7F5" stroke="#D9D9D9" stroke-width="0.8"/>
  <text x="500" y="232" fill="#121212">物質基盤が律速</text>
  <text x="500" y="247" fill="#999" font-size="9.5">電力・素材・実機データが限界</text>

  <!-- row5 -->
  <rect x="40" y="254" width="180" height="42" fill="none" stroke="#D9D9D9" stroke-width="0.8"/>
  <text x="50" y="280" fill="#121212">歴史的位置</text>
  <rect x="220" y="254" width="270" height="42" fill="none" stroke="#D9D9D9" stroke-width="0.8"/>
  <text x="230" y="273" fill="#555">史上類例なき超越的事象</text>
  <text x="230" y="289" fill="#999" font-size="9.5">過去から学べない</text>
  <rect x="490" y="254" width="230" height="42" fill="none" stroke="#D9D9D9" stroke-width="0.8"/>
  <text x="500" y="273" fill="#121212">高位高原での構造的反復</text>
  <text x="500" y="289" fill="#999" font-size="9.5">情報革命の後峰として読む</text>

  <!-- row6 -->
  <rect x="40" y="296" width="180" height="42" fill="#F7F7F5" stroke="#D9D9D9" stroke-width="0.8"/>
  <text x="50" y="322" fill="#121212">行為への含意</text>
  <rect x="220" y="296" width="270" height="42" fill="#F7F7F5" stroke="#D9D9D9" stroke-width="0.8"/>
  <text x="230" y="315" fill="#555">準備か待機しかできない</text>
  <text x="230" y="331" fill="#999" font-size="9.5">設計の余地は限定的</text>
  <rect x="490" y="296" width="230" height="42" fill="#F7F7F5" stroke="#D9D9D9" stroke-width="0.8"/>
  <text x="500" y="315" fill="#121212">5系統それぞれに介入余地</text>
  <text x="500" y="331" fill="#999" font-size="9.5">設計・規制・市民選択が効く</text>
</g>

<text x="380" y="368" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#CC1400" text-anchor="middle" font-style="italic">本書は右列の立場を採る</text>
</svg>
<figcaption style="font-family:var(--font);font-size:0.78rem;color:#6B6B6B;margin-top:12px;text-align:center;">図 D5-2: 特異性主張への留保。シンギュラリティ説と 5系統合流説 を 6観点で対比。本書は後者の立場から、74年の時間幅と8系統の構造分解で、フィジカルAIを「介入可能な運動」として記述する。</figcaption>
</figure>
```

---

## 図 D5-3: 冷静と真剣のバランス（楽観 vs 悲観 / 軌跡 vs 跳躍 の四象限）

```html
<figure style="margin:36px 0;text-align:center;background:rgba(204,20,0,0.02);border-top:1px solid #CC1400;border-bottom:1px solid #CC1400;padding:32px 16px;">
<svg viewBox="0 0 680 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="d5-3-title d5-3-desc" style="width:100%;max-width:680px;height:auto;">
<title id="d5-3-title">冷静と真剣のバランス図</title>
<desc id="d5-3-desc">縦軸「楽観─悲観」、横軸「軌跡的=構造的反復─跳躍的=特異点」の四象限で、4態度を配置。本書の立場は中央の交差点に位置する。</desc>

<text x="340" y="28" font-family="Noto Sans JP, sans-serif" font-size="13" fill="#121212" text-anchor="middle" font-weight="700">冷静と真剣の両立 ── 4態度の四象限</text>

<!-- 軸 -->
<line x1="340" y1="60" x2="340" y2="350" stroke="#121212" stroke-width="1.5"/>
<line x1="60" y1="205" x2="620" y2="205" stroke="#121212" stroke-width="1.5"/>

<!-- 軸ラベル -->
<text x="340" y="50" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#555" text-anchor="middle" font-weight="700">楽観</text>
<text x="340" y="368" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#555" text-anchor="middle" font-weight="700">悲観</text>
<text x="58" y="220" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#555" text-anchor="end" font-weight="700">軌跡的</text>
<text x="58" y="232" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999" text-anchor="end">構造的反復</text>
<text x="622" y="220" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#555" text-anchor="start" font-weight="700">跳躍的</text>
<text x="622" y="232" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999" text-anchor="start">特異点・断絶</text>

<!-- 第1象限: 右上 跳躍×楽観 -->
<g>
  <rect x="345" y="65" width="270" height="135" fill="rgba(204,20,0,0.03)" stroke="#D9D9D9" stroke-width="0.5"/>
  <text x="480" y="90" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#CC1400" text-anchor="middle" font-weight="700">A. 技術ユートピア</text>
  <text x="480" y="110" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#555" text-anchor="middle">特異点に至り、希少性が消える</text>
  <text x="480" y="128" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#555" text-anchor="middle">労働・病・物質の制約から解放</text>
  <text x="480" y="155" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#6B6B6B" text-anchor="middle" font-style="italic">代表: Kurzweil 2005, abundance系</text>
  <text x="480" y="180" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#999" text-anchor="middle">→ 物質制約を過小評価</text>
</g>

<!-- 第2象限: 左上 軌跡×楽観 -->
<g>
  <rect x="65" y="65" width="270" height="135" fill="none" stroke="#D9D9D9" stroke-width="0.5"/>
  <text x="200" y="90" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#121212" text-anchor="middle" font-weight="700">B. 漸進的改善</text>
  <text x="200" y="110" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#555" text-anchor="middle">過去の革命の延長として</text>
  <text x="200" y="128" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#555" text-anchor="middle">便益が穏当に積み上がる</text>
  <text x="200" y="155" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#6B6B6B" text-anchor="middle" font-style="italic">代表: Solow派・標準的経済学</text>
  <text x="200" y="180" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#999" text-anchor="middle">→ 質的転換を見落とす</text>
</g>

<!-- 第3象限: 左下 軌跡×悲観 -->
<g>
  <rect x="65" y="210" width="270" height="135" fill="none" stroke="#D9D9D9" stroke-width="0.5"/>
  <text x="200" y="235" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#121212" text-anchor="middle" font-weight="700">C. 既定路線的衰退</text>
  <text x="200" y="255" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#555" text-anchor="middle">過去の革命と同様に</text>
  <text x="200" y="273" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#555" text-anchor="middle">格差・環境を悪化させる</text>
  <text x="200" y="300" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#6B6B6B" text-anchor="middle" font-style="italic">代表: 第二次産業革命の負債論</text>
  <text x="200" y="325" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#999" text-anchor="middle">→ 介入余地を放棄</text>
</g>

<!-- 第4象限: 右下 跳躍×悲観 -->
<g>
  <rect x="345" y="210" width="270" height="135" fill="rgba(204,20,0,0.03)" stroke="#D9D9D9" stroke-width="0.5"/>
  <text x="480" y="235" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#CC1400" text-anchor="middle" font-weight="700">D. AI終末論</text>
  <text x="480" y="255" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#555" text-anchor="middle">特異点が人類存続を脅かす</text>
  <text x="480" y="273" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#555" text-anchor="middle">準備か防御しかできない</text>
  <text x="480" y="300" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#6B6B6B" text-anchor="middle" font-style="italic">代表: Bostrom・x-risk 系</text>
  <text x="480" y="325" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#999" text-anchor="middle">→ 設計の余地を見落とす</text>
</g>

<!-- 中央の本書の立場 -->
<circle cx="340" cy="205" r="38" fill="#FFFFFF" stroke="#CC1400" stroke-width="2.5"/>
<text x="340" y="200" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#CC1400" text-anchor="middle" font-weight="700">本書の立場</text>
<text x="340" y="216" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#CC1400" text-anchor="middle">冷静 × 真剣</text>

<text x="340" y="390" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#6B6B6B" text-anchor="middle" font-style="italic">4象限のいずれにも振れず、中央で両軸を同時に保持する</text>
</svg>
<figcaption style="font-family:var(--font);font-size:0.78rem;color:#6B6B6B;margin-top:12px;text-align:center;">図 D5-3: 冷静と真剣のバランス。縦軸（楽観─悲観）と横軸（軌跡的─跳躍的）で4態度を配置。本書はいずれの象限にも振れず、中央で「軌跡的読みの冷静」と「74年の真剣な引き受け」を同時保持する立場をとる。</figcaption>
</figure>
```

---

## 図 D5-4: 次の千年シナリオ（2100年以降の3シナリオ）

```html
<figure style="margin:36px 0;text-align:center;background:rgba(204,20,0,0.02);border-top:1px solid #CC1400;border-bottom:1px solid #CC1400;padding:32px 16px;">
<svg viewBox="0 0 760 380" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="d5-4-title d5-4-desc" style="width:100%;max-width:760px;height:auto;">
<title id="d5-4-title">2100年以降の3シナリオ図</title>
<desc id="d5-4-desc">2100年を分岐点に、Continuation/Dissolution/Post-Physical の3シナリオが分岐する。2026年から3000年までを横軸とする。</desc>

<text x="380" y="28" font-family="Noto Sans JP, sans-serif" font-size="13" fill="#121212" text-anchor="middle" font-weight="700">次の千年 ── 2100年以降の3シナリオ</text>

<!-- 横軸: 時間 -->
<line x1="60" y1="320" x2="720" y2="320" stroke="#121212" stroke-width="1.5"/>
<text x="60" y="340" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#555" text-anchor="middle">2026</text>
<text x="180" y="340" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#555" text-anchor="middle">2100</text>
<text x="320" y="340" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#555" text-anchor="middle">2300</text>
<text x="500" y="340" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#555" text-anchor="middle">2600</text>
<text x="710" y="340" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#555" text-anchor="middle">3000</text>

<!-- 縦軸ラベル -->
<text x="40" y="100" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#555" text-anchor="end">物質依存度</text>
<text x="40" y="115" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999" text-anchor="end">（暮らしの）</text>

<!-- 分岐点 2100年 -->
<line x1="180" y1="60" x2="180" y2="320" stroke="#CC1400" stroke-width="0.8" stroke-dasharray="3,3"/>
<text x="180" y="55" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#CC1400" text-anchor="middle" font-weight="700">分岐点</text>

<!-- 2026-2100共通幹 -->
<path d="M 60,200 Q 110,195 180,180" stroke="#121212" stroke-width="2.2" fill="none"/>

<!-- シナリオ A: continuation 物質依存維持 -->
<path d="M 180,180 Q 350,175 720,165" stroke="#CC1400" stroke-width="2.5" fill="none"/>
<text x="510" y="155" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#CC1400" font-weight="700">A. 継続 (Continuation)</text>
<text x="510" y="170" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#6B6B6B">フィジカルAIが物質基盤を支え続ける／人類は物質的暮らしを保つ</text>

<!-- シナリオ B: dissolution 物質依存低下 -->
<path d="M 180,180 Q 350,240 720,275" stroke="#121212" stroke-width="2.5" fill="none"/>
<text x="510" y="255" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#121212" font-weight="700">B. 解消 (Dissolution)</text>
<text x="510" y="270" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#6B6B6B">エネルギー枯渇・気候破局で物質基盤が縮退／低位高原への撤退</text>

<!-- シナリオ C: post-physical 物質性そのものが変容 -->
<path d="M 180,180 Q 350,130 720,80" stroke="#555555" stroke-width="2.5" fill="none" stroke-dasharray="6,4"/>
<text x="510" y="100" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#555" font-weight="700">C. Post-Physical</text>
<text x="510" y="115" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#6B6B6B">合成生物・分子製造・意識アップロードで「物質」概念そのものが再定義</text>

<!-- 共通幹ラベル -->
<text x="120" y="190" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555" text-anchor="middle">74年の共通幹</text>
<text x="120" y="204" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999" text-anchor="middle">(本書の対象)</text>

<!-- 注釈枠 -->
<rect x="60" y="350" width="660" height="22" fill="none" stroke="#D9D9D9" stroke-width="0.5"/>
<text x="380" y="365" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#6B6B6B" text-anchor="middle" font-style="italic">本書は2100年までを扱う。それ以降は3シナリオの分岐を「次の千年の問い」として開いたまま残す。</text>
</svg>
<figcaption style="font-family:var(--font);font-size:0.78rem;color:#6B6B6B;margin-top:12px;text-align:center;">図 D5-4: 次の千年シナリオ。2100年を分岐点とする3シナリオ（Continuation / Dissolution / Post-Physical）。本書の射程は2026-2100年の共通幹までであり、その先は判断の余地として開かれている。</figcaption>
</figure>
```

---

## 図 D5-5: 市民活用ガイド ── 一般読者向け年表（家事/医療/移動/教育）

```html
<figure style="margin:36px 0;text-align:center;background:rgba(204,20,0,0.02);border-top:1px solid #CC1400;border-bottom:1px solid #CC1400;padding:32px 16px;">
<svg viewBox="0 0 760 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="d5-5-title d5-5-desc" style="width:100%;max-width:760px;height:auto;">
<title id="d5-5-title">市民活用ガイド年表</title>
<desc id="d5-5-desc">家事・医療・移動・教育の4領域で、2030/2050/2080/2100に何が変わるかを示す年表。</desc>

<text x="380" y="28" font-family="Noto Sans JP, sans-serif" font-size="13" fill="#121212" text-anchor="middle" font-weight="700">市民活用ガイド ── 4領域で何が変わるか</text>

<!-- 列見出し（時代） -->
<g font-family="Noto Sans JP, sans-serif" font-size="10.5" font-weight="700">
  <rect x="160" y="50" width="140" height="30" fill="#F7F7F5" stroke="#121212" stroke-width="0.8"/>
  <text x="230" y="69" fill="#CC1400" text-anchor="middle">2030 (Phase A)</text>
  <rect x="300" y="50" width="140" height="30" fill="#F7F7F5" stroke="#121212" stroke-width="0.8"/>
  <text x="370" y="69" fill="#CC1400" text-anchor="middle">2050 (Phase C)</text>
  <rect x="440" y="50" width="140" height="30" fill="#F7F7F5" stroke="#121212" stroke-width="0.8"/>
  <text x="510" y="69" fill="#CC1400" text-anchor="middle">2080 (Phase F)</text>
  <rect x="580" y="50" width="140" height="30" fill="#F7F7F5" stroke="#121212" stroke-width="0.8"/>
  <text x="650" y="69" fill="#CC1400" text-anchor="middle">2100 (Phase G)</text>
</g>

<!-- 行: 家事 -->
<rect x="40" y="80" width="120" height="70" fill="#F7F7F5" stroke="#121212" stroke-width="0.8"/>
<text x="100" y="118" font-family="Noto Sans JP, sans-serif" font-size="12" fill="#121212" text-anchor="middle" font-weight="700">家事</text>
<rect x="160" y="80" width="140" height="70" fill="none" stroke="#D9D9D9"/>
<text x="170" y="100" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555">特化型 (掃除/食洗)</text>
<text x="170" y="115" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">価格 5-20万円</text>
<text x="170" y="133" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">家事削減 1-2h/週</text>
<rect x="300" y="80" width="140" height="70" fill="none" stroke="#D9D9D9"/>
<text x="310" y="100" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555">ヒューマノイド導入</text>
<text x="310" y="115" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">価格 2-5万ドル</text>
<text x="310" y="133" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">家事削減 8-12h/週</text>
<rect x="440" y="80" width="140" height="70" fill="none" stroke="#D9D9D9"/>
<text x="450" y="100" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555">家庭1台時代</text>
<text x="450" y="115" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">価格 1万ドル以下</text>
<text x="450" y="133" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">調理/介助/育児補助</text>
<rect x="580" y="80" width="140" height="70" fill="none" stroke="#D9D9D9"/>
<text x="590" y="100" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555">家事概念の再定義</text>
<text x="590" y="115" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">「住まう」のかたち変容</text>
<text x="590" y="133" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">余暇/関係性に再配分</text>

<!-- 行: 医療 -->
<rect x="40" y="150" width="120" height="70" fill="#F7F7F5" stroke="#121212" stroke-width="0.8"/>
<text x="100" y="188" font-family="Noto Sans JP, sans-serif" font-size="12" fill="#121212" text-anchor="middle" font-weight="700">医療</text>
<rect x="160" y="150" width="140" height="70" fill="none" stroke="#D9D9D9"/>
<text x="170" y="170" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555">手術支援/画像診断</text>
<text x="170" y="185" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">da Vinci 系の延長</text>
<text x="170" y="203" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">外科医の補助</text>
<rect x="300" y="150" width="140" height="70" fill="none" stroke="#D9D9D9"/>
<text x="310" y="170" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555">介護ロボ標準装備</text>
<text x="310" y="185" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">在宅看取り支援</text>
<text x="310" y="203" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">移乗/見守り/服薬</text>
<rect x="440" y="150" width="140" height="70" fill="none" stroke="#D9D9D9"/>
<text x="450" y="170" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555">体内ナノロボ普及</text>
<text x="450" y="185" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">早期診断/標的治療</text>
<text x="450" y="203" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">健康寿命 +10〜15y</text>
<rect x="580" y="150" width="140" height="70" fill="none" stroke="#D9D9D9"/>
<text x="590" y="170" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555">病院↔家の境界消失</text>
<text x="590" y="185" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">医療=日常モニタ</text>
<text x="590" y="203" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">「治す」→「保つ」</text>

<!-- 行: 移動 -->
<rect x="40" y="220" width="120" height="70" fill="#F7F7F5" stroke="#121212" stroke-width="0.8"/>
<text x="100" y="258" font-family="Noto Sans JP, sans-serif" font-size="12" fill="#121212" text-anchor="middle" font-weight="700">移動</text>
<rect x="160" y="220" width="140" height="70" fill="none" stroke="#D9D9D9"/>
<text x="170" y="240" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555">L4 robotaxi 都市部</text>
<text x="170" y="255" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">Waymo/Cruise 系</text>
<text x="170" y="273" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">限定地域での実装</text>
<rect x="300" y="220" width="140" height="70" fill="none" stroke="#D9D9D9"/>
<text x="310" y="240" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555">L5 普及・私有減</text>
<text x="310" y="255" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">MaaS 主流化</text>
<text x="310" y="273" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">運転免許の意味変容</text>
<rect x="440" y="220" width="140" height="70" fill="none" stroke="#D9D9D9"/>
<text x="450" y="240" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555">空中モビリティ常用</text>
<text x="450" y="255" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">eVTOL 都市間</text>
<text x="450" y="273" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">2次元→3次元化</text>
<rect x="580" y="220" width="140" height="70" fill="none" stroke="#D9D9D9"/>
<text x="590" y="240" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555">居住地選択の自由化</text>
<text x="590" y="255" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">都市集中の緩和</text>
<text x="590" y="273" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">通勤概念の希薄化</text>

<!-- 行: 教育 -->
<rect x="40" y="290" width="120" height="70" fill="#F7F7F5" stroke="#121212" stroke-width="0.8"/>
<text x="100" y="328" font-family="Noto Sans JP, sans-serif" font-size="12" fill="#121212" text-anchor="middle" font-weight="700">教育</text>
<rect x="160" y="290" width="140" height="70" fill="none" stroke="#D9D9D9"/>
<text x="170" y="310" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555">AI個別チューター</text>
<text x="170" y="325" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">対話LLMが中心</text>
<text x="170" y="343" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">PCの延長</text>
<rect x="300" y="290" width="140" height="70" fill="none" stroke="#D9D9D9"/>
<text x="310" y="310" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555">身体性ある学習相手</text>
<text x="310" y="325" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">実験/工作/演奏伴走</text>
<text x="310" y="343" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">「触れて学ぶ」復権</text>
<rect x="440" y="290" width="140" height="70" fill="none" stroke="#D9D9D9"/>
<text x="450" y="310" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555">学校の機能再編</text>
<text x="450" y="325" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">知識伝達は外部委託</text>
<text x="450" y="343" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">関係性形成が中核</text>
<rect x="580" y="290" width="140" height="70" fill="none" stroke="#D9D9D9"/>
<text x="590" y="310" font-family="Noto Sans JP, sans-serif" font-size="9.5" fill="#555">生涯学習の常態化</text>
<text x="590" y="325" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">職業/学習の境界消失</text>
<text x="590" y="343" font-family="Noto Sans JP, sans-serif" font-size="9" fill="#999">学ぶ=生きる</text>

<text x="380" y="385" font-family="Noto Sans JP, sans-serif" font-size="10" fill="#6B6B6B" text-anchor="middle" font-style="italic">出典: AID-DB ロードマップ + FTT-DB 領域別予測 + AGI-DB 能力マイルストーン</text>
</svg>
<figcaption style="font-family:var(--font);font-size:0.78rem;color:#6B6B6B;margin-top:12px;text-align:center;">図 D5-5: 市民活用ガイド。家事・医療・移動・教育の4領域で、2030・2050・2080・2100の各時点に何が変わるかを学術論文ベースで限定。個人差・地域差は大きいが、構造的な方向性として参照可能。</figcaption>
</figure>
```

---

## 補足: ダークモード対応について

5図ともダークモード時の視認性を確保するため、以下の方針を採る:
1. **背景**: figure 外枠の `background:rgba(204,20,0,0.02)` は赤の極薄。ライト・ダークいずれでも紙地に馴染む
2. **罫線**: `stroke="#121212"` はダーク時 (背景 `#121212`) で消える可能性 → 既存25 SVGと同様、本設計でも `#121212` を保持（既存教科書のCSSが `.chapter-section svg { filter: invert(...) }` で一括反転を担う既存パターンを継承。新規SVGも同じ figure wrapping 内に置けば連動）
3. **赤アクセント**: `#CC1400` はダーク時に `#FF4030` 相当へCSS変数で再マップ可能。SVG内のhardcodeを minimize するため、主要アクセントは `#CC1400` で固定し、教科書側CSSの `[data-theme="dark"] figure svg [stroke="#CC1400"] { stroke: #FF4030 }` セレクタで上書き運用とする（QAチェックリストD4項目で検証）

---

## 統合チェックリスト

5図ともに以下を満たす:
- [x] viewBox 既存パターン準拠 (680/760 幅)
- [x] フォント Noto Sans JP のみ
- [x] 赤アクセント #CC1400 / 主軸 #121212 / 副 #555,#6B6B6B,#999
- [x] `<title>` + `<desc>` + `role="img"` でアクセシビリティ確保
- [x] `<figcaption>` で図注説明
- [x] figure wrapping で背景・上下罫線
- [x] 凡例配置 (時代軸/カテゴリ列見出し)

