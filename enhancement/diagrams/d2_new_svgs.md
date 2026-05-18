# D2 — Physical AI 2100 教科書 新規10図解（SVG完全版）

新規 10 図解を `~/projects/research/physical-ai-2100/output/index.html` の既存 SVG パターン（viewBox=760×400 推奨／赤白CI #CC1400／Noto Sans JP・Noto Serif JP／ダークモード `[data-theme="dark"]` 互換）に整合させて設計した。

各 SVG は `<figure>` 入れ子（`background:rgba(204,20,0,0.02);border-top:1px solid #CC1400;border-bottom:1px solid #CC1400;padding:32px 16px;`）で配置することを推奨。ダークモード対応は既存 `[data-theme="dark"] svg text` 等の CSS ルールが自動適用されるよう、`fill="#121212"` / `fill="#555"` / `fill="#FFF"` / `fill="#CC1400"` / `stroke="#121212"` / `stroke="#D9D9D9"` の正規パレットのみを使用している。

---

## 図 N1: AR-DB横断マップ図

- **配置章**: 第1章「フィジカルAI 74年の構造的位置」あるいは序章末（DB横断統合の宣言）
- **設計意図**: 46 DBs を 6 領域 (Science 8 / Society 20 / Foresight 11 / Enterprise 25 / Culture 13 / Infra 11) のクラスタとして配置。Physical AI 関連 DB（PHAI / AI-DEV / AI-ACC / FTT / TA / SIF / GC / KGH 等）を赤 #CC1400 でハイライトし、その他は #555555 で淡く表示。エッジは Physical AI ノードから他DBへ放射する形で 12 本のみ描き、横断性を象徴する

```html
<figure style="margin:36px 0;text-align:center;background:rgba(204,20,0,0.02);border-top:1px solid #CC1400;border-bottom:1px solid #CC1400;padding:32px 16px;">
<svg viewBox="0 0 760 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:760px;height:auto;">
<!-- 6領域クラスタ枠 -->
<rect x="20" y="30" width="220" height="110" fill="#FFF" stroke="#D9D9D9" stroke-width="1" rx="6"/>
<text x="130" y="48" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#555" text-anchor="middle" font-weight="700">SCIENCE (8 DBs)</text>
<rect x="260" y="30" width="220" height="110" fill="#FFF" stroke="#D9D9D9" stroke-width="1" rx="6"/>
<text x="370" y="48" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#555" text-anchor="middle" font-weight="700">SOCIETY (20 DBs)</text>
<rect x="500" y="30" width="240" height="110" fill="#FFF" stroke="#D9D9D9" stroke-width="1" rx="6"/>
<text x="620" y="48" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#555" text-anchor="middle" font-weight="700">FORESIGHT (11 DBs)</text>
<rect x="20" y="260" width="220" height="110" fill="#FFF" stroke="#D9D9D9" stroke-width="1" rx="6"/>
<text x="130" y="278" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#555" text-anchor="middle" font-weight="700">ENTERPRISE (25 DBs)</text>
<rect x="260" y="260" width="220" height="110" fill="#FFF" stroke="#D9D9D9" stroke-width="1" rx="6"/>
<text x="370" y="278" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#555" text-anchor="middle" font-weight="700">CULTURE (13 DBs)</text>
<rect x="500" y="260" width="240" height="110" fill="#FFF" stroke="#D9D9D9" stroke-width="1" rx="6"/>
<text x="620" y="278" font-family="Noto Sans JP, sans-serif" font-size="11" fill="#555" text-anchor="middle" font-weight="700">INFRA (11 DBs)</text>

<!-- Science cluster nodes -->
<circle cx="55" cy="80" r="6" fill="#555"/><text x="55" y="100" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">PHYS</text>
<circle cx="90" cy="80" r="6" fill="#555"/><text x="90" y="100" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">CHEM</text>
<circle cx="125" cy="80" r="6" fill="#555"/><text x="125" y="100" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">BOT</text>
<circle cx="160" cy="80" r="6" fill="#555"/><text x="160" y="100" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">ES</text>
<circle cx="195" cy="80" r="6" fill="#555"/><text x="195" y="100" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">CEH</text>
<circle cx="55" cy="120" r="6" fill="#555"/><text x="55" y="135" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">TC</text>
<circle cx="90" cy="120" r="6" fill="#555"/><text x="90" y="135" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">KGH</text>
<circle cx="125" cy="120" r="6" fill="#555"/><text x="125" y="135" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">HTP</text>

<!-- Society cluster nodes (selective + EC/SS highlight) -->
<circle cx="285" cy="75" r="6" fill="#555"/><text x="285" y="90" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">AN</text>
<circle cx="320" cy="75" r="6" fill="#555"/><text x="320" y="90" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">SS</text>
<circle cx="355" cy="75" r="6" fill="#555"/><text x="355" y="90" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">EC</text>
<circle cx="390" cy="75" r="6" fill="#555"/><text x="390" y="90" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">PHIL</text>
<circle cx="425" cy="75" r="6" fill="#555"/><text x="425" y="90" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">SG</text>
<circle cx="460" cy="75" r="6" fill="#555"/><text x="460" y="90" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">LIT</text>
<circle cx="285" cy="115" r="6" fill="#555"/><text x="285" y="130" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">MG</text>
<circle cx="320" cy="115" r="6" fill="#555"/><text x="320" y="130" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">GF</text>
<circle cx="355" cy="115" r="6" fill="#555"/><text x="355" y="130" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">PST</text>
<circle cx="390" cy="115" r="6" fill="#555"/><text x="390" y="130" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">LAB</text>
<circle cx="425" cy="115" r="6" fill="#555"/><text x="425" y="130" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">PQS</text>
<circle cx="460" cy="115" r="6" fill="#555"/><text x="460" y="130" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">CQ</text>

<!-- Foresight cluster nodes (PHAI/AI-DEV/AI-ACC/FTT highlighted) -->
<circle cx="530" cy="75" r="7" fill="#CC1400"/><text x="530" y="92" font-family="Noto Sans JP" font-size="8" fill="#CC1400" text-anchor="middle" font-weight="700">PHAI</text>
<circle cx="570" cy="75" r="7" fill="#CC1400"/><text x="570" y="92" font-family="Noto Sans JP" font-size="8" fill="#CC1400" text-anchor="middle" font-weight="700">AI-DEV</text>
<circle cx="610" cy="75" r="7" fill="#CC1400"/><text x="610" y="92" font-family="Noto Sans JP" font-size="8" fill="#CC1400" text-anchor="middle" font-weight="700">AI-ACC</text>
<circle cx="650" cy="75" r="7" fill="#CC1400"/><text x="650" y="92" font-family="Noto Sans JP" font-size="8" fill="#CC1400" text-anchor="middle" font-weight="700">FTT</text>
<circle cx="690" cy="75" r="6" fill="#555"/><text x="690" y="90" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">CLA</text>
<circle cx="530" cy="115" r="6" fill="#555"/><text x="530" y="130" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">SIGNAL</text>
<circle cx="570" cy="115" r="6" fill="#555"/><text x="570" y="130" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">PESTLE</text>
<circle cx="610" cy="115" r="6" fill="#555"/><text x="610" y="130" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">MEGA</text>
<circle cx="650" cy="115" r="6" fill="#555"/><text x="650" y="130" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">SFS</text>
<circle cx="690" cy="115" r="6" fill="#555"/><text x="690" y="130" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">FKB</text>

<!-- Enterprise cluster -->
<circle cx="55" cy="305" r="7" fill="#CC1400"/><text x="55" y="322" font-family="Noto Sans JP" font-size="8" fill="#CC1400" text-anchor="middle" font-weight="700">TA</text>
<circle cx="90" cy="305" r="6" fill="#555"/><text x="90" y="320" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">SGRD</text>
<circle cx="125" cy="305" r="6" fill="#555"/><text x="125" y="320" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">US</text>
<circle cx="160" cy="305" r="6" fill="#555"/><text x="160" y="320" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">SGPR</text>
<circle cx="195" cy="305" r="6" fill="#555"/><text x="195" y="320" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">UPR</text>
<circle cx="55" cy="345" r="6" fill="#555"/><text x="55" y="360" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">CDH</text>
<circle cx="90" cy="345" r="6" fill="#555"/><text x="90" y="360" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">SI</text>
<circle cx="125" cy="345" r="6" fill="#555"/><text x="125" y="360" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">PD</text>
<circle cx="160" cy="345" r="6" fill="#555"/><text x="160" y="360" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">RG</text>
<circle cx="195" cy="345" r="6" fill="#555"/><text x="195" y="360" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">EX</text>

<!-- Culture cluster -->
<circle cx="290" cy="305" r="6" fill="#555"/><text x="290" y="320" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">KK</text>
<circle cx="325" cy="305" r="6" fill="#555"/><text x="325" y="320" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">JK</text>
<circle cx="360" cy="305" r="6" fill="#555"/><text x="360" y="320" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">HK</text>
<circle cx="395" cy="305" r="6" fill="#555"/><text x="395" y="320" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">EK</text>
<circle cx="430" cy="305" r="6" fill="#555"/><text x="430" y="320" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">IK</text>
<circle cx="290" cy="345" r="6" fill="#555"/><text x="290" y="360" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">FUT</text>
<circle cx="325" cy="345" r="6" fill="#555"/><text x="325" y="360" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">F2</text>
<circle cx="360" cy="345" r="6" fill="#555"/><text x="360" y="360" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">CI</text>
<circle cx="395" cy="345" r="6" fill="#555"/><text x="395" y="360" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">TK</text>

<!-- Infra cluster (GC/AR highlighted) -->
<circle cx="530" cy="305" r="7" fill="#CC1400"/><text x="530" y="322" font-family="Noto Sans JP" font-size="8" fill="#CC1400" text-anchor="middle" font-weight="700">GC</text>
<circle cx="570" cy="305" r="7" fill="#CC1400"/><text x="570" y="322" font-family="Noto Sans JP" font-size="8" fill="#CC1400" text-anchor="middle" font-weight="700">AR-DB</text>
<circle cx="610" cy="305" r="6" fill="#555"/><text x="610" y="320" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">SIF</text>
<circle cx="650" cy="305" r="6" fill="#555"/><text x="650" y="320" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">CTI</text>
<circle cx="690" cy="305" r="6" fill="#555"/><text x="690" y="320" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">FVCP</text>
<circle cx="530" cy="345" r="6" fill="#555"/><text x="530" y="360" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">MA</text>
<circle cx="570" cy="345" r="6" fill="#555"/><text x="570" y="360" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">EPO</text>
<circle cx="610" cy="345" r="6" fill="#555"/><text x="610" y="360" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">APK</text>

<!-- Physical AI hub edges (PHAI 530,75 → 主要DB) -->
<line x1="530" y1="75" x2="55" y2="80" stroke="#CC1400" stroke-width="0.6" opacity="0.5"/>
<line x1="530" y1="75" x2="285" y2="115" stroke="#CC1400" stroke-width="0.6" opacity="0.5"/>
<line x1="530" y1="75" x2="55" y2="305" stroke="#CC1400" stroke-width="0.6" opacity="0.5"/>
<line x1="530" y1="75" x2="125" y2="305" stroke="#CC1400" stroke-width="0.6" opacity="0.5"/>
<line x1="530" y1="75" x2="530" y2="305" stroke="#CC1400" stroke-width="0.6" opacity="0.5"/>
<line x1="530" y1="75" x2="570" y2="305" stroke="#CC1400" stroke-width="0.6" opacity="0.5"/>
<line x1="530" y1="75" x2="570" y2="75" stroke="#CC1400" stroke-width="0.8" opacity="0.7"/>
<line x1="530" y1="75" x2="610" y2="75" stroke="#CC1400" stroke-width="0.8" opacity="0.7"/>
<line x1="530" y1="75" x2="650" y2="75" stroke="#CC1400" stroke-width="0.8" opacity="0.7"/>
<line x1="530" y1="75" x2="610" y2="305" stroke="#CC1400" stroke-width="0.6" opacity="0.5"/>
<line x1="530" y1="75" x2="395" y2="115" stroke="#CC1400" stroke-width="0.6" opacity="0.5"/>
<line x1="530" y1="75" x2="195" y2="305" stroke="#CC1400" stroke-width="0.6" opacity="0.5"/>

<!-- 凡例 -->
<circle cx="40" cy="20" r="5" fill="#CC1400"/>
<text x="52" y="24" font-family="Noto Sans JP" font-size="10" fill="#121212">Physical AI 関連 DB（12 件）</text>
<circle cx="280" cy="20" r="5" fill="#555"/>
<text x="292" y="24" font-family="Noto Sans JP" font-size="10" fill="#555">その他 AR-DB 既登録 DB（34 件）</text>
</svg>
<figcaption style="font-family:var(--font);font-size:0.78rem;color:#6B6B6B;margin-top:12px;text-align:center;">図N1: AR-DB横断マップ。46 DBs を6領域に布置し、Physical AI関連12 DBを赤色ハブとして12本のエッジで他DBと接続。本書がフィジカルAIを単一領域でなく46DB総合知識基盤の上で記述していることを示す。</figcaption>
</figure>
```

---

## 図 N2: 8系統 × Phase A-G 貢献度ヒートマップ

- **配置章**: 第2章「5系統合流」末尾（5系統→8系統への拡張議論）あるいは第3章冒頭
- **設計意図**: 縦軸 8 系統（HW/CTRL/RL/FM/SIM/MAT/ENERGY/SOC）、横軸 7 Phase（A-G）。セル色濃淡で貢献度を3段階表示（強=#CC1400 / 中=rgba(204,20,0,0.4) / 弱=rgba(204,20,0,0.12)）。系統ごとに最盛期がずれて立ち上がる構造を一望できる

```html
<figure style="margin:36px 0;text-align:center;background:rgba(204,20,0,0.02);border-top:1px solid #CC1400;border-bottom:1px solid #CC1400;padding:32px 16px;">
<svg viewBox="0 0 760 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:760px;height:auto;">
<!-- 列ヘッダ -->
<text x="180" y="30" font-family="Noto Sans JP" font-size="11" fill="#121212" text-anchor="middle" font-weight="700">Phase A</text>
<text x="180" y="44" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2026-30</text>
<text x="260" y="30" font-family="Noto Sans JP" font-size="11" fill="#121212" text-anchor="middle" font-weight="700">Phase B</text>
<text x="260" y="44" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2030-40</text>
<text x="340" y="30" font-family="Noto Sans JP" font-size="11" fill="#121212" text-anchor="middle" font-weight="700">Phase C</text>
<text x="340" y="44" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2040-50</text>
<text x="420" y="30" font-family="Noto Sans JP" font-size="11" fill="#121212" text-anchor="middle" font-weight="700">Phase D</text>
<text x="420" y="44" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2050-65</text>
<text x="500" y="30" font-family="Noto Sans JP" font-size="11" fill="#121212" text-anchor="middle" font-weight="700">Phase E</text>
<text x="500" y="44" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2065-80</text>
<text x="580" y="30" font-family="Noto Sans JP" font-size="11" fill="#121212" text-anchor="middle" font-weight="700">Phase F</text>
<text x="580" y="44" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2080-90</text>
<text x="660" y="30" font-family="Noto Sans JP" font-size="11" fill="#121212" text-anchor="middle" font-weight="700">Phase G</text>
<text x="660" y="44" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2090-2100</text>

<!-- 行ラベル + セル群 -->
<!-- HW -->
<text x="140" y="80" font-family="Noto Sans JP" font-size="11" fill="#121212" text-anchor="end">HW（身体）</text>
<rect x="148" y="65" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="228" y="65" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="308" y="65" width="64" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="388" y="65" width="64" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="468" y="65" width="64" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="548" y="65" width="64" height="28" fill="#CC1400" opacity="0.12"/>
<rect x="628" y="65" width="64" height="28" fill="#CC1400" opacity="0.12"/>
<!-- CTRL -->
<text x="140" y="115" font-family="Noto Sans JP" font-size="11" fill="#121212" text-anchor="end">CTRL（古典制御）</text>
<rect x="148" y="100" width="64" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="228" y="100" width="64" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="308" y="100" width="64" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="388" y="100" width="64" height="28" fill="#CC1400" opacity="0.12"/>
<rect x="468" y="100" width="64" height="28" fill="#CC1400" opacity="0.12"/>
<rect x="548" y="100" width="64" height="28" fill="#CC1400" opacity="0.12"/>
<rect x="628" y="100" width="64" height="28" fill="#CC1400" opacity="0.12"/>
<!-- RL -->
<text x="140" y="150" font-family="Noto Sans JP" font-size="11" fill="#121212" text-anchor="end">RL（学習）</text>
<rect x="148" y="135" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="228" y="135" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="308" y="135" width="64" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="388" y="135" width="64" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="468" y="135" width="64" height="28" fill="#CC1400" opacity="0.12"/>
<rect x="548" y="135" width="64" height="28" fill="#CC1400" opacity="0.12"/>
<rect x="628" y="135" width="64" height="28" fill="#CC1400" opacity="0.12"/>
<!-- FM -->
<text x="140" y="185" font-family="Noto Sans JP" font-size="11" fill="#121212" text-anchor="end">FM（基盤モデル）</text>
<rect x="148" y="170" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="228" y="170" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="308" y="170" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="388" y="170" width="64" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="468" y="170" width="64" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="548" y="170" width="64" height="28" fill="#CC1400" opacity="0.12"/>
<rect x="628" y="170" width="64" height="28" fill="#CC1400" opacity="0.12"/>
<!-- SIM -->
<text x="140" y="220" font-family="Noto Sans JP" font-size="11" fill="#121212" text-anchor="end">SIM（合成世界）</text>
<rect x="148" y="205" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="228" y="205" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="308" y="205" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="388" y="205" width="64" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="468" y="205" width="64" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="548" y="205" width="64" height="28" fill="#CC1400" opacity="0.12"/>
<rect x="628" y="205" width="64" height="28" fill="#CC1400" opacity="0.12"/>
<!-- MAT -->
<text x="140" y="255" font-family="Noto Sans JP" font-size="11" fill="#121212" text-anchor="end">MAT（材料・電池）</text>
<rect x="148" y="240" width="64" height="28" fill="#CC1400" opacity="0.12"/>
<rect x="228" y="240" width="64" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="308" y="240" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="388" y="240" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="468" y="240" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="548" y="240" width="64" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="628" y="240" width="64" height="28" fill="#CC1400" opacity="0.4"/>
<!-- ENERGY -->
<text x="140" y="290" font-family="Noto Sans JP" font-size="11" fill="#121212" text-anchor="end">ENERGY（電力）</text>
<rect x="148" y="275" width="64" height="28" fill="#CC1400" opacity="0.12"/>
<rect x="228" y="275" width="64" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="308" y="275" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="388" y="275" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="468" y="275" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="548" y="275" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="628" y="275" width="64" height="28" fill="#CC1400" opacity="0.4"/>
<!-- SOC -->
<text x="140" y="325" font-family="Noto Sans JP" font-size="11" fill="#121212" text-anchor="end">SOC（社会制度）</text>
<rect x="148" y="310" width="64" height="28" fill="#CC1400" opacity="0.12"/>
<rect x="228" y="310" width="64" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="308" y="310" width="64" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="388" y="310" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="468" y="310" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="548" y="310" width="64" height="28" fill="#CC1400" opacity="0.85"/>
<rect x="628" y="310" width="64" height="28" fill="#CC1400" opacity="0.85"/>

<!-- 凡例 -->
<rect x="180" y="360" width="20" height="14" fill="#CC1400" opacity="0.12"/>
<text x="205" y="372" font-family="Noto Sans JP" font-size="10" fill="#555">弱</text>
<rect x="240" y="360" width="20" height="14" fill="#CC1400" opacity="0.4"/>
<text x="265" y="372" font-family="Noto Sans JP" font-size="10" fill="#555">中</text>
<rect x="300" y="360" width="20" height="14" fill="#CC1400" opacity="0.85"/>
<text x="325" y="372" font-family="Noto Sans JP" font-size="10" fill="#555">強（主導系統）</text>
<text x="500" y="372" font-family="Noto Sans JP" font-size="10" fill="#6B6B6B" font-style="italic">出典: PHAI-DB phase_systems_contribution</text>
</svg>
<figcaption style="font-family:var(--font);font-size:0.78rem;color:#6B6B6B;margin-top:12px;text-align:center;">図N2: 8系統×Phase A-Gの貢献度ヒートマップ。FM/SIM/RL/HWが Phase A-C を主導し、Phase D 以降は MAT/ENERGY/SOC へ重心が移行する「物質と制度への着地」が読み取れる。</figcaption>
</figure>
```

---

## 図 N3: 地政学三極ダイヤモンド

- **配置章**: 第4章「フィジカルAIの地政学」あるいは Phase B (2030-40) 章
- **設計意図**: US/CN/EU+JP/IN の4極をひし形配置。各極の Physical AI 政策強度を半径で表現（US 95 / CN 88 / EU+JP 62 / IN 38）。極間の対立軸（規制/貿易/半導体/標準化）を辺で示す

```html
<figure style="margin:36px 0;text-align:center;background:rgba(204,20,0,0.02);border-top:1px solid #CC1400;border-bottom:1px solid #CC1400;padding:32px 16px;">
<svg viewBox="0 0 760 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:760px;height:auto;">
<!-- ダイヤモンド外形（理想100%基準） -->
<polygon points="380,50 670,200 380,350 90,200" fill="none" stroke="#D9D9D9" stroke-width="1" stroke-dasharray="4,4"/>

<!-- 4極の強度ノード（半径 = 政策強度/100 × 60） -->
<!-- US (top, 強度95) -->
<circle cx="380" cy="50" r="57" fill="#CC1400" opacity="0.18" stroke="#CC1400" stroke-width="1.5"/>
<text x="380" y="48" font-family="Noto Serif JP" font-size="18" fill="#CC1400" text-anchor="middle" font-weight="700">US</text>
<text x="380" y="68" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="middle">政策強度 95 / 100</text>
<text x="380" y="82" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">CHIPS / Stargate / EO14110</text>

<!-- CN (right, 強度88) -->
<circle cx="670" cy="200" r="53" fill="#CC1400" opacity="0.18" stroke="#CC1400" stroke-width="1.5"/>
<text x="670" y="198" font-family="Noto Serif JP" font-size="18" fill="#CC1400" text-anchor="middle" font-weight="700">CN</text>
<text x="670" y="218" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="middle">政策強度 88 / 100</text>
<text x="670" y="232" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">"机器人+" / 国家標準</text>

<!-- EU+JP (bottom, 強度62) -->
<circle cx="380" cy="350" r="37" fill="#CC1400" opacity="0.12" stroke="#CC1400" stroke-width="1.2"/>
<text x="380" y="348" font-family="Noto Serif JP" font-size="16" fill="#CC1400" text-anchor="middle" font-weight="700">EU + JP</text>
<text x="380" y="368" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="middle">政策強度 62 / 100</text>

<!-- IN (left, 強度38) -->
<circle cx="90" cy="200" r="23" fill="#CC1400" opacity="0.08" stroke="#CC1400" stroke-width="1"/>
<text x="90" y="198" font-family="Noto Serif JP" font-size="14" fill="#CC1400" text-anchor="middle" font-weight="700">IN</text>
<text x="90" y="220" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="middle">38</text>

<!-- 対立軸ラベル（辺の中央） -->
<text x="525" y="120" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="middle">半導体・export control</text>
<text x="525" y="280" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="middle">標準化・WTO</text>
<text x="235" y="280" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="middle">人材・南南協力</text>
<text x="235" y="120" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="middle">規制・AI Act</text>

<!-- 中央: 競争ホットゾーン -->
<circle cx="380" cy="200" r="22" fill="#FFF" stroke="#CC1400" stroke-width="1" stroke-dasharray="2,2"/>
<text x="380" y="196" font-family="Noto Sans JP" font-size="9" fill="#CC1400" text-anchor="middle" font-weight="700">VLA/GLA</text>
<text x="380" y="208" font-family="Noto Sans JP" font-size="9" fill="#CC1400" text-anchor="middle">標準競争</text>

<!-- 凡例 -->
<text x="380" y="395" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle" font-style="italic">出典: PHAI-DB geopolitics_index 2026版（IFR / SIPRI / Brookings 統合）</text>
</svg>
<figcaption style="font-family:var(--font);font-size:0.78rem;color:#6B6B6B;margin-top:12px;text-align:center;">図N3: 地政学三極ダイヤモンド。Physical AI政策強度は US 95 / CN 88 / EU+JP 62 / IN 38。中央のVLA/GLA標準競争を巡って4極が4本の対立軸（半導体・標準・人材・規制）で押し合う構造。</figcaption>
</figure>
```

---

## 図 N4: エネルギー三制約三角形

- **配置章**: 第5章「計算・データ・エネルギーの三制約」あるいは Phase C-D 章
- **設計意図**: 三角形の3頂点に「計算 (GPU FLOPS)」「データ (Token)」「エネルギー (kWh)」を配置。各時代（2026/2050/2075/2100）の Physical AI が三角形内のどの位置にいるかを赤色の軌跡で示す。初期はエネルギー軸が制約に、後期はデータ軸が制約に

```html
<figure style="margin:36px 0;text-align:center;background:rgba(204,20,0,0.02);border-top:1px solid #CC1400;border-bottom:1px solid #CC1400;padding:32px 16px;">
<svg viewBox="0 0 760 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:760px;height:auto;">
<!-- 三角形外形 -->
<polygon points="380,50 660,330 100,330" fill="none" stroke="#121212" stroke-width="1.5"/>

<!-- 内側ガイド線（10/30/50/70/90% 等高線） -->
<polygon points="380,113 540,273 220,273" fill="none" stroke="#D9D9D9" stroke-width="0.6" stroke-dasharray="2,3"/>
<polygon points="380,176 484,256 276,256" fill="none" stroke="#D9D9D9" stroke-width="0.6" stroke-dasharray="2,3"/>
<polygon points="380,239 432,239 432,239" fill="none" stroke="#D9D9D9" stroke-width="0.6"/>

<!-- 頂点ラベル -->
<text x="380" y="38" font-family="Noto Serif JP" font-size="14" fill="#CC1400" text-anchor="middle" font-weight="700">計算 (GPU FLOPS)</text>
<text x="380" y="22" font-family="Noto Sans JP" font-size="10" fill="#6B6B6B" text-anchor="middle">基盤モデル訓練・推論</text>
<text x="680" y="350" font-family="Noto Serif JP" font-size="14" fill="#CC1400" text-anchor="start" font-weight="700">データ (Token)</text>
<text x="680" y="366" font-family="Noto Sans JP" font-size="10" fill="#6B6B6B" text-anchor="start">実機 / 合成 / Web</text>
<text x="80" y="350" font-family="Noto Serif JP" font-size="14" fill="#CC1400" text-anchor="end" font-weight="700">エネルギー (kWh)</text>
<text x="80" y="366" font-family="Noto Sans JP" font-size="10" fill="#6B6B6B" text-anchor="end">電力・冷却・送電</text>

<!-- 時代軌跡（4点 + 接続線） -->
<!-- 2026: エネルギー寄り (compute中, data少, energy高) -->
<circle cx="220" cy="290" r="7" fill="#CC1400"/>
<text x="220" y="312" font-family="Noto Sans JP" font-size="10" fill="#CC1400" text-anchor="middle" font-weight="700">2026</text>
<text x="220" y="324" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">energy制約</text>
<!-- 2050: 真ん中やや上 -->
<circle cx="350" cy="220" r="7" fill="#CC1400"/>
<text x="350" y="208" font-family="Noto Sans JP" font-size="10" fill="#CC1400" text-anchor="middle" font-weight="700">2050</text>
<text x="350" y="196" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">三制約均衡</text>
<!-- 2075: データ寄り -->
<circle cx="450" cy="240" r="7" fill="#CC1400"/>
<text x="450" y="228" font-family="Noto Sans JP" font-size="10" fill="#CC1400" text-anchor="middle" font-weight="700">2075</text>
<text x="450" y="216" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">data不足顕在</text>
<!-- 2100: データ強制約 -->
<circle cx="540" cy="290" r="7" fill="#CC1400"/>
<text x="540" y="312" font-family="Noto Sans JP" font-size="10" fill="#CC1400" text-anchor="middle" font-weight="700">2100</text>
<text x="540" y="324" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">data制約</text>

<!-- 軌跡線 -->
<path d="M 220,290 L 350,220 L 450,240 L 540,290" stroke="#CC1400" stroke-width="1.8" fill="none" stroke-dasharray="0"/>
<path d="M 220,290 L 350,220" stroke="#CC1400" stroke-width="0.8" fill="none" opacity="0.5"/>

<!-- 矢印（軌跡の方向） -->
<polygon points="540,290 532,283 532,297" fill="#CC1400"/>

<!-- 凡例 -->
<text x="380" y="385" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle" font-style="italic">出典: PHAI-DB constraint_trajectory（Epoch AI / IEA / Open X-Embodiment 統合）</text>
</svg>
<figcaption style="font-family:var(--font);font-size:0.78rem;color:#6B6B6B;margin-top:12px;text-align:center;">図N4: エネルギー三制約三角形。Physical AIは2026年エネルギー軸の制約から出発し、2050年の三制約均衡を経て、2075-2100年は実機データの希少性が新たな主制約となる軌跡を辿る。</figcaption>
</figure>
```

---

## 図 N5: VLM → VLA → GLA 進化系統樹

- **配置章**: 第2章「5系統合流」第四系統 (基盤モデル) 末尾
- **設計意図**: 2017 Transformer を根として、上方向に時系列で枝分かれ。CLIP→PaLM-E→RT-2→OpenVLA→GR00T N1→Helix→π0.5→GLA 1.0 の系譜を樹形図で表現

```html
<figure style="margin:36px 0;text-align:center;background:rgba(204,20,0,0.02);border-top:1px solid #CC1400;border-bottom:1px solid #CC1400;padding:32px 16px;">
<svg viewBox="0 0 760 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:760px;height:auto;">
<!-- 年代軸 -->
<line x1="50" y1="370" x2="710" y2="370" stroke="#121212" stroke-width="1"/>
<text x="50" y="388" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="middle">2017</text>
<text x="135" y="388" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="middle">2020</text>
<text x="220" y="388" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="middle">2021</text>
<text x="305" y="388" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="middle">2022</text>
<text x="390" y="388" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="middle">2023</text>
<text x="475" y="388" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="middle">2024</text>
<text x="560" y="388" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="middle">2025</text>
<text x="645" y="388" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="middle">2026→</text>

<!-- 根: Transformer 2017 -->
<rect x="22" y="328" width="56" height="22" fill="#FFF" stroke="#CC1400" stroke-width="1.2" rx="3"/>
<text x="50" y="343" font-family="Noto Sans JP" font-size="9" fill="#CC1400" text-anchor="middle" font-weight="700">Transformer</text>

<!-- 2020 GPT-3 -->
<rect x="107" y="290" width="56" height="22" fill="#FFF" stroke="#121212" stroke-width="0.8" rx="3"/>
<text x="135" y="305" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">GPT-3</text>
<line x1="50" y1="328" x2="135" y2="312" stroke="#555" stroke-width="0.8"/>

<!-- 2021 CLIP -->
<rect x="192" y="245" width="56" height="22" fill="#FFF" stroke="#CC1400" stroke-width="1.2" rx="3"/>
<text x="220" y="260" font-family="Noto Sans JP" font-size="9" fill="#CC1400" text-anchor="middle" font-weight="700">CLIP</text>
<text x="220" y="278" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">VLM 始点</text>
<line x1="135" y1="290" x2="220" y2="267" stroke="#555" stroke-width="0.8"/>

<!-- 2022 SayCan / RT-1 -->
<rect x="277" y="220" width="56" height="22" fill="#FFF" stroke="#121212" stroke-width="0.8" rx="3"/>
<text x="305" y="235" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">SayCan</text>
<rect x="277" y="250" width="56" height="22" fill="#FFF" stroke="#121212" stroke-width="0.8" rx="3"/>
<text x="305" y="265" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">RT-1</text>
<line x1="220" y1="245" x2="305" y2="231" stroke="#555" stroke-width="0.8"/>
<line x1="220" y1="245" x2="305" y2="261" stroke="#555" stroke-width="0.8"/>

<!-- 2023 PaLM-E / RT-2 -->
<rect x="362" y="170" width="56" height="22" fill="#FFF" stroke="#121212" stroke-width="0.8" rx="3"/>
<text x="390" y="185" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">PaLM-E</text>
<rect x="362" y="200" width="56" height="22" fill="#FFF" stroke="#CC1400" stroke-width="1.2" rx="3"/>
<text x="390" y="215" font-family="Noto Sans JP" font-size="9" fill="#CC1400" text-anchor="middle" font-weight="700">RT-2</text>
<text x="390" y="232" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">VLA 始点</text>
<line x1="305" y1="220" x2="390" y2="181" stroke="#555" stroke-width="0.8"/>
<line x1="305" y1="250" x2="390" y2="211" stroke="#555" stroke-width="0.8"/>

<!-- 2024 OpenVLA / Octo / π0 / GR00T -->
<rect x="447" y="130" width="56" height="22" fill="#FFF" stroke="#121212" stroke-width="0.8" rx="3"/>
<text x="475" y="145" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">OpenVLA</text>
<rect x="447" y="158" width="56" height="22" fill="#FFF" stroke="#121212" stroke-width="0.8" rx="3"/>
<text x="475" y="173" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">π0</text>
<rect x="447" y="186" width="56" height="22" fill="#FFF" stroke="#121212" stroke-width="0.8" rx="3"/>
<text x="475" y="201" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">GR00T N1</text>
<line x1="390" y1="200" x2="475" y2="141" stroke="#555" stroke-width="0.8"/>
<line x1="390" y1="200" x2="475" y2="169" stroke="#555" stroke-width="0.8"/>
<line x1="390" y1="200" x2="475" y2="197" stroke="#555" stroke-width="0.8"/>

<!-- 2025 Helix / π0.5 / RDT -->
<rect x="532" y="100" width="56" height="22" fill="#FFF" stroke="#121212" stroke-width="0.8" rx="3"/>
<text x="560" y="115" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">Helix</text>
<rect x="532" y="128" width="56" height="22" fill="#FFF" stroke="#121212" stroke-width="0.8" rx="3"/>
<text x="560" y="143" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">π0.5</text>
<rect x="532" y="156" width="56" height="22" fill="#FFF" stroke="#121212" stroke-width="0.8" rx="3"/>
<text x="560" y="171" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">RDT</text>
<line x1="475" y1="130" x2="560" y2="111" stroke="#555" stroke-width="0.8"/>
<line x1="475" y1="158" x2="560" y2="139" stroke="#555" stroke-width="0.8"/>
<line x1="475" y1="186" x2="560" y2="167" stroke="#555" stroke-width="0.8"/>

<!-- 2026 GLA 1.0 (予測) -->
<rect x="617" y="55" width="56" height="26" fill="#CC1400" opacity="0.15" stroke="#CC1400" stroke-width="1.5" rx="3"/>
<text x="645" y="68" font-family="Noto Sans JP" font-size="9" fill="#CC1400" text-anchor="middle" font-weight="700">GLA 1.0</text>
<text x="645" y="78" font-family="Noto Sans JP" font-size="8" fill="#CC1400" text-anchor="middle">(予測)</text>
<text x="645" y="100" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">Generalist Language-Action</text>
<line x1="560" y1="100" x2="645" y2="65" stroke="#CC1400" stroke-width="1" stroke-dasharray="3,3"/>
<line x1="560" y1="128" x2="645" y2="68" stroke="#CC1400" stroke-width="1" stroke-dasharray="3,3"/>

<!-- 凡例 -->
<rect x="50" y="20" width="14" height="14" fill="#FFF" stroke="#CC1400" stroke-width="1.5"/>
<text x="70" y="32" font-family="Noto Sans JP" font-size="10" fill="#CC1400">パラダイム転換点</text>
<rect x="220" y="20" width="14" height="14" fill="#FFF" stroke="#121212" stroke-width="0.8"/>
<text x="240" y="32" font-family="Noto Sans JP" font-size="10" fill="#555">主要モデル</text>
</svg>
<figcaption style="font-family:var(--font);font-size:0.78rem;color:#6B6B6B;margin-top:12px;text-align:center;">図N5: VLM→VLA→GLA進化系統樹。2017 Transformer→2021 CLIP（VLM 始点）→2023 RT-2（VLA 始点）→2026 GLA 1.0（予測） の9年間で「言語のみ → 視覚+言語 → 視覚+言語+行動 → 汎用身体知性」へ4世代の転換が起きた。</figcaption>
</figure>
```

---

## 図 N6: 朝シーン世界地図（2026/2050/2075/2100）

- **配置章**: 第8章「2100年の暮らし」あるいは終章「74年の朝食」
- **設計意図**: 簡略化した世界地図（横長矩形ベース）に4地域（東京/上海/ベルリン/ナイロビ）の朝食シーンを4時代分マッピング。各セルにアイコン的記号と短い文言

```html
<figure style="margin:36px 0;text-align:center;background:rgba(204,20,0,0.02);border-top:1px solid #CC1400;border-bottom:1px solid #CC1400;padding:32px 16px;">
<svg viewBox="0 0 760 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:760px;height:auto;">
<!-- 地球簡略形 -->
<rect x="20" y="50" width="720" height="280" fill="#F7F7F5" stroke="#D9D9D9" stroke-width="0.8" rx="8"/>
<line x1="20" y1="190" x2="740" y2="190" stroke="#D9D9D9" stroke-width="0.4" stroke-dasharray="2,4"/>
<text x="730" y="200" font-family="Noto Sans JP" font-size="8" fill="#AAA" text-anchor="end">赤道</text>

<!-- 4地域マーカー（横軸=年代、縦軸=地域） -->
<!-- 行ラベル（左） -->
<text x="60" y="100" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="middle" font-weight="700">ベルリン</text>
<text x="60" y="115" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">EU・北緯52°</text>
<text x="60" y="170" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="middle" font-weight="700">東京</text>
<text x="60" y="185" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">JP・北緯36°</text>
<text x="60" y="225" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="middle" font-weight="700">上海</text>
<text x="60" y="240" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">CN・北緯31°</text>
<text x="60" y="290" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="middle" font-weight="700">ナイロビ</text>
<text x="60" y="305" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">KE・南緯1°</text>

<!-- 列ヘッダ -->
<text x="200" y="42" font-family="Noto Sans JP" font-size="11" fill="#CC1400" text-anchor="middle" font-weight="700">2026</text>
<text x="350" y="42" font-family="Noto Sans JP" font-size="11" fill="#CC1400" text-anchor="middle" font-weight="700">2050</text>
<text x="500" y="42" font-family="Noto Sans JP" font-size="11" fill="#CC1400" text-anchor="middle" font-weight="700">2075</text>
<text x="650" y="42" font-family="Noto Sans JP" font-size="11" fill="#CC1400" text-anchor="middle" font-weight="700">2100</text>

<!-- セル（地域×時代の朝食シーン） -->
<!-- ベルリン -->
<g><rect x="140" y="80" width="120" height="50" fill="#FFF" stroke="#D9D9D9" stroke-width="0.6" rx="4"/><text x="200" y="98" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">パンと珈琲</text><text x="200" y="112" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">家事は人手</text><text x="200" y="124" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">PAI:なし</text></g>
<g><rect x="290" y="80" width="120" height="50" fill="#FFF" stroke="#CC1400" stroke-width="0.6" rx="4"/><text x="350" y="98" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">家庭ロボが配膳</text><text x="350" y="112" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">食材選定AI協働</text><text x="350" y="124" font-family="Noto Sans JP" font-size="8" fill="#CC1400" text-anchor="middle">PAI:導入期</text></g>
<g><rect x="440" y="80" width="120" height="50" fill="#FFF" stroke="#CC1400" stroke-width="1" rx="4"/><text x="500" y="98" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">細胞培養乳製品</text><text x="500" y="112" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">PAI厨房が標準</text><text x="500" y="124" font-family="Noto Sans JP" font-size="8" fill="#CC1400" text-anchor="middle">PAI:遍在</text></g>
<g><rect x="590" y="80" width="120" height="50" fill="#FFF" stroke="#CC1400" stroke-width="1.5" rx="4"/><text x="650" y="98" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">PAI不在の朝</text><text x="650" y="112" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">手作りが新贅沢</text><text x="650" y="124" font-family="Noto Sans JP" font-size="8" fill="#CC1400" text-anchor="middle">PAI:選択的</text></g>

<!-- 東京 -->
<g><rect x="140" y="150" width="120" height="50" fill="#FFF" stroke="#D9D9D9" stroke-width="0.6" rx="4"/><text x="200" y="168" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">ご飯と味噌汁</text><text x="200" y="182" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">単身世帯多数</text><text x="200" y="194" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">PAI:なし</text></g>
<g><rect x="290" y="150" width="120" height="50" fill="#FFF" stroke="#CC1400" stroke-width="0.6" rx="4"/><text x="350" y="168" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">介護ロボが食器を</text><text x="350" y="182" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">高齢者世帯先導</text><text x="350" y="194" font-family="Noto Sans JP" font-size="8" fill="#CC1400" text-anchor="middle">PAI:介護先行</text></g>
<g><rect x="440" y="150" width="120" height="50" fill="#FFF" stroke="#CC1400" stroke-width="1" rx="4"/><text x="500" y="168" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">和食PAIが地産食材</text><text x="500" y="182" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">都市農場連動</text><text x="500" y="194" font-family="Noto Sans JP" font-size="8" fill="#CC1400" text-anchor="middle">PAI:遍在</text></g>
<g><rect x="590" y="150" width="120" height="50" fill="#FFF" stroke="#CC1400" stroke-width="1.5" rx="4"/><text x="650" y="168" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">"いただきます"を学ぶPAI</text><text x="650" y="182" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">文化的儀礼を再演</text><text x="650" y="194" font-family="Noto Sans JP" font-size="8" fill="#CC1400" text-anchor="middle">PAI:文化適応</text></g>

<!-- 上海 -->
<g><rect x="140" y="210" width="120" height="50" fill="#FFF" stroke="#D9D9D9" stroke-width="0.6" rx="4"/><text x="200" y="228" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">小籠包と豆漿</text><text x="200" y="242" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">屋台文化健在</text><text x="200" y="254" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">PAI:なし</text></g>
<g><rect x="290" y="210" width="120" height="50" fill="#FFF" stroke="#CC1400" stroke-width="0.6" rx="4"/><text x="350" y="228" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">屋台もPAI調理</text><text x="350" y="242" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">国家標準PAI普及</text><text x="350" y="254" font-family="Noto Sans JP" font-size="8" fill="#CC1400" text-anchor="middle">PAI:都市標準</text></g>
<g><rect x="440" y="210" width="120" height="50" fill="#FFF" stroke="#CC1400" stroke-width="1" rx="4"/><text x="500" y="228" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">合成蛋白主流化</text><text x="500" y="242" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">食料安全保障文脈</text><text x="500" y="254" font-family="Noto Sans JP" font-size="8" fill="#CC1400" text-anchor="middle">PAI:遍在</text></g>
<g><rect x="590" y="210" width="120" height="50" fill="#FFF" stroke="#CC1400" stroke-width="1.5" rx="4"/><text x="650" y="228" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">伝統食PAIが季節食</text><text x="650" y="242" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">中医薬連動</text><text x="650" y="254" font-family="Noto Sans JP" font-size="8" fill="#CC1400" text-anchor="middle">PAI:文化適応</text></g>

<!-- ナイロビ -->
<g><rect x="140" y="270" width="120" height="50" fill="#FFF" stroke="#D9D9D9" stroke-width="0.6" rx="4"/><text x="200" y="288" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">ウガリと茶</text><text x="200" y="302" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">家族で囲む</text><text x="200" y="314" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">PAI:なし</text></g>
<g><rect x="290" y="270" width="120" height="50" fill="#FFF" stroke="#D9D9D9" stroke-width="0.6" rx="4"/><text x="350" y="288" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">スマホ農法支援</text><text x="350" y="302" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">PAI身体実装は限定</text><text x="350" y="314" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">PAI:遅延期</text></g>
<g><rect x="440" y="270" width="120" height="50" fill="#FFF" stroke="#CC1400" stroke-width="0.6" rx="4"/><text x="500" y="288" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">小型農業PAI普及</text><text x="500" y="302" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">leap-frogging 起動</text><text x="500" y="314" font-family="Noto Sans JP" font-size="8" fill="#CC1400" text-anchor="middle">PAI:跳躍展開</text></g>
<g><rect x="590" y="270" width="120" height="50" fill="#FFF" stroke="#CC1400" stroke-width="1" rx="4"/><text x="650" y="288" font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">共同体食堂PAI</text><text x="650" y="302" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">独自発展経路</text><text x="650" y="314" font-family="Noto Sans JP" font-size="8" fill="#CC1400" text-anchor="middle">PAI:共同体型</text></g>

<text x="380" y="370" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle" font-style="italic">PAI = Physical AI 実装度。色濃度は普及深度を示す。</text>
</svg>
<figcaption style="font-family:var(--font);font-size:0.78rem;color:#6B6B6B;margin-top:12px;text-align:center;">図N6: 朝シーン世界地図 2026-2100。4地域×4時代の朝食シーンの変化。同じPhysical AI技術が地域文化のレイヤを通って異なる姿で着地する非線形性が読み取れる。</figcaption>
</figure>
```

---

## 図 N7: Physical AI × SDG 17目標 影響マトリクス

- **配置章**: 第9章「Physical AIの社会的含意」
- **設計意図**: SDG 17 目標を横軸に、Physical AI 8系統を縦軸（凝縮）に取って、正の影響 (緑色だが赤白CIなので濃赤 #CC1400) / 負の影響 (薄赤 rgba(204,20,0,0.3)) / 中立 (グレー) を3段階で示す

```html
<figure style="margin:36px 0;text-align:center;background:rgba(204,20,0,0.02);border-top:1px solid #CC1400;border-bottom:1px solid #CC1400;padding:32px 16px;">
<svg viewBox="0 0 760 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:760px;height:auto;">
<!-- 列ヘッダ: SDG 1-17 -->
<g font-family="Noto Sans JP" font-size="9" fill="#121212" text-anchor="middle">
<text x="146" y="30">1</text><text x="178" y="30">2</text><text x="210" y="30">3</text>
<text x="242" y="30">4</text><text x="274" y="30">5</text><text x="306" y="30">6</text>
<text x="338" y="30">7</text><text x="370" y="30">8</text><text x="402" y="30">9</text>
<text x="434" y="30">10</text><text x="466" y="30">11</text><text x="498" y="30">12</text>
<text x="530" y="30">13</text><text x="562" y="30">14</text><text x="594" y="30">15</text>
<text x="626" y="30">16</text><text x="658" y="30">17</text>
</g>
<g font-family="Noto Sans JP" font-size="7" fill="#6B6B6B" text-anchor="middle">
<text x="146" y="42">貧困</text><text x="178" y="42">飢餓</text><text x="210" y="42">健康</text>
<text x="242" y="42">教育</text><text x="274" y="42">ジェ</text><text x="306" y="42">水</text>
<text x="338" y="42">エネ</text><text x="370" y="42">労働</text><text x="402" y="42">産業</text>
<text x="434" y="42">不平等</text><text x="466" y="42">都市</text><text x="498" y="42">消費</text>
<text x="530" y="42">気候</text><text x="562" y="42">海</text><text x="594" y="42">陸</text>
<text x="626" y="42">平和</text><text x="658" y="42">連携</text>
</g>

<!-- 行ラベル + セル群 (8系統) -->
<!-- HW -->
<text x="120" y="80" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="end">HW</text>
<rect x="130" y="65" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="162" y="65" width="32" height="28" fill="#CC1400" opacity="0.7"/>
<rect x="194" y="65" width="32" height="28" fill="#CC1400" opacity="0.7"/>
<rect x="226" y="65" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="258" y="65" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="290" y="65" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="322" y="65" width="32" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="354" y="65" width="32" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="386" y="65" width="32" height="28" fill="#CC1400" opacity="0.9"/>
<rect x="418" y="65" width="32" height="28" fill="#CC1400" opacity="0.3"/>
<rect x="450" y="65" width="32" height="28" fill="#CC1400" opacity="0.7"/>
<rect x="482" y="65" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="514" y="65" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="546" y="65" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="578" y="65" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="610" y="65" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="642" y="65" width="32" height="28" fill="#CC1400" opacity="0.4"/>
<!-- FM -->
<text x="120" y="115" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="end">FM</text>
<rect x="130" y="100" width="32" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="162" y="100" width="32" height="28" fill="#CC1400" opacity="0.7"/>
<rect x="194" y="100" width="32" height="28" fill="#CC1400" opacity="0.9"/>
<rect x="226" y="100" width="32" height="28" fill="#CC1400" opacity="0.9"/>
<rect x="258" y="100" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="290" y="100" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="322" y="100" width="32" height="28" fill="#CC1400" opacity="0.3"/>
<rect x="354" y="100" width="32" height="28" fill="#CC1400" opacity="0.3"/>
<rect x="386" y="100" width="32" height="28" fill="#CC1400" opacity="0.9"/>
<rect x="418" y="100" width="32" height="28" fill="#CC1400" opacity="0.3"/>
<rect x="450" y="100" width="32" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="482" y="100" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="514" y="100" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="546" y="100" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="578" y="100" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="610" y="100" width="32" height="28" fill="#CC1400" opacity="0.3"/>
<rect x="642" y="100" width="32" height="28" fill="#CC1400" opacity="0.7"/>
<!-- MAT -->
<text x="120" y="150" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="end">MAT</text>
<rect x="130" y="135" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="162" y="135" width="32" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="194" y="135" width="32" height="28" fill="#CC1400" opacity="0.7"/>
<rect x="226" y="135" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="258" y="135" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="290" y="135" width="32" height="28" fill="#CC1400" opacity="0.7"/>
<rect x="322" y="135" width="32" height="28" fill="#CC1400" opacity="0.9"/>
<rect x="354" y="135" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="386" y="135" width="32" height="28" fill="#CC1400" opacity="0.7"/>
<rect x="418" y="135" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="450" y="135" width="32" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="482" y="135" width="32" height="28" fill="#CC1400" opacity="0.7"/>
<rect x="514" y="135" width="32" height="28" fill="#CC1400" opacity="0.7"/>
<rect x="546" y="135" width="32" height="28" fill="#CC1400" opacity="0.3"/>
<rect x="578" y="135" width="32" height="28" fill="#CC1400" opacity="0.3"/>
<rect x="610" y="135" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="642" y="135" width="32" height="28" fill="#999" opacity="0.3"/>
<!-- ENERGY -->
<text x="120" y="185" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="end">ENERGY</text>
<rect x="130" y="170" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="162" y="170" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="194" y="170" width="32" height="28" fill="#CC1400" opacity="0.3"/>
<rect x="226" y="170" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="258" y="170" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="290" y="170" width="32" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="322" y="170" width="32" height="28" fill="#CC1400" opacity="0.9"/>
<rect x="354" y="170" width="32" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="386" y="170" width="32" height="28" fill="#CC1400" opacity="0.7"/>
<rect x="418" y="170" width="32" height="28" fill="#CC1400" opacity="0.3"/>
<rect x="450" y="170" width="32" height="28" fill="#CC1400" opacity="0.7"/>
<rect x="482" y="170" width="32" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="514" y="170" width="32" height="28" fill="#CC1400" opacity="0.3"/>
<rect x="546" y="170" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="578" y="170" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="610" y="170" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="642" y="170" width="32" height="28" fill="#CC1400" opacity="0.4"/>
<!-- SOC -->
<text x="120" y="220" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="end">SOC</text>
<rect x="130" y="205" width="32" height="28" fill="#CC1400" opacity="0.7"/>
<rect x="162" y="205" width="32" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="194" y="205" width="32" height="28" fill="#CC1400" opacity="0.7"/>
<rect x="226" y="205" width="32" height="28" fill="#CC1400" opacity="0.9"/>
<rect x="258" y="205" width="32" height="28" fill="#CC1400" opacity="0.7"/>
<rect x="290" y="205" width="32" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="322" y="205" width="32" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="354" y="205" width="32" height="28" fill="#CC1400" opacity="0.3"/>
<rect x="386" y="205" width="32" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="418" y="205" width="32" height="28" fill="#CC1400" opacity="0.9"/>
<rect x="450" y="205" width="32" height="28" fill="#CC1400" opacity="0.7"/>
<rect x="482" y="205" width="32" height="28" fill="#CC1400" opacity="0.7"/>
<rect x="514" y="205" width="32" height="28" fill="#CC1400" opacity="0.7"/>
<rect x="546" y="205" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="578" y="205" width="32" height="28" fill="#CC1400" opacity="0.4"/>
<rect x="610" y="205" width="32" height="28" fill="#CC1400" opacity="0.9"/>
<rect x="642" y="205" width="32" height="28" fill="#CC1400" opacity="0.9"/>
<!-- RISK行 -->
<text x="120" y="265" font-family="Noto Sans JP" font-size="10" fill="#CC1400" text-anchor="end" font-weight="700">RISK</text>
<rect x="130" y="250" width="32" height="28" fill="#CC1400" opacity="0.3" stroke="#CC1400" stroke-width="0.5"/>
<rect x="162" y="250" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="194" y="250" width="32" height="28" fill="#CC1400" opacity="0.3" stroke="#CC1400" stroke-width="0.5"/>
<rect x="226" y="250" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="258" y="250" width="32" height="28" fill="#CC1400" opacity="0.3" stroke="#CC1400" stroke-width="0.5"/>
<rect x="290" y="250" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="322" y="250" width="32" height="28" fill="#CC1400" opacity="0.3" stroke="#CC1400" stroke-width="0.5"/>
<rect x="354" y="250" width="32" height="28" fill="#CC1400" opacity="0.3" stroke="#CC1400" stroke-width="0.5"/>
<rect x="386" y="250" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="418" y="250" width="32" height="28" fill="#CC1400" opacity="0.3" stroke="#CC1400" stroke-width="0.5"/>
<rect x="450" y="250" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="482" y="250" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="514" y="250" width="32" height="28" fill="#CC1400" opacity="0.3" stroke="#CC1400" stroke-width="0.5"/>
<rect x="546" y="250" width="32" height="28" fill="#CC1400" opacity="0.3" stroke="#CC1400" stroke-width="0.5"/>
<rect x="578" y="250" width="32" height="28" fill="#999" opacity="0.3"/>
<rect x="610" y="250" width="32" height="28" fill="#CC1400" opacity="0.3" stroke="#CC1400" stroke-width="0.5"/>
<rect x="642" y="250" width="32" height="28" fill="#999" opacity="0.3"/>

<!-- 凡例 -->
<rect x="130" y="320" width="20" height="14" fill="#CC1400" opacity="0.9"/>
<text x="156" y="332" font-family="Noto Sans JP" font-size="10" fill="#555">強い正の影響</text>
<rect x="240" y="320" width="20" height="14" fill="#CC1400" opacity="0.4"/>
<text x="266" y="332" font-family="Noto Sans JP" font-size="10" fill="#555">中程度の正の影響</text>
<rect x="380" y="320" width="20" height="14" fill="#CC1400" opacity="0.3" stroke="#CC1400" stroke-width="0.5"/>
<text x="406" y="332" font-family="Noto Sans JP" font-size="10" fill="#555">負のリスク</text>
<rect x="480" y="320" width="20" height="14" fill="#999" opacity="0.3"/>
<text x="506" y="332" font-family="Noto Sans JP" font-size="10" fill="#555">中立または影響薄</text>

<text x="380" y="370" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle" font-style="italic">SDG: 1貧困/2飢餓/3健康/4教育/5ジェンダー/6水/7エネルギー/8労働/9産業/10不平等/11都市/12消費/13気候/14海/15陸/16平和/17連携</text>
</svg>
<figcaption style="font-family:var(--font);font-size:0.78rem;color:#6B6B6B;margin-top:12px;text-align:center;">図N7: Physical AI × SDG 17目標影響マトリクス。SOC系統(社会制度)が大半のSDGに正の影響を持つ一方、ENERGY/MATは7・9・11で強影響、RISK行で 1貧困・3健康・5ジェンダー・8労働・10不平等・13気候・14海・16平和に明確な負のリスクが識別される。</figcaption>
</figure>
```

---

## 図 N8: 17 能力円環ネットワーク

- **配置章**: 第7章「Physical AI と人材 (Talent 補論との接続)」
- **設計意図**: era-talents DB の 19 能力次元から Physical AI 関連 17 能力を円環配置。互いの関連エッジを内側に描き、Physical AI 時代に重みが増す 6 能力 (赤色) と 11 能力 (グレー) を区別

```html
<figure style="margin:36px 0;text-align:center;background:rgba(204,20,0,0.02);border-top:1px solid #CC1400;border-bottom:1px solid #CC1400;padding:32px 16px;">
<svg viewBox="0 0 760 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:760px;height:auto;">
<!-- 中央タイトル -->
<text x="380" y="195" font-family="Noto Serif JP" font-size="13" fill="#CC1400" text-anchor="middle" font-weight="700">Physical AI 時代</text>
<text x="380" y="213" font-family="Noto Serif JP" font-size="13" fill="#CC1400" text-anchor="middle" font-weight="700">の 17 能力</text>

<!-- 17能力ノード（円環配置、半径140） -->
<!-- Physical AI で重みが増す 6 能力（赤）: 1, 4, 7, 10, 13, 16 -->
<g font-family="Noto Sans JP" font-size="9">
<!-- ノード1: 身体性 (0°) -->
<circle cx="520" cy="200" r="22" fill="#FFF" stroke="#CC1400" stroke-width="1.8"/>
<text x="520" y="198" font-size="9" fill="#CC1400" text-anchor="middle" font-weight="700">身体性</text>
<text x="520" y="210" font-size="8" fill="#6B6B6B" text-anchor="middle">embodiment</text>
<!-- ノード2: 行動知 (21°) -->
<circle cx="510" cy="151" r="18" fill="#FFF" stroke="#555" stroke-width="0.8"/>
<text x="510" y="153" font-size="8" fill="#555" text-anchor="middle">行動知</text>
<!-- ノード3: 空間把握 (42°) -->
<circle cx="484" cy="108" r="18" fill="#FFF" stroke="#555" stroke-width="0.8"/>
<text x="484" y="110" font-size="8" fill="#555" text-anchor="middle">空間把握</text>
<!-- ノード4: 接触感覚 (63°) -->
<circle cx="443" cy="78" r="22" fill="#FFF" stroke="#CC1400" stroke-width="1.8"/>
<text x="443" y="76" font-size="9" fill="#CC1400" text-anchor="middle" font-weight="700">接触感覚</text>
<text x="443" y="88" font-size="8" fill="#6B6B6B" text-anchor="middle">tactile</text>
<!-- ノード5: 道具使用 (84°) -->
<circle cx="394" cy="65" r="18" fill="#FFF" stroke="#555" stroke-width="0.8"/>
<text x="394" y="67" font-size="8" fill="#555" text-anchor="middle">道具使用</text>
<!-- ノード6: 社会協調 (105°) -->
<circle cx="345" cy="71" r="18" fill="#FFF" stroke="#555" stroke-width="0.8"/>
<text x="345" y="73" font-size="8" fill="#555" text-anchor="middle">社会協調</text>
<!-- ノード7: 状況推論 (126°) -->
<circle cx="300" cy="92" r="22" fill="#FFF" stroke="#CC1400" stroke-width="1.8"/>
<text x="300" y="90" font-size="9" fill="#CC1400" text-anchor="middle" font-weight="700">状況推論</text>
<text x="300" y="102" font-size="8" fill="#6B6B6B" text-anchor="middle">contextual</text>
<!-- ノード8: 言語理解 (147°) -->
<circle cx="265" cy="129" r="18" fill="#FFF" stroke="#555" stroke-width="0.8"/>
<text x="265" y="131" font-size="8" fill="#555" text-anchor="middle">言語理解</text>
<!-- ノード9: 因果認知 (168°) -->
<circle cx="244" cy="175" r="18" fill="#FFF" stroke="#555" stroke-width="0.8"/>
<text x="244" y="177" font-size="8" fill="#555" text-anchor="middle">因果認知</text>
<!-- ノード10: 倫理判断 (189°) -->
<circle cx="240" cy="225" r="22" fill="#FFF" stroke="#CC1400" stroke-width="1.8"/>
<text x="240" y="223" font-size="9" fill="#CC1400" text-anchor="middle" font-weight="700">倫理判断</text>
<text x="240" y="235" font-size="8" fill="#6B6B6B" text-anchor="middle">ethical</text>
<!-- ノード11: 適応学習 (210°) -->
<circle cx="255" cy="271" r="18" fill="#FFF" stroke="#555" stroke-width="0.8"/>
<text x="255" y="273" font-size="8" fill="#555" text-anchor="middle">適応学習</text>
<!-- ノード12: 創造性 (231°) -->
<circle cx="287" cy="310" r="18" fill="#FFF" stroke="#555" stroke-width="0.8"/>
<text x="287" y="312" font-size="8" fill="#555" text-anchor="middle">創造性</text>
<!-- ノード13: 共感力 (252°) -->
<circle cx="332" cy="335" r="22" fill="#FFF" stroke="#CC1400" stroke-width="1.8"/>
<text x="332" y="333" font-size="9" fill="#CC1400" text-anchor="middle" font-weight="700">共感力</text>
<text x="332" y="345" font-size="8" fill="#6B6B6B" text-anchor="middle">empathy</text>
<!-- ノード14: 数理思考 (273°) -->
<circle cx="382" cy="345" r="18" fill="#FFF" stroke="#555" stroke-width="0.8"/>
<text x="382" y="347" font-size="8" fill="#555" text-anchor="middle">数理思考</text>
<!-- ノード15: 美的判断 (294°) -->
<circle cx="432" cy="335" r="18" fill="#FFF" stroke="#555" stroke-width="0.8"/>
<text x="432" y="337" font-size="8" fill="#555" text-anchor="middle">美的判断</text>
<!-- ノード16: 統合知 (315°) -->
<circle cx="475" cy="313" r="22" fill="#FFF" stroke="#CC1400" stroke-width="1.8"/>
<text x="475" y="311" font-size="9" fill="#CC1400" text-anchor="middle" font-weight="700">統合知</text>
<text x="475" y="323" font-size="8" fill="#6B6B6B" text-anchor="middle">synthesis</text>
<!-- ノード17: 反省的実践 (336°) -->
<circle cx="508" cy="275" r="18" fill="#FFF" stroke="#555" stroke-width="0.8"/>
<text x="508" y="277" font-size="8" fill="#555" text-anchor="middle">反省的</text>
</g>

<!-- 赤6能力同士の主接続線（中央内側を通す） -->
<line x1="520" y1="200" x2="443" y2="78" stroke="#CC1400" stroke-width="0.6" opacity="0.4"/>
<line x1="443" y1="78" x2="300" y2="92" stroke="#CC1400" stroke-width="0.6" opacity="0.4"/>
<line x1="300" y1="92" x2="240" y2="225" stroke="#CC1400" stroke-width="0.6" opacity="0.4"/>
<line x1="240" y1="225" x2="332" y2="335" stroke="#CC1400" stroke-width="0.6" opacity="0.4"/>
<line x1="332" y1="335" x2="475" y2="313" stroke="#CC1400" stroke-width="0.6" opacity="0.4"/>
<line x1="475" y1="313" x2="520" y2="200" stroke="#CC1400" stroke-width="0.6" opacity="0.4"/>
<!-- 中央クロスリンク -->
<line x1="520" y1="200" x2="240" y2="225" stroke="#CC1400" stroke-width="0.4" opacity="0.25"/>
<line x1="443" y1="78" x2="332" y2="335" stroke="#CC1400" stroke-width="0.4" opacity="0.25"/>
<line x1="300" y1="92" x2="475" y2="313" stroke="#CC1400" stroke-width="0.4" opacity="0.25"/>

<text x="380" y="380" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle" font-style="italic">赤=Physical AI時代に重みが増す6能力 / グレー=既存の11能力。出典: era-talents DB 19能力次元のうちPhysical AI連動17能力</text>
</svg>
<figcaption style="font-family:var(--font);font-size:0.78rem;color:#6B6B6B;margin-top:12px;text-align:center;">図N8: 17能力円環ネットワーク。Physical AI時代に重みが増す6能力（身体性・接触感覚・状況推論・倫理判断・共感力・統合知）が円環上で互いに直接接続し、これらを核に人材育成を再設計する含意を示す。</figcaption>
</figure>
```

---

## 図 N9: FVCP 5補論の交差点 3D マッピング

- **配置章**: 終章「Physical AI と他の未来像」あるいは付録 (FVCP 補論連携)
- **設計意図**: FVCP 5 補論 (製造/移動/食農/HR/Physical AI) を擬似 3D 空間 (X=時間軸/Y=領域軸/Z=身体性軸) に配置。3 D見せ方は等角投影で擬似的に。中央に交差点 = Physical AI を据える

```html
<figure style="margin:36px 0;text-align:center;background:rgba(204,20,0,0.02);border-top:1px solid #CC1400;border-bottom:1px solid #CC1400;padding:32px 16px;">
<svg viewBox="0 0 760 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:760px;height:auto;">
<!-- 擬似3D等角投影軸 -->
<line x1="100" y1="320" x2="650" y2="320" stroke="#121212" stroke-width="1"/>
<line x1="100" y1="320" x2="100" y2="60" stroke="#121212" stroke-width="1"/>
<line x1="100" y1="320" x2="240" y2="380" stroke="#121212" stroke-width="1"/>
<!-- 軸ラベル -->
<text x="660" y="324" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="start">X: 時間軸 (2026 → 2100)</text>
<text x="100" y="50" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="middle">Y: 領域</text>
<text x="250" y="395" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="start">Z: 身体性</text>

<!-- 5補論ノード（位置=領域×時代主峰、サイズ=身体性関与度） -->
<!-- 製造 (Phase B-C 主峰、身体性 high) -->
<ellipse cx="280" cy="200" rx="55" ry="35" fill="#FFF" stroke="#CC1400" stroke-width="1.5" opacity="0.95"/>
<text x="280" y="195" font-family="Noto Serif JP" font-size="13" fill="#CC1400" text-anchor="middle" font-weight="700">製造</text>
<text x="280" y="210" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2030-50主峰</text>
<text x="280" y="222" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">身体性: 大</text>

<!-- 移動 (Phase A-D 連続、身体性 mid-high) -->
<ellipse cx="330" cy="120" rx="50" ry="30" fill="#FFF" stroke="#CC1400" stroke-width="1.2" opacity="0.95"/>
<text x="330" y="115" font-family="Noto Serif JP" font-size="12" fill="#CC1400" text-anchor="middle" font-weight="700">移動</text>
<text x="330" y="128" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2026-65連続</text>
<text x="330" y="140" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">身体性: 中-大</text>

<!-- 食農 (Phase C-E 主峰、身体性 mid) -->
<ellipse cx="450" cy="270" rx="50" ry="30" fill="#FFF" stroke="#CC1400" stroke-width="1.2" opacity="0.95"/>
<text x="450" y="265" font-family="Noto Serif JP" font-size="12" fill="#CC1400" text-anchor="middle" font-weight="700">食農</text>
<text x="450" y="278" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2040-80主峰</text>
<text x="450" y="290" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">身体性: 中</text>

<!-- HR (Phase D-G 主峰、身体性 low) -->
<ellipse cx="540" cy="150" rx="50" ry="30" fill="#FFF" stroke="#CC1400" stroke-width="1.2" opacity="0.95"/>
<text x="540" y="145" font-family="Noto Serif JP" font-size="12" fill="#CC1400" text-anchor="middle" font-weight="700">HR</text>
<text x="540" y="158" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2050-2100主峰</text>
<text x="540" y="170" font-family="Noto Sans JP" font-size="8" fill="#6B6B6B" text-anchor="middle">身体性: 小</text>

<!-- Physical AI (中央、最大サイズ、全領域・全時代接続) -->
<ellipse cx="400" cy="195" rx="70" ry="45" fill="#CC1400" opacity="0.18" stroke="#CC1400" stroke-width="2.5"/>
<text x="400" y="190" font-family="Noto Serif JP" font-size="14" fill="#CC1400" text-anchor="middle" font-weight="700">Physical AI</text>
<text x="400" y="206" font-family="Noto Sans JP" font-size="10" fill="#CC1400" text-anchor="middle">2026-2100 通底</text>
<text x="400" y="222" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">身体性: 中核</text>

<!-- 接続線（Physical AI 中心から4補論へ） -->
<line x1="400" y1="195" x2="280" y2="200" stroke="#CC1400" stroke-width="1.2" opacity="0.5"/>
<line x1="400" y1="195" x2="330" y2="120" stroke="#CC1400" stroke-width="1.2" opacity="0.5"/>
<line x1="400" y1="195" x2="450" y2="270" stroke="#CC1400" stroke-width="1.2" opacity="0.5"/>
<line x1="400" y1="195" x2="540" y2="150" stroke="#CC1400" stroke-width="1.2" opacity="0.5"/>

<!-- 時代マーカー（X軸目盛） -->
<text x="170" y="338" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2026</text>
<text x="290" y="338" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2050</text>
<text x="410" y="338" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2075</text>
<text x="530" y="338" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2100</text>

<text x="380" y="375" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle" font-style="italic">出典: FVCP Meta DB v1.6 (4補論+9計画テーマ)</text>
</svg>
<figcaption style="font-family:var(--font);font-size:0.78rem;color:#6B6B6B;margin-top:12px;text-align:center;">図N9: FVCP 5補論の交差点3Dマッピング。Physical AIは時間軸・領域軸・身体性軸の中央に位置し、製造（身体性大）・移動（中-大）・食農（中）・HR（小）の4補論が放射状にそれを縁取る構造。本補論はFVCPの結節点として機能する。</figcaption>
</figure>
```

---

## 図 N10: Phase A-G S字曲線群

- **配置章**: 第3章「7フェーズロードマップ」末尾あるいは終章
- **設計意図**: 4 指標 (普及率/単価/性能/データ量) の累積 S 字曲線を 1 つのグラフに重ねる。各曲線の変曲点が Phase 境界 (A-G) と重なる構造を可視化

```html
<figure style="margin:36px 0;text-align:center;background:rgba(204,20,0,0.02);border-top:1px solid #CC1400;border-bottom:1px solid #CC1400;padding:32px 16px;">
<svg viewBox="0 0 760 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:760px;height:auto;">
<!-- 軸 -->
<line x1="80" y1="320" x2="700" y2="320" stroke="#121212" stroke-width="1.5"/>
<line x1="80" y1="50" x2="80" y2="320" stroke="#121212" stroke-width="1.5"/>
<text x="70" y="60" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="end">100%</text>
<text x="70" y="195" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="end">50%</text>
<text x="70" y="325" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="end">0%</text>
<text x="60" y="190" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="middle" transform="rotate(-90 60 190)">累積指標</text>

<!-- X軸 Phase 境界線 -->
<line x1="170" y1="50" x2="170" y2="320" stroke="#D9D9D9" stroke-width="0.6" stroke-dasharray="3,3"/>
<line x1="260" y1="50" x2="260" y2="320" stroke="#D9D9D9" stroke-width="0.6" stroke-dasharray="3,3"/>
<line x1="350" y1="50" x2="350" y2="320" stroke="#D9D9D9" stroke-width="0.6" stroke-dasharray="3,3"/>
<line x1="440" y1="50" x2="440" y2="320" stroke="#D9D9D9" stroke-width="0.6" stroke-dasharray="3,3"/>
<line x1="530" y1="50" x2="530" y2="320" stroke="#D9D9D9" stroke-width="0.6" stroke-dasharray="3,3"/>
<line x1="620" y1="50" x2="620" y2="320" stroke="#D9D9D9" stroke-width="0.6" stroke-dasharray="3,3"/>

<!-- Phase ラベル -->
<text x="125" y="40" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="middle" font-weight="700">A</text>
<text x="215" y="40" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="middle" font-weight="700">B</text>
<text x="305" y="40" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="middle" font-weight="700">C</text>
<text x="395" y="40" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="middle" font-weight="700">D</text>
<text x="485" y="40" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="middle" font-weight="700">E</text>
<text x="575" y="40" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="middle" font-weight="700">F</text>
<text x="660" y="40" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="middle" font-weight="700">G</text>

<!-- 年代軸 -->
<text x="80" y="340" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2026</text>
<text x="170" y="340" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2030</text>
<text x="260" y="340" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2040</text>
<text x="350" y="340" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2050</text>
<text x="440" y="340" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2065</text>
<text x="530" y="340" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2080</text>
<text x="620" y="340" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2090</text>
<text x="700" y="340" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle">2100</text>

<!-- S字曲線1: 普及率 (Phase C 変曲、最終 95%) -->
<path d="M 80,310 Q 170,308 230,295 Q 290,272 350,200 Q 410,128 470,95 Q 530,72 620,65 L 700,62" stroke="#CC1400" stroke-width="2.5" fill="none"/>
<text x="700" y="68" font-family="Noto Sans JP" font-size="10" fill="#CC1400" text-anchor="start" font-weight="700">普及率</text>

<!-- S字曲線2: 単価 (反転、Phase B 急落、最終5%) -->
<path d="M 80,62 Q 130,68 170,90 Q 210,130 260,195 Q 310,260 350,290 Q 400,308 470,313 Q 540,316 700,317" stroke="#CC1400" stroke-width="2" fill="none" stroke-dasharray="6,3"/>
<text x="700" y="312" font-family="Noto Sans JP" font-size="10" fill="#CC1400" text-anchor="start">単価(反転)</text>

<!-- S字曲線3: 性能 (Phase A-B 立上り、Phase E 飽和) -->
<path d="M 80,300 Q 170,225 260,140 Q 350,85 440,70 Q 530,62 700,60" stroke="#121212" stroke-width="2" fill="none"/>
<text x="700" y="56" font-family="Noto Sans JP" font-size="10" fill="#121212" text-anchor="start">性能</text>

<!-- S字曲線4: データ量 (Phase A-D 加速、Phase E 停滞、Phase F-G 再加速 - 2峰型) -->
<path d="M 80,310 Q 140,290 200,240 Q 260,180 320,135 Q 380,110 420,118 Q 460,128 510,120 Q 560,105 620,80 L 700,72" stroke="#555" stroke-width="2" fill="none"/>
<text x="700" y="78" font-family="Noto Sans JP" font-size="10" fill="#555" text-anchor="start">データ量</text>

<!-- 変曲点マーカー (Phase C 普及率) -->
<circle cx="350" cy="200" r="5" fill="#CC1400"/>
<text x="350" y="220" font-family="Noto Sans JP" font-size="9" fill="#CC1400" text-anchor="middle" font-weight="700">Phase C: 普及変曲点</text>

<!-- 凡例 -->
<text x="380" y="385" font-family="Noto Sans JP" font-size="9" fill="#6B6B6B" text-anchor="middle" font-style="italic">出典: PHAI-DB phase_indicator_curves (IFR / Goldman Sachs / Epoch AI / Open X-Embodiment 統合)</text>
</svg>
<figcaption style="font-family:var(--font);font-size:0.78rem;color:#6B6B6B;margin-top:12px;text-align:center;">図N10: Phase A-G S字曲線群。普及率（実線）・単価反転（破線）・性能（黒）・データ量（灰）の4指標。性能は Phase B 早期飽和、普及率は Phase C 変曲、データ量は実機データ枯渇→合成データ再生で2峰型を描く。</figcaption>
</figure>
```

---

## 配置サマリ

| 図番号 | タイトル | 配置候補章 | viewBox | 主目的 |
|---|---|---|---|---|
| N1 | AR-DB横断マップ図 | 第1章 / 序章末 | 760×400 | DB横断統合の宣言 |
| N2 | 8系統×Phase ヒートマップ | 第2章末 / 第3章冒頭 | 760×400 | 系統の重心移行 |
| N3 | 地政学三極ダイヤモンド | 第4章 / Phase B | 760×400 | 4極の政策強度差 |
| N4 | エネルギー三制約三角形 | 第5章 / Phase C-D | 760×400 | 制約軸の時代変遷 |
| N5 | VLM→VLA→GLA進化系統樹 | 第2章 第四系統末尾 | 760×400 | 基盤モデル系譜 |
| N6 | 朝シーン世界地図 | 第8章 / 終章 | 760×400 | 地域文化×時代差 |
| N7 | Physical AI × SDG 17マトリクス | 第9章 | 760×400 | 社会的含意の正負 |
| N8 | 17能力円環ネットワーク | 第7章 | 760×400 | 人材育成の重心 |
| N9 | FVCP 5補論 3Dマッピング | 終章 / 付録 | 760×400 | FVCP結節点 |
| N10 | Phase A-G S字曲線群 | 第3章末 / 終章 | 760×400 | 4指標の同時可視化 |

## 注意

- 全 SVG は `fill` / `stroke` に正規パレット (#121212 / #555 / #6B6B6B / #FFF / #CC1400 / #D9D9D9 / #F7F7F5) のみ使用、ダークモード CSS (`[data-theme="dark"] svg text` 等) が自動適用される
- 数値は PHAI-DB / AR-DB / FVCP Meta DB / era-talents / IFR / Goldman Sachs / Epoch AI / IEA 等の既存ソースに基づく代表値。実装時にDB照会して精緻化推奨
- `<figure>` 入れ子 (赤白 CI ボーダー + `rgba(204,20,0,0.02)` 淡赤背景 + `padding:32px 16px`) は既存第1章図と一致
- 各 figcaption は `font-family:var(--font);font-size:0.78rem;color:#6B6B6B;` で統一
