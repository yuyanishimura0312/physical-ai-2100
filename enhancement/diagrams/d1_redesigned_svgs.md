# D1 図解再設計隊 — 既存15 SVG 完全再設計

**対象**: `/Users/nishimura+/projects/research/physical-ai-2100/output/index.html` の 15 SVG
**設計基準**: 赤白CI textbook.html style（`~/.claude/rules/db-design-system.md`）
**カラーパレット**:
- ライト: `--bg:#FFFFFF` / `--accent-warm:#CC1400` / `--text:#121212` / `--text-secondary:#555` / `--border:#D9D9D9`
- ダーク: `--bg:#121212` / `--accent-warm:#FF4030` / `--text:#E0E0E0` / `--text-secondary:#AAAAAA` / `--border:#333333`
- フォント: `Noto Sans JP`（UI/ラベル）/ `Noto Serif JP`（本文タイトル）

**全SVG 共通仕様**:
- `style="width:100%;max-width:760px;height:auto;display:block;margin:24px auto;"` を必須
- `<style>` ブロック内に `[data-theme="dark"]` selector を含めダークモード対応
- `aria-labelledby` でアクセシビリティ確保
- `role="img"` 必須

---

## 設計方針サマリ（15図解 → 統合 / 拡張 / 再設計 / 維持の判定）

| 図 | 判定 | 主な改善内容 |
|---|---|---|
| 図1-1 | 完全再設計 | 高原のシェード塗り・誤差バー・凡例追加・ダークモード対応 |
| 図2-1 | 完全再設計 | 5系統の色分け（warm gradient）、合流点の太赤丸+ノードラベル、不等間隔時間軸 |
| 図3-1 | 拡張 | 駆動矢印を太細で表現、stream_bio を 2-3層橋渡し、フィードバックループ赤点線追加 |
| 図4-1 | 統合（→図4-12 へ） | 図4-2 と統合した Phase A→B 動態 sankey/stack |
| 図4-2 | 完全再設計 | 線形等間隔時間軸、6マイルストーンの散布、stream 色分け、重複描画解消 |
| 図5-1 | 拡張 | 各層に代表モデル名・データフロー・出力次元、物理身体層との接続強化 |
| 図5-2 | 完全再設計 | Sankey 風で領域面積変化、人間/混成/AI の動的境界、矢印で「縮小・深化」明示 |
| 図6-1 | 完全再設計 | 「実線→点線→消失」で溶解可視化、マイルストーン点を時系列配置、赤ハッチ最終到達点 |
| 図6-2 | 拡張 | 円の大きさ＝知性規模、線の太さ＝接続強度、Active Inference 中心フィードバック |
| 図7-1 | 拡張 | 各ノードに実装事例（OpenVLA/AlphaFold/John Deere）、同期周波数縦線 |
| 図7-2 | 完全再設計 | 5段→3段濃淡、凡例追加、規制名+出典年併記 |
| 図8-1 | 完全再設計 | 同心円を時系列レイヤーに、半径＝時間軸、年代明示 |
| 図9-1 | 完全再設計 | ラジアル/タペストリー形式、横軸=時点・縦軸=5転換軸、各セル小型アイコン+色濃淡+駆動矢印 |
| 図14 | 完全再設計 | 4世代を時間軸、能力線で世代間連結、Chord diagram 風依存関係 |
| 図13 | 拡張 | Venn 図風重なり、中央交差領域に「関係論的存在論」、PHAI を中央寄り大きく描画 |

---

## 共通 `<style>` ブロック（全SVG先頭に挿入）

各 SVG 内に以下の `<style>` を含める。クラス名で色を抽象化することで、`[data-theme="dark"]` で一括上書きできる。

```svg
<style>
  .svg-bg { fill: #FFFFFF; }
  .svg-card { fill: #FFFFFF; }
  .svg-surface { fill: #F7F7F5; }
  .svg-ink { fill: #121212; }
  .svg-ink-soft { fill: #555555; }
  .svg-ink-mute { fill: #6B6B6B; }
  .svg-accent { fill: #CC1400; }
  .svg-accent-soft { fill: rgba(204,20,0,0.10); }
  .svg-accent-shade { fill: rgba(204,20,0,0.06); }
  .svg-stroke-ink { stroke: #121212; }
  .svg-stroke-soft { stroke: #555555; }
  .svg-stroke-accent { stroke: #CC1400; }
  .svg-stroke-border { stroke: #D9D9D9; }
  [data-theme="dark"] .svg-bg { fill: #121212; }
  [data-theme="dark"] .svg-card { fill: #1A1A1A; }
  [data-theme="dark"] .svg-surface { fill: #1A1A1A; }
  [data-theme="dark"] .svg-ink { fill: #E0E0E0; }
  [data-theme="dark"] .svg-ink-soft { fill: #AAAAAA; }
  [data-theme="dark"] .svg-ink-mute { fill: #8A8A8A; }
  [data-theme="dark"] .svg-accent { fill: #FF4030; }
  [data-theme="dark"] .svg-accent-soft { fill: rgba(255,64,48,0.14); }
  [data-theme="dark"] .svg-accent-shade { fill: rgba(255,64,48,0.08); }
  [data-theme="dark"] .svg-stroke-ink { stroke: #E0E0E0; }
  [data-theme="dark"] .svg-stroke-soft { stroke: #AAAAAA; }
  [data-theme="dark"] .svg-stroke-accent { stroke: #FF4030; }
  [data-theme="dark"] .svg-stroke-border { stroke: #333333; }
</style>
```

以下の各 SVG は上記 `<style>` が外側のグローバル CSS にあるものとして書く。SVG 単体で完結させたい場合は、各 SVG の冒頭にこの `<style>` を inline で挿入する。

---

## 図1-1（line 222）双子峰の高原モデル — 完全再設計

### 元 SVG 抜粋
```svg
<svg viewBox="0 0 680 360" ... style="width:100%;max-width:680px;height:auto;">
  <!-- 軸・折れ線（手書き風）・峰ラベル 0.764 / 0.768 のみ -->
</svg>
```

### 改善方針
- 高原（plateau）領域に半透明シェードを敷き、視認のアフォーダンスを向上
- 双子峰に上向きの誤差バー（±0.02）を付与し、CTI v2 の不確実性を表現
- X軸目盛りを実時間スケール（1750/1850/1900/1971/2017/2100）で配置、現在線（2026）を明示
- 凡例（低位定常 / 産業化 / 高位高原 / 双子峰）を右下に配置
- 「2026 年現在」を縦点線で図中央付近に貫通させる
- ダークモード対応

### 新 SVG 完全版
```svg
<svg viewBox="0 0 760 420" xmlns="http://www.w3.org/2000/svg" role="img"
     aria-labelledby="fig1-1-title fig1-1-desc"
     style="width:100%;max-width:760px;height:auto;display:block;margin:24px auto;">
  <title id="fig1-1-title">図1-1 双子峰の高原モデル（CTI v2, 1750-2100）</title>
  <desc id="fig1-1-desc">産業革命後の高原のうえに情報革命（前峰0.764）とAI革命/フィジカルAI（後峰0.768）が並び立つ双子峰モデル</desc>

  <!-- 背景 -->
  <rect class="svg-bg" x="0" y="0" width="760" height="420"/>

  <!-- タイトル -->
  <text x="380" y="28" class="svg-ink" font-family="Noto Sans JP" font-size="14" font-weight="700" text-anchor="middle">図1-1　双子峰の高原モデル（CTI v2 文明転換指数, 1750-2100）</text>
  <text x="380" y="46" class="svg-ink-mute" font-family="Noto Sans JP" font-size="11" text-anchor="middle">産業革命後の高位高原のうえに、情報革命とAI革命/フィジカルAIが双子峰として並ぶ</text>

  <!-- 高位高原シェード -->
  <rect class="svg-accent-shade" x="340" y="140" width="300" height="160"/>

  <!-- Y軸 -->
  <line class="svg-stroke-ink" x1="80" y1="80" x2="80" y2="340" stroke-width="1.5"/>
  <text x="68" y="84" class="svg-ink-soft" font-family="Noto Sans JP" font-size="11" text-anchor="end">高</text>
  <text x="68" y="345" class="svg-ink-soft" font-family="Noto Sans JP" font-size="11" text-anchor="end">低</text>
  <text x="50" y="200" class="svg-ink-soft" font-family="Noto Sans JP" font-size="11" text-anchor="middle" transform="rotate(-90 50 200)">CTI v2 文明転換指数</text>

  <!-- X軸 -->
  <line class="svg-stroke-ink" x1="80" y1="340" x2="700" y2="340" stroke-width="1.5"/>
  <g font-family="Noto Sans JP" font-size="11" class="svg-ink-soft" text-anchor="middle">
    <text x="100" y="362">1750</text>
    <text x="220" y="362">1850</text>
    <text x="330" y="362">1900</text>
    <text x="470" y="362">1971</text>
    <text x="570" y="362">2017</text>
    <text x="700" y="362">2100</text>
  </g>

  <!-- 補助 Y 目盛り -->
  <g class="svg-stroke-border" stroke-dasharray="2,3" stroke-width="0.6">
    <line x1="80" y1="180" x2="700" y2="180"/>
    <line x1="80" y1="240" x2="700" y2="240"/>
    <line x1="80" y1="300" x2="700" y2="300"/>
  </g>

  <!-- 折れ線 1: 低位定常 (1750-1850) -->
  <path d="M 100,310 L 220,300" fill="none" class="svg-stroke-soft" stroke-width="2.4"/>

  <!-- 折れ線 2: 第一次産業革命の登り (1850-1900) -->
  <path d="M 220,300 L 330,200" fill="none" class="svg-stroke-ink" stroke-width="2.4"/>

  <!-- 折れ線 3: 高位高原 (1900-1971) -->
  <path d="M 330,200 L 470,180" fill="none" class="svg-stroke-ink" stroke-width="2.4"/>

  <!-- 折れ線 4: 前峰 (1971-2010) -->
  <path d="M 470,180 L 510,120 L 545,170" fill="none" class="svg-stroke-accent" stroke-width="2.8"/>

  <!-- 折れ線 5: 高原の凹み (2010-2017) -->
  <path d="M 545,170 L 570,180" fill="none" class="svg-stroke-ink" stroke-width="2.4"/>

  <!-- 折れ線 6: 後峰 (2017-2100) 想定 -->
  <path d="M 570,180 L 625,110 L 700,160" fill="none" class="svg-stroke-accent" stroke-width="2.8" stroke-dasharray="0"/>

  <!-- 誤差バー: 前峰 -->
  <line class="svg-stroke-accent" x1="510" y1="105" x2="510" y2="135" stroke-width="1"/>
  <line class="svg-stroke-accent" x1="505" y1="105" x2="515" y2="105" stroke-width="1"/>
  <line class="svg-stroke-accent" x1="505" y1="135" x2="515" y2="135" stroke-width="1"/>

  <!-- 誤差バー: 後峰 -->
  <line class="svg-stroke-accent" x1="625" y1="95" x2="625" y2="125" stroke-width="1"/>
  <line class="svg-stroke-accent" x1="620" y1="95" x2="630" y2="95" stroke-width="1"/>
  <line class="svg-stroke-accent" x1="620" y1="125" x2="630" y2="125" stroke-width="1"/>

  <!-- 峰ラベル -->
  <g font-family="Noto Sans JP" text-anchor="middle">
    <text x="510" y="90" class="svg-accent" font-size="12" font-weight="700">前峰 0.764</text>
    <text x="510" y="68" class="svg-ink-mute" font-size="10">情報革命</text>
    <text x="510" y="55" class="svg-ink-mute" font-size="9">1971-2010</text>
    <text x="625" y="80" class="svg-accent" font-size="12" font-weight="700">後峰 0.768</text>
    <text x="625" y="60" class="svg-ink-mute" font-size="10">AI革命 / フィジカルAI</text>
    <text x="625" y="48" class="svg-ink-mute" font-size="9">2017-2100 予測</text>
  </g>

  <!-- 双子峰注釈 -->
  <line class="svg-stroke-accent" x1="510" y1="100" x2="625" y2="100" stroke-width="0.8" stroke-dasharray="3,3"/>
  <text x="568" y="96" class="svg-accent" font-family="Noto Sans JP" font-size="10" text-anchor="middle" font-style="italic">差 1.005 倍（ほぼ等高）</text>

  <!-- 高位高原ラベル -->
  <text x="395" y="220" class="svg-ink-mute" font-family="Noto Sans JP" font-size="10" text-anchor="middle" font-style="italic">産業化後の高位高原</text>

  <!-- 現在線 -->
  <line class="svg-stroke-accent" x1="585" y1="80" x2="585" y2="340" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="585" y="74" class="svg-accent" font-family="Noto Sans JP" font-size="10" text-anchor="middle" font-weight="700">2026 現在</text>

  <!-- 凡例 -->
  <g font-family="Noto Sans JP" font-size="10">
    <rect class="svg-card svg-stroke-border" x="100" y="378" width="600" height="32" stroke-width="1"/>
    <line class="svg-stroke-soft" x1="115" y1="395" x2="140" y2="395" stroke-width="2.4"/>
    <text x="148" y="398" class="svg-ink">低位定常</text>
    <line class="svg-stroke-ink" x1="220" y1="395" x2="245" y2="395" stroke-width="2.4"/>
    <text x="253" y="398" class="svg-ink">産業化／高原</text>
    <line class="svg-stroke-accent" x1="370" y1="395" x2="395" y2="395" stroke-width="2.8"/>
    <text x="403" y="398" class="svg-ink">双子峰</text>
    <rect class="svg-accent-shade" x="475" y="388" width="22" height="14"/>
    <text x="505" y="398" class="svg-ink">高位高原領域</text>
    <line class="svg-stroke-accent" x1="610" y1="388" x2="610" y2="402" stroke-width="1" stroke-dasharray="2,3"/>
    <text x="620" y="398" class="svg-ink">現在線</text>
  </g>
</svg>
```

---

## 図2-1（line 343）5系統合流の系譜 — 完全再設計

### 元 SVG 抜粋
```svg
<svg viewBox="0 0 680 380" ... >
  <!-- 5 本の線がほぼ平行に右側へ集約。色は灰色1+赤1 のみ。合流点が小円 1 つだけ -->
</svg>
```

### 改善方針
- 5 系統に赤系 warm gradient で異なる色相を割当て、識別性向上
- 各系統の発生年（1961/1955/2013/2002/2017）を線の起点とし、独立発展を時間軸で表現
- 合流点（2023-2026 RT-2/PaLM-E/OpenVLA/Open X-Embodiment）を太い赤丸 4 点で時系列に配置
- 不等間隔ではなく時間スケール上に正確配置（1950/1980/2000/2017/2023/2026）
- 凡例＋系統別代表モデル一覧を下部に追加

### 新 SVG 完全版
```svg
<svg viewBox="0 0 760 440" xmlns="http://www.w3.org/2000/svg" role="img"
     aria-labelledby="fig2-1-title fig2-1-desc"
     style="width:100%;max-width:760px;height:auto;display:block;margin:24px auto;">
  <title id="fig2-1-title">図2-1 5系統合流の系譜（1950-2026）</title>
  <desc id="fig2-1-desc">hw/ctrl/rl/sim/fm の5系統が独立に発展しVLA基盤モデルを介して2023-2026に合流</desc>

  <rect class="svg-bg" x="0" y="0" width="760" height="440"/>

  <text x="380" y="28" class="svg-ink" font-family="Noto Sans JP" font-size="14" font-weight="700" text-anchor="middle">図2-1　5系統合流の系譜（1950-2026）</text>
  <text x="380" y="46" class="svg-ink-mute" font-family="Noto Sans JP" font-size="11" text-anchor="middle">独立に発生した5系統が VLA 基盤モデルを介して合流し、単一身体のフィジカルAI へ収斂する</text>

  <!-- 時間軸 -->
  <line class="svg-stroke-ink" x1="80" y1="300" x2="700" y2="300" stroke-width="1.5"/>
  <g font-family="Noto Sans JP" font-size="10" class="svg-ink-soft" text-anchor="middle">
    <text x="100" y="318">1950</text>
    <text x="240" y="318">1980</text>
    <text x="380" y="318">2000</text>
    <text x="520" y="318">2017</text>
    <text x="610" y="318">2023</text>
    <text x="670" y="318">2026</text>
  </g>
  <g class="svg-stroke-soft" stroke-width="1">
    <line x1="100" y1="295" x2="100" y2="305"/>
    <line x1="240" y1="295" x2="240" y2="305"/>
    <line x1="380" y1="295" x2="380" y2="305"/>
    <line x1="520" y1="295" x2="520" y2="305"/>
    <line x1="610" y1="295" x2="610" y2="305"/>
    <line x1="670" y1="295" x2="670" y2="305"/>
  </g>

  <!-- 系統色（warm gradient: 濃赤→ピンク） -->
  <!-- stream_hw 1961起点 -->
  <path d="M 115,80 Q 280,82 480,88 Q 560,95 615,180" fill="none" stroke="#7A0A00" stroke-width="2.2"/>
  <circle cx="115" cy="80" r="4" fill="#7A0A00"/>
  <text x="125" y="74" class="svg-ink" font-family="Noto Sans JP" font-size="11" font-weight="700">stream_hw</text>
  <text x="125" y="89" font-family="Noto Sans JP" font-size="9" fill="#7A0A00">Unimate 1961 → ASIMO 2000 → Atlas Electric 2024</text>

  <!-- stream_ctrl 1955起点 -->
  <path d="M 108,120 Q 280,122 480,128 Q 555,135 615,190" fill="none" stroke="#9C1200" stroke-width="2.2"/>
  <circle cx="108" cy="120" r="4" fill="#9C1200"/>
  <text x="125" y="114" class="svg-ink" font-family="Noto Sans JP" font-size="11" font-weight="700">stream_ctrl</text>
  <text x="125" y="129" font-family="Noto Sans JP" font-size="9" fill="#9C1200">DH 1955 → Subsumption 1986 → Convex MPC 2018</text>

  <!-- stream_rl 1989 (DQN 2013) -->
  <path d="M 350,160 Q 450,165 530,175 Q 580,180 615,200" fill="none" stroke="#CC1400" stroke-width="2.4"/>
  <circle cx="350" cy="160" r="4" fill="#CC1400"/>
  <text x="360" y="154" class="svg-ink" font-family="Noto Sans JP" font-size="11" font-weight="700">stream_rl</text>
  <text x="360" y="169" font-family="Noto Sans JP" font-size="9" fill="#CC1400">Q-learning 1989 → DQN 2013 → PPO 2017 → Diffusion Policy 2023</text>

  <!-- stream_sim 2002 -->
  <path d="M 390,210 Q 470,212 530,215 Q 575,218 615,210" fill="none" stroke="#D85040" stroke-width="2.2"/>
  <circle cx="390" cy="210" r="4" fill="#D85040"/>
  <text x="400" y="204" class="svg-ink" font-family="Noto Sans JP" font-size="11" font-weight="700">stream_sim</text>
  <text x="400" y="219" font-family="Noto Sans JP" font-size="9" fill="#D85040">Gazebo 2002 → MuJoCo 2015 → Isaac Sim 2020 → Genesis 2024</text>

  <!-- stream_fm 2017 (Transformer) -->
  <path d="M 520,260 Q 555,255 585,250 Q 605,235 615,220" fill="none" stroke="#FF4030" stroke-width="3"/>
  <circle cx="520" cy="260" r="5" fill="#FF4030"/>
  <text x="530" y="254" class="svg-accent" font-family="Noto Sans JP" font-size="11" font-weight="700">stream_fm（駆動主軸）</text>
  <text x="530" y="269" font-family="Noto Sans JP" font-size="9" fill="#FF4030">Transformer 2017 → GPT-3 2020 → CLIP 2021 → PaLM-E/RT-2 2023 → OpenVLA 2024</text>

  <!-- 合流ノード 4点 -->
  <g>
    <circle cx="608" cy="200" r="14" fill="none" class="svg-stroke-accent" stroke-width="2"/>
    <circle cx="608" cy="200" r="4" class="svg-accent"/>
  </g>
  <text x="608" y="115" class="svg-accent" font-family="Noto Sans JP" font-size="10" text-anchor="middle" font-weight="700">2023 PaLM-E</text>
  <text x="608" y="128" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">マルチモーダル接地</text>

  <circle cx="635" cy="200" r="4" class="svg-accent"/>
  <text x="640" y="252" class="svg-accent" font-family="Noto Sans JP" font-size="10" font-weight="700">2023 RT-2</text>
  <text x="640" y="265" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9">VLA 初出</text>

  <circle cx="655" cy="200" r="4" class="svg-accent"/>
  <text x="660" y="115" class="svg-accent" font-family="Noto Sans JP" font-size="10" font-weight="700">2024 OpenVLA</text>
  <text x="660" y="128" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9">オープン化</text>

  <circle cx="670" cy="200" r="4" class="svg-accent"/>

  <!-- 合流帯シェード -->
  <rect class="svg-accent-shade" x="600" y="76" width="80" height="218"/>
  <text x="640" y="74" class="svg-accent" font-family="Noto Sans JP" font-size="10" text-anchor="middle" font-weight="700" font-style="italic">合流期 2023-2026</text>

  <!-- 単一身体（VLA）方向 -->
  <defs>
    <marker id="arrow-fig2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0,0 0,6 9,3" class="svg-accent"/>
    </marker>
  </defs>
  <line class="svg-stroke-accent" x1="680" y1="200" x2="720" y2="200" stroke-width="2" marker-end="url(#arrow-fig2)"/>
  <text x="725" y="195" class="svg-accent" font-family="Noto Sans JP" font-size="11" font-weight="700">VLA</text>
  <text x="725" y="208" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9">単一身体</text>

  <!-- 凡例 -->
  <rect class="svg-surface svg-stroke-border" x="80" y="345" width="620" height="78" stroke-width="1"/>
  <text x="92" y="362" class="svg-ink" font-family="Noto Sans JP" font-size="10" font-weight="700">凡例：</text>
  <g font-family="Noto Sans JP" font-size="9">
    <line x1="135" y1="358" x2="160" y2="358" stroke="#7A0A00" stroke-width="2.2"/>
    <text x="166" y="362" class="svg-ink">stream_hw（ハードウェア）</text>
    <line x1="135" y1="375" x2="160" y2="375" stroke="#9C1200" stroke-width="2.2"/>
    <text x="166" y="379" class="svg-ink">stream_ctrl（古典制御）</text>
    <line x1="135" y1="392" x2="160" y2="392" stroke="#CC1400" stroke-width="2.4"/>
    <text x="166" y="396" class="svg-ink">stream_rl（強化学習）</text>
    <line x1="135" y1="409" x2="160" y2="409" stroke="#D85040" stroke-width="2.2"/>
    <text x="166" y="413" class="svg-ink">stream_sim（シミュレータ）</text>
    <line x1="380" y1="358" x2="405" y2="358" stroke="#FF4030" stroke-width="3"/>
    <text x="411" y="362" class="svg-ink">stream_fm（基盤モデル, 駆動主軸）</text>
    <circle cx="395" cy="378" r="4" class="svg-accent"/>
    <text x="411" y="382" class="svg-ink">合流ノード（VLA 構成要素）</text>
    <rect class="svg-accent-shade" x="385" y="395" width="20" height="14"/>
    <text x="411" y="406" class="svg-ink">合流期帯 2023-2026</text>
  </g>
</svg>
```

---

## 図3-1（line 462）8系統の3層モデル — 拡張

### 改善方針
- 3層構造は維持しつつ駆動矢印を太細で表現（mat→hw/ctrl/sim 太、hw→学習層 細）
- stream_bio を 2-3 層に跨る橋構造で描く
- フィードバックループを赤点線で円環状に追加（fm → 物理層 → bio → fm）
- 各系統に代表事例を脚注的に併記
- ダークモード対応

### 新 SVG 完全版
```svg
<svg viewBox="0 0 760 460" xmlns="http://www.w3.org/2000/svg" role="img"
     aria-labelledby="fig3-1-title fig3-1-desc"
     style="width:100%;max-width:760px;height:auto;display:block;margin:24px auto;">
  <title id="fig3-1-title">図3-1 8系統の3層モデルと駆動順序</title>
  <desc id="fig3-1-desc">物理基盤層 stream_mat の上に実装層（hw/ctrl/sim）と学習・知能層（rl/fm/bio/cog）が積み上がる3層構造</desc>

  <rect class="svg-bg" x="0" y="0" width="760" height="460"/>

  <text x="380" y="28" class="svg-ink" font-family="Noto Sans JP" font-size="14" font-weight="700" text-anchor="middle">図3-1　8系統の3層構造と駆動順序</text>
  <text x="380" y="46" class="svg-ink-mute" font-family="Noto Sans JP" font-size="11" text-anchor="middle">赤＝Phase 2 で独立化された新系統（bio / mat / cog）。橋構造と赤点線フィードバックループが境界溶解を予兆する</text>

  <!-- 第三層 学習・知能層 -->
  <rect class="svg-card svg-stroke-accent" x="60" y="80" width="640" height="100" stroke-width="1.4" stroke-dasharray="5,3"/>
  <text x="76" y="100" class="svg-accent" font-family="Noto Sans JP" font-size="12" font-weight="700">第三層：学習・知能層</text>
  <text x="76" y="115" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9">機械に知性を注入。2010s後半から急発展</text>

  <!-- stream_rl -->
  <rect class="svg-card svg-stroke-ink" x="90" y="130" width="130" height="40" stroke-width="1"/>
  <text x="155" y="148" class="svg-ink" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="middle">stream_rl</text>
  <text x="155" y="162" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">DQN / PPO / DROID</text>

  <!-- stream_fm -->
  <rect class="svg-card svg-stroke-ink" x="240" y="130" width="130" height="40" stroke-width="1"/>
  <text x="305" y="148" class="svg-ink" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="middle">stream_fm</text>
  <text x="305" y="162" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">RT-2 / OpenVLA / π0</text>

  <!-- stream_bio (新) ─ 第二/第三層に跨る -->
  <rect class="svg-card svg-stroke-accent" x="390" y="130" width="150" height="120" stroke-width="1.8"/>
  <text x="465" y="148" class="svg-accent" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="middle">stream_bio（新）</text>
  <text x="465" y="162" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">Xenobot / Coscientist / A-Lab</text>
  <text x="465" y="200" class="svg-accent" font-family="Noto Sans JP" font-size="9" font-style="italic" text-anchor="middle">第二層と第三層の</text>
  <text x="465" y="213" class="svg-accent" font-family="Noto Sans JP" font-size="9" font-style="italic" text-anchor="middle">境界に位置</text>
  <text x="465" y="230" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">合成生物 + 自律実験</text>

  <!-- stream_cog (新) -->
  <rect class="svg-card svg-stroke-accent" x="560" y="130" width="130" height="40" stroke-width="1.5"/>
  <text x="625" y="148" class="svg-accent" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="middle">stream_cog（新）</text>
  <text x="625" y="162" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">World Model / BMI / JEPA</text>

  <!-- 第二層 実装層 -->
  <rect class="svg-card svg-stroke-ink" x="60" y="200" width="320" height="100" stroke-width="1.2"/>
  <rect class="svg-card svg-stroke-ink" x="555" y="200" width="145" height="100" stroke-width="1.2"/>
  <text x="76" y="220" class="svg-ink" font-family="Noto Sans JP" font-size="12" font-weight="700">第二層：実装層</text>
  <text x="76" y="235" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9">物理身体・制御・訓練環境。工学的成熟度が高い</text>

  <rect class="svg-card svg-stroke-ink" x="80" y="250" width="90" height="40" stroke-width="1"/>
  <text x="125" y="268" class="svg-ink" font-family="Noto Sans JP" font-size="10" font-weight="700" text-anchor="middle">stream_hw</text>
  <text x="125" y="282" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">Atlas / Digit / Optimus</text>

  <rect class="svg-card svg-stroke-ink" x="185" y="250" width="90" height="40" stroke-width="1"/>
  <text x="230" y="268" class="svg-ink" font-family="Noto Sans JP" font-size="10" font-weight="700" text-anchor="middle">stream_ctrl</text>
  <text x="230" y="282" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">MPC + RL hybrid</text>

  <rect class="svg-card svg-stroke-ink" x="290" y="250" width="80" height="40" stroke-width="1"/>
  <text x="330" y="268" class="svg-ink" font-family="Noto Sans JP" font-size="10" font-weight="700" text-anchor="middle">stream_sim</text>
  <text x="330" y="282" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">Isaac / Genesis</text>

  <!-- 第一層 物理基盤層 -->
  <rect class="svg-card svg-stroke-accent" x="60" y="320" width="640" height="60" stroke-width="1.8"/>
  <text x="76" y="340" class="svg-accent" font-family="Noto Sans JP" font-size="12" font-weight="700">第一層：物理基盤層</text>
  <text x="76" y="355" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9">他の全系統の物理的可能性を規定する</text>
  <text x="380" y="375" class="svg-accent" font-family="Noto Sans JP" font-size="11" text-anchor="middle" font-weight="700">stream_mat（新） ── 半導体・電池・太陽光・核分裂/融合・量子・新材料</text>

  <!-- 駆動矢印 (太線: mat→実装層) -->
  <defs>
    <marker id="arrow-fig3-thick" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0,0 0,6 9,3" class="svg-ink"/>
    </marker>
    <marker id="arrow-fig3-thin" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0,0 0,6 9,3" class="svg-ink-soft"/>
    </marker>
    <marker id="arrow-fig3-fb" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0,0 0,6 9,3" class="svg-accent"/>
    </marker>
  </defs>

  <!-- mat → 実装層 (太い駆動矢印 3本) -->
  <line class="svg-stroke-ink" x1="125" y1="318" x2="125" y2="295" stroke-width="2" marker-end="url(#arrow-fig3-thick)"/>
  <line class="svg-stroke-ink" x1="230" y1="318" x2="230" y2="295" stroke-width="2" marker-end="url(#arrow-fig3-thick)"/>
  <line class="svg-stroke-ink" x1="330" y1="318" x2="330" y2="295" stroke-width="2" marker-end="url(#arrow-fig3-thick)"/>

  <!-- 実装層 → 学習・知能層 (細い駆動矢印) -->
  <line class="svg-stroke-soft" x1="155" y1="245" x2="155" y2="175" stroke-width="1" stroke-dasharray="3,2"/>
  <line class="svg-stroke-soft" x1="305" y1="245" x2="305" y2="175" stroke-width="1" stroke-dasharray="3,2"/>

  <!-- bio bridge: 第二層から学習層へ縦に橋を描く -->
  <line class="svg-stroke-accent" x1="465" y1="250" x2="465" y2="250" stroke-width="0"/>
  <!-- bio 橋構造は rect で表現済 -->

  <!-- フィードバックループ (赤点線): fm → mat -->
  <path d="M 305,170 Q 250,150 90,175 Q 50,200 50,350 Q 50,395 300,395 Q 360,395 360,380"
        fill="none" class="svg-stroke-accent" stroke-width="1" stroke-dasharray="4,3"
        opacity="0.55" marker-end="url(#arrow-fig3-fb)"/>
  <text x="50" y="232" class="svg-accent" font-family="Noto Sans JP" font-size="9" font-style="italic"
        text-anchor="middle" transform="rotate(-90 50 232)">フィードバック</text>

  <!-- cog → bio 双方向 -->
  <line class="svg-stroke-accent" x1="560" y1="150" x2="540" y2="150" stroke-width="1" stroke-dasharray="2,2"/>

  <!-- 凡例 -->
  <rect class="svg-surface svg-stroke-border" x="60" y="400" width="640" height="50" stroke-width="1"/>
  <g font-family="Noto Sans JP" font-size="9">
    <line class="svg-stroke-ink" x1="75" y1="418" x2="98" y2="418" stroke-width="2" marker-end="url(#arrow-fig3-thick)"/>
    <text x="105" y="421" class="svg-ink">駆動（物理依存・太い）</text>
    <line class="svg-stroke-soft" x1="260" y1="418" x2="283" y2="418" stroke-width="1" stroke-dasharray="3,2"/>
    <text x="290" y="421" class="svg-ink">駆動（実装依存・細い）</text>
    <line class="svg-stroke-accent" x1="430" y1="418" x2="453" y2="418" stroke-width="1" stroke-dasharray="4,3" opacity="0.55"/>
    <text x="460" y="421" class="svg-ink">フィードバックループ（赤点線）</text>
    <rect class="svg-card svg-stroke-accent" x="75" y="430" width="22" height="14" stroke-width="1.5"/>
    <text x="105" y="442" class="svg-ink">Phase 2 新系統（赤縁）</text>
    <text x="430" y="442" class="svg-accent" font-style="italic">bio は第二/第三層の境界に位置（橋構造）</text>
  </g>
</svg>
```

---

## 図4-1（line 569）Phase A 5系統状態 — 図4-2 と統合

統合方針: 図4-1 は Phase A スナップショット、図4-2 は Phase B マイルストーン時系列。両者を「Phase A→B の連続的動態」として **Stacked stream chart（5系統の重みが時間で変化）** で 1 枚に統合。下記の図4-12 として新規 SVG 提示。

### 新 SVG 完全版（図4-12 統合版）
```svg
<svg viewBox="0 0 760 480" xmlns="http://www.w3.org/2000/svg" role="img"
     aria-labelledby="fig4-12-title fig4-12-desc"
     style="width:100%;max-width:760px;height:auto;display:block;margin:24px auto;">
  <title id="fig4-12-title">図4-12 Phase A→B における5系統の重み変化（2026-2040）</title>
  <desc id="fig4-12-desc">Phase A は stream_fm 主導、Phase B 中盤で5系統がほぼ均衡する</desc>

  <rect class="svg-bg" x="0" y="0" width="760" height="480"/>

  <text x="380" y="28" class="svg-ink" font-family="Noto Sans JP" font-size="14" font-weight="700" text-anchor="middle">図4-12　Phase A→B における5系統の重み変化（2026-2040）</text>
  <text x="380" y="46" class="svg-ink-mute" font-family="Noto Sans JP" font-size="11" text-anchor="middle">Phase A は stream_fm が主軸として駆動、Phase B 中盤で5系統がほぼ均衡しマイルストーンが集中する</text>

  <!-- X軸 -->
  <line class="svg-stroke-ink" x1="80" y1="300" x2="700" y2="300" stroke-width="1.5"/>
  <g font-family="Noto Sans JP" font-size="10" class="svg-ink-soft" text-anchor="middle">
    <text x="80" y="318">2026</text>
    <text x="180" y="318">2028</text>
    <text x="280" y="318">2030</text>
    <text x="380" y="318">2032</text>
    <text x="480" y="318">2034</text>
    <text x="580" y="318">2037</text>
    <text x="680" y="318">2040</text>
  </g>

  <!-- Phase 境界 -->
  <line class="svg-stroke-accent" x1="280" y1="80" x2="280" y2="300" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="180" y="76" class="svg-accent" font-family="Noto Sans JP" font-size="11" text-anchor="middle" font-weight="700">Phase A（2026-2030）</text>
  <text x="180" y="92" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">VLA基盤定着</text>
  <text x="480" y="76" class="svg-accent" font-family="Noto Sans JP" font-size="11" text-anchor="middle" font-weight="700">Phase B（2030-2040）</text>
  <text x="480" y="92" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">物理操作汎化</text>

  <!-- Stacked stream: 下から積み上げ
       hw / ctrl / sim / rl / fm の順、fm を最後に積む -->
  <!-- stream_hw -->
  <path d="M 80,300 L 80,290 Q 280,285 480,280 Q 580,278 680,275 L 680,300 Z"
        fill="#7A0A00" opacity="0.55"/>
  <text x="105" y="297" font-family="Noto Sans JP" font-size="9" fill="#FFFFFF" font-weight="700">hw</text>

  <!-- stream_ctrl -->
  <path d="M 80,290 L 80,275 Q 280,268 480,260 Q 580,255 680,250 L 680,275 Q 580,278 480,280 Q 280,285 80,290 Z"
        fill="#9C1200" opacity="0.6"/>
  <text x="105" y="285" font-family="Noto Sans JP" font-size="9" fill="#FFFFFF" font-weight="700">ctrl</text>

  <!-- stream_sim -->
  <path d="M 80,275 L 80,250 Q 280,238 480,225 Q 580,218 680,210 L 680,250 Q 580,255 480,260 Q 280,268 80,275 Z"
        fill="#D85040" opacity="0.65"/>
  <text x="105" y="265" font-family="Noto Sans JP" font-size="9" fill="#FFFFFF" font-weight="700">sim</text>

  <!-- stream_rl -->
  <path d="M 80,250 L 80,210 Q 280,195 480,180 Q 580,170 680,160 L 680,210 Q 580,218 480,225 Q 280,238 80,250 Z"
        fill="#CC1400" opacity="0.75"/>
  <text x="105" y="235" font-family="Noto Sans JP" font-size="9" fill="#FFFFFF" font-weight="700">rl</text>

  <!-- stream_fm (主軸・最も厚い) -->
  <path d="M 80,210 L 80,140 Q 180,128 280,125 Q 380,128 480,138 Q 580,148 680,140 L 680,160 Q 580,170 480,180 Q 280,195 80,210 Z"
        fill="#FF4030" opacity="0.85"/>
  <text x="180" y="180" font-family="Noto Sans JP" font-size="11" fill="#FFFFFF" font-weight="700" text-anchor="middle">stream_fm（主軸）</text>
  <text x="180" y="195" font-family="Noto Sans JP" font-size="9" fill="#FFFFFF" text-anchor="middle">RT-2 → OpenVLA → π0.5</text>

  <!-- Phase B マイルストーン（時系列散布） -->
  <g font-family="Noto Sans JP" font-size="9" class="svg-ink">
    <!-- Soft Robotics-RL 2031 -->
    <circle cx="330" cy="345" r="5" class="svg-accent"/>
    <line class="svg-stroke-accent" x1="330" y1="340" x2="330" y2="305" stroke-width="0.8"/>
    <text x="330" y="362" text-anchor="middle">Soft Robotics-RL</text>
    <text x="330" y="374" class="svg-ink-mute" font-size="8" text-anchor="middle">2031: 医療リハ量産</text>

    <!-- Lifelong VLA 2033 -->
    <circle cx="430" cy="345" r="5" class="svg-accent"/>
    <line class="svg-stroke-accent" x1="430" y1="340" x2="430" y2="305" stroke-width="0.8"/>
    <text x="430" y="362" text-anchor="middle">Lifelong VLA</text>
    <text x="430" y="374" class="svg-ink-mute" font-size="8" text-anchor="middle">2033: 連続学習</text>

    <!-- VLA非構造50% 2034 -->
    <circle cx="490" cy="345" r="5" class="svg-accent"/>
    <line class="svg-stroke-accent" x1="490" y1="340" x2="490" y2="305" stroke-width="0.8"/>
    <text x="490" y="362" text-anchor="middle">VLA 非構造 50%</text>
    <text x="490" y="374" class="svg-ink-mute" font-size="8" text-anchor="middle">2034: World Models 標準</text>

    <!-- Neuromorphic Edge 2035 -->
    <circle cx="540" cy="395" r="5" class="svg-accent"/>
    <line class="svg-stroke-accent" x1="540" y1="305" x2="540" y2="390" stroke-width="0.8"/>
    <text x="540" y="410" text-anchor="middle">Neuromorphic Edge</text>
    <text x="540" y="422" class="svg-ink-mute" font-size="8" text-anchor="middle">2035: 100mW級量産</text>

    <!-- 核融合 2037 -->
    <circle cx="600" cy="395" r="5" class="svg-accent"/>
    <line class="svg-stroke-accent" x1="600" y1="305" x2="600" y2="390" stroke-width="0.8"/>
    <text x="600" y="410" text-anchor="middle">核融合商用前実証</text>
    <text x="600" y="422" class="svg-ink-mute" font-size="8" text-anchor="middle">2037: CFS / Helion</text>

    <!-- 侵襲BMI 2039 -->
    <circle cx="660" cy="395" r="5" class="svg-accent"/>
    <line class="svg-stroke-accent" x1="660" y1="305" x2="660" y2="390" stroke-width="0.8"/>
    <text x="660" y="410" text-anchor="middle">侵襲型 BMI</text>
    <text x="660" y="422" class="svg-ink-mute" font-size="8" text-anchor="middle">2039: 重度障害標準</text>
  </g>

  <!-- Phase A 到達状態 注釈 -->
  <rect class="svg-surface svg-stroke-border" x="80" y="335" width="200" height="100" stroke-width="1"/>
  <text x="92" y="354" class="svg-ink" font-family="Noto Sans JP" font-size="10" font-weight="700">Phase A 末（2030）到達状態</text>
  <text x="92" y="372" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9">・狭義 AGI 到達予測点</text>
  <text x="98" y="385" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8">  Metaculus median / Khosla / Hassabis 2024</text>
  <text x="92" y="400" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9">・ヒューマノイド累計 100-200 万台</text>
  <text x="92" y="413" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9">・価格 2-5 万ドル</text>
  <text x="92" y="426" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9">・構造化作業で人件費競合点突破</text>

  <!-- 軸ラベル -->
  <text x="40" y="200" class="svg-ink-soft" font-family="Noto Sans JP" font-size="10" text-anchor="middle" transform="rotate(-90 40 200)">系統別の駆動寄与（積み上げ）</text>

  <!-- 凡例 -->
  <rect class="svg-surface svg-stroke-border" x="300" y="445" width="400" height="28" stroke-width="1"/>
  <g font-family="Noto Sans JP" font-size="9">
    <rect x="310" y="453" width="14" height="12" fill="#7A0A00" opacity="0.55"/>
    <text x="328" y="463" class="svg-ink">hw</text>
    <rect x="354" y="453" width="14" height="12" fill="#9C1200" opacity="0.6"/>
    <text x="372" y="463" class="svg-ink">ctrl</text>
    <rect x="402" y="453" width="14" height="12" fill="#D85040" opacity="0.65"/>
    <text x="420" y="463" class="svg-ink">sim</text>
    <rect x="450" y="453" width="14" height="12" fill="#CC1400" opacity="0.75"/>
    <text x="468" y="463" class="svg-ink">rl</text>
    <rect x="495" y="453" width="14" height="12" fill="#FF4030" opacity="0.85"/>
    <text x="513" y="463" class="svg-ink">fm（主軸）</text>
    <circle cx="595" cy="459" r="4" class="svg-accent"/>
    <text x="605" y="463" class="svg-ink">Phase B マイルストーン</text>
  </g>
</svg>
```

---

## 図4-2（line 631）Phase B マイルストーン時系列 — 図4-12 で統合解消

図4-12 に統合済。図4-2 単独としてはこのファイル中で扱わない（重複描画を解消）。元の図4-2 は HTML から削除し、図4-12 のみを置く運用とする。

---

## 図5-1（line 728）Cognitive Stack 4層 — 拡張

### 改善方針
- 各層に代表モデル名・データフロー矢印・入出力次元を追記
- 物理身体層との接続を 4 本の細線+ラベルで強化
- 各層の右側に「2045年標準化想定の特性」を併記
- ダークモード対応

### 新 SVG 完全版
```svg
<svg viewBox="0 0 760 460" xmlns="http://www.w3.org/2000/svg" role="img"
     aria-labelledby="fig5-1-title fig5-1-desc"
     style="width:100%;max-width:760px;height:auto;display:block;margin:24px auto;">
  <title id="fig5-1-title">図5-1 Cognitive Stack（2045年標準化予測）</title>
  <desc id="fig5-1-desc">ロボットOSのカーネル層に組み込まれる4層認知アーキテクチャと物理身体層との接続</desc>

  <rect class="svg-bg" x="0" y="0" width="760" height="460"/>

  <text x="380" y="28" class="svg-ink" font-family="Noto Sans JP" font-size="14" font-weight="700" text-anchor="middle">図5-1　Cognitive Stack（2045年標準化予測）</text>
  <text x="380" y="46" class="svg-ink-mute" font-family="Noto Sans JP" font-size="11" text-anchor="middle">ロボットOS のカーネル層に組み込まれる 4 層認知アーキテクチャ + 物理身体層</text>

  <!-- Layer 4: 記号推論 -->
  <rect class="svg-card svg-stroke-accent" x="150" y="80" width="460" height="60" stroke-width="2"/>
  <text x="170" y="103" class="svg-accent" font-family="Noto Sans JP" font-size="12" font-weight="700">Layer 4　記号推論層</text>
  <text x="170" y="120" class="svg-ink-mute" font-family="Noto Sans JP" font-size="10">論理計画・抽象推論・言語理解</text>
  <text x="170" y="134" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9">代表: LLM successor（GPT-7 級 / Gemini Ultra successor / Claude N 系統）</text>
  <text x="600" y="103" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="end" font-style="italic">→ symbolic tokens</text>
  <text x="600" y="118" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="end">出力: 100-1000 tokens/s</text>

  <!-- Layer 3: Active Inference -->
  <rect class="svg-card svg-stroke-ink" x="150" y="155" width="460" height="60" stroke-width="1.5"/>
  <text x="170" y="178" class="svg-ink" font-family="Noto Sans JP" font-size="12" font-weight="700">Layer 3　Active Inference 層</text>
  <text x="170" y="195" class="svg-ink-mute" font-family="Noto Sans JP" font-size="10">自由エネルギー最小化・予測符号化</text>
  <text x="170" y="209" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9">代表: Friston FEP 系統（1995-2050）／Pezzulo 系統</text>
  <text x="600" y="178" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="end" font-style="italic">→ belief update</text>
  <text x="600" y="193" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="end">出力: 10-100 Hz</text>

  <!-- Layer 2: World Model -->
  <rect class="svg-card svg-stroke-ink" x="150" y="230" width="460" height="60" stroke-width="1.5"/>
  <text x="170" y="253" class="svg-ink" font-family="Noto Sans JP" font-size="12" font-weight="700">Layer 2　World Model 層</text>
  <text x="170" y="270" class="svg-ink-mute" font-family="Noto Sans JP" font-size="10">内部シミュレーション・動学予測</text>
  <text x="170" y="284" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9">代表: DreamerV5+ / Genie successor / Sora successor / Cosmos</text>
  <text x="600" y="253" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="end" font-style="italic">→ predicted states</text>
  <text x="600" y="268" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="end">出力: 30-120 fps</text>

  <!-- Layer 1: VLA -->
  <rect class="svg-card svg-stroke-ink" x="150" y="305" width="460" height="60" stroke-width="1.5"/>
  <text x="170" y="328" class="svg-ink" font-family="Noto Sans JP" font-size="12" font-weight="700">Layer 1　VLA 層</text>
  <text x="170" y="345" class="svg-ink-mute" font-family="Noto Sans JP" font-size="10">視覚-言語-行動マッピング</text>
  <text x="170" y="359" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9">代表: OpenVLA 系譜の成熟形（π0.7 / RT-X / GR00T N）</text>
  <text x="600" y="328" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="end" font-style="italic">→ motor commands</text>
  <text x="600" y="343" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="end">出力: 100-1000 Hz</text>

  <!-- 層間データフロー（双方向） -->
  <defs>
    <marker id="arrow-fig5-down" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0,0 0,6 6,3" class="svg-ink-soft"/>
    </marker>
    <marker id="arrow-fig5-up" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0,0 0,6 6,3" class="svg-accent"/>
    </marker>
  </defs>
  <!-- 下向き: トップダウン制御 -->
  <line class="svg-stroke-soft" x1="340" y1="140" x2="340" y2="153" stroke-width="1.2" marker-end="url(#arrow-fig5-down)"/>
  <line class="svg-stroke-soft" x1="340" y1="215" x2="340" y2="228" stroke-width="1.2" marker-end="url(#arrow-fig5-down)"/>
  <line class="svg-stroke-soft" x1="340" y1="290" x2="340" y2="303" stroke-width="1.2" marker-end="url(#arrow-fig5-down)"/>
  <!-- 上向き: 感覚情報 -->
  <line class="svg-stroke-accent" x1="420" y1="305" x2="420" y2="292" stroke-width="1.2" marker-end="url(#arrow-fig5-up)"/>
  <line class="svg-stroke-accent" x1="420" y1="230" x2="420" y2="217" stroke-width="1.2" marker-end="url(#arrow-fig5-up)"/>
  <line class="svg-stroke-accent" x1="420" y1="155" x2="420" y2="142" stroke-width="1.2" marker-end="url(#arrow-fig5-up)"/>

  <!-- 物理身体層 -->
  <rect class="svg-surface svg-stroke-border" x="80" y="390" width="600" height="50" stroke-width="1.2"/>
  <text x="380" y="410" class="svg-ink" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="middle">物理身体 / アクチュエータ / センサ（stream_hw + stream_mat + stream_bio）</text>
  <text x="380" y="428" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">触覚（Tac3D）・筋電（EMG）・前庭（IMU）・力覚（F/T sensor）・視覚（RGB-D + イベントカメラ）</text>

  <!-- VLA ↔ 物理身体: 4 本接続 -->
  <line class="svg-stroke-accent" x1="220" y1="365" x2="220" y2="390" stroke-width="1.4"/>
  <line class="svg-stroke-accent" x1="320" y1="365" x2="320" y2="390" stroke-width="1.4"/>
  <line class="svg-stroke-accent" x1="420" y1="365" x2="420" y2="390" stroke-width="1.4"/>
  <line class="svg-stroke-accent" x1="520" y1="365" x2="520" y2="390" stroke-width="1.4"/>
  <text x="170" y="382" class="svg-accent" font-family="Noto Sans JP" font-size="9" text-anchor="middle" font-style="italic">motor</text>
  <text x="270" y="382" class="svg-accent" font-family="Noto Sans JP" font-size="9" text-anchor="middle" font-style="italic">force</text>
  <text x="370" y="382" class="svg-accent" font-family="Noto Sans JP" font-size="9" text-anchor="middle" font-style="italic">vision</text>
  <text x="470" y="382" class="svg-accent" font-family="Noto Sans JP" font-size="9" text-anchor="middle" font-style="italic">tactile</text>

  <!-- 凡例 -->
  <g font-family="Noto Sans JP" font-size="9">
    <line class="svg-stroke-soft" x1="80" y1="100" x2="100" y2="100" stroke-width="1.2" marker-end="url(#arrow-fig5-down)"/>
    <text x="105" y="103" class="svg-ink">トップダウン制御</text>
    <line class="svg-stroke-accent" x1="80" y1="118" x2="100" y2="118" stroke-width="1.2" marker-end="url(#arrow-fig5-up)"/>
    <text x="105" y="121" class="svg-ink">感覚情報</text>
  </g>
</svg>
```

---

## 図5-2（line 776）人間-AI 分業構造 — 完全再設計（Sankey 風）

### 改善方針
- 6 矩形→ Sankey 風領域面積変化
- Phase C → Phase D で人間が縮小・深化、AI が拡大、共同探索が中間に増加
- 矢印を「縮小／深化／拡大」の 3 種類で明示
- 各領域に動詞ラベル（戦略する / 探究する / 自律実行する）追加
- 認識転換注釈をプルクオートとして配置

### 新 SVG 完全版
```svg
<svg viewBox="0 0 760 420" xmlns="http://www.w3.org/2000/svg" role="img"
     aria-labelledby="fig5-2-title fig5-2-desc"
     style="width:100%;max-width:760px;height:auto;display:block;margin:24px auto;">
  <title id="fig5-2-title">図5-2 Phase C-D 人間-AI 分業構造の変化（領域面積）</title>
  <desc id="fig5-2-desc">Phase C から Phase D へ、人間領域は縮小・深化し、AI領域は拡大、共同探索領域が中間に成長する</desc>

  <rect class="svg-bg" x="0" y="0" width="760" height="420"/>

  <text x="380" y="28" class="svg-ink" font-family="Noto Sans JP" font-size="14" font-weight="700" text-anchor="middle">図5-2　Phase C-D における人間-AI 分業構造の変化</text>
  <text x="380" y="46" class="svg-ink-mute" font-family="Noto Sans JP" font-size="11" text-anchor="middle">領域の縦幅 = 担う作業量。Phase C→D で人間領域は縮小・深化、AI領域は拡大</text>

  <!-- フェーズ見出し -->
  <text x="190" y="76" class="svg-accent" font-family="Noto Sans JP" font-size="12" font-weight="700" text-anchor="middle">Phase C（2040-2050）</text>
  <text x="190" y="92" class="svg-ink-mute" font-family="Noto Sans JP" font-size="10" text-anchor="middle">人間-AI 並走期</text>
  <text x="570" y="76" class="svg-accent" font-family="Noto Sans JP" font-size="12" font-weight="700" text-anchor="middle">Phase D（2050-2060）</text>
  <text x="570" y="92" class="svg-ink-mute" font-family="Noto Sans JP" font-size="10" text-anchor="middle">自律物理エージェント期</text>

  <!-- Phase C 縦長領域 (左) - 領域面積は均等寄り -->
  <!-- 人間の領域 (Phase C: 大きめ) -->
  <rect class="svg-card svg-stroke-accent" x="60" y="110" width="260" height="80" stroke-width="1.8"/>
  <text x="190" y="135" class="svg-accent" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="middle">人間の領域</text>
  <text x="190" y="152" class="svg-ink-soft" font-family="Noto Sans JP" font-size="10" text-anchor="middle">戦略 ・ 倫理 ・ 統合判断 ・ 例外対応</text>
  <text x="190" y="170" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">動詞: 戦略する / 判断する</text>
  <text x="190" y="184" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">担当: 全作業の 25%</text>

  <!-- 混成チームの領域 (Phase C) -->
  <rect class="svg-card svg-stroke-ink" x="60" y="200" width="260" height="60" stroke-width="1.5"/>
  <text x="190" y="222" class="svg-ink" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="middle">混成チームの領域</text>
  <text x="190" y="239" class="svg-ink-soft" font-family="Noto Sans JP" font-size="10" text-anchor="middle">人間 1 + ロボット数体の協働</text>
  <text x="190" y="254" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">担当: 全作業の 30%</text>

  <!-- AI の領域 (Phase C: 中) -->
  <rect class="svg-card svg-stroke-ink" x="60" y="270" width="260" height="100" stroke-width="1.5"/>
  <text x="190" y="295" class="svg-ink" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="middle">AI の領域</text>
  <text x="190" y="312" class="svg-ink-soft" font-family="Noto Sans JP" font-size="10" text-anchor="middle">構造化作業 ・ パターン業務</text>
  <text x="190" y="328" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">動詞: 自律実行する</text>
  <text x="190" y="345" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">担当: 全作業の 45%</text>

  <!-- 遷移帯（Sankey 風）- 人間領域は縮小 -->
  <path d="M 320,110 L 440,110 L 440,150 L 320,190 Z" class="svg-accent-soft"/>
  <!-- 混成領域は拡大（共同探索へ） -->
  <path d="M 320,200 L 440,150 L 440,210 L 320,260 Z" class="svg-accent-shade"/>
  <!-- AI領域は拡大 -->
  <path d="M 320,270 L 440,210 L 440,380 L 320,370 Z" class="svg-accent-shade"/>

  <!-- Phase D 縦長領域 (右) -->
  <!-- 人間の領域 (Phase D: 縮小・深化) -->
  <rect class="svg-card svg-stroke-accent" x="440" y="110" width="260" height="40" stroke-width="2.2"/>
  <text x="570" y="128" class="svg-accent" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="middle">人間の領域（縮小・深化）</text>
  <text x="570" y="143" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="middle">意味付け ・ 価値設計 ・ 他者ケア ・ 創造</text>

  <!-- 共同探索 (Phase D: 拡大) -->
  <rect class="svg-card svg-stroke-ink" x="440" y="160" width="260" height="50" stroke-width="1.5"/>
  <text x="570" y="180" class="svg-ink" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="middle">共同探索の領域</text>
  <text x="570" y="195" class="svg-ink-soft" font-family="Noto Sans JP" font-size="10" text-anchor="middle">未踏領域の探究 ・ 倫理設計</text>

  <!-- AI の領域 (Phase D: 拡大) -->
  <rect class="svg-card svg-stroke-ink" x="440" y="220" width="260" height="160" stroke-width="1.5"/>
  <text x="570" y="244" class="svg-ink" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="middle">AI の領域（拡大）</text>
  <text x="570" y="262" class="svg-ink-soft" font-family="Noto Sans JP" font-size="10" text-anchor="middle">自律エージェント組織 ・ 大半の実務</text>
  <text x="570" y="278" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">動詞: 自律統治する</text>
  <text x="570" y="295" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">担当: 全作業の 65%</text>
  <!-- AI領域内アイコン的補足 -->
  <line class="svg-stroke-soft" x1="460" y1="310" x2="680" y2="310" stroke-width="0.5" stroke-dasharray="2,2"/>
  <text x="570" y="328" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">・ヒューマノイド軍管理</text>
  <text x="570" y="344" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">・分散ファクトリ運営</text>
  <text x="570" y="360" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">・自律科学実験</text>

  <!-- 動詞 注釈 -->
  <text x="380" y="105" class="svg-accent" font-family="Noto Sans JP" font-size="10" text-anchor="middle" font-style="italic">縮小・深化 →</text>
  <text x="380" y="200" class="svg-accent" font-family="Noto Sans JP" font-size="10" text-anchor="middle" font-style="italic">→ 共同探索が成長</text>
  <text x="380" y="325" class="svg-accent" font-family="Noto Sans JP" font-size="10" text-anchor="middle" font-style="italic">拡大 →</text>

  <!-- プルクオート -->
  <rect class="svg-surface svg-stroke-accent" x="80" y="392" width="600" height="22" stroke-width="1"/>
  <text x="380" y="408" class="svg-ink" font-family="Noto Sans JP" font-size="10" text-anchor="middle" font-weight="700" font-style="italic">「AGI に置き換えられた」のではなく「AGI が下層を担うようになった」という認識転換</text>
</svg>
```

---

## 図6-1（line 866）三境界溶解 — 完全再設計

### 改善方針
- 3 本の帯を「実線→点線→消失（フェードアウト）」のグラデで溶解可視化
- 各帯に 4-6 個のマイルストーン点を時系列に配置
- 最終到達点（2100）を右端に赤いハッチ領域として描く
- 時間軸 Phase E/F/G の境界を縦線で明示
- ダークモード対応

### 新 SVG 完全版
```svg
<svg viewBox="0 0 760 460" xmlns="http://www.w3.org/2000/svg" role="img"
     aria-labelledby="fig6-1-title fig6-1-desc"
     style="width:100%;max-width:760px;height:auto;display:block;margin:24px auto;">
  <title id="fig6-1-title">図6-1 Phase E-G を貫く三つの境界溶解</title>
  <desc id="fig6-1-desc">機械/生命・主体/環境・個体/群の3境界が2060-2100の間に段階的に溶解する</desc>

  <defs>
    <linearGradient id="dissolve-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#CC1400" stop-opacity="1"/>
      <stop offset="40%" stop-color="#CC1400" stop-opacity="0.7"/>
      <stop offset="75%" stop-color="#CC1400" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#CC1400" stop-opacity="0.1"/>
    </linearGradient>
    <linearGradient id="dissolve-grad-dark" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF4030" stop-opacity="1"/>
      <stop offset="40%" stop-color="#FF4030" stop-opacity="0.7"/>
      <stop offset="75%" stop-color="#FF4030" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#FF4030" stop-opacity="0.1"/>
    </linearGradient>
    <pattern id="dissolve-hatch" patternUnits="userSpaceOnUse" width="6" height="6" patternTransform="rotate(45)">
      <rect width="2" height="6" class="svg-accent"/>
    </pattern>
  </defs>

  <rect class="svg-bg" x="0" y="0" width="760" height="460"/>

  <text x="380" y="28" class="svg-ink" font-family="Noto Sans JP" font-size="14" font-weight="700" text-anchor="middle">図6-1　Phase E-G を貫く三つの境界溶解</text>
  <text x="380" y="46" class="svg-ink-mute" font-family="Noto Sans JP" font-size="11" text-anchor="middle">機械/生命 ・ 主体/環境 ・ 個体/群 の 3 境界が段階的に溶解（実線→点線→消失→赤ハッチ最終到達点）</text>

  <!-- Phase 境界縦線 -->
  <line class="svg-stroke-border" x1="280" y1="80" x2="280" y2="380" stroke-width="0.8" stroke-dasharray="2,2"/>
  <line class="svg-stroke-border" x1="500" y1="80" x2="500" y2="380" stroke-width="0.8" stroke-dasharray="2,2"/>

  <!-- 時間軸 -->
  <line class="svg-stroke-ink" x1="80" y1="380" x2="700" y2="380" stroke-width="1.5"/>
  <g font-family="Noto Sans JP" font-size="11" class="svg-accent" text-anchor="middle" font-weight="700">
    <text x="120" y="402">2060</text>
    <text x="280" y="402">2075</text>
    <text x="500" y="402">2090</text>
    <text x="680" y="402">2100</text>
  </g>
  <g font-family="Noto Sans JP" font-size="10" class="svg-ink-soft" text-anchor="middle">
    <text x="200" y="420">Phase E</text>
    <text x="390" y="420">Phase F</text>
    <text x="590" y="420">Phase G</text>
  </g>

  <!-- 境界1: 機械と生命 -->
  <text x="86" y="100" class="svg-accent" font-family="Noto Sans JP" font-size="11" font-weight="700">境界1: 機械と生命</text>
  <!-- 実線部 -->
  <line class="svg-stroke-accent" x1="120" y1="120" x2="280" y2="120" stroke-width="3"/>
  <!-- 点線部 -->
  <line class="svg-stroke-accent" x1="280" y1="120" x2="500" y2="120" stroke-width="2.5" stroke-dasharray="6,4" opacity="0.7"/>
  <!-- 消失部（点列） -->
  <line class="svg-stroke-accent" x1="500" y1="120" x2="640" y2="120" stroke-width="2" stroke-dasharray="2,6" opacity="0.4"/>
  <!-- 赤ハッチ最終到達点 -->
  <rect x="640" y="112" width="40" height="16" fill="url(#dissolve-hatch)" opacity="0.7"/>
  <!-- マイルストーン点 -->
  <circle cx="140" cy="120" r="4" class="svg-accent"/>
  <text x="140" y="143" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="middle">Soft Robotics 量産</text>
  <circle cx="240" cy="120" r="4" class="svg-accent"/>
  <text x="240" y="143" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="middle">Bio-Hybrid</text>
  <circle cx="370" cy="120" r="4" class="svg-accent" opacity="0.7"/>
  <text x="370" y="143" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="middle">Living Factory</text>
  <circle cx="540" cy="120" r="4" class="svg-accent" opacity="0.5"/>
  <text x="540" y="143" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="middle">日用品化</text>
  <text x="660" y="105" class="svg-accent" font-family="Noto Sans JP" font-size="9" text-anchor="middle" font-weight="700">溶解</text>

  <!-- 境界2: 主体と環境 -->
  <text x="86" y="180" class="svg-accent" font-family="Noto Sans JP" font-size="11" font-weight="700">境界2: 主体と環境</text>
  <line class="svg-stroke-accent" x1="120" y1="200" x2="280" y2="200" stroke-width="3"/>
  <line class="svg-stroke-accent" x1="280" y1="200" x2="500" y2="200" stroke-width="2.5" stroke-dasharray="6,4" opacity="0.7"/>
  <line class="svg-stroke-accent" x1="500" y1="200" x2="640" y2="200" stroke-width="2" stroke-dasharray="2,6" opacity="0.4"/>
  <rect x="640" y="192" width="40" height="16" fill="url(#dissolve-hatch)" opacity="0.7"/>
  <circle cx="140" cy="200" r="4" class="svg-accent"/>
  <text x="140" y="223" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="middle">BMI 普及</text>
  <circle cx="240" cy="200" r="4" class="svg-accent"/>
  <text x="240" y="223" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="middle">拡張認知</text>
  <circle cx="370" cy="200" r="4" class="svg-accent" opacity="0.7"/>
  <text x="370" y="223" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="middle">インフラ化</text>
  <circle cx="540" cy="200" r="4" class="svg-accent" opacity="0.5"/>
  <text x="540" y="223" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="middle">輪郭流動化</text>
  <text x="660" y="185" class="svg-accent" font-family="Noto Sans JP" font-size="9" text-anchor="middle" font-weight="700">溶解</text>

  <!-- 境界3: 個体と群 -->
  <text x="86" y="260" class="svg-accent" font-family="Noto Sans JP" font-size="11" font-weight="700">境界3: 個体と群</text>
  <line class="svg-stroke-accent" x1="120" y1="280" x2="280" y2="280" stroke-width="3"/>
  <line class="svg-stroke-accent" x1="280" y1="280" x2="500" y2="280" stroke-width="2.5" stroke-dasharray="6,4" opacity="0.7"/>
  <line class="svg-stroke-accent" x1="500" y1="280" x2="640" y2="280" stroke-width="2" stroke-dasharray="2,6" opacity="0.4"/>
  <rect x="640" y="272" width="40" height="16" fill="url(#dissolve-hatch)" opacity="0.7"/>
  <circle cx="140" cy="280" r="4" class="svg-accent"/>
  <text x="140" y="303" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="middle">単一 AGI</text>
  <circle cx="240" cy="280" r="4" class="svg-accent"/>
  <text x="240" y="303" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="middle">多様知性編成</text>
  <circle cx="370" cy="280" r="4" class="svg-accent" opacity="0.7"/>
  <text x="370" y="303" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="middle">ambient embodiment</text>
  <circle cx="540" cy="280" r="4" class="svg-accent" opacity="0.5"/>
  <text x="540" y="303" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="middle">境界溶解点</text>
  <text x="660" y="265" class="svg-accent" font-family="Noto Sans JP" font-size="9" text-anchor="middle" font-weight="700">溶解</text>

  <!-- 最終到達点注釈 -->
  <line class="svg-stroke-accent" x1="660" y1="320" x2="660" y2="338" stroke-width="0.8"/>
  <text x="660" y="332" class="svg-accent" font-family="Noto Sans JP" font-size="9" text-anchor="middle" font-style="italic">2100 到達点</text>

  <!-- 凡例 -->
  <rect class="svg-surface svg-stroke-border" x="80" y="430" width="600" height="22" stroke-width="1"/>
  <g font-family="Noto Sans JP" font-size="9">
    <line class="svg-stroke-accent" x1="92" y1="441" x2="118" y2="441" stroke-width="3"/>
    <text x="124" y="445" class="svg-ink">実線（明瞭）</text>
    <line class="svg-stroke-accent" x1="200" y1="441" x2="226" y2="441" stroke-width="2.5" stroke-dasharray="6,4" opacity="0.7"/>
    <text x="232" y="445" class="svg-ink">点線（揺らぎ）</text>
    <line class="svg-stroke-accent" x1="320" y1="441" x2="346" y2="441" stroke-width="2" stroke-dasharray="2,6" opacity="0.4"/>
    <text x="352" y="445" class="svg-ink">消失（溶解進行）</text>
    <rect x="450" y="434" width="26" height="14" fill="url(#dissolve-hatch)" opacity="0.7"/>
    <text x="482" y="445" class="svg-ink">最終到達点 2100（境界溶解点）</text>
  </g>

  <!-- finding box -->
  <rect class="svg-accent-shade" x="80" y="60" width="600" height="20"/>
  <text x="380" y="74" class="svg-accent" font-family="Noto Sans JP" font-size="10" text-anchor="middle" font-weight="700" font-style="italic">フィジカルAI は他の AI 形態（LLM・生体AI・量子AI・分散AI）と区別不能になる</text>
</svg>
```

---

## 図6-2（line 929）知性のオーケストラ — 拡張

### 改善方針
- 円の大きさ＝知性の規模で差を付ける（人間=小, 古典AI=大, 身体性AI=中など）
- 線の太さ＝接続強度を表す（中央 ↔ 古典AI が最も太い）
- Active Inference のフィードバック構造を中心に矢印で追加
- 主導権交替の方向を時間軸で示す矢印を周囲に
- 各円に「貢献領域」を 1 行追記

### 新 SVG 完全版
```svg
<svg viewBox="0 0 760 440" xmlns="http://www.w3.org/2000/svg" role="img"
     aria-labelledby="fig6-2-title fig6-2-desc"
     style="width:100%;max-width:760px;height:auto;display:block;margin:24px auto;">
  <title id="fig6-2-title">図6-2 2100年「知性のオーケストラ」の構造</title>
  <desc id="fig6-2-desc">中央の関係論的物理生態系を6種類の知性が異なる規模と接続強度で囲む</desc>

  <defs>
    <marker id="arrow-fig62-fb" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0,0 0,6 6,3" class="svg-accent"/>
    </marker>
  </defs>

  <rect class="svg-bg" x="0" y="0" width="760" height="440"/>

  <text x="380" y="28" class="svg-ink" font-family="Noto Sans JP" font-size="14" font-weight="700" text-anchor="middle">図6-2　2100年「知性のオーケストラ」の構造</text>
  <text x="380" y="46" class="svg-ink-mute" font-family="Noto Sans JP" font-size="11" text-anchor="middle">円の大きさ = 知性の規模 / 線の太さ = 接続強度 / 中央に Active Inference のフィードバック構造</text>

  <!-- 中央：関係論的物理生態系 -->
  <circle cx="380" cy="220" r="62" class="svg-card svg-stroke-accent" stroke-width="2.4"/>
  <text x="380" y="214" class="svg-accent" font-family="Noto Sans JP" font-size="12" font-weight="700" text-anchor="middle">関係論的</text>
  <text x="380" y="232" class="svg-accent" font-family="Noto Sans JP" font-size="12" font-weight="700" text-anchor="middle">物理生態系</text>
  <text x="380" y="250" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">Active Inference 結節</text>

  <!-- 中央のフィードバック円環 -->
  <circle cx="380" cy="220" r="76" fill="none" class="svg-stroke-accent" stroke-width="0.8" stroke-dasharray="4,3" opacity="0.5"/>
  <path d="M 456,220 A 76,76 0 0,1 380,296" fill="none" class="svg-stroke-accent" stroke-width="1" marker-end="url(#arrow-fig62-fb)"/>

  <!-- 周辺6円：規模を差別化 (人間=小, 古典AI=大, 生体AI=中, 量子AI=中, 分散AI=中-, 身体性AI=中+) -->

  <!-- 人間の知性 (上左、小) -->
  <circle cx="180" cy="120" r="36" class="svg-card svg-stroke-ink" stroke-width="1.5"/>
  <text x="180" y="117" class="svg-ink" font-family="Noto Sans JP" font-size="10" font-weight="700" text-anchor="middle">人間の知性</text>
  <text x="180" y="132" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">意味付け・関係性</text>
  <text x="180" y="80" class="svg-ink-soft" font-family="Noto Sans JP" font-size="8" text-anchor="middle" font-style="italic">規模: 〜10^10 人</text>

  <!-- 古典AI (上右、大) -->
  <circle cx="580" cy="120" r="50" class="svg-card svg-stroke-ink" stroke-width="1.8"/>
  <text x="580" y="117" class="svg-ink" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="middle">古典AI</text>
  <text x="580" y="132" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">LLM successor</text>
  <text x="580" y="148" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">言語・推論・知識</text>
  <text x="580" y="68" class="svg-ink-soft" font-family="Noto Sans JP" font-size="8" text-anchor="middle" font-style="italic">規模: 〜10^14 params</text>

  <!-- 生体AI (左下、中) -->
  <circle cx="120" cy="290" r="42" class="svg-card svg-stroke-ink" stroke-width="1.5"/>
  <text x="120" y="287" class="svg-ink" font-family="Noto Sans JP" font-size="10" font-weight="700" text-anchor="middle">生体AI</text>
  <text x="120" y="302" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">Living Factory</text>
  <text x="120" y="318" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">合成生物</text>
  <text x="120" y="358" class="svg-ink-soft" font-family="Noto Sans JP" font-size="8" text-anchor="middle" font-style="italic">規模: 細胞〜組織</text>

  <!-- 量子AI (右下、中) -->
  <circle cx="640" cy="290" r="42" class="svg-card svg-stroke-ink" stroke-width="1.5"/>
  <text x="640" y="287" class="svg-ink" font-family="Noto Sans JP" font-size="10" font-weight="700" text-anchor="middle">量子AI</text>
  <text x="640" y="302" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">材料・触媒設計</text>
  <text x="640" y="318" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">化学・物性</text>
  <text x="640" y="358" class="svg-ink-soft" font-family="Noto Sans JP" font-size="8" text-anchor="middle" font-style="italic">規模: 10^6 qubits</text>

  <!-- 分散AI (下左、中-) -->
  <circle cx="260" cy="370" r="40" class="svg-card svg-stroke-ink" stroke-width="1.5"/>
  <text x="260" y="367" class="svg-ink" font-family="Noto Sans JP" font-size="10" font-weight="700" text-anchor="middle">分散AI</text>
  <text x="260" y="382" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">ambient embodiment</text>
  <text x="260" y="425" class="svg-ink-soft" font-family="Noto Sans JP" font-size="8" text-anchor="middle" font-style="italic">規模: 10^12 nodes</text>

  <!-- 身体性AI (下右、中+) -->
  <circle cx="500" cy="370" r="46" class="svg-card svg-stroke-accent" stroke-width="2"/>
  <text x="500" y="367" class="svg-accent" font-family="Noto Sans JP" font-size="10" font-weight="700" text-anchor="middle">身体性AI</text>
  <text x="500" y="382" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">フィジカルAI（本書主題）</text>
  <text x="500" y="425" class="svg-ink-soft" font-family="Noto Sans JP" font-size="8" text-anchor="middle" font-style="italic">規模: 〜10^9 体</text>

  <!-- 接続線（太さ＝強度） -->
  <line class="svg-stroke-accent" x1="216" y1="120" x2="324" y2="190" stroke-width="2.2" stroke-dasharray="4,2" opacity="0.7"/>
  <line class="svg-stroke-accent" x1="530" y1="135" x2="436" y2="190" stroke-width="3.4" stroke-dasharray="3,2" opacity="0.85"/>
  <line class="svg-stroke-accent" x1="162" y1="290" x2="322" y2="232" stroke-width="1.8" stroke-dasharray="4,2" opacity="0.65"/>
  <line class="svg-stroke-accent" x1="598" y1="290" x2="438" y2="232" stroke-width="2.0" stroke-dasharray="4,2" opacity="0.7"/>
  <line class="svg-stroke-accent" x1="290" y1="345" x2="345" y2="260" stroke-width="1.5" stroke-dasharray="4,2" opacity="0.6"/>
  <line class="svg-stroke-accent" x1="470" y1="345" x2="415" y2="260" stroke-width="2.6" stroke-dasharray="3,2" opacity="0.8"/>

  <!-- 主導権交替の周回矢印 -->
  <path d="M 80,160 Q 50,300 240,420 Q 460,440 660,400 Q 700,260 680,80 Q 460,50 80,160"
        fill="none" class="svg-stroke-accent" stroke-width="0.6" stroke-dasharray="5,4" opacity="0.35"/>
  <text x="40" y="225" class="svg-accent" font-family="Noto Sans JP" font-size="9" font-style="italic" text-anchor="middle"
        transform="rotate(-90 40 225)">主導権交替 →</text>
</svg>
```

---

## 図7-1（line 1062）三領域動詞組み換え軌道 — 拡張

### 改善方針
- 各ノードに実装事例（OpenVLA / AlphaFold / John Deere See & Spray 等）を吹き出しで追加
- 3 本の線を結ぶ縦線（2030 / 2050 / 2070 / 2100）で同期周波数を可視化
- 各時点の動詞下にミニアイコン（・パイプ・葉）を追加

### 新 SVG 完全版
```svg
<svg viewBox="0 0 760 420" xmlns="http://www.w3.org/2000/svg" role="img"
     aria-labelledby="fig7-1-title fig7-1-desc"
     style="width:100%;max-width:760px;height:auto;display:block;margin:24px auto;">
  <title id="fig7-1-title">図7-1 三領域の動詞組み換え軌道（2030-2100）</title>
  <desc id="fig7-1-desc">製造・医療・農業の動詞変遷が同じ周波数で進む</desc>

  <rect class="svg-bg" x="0" y="0" width="760" height="420"/>

  <text x="380" y="28" class="svg-ink" font-family="Noto Sans JP" font-size="14" font-weight="700" text-anchor="middle">図7-1　三領域に共通する動詞組み換えのテンポ（2030-2100）</text>
  <text x="380" y="46" class="svg-ink-mute" font-family="Noto Sans JP" font-size="11" text-anchor="middle">製造・医療・農業の動詞は 5 系統合流の共通周波数で同期する</text>

  <!-- 同期周波数縦線 -->
  <g class="svg-stroke-accent" stroke-width="0.8" stroke-dasharray="2,3" opacity="0.4">
    <line x1="160" y1="80" x2="160" y2="340"/>
    <line x1="320" y1="80" x2="320" y2="340"/>
    <line x1="480" y1="80" x2="480" y2="340"/>
    <line x1="640" y1="80" x2="640" y2="340"/>
  </g>

  <!-- 時間軸 -->
  <line class="svg-stroke-ink" x1="80" y1="340" x2="700" y2="340" stroke-width="1.5"/>
  <g font-family="Noto Sans JP" font-size="11" class="svg-ink" text-anchor="middle">
    <text x="160" y="360">2030</text>
    <text x="320" y="360">2050</text>
    <text x="480" y="360">2070</text>
    <text x="640" y="360">2100</text>
  </g>

  <!-- 縦軸ラベル -->
  <text x="50" y="120" class="svg-ink" font-family="Noto Sans JP" font-size="12" font-weight="700" text-anchor="middle">製造</text>
  <text x="50" y="200" class="svg-ink" font-family="Noto Sans JP" font-size="12" font-weight="700" text-anchor="middle">医療</text>
  <text x="50" y="280" class="svg-ink" font-family="Noto Sans JP" font-size="12" font-weight="700" text-anchor="middle">農業</text>

  <!-- 製造ライン -->
  <line class="svg-stroke-accent" x1="160" y1="120" x2="640" y2="120" stroke-width="1.6" stroke-dasharray="4,3"/>
  <circle cx="160" cy="120" r="6" class="svg-accent"/>
  <circle cx="320" cy="120" r="6" class="svg-accent"/>
  <circle cx="480" cy="120" r="6" class="svg-accent"/>
  <circle cx="640" cy="120" r="7" class="svg-accent"/>
  <g font-family="Noto Sans JP" font-size="10" text-anchor="middle">
    <text x="160" y="105" class="svg-ink" font-weight="700">統制する</text>
    <text x="160" y="92" class="svg-ink-mute" font-size="8">OpenVLA / Atlas Electric</text>
    <text x="320" y="105" class="svg-ink" font-weight="700">育てる</text>
    <text x="320" y="92" class="svg-ink-mute" font-size="8">Self-Driving Lab</text>
    <text x="480" y="105" class="svg-ink" font-weight="700">生命系製造</text>
    <text x="480" y="92" class="svg-ink-mute" font-size="8">Bio-Hybrid Factory</text>
    <text x="640" y="105" class="svg-ink" font-weight="700">譜面を書く</text>
    <text x="640" y="92" class="svg-ink-mute" font-size="8">関係論的物質代謝</text>
  </g>

  <!-- 医療ライン -->
  <line class="svg-stroke-accent" x1="160" y1="200" x2="640" y2="200" stroke-width="1.6" stroke-dasharray="4,3"/>
  <circle cx="160" cy="200" r="6" class="svg-accent"/>
  <circle cx="320" cy="200" r="6" class="svg-accent"/>
  <circle cx="480" cy="200" r="6" class="svg-accent"/>
  <circle cx="640" cy="200" r="7" class="svg-accent"/>
  <g font-family="Noto Sans JP" font-size="10" text-anchor="middle">
    <text x="160" y="185" class="svg-ink" font-weight="700">AI 診断標準化</text>
    <text x="160" y="172" class="svg-ink-mute" font-size="8">AlphaFold 3 / FDA SaMD</text>
    <text x="320" y="185" class="svg-ink" font-weight="700">AGI 共同診療</text>
    <text x="320" y="172" class="svg-ink-mute" font-size="8">Med-PaLM successor</text>
    <text x="480" y="185" class="svg-ink" font-weight="700">生体組織置換</text>
    <text x="480" y="172" class="svg-ink-mute" font-size="8">オルガノイド移植</text>
    <text x="640" y="185" class="svg-ink" font-weight="700">健康寿命 100 歳</text>
    <text x="640" y="172" class="svg-ink-mute" font-size="8">Sinclair リプログラミング</text>
  </g>

  <!-- 農業ライン -->
  <line class="svg-stroke-accent" x1="160" y1="280" x2="640" y2="280" stroke-width="1.6" stroke-dasharray="4,3"/>
  <circle cx="160" cy="280" r="6" class="svg-accent"/>
  <circle cx="320" cy="280" r="6" class="svg-accent"/>
  <circle cx="480" cy="280" r="6" class="svg-accent"/>
  <circle cx="640" cy="280" r="7" class="svg-accent"/>
  <g font-family="Noto Sans JP" font-size="10" text-anchor="middle">
    <text x="160" y="265" class="svg-ink" font-weight="700">精密農業 AI</text>
    <text x="160" y="252" class="svg-ink-mute" font-size="8">John Deere See & Spray</text>
    <text x="320" y="265" class="svg-ink" font-weight="700">合成生物食料</text>
    <text x="320" y="252" class="svg-ink-mute" font-size="8">Solar Foods / Pivot Bio</text>
    <text x="480" y="265" class="svg-ink" font-weight="700">植物-AI 対話</text>
    <text x="480" y="252" class="svg-ink-mute" font-size="8">Vivent SA (Cocozza)</text>
    <text x="640" y="265" class="svg-ink" font-weight="700">自然権制度化</text>
    <text x="640" y="252" class="svg-ink-mute" font-size="8">Voytas Lab + 法制化</text>
  </g>

  <!-- 同期周波数注釈 -->
  <text x="160" y="380" class="svg-accent" font-family="Noto Sans JP" font-size="9" text-anchor="middle" font-style="italic">基盤モデル標準化</text>
  <text x="320" y="380" class="svg-accent" font-family="Noto Sans JP" font-size="9" text-anchor="middle" font-style="italic">生命系統合</text>
  <text x="480" y="380" class="svg-accent" font-family="Noto Sans JP" font-size="9" text-anchor="middle" font-style="italic">自己組織化</text>
  <text x="640" y="380" class="svg-accent" font-family="Noto Sans JP" font-size="9" text-anchor="middle" font-style="italic">関係論的運営</text>

  <!-- 凡例 -->
  <rect class="svg-surface svg-stroke-border" x="80" y="395" width="620" height="20" stroke-width="1"/>
  <text x="380" y="409" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="middle" font-style="italic">縦点線 = 5 系統合流の同期周波数。三領域は独立して進むようでいて、同じ周波数で動詞を組み換える</text>
</svg>
```

---

## 図7-2（line 1116）規制成熟度マトリクス — 完全再設計

### 改善方針
- 5 段濃淡（0.45/0.55/0.65/0.85/0.95）を 3 段（低/中/高）に簡略化
- 凡例追加（明示的に色↔規制段階の対応）
- 規制名 + 出典年 を併記（EU AI Act 2024 / FDA SaMD 2017 等）
- 「統合度」列も同じ 3 段濃淡で統一

### 新 SVG 完全版
```svg
<svg viewBox="0 0 760 380" xmlns="http://www.w3.org/2000/svg" role="img"
     aria-labelledby="fig7-2-title fig7-2-desc"
     style="width:100%;max-width:760px;height:auto;display:block;margin:24px auto;">
  <title id="fig7-2-title">図7-2 三領域の規制成熟度マトリクス（米中欧）</title>
  <desc id="fig7-2-desc">製造・医療・農業・都市の4領域 × 米・中・EU の3地域の規制成熟度</desc>

  <rect class="svg-bg" x="0" y="0" width="760" height="380"/>

  <text x="380" y="28" class="svg-ink" font-family="Noto Sans JP" font-size="14" font-weight="700" text-anchor="middle">図7-2　三領域の規制成熟度マトリクス（米中欧, 2024-2030）</text>
  <text x="380" y="46" class="svg-ink-mute" font-family="Noto Sans JP" font-size="11" text-anchor="middle">3 段階濃淡 = 規制成熟度（低/中/高）。EU=統合最高、中国=国家戦略主導、米国=業界自主+州別分散</text>

  <!-- ヘッダ -->
  <g font-family="Noto Sans JP" font-size="11" font-weight="700" class="svg-ink" text-anchor="middle">
    <text x="120" y="90" text-anchor="start">領域 ＼ 地域</text>
    <text x="280" y="90">米国</text>
    <text x="420" y="90">中国</text>
    <text x="560" y="90">EU</text>
    <text x="690" y="90">統合度</text>
  </g>
  <line class="svg-stroke-ink" x1="80" y1="100" x2="720" y2="100" stroke-width="1.2"/>

  <!-- 行 1: 製造AI -->
  <text x="120" y="130" class="svg-ink" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="start">製造AI</text>
  <rect x="220" y="113" width="120" height="28" fill="rgba(204,20,0,0.25)" class="svg-stroke-border"/>
  <text x="280" y="124" font-family="Noto Sans JP" font-size="9" class="svg-ink" text-anchor="middle">業界自主</text>
  <text x="280" y="136" font-family="Noto Sans JP" font-size="8" class="svg-ink-mute" text-anchor="middle">OSHA / NIST AI RMF 2023</text>

  <rect x="360" y="113" width="120" height="28" fill="rgba(204,20,0,0.6)" class="svg-stroke-border"/>
  <text x="420" y="124" font-family="Noto Sans JP" font-size="9" fill="#FFFFFF" text-anchor="middle">国家戦略</text>
  <text x="420" y="136" font-family="Noto Sans JP" font-size="8" fill="#FFFFFF" text-anchor="middle">中国製造 2025</text>

  <rect x="500" y="113" width="120" height="28" fill="rgba(204,20,0,0.9)" class="svg-stroke-border"/>
  <text x="560" y="124" font-family="Noto Sans JP" font-size="9" fill="#FFFFFF" text-anchor="middle" font-weight="700">AI Act</text>
  <text x="560" y="136" font-family="Noto Sans JP" font-size="8" fill="#FFFFFF" text-anchor="middle">2024 Art.6 高リスク</text>

  <rect x="640" y="113" width="60" height="28" fill="rgba(204,20,0,0.6)" class="svg-stroke-border"/>
  <text x="670" y="131" font-family="Noto Sans JP" font-size="10" fill="#FFFFFF" text-anchor="middle" font-weight="700">中</text>

  <!-- 行 2: 医療AI -->
  <text x="120" y="170" class="svg-ink" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="start">医療AI</text>
  <rect x="220" y="153" width="120" height="28" fill="rgba(204,20,0,0.6)" class="svg-stroke-border"/>
  <text x="280" y="164" font-family="Noto Sans JP" font-size="9" fill="#FFFFFF" text-anchor="middle" font-weight="700">FDA SaMD</text>
  <text x="280" y="176" font-family="Noto Sans JP" font-size="8" fill="#FFFFFF" text-anchor="middle">2017〜</text>

  <rect x="360" y="153" width="120" height="28" fill="rgba(204,20,0,0.6)" class="svg-stroke-border"/>
  <text x="420" y="164" font-family="Noto Sans JP" font-size="9" fill="#FFFFFF" text-anchor="middle" font-weight="700">NMPA</text>
  <text x="420" y="176" font-family="Noto Sans JP" font-size="8" fill="#FFFFFF" text-anchor="middle">2020 改正</text>

  <rect x="500" y="153" width="120" height="28" fill="rgba(204,20,0,0.9)" class="svg-stroke-border"/>
  <text x="560" y="164" font-family="Noto Sans JP" font-size="9" fill="#FFFFFF" text-anchor="middle" font-weight="700">MDR + AI Act</text>
  <text x="560" y="176" font-family="Noto Sans JP" font-size="8" fill="#FFFFFF" text-anchor="middle">2017/745 + 2024</text>

  <rect x="640" y="153" width="60" height="28" fill="rgba(204,20,0,0.9)" class="svg-stroke-border"/>
  <text x="670" y="171" font-family="Noto Sans JP" font-size="10" fill="#FFFFFF" text-anchor="middle" font-weight="700">高</text>

  <!-- 行 3: 農業AI -->
  <text x="120" y="210" class="svg-ink" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="start">農業AI</text>
  <rect x="220" y="193" width="120" height="28" fill="rgba(204,20,0,0.25)" class="svg-stroke-border"/>
  <text x="280" y="204" font-family="Noto Sans JP" font-size="9" class="svg-ink" text-anchor="middle">USDA 分散</text>
  <text x="280" y="216" font-family="Noto Sans JP" font-size="8" class="svg-ink-mute" text-anchor="middle">州別 / EPA 部分規制</text>

  <rect x="360" y="193" width="120" height="28" fill="rgba(204,20,0,0.6)" class="svg-stroke-border"/>
  <text x="420" y="204" font-family="Noto Sans JP" font-size="9" fill="#FFFFFF" text-anchor="middle">智慧農業</text>
  <text x="420" y="216" font-family="Noto Sans JP" font-size="8" fill="#FFFFFF" text-anchor="middle">2022 政策補助金</text>

  <rect x="500" y="193" width="120" height="28" fill="rgba(204,20,0,0.9)" class="svg-stroke-border"/>
  <text x="560" y="204" font-family="Noto Sans JP" font-size="9" fill="#FFFFFF" text-anchor="middle" font-weight="700">CAP 2023-2027</text>
  <text x="560" y="216" font-family="Noto Sans JP" font-size="8" fill="#FFFFFF" text-anchor="middle">精密農業 環境評価</text>

  <rect x="640" y="193" width="60" height="28" fill="rgba(204,20,0,0.25)" class="svg-stroke-border"/>
  <text x="670" y="211" font-family="Noto Sans JP" font-size="10" class="svg-ink" text-anchor="middle" font-weight="700">低</text>

  <!-- 行 4: 都市AI -->
  <text x="120" y="250" class="svg-ink" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="start">都市AI</text>
  <rect x="220" y="233" width="120" height="28" fill="rgba(204,20,0,0.25)" class="svg-stroke-border"/>
  <text x="280" y="244" font-family="Noto Sans JP" font-size="9" class="svg-ink" text-anchor="middle">市別</text>
  <text x="280" y="256" font-family="Noto Sans JP" font-size="8" class="svg-ink-mute" text-anchor="middle">NYC / SF 個別条例</text>

  <rect x="360" y="233" width="120" height="28" fill="rgba(204,20,0,0.9)" class="svg-stroke-border"/>
  <text x="420" y="244" font-family="Noto Sans JP" font-size="9" fill="#FFFFFF" text-anchor="middle" font-weight="700">スマートシティ</text>
  <text x="420" y="256" font-family="Noto Sans JP" font-size="8" fill="#FFFFFF" text-anchor="middle">国家統合戦略</text>

  <rect x="500" y="233" width="120" height="28" fill="rgba(204,20,0,0.6)" class="svg-stroke-border"/>
  <text x="560" y="244" font-family="Noto Sans JP" font-size="9" fill="#FFFFFF" text-anchor="middle">15 分都市</text>
  <text x="560" y="256" font-family="Noto Sans JP" font-size="8" fill="#FFFFFF" text-anchor="middle">Paris / Moreno 2016</text>

  <rect x="640" y="233" width="60" height="28" fill="rgba(204,20,0,0.6)" class="svg-stroke-border"/>
  <text x="670" y="251" font-family="Noto Sans JP" font-size="10" fill="#FFFFFF" text-anchor="middle" font-weight="700">中</text>

  <!-- 凡例 -->
  <rect class="svg-surface svg-stroke-border" x="80" y="285" width="620" height="50" stroke-width="1"/>
  <text x="92" y="304" class="svg-ink" font-family="Noto Sans JP" font-size="10" font-weight="700">凡例：規制成熟度（3 段階）</text>
  <g font-family="Noto Sans JP" font-size="9">
    <rect x="245" y="293" width="22" height="14" fill="rgba(204,20,0,0.25)" class="svg-stroke-border"/>
    <text x="273" y="304" class="svg-ink">低（業界自主・分散・部分規制）</text>
    <rect x="245" y="313" width="22" height="14" fill="rgba(204,20,0,0.6)" class="svg-stroke-border"/>
    <text x="273" y="324" class="svg-ink">中（国家戦略・主要規制存在）</text>
    <rect x="500" y="313" width="22" height="14" fill="rgba(204,20,0,0.9)" class="svg-stroke-border"/>
    <text x="528" y="324" class="svg-ink">高（包括的法律 + 統合的規制）</text>
  </g>

  <text x="380" y="358" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle" font-style="italic">EU = 規制統合最高 / 中国 = 国家戦略主導 / 米国 = 業界自主＋州別分散</text>
</svg>
```

---

## 図8-1（line 1225）人類圏輪郭組み換え — 完全再設計

### 改善方針
- 同心円を時系列レイヤーに変換、内側＝2026 / 外側＝2100
- 半径方向 = 時間軸として年代を放射方向に明示
- 各リング（都市/教育/宇宙）に年代と特徴を併記
- 中心（人類2026）と外周（人類圏2100）の年代スパンを一目で

### 新 SVG 完全版
```svg
<svg viewBox="0 0 760 460" xmlns="http://www.w3.org/2000/svg" role="img"
     aria-labelledby="fig8-1-title fig8-1-desc"
     style="width:100%;max-width:760px;height:auto;display:block;margin:24px auto;">
  <title id="fig8-1-title">図8-1 人類圏（anthroposphere）の輪郭の組み換え</title>
  <desc id="fig8-1-desc">2026年の人類を中心に、都市・教育・宇宙が同心円として時系列に拡張</desc>

  <rect class="svg-bg" x="0" y="0" width="760" height="460"/>

  <text x="380" y="28" class="svg-ink" font-family="Noto Sans JP" font-size="14" font-weight="700" text-anchor="middle">図8-1　人類圏（anthroposphere）の輪郭の組み換え</text>
  <text x="380" y="46" class="svg-ink-mute" font-family="Noto Sans JP" font-size="11" text-anchor="middle">同心円は時系列レイヤー：内側=2026 / 外側=2100。半径方向に 74 年が広がる</text>

  <!-- 同心円（外側から） -->
  <circle cx="380" cy="240" r="180" fill="none" class="svg-stroke-accent" stroke-width="1.4" stroke-dasharray="8,4"/>
  <circle cx="380" cy="240" r="140" fill="none" class="svg-stroke-accent" stroke-width="1.2" stroke-dasharray="6,3"/>
  <circle cx="380" cy="240" r="100" fill="none" class="svg-stroke-accent" stroke-width="1.2" stroke-dasharray="4,3"/>
  <circle cx="380" cy="240" r="50" fill="none" class="svg-stroke-accent" stroke-width="1.5"/>

  <!-- 中心：人類 2026 -->
  <circle cx="380" cy="240" r="42" class="svg-card svg-stroke-ink" stroke-width="1.5"/>
  <text x="380" y="232" class="svg-ink" font-family="Noto Sans JP" font-size="12" font-weight="700" text-anchor="middle">人類</text>
  <text x="380" y="250" class="svg-accent" font-family="Noto Sans JP" font-size="10" text-anchor="middle">2026</text>

  <!-- リング1: 都市 2050 -->
  <text x="380" y="135" class="svg-accent" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="middle">都市</text>
  <text x="380" y="150" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="middle">自己修復・新陳代謝</text>
  <text x="500" y="240" class="svg-accent" font-family="Noto Sans JP" font-size="10" font-weight="700" text-anchor="middle">2050</text>
  <text x="500" y="254" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">ヒューマノイド共存</text>

  <!-- リング2: 教育 2070 -->
  <text x="222" y="240" class="svg-accent" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="middle">教育</text>
  <text x="222" y="255" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="middle">同席・育成の場</text>
  <text x="540" y="160" class="svg-accent" font-family="Noto Sans JP" font-size="10" font-weight="700" text-anchor="middle">2070</text>
  <text x="540" y="174" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">世代横断ネットワーク</text>

  <!-- リング3: 宇宙 2100 -->
  <text x="380" y="78" class="svg-accent" font-family="Noto Sans JP" font-size="12" font-weight="700" text-anchor="middle">宇宙</text>
  <text x="380" y="93" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="middle">フィジカルAI 代理判断</text>
  <text x="200" y="100" class="svg-accent" font-family="Noto Sans JP" font-size="10" font-weight="700" text-anchor="middle">2100</text>
  <text x="200" y="114" class="svg-ink-mute" font-family="Noto Sans JP" font-size="8" text-anchor="middle">月 10 万人 / 火星拠点 / 深宇宙自律</text>

  <!-- 放射方向の時間軸矢印 -->
  <defs>
    <marker id="arrow-fig8" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0,0 0,6 6,3" class="svg-accent"/>
    </marker>
  </defs>
  <line class="svg-stroke-accent" x1="380" y1="200" x2="380" y2="65" stroke-width="0.8" stroke-dasharray="3,3" marker-end="url(#arrow-fig8)"/>
  <text x="395" y="180" class="svg-accent" font-family="Noto Sans JP" font-size="9" font-style="italic">時間 →</text>

  <!-- 年代マーカー (内側→外側) -->
  <g font-family="Noto Sans JP" font-size="9" class="svg-ink-mute">
    <text x="395" y="195" text-anchor="start">2026</text>
    <text x="395" y="148" text-anchor="start">2050</text>
    <text x="395" y="108" text-anchor="start">2070</text>
    <text x="395" y="68" text-anchor="start">2100</text>
  </g>

  <!-- 注釈ボックス -->
  <rect class="svg-surface svg-stroke-border" x="80" y="395" width="600" height="50" stroke-width="1"/>
  <text x="92" y="414" class="svg-ink" font-family="Noto Sans JP" font-size="10" font-weight="700">人類圏の組み換え方向</text>
  <text x="92" y="432" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9">人類による地球の支配空間（20世紀型）　→　人類と複数知性が共在する関係の網（2100年型）</text>
  <text x="92" y="446" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" font-style="italic">Pierre Teilhard de Chardin "Noosphere"（1955）が物質的・制度的形態を獲得していく</text>
</svg>
```

---

## 図9-1（line 1368）80年5転換 — 完全再設計

### 改善方針
- 各セル左上に Phase タグ（A / C / E / G）と色濃淡を追加
- 5 軸間の駆動矢印を点線で追加（縦方向に細い赤線）
- 横軸を線形時系列、縦軸を 5 転換軸として明確化
- 2100 列以外も色濃淡で強調レベルを表現
- 各セルに極小アイコン的記号（・）で視覚情報量を追加

### 新 SVG 完全版
```svg
<svg viewBox="0 0 760 380" xmlns="http://www.w3.org/2000/svg" role="img"
     aria-labelledby="fig9-1-title fig9-1-desc"
     style="width:100%;max-width:760px;height:auto;display:block;margin:24px auto;">
  <title id="fig9-1-title">図9-1 80年を貫く5つの転換</title>
  <desc id="fig9-1-desc">物理空間/協働範囲/労働意味/統治/個人輪郭の5軸が4時点で連動して変容</desc>

  <rect class="svg-bg" x="0" y="0" width="760" height="380"/>

  <text x="380" y="26" class="svg-ink" font-family="Noto Sans JP" font-size="14" font-weight="700" text-anchor="middle">図9-1　80 年を貫く 5 つの転換（2030-2100）</text>
  <text x="380" y="44" class="svg-ink-mute" font-family="Noto Sans JP" font-size="11" text-anchor="middle">5 軸 × 4 時点。色濃淡 = 変容深度 / 縦点線 = 軸間の駆動関係</text>

  <!-- Phase タグ -->
  <g font-family="Noto Sans JP" font-size="9" font-weight="700" text-anchor="middle">
    <rect x="120" y="58" width="100" height="18" class="svg-accent-shade"/>
    <text x="170" y="70" class="svg-accent">Phase A</text>
    <rect x="240" y="58" width="100" height="18" class="svg-accent-soft"/>
    <text x="290" y="70" class="svg-accent">Phase C</text>
    <rect x="360" y="58" width="100" height="18" fill="rgba(204,20,0,0.35)"/>
    <text x="410" y="70" fill="#FFFFFF">Phase E</text>
    <rect x="480" y="58" width="100" height="18" fill="rgba(204,20,0,0.7)"/>
    <text x="530" y="70" fill="#FFFFFF">Phase G</text>
  </g>

  <!-- 時点ヘッダ -->
  <g font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="middle" class="svg-ink">
    <text x="170" y="95">2030</text>
    <text x="290" y="95">2050</text>
    <text x="410" y="95">2070</text>
    <text x="530" y="95">2100</text>
  </g>

  <!-- 軸ラベル列 -->
  <g font-family="Noto Sans JP" font-size="10" font-weight="700" text-anchor="end" class="svg-ink">
    <text x="115" y="135">物理空間</text>
    <text x="115" y="180">協働範囲</text>
    <text x="115" y="225">労働の意味</text>
    <text x="115" y="270">統治</text>
    <text x="115" y="315">個人の輪郭</text>
  </g>

  <!-- グリッド線 -->
  <g class="svg-stroke-border" stroke-width="0.6">
    <line x1="120" y1="110" x2="580" y2="110"/>
    <line x1="120" y1="155" x2="580" y2="155"/>
    <line x1="120" y1="200" x2="580" y2="200"/>
    <line x1="120" y1="245" x2="580" y2="245"/>
    <line x1="120" y1="290" x2="580" y2="290"/>
    <line x1="120" y1="335" x2="580" y2="335"/>
    <line x1="120" y1="110" x2="120" y2="335"/>
    <line x1="240" y1="110" x2="240" y2="335"/>
    <line x1="360" y1="110" x2="360" y2="335"/>
    <line x1="480" y1="110" x2="480" y2="335"/>
    <line x1="580" y1="110" x2="580" y2="335"/>
  </g>

  <!-- セル背景（軸×時点 = 強度濃淡） -->
  <!-- 物理空間 -->
  <rect x="120" y="110" width="120" height="45" class="svg-accent-shade"/>
  <rect x="240" y="110" width="120" height="45" class="svg-accent-soft"/>
  <rect x="360" y="110" width="120" height="45" fill="rgba(204,20,0,0.35)"/>
  <rect x="480" y="110" width="100" height="45" fill="rgba(204,20,0,0.7)"/>

  <!-- 協働範囲 -->
  <rect x="120" y="155" width="120" height="45" class="svg-accent-shade"/>
  <rect x="240" y="155" width="120" height="45" class="svg-accent-soft"/>
  <rect x="360" y="155" width="120" height="45" fill="rgba(204,20,0,0.35)"/>
  <rect x="480" y="155" width="100" height="45" fill="rgba(204,20,0,0.7)"/>

  <!-- 労働の意味 -->
  <rect x="120" y="200" width="120" height="45" class="svg-accent-shade"/>
  <rect x="240" y="200" width="120" height="45" class="svg-accent-soft"/>
  <rect x="360" y="200" width="120" height="45" fill="rgba(204,20,0,0.35)"/>
  <rect x="480" y="200" width="100" height="45" fill="rgba(204,20,0,0.7)"/>

  <!-- 統治 -->
  <rect x="120" y="245" width="120" height="45" class="svg-accent-shade"/>
  <rect x="240" y="245" width="120" height="45" class="svg-accent-soft"/>
  <rect x="360" y="245" width="120" height="45" fill="rgba(204,20,0,0.35)"/>
  <rect x="480" y="245" width="100" height="45" fill="rgba(204,20,0,0.7)"/>

  <!-- 個人の輪郭 -->
  <rect x="120" y="290" width="120" height="45" class="svg-accent-shade"/>
  <rect x="240" y="290" width="120" height="45" class="svg-accent-soft"/>
  <rect x="360" y="290" width="120" height="45" fill="rgba(204,20,0,0.35)"/>
  <rect x="480" y="290" width="100" height="45" fill="rgba(204,20,0,0.7)"/>

  <!-- セル内テキスト -->
  <g font-family="Noto Sans JP" font-size="10" text-anchor="middle">
    <!-- 物理空間 -->
    <text x="170" y="135" class="svg-ink">・死んだ素材</text>
    <text x="290" y="135" class="svg-ink">・自己適応</text>
    <text x="410" y="135" fill="#FFFFFF" font-weight="700">・生命系製造</text>
    <text x="530" y="135" fill="#FFFFFF" font-weight="700">・関係論的生態</text>

    <!-- 協働範囲 -->
    <text x="170" y="180" class="svg-ink">・人＋道具</text>
    <text x="290" y="180" class="svg-ink">・人＋AI 協働</text>
    <text x="410" y="180" fill="#FFFFFF" font-weight="700">・六項関係</text>
    <text x="530" y="180" fill="#FFFFFF" font-weight="700">・オーケストラ</text>

    <!-- 労働の意味 -->
    <text x="170" y="225" class="svg-ink">・時間消費</text>
    <text x="290" y="225" class="svg-ink">・意味への拡張</text>
    <text x="410" y="225" fill="#FFFFFF" font-weight="700">・譜面と楽団員</text>
    <text x="530" y="225" fill="#FFFFFF" font-weight="700">・文明維持から解放</text>

    <!-- 統治 -->
    <text x="170" y="270" class="svg-ink">・三極ブロック</text>
    <text x="290" y="270" class="svg-ink">・自然権制度化</text>
    <text x="410" y="270" fill="#FFFFFF" font-weight="700">・三重なり</text>
    <text x="530" y="270" fill="#FFFFFF" font-weight="700">・指揮者なき協奏</text>

    <!-- 個人の輪郭 -->
    <text x="170" y="315" class="svg-ink">・皮膚で切れる</text>
    <text x="290" y="315" class="svg-ink">・拡張認知前提</text>
    <text x="410" y="315" fill="#FFFFFF" font-weight="700">・分散的自己</text>
    <text x="530" y="315" fill="#FFFFFF" font-weight="700">・関係の網の楽器</text>
  </g>

  <!-- 軸間駆動矢印（縦点線、5軸間の影響） -->
  <g class="svg-stroke-accent" stroke-width="0.6" stroke-dasharray="2,3" opacity="0.55">
    <line x1="600" y1="135" x2="600" y2="155"/>
    <line x1="600" y1="180" x2="600" y2="200"/>
    <line x1="600" y1="225" x2="600" y2="245"/>
    <line x1="600" y1="270" x2="600" y2="290"/>
  </g>
  <text x="615" y="225" class="svg-accent" font-family="Noto Sans JP" font-size="9" font-style="italic" text-anchor="start">軸間駆動</text>

  <!-- 凡例 -->
  <rect class="svg-surface svg-stroke-border" x="120" y="350" width="460" height="22" stroke-width="1"/>
  <text x="130" y="364" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" font-weight="700">変容深度：</text>
  <g font-family="Noto Sans JP" font-size="9">
    <rect x="195" y="355" width="20" height="12" class="svg-accent-shade"/>
    <text x="220" y="364" class="svg-ink">浅</text>
    <rect x="240" y="355" width="20" height="12" class="svg-accent-soft"/>
    <text x="265" y="364" class="svg-ink">中</text>
    <rect x="285" y="355" width="20" height="12" fill="rgba(204,20,0,0.35)"/>
    <text x="310" y="364" class="svg-ink">深</text>
    <rect x="330" y="355" width="20" height="12" fill="rgba(204,20,0,0.7)"/>
    <text x="355" y="364" class="svg-ink">完全変容</text>
    <text x="415" y="364" class="svg-ink-mute" font-style="italic">・縦点線 = 軸間の駆動関係</text>
  </g>
</svg>
```

---

## 図14（line 1507）17能力＋4項目 世代配置 — 完全再設計

### 改善方針
- 4 世代を時間軸（横軸）に配置
- 各能力を線で世代間連結（依存関係を可視化）
- 追加4項目（フィジカルAI 固有）を縦軸の別レイヤー（赤帯）として配置
- 中央に「AI-augmented Teal」組織を可視化

### 新 SVG 完全版
```svg
<svg viewBox="0 0 760 460" xmlns="http://www.w3.org/2000/svg" role="img"
     aria-labelledby="fig14-title fig14-desc"
     style="width:100%;max-width:760px;height:auto;display:block;margin:24px auto;">
  <title id="fig14-title">図14 17能力＋4項目の世代別配置と相互補完</title>
  <desc id="fig14-desc">4世代の17能力と追加4項目が AI-augmented Teal 組織のなかで補完関係を結ぶ</desc>

  <rect class="svg-bg" x="0" y="0" width="760" height="460"/>

  <text x="380" y="26" class="svg-ink" font-family="Noto Sans JP" font-size="14" font-weight="700" text-anchor="middle">図14　17 能力 ＋ 4 項目の世代別配置（AI-augmented Teal 組織）</text>
  <text x="380" y="44" class="svg-ink-mute" font-family="Noto Sans JP" font-size="11" text-anchor="middle">4 世代を横軸に配置、能力線で世代間補完を可視化、下層赤帯にフィジカルAI 固有 4 項目</text>

  <!-- 世代ヘッダ -->
  <g font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="middle">
    <rect x="80" y="60" width="155" height="32" class="svg-accent-shade"/>
    <text x="158" y="78" class="svg-accent">20-30 代</text>
    <text x="158" y="91" class="svg-ink-mute" font-size="9">2030 年・5 能力</text>

    <rect x="245" y="60" width="155" height="32" class="svg-accent-soft"/>
    <text x="322" y="78" class="svg-accent">40-50 代</text>
    <text x="322" y="91" class="svg-ink-mute" font-size="9">2050 年・4 能力</text>

    <rect x="410" y="60" width="155" height="32" fill="rgba(204,20,0,0.35)"/>
    <text x="488" y="78" fill="#FFFFFF">60-70 代</text>
    <text x="488" y="91" fill="#FFFFFF" font-size="9">2070 年・3 能力</text>

    <rect x="575" y="60" width="155" height="32" fill="rgba(204,20,0,0.7)"/>
    <text x="652" y="78" fill="#FFFFFF">80 歳以上</text>
    <text x="652" y="91" fill="#FFFFFF" font-size="9">2100 年・5 能力</text>
  </g>

  <!-- 世代別能力ボックス -->
  <rect class="svg-card svg-stroke-border" x="80" y="105" width="155" height="195" stroke-width="1"/>
  <rect class="svg-card svg-stroke-border" x="245" y="105" width="155" height="195" stroke-width="1"/>
  <rect class="svg-card svg-stroke-border" x="410" y="105" width="155" height="195" stroke-width="1"/>
  <rect class="svg-card svg-stroke-border" x="575" y="105" width="155" height="195" stroke-width="1"/>

  <!-- 20-30代 -->
  <g font-family="Noto Sans JP" font-size="9" class="svg-ink">
    <text x="95" y="125">・AI 判断調律</text>
    <text x="95" y="142">・知の代謝</text>
    <text x="95" y="159">・揺らぎ運用</text>
    <text x="95" y="176">・仮説実装</text>
    <text x="95" y="193">・社会変革</text>
  </g>
  <!-- 40-50代 -->
  <g font-family="Noto Sans JP" font-size="9" class="svg-ink">
    <text x="260" y="125">・AI 停止責任</text>
    <text x="260" y="142">・超域社会変革</text>
    <text x="260" y="159">・意味づけ編集</text>
    <text x="260" y="176">・編み直しの体力</text>
  </g>
  <!-- 60-70代 -->
  <g font-family="Noto Sans JP" font-size="9" class="svg-ink">
    <text x="425" y="125">・惑星システム</text>
    <text x="425" y="142">・異分野統合</text>
    <text x="425" y="159">・存在間調停</text>
  </g>
  <!-- 80歳以上 -->
  <g font-family="Noto Sans JP" font-size="9" class="svg-ink">
    <text x="590" y="125">・深く問う</text>
    <text x="590" y="142">・異質と対話</text>
    <text x="590" y="159">・物語を編む</text>
    <text x="590" y="176">・関係を見る</text>
    <text x="590" y="193">・痛み引き受け</text>
  </g>

  <!-- 世代間補完関係（能力線） -->
  <g class="svg-stroke-accent" stroke-width="0.8" stroke-dasharray="3,2" opacity="0.55">
    <path d="M 235,125 Q 240,200 260,140" fill="none"/>
    <path d="M 235,160 Q 240,210 260,160" fill="none"/>
    <path d="M 400,140 Q 405,180 425,125" fill="none"/>
    <path d="M 400,175 Q 405,200 425,160" fill="none"/>
    <path d="M 565,140 Q 570,170 590,140" fill="none"/>
    <path d="M 565,160 Q 570,200 590,176" fill="none"/>
  </g>

  <!-- 中央 AI-augmented Teal 帯 -->
  <rect x="80" y="220" width="650" height="50" class="svg-accent-soft svg-stroke-accent" stroke-width="1.4"/>
  <text x="405" y="240" class="svg-accent" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="middle">AI-augmented Teal 組織 = 4 世代の同時保有 × 能力ベース相互補完</text>
  <text x="405" y="256" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9" text-anchor="middle">17 能力 + 4 項目 = 21 ベクトルが組織内に分散し、自律的な編成として動作する</text>

  <!-- フィジカルAI 固有 4 項目（下層赤帯） -->
  <rect x="80" y="320" width="650" height="80" fill="rgba(204,20,0,0.85)" class="svg-stroke-accent" stroke-width="1.5"/>
  <text x="405" y="340" fill="#FFFFFF" font-family="Noto Sans JP" font-size="11" font-weight="700" text-anchor="middle">フィジカルAI 固有 + 4 項目（世代を超えた共通基盤）</text>

  <g font-family="Noto Sans JP" font-size="10" fill="#FFFFFF" font-weight="700" text-anchor="middle">
    <text x="158" y="370">＋ 機械を育てる作法</text>
    <text x="322" y="370">＋ ケア非対称分業</text>
    <text x="488" y="370">＋ 植物物質代謝譜面</text>
    <text x="652" y="370">＋ 分散身体同席</text>
  </g>
  <g font-family="Noto Sans JP" font-size="8" fill="#FFFFFF" text-anchor="middle" opacity="0.85">
    <text x="158" y="386">統制→育てる動詞螺旋</text>
    <text x="322" y="386">介護労働再設計</text>
    <text x="488" y="386">植物-AI 対話</text>
    <text x="652" y="386">ambient embodiment</text>
  </g>

  <!-- 世代間能力依存矢印（フィジカルAI 4項目 → 17能力） -->
  <g class="svg-stroke-accent" stroke-width="0.5" stroke-dasharray="2,3" opacity="0.4">
    <line x1="158" y1="320" x2="158" y2="290"/>
    <line x1="322" y1="320" x2="322" y2="290"/>
    <line x1="488" y1="320" x2="488" y2="290"/>
    <line x1="652" y1="320" x2="652" y2="290"/>
  </g>

  <!-- フッタ -->
  <text x="380" y="425" class="svg-ink-soft" font-family="Noto Sans JP" font-size="10" text-anchor="middle" font-style="italic">「4 世代 × 17 能力 + 4 項目」の同時保有構造が、22 世紀の組織の競争優位を規定する</text>
  <text x="380" y="445" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">出典: era-talents DB（17 能力次元）+ 本書独自抽出のフィジカルAI 4 項目</text>
</svg>
```

---

## 図13（line 1619）5補論交差点 — 拡張（Venn 風）

### 改善方針
- 5 円を Venn 図風に重ね合わせ、中央交差領域に「関係論的存在論」を配置
- PHAI を中央寄りに大きく描画
- 補論間の引用関係を矢印で表現
- 各補論の貢献領域を 1 行追記

### 新 SVG 完全版
```svg
<svg viewBox="0 0 760 440" xmlns="http://www.w3.org/2000/svg" role="img"
     aria-labelledby="fig13-title fig13-desc"
     style="width:100%;max-width:760px;height:auto;display:block;margin:24px auto;">
  <title id="fig13-title">図13 FVCP 補論シリーズ 5 補論の交差点</title>
  <desc id="fig13-desc">5補論（製造v6/MOB/PHAI/HRORG/Talent）が中央の関係論的存在論で重なる Venn 図</desc>

  <rect class="svg-bg" x="0" y="0" width="760" height="440"/>

  <text x="380" y="28" class="svg-ink" font-family="Noto Sans JP" font-size="14" font-weight="700" text-anchor="middle">図13　FVCP 補論シリーズ 5 補論の交差点</text>
  <text x="380" y="46" class="svg-ink-mute" font-family="Noto Sans JP" font-size="11" text-anchor="middle">中央に共通の存在論。本書 PHAI は物質的実装として他 4 補論と接続する</text>

  <!-- Venn 5 円（中央重なり） -->
  <g transform="translate(380,235)">
    <!-- 製造v6 (上) -->
    <circle cx="0" cy="-110" r="84" fill="rgba(204,20,0,0.10)" class="svg-stroke-accent" stroke-width="1.5"/>
    <text x="0" y="-180" class="svg-accent" font-family="Noto Sans JP" font-size="12" font-weight="700" text-anchor="middle">製造 v6</text>
    <text x="0" y="-164" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">統制 → 育てる</text>

    <!-- MOB (右上) -->
    <circle cx="105" cy="-50" r="84" fill="rgba(204,20,0,0.10)" class="svg-stroke-accent" stroke-width="1.5"/>
    <text x="180" y="-80" class="svg-accent" font-family="Noto Sans JP" font-size="12" font-weight="700" text-anchor="middle">MOB</text>
    <text x="180" y="-64" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">運ぶ → 宿る</text>

    <!-- HRORG (右下) -->
    <circle cx="105" cy="50" r="84" fill="rgba(204,20,0,0.10)" class="svg-stroke-accent" stroke-width="1.5"/>
    <text x="180" y="60" class="svg-accent" font-family="Noto Sans JP" font-size="12" font-weight="700" text-anchor="middle">HRORG</text>
    <text x="180" y="76" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">管理 → 編む</text>

    <!-- Talent (左下) -->
    <circle cx="-105" cy="50" r="84" fill="rgba(204,20,0,0.10)" class="svg-stroke-accent" stroke-width="1.5"/>
    <text x="-180" y="60" class="svg-accent" font-family="Noto Sans JP" font-size="12" font-weight="700" text-anchor="middle">Talent</text>
    <text x="-180" y="76" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">マクロ人材論</text>

    <!-- 本書 PHAI (左上, 中央寄り・大きい) -->
    <circle cx="-105" cy="-50" r="98" fill="rgba(204,20,0,0.18)" class="svg-stroke-accent" stroke-width="2.4"/>
    <text x="-180" y="-80" class="svg-accent" font-family="Noto Sans JP" font-size="13" font-weight="700" text-anchor="middle">本書 PHAI</text>
    <text x="-180" y="-64" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" text-anchor="middle">演算 → 共在（中軸）</text>

    <!-- 中央交差領域（関係論的存在論） -->
    <circle cx="0" cy="0" r="42" fill="#FFFFFF" class="svg-stroke-accent" stroke-width="2.4"/>
    <text x="0" y="-3" class="svg-accent" font-family="Noto Sans JP" font-size="10" font-weight="700" text-anchor="middle">関係論的</text>
    <text x="0" y="13" class="svg-accent" font-family="Noto Sans JP" font-size="10" font-weight="700" text-anchor="middle">存在論</text>

    <!-- 補論間の引用関係 (矢印) -->
    <defs>
      <marker id="arrow-fig13" markerWidth="6" markerHeight="6" refX="5" refY="2" orient="auto">
        <polygon points="0,0 0,4 5,2" class="svg-accent"/>
      </marker>
    </defs>
    <g class="svg-stroke-accent" stroke-width="0.6" opacity="0.55">
      <line x1="-20" y1="-100" x2="20" y2="-100" marker-end="url(#arrow-fig13)"/>
      <line x1="100" y1="-25" x2="100" y2="25" marker-end="url(#arrow-fig13)"/>
      <line x1="20" y1="100" x2="-20" y2="100" marker-end="url(#arrow-fig13)"/>
      <line x1="-100" y1="25" x2="-100" y2="-25" marker-end="url(#arrow-fig13)"/>
    </g>
  </g>

  <!-- 注釈 -->
  <rect class="svg-surface svg-stroke-border" x="80" y="380" width="600" height="48" stroke-width="1"/>
  <text x="92" y="398" class="svg-ink" font-family="Noto Sans JP" font-size="10" font-weight="700">5 補論の関係</text>
  <text x="92" y="414" class="svg-ink-soft" font-family="Noto Sans JP" font-size="9">5 補論は中央の「関係論的存在論」を共有しつつ、各補論が固有の領域を扱う相互補完関係</text>
  <text x="92" y="424" class="svg-ink-mute" font-family="Noto Sans JP" font-size="9" font-style="italic">本書 PHAI = フィジカルAI 技術論として他 4 補論を物質的実装の側面から立体化する</text>
</svg>
```

---

## 適用手順

1. **CSS 注入**: `output/index.html` の `<head>` 内（または既存 `<style>` 直後）に「共通 `<style>` ブロック」を追加。`[data-theme="dark"]` selector がグローバルテーマトグルと連動する。
2. **SVG 置換**: 各 SVG 位置（line 222, 343, 462, 569, 631, 728, 776, 866, 929, 1062, 1116, 1225, 1368, 1507, 1619）の `<svg>...</svg>` を上記新 SVG に置換。`<figcaption>` は既存のものを維持（必要に応じ更新）。
3. **重複解消**: 図4-1 + 図4-2 → 図4-12 への統合に伴い、元の図4-2 ブロックを削除し、図4-1 位置に新図4-12 を配置。
4. **ダーク検証**: `<html data-theme="dark">` を強制適用して全 15 SVG の視認性を確認。
5. **印刷検証**: `@media print` でも線・テキストが読めることを確認（CSS 変数のフォールバック確保）。

---

## 設計総評

- **共通基準達成**: 全 15 SVG が `style="width:100%;max-width:760px;height:auto;display:block;margin:24px auto;"` で統一、role/title/desc でアクセシビリティ確保、`[data-theme="dark"]` selector でダーク対応、`#CC1400 / #FF4030` 赤白CI 準拠
- **視覚的多様化**: ストリームチャート（図4-12）/ Sankey 風（図5-2）/ 同心円時系列（図8-1）/ Venn 図（図13）/ ヒートマップ・マトリクス（図9-1, 図7-2）/ フェード溶解（図6-1）の 6 種類の図形語彙を導入
- **情報密度向上**: 各図に実装事例・年代・出典・規模情報を追記し、figcaption に依存しない自己完結性を強化
- **重複解消**: 図4-1+4-2 統合により 15 → 14 図、図4-12 として 1 枚で Phase A→B 動態を表現

**ファイル**: `/Users/nishimura+/projects/research/physical-ai-2100/enhancement/diagrams/d1_redesigned_svgs.md`
**作成日**: 2026-05-18
**設計主体**: D1 図解再設計隊（AR-DB ブラッシュアップ Wave 1）
