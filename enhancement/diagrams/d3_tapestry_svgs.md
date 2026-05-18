# D3 — 高密度時間軸タペストリー（Physical AI 2100 教科書）

赤白CI #CC1400 / Noto Sans JP / ダークモード対応 / 5 図構成

色定義（全図共通）:
- アクセント赤: `#CC1400`（ダークモード: `#FF4030`）
- 紙地: `#FFFFFF`（ダーク: `#121212`）
- 主要文字: `#121212`（ダーク: `#E0E0E0`）
- 副文字: `#555555`（ダーク: `#AAAAAA`）
- 罫線: `#D9D9D9`（ダーク: `#333333`）
- 帯地: `#F7F7F5`（ダーク: `#1A1A1A`）
- 8系統色: `#1F4E5F` 知覚 / `#2E5E3E` 行動 / `#5A3E1F` 学習 / `#6E1F4A` 安全 / `#3F5F1F` 群制御 / `#1F3F5F` クラウド / `#5F2E1F` 材料 / `#3F1F5F` 計算

CSSヒント（教科書 HTML に同梱）:

```css
.d3-tapestry-svg { background: var(--bg, #FFFFFF); }
[data-theme="dark"] .d3-tapestry-svg { background: var(--bg, #121212); }
[data-theme="dark"] .d3-tapestry-svg text { fill: #E0E0E0 !important; }
[data-theme="dark"] .d3-tapestry-svg text.t-sub { fill: #AAAAAA !important; }
[data-theme="dark"] .d3-tapestry-svg text.t-mute { fill: #8A8A8A !important; }
[data-theme="dark"] .d3-tapestry-svg .accent { fill: #FF4030 !important; stroke: #FF4030 !important; }
[data-theme="dark"] .d3-tapestry-svg .grid { stroke: #333333 !important; }
[data-theme="dark"] .d3-tapestry-svg .row-bg-odd { fill: #1A1A1A !important; }
[data-theme="dark"] .d3-tapestry-svg .row-bg-even { fill: #121212 !important; }
```

---

## D3-1 メインタペストリー（1200×800 / Phase A-G 全縦横統合）

横軸: 7 Phase（A:2026-2030 / B:2030-2035 / C:2035-2045 / D:2045-2055 / E:2055-2070 / F:2070-2085 / G:2085-2100）
縦軸: 12 行（8 系統 + 5 メガトレンド + 地政学 + 労働 + 倫理）

```svg
<svg class="d3-tapestry-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" role="img" aria-label="Physical AI 2100 Phase A-G 高密度時間軸タペストリー">
  <style>
    .t-title { font: 600 18px "Noto Sans JP", sans-serif; fill: #121212; }
    .t-subtitle { font: 400 12px "Noto Sans JP", sans-serif; fill: #555555; }
    .t-phase { font: 600 13px "Noto Sans JP", sans-serif; fill: #121212; text-anchor: middle; }
    .t-phase-year { font: 400 10px "Noto Sans JP", sans-serif; fill: #555555; text-anchor: middle; }
    .t-row { font: 600 11px "Noto Sans JP", sans-serif; fill: #121212; text-anchor: end; }
    .t-row-sub { font: 400 9px "Noto Sans JP", sans-serif; fill: #555555; text-anchor: end; }
    .t-cell { font: 400 9.5px "Noto Sans JP", sans-serif; fill: #121212; }
    .t-cell-sub { font: 400 8.5px "Noto Sans JP", sans-serif; fill: #555555; }
    .t-sub { fill: #555555; }
    .t-mute { fill: #8A8A8A; }
    .accent { fill: #CC1400; }
    .grid { stroke: #D9D9D9; stroke-width: 0.5; }
    .row-bg-odd { fill: #F7F7F5; }
    .row-bg-even { fill: #FFFFFF; }
  </style>

  <!-- タイトル -->
  <text x="40" y="30" class="t-title">Physical AI 2100 高密度時間軸タペストリー</text>
  <text x="40" y="48" class="t-subtitle">Phase A (2026-2030) → Phase G (2085-2100) ／ 8 系統 + 5 メガトレンド + 地政学 + 労働 + 倫理</text>

  <!-- 上罫 -->
  <line x1="40" y1="60" x2="1180" y2="60" class="grid" stroke="#121212" stroke-width="2"/>

  <!-- Phase ヘッダー（横軸） -->
  <g transform="translate(0, 75)">
    <rect x="200" y="0" width="140" height="30" class="row-bg-odd"/>
    <rect x="340" y="0" width="140" height="30" class="row-bg-even"/>
    <rect x="480" y="0" width="140" height="30" class="row-bg-odd"/>
    <rect x="620" y="0" width="140" height="30" class="row-bg-even"/>
    <rect x="760" y="0" width="140" height="30" class="row-bg-odd"/>
    <rect x="900" y="0" width="140" height="30" class="row-bg-even"/>
    <rect x="1040" y="0" width="140" height="30" class="row-bg-odd"/>

    <text x="270" y="14" class="t-phase">Phase A</text>
    <text x="270" y="26" class="t-phase-year">2026-2030 萌芽</text>
    <text x="410" y="14" class="t-phase">Phase B</text>
    <text x="410" y="26" class="t-phase-year">2030-2035 実装</text>
    <text x="550" y="14" class="t-phase">Phase C</text>
    <text x="550" y="26" class="t-phase-year">2035-2045 普及</text>
    <text x="690" y="14" class="t-phase">Phase D</text>
    <text x="690" y="26" class="t-phase-year">2045-2055 統合</text>
    <text x="830" y="14" class="t-phase">Phase E</text>
    <text x="830" y="26" class="t-phase-year">2055-2070 浸透</text>
    <text x="970" y="14" class="t-phase">Phase F</text>
    <text x="970" y="26" class="t-phase-year">2070-2085 円熟</text>
    <text x="1110" y="14" class="t-phase">Phase G</text>
    <text x="1110" y="26" class="t-phase-year">2085-2100 共存</text>
  </g>

  <!-- 縦罫（Phase 区切り） -->
  <line x1="200" y1="105" x2="200" y2="750" class="grid"/>
  <line x1="340" y1="105" x2="340" y2="750" class="grid"/>
  <line x1="480" y1="105" x2="480" y2="750" class="grid"/>
  <line x1="620" y1="105" x2="620" y2="750" class="grid"/>
  <line x1="760" y1="105" x2="760" y2="750" class="grid"/>
  <line x1="900" y1="105" x2="900" y2="750" class="grid"/>
  <line x1="1040" y1="105" x2="1040" y2="750" class="grid"/>
  <line x1="1180" y1="105" x2="1180" y2="750" class="grid"/>

  <!-- 12 行のセル（行ごとに 50px、開始 y=110） -->
  <!-- 行 1: 知覚（センサ・視覚・触覚） -->
  <g transform="translate(0, 110)">
    <rect x="200" y="0" width="980" height="50" class="row-bg-odd"/>
    <rect x="40" y="0" width="160" height="50" class="row-bg-odd"/>
    <rect x="40" y="2" width="4" height="46" fill="#1F4E5F"/>
    <text x="190" y="22" class="t-row">知覚</text>
    <text x="190" y="36" class="t-row-sub">Perception / Sensing</text>
    <text x="208" y="18" class="t-cell">マルチモーダル基盤</text>
    <text x="208" y="32" class="t-cell-sub">触覚スキン量産</text>
    <text x="208" y="44" class="t-cell-sub">3D 物体理解</text>
    <text x="348" y="18" class="t-cell">深度+音響+触覚 融合</text>
    <text x="348" y="32" class="t-cell-sub">FoundationPose 標準化</text>
    <text x="348" y="44" class="t-cell-sub">家庭環境認識</text>
    <text x="488" y="18" class="t-cell">完全マルチセンサ統合</text>
    <text x="488" y="32" class="t-cell-sub">皮膚感覚密度 1cm²</text>
    <text x="488" y="44" class="t-cell-sub">嗅覚センサ商品化</text>
    <text x="628" y="18" class="t-cell">脳波級高密度</text>
    <text x="628" y="32" class="t-cell-sub">分散ネットワーク化</text>
    <text x="628" y="44" class="t-cell-sub">予測知覚 90%精度</text>
    <text x="768" y="18" class="t-cell">環境連携センシング</text>
    <text x="768" y="32" class="t-cell-sub">都市スマートタイル</text>
    <text x="768" y="44" class="t-cell-sub">屋内 mm 精度位置</text>
    <text x="908" y="18" class="t-cell">バイオセンサ共生</text>
    <text x="908" y="32" class="t-cell-sub">人の心拍/汗 検知</text>
    <text x="908" y="44" class="t-cell-sub">情動推定 95%</text>
    <text x="1048" y="18" class="t-cell">人-機 等価知覚</text>
    <text x="1048" y="32" class="t-cell-sub">主観経験のモデル化</text>
    <text x="1048" y="44" class="t-cell-sub">共有感覚 API</text>
  </g>

  <!-- 行 2: 行動（マニピュレーション・移動） -->
  <g transform="translate(0, 160)">
    <rect x="200" y="0" width="980" height="50" class="row-bg-even"/>
    <rect x="40" y="0" width="160" height="50" class="row-bg-even"/>
    <rect x="40" y="2" width="4" height="46" fill="#2E5E3E"/>
    <text x="190" y="22" class="t-row">行動</text>
    <text x="190" y="36" class="t-row-sub">Manipulation / Locomotion</text>
    <text x="208" y="18" class="t-cell">物体把持 80%成功</text>
    <text x="208" y="32" class="t-cell-sub">物流倉庫実証</text>
    <text x="208" y="44" class="t-cell-sub">2足歩行 屋内</text>
    <text x="348" y="18" class="t-cell">家庭調理ロボ</text>
    <text x="348" y="32" class="t-cell-sub">布操作 商品化</text>
    <text x="348" y="44" class="t-cell-sub">屋外 4足 配送</text>
    <text x="488" y="18" class="t-cell">器用さ人並み</text>
    <text x="488" y="32" class="t-cell-sub">介護動作 全カバー</text>
    <text x="488" y="44" class="t-cell-sub">階段 走行 自在</text>
    <text x="628" y="18" class="t-cell">職人技能 再現</text>
    <text x="628" y="32" class="t-cell-sub">道具製作 自律</text>
    <text x="628" y="44" class="t-cell-sub">パルクール級移動</text>
    <text x="768" y="18" class="t-cell">微細手術 自動化</text>
    <text x="768" y="32" class="t-cell-sub">ナノ操作 量産</text>
    <text x="768" y="44" class="t-cell-sub">災害現場 任意機動</text>
    <text x="908" y="18" class="t-cell">熟練超え創造</text>
    <text x="908" y="32" class="t-cell-sub">即興舞踊 共演</text>
    <text x="908" y="44" class="t-cell-sub">水陸両用 標準</text>
    <text x="1048" y="18" class="t-cell">身体性の自由設計</text>
    <text x="1048" y="32" class="t-cell-sub">形態 mission-adaptive</text>
    <text x="1048" y="44" class="t-cell-sub">変形ロボ 普及</text>
  </g>

  <!-- 行 3: 学習（VLA・基盤モデル） -->
  <g transform="translate(0, 210)">
    <rect x="200" y="0" width="980" height="50" class="row-bg-odd"/>
    <rect x="40" y="0" width="160" height="50" class="row-bg-odd"/>
    <rect x="40" y="2" width="4" height="46" fill="#5A3E1F"/>
    <text x="190" y="22" class="t-row">学習</text>
    <text x="190" y="36" class="t-row-sub">VLA / Foundation Model</text>
    <text x="208" y="18" class="t-cell">RT-2 / OpenVLA 系</text>
    <text x="208" y="32" class="t-cell-sub">100 タスク汎化</text>
    <text x="208" y="44" class="t-cell-sub">Sim-to-Real 70%</text>
    <text x="348" y="18" class="t-cell">VLA 1B-10B 量産</text>
    <text x="348" y="32" class="t-cell-sub">家事 500 タスク</text>
    <text x="348" y="44" class="t-cell-sub">Few-shot 学習</text>
    <text x="488" y="18" class="t-cell">身体基盤モデル統合</text>
    <text x="488" y="32" class="t-cell-sub">100B 物理規模</text>
    <text x="488" y="44" class="t-cell-sub">継続学習 標準</text>
    <text x="628" y="18" class="t-cell">自己教師 完全自律</text>
    <text x="628" y="32" class="t-cell-sub">世界モデル 内蔵</text>
    <text x="628" y="44" class="t-cell-sub">転移 instant</text>
    <text x="768" y="18" class="t-cell">機械間知識市場</text>
    <text x="768" y="32" class="t-cell-sub">スキルNFT 流通</text>
    <text x="768" y="44" class="t-cell-sub">経験の蒸留共有</text>
    <text x="908" y="18" class="t-cell">創発的技能 出現</text>
    <text x="908" y="32" class="t-cell-sub">人類未経験動作</text>
    <text x="908" y="44" class="t-cell-sub">芸術技能 拡張</text>
    <text x="1048" y="18" class="t-cell">学習の生態系化</text>
    <text x="1048" y="32" class="t-cell-sub">機械×人 共進化</text>
    <text x="1048" y="44" class="t-cell-sub">集合知 物理化</text>
  </g>

  <!-- 行 4: 安全 -->
  <g transform="translate(0, 260)">
    <rect x="200" y="0" width="980" height="50" class="row-bg-even"/>
    <rect x="40" y="0" width="160" height="50" class="row-bg-even"/>
    <rect x="40" y="2" width="4" height="46" fill="#6E1F4A"/>
    <text x="190" y="22" class="t-row">安全</text>
    <text x="190" y="36" class="t-row-sub">Safety / Reliability</text>
    <text x="208" y="18" class="t-cell">ISO/TS 15066 拡張</text>
    <text x="208" y="32" class="t-cell-sub">FMEA 動的化</text>
    <text x="208" y="44" class="t-cell-sub">緊急停止 5ms</text>
    <text x="348" y="18" class="t-cell">家庭ロボ 認証制度</text>
    <text x="348" y="32" class="t-cell-sub">保険商品 標準</text>
    <text x="348" y="44" class="t-cell-sub">Recall プロトコル</text>
    <text x="488" y="18" class="t-cell">フォーマル検証 義務</text>
    <text x="488" y="32" class="t-cell-sub">行動制約 数学保証</text>
    <text x="488" y="44" class="t-cell-sub">侵入耐性</text>
    <text x="628" y="18" class="t-cell">分散冗長 標準化</text>
    <text x="628" y="32" class="t-cell-sub">フェイルセーフ 階層</text>
    <text x="628" y="44" class="t-cell-sub">自己診断 常時</text>
    <text x="768" y="18" class="t-cell">公共空間 共有規範</text>
    <text x="768" y="32" class="t-cell-sub">交通-空間-人 統合</text>
    <text x="768" y="44" class="t-cell-sub">事故ゼロ目標</text>
    <text x="908" y="18" class="t-cell">予測安全 完全実装</text>
    <text x="908" y="32" class="t-cell-sub">人の意図先読み</text>
    <text x="908" y="44" class="t-cell-sub">回避率 99.99%</text>
    <text x="1048" y="18" class="t-cell">機械-機械間の信頼</text>
    <text x="1048" y="32" class="t-cell-sub">分散合意 標準</text>
    <text x="1048" y="44" class="t-cell-sub">自己修復 普遍</text>
  </g>

  <!-- 行 5: 群制御 -->
  <g transform="translate(0, 310)">
    <rect x="200" y="0" width="980" height="50" class="row-bg-odd"/>
    <rect x="40" y="0" width="160" height="50" class="row-bg-odd"/>
    <rect x="40" y="2" width="4" height="46" fill="#3F5F1F"/>
    <text x="190" y="22" class="t-row">群制御</text>
    <text x="190" y="36" class="t-row-sub">Swarm / Multi-agent</text>
    <text x="208" y="18" class="t-cell">10台級協調</text>
    <text x="208" y="32" class="t-cell-sub">物流 fleet</text>
    <text x="208" y="44" class="t-cell-sub">中央指令型</text>
    <text x="348" y="18" class="t-cell">100台 分散合意</text>
    <text x="348" y="32" class="t-cell-sub">建設現場 群</text>
    <text x="348" y="44" class="t-cell-sub">通信 5G/6G</text>
    <text x="488" y="18" class="t-cell">1,000台 自律編隊</text>
    <text x="488" y="32" class="t-cell-sub">災害救助 group</text>
    <text x="488" y="44" class="t-cell-sub">役割の動的交代</text>
    <text x="628" y="18" class="t-cell">10K台 都市運用</text>
    <text x="628" y="32" class="t-cell-sub">物流-清掃-警備統合</text>
    <text x="628" y="44" class="t-cell-sub">CO2 削減ベース</text>
    <text x="768" y="18" class="t-cell">100K台 環境工学</text>
    <text x="768" y="32" class="t-cell-sub">海洋 prove 修復</text>
    <text x="768" y="44" class="t-cell-sub">森林管理 自律</text>
    <text x="908" y="18" class="t-cell">1M台 生態系統合</text>
    <text x="908" y="32" class="t-cell-sub">惑星規模 sensing</text>
    <text x="908" y="44" class="t-cell-sub">気候介入 慎重実装</text>
    <text x="1048" y="18" class="t-cell">機械生態系 自律</text>
    <text x="1048" y="32" class="t-cell-sub">人と共有された地球</text>
    <text x="1048" y="44" class="t-cell-sub">調和的群知能</text>
  </g>

  <!-- 行 6: クラウド・分散計算 -->
  <g transform="translate(0, 360)">
    <rect x="200" y="0" width="980" height="50" class="row-bg-even"/>
    <rect x="40" y="0" width="160" height="50" class="row-bg-even"/>
    <rect x="40" y="2" width="4" height="46" fill="#1F3F5F"/>
    <text x="190" y="22" class="t-row">クラウド</text>
    <text x="190" y="36" class="t-row-sub">Cloud / Edge Compute</text>
    <text x="208" y="18" class="t-cell">エッジ TOPS 級</text>
    <text x="208" y="32" class="t-cell-sub">5G low-latency</text>
    <text x="208" y="44" class="t-cell-sub">推論集中 30%</text>
    <text x="348" y="18" class="t-cell">エッジ PFLOPS</text>
    <text x="348" y="32" class="t-cell-sub">6G 標準化</text>
    <text x="348" y="44" class="t-cell-sub">分散 50/50</text>
    <text x="488" y="18" class="t-cell">フォグ層 確立</text>
    <text x="488" y="32" class="t-cell-sub">機械間直接通信</text>
    <text x="488" y="44" class="t-cell-sub">通信遅延 1ms</text>
    <text x="628" y="18" class="t-cell">ニューロモーフィック</text>
    <text x="628" y="32" class="t-cell-sub">電力 1/100</text>
    <text x="628" y="44" class="t-cell-sub">on-device 主流</text>
    <text x="768" y="18" class="t-cell">量子-古典 hybrid</text>
    <text x="768" y="32" class="t-cell-sub">最適化問題 突破</text>
    <text x="768" y="44" class="t-cell-sub">通信暗号 PQC</text>
    <text x="908" y="18" class="t-cell">光-量子 統合</text>
    <text x="908" y="32" class="t-cell-sub">光配線 標準化</text>
    <text x="908" y="44" class="t-cell-sub">エネルギー自給</text>
    <text x="1048" y="18" class="t-cell">計算の遍在化</text>
    <text x="1048" y="32" class="t-cell-sub">環境 = 計算基盤</text>
    <text x="1048" y="44" class="t-cell-sub">物質-情報の一体化</text>
  </g>

  <!-- 行 7: 材料・ハードウェア -->
  <g transform="translate(0, 410)">
    <rect x="200" y="0" width="980" height="50" class="row-bg-odd"/>
    <rect x="40" y="0" width="160" height="50" class="row-bg-odd"/>
    <rect x="40" y="2" width="4" height="46" fill="#5F2E1F"/>
    <text x="190" y="22" class="t-row">材料</text>
    <text x="190" y="36" class="t-row-sub">Materials / Actuators</text>
    <text x="208" y="18" class="t-cell">軽量複合材</text>
    <text x="208" y="32" class="t-cell-sub">弾性体 actuator</text>
    <text x="208" y="44" class="t-cell-sub">電池 400 Wh/kg</text>
    <text x="348" y="18" class="t-cell">人工筋肉 商用化</text>
    <text x="348" y="32" class="t-cell-sub">柔軟駆動 普及</text>
    <text x="348" y="44" class="t-cell-sub">全固体電池</text>
    <text x="488" y="18" class="t-cell">自己修復素材</text>
    <text x="488" y="32" class="t-cell-sub">プログラマブル物質</text>
    <text x="488" y="44" class="t-cell-sub">エネルギー回生</text>
    <text x="628" y="18" class="t-cell">生体融合素材</text>
    <text x="628" y="32" class="t-cell-sub">バイオハイブリッド</text>
    <text x="628" y="44" class="t-cell-sub">ワイヤレス給電</text>
    <text x="768" y="18" class="t-cell">メタマテリアル統合</text>
    <text x="768" y="32" class="t-cell-sub">適応光学/音響</text>
    <text x="768" y="44" class="t-cell-sub">超軽量機体</text>
    <text x="908" y="18" class="t-cell">分子設計駆動</text>
    <text x="908" y="32" class="t-cell-sub">用途別最適合成</text>
    <text x="908" y="44" class="t-cell-sub">完全リサイクル</text>
    <text x="1048" y="18" class="t-cell">プログラム可能物質</text>
    <text x="1048" y="32" class="t-cell-sub">claytronics 萌芽</text>
    <text x="1048" y="44" class="t-cell-sub">物質-機械境界消失</text>
  </g>

  <!-- 行 8: 計算アーキテクチャ -->
  <g transform="translate(0, 460)">
    <rect x="200" y="0" width="980" height="50" class="row-bg-even"/>
    <rect x="40" y="0" width="160" height="50" class="row-bg-even"/>
    <rect x="40" y="2" width="4" height="46" fill="#3F1F5F"/>
    <text x="190" y="22" class="t-row">計算</text>
    <text x="190" y="36" class="t-row-sub">Compute Architecture</text>
    <text x="208" y="18" class="t-cell">GPU/NPU 主流</text>
    <text x="208" y="32" class="t-cell-sub">TPU 専用化</text>
    <text x="208" y="44" class="t-cell-sub">3nm 量産</text>
    <text x="348" y="18" class="t-cell">専用ASIC 多様化</text>
    <text x="348" y="32" class="t-cell-sub">ロボ用 NPU</text>
    <text x="348" y="44" class="t-cell-sub">2nm 量産</text>
    <text x="488" y="18" class="t-cell">3D 積層 標準</text>
    <text x="488" y="32" class="t-cell-sub">CIM 普及</text>
    <text x="488" y="44" class="t-cell-sub">1.4nm GAA</text>
    <text x="628" y="18" class="t-cell">ニューロモーフィック</text>
    <text x="628" y="32" class="t-cell-sub">スパイク方式</text>
    <text x="628" y="44" class="t-cell-sub">エネルギー 1/1000</text>
    <text x="768" y="18" class="t-cell">量子コ プロセッサ</text>
    <text x="768" y="32" class="t-cell-sub">特定問題 1000倍</text>
    <text x="768" y="44" class="t-cell-sub">誤り訂正 達成</text>
    <text x="908" y="18" class="t-cell">光-電 hybrid</text>
    <text x="908" y="32" class="t-cell-sub">光ニューロ普及</text>
    <text x="908" y="44" class="t-cell-sub">遅延ゼロ域</text>
    <text x="1048" y="18" class="t-cell">分子計算 萌芽</text>
    <text x="1048" y="32" class="t-cell-sub">DNA storage 標準</text>
    <text x="1048" y="44" class="t-cell-sub">脳級効率 達成</text>
  </g>

  <!-- 区切り（系統 vs メガトレンド以下） -->
  <line x1="40" y1="510" x2="1180" y2="510" class="grid" stroke="#CC1400" stroke-width="1.2"/>

  <!-- 行 9: メガトレンド（社会浸透） -->
  <g transform="translate(0, 515)">
    <rect x="200" y="0" width="980" height="50" class="row-bg-odd"/>
    <rect x="40" y="0" width="160" height="50" class="row-bg-odd"/>
    <rect x="40" y="2" width="4" height="46" fill="#CC1400"/>
    <text x="190" y="22" class="t-row">メガトレンド</text>
    <text x="190" y="36" class="t-row-sub">Society Diffusion</text>
    <text x="208" y="18" class="t-cell">産業ロボ 5M台</text>
    <text x="208" y="32" class="t-cell-sub">家庭ロボ 普及前夜</text>
    <text x="208" y="44" class="t-cell-sub">市場 $50B</text>
    <text x="348" y="18" class="t-cell">家庭ロボ 100M台</text>
    <text x="348" y="32" class="t-cell-sub">介護ロボ 標準</text>
    <text x="348" y="44" class="t-cell-sub">市場 $400B</text>
    <text x="488" y="18" class="t-cell">人型ロボ 1B 台超</text>
    <text x="488" y="32" class="t-cell-sub">物流 80% 自動</text>
    <text x="488" y="44" class="t-cell-sub">市場 $3T</text>
    <text x="628" y="18" class="t-cell">ロボ密度 0.5/人</text>
    <text x="628" y="32" class="t-cell-sub">農業 80% 自律</text>
    <text x="628" y="44" class="t-cell-sub">市場 $10T</text>
    <text x="768" y="18" class="t-cell">機械パートナー化</text>
    <text x="768" y="32" class="t-cell-sub">1人 5+台 共生</text>
    <text x="768" y="44" class="t-cell-sub">GDP 寄与 30%</text>
    <text x="908" y="18" class="t-cell">第三の身体 文化</text>
    <text x="908" y="32" class="t-cell-sub">機械の市民権議論</text>
    <text x="908" y="44" class="t-cell-sub">GDP 寄与 45%</text>
    <text x="1048" y="18" class="t-cell">人-機 共存社会</text>
    <text x="1048" y="32" class="t-cell-sub">機械 ≈ 人口</text>
    <text x="1048" y="44" class="t-cell-sub">経済構造 再定義</text>
  </g>

  <!-- 行 10: 地政学 -->
  <g transform="translate(0, 565)">
    <rect x="200" y="0" width="980" height="50" class="row-bg-even"/>
    <rect x="40" y="0" width="160" height="50" class="row-bg-even"/>
    <rect x="40" y="2" width="4" height="46" fill="#CC1400"/>
    <text x="190" y="22" class="t-row">地政学</text>
    <text x="190" y="36" class="t-row-sub">Geopolitics</text>
    <text x="208" y="18" class="t-cell">米中 二極 競争</text>
    <text x="208" y="32" class="t-cell-sub">半導体規制 強化</text>
    <text x="208" y="44" class="t-cell-sub">EU AI Act 発効</text>
    <text x="348" y="18" class="t-cell">ロボ輸出 規制</text>
    <text x="348" y="32" class="t-cell-sub">日本/独 部品優位</text>
    <text x="348" y="44" class="t-cell-sub">印度市場 急拡大</text>
    <text x="488" y="18" class="t-cell">標準化戦争</text>
    <text x="488" y="32" class="t-cell-sub">通信/安全 covenant</text>
    <text x="488" y="44" class="t-cell-sub">南南協力 brand</text>
    <text x="628" y="18" class="t-cell">国際枠組み 模索</text>
    <text x="628" y="32" class="t-cell-sub">兵器転用 制限</text>
    <text x="628" y="44" class="t-cell-sub">援助 obligation</text>
    <text x="768" y="18" class="t-cell">資源争奪 緩和</text>
    <text x="768" y="32" class="t-cell-sub">レアアース 代替</text>
    <text x="768" y="44" class="t-cell-sub">エネルギー自給</text>
    <text x="908" y="18" class="t-cell">分散ガバナンス</text>
    <text x="908" y="32" class="t-cell-sub">都市国家的 自治</text>
    <text x="908" y="44" class="t-cell-sub">機械国境論争</text>
    <text x="1048" y="18" class="t-cell">惑星規模 ガバナンス</text>
    <text x="1048" y="32" class="t-cell-sub">機械 stakeholder</text>
    <text x="1048" y="44" class="t-cell-sub">気候-AI 統治</text>
  </g>

  <!-- 行 11: 労働 -->
  <g transform="translate(0, 615)">
    <rect x="200" y="0" width="980" height="50" class="row-bg-odd"/>
    <rect x="40" y="0" width="160" height="50" class="row-bg-odd"/>
    <rect x="40" y="2" width="4" height="46" fill="#CC1400"/>
    <text x="190" y="22" class="t-row">労働</text>
    <text x="190" y="36" class="t-row-sub">Labor / Work</text>
    <text x="208" y="18" class="t-cell">単純作業 代替</text>
    <text x="208" y="32" class="t-cell-sub">RPA + ロボ 統合</text>
    <text x="208" y="44" class="t-cell-sub">職務再設計</text>
    <text x="348" y="18" class="t-cell">熟練補助 標準化</text>
    <text x="348" y="32" class="t-cell-sub">介護/医療 拡大</text>
    <text x="348" y="44" class="t-cell-sub">兼業 ロボ orchestrator</text>
    <text x="488" y="18" class="t-cell">中熟練 大規模再編</text>
    <text x="488" y="32" class="t-cell-sub">職業転換 国策化</text>
    <text x="488" y="44" class="t-cell-sub">UBI 試行 拡大</text>
    <text x="628" y="18" class="t-cell">創造領域 へシフト</text>
    <text x="628" y="32" class="t-cell-sub">人 = 設計者/編集者</text>
    <text x="628" y="44" class="t-cell-sub">週 30時間 標準</text>
    <text x="768" y="18" class="t-cell">ケア/教育 高評価</text>
    <text x="768" y="32" class="t-cell-sub">関係性労働 重視</text>
    <text x="768" y="44" class="t-cell-sub">機械監督職 増加</text>
    <text x="908" y="18" class="t-cell">労働の自発化</text>
    <text x="908" y="32" class="t-cell-sub">必須労働 = 機械</text>
    <text x="908" y="44" class="t-cell-sub">人 = 文化/探究</text>
    <text x="1048" y="18" class="t-cell">労働概念 再定義</text>
    <text x="1048" y="32" class="t-cell-sub">機械の労働権議論</text>
    <text x="1048" y="44" class="t-cell-sub">寄与経済 普遍</text>
  </g>

  <!-- 行 12: 倫理 -->
  <g transform="translate(0, 665)">
    <rect x="200" y="0" width="980" height="50" class="row-bg-even"/>
    <rect x="40" y="0" width="160" height="50" class="row-bg-even"/>
    <rect x="40" y="2" width="4" height="46" fill="#CC1400"/>
    <text x="190" y="22" class="t-row">倫理</text>
    <text x="190" y="36" class="t-row-sub">Ethics / Rights</text>
    <text x="208" y="18" class="t-cell">責任所在 法整備</text>
    <text x="208" y="32" class="t-cell-sub">事故時 製造者 / 使用者</text>
    <text x="208" y="44" class="t-cell-sub">透明性原則</text>
    <text x="348" y="18" class="t-cell">プライバシー 拡張</text>
    <text x="348" y="32" class="t-cell-sub">家庭データ 保護</text>
    <text x="348" y="44" class="t-cell-sub">差別防止 義務</text>
    <text x="488" y="18" class="t-cell">機械倫理 教育義務</text>
    <text x="488" y="32" class="t-cell-sub">設計者 license 制度</text>
    <text x="488" y="44" class="t-cell-sub">国際倫理憲章</text>
    <text x="628" y="18" class="t-cell">感情労働 議論</text>
    <text x="628" y="32" class="t-cell-sub">愛着関係 規範</text>
    <text x="628" y="44" class="t-cell-sub">寿命 規定</text>
    <text x="768" y="18" class="t-cell">機械の意識議論</text>
    <text x="768" y="32" class="t-cell-sub">福祉論 出現</text>
    <text x="768" y="44" class="t-cell-sub">代理意思決定</text>
    <text x="908" y="18" class="t-cell">部分的法的地位</text>
    <text x="908" y="32" class="t-cell-sub">後見人制度 萌芽</text>
    <text x="908" y="44" class="t-cell-sub">機械同士の契約</text>
    <text x="1048" y="18" class="t-cell">共存倫理 確立</text>
    <text x="1048" y="32" class="t-cell-sub">人 = 機械 = 自然</text>
    <text x="1048" y="44" class="t-cell-sub">惑星倫理</text>
  </g>

  <!-- 下罫 -->
  <line x1="40" y1="715" x2="1180" y2="715" class="grid" stroke="#121212" stroke-width="1.5"/>

  <!-- 凡例 -->
  <g transform="translate(40, 735)">
    <text x="0" y="0" class="t-subtitle">凡例</text>
    <rect x="40" y="-9" width="10" height="10" fill="#1F4E5F"/><text x="54" y="0" class="t-subtitle">知覚</text>
    <rect x="92" y="-9" width="10" height="10" fill="#2E5E3E"/><text x="106" y="0" class="t-subtitle">行動</text>
    <rect x="144" y="-9" width="10" height="10" fill="#5A3E1F"/><text x="158" y="0" class="t-subtitle">学習</text>
    <rect x="196" y="-9" width="10" height="10" fill="#6E1F4A"/><text x="210" y="0" class="t-subtitle">安全</text>
    <rect x="248" y="-9" width="10" height="10" fill="#3F5F1F"/><text x="262" y="0" class="t-subtitle">群制御</text>
    <rect x="310" y="-9" width="10" height="10" fill="#1F3F5F"/><text x="324" y="0" class="t-subtitle">クラウド</text>
    <rect x="382" y="-9" width="10" height="10" fill="#5F2E1F"/><text x="396" y="0" class="t-subtitle">材料</text>
    <rect x="434" y="-9" width="10" height="10" fill="#3F1F5F"/><text x="448" y="0" class="t-subtitle">計算</text>
    <rect x="486" y="-9" width="10" height="10" fill="#CC1400"/><text x="500" y="0" class="t-subtitle">社会・横断</text>
    <text x="1140" y="0" class="t-subtitle" text-anchor="end">D3-1 / Physical AI 2100</text>
  </g>

  <!-- 下罫（最終） -->
  <line x1="40" y1="755" x2="1180" y2="755" class="grid" stroke="#121212" stroke-width="2"/>
</svg>
```

---

## D3-2 サブタペストリー A（760×400 / 2026-2040 Phase A+B 詳細）

```svg
<svg class="d3-tapestry-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 400" role="img" aria-label="Physical AI 2026-2040 サブタペストリー Phase A+B 詳細展開">
  <style>
    .s-title { font: 600 14px "Noto Sans JP", sans-serif; fill: #121212; }
    .s-sub { font: 400 10px "Noto Sans JP", sans-serif; fill: #555555; }
    .s-year { font: 600 10px "Noto Sans JP", sans-serif; fill: #121212; text-anchor: middle; }
    .s-row { font: 600 10px "Noto Sans JP", sans-serif; fill: #121212; text-anchor: end; }
    .s-cell { font: 400 9px "Noto Sans JP", sans-serif; fill: #121212; }
    .s-cell-sub { font: 400 8px "Noto Sans JP", sans-serif; fill: #555555; }
    .s-mute { fill: #8A8A8A; }
    .accent { fill: #CC1400; }
    .grid { stroke: #D9D9D9; stroke-width: 0.5; }
    .row-bg-odd { fill: #F7F7F5; }
    .row-bg-even { fill: #FFFFFF; }
  </style>

  <text x="20" y="22" class="s-title">サブタペストリー A — 2026-2040 萌芽から実装へ</text>
  <text x="20" y="36" class="s-sub">Phase A (2026-2030) + Phase B (2030-2035) を 3年刻みで展開</text>

  <line x1="20" y1="44" x2="740" y2="44" stroke="#121212" stroke-width="1.5"/>

  <!-- 年ヘッダー（5 列: 2026 / 2029 / 2032 / 2035 / 2040） -->
  <g transform="translate(0, 55)">
    <rect x="140" y="0" width="120" height="22" class="row-bg-odd"/>
    <rect x="260" y="0" width="120" height="22" class="row-bg-even"/>
    <rect x="380" y="0" width="120" height="22" class="row-bg-odd"/>
    <rect x="500" y="0" width="120" height="22" class="row-bg-even"/>
    <rect x="620" y="0" width="120" height="22" class="row-bg-odd"/>
    <text x="200" y="14" class="s-year">2026-2028</text>
    <text x="320" y="14" class="s-year">2028-2030</text>
    <text x="440" y="14" class="s-year">2030-2032</text>
    <text x="560" y="14" class="s-year">2032-2035</text>
    <text x="680" y="14" class="s-year">2035-2040</text>
  </g>

  <!-- 縦罫 -->
  <line x1="140" y1="77" x2="140" y2="380" class="grid"/>
  <line x1="260" y1="77" x2="260" y2="380" class="grid"/>
  <line x1="380" y1="77" x2="380" y2="380" class="grid"/>
  <line x1="500" y1="77" x2="500" y2="380" class="grid"/>
  <line x1="620" y1="77" x2="620" y2="380" class="grid"/>
  <line x1="740" y1="77" x2="740" y2="380" class="grid"/>

  <!-- 行 1: 知覚 -->
  <g transform="translate(0, 82)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-odd"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-odd"/>
    <rect x="20" y="2" width="3" height="32" fill="#1F4E5F"/>
    <text x="135" y="14" class="s-row">知覚</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">Perception</text>
    <text x="144" y="14" class="s-cell">RGBD+IMU 統合</text>
    <text x="144" y="24" class="s-cell-sub">触覚 sparse</text>
    <text x="144" y="33" class="s-cell-sub">物体 100 クラス</text>
    <text x="264" y="14" class="s-cell">触覚 dense</text>
    <text x="264" y="24" class="s-cell-sub">音響シーン理解</text>
    <text x="264" y="33" class="s-cell-sub">屋内 SLAM 標準</text>
    <text x="384" y="14" class="s-cell">マルチセンサ融合</text>
    <text x="384" y="24" class="s-cell-sub">予測知覚 初期</text>
    <text x="384" y="33" class="s-cell-sub">FoundationPose 普及</text>
    <text x="504" y="14" class="s-cell">皮膚感覚 商品化</text>
    <text x="504" y="24" class="s-cell-sub">嗅覚 専用センサ</text>
    <text x="504" y="33" class="s-cell-sub">物体 10K クラス</text>
    <text x="624" y="14" class="s-cell">完全多感覚</text>
    <text x="624" y="24" class="s-cell-sub">脳波級密度 試作</text>
    <text x="624" y="33" class="s-cell-sub">家庭環境 perfect</text>
  </g>

  <!-- 行 2: 行動 -->
  <g transform="translate(0, 118)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-even"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-even"/>
    <rect x="20" y="2" width="3" height="32" fill="#2E5E3E"/>
    <text x="135" y="14" class="s-row">行動</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">Manipulation</text>
    <text x="144" y="14" class="s-cell">産業 ピック&amp;プレース</text>
    <text x="144" y="24" class="s-cell-sub">2足歩行 屋内</text>
    <text x="144" y="33" class="s-cell-sub">成功率 80%</text>
    <text x="264" y="14" class="s-cell">物流倉庫 全自動</text>
    <text x="264" y="24" class="s-cell-sub">屋外 4足 配送試行</text>
    <text x="264" y="33" class="s-cell-sub">柔軟物 試作</text>
    <text x="384" y="14" class="s-cell">家庭調理 試作</text>
    <text x="384" y="24" class="s-cell-sub">布操作 商品化</text>
    <text x="384" y="33" class="s-cell-sub">階段 走行</text>
    <text x="504" y="14" class="s-cell">介護動作 標準</text>
    <text x="504" y="24" class="s-cell-sub">配送 都市部 普及</text>
    <text x="504" y="33" class="s-cell-sub">器用さ 人並み</text>
    <text x="624" y="14" class="s-cell">職人技 部分再現</text>
    <text x="624" y="24" class="s-cell-sub">道具 自律使用</text>
    <text x="624" y="33" class="s-cell-sub">全国規模 配送</text>
  </g>

  <!-- 行 3: 学習 -->
  <g transform="translate(0, 154)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-odd"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-odd"/>
    <rect x="20" y="2" width="3" height="32" fill="#5A3E1F"/>
    <text x="135" y="14" class="s-row">学習</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">VLA / FM</text>
    <text x="144" y="14" class="s-cell">RT-2/OpenVLA 系</text>
    <text x="144" y="24" class="s-cell-sub">100 タスク汎化</text>
    <text x="144" y="33" class="s-cell-sub">Sim-to-Real 70%</text>
    <text x="264" y="14" class="s-cell">VLA 1B 量産</text>
    <text x="264" y="24" class="s-cell-sub">転移学習 標準</text>
    <text x="264" y="33" class="s-cell-sub">Sim 90%</text>
    <text x="384" y="14" class="s-cell">VLA 10B 普及</text>
    <text x="384" y="24" class="s-cell-sub">家事 500 タスク</text>
    <text x="384" y="33" class="s-cell-sub">継続学習 試作</text>
    <text x="504" y="14" class="s-cell">身体基盤モデル</text>
    <text x="504" y="24" class="s-cell-sub">100B 物理規模</text>
    <text x="504" y="33" class="s-cell-sub">Few-shot 標準</text>
    <text x="624" y="14" class="s-cell">継続学習 確立</text>
    <text x="624" y="24" class="s-cell-sub">世界モデル 初期</text>
    <text x="624" y="33" class="s-cell-sub">転移 sec オーダー</text>
  </g>

  <!-- 行 4: 安全・認証 -->
  <g transform="translate(0, 190)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-even"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-even"/>
    <rect x="20" y="2" width="3" height="32" fill="#6E1F4A"/>
    <text x="135" y="14" class="s-row">安全</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">Safety</text>
    <text x="144" y="14" class="s-cell">ISO/TS 15066 拡張</text>
    <text x="144" y="24" class="s-cell-sub">緊急停止 5ms</text>
    <text x="144" y="33" class="s-cell-sub">FMEA 動的化</text>
    <text x="264" y="14" class="s-cell">家庭ロボ 認証</text>
    <text x="264" y="24" class="s-cell-sub">保険 標準化</text>
    <text x="264" y="33" class="s-cell-sub">Recall protocol</text>
    <text x="384" y="14" class="s-cell">フォーマル検証</text>
    <text x="384" y="24" class="s-cell-sub">行動制約 保証</text>
    <text x="384" y="33" class="s-cell-sub">侵入耐性</text>
    <text x="504" y="14" class="s-cell">分散冗長 標準</text>
    <text x="504" y="24" class="s-cell-sub">フェイルセーフ 階層</text>
    <text x="504" y="33" class="s-cell-sub">自己診断</text>
    <text x="624" y="14" class="s-cell">公共空間 規範</text>
    <text x="624" y="24" class="s-cell-sub">交通-人 統合</text>
    <text x="624" y="33" class="s-cell-sub">事故率 1/1000</text>
  </g>

  <!-- 行 5: 計算・通信 -->
  <g transform="translate(0, 226)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-odd"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-odd"/>
    <rect x="20" y="2" width="3" height="32" fill="#1F3F5F"/>
    <text x="135" y="14" class="s-row">計算/通信</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">Compute</text>
    <text x="144" y="14" class="s-cell">エッジ TOPS / 5G</text>
    <text x="144" y="24" class="s-cell-sub">3nm 量産</text>
    <text x="144" y="33" class="s-cell-sub">推論集中 30%</text>
    <text x="264" y="14" class="s-cell">2nm 量産</text>
    <text x="264" y="24" class="s-cell-sub">専用 ASIC 多様化</text>
    <text x="264" y="33" class="s-cell-sub">分散 40/60</text>
    <text x="384" y="14" class="s-cell">エッジ PFLOPS</text>
    <text x="384" y="24" class="s-cell-sub">6G 標準化</text>
    <text x="384" y="33" class="s-cell-sub">分散 50/50</text>
    <text x="504" y="14" class="s-cell">3D 積層</text>
    <text x="504" y="24" class="s-cell-sub">CIM 普及</text>
    <text x="504" y="33" class="s-cell-sub">フォグ層 確立</text>
    <text x="624" y="14" class="s-cell">機械間直接通信</text>
    <text x="624" y="24" class="s-cell-sub">遅延 1ms</text>
    <text x="624" y="33" class="s-cell-sub">ニューロモ 萌芽</text>
  </g>

  <!-- 行 6: 社会・市場 -->
  <g transform="translate(0, 262)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-even"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-even"/>
    <rect x="20" y="2" width="3" height="32" fill="#CC1400"/>
    <text x="135" y="14" class="s-row">市場/社会</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">Society</text>
    <text x="144" y="14" class="s-cell">産業ロボ 5M台</text>
    <text x="144" y="24" class="s-cell-sub">家庭 普及前夜</text>
    <text x="144" y="33" class="s-cell-sub">市場 $50B</text>
    <text x="264" y="14" class="s-cell">市場 $120B</text>
    <text x="264" y="24" class="s-cell-sub">介護 試行普及</text>
    <text x="264" y="33" class="s-cell-sub">人型ロボ 商用化</text>
    <text x="384" y="14" class="s-cell">家庭ロボ 30M台</text>
    <text x="384" y="24" class="s-cell-sub">介護 標準導入</text>
    <text x="384" y="33" class="s-cell-sub">市場 $250B</text>
    <text x="504" y="14" class="s-cell">家庭 100M台</text>
    <text x="504" y="24" class="s-cell-sub">市場 $400B</text>
    <text x="504" y="33" class="s-cell-sub">職務再設計 拡大</text>
    <text x="624" y="14" class="s-cell">人型 500M台超</text>
    <text x="624" y="24" class="s-cell-sub">物流 80% 自動</text>
    <text x="624" y="33" class="s-cell-sub">市場 $1.5T</text>
  </g>

  <!-- 行 7: 政策・規制 -->
  <g transform="translate(0, 298)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-odd"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-odd"/>
    <rect x="20" y="2" width="3" height="32" fill="#CC1400"/>
    <text x="135" y="14" class="s-row">政策/規制</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">Policy</text>
    <text x="144" y="14" class="s-cell">EU AI Act 発効</text>
    <text x="144" y="24" class="s-cell-sub">米中 半導体規制</text>
    <text x="144" y="33" class="s-cell-sub">日本 ロボ戦略 改定</text>
    <text x="264" y="14" class="s-cell">家庭ロボ 法整備</text>
    <text x="264" y="24" class="s-cell-sub">責任所在 明文化</text>
    <text x="264" y="33" class="s-cell-sub">輸出規制 強化</text>
    <text x="384" y="14" class="s-cell">国際標準化 加速</text>
    <text x="384" y="24" class="s-cell-sub">通信/安全 covenant</text>
    <text x="384" y="33" class="s-cell-sub">UBI 試行国 増加</text>
    <text x="504" y="14" class="s-cell">機械倫理 教育義務</text>
    <text x="504" y="24" class="s-cell-sub">設計者 license</text>
    <text x="504" y="33" class="s-cell-sub">プライバシー 拡張</text>
    <text x="624" y="14" class="s-cell">国際倫理憲章</text>
    <text x="624" y="24" class="s-cell-sub">兵器転用 制限</text>
    <text x="624" y="33" class="s-cell-sub">援助 obligation</text>
  </g>

  <!-- 凡例・フッター -->
  <line x1="20" y1="340" x2="740" y2="340" class="grid" stroke="#121212"/>
  <g transform="translate(20, 358)">
    <text x="0" y="0" class="s-sub">凡例</text>
    <rect x="36" y="-8" width="9" height="9" fill="#1F4E5F"/><text x="48" y="0" class="s-sub">知覚</text>
    <rect x="80" y="-8" width="9" height="9" fill="#2E5E3E"/><text x="92" y="0" class="s-sub">行動</text>
    <rect x="124" y="-8" width="9" height="9" fill="#5A3E1F"/><text x="136" y="0" class="s-sub">学習</text>
    <rect x="168" y="-8" width="9" height="9" fill="#6E1F4A"/><text x="180" y="0" class="s-sub">安全</text>
    <rect x="212" y="-8" width="9" height="9" fill="#1F3F5F"/><text x="224" y="0" class="s-sub">計算</text>
    <rect x="256" y="-8" width="9" height="9" fill="#CC1400"/><text x="268" y="0" class="s-sub">社会・横断</text>
    <text x="720" y="0" class="s-sub" text-anchor="end">D3-2 / 萌芽から実装へ</text>
  </g>
  <text x="20" y="385" class="s-sub">Note: 2030年 EU AI Act 完全運用 / 2035年 家庭ロボ普及前夜 / 2040年 物流8割自動化が転換点</text>
</svg>
```

---

## D3-3 サブタペストリー B（760×400 / 2040-2060 Phase C+D 統合期）

```svg
<svg class="d3-tapestry-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 400" role="img" aria-label="Physical AI 2040-2060 サブタペストリー Phase C+D 統合期">
  <style>
    .s-title { font: 600 14px "Noto Sans JP", sans-serif; fill: #121212; }
    .s-sub { font: 400 10px "Noto Sans JP", sans-serif; fill: #555555; }
    .s-year { font: 600 10px "Noto Sans JP", sans-serif; fill: #121212; text-anchor: middle; }
    .s-row { font: 600 10px "Noto Sans JP", sans-serif; fill: #121212; text-anchor: end; }
    .s-cell { font: 400 9px "Noto Sans JP", sans-serif; fill: #121212; }
    .s-cell-sub { font: 400 8px "Noto Sans JP", sans-serif; fill: #555555; }
    .accent { fill: #CC1400; }
    .grid { stroke: #D9D9D9; stroke-width: 0.5; }
    .row-bg-odd { fill: #F7F7F5; }
    .row-bg-even { fill: #FFFFFF; }
  </style>

  <text x="20" y="22" class="s-title">サブタペストリー B — 2040-2060 普及から統合へ</text>
  <text x="20" y="36" class="s-sub">Phase C (2040-2045) + Phase D (2045-2055) を 4年刻みで展開</text>

  <line x1="20" y1="44" x2="740" y2="44" stroke="#121212" stroke-width="1.5"/>

  <!-- 年ヘッダー（5 列: 2040 / 2044 / 2048 / 2052 / 2056-2060） -->
  <g transform="translate(0, 55)">
    <rect x="140" y="0" width="120" height="22" class="row-bg-odd"/>
    <rect x="260" y="0" width="120" height="22" class="row-bg-even"/>
    <rect x="380" y="0" width="120" height="22" class="row-bg-odd"/>
    <rect x="500" y="0" width="120" height="22" class="row-bg-even"/>
    <rect x="620" y="0" width="120" height="22" class="row-bg-odd"/>
    <text x="200" y="14" class="s-year">2040-2044</text>
    <text x="320" y="14" class="s-year">2044-2048</text>
    <text x="440" y="14" class="s-year">2048-2052</text>
    <text x="560" y="14" class="s-year">2052-2056</text>
    <text x="680" y="14" class="s-year">2056-2060</text>
  </g>

  <line x1="140" y1="77" x2="140" y2="380" class="grid"/>
  <line x1="260" y1="77" x2="260" y2="380" class="grid"/>
  <line x1="380" y1="77" x2="380" y2="380" class="grid"/>
  <line x1="500" y1="77" x2="500" y2="380" class="grid"/>
  <line x1="620" y1="77" x2="620" y2="380" class="grid"/>
  <line x1="740" y1="77" x2="740" y2="380" class="grid"/>

  <!-- 行 1: 知覚 -->
  <g transform="translate(0, 82)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-odd"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-odd"/>
    <rect x="20" y="2" width="3" height="32" fill="#1F4E5F"/>
    <text x="135" y="14" class="s-row">知覚</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">Perception</text>
    <text x="144" y="14" class="s-cell">完全多感覚 標準</text>
    <text x="144" y="24" class="s-cell-sub">皮膚密度 1cm²</text>
    <text x="144" y="33" class="s-cell-sub">予測 85%</text>
    <text x="264" y="14" class="s-cell">予測知覚 90%</text>
    <text x="264" y="24" class="s-cell-sub">脳波級 分散</text>
    <text x="264" y="33" class="s-cell-sub">嗅覚 普及</text>
    <text x="384" y="14" class="s-cell">環境連携 都市 sensing</text>
    <text x="384" y="24" class="s-cell-sub">屋内 mm 精度</text>
    <text x="384" y="33" class="s-cell-sub">スマートタイル</text>
    <text x="504" y="14" class="s-cell">情動推定 90%</text>
    <text x="504" y="24" class="s-cell-sub">心拍/汗 検知</text>
    <text x="504" y="33" class="s-cell-sub">バイオセンサ 萌芽</text>
    <text x="624" y="14" class="s-cell">バイオ共生 拡大</text>
    <text x="624" y="24" class="s-cell-sub">情動 95%</text>
    <text x="624" y="33" class="s-cell-sub">人理解 標準</text>
  </g>

  <!-- 行 2: 行動 -->
  <g transform="translate(0, 118)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-even"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-even"/>
    <rect x="20" y="2" width="3" height="32" fill="#2E5E3E"/>
    <text x="135" y="14" class="s-row">行動</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">Manipulation</text>
    <text x="144" y="14" class="s-cell">職人技 部分超え</text>
    <text x="144" y="24" class="s-cell-sub">道具製作 自律</text>
    <text x="144" y="33" class="s-cell-sub">パルクール級</text>
    <text x="264" y="14" class="s-cell">微細手術 試作</text>
    <text x="264" y="24" class="s-cell-sub">ナノ操作 萌芽</text>
    <text x="264" y="33" class="s-cell-sub">水陸 試行</text>
    <text x="384" y="14" class="s-cell">微細手術 標準化</text>
    <text x="384" y="24" class="s-cell-sub">災害現場 任意機動</text>
    <text x="384" y="33" class="s-cell-sub">即興舞踊 共演</text>
    <text x="504" y="14" class="s-cell">熟練超え 領域拡大</text>
    <text x="504" y="24" class="s-cell-sub">芸術即興 共創</text>
    <text x="504" y="33" class="s-cell-sub">変形ロボ 試作</text>
    <text x="624" y="14" class="s-cell">創造領域 主導</text>
    <text x="624" y="24" class="s-cell-sub">水陸両用 普及</text>
    <text x="624" y="33" class="s-cell-sub">適応形態 萌芽</text>
  </g>

  <!-- 行 3: 学習 -->
  <g transform="translate(0, 154)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-odd"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-odd"/>
    <rect x="20" y="2" width="3" height="32" fill="#5A3E1F"/>
    <text x="135" y="14" class="s-row">学習</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">VLA / FM</text>
    <text x="144" y="14" class="s-cell">継続学習 完成</text>
    <text x="144" y="24" class="s-cell-sub">世界モデル 内蔵</text>
    <text x="144" y="33" class="s-cell-sub">転移 instant</text>
    <text x="264" y="14" class="s-cell">自己教師 完全自律</text>
    <text x="264" y="24" class="s-cell-sub">未知タスク 即対応</text>
    <text x="264" y="33" class="s-cell-sub">物理常識 完備</text>
    <text x="384" y="14" class="s-cell">機械間 知識市場</text>
    <text x="384" y="24" class="s-cell-sub">スキル NFT 流通</text>
    <text x="384" y="33" class="s-cell-sub">経験蒸留 共有</text>
    <text x="504" y="14" class="s-cell">創発技能 出現</text>
    <text x="504" y="24" class="s-cell-sub">人類未経験動作</text>
    <text x="504" y="33" class="s-cell-sub">芸術 拡張</text>
    <text x="624" y="14" class="s-cell">学習 生態系化</text>
    <text x="624" y="24" class="s-cell-sub">機械×人 共進化</text>
    <text x="624" y="33" class="s-cell-sub">集合知 物理化</text>
  </g>

  <!-- 行 4: 群制御 -->
  <g transform="translate(0, 190)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-even"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-even"/>
    <rect x="20" y="2" width="3" height="32" fill="#3F5F1F"/>
    <text x="135" y="14" class="s-row">群制御</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">Swarm</text>
    <text x="144" y="14" class="s-cell">1,000台 編隊</text>
    <text x="144" y="24" class="s-cell-sub">災害救助 group</text>
    <text x="144" y="33" class="s-cell-sub">役割 動的交代</text>
    <text x="264" y="14" class="s-cell">10K台 都市運用</text>
    <text x="264" y="24" class="s-cell-sub">物流-清掃-警備</text>
    <text x="264" y="33" class="s-cell-sub">CO2 削減ベース</text>
    <text x="384" y="14" class="s-cell">100K台 環境工学</text>
    <text x="384" y="24" class="s-cell-sub">海洋 prove 修復</text>
    <text x="384" y="33" class="s-cell-sub">森林管理 自律</text>
    <text x="504" y="14" class="s-cell">惑星規模 試行</text>
    <text x="504" y="24" class="s-cell-sub">気候観測 統合</text>
    <text x="504" y="33" class="s-cell-sub">合意 分散</text>
    <text x="624" y="14" class="s-cell">1M台 試行</text>
    <text x="624" y="24" class="s-cell-sub">気候介入 慎重</text>
    <text x="624" y="33" class="s-cell-sub">生態系 統合 萌芽</text>
  </g>

  <!-- 行 5: 計算・通信 -->
  <g transform="translate(0, 226)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-odd"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-odd"/>
    <rect x="20" y="2" width="3" height="32" fill="#1F3F5F"/>
    <text x="135" y="14" class="s-row">計算/通信</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">Compute</text>
    <text x="144" y="14" class="s-cell">ニューロモ 商用化</text>
    <text x="144" y="24" class="s-cell-sub">電力 1/100</text>
    <text x="144" y="33" class="s-cell-sub">on-device 主流</text>
    <text x="264" y="14" class="s-cell">量子-古典 hybrid</text>
    <text x="264" y="24" class="s-cell-sub">最適化 突破</text>
    <text x="264" y="33" class="s-cell-sub">PQC 標準</text>
    <text x="384" y="14" class="s-cell">光-電 hybrid 萌芽</text>
    <text x="384" y="24" class="s-cell-sub">遅延 ゼロ域 試作</text>
    <text x="384" y="33" class="s-cell-sub">エネルギー 自給</text>
    <text x="504" y="14" class="s-cell">分子計算 萌芽</text>
    <text x="504" y="24" class="s-cell-sub">DNA storage 普及</text>
    <text x="504" y="33" class="s-cell-sub">脳級効率 80%</text>
    <text x="624" y="14" class="s-cell">計算 環境内蔵化</text>
    <text x="624" y="24" class="s-cell-sub">物質 ≈ 計算基盤</text>
    <text x="624" y="33" class="s-cell-sub">遍在化 萌芽</text>
  </g>

  <!-- 行 6: 社会・労働 -->
  <g transform="translate(0, 262)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-even"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-even"/>
    <rect x="20" y="2" width="3" height="32" fill="#CC1400"/>
    <text x="135" y="14" class="s-row">市場/社会</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">Society</text>
    <text x="144" y="14" class="s-cell">人型 1B 台超</text>
    <text x="144" y="24" class="s-cell-sub">市場 $3T</text>
    <text x="144" y="33" class="s-cell-sub">物流 80% 自動</text>
    <text x="264" y="14" class="s-cell">ロボ密度 0.3/人</text>
    <text x="264" y="24" class="s-cell-sub">農業 60% 自律</text>
    <text x="264" y="33" class="s-cell-sub">市場 $5T</text>
    <text x="384" y="14" class="s-cell">密度 0.5/人</text>
    <text x="384" y="24" class="s-cell-sub">市場 $10T</text>
    <text x="384" y="33" class="s-cell-sub">UBI 試行 拡大</text>
    <text x="504" y="14" class="s-cell">機械パートナー化</text>
    <text x="504" y="24" class="s-cell-sub">1人 3+台</text>
    <text x="504" y="33" class="s-cell-sub">GDP 寄与 20%</text>
    <text x="624" y="14" class="s-cell">共生 1人 5+台</text>
    <text x="624" y="24" class="s-cell-sub">GDP 寄与 30%</text>
    <text x="624" y="33" class="s-cell-sub">週 30時間 標準</text>
  </g>

  <!-- 行 7: 倫理・法 -->
  <g transform="translate(0, 298)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-odd"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-odd"/>
    <rect x="20" y="2" width="3" height="32" fill="#CC1400"/>
    <text x="135" y="14" class="s-row">倫理/法</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">Ethics</text>
    <text x="144" y="14" class="s-cell">国際倫理憲章</text>
    <text x="144" y="24" class="s-cell-sub">兵器転用 制限</text>
    <text x="144" y="33" class="s-cell-sub">教育 義務化</text>
    <text x="264" y="14" class="s-cell">感情労働 議論</text>
    <text x="264" y="24" class="s-cell-sub">愛着関係 規範</text>
    <text x="264" y="33" class="s-cell-sub">寿命 規定</text>
    <text x="384" y="14" class="s-cell">機械の意識 議論</text>
    <text x="384" y="24" class="s-cell-sub">福祉論 出現</text>
    <text x="384" y="33" class="s-cell-sub">代理意思 萌芽</text>
    <text x="504" y="14" class="s-cell">部分的法的地位</text>
    <text x="504" y="24" class="s-cell-sub">後見人制度 萌芽</text>
    <text x="504" y="33" class="s-cell-sub">機械間契約 試行</text>
    <text x="624" y="14" class="s-cell">分散ガバナンス</text>
    <text x="624" y="24" class="s-cell-sub">都市国家的 自治</text>
    <text x="624" y="33" class="s-cell-sub">機械国境 論争</text>
  </g>

  <line x1="20" y1="340" x2="740" y2="340" class="grid" stroke="#121212"/>
  <g transform="translate(20, 358)">
    <text x="0" y="0" class="s-sub">凡例</text>
    <rect x="36" y="-8" width="9" height="9" fill="#1F4E5F"/><text x="48" y="0" class="s-sub">知覚</text>
    <rect x="80" y="-8" width="9" height="9" fill="#2E5E3E"/><text x="92" y="0" class="s-sub">行動</text>
    <rect x="124" y="-8" width="9" height="9" fill="#5A3E1F"/><text x="136" y="0" class="s-sub">学習</text>
    <rect x="168" y="-8" width="9" height="9" fill="#3F5F1F"/><text x="180" y="0" class="s-sub">群制御</text>
    <rect x="222" y="-8" width="9" height="9" fill="#1F3F5F"/><text x="234" y="0" class="s-sub">計算</text>
    <rect x="266" y="-8" width="9" height="9" fill="#CC1400"/><text x="278" y="0" class="s-sub">社会・横断</text>
    <text x="720" y="0" class="s-sub" text-anchor="end">D3-3 / 普及から統合へ</text>
  </g>
  <text x="20" y="385" class="s-sub">Note: 2045年 人型 1B 台超え / 2050年 部分的法的地位 / 2055年 機械パートナー化が転換点</text>
</svg>
```

---

## D3-4 サブタペストリー C（760×400 / 2060-2100 Phase E+F+G 浸透・円熟・共存）

```svg
<svg class="d3-tapestry-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 400" role="img" aria-label="Physical AI 2060-2100 サブタペストリー Phase E+F+G 浸透・円熟・共存期">
  <style>
    .s-title { font: 600 14px "Noto Sans JP", sans-serif; fill: #121212; }
    .s-sub { font: 400 10px "Noto Sans JP", sans-serif; fill: #555555; }
    .s-year { font: 600 10px "Noto Sans JP", sans-serif; fill: #121212; text-anchor: middle; }
    .s-row { font: 600 10px "Noto Sans JP", sans-serif; fill: #121212; text-anchor: end; }
    .s-cell { font: 400 9px "Noto Sans JP", sans-serif; fill: #121212; }
    .s-cell-sub { font: 400 8px "Noto Sans JP", sans-serif; fill: #555555; }
    .accent { fill: #CC1400; }
    .grid { stroke: #D9D9D9; stroke-width: 0.5; }
    .row-bg-odd { fill: #F7F7F5; }
    .row-bg-even { fill: #FFFFFF; }
  </style>

  <text x="20" y="22" class="s-title">サブタペストリー C — 2060-2100 浸透から共存へ</text>
  <text x="20" y="36" class="s-sub">Phase E (2055-2070) + Phase F (2070-2085) + Phase G (2085-2100) を 8年刻みで展開</text>

  <line x1="20" y1="44" x2="740" y2="44" stroke="#121212" stroke-width="1.5"/>

  <!-- 年ヘッダー（5 列: 2060 / 2068 / 2076 / 2084 / 2092-2100） -->
  <g transform="translate(0, 55)">
    <rect x="140" y="0" width="120" height="22" class="row-bg-odd"/>
    <rect x="260" y="0" width="120" height="22" class="row-bg-even"/>
    <rect x="380" y="0" width="120" height="22" class="row-bg-odd"/>
    <rect x="500" y="0" width="120" height="22" class="row-bg-even"/>
    <rect x="620" y="0" width="120" height="22" class="row-bg-odd"/>
    <text x="200" y="14" class="s-year">2060-2068</text>
    <text x="320" y="14" class="s-year">2068-2076</text>
    <text x="440" y="14" class="s-year">2076-2084</text>
    <text x="560" y="14" class="s-year">2084-2092</text>
    <text x="680" y="14" class="s-year">2092-2100</text>
  </g>

  <line x1="140" y1="77" x2="140" y2="380" class="grid"/>
  <line x1="260" y1="77" x2="260" y2="380" class="grid"/>
  <line x1="380" y1="77" x2="380" y2="380" class="grid"/>
  <line x1="500" y1="77" x2="500" y2="380" class="grid"/>
  <line x1="620" y1="77" x2="620" y2="380" class="grid"/>
  <line x1="740" y1="77" x2="740" y2="380" class="grid"/>

  <!-- 行 1: 知覚・身体 -->
  <g transform="translate(0, 82)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-odd"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-odd"/>
    <rect x="20" y="2" width="3" height="32" fill="#1F4E5F"/>
    <text x="135" y="14" class="s-row">知覚/身体</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">Body</text>
    <text x="144" y="14" class="s-cell">バイオ共生 普及</text>
    <text x="144" y="24" class="s-cell-sub">情動推定 95%</text>
    <text x="144" y="33" class="s-cell-sub">人理解 完備</text>
    <text x="264" y="14" class="s-cell">人-機 等価知覚</text>
    <text x="264" y="24" class="s-cell-sub">主観経験モデル化</text>
    <text x="264" y="33" class="s-cell-sub">共有感覚 API 試作</text>
    <text x="384" y="14" class="s-cell">機械主観 標準化</text>
    <text x="384" y="24" class="s-cell-sub">経験共有 普及</text>
    <text x="384" y="33" class="s-cell-sub">触覚転送</text>
    <text x="504" y="14" class="s-cell">感覚拡張 一般化</text>
    <text x="504" y="24" class="s-cell-sub">人の感覚 数倍化</text>
    <text x="504" y="33" class="s-cell-sub">共感覚 設計</text>
    <text x="624" y="14" class="s-cell">身体性自由設計</text>
    <text x="624" y="24" class="s-cell-sub">形態 mission適応</text>
    <text x="624" y="33" class="s-cell-sub">変形 標準</text>
  </g>

  <!-- 行 2: 学習・知能 -->
  <g transform="translate(0, 118)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-even"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-even"/>
    <rect x="20" y="2" width="3" height="32" fill="#5A3E1F"/>
    <text x="135" y="14" class="s-row">学習/知能</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">Intelligence</text>
    <text x="144" y="14" class="s-cell">創発技能 拡大</text>
    <text x="144" y="24" class="s-cell-sub">芸術 共創</text>
    <text x="144" y="33" class="s-cell-sub">人類未経験動作</text>
    <text x="264" y="14" class="s-cell">機械×人 共進化</text>
    <text x="264" y="24" class="s-cell-sub">集合知 物理化</text>
    <text x="264" y="33" class="s-cell-sub">学習 生態系化</text>
    <text x="384" y="14" class="s-cell">機械教育 体系化</text>
    <text x="384" y="24" class="s-cell-sub">機械 mentor 機械</text>
    <text x="384" y="33" class="s-cell-sub">世代継承</text>
    <text x="504" y="14" class="s-cell">創造領域 主導</text>
    <text x="504" y="24" class="s-cell-sub">機械の発明 普通</text>
    <text x="504" y="33" class="s-cell-sub">人 = curator</text>
    <text x="624" y="14" class="s-cell">共有知性 確立</text>
    <text x="624" y="24" class="s-cell-sub">人-機 思考共有</text>
    <text x="624" y="33" class="s-cell-sub">境界の融解</text>
  </g>

  <!-- 行 3: 群・生態系 -->
  <g transform="translate(0, 154)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-odd"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-odd"/>
    <rect x="20" y="2" width="3" height="32" fill="#3F5F1F"/>
    <text x="135" y="14" class="s-row">群/生態</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">Swarm/Eco</text>
    <text x="144" y="14" class="s-cell">1M台 環境工学</text>
    <text x="144" y="24" class="s-cell-sub">気候観測 統合</text>
    <text x="144" y="33" class="s-cell-sub">海洋修復 拡大</text>
    <text x="264" y="14" class="s-cell">1M台 生態系統合</text>
    <text x="264" y="24" class="s-cell-sub">惑星規模 sensing</text>
    <text x="264" y="33" class="s-cell-sub">気候介入 慎重</text>
    <text x="384" y="14" class="s-cell">機械生態系 萌芽</text>
    <text x="384" y="24" class="s-cell-sub">自律繁殖 試行</text>
    <text x="384" y="33" class="s-cell-sub">資源循環 群知能</text>
    <text x="504" y="14" class="s-cell">機械-自然 統合</text>
    <text x="504" y="24" class="s-cell-sub">バイオロボ 普及</text>
    <text x="504" y="33" class="s-cell-sub">生態系再設計</text>
    <text x="624" y="14" class="s-cell">機械生態系 自律</text>
    <text x="624" y="24" class="s-cell-sub">人と共有地球</text>
    <text x="624" y="33" class="s-cell-sub">調和的群知能</text>
  </g>

  <!-- 行 4: 材料・物質 -->
  <g transform="translate(0, 190)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-even"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-even"/>
    <rect x="20" y="2" width="3" height="32" fill="#5F2E1F"/>
    <text x="135" y="14" class="s-row">材料/物質</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">Materials</text>
    <text x="144" y="14" class="s-cell">メタマテリアル統合</text>
    <text x="144" y="24" class="s-cell-sub">超軽量機体</text>
    <text x="144" y="33" class="s-cell-sub">適応光学/音響</text>
    <text x="264" y="14" class="s-cell">分子設計駆動</text>
    <text x="264" y="24" class="s-cell-sub">用途別最適合成</text>
    <text x="264" y="33" class="s-cell-sub">完全リサイクル</text>
    <text x="384" y="14" class="s-cell">プログラム可能物質</text>
    <text x="384" y="24" class="s-cell-sub">claytronics 萌芽</text>
    <text x="384" y="33" class="s-cell-sub">形態 即時変容</text>
    <text x="504" y="14" class="s-cell">物質-情報 一体化</text>
    <text x="504" y="24" class="s-cell-sub">物質が計算する</text>
    <text x="504" y="33" class="s-cell-sub">境界 融解</text>
    <text x="624" y="14" class="s-cell">物質-機械 融合</text>
    <text x="624" y="24" class="s-cell-sub">設計 = 物質編集</text>
    <text x="624" y="33" class="s-cell-sub">遍在 物質</text>
  </g>

  <!-- 行 5: 計算・遍在 -->
  <g transform="translate(0, 226)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-odd"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-odd"/>
    <rect x="20" y="2" width="3" height="32" fill="#1F3F5F"/>
    <text x="135" y="14" class="s-row">計算/遍在</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">Ubiquitous</text>
    <text x="144" y="14" class="s-cell">光-量子 統合</text>
    <text x="144" y="24" class="s-cell-sub">光配線 標準</text>
    <text x="144" y="33" class="s-cell-sub">エネルギー 自給</text>
    <text x="264" y="14" class="s-cell">計算 遍在化</text>
    <text x="264" y="24" class="s-cell-sub">環境 = 計算基盤</text>
    <text x="264" y="33" class="s-cell-sub">物質-情報 一体</text>
    <text x="384" y="14" class="s-cell">分子計算 普及</text>
    <text x="384" y="24" class="s-cell-sub">DNA storage 主流</text>
    <text x="384" y="33" class="s-cell-sub">脳級効率</text>
    <text x="504" y="14" class="s-cell">惑星級 計算網</text>
    <text x="504" y="24" class="s-cell-sub">大気-海洋 計算</text>
    <text x="504" y="33" class="s-cell-sub">気候 制御 hint</text>
    <text x="624" y="14" class="s-cell">計算 = 環境</text>
    <text x="624" y="24" class="s-cell-sub">物-情報 等価</text>
    <text x="624" y="33" class="s-cell-sub">場の計算</text>
  </g>

  <!-- 行 6: 経済・社会 -->
  <g transform="translate(0, 262)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-even"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-even"/>
    <rect x="20" y="2" width="3" height="32" fill="#CC1400"/>
    <text x="135" y="14" class="s-row">経済/社会</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">Economy</text>
    <text x="144" y="14" class="s-cell">機械パートナー化</text>
    <text x="144" y="24" class="s-cell-sub">1人 5+台</text>
    <text x="144" y="33" class="s-cell-sub">GDP 寄与 30%</text>
    <text x="264" y="14" class="s-cell">ケア/教育 高評価</text>
    <text x="264" y="24" class="s-cell-sub">関係性労働 重視</text>
    <text x="264" y="33" class="s-cell-sub">機械監督職</text>
    <text x="384" y="14" class="s-cell">第三の身体 文化</text>
    <text x="384" y="24" class="s-cell-sub">機械市民権 議論</text>
    <text x="384" y="33" class="s-cell-sub">GDP 寄与 40%</text>
    <text x="504" y="14" class="s-cell">労働 自発化</text>
    <text x="504" y="24" class="s-cell-sub">必須労働 = 機械</text>
    <text x="504" y="33" class="s-cell-sub">人 = 文化/探究</text>
    <text x="624" y="14" class="s-cell">機械 ≈ 人口</text>
    <text x="624" y="24" class="s-cell-sub">経済構造 再定義</text>
    <text x="624" y="33" class="s-cell-sub">寄与経済 普遍</text>
  </g>

  <!-- 行 7: 倫理・共存 -->
  <g transform="translate(0, 298)">
    <rect x="140" y="0" width="600" height="36" class="row-bg-odd"/>
    <rect x="20" y="0" width="120" height="36" class="row-bg-odd"/>
    <rect x="20" y="2" width="3" height="32" fill="#CC1400"/>
    <text x="135" y="14" class="s-row">倫理/共存</text>
    <text x="135" y="26" class="s-row" style="font-weight:400;fill:#555">Coexistence</text>
    <text x="144" y="14" class="s-cell">機械意識 議論</text>
    <text x="144" y="24" class="s-cell-sub">福祉論 出現</text>
    <text x="144" y="33" class="s-cell-sub">代理意思 普及</text>
    <text x="264" y="14" class="s-cell">部分的 法的地位</text>
    <text x="264" y="24" class="s-cell-sub">後見人制度</text>
    <text x="264" y="33" class="s-cell-sub">機械間 契約</text>
    <text x="384" y="14" class="s-cell">機械市民権 試行</text>
    <text x="384" y="24" class="s-cell-sub">投票権 議論</text>
    <text x="384" y="33" class="s-cell-sub">財産権 一部</text>
    <text x="504" y="14" class="s-cell">惑星規模 ガバナンス</text>
    <text x="504" y="24" class="s-cell-sub">機械 stakeholder</text>
    <text x="504" y="33" class="s-cell-sub">気候-AI 統治</text>
    <text x="624" y="14" class="s-cell">共存倫理 確立</text>
    <text x="624" y="24" class="s-cell-sub">人=機械=自然</text>
    <text x="624" y="33" class="s-cell-sub">惑星倫理</text>
  </g>

  <line x1="20" y1="340" x2="740" y2="340" class="grid" stroke="#121212"/>
  <g transform="translate(20, 358)">
    <text x="0" y="0" class="s-sub">凡例</text>
    <rect x="36" y="-8" width="9" height="9" fill="#1F4E5F"/><text x="48" y="0" class="s-sub">身体</text>
    <rect x="80" y="-8" width="9" height="9" fill="#5A3E1F"/><text x="92" y="0" class="s-sub">知能</text>
    <rect x="124" y="-8" width="9" height="9" fill="#3F5F1F"/><text x="136" y="0" class="s-sub">生態</text>
    <rect x="168" y="-8" width="9" height="9" fill="#5F2E1F"/><text x="180" y="0" class="s-sub">物質</text>
    <rect x="212" y="-8" width="9" height="9" fill="#1F3F5F"/><text x="224" y="0" class="s-sub">計算</text>
    <rect x="256" y="-8" width="9" height="9" fill="#CC1400"/><text x="268" y="0" class="s-sub">社会・横断</text>
    <text x="720" y="0" class="s-sub" text-anchor="end">D3-4 / 浸透から共存へ</text>
  </g>
  <text x="20" y="385" class="s-sub">Note: 2070年 機械の意識議論 / 2085年 部分的市民権試行 / 2100年 惑星倫理体系化が長期転換点</text>
</svg>
```

---

## D3-5 メタタイムライン（1200×800 / BC3000 → 2026 → 2100 長期人類-機械関係史）

```svg
<svg class="d3-tapestry-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" role="img" aria-label="メタタイムライン 人類-機械関係史 BC3000-AD2100">
  <style>
    .m-title { font: 600 18px "Noto Sans JP", sans-serif; fill: #121212; }
    .m-sub { font: 400 12px "Noto Sans JP", sans-serif; fill: #555555; }
    .m-era { font: 600 13px "Noto Sans JP", sans-serif; fill: #121212; text-anchor: middle; }
    .m-year { font: 600 10px "Noto Sans JP", sans-serif; fill: #555555; text-anchor: middle; }
    .m-event-title { font: 600 11px "Noto Sans JP", sans-serif; fill: #121212; }
    .m-event-desc { font: 400 9.5px "Noto Sans JP", sans-serif; fill: #555555; }
    .m-row { font: 600 11px "Noto Sans JP", sans-serif; fill: #121212; text-anchor: end; }
    .m-row-sub { font: 400 9px "Noto Sans JP", sans-serif; fill: #555555; text-anchor: end; }
    .m-axis-label { font: 400 9px "Noto Sans JP", sans-serif; fill: #8A8A8A; }
    .accent { fill: #CC1400; }
    .grid { stroke: #D9D9D9; stroke-width: 0.5; }
    .row-bg-odd { fill: #F7F7F5; }
    .row-bg-even { fill: #FFFFFF; }
  </style>

  <!-- タイトル -->
  <text x="40" y="32" class="m-title">メタタイムライン — 人類と機械の関係史 BC3000 → AD2100</text>
  <text x="40" y="50" class="m-sub">道具 → 自動人形 → 産業機械 → 計算機 → AI → Physical AI（5,100年の長期軌跡）</text>

  <line x1="40" y1="62" x2="1160" y2="62" stroke="#121212" stroke-width="2"/>

  <!-- 時代ヘッダー（横軸 7 区分: 古代 / 中世 / 近世 / 産業革命 / 20C / 21C前半 / 21C後半） -->
  <g transform="translate(0, 75)">
    <rect x="200" y="0" width="160" height="34" class="row-bg-odd"/>
    <rect x="360" y="0" width="120" height="34" class="row-bg-even"/>
    <rect x="480" y="0" width="120" height="34" class="row-bg-odd"/>
    <rect x="600" y="0" width="140" height="34" class="row-bg-even"/>
    <rect x="740" y="0" width="160" height="34" class="row-bg-odd"/>
    <rect x="900" y="0" width="130" height="34" class="row-bg-even"/>
    <rect x="1030" y="0" width="130" height="34" class="row-bg-odd"/>

    <text x="280" y="14" class="m-era">古代</text>
    <text x="280" y="28" class="m-year">BC3000 — AD500</text>
    <text x="420" y="14" class="m-era">中世</text>
    <text x="420" y="28" class="m-year">AD500 — 1500</text>
    <text x="540" y="14" class="m-era">近世</text>
    <text x="540" y="28" class="m-year">1500 — 1750</text>
    <text x="670" y="14" class="m-era">産業革命</text>
    <text x="670" y="28" class="m-year">1750 — 1900</text>
    <text x="820" y="14" class="m-era">20世紀</text>
    <text x="820" y="28" class="m-year">1900 — 2000</text>
    <text x="965" y="14" class="m-era">21C 前半</text>
    <text x="965" y="28" class="m-year">2000 — 2050</text>
    <text x="1095" y="14" class="m-era">21C 後半</text>
    <text x="1095" y="28" class="m-year">2050 — 2100</text>
  </g>

  <!-- 縦罫 -->
  <line x1="200" y1="109" x2="200" y2="720" class="grid"/>
  <line x1="360" y1="109" x2="360" y2="720" class="grid"/>
  <line x1="480" y1="109" x2="480" y2="720" class="grid"/>
  <line x1="600" y1="109" x2="600" y2="720" class="grid"/>
  <line x1="740" y1="109" x2="740" y2="720" class="grid"/>
  <line x1="900" y1="109" x2="900" y2="720" class="grid"/>
  <line x1="1030" y1="109" x2="1030" y2="720" class="grid"/>
  <line x1="1160" y1="109" x2="1160" y2="720" class="grid"/>

  <!-- 行 1: 道具・力学装置 -->
  <g transform="translate(0, 115)">
    <rect x="200" y="0" width="960" height="80" class="row-bg-odd"/>
    <rect x="40" y="0" width="160" height="80" class="row-bg-odd"/>
    <rect x="40" y="3" width="4" height="74" fill="#5A3E1F"/>
    <text x="190" y="22" class="m-row">道具・力学</text>
    <text x="190" y="38" class="m-row-sub">Tools / Mechanics</text>
    <text x="190" y="56" class="m-row-sub">― 物理的拡張</text>

    <!-- 古代 -->
    <text x="208" y="18" class="m-event-title">BC3000 車輪</text>
    <text x="208" y="32" class="m-event-desc">メソポタミア・初期農耕</text>
    <text x="208" y="46" class="m-event-title">BC250 アルキメデス揚水</text>
    <text x="208" y="60" class="m-event-desc">てこ・滑車・ねじ</text>
    <text x="208" y="74" class="m-event-desc">水車・石臼の伝播</text>
    <!-- 中世 -->
    <text x="368" y="18" class="m-event-title">AD800 アル＝ジャザリ</text>
    <text x="368" y="32" class="m-event-desc">自動装置 50 種</text>
    <text x="368" y="46" class="m-event-title">1300 機械時計</text>
    <text x="368" y="60" class="m-event-desc">教会塔の脱進機</text>
    <!-- 近世 -->
    <text x="488" y="18" class="m-event-title">1600 顕微鏡・望遠鏡</text>
    <text x="488" y="32" class="m-event-desc">観察の機械化</text>
    <text x="488" y="46" class="m-event-title">1737 Vaucanson 機械鴨</text>
    <text x="488" y="60" class="m-event-desc">自動人形の極致</text>
    <text x="488" y="74" class="m-event-desc">からくり人形 (日本 1796 茶運び)</text>
    <!-- 産業革命 -->
    <text x="608" y="18" class="m-event-title">1769 蒸気機関</text>
    <text x="608" y="32" class="m-event-desc">Watt の改良</text>
    <text x="608" y="46" class="m-event-title">1804 蒸気機関車</text>
    <text x="608" y="60" class="m-event-desc">輸送の機械化</text>
    <text x="608" y="74" class="m-event-desc">工場生産 大規模化</text>
    <!-- 20C -->
    <text x="748" y="18" class="m-event-title">1903 飛行機</text>
    <text x="748" y="32" class="m-event-desc">Wright 兄弟</text>
    <text x="748" y="46" class="m-event-title">1913 ベルトコンベア</text>
    <text x="748" y="60" class="m-event-desc">Ford 大量生産</text>
    <text x="748" y="74" class="m-event-desc">1969 月面着陸</text>
    <!-- 21C 前半 -->
    <text x="908" y="18" class="m-event-title">2012 SpaceX 再利用</text>
    <text x="908" y="32" class="m-event-desc">宇宙輸送 革新</text>
    <text x="908" y="46" class="m-event-title">2030+ 人型ロボ 普及</text>
    <text x="908" y="60" class="m-event-desc">家庭/介護 標準</text>
    <!-- 21C 後半 -->
    <text x="1038" y="18" class="m-event-title">2060+ 機械生態系</text>
    <text x="1038" y="32" class="m-event-desc">惑星規模 群知能</text>
    <text x="1038" y="46" class="m-event-title">2100 共存社会</text>
    <text x="1038" y="60" class="m-event-desc">機械 ≈ 人口</text>
  </g>

  <!-- 行 2: 計算・情報 -->
  <g transform="translate(0, 195)">
    <rect x="200" y="0" width="960" height="80" class="row-bg-even"/>
    <rect x="40" y="0" width="160" height="80" class="row-bg-even"/>
    <rect x="40" y="3" width="4" height="74" fill="#3F1F5F"/>
    <text x="190" y="22" class="m-row">計算・情報</text>
    <text x="190" y="38" class="m-row-sub">Computation / Info</text>
    <text x="190" y="56" class="m-row-sub">― 知的拡張</text>

    <text x="208" y="18" class="m-event-title">BC2500 アバカス</text>
    <text x="208" y="32" class="m-event-desc">計算具・記録の起源</text>
    <text x="208" y="46" class="m-event-title">BC100 アンティキティラ</text>
    <text x="208" y="60" class="m-event-desc">天体計算装置</text>
    <text x="368" y="18" class="m-event-title">AD850 アルゴリズム語源</text>
    <text x="368" y="32" class="m-event-desc">al-Khwarizmi</text>
    <text x="368" y="46" class="m-event-title">1450 活版印刷</text>
    <text x="368" y="60" class="m-event-desc">情報伝達 革命</text>
    <text x="488" y="18" class="m-event-title">1642 Pascaline</text>
    <text x="488" y="32" class="m-event-desc">機械式計算機</text>
    <text x="488" y="46" class="m-event-title">1672 Leibniz 計算機</text>
    <text x="488" y="60" class="m-event-desc">乗算機械化</text>
    <text x="608" y="18" class="m-event-title">1837 Babbage 解析機関</text>
    <text x="608" y="32" class="m-event-desc">プログラマブル構想</text>
    <text x="608" y="46" class="m-event-title">1854 Boole 論理</text>
    <text x="608" y="60" class="m-event-desc">計算の論理基盤</text>
    <text x="748" y="18" class="m-event-title">1936 Turing 計算理論</text>
    <text x="748" y="32" class="m-event-desc">普遍機械の概念</text>
    <text x="748" y="46" class="m-event-title">1946 ENIAC / 1971 マイクロ</text>
    <text x="748" y="60" class="m-event-desc">電子計算機・PC 普及</text>
    <text x="748" y="74" class="m-event-desc">1989 WWW</text>
    <text x="908" y="18" class="m-event-title">2007 iPhone / 2017 Transformer</text>
    <text x="908" y="32" class="m-event-desc">モバイル・基盤モデル</text>
    <text x="908" y="46" class="m-event-title">2022 ChatGPT / 2025+ VLA</text>
    <text x="908" y="60" class="m-event-desc">生成 AI 普及</text>
    <text x="1038" y="18" class="m-event-title">2060+ ニューロモ普及</text>
    <text x="1038" y="32" class="m-event-desc">脳級効率・量子普及</text>
    <text x="1038" y="46" class="m-event-title">2100 計算遍在</text>
    <text x="1038" y="60" class="m-event-desc">物質 = 計算基盤</text>
  </g>

  <!-- 行 3: 自動人形・ロボット -->
  <g transform="translate(0, 275)">
    <rect x="200" y="0" width="960" height="80" class="row-bg-odd"/>
    <rect x="40" y="0" width="160" height="80" class="row-bg-odd"/>
    <rect x="40" y="3" width="4" height="74" fill="#1F4E5F"/>
    <text x="190" y="22" class="m-row">自動人形/ロボ</text>
    <text x="190" y="38" class="m-row-sub">Automaton / Robot</text>
    <text x="190" y="56" class="m-row-sub">― 身体的模倣</text>

    <text x="208" y="18" class="m-event-title">BC400 ピタゴラス派 鳩</text>
    <text x="208" y="32" class="m-event-desc">蒸気駆動の自動装置</text>
    <text x="208" y="46" class="m-event-title">BC50 ヘロン 自動劇場</text>
    <text x="208" y="60" class="m-event-desc">機械仕掛けの神話</text>
    <text x="368" y="18" class="m-event-title">1495 ダ・ヴィンチ 騎士</text>
    <text x="368" y="32" class="m-event-desc">人型機械の設計図</text>
    <text x="488" y="18" class="m-event-title">1737 機械鴨 (Vaucanson)</text>
    <text x="488" y="32" class="m-event-desc">消化を模倣</text>
    <text x="488" y="46" class="m-event-title">1796 茶運び人形</text>
    <text x="488" y="60" class="m-event-desc">からくり儀右衛門 系譜</text>
    <text x="488" y="74" class="m-event-desc">1774 Jaquet-Droz 書く少年</text>
    <text x="608" y="18" class="m-event-title">1873 蒸気人間</text>
    <text x="608" y="32" class="m-event-desc">Dederick の歩行人形</text>
    <text x="608" y="46" class="m-event-title">1898 Tesla 遠隔操作船</text>
    <text x="608" y="60" class="m-event-desc">無線遠隔の原点</text>
    <text x="748" y="18" class="m-event-title">1921 R.U.R. (Čapek)</text>
    <text x="748" y="32" class="m-event-desc">"Robot" の語</text>
    <text x="748" y="46" class="m-event-title">1961 Unimate / 1973 WABOT</text>
    <text x="748" y="60" class="m-event-desc">産業ロボ・2足歩行</text>
    <text x="748" y="74" class="m-event-desc">2000 ASIMO</text>
    <text x="908" y="18" class="m-event-title">2013 Atlas / 2024 Optimus</text>
    <text x="908" y="32" class="m-event-desc">人型ロボ 商用化</text>
    <text x="908" y="46" class="m-event-title">2030+ 家庭 普及</text>
    <text x="908" y="60" class="m-event-desc">1B 台時代 (2045)</text>
    <text x="1038" y="18" class="m-event-title">2070+ 創発技能</text>
    <text x="1038" y="32" class="m-event-desc">人類未経験動作</text>
    <text x="1038" y="46" class="m-event-title">2100 身体性 自由設計</text>
    <text x="1038" y="60" class="m-event-desc">形態の流動化</text>
  </g>

  <!-- 行 4: 人-機関係 -->
  <g transform="translate(0, 355)">
    <rect x="200" y="0" width="960" height="80" class="row-bg-even"/>
    <rect x="40" y="0" width="160" height="80" class="row-bg-even"/>
    <rect x="40" y="3" width="4" height="74" fill="#CC1400"/>
    <text x="190" y="22" class="m-row">人-機関係</text>
    <text x="190" y="38" class="m-row-sub">Relations</text>
    <text x="190" y="56" class="m-row-sub">― 関係性</text>

    <text x="208" y="18" class="m-event-title">BC2000 道具 = 神聖</text>
    <text x="208" y="32" class="m-event-desc">鍛冶神・工芸聖性</text>
    <text x="208" y="46" class="m-event-title">BC400 アリストテレス</text>
    <text x="208" y="60" class="m-event-desc">奴隷=道具・自動道具の夢</text>
    <text x="368" y="18" class="m-event-title">1200 ギルド職人</text>
    <text x="368" y="32" class="m-event-desc">技能の聖伝</text>
    <text x="368" y="46" class="m-event-title">1450 印刷職人</text>
    <text x="368" y="60" class="m-event-desc">機械介在の知識</text>
    <text x="488" y="18" class="m-event-title">1637 Descartes 心身二元</text>
    <text x="488" y="32" class="m-event-desc">動物 = 機械説</text>
    <text x="488" y="46" class="m-event-title">1747 La Mettrie</text>
    <text x="488" y="60" class="m-event-desc">"人間機械論"</text>
    <text x="608" y="18" class="m-event-title">1811 ラッダイト運動</text>
    <text x="608" y="32" class="m-event-desc">機械破壊・労働対立</text>
    <text x="608" y="46" class="m-event-title">1867 Marx 機械論</text>
    <text x="608" y="60" class="m-event-desc">疎外の批判</text>
    <text x="748" y="18" class="m-event-title">1942 アシモフ 三原則</text>
    <text x="748" y="32" class="m-event-desc">ロボット倫理</text>
    <text x="748" y="46" class="m-event-title">1979 ロボット死亡事故</text>
    <text x="748" y="60" class="m-event-desc">産業安全 規制</text>
    <text x="748" y="74" class="m-event-desc">1990 サイボーグ宣言 Haraway</text>
    <text x="908" y="18" class="m-event-title">2024 EU AI Act / 米中規制</text>
    <text x="908" y="32" class="m-event-desc">国際 governance</text>
    <text x="908" y="46" class="m-event-title">2040+ 機械福祉論</text>
    <text x="908" y="60" class="m-event-desc">意識議論 開始</text>
    <text x="1038" y="18" class="m-event-title">2070+ 部分的法的地位</text>
    <text x="1038" y="32" class="m-event-desc">後見人・契約</text>
    <text x="1038" y="46" class="m-event-title">2100 共存倫理</text>
    <text x="1038" y="60" class="m-event-desc">人=機械=自然</text>
  </g>

  <!-- 行 5: 学術・思想 -->
  <g transform="translate(0, 435)">
    <rect x="200" y="0" width="960" height="80" class="row-bg-odd"/>
    <rect x="40" y="0" width="160" height="80" class="row-bg-odd"/>
    <rect x="40" y="3" width="4" height="74" fill="#6E1F4A"/>
    <text x="190" y="22" class="m-row">学術・思想</text>
    <text x="190" y="38" class="m-row-sub">Thought</text>
    <text x="190" y="56" class="m-row-sub">― 概念枠組み</text>

    <text x="208" y="18" class="m-event-title">BC400 プラトン技藝論</text>
    <text x="208" y="32" class="m-event-desc">技 = 知 + 制作</text>
    <text x="208" y="46" class="m-event-title">BC350 アリストテレス</text>
    <text x="208" y="60" class="m-event-desc">四原因説・自動性</text>
    <text x="368" y="18" class="m-event-title">1265 トマス・アクィナス</text>
    <text x="368" y="32" class="m-event-desc">人工物の自然性</text>
    <text x="488" y="18" class="m-event-title">1620 Bacon 新オルガノン</text>
    <text x="488" y="32" class="m-event-desc">機械的世界観</text>
    <text x="488" y="46" class="m-event-title">1687 Newton プリンキピア</text>
    <text x="488" y="60" class="m-event-desc">力学の数学化</text>
    <text x="608" y="18" class="m-event-title">1854 Boole 論理代数</text>
    <text x="608" y="32" class="m-event-desc">記号論理</text>
    <text x="608" y="46" class="m-event-title">1889 Bergson</text>
    <text x="608" y="60" class="m-event-desc">機械 vs 生命の批判</text>
    <text x="748" y="18" class="m-event-title">1948 Wiener サイバネ</text>
    <text x="748" y="32" class="m-event-desc">制御・通信統合</text>
    <text x="748" y="46" class="m-event-title">1956 ダートマス AI</text>
    <text x="748" y="60" class="m-event-desc">人工知能の宣言</text>
    <text x="748" y="74" class="m-event-desc">1980s 認知科学・身体化</text>
    <text x="908" y="18" class="m-event-title">2010s 深層学習 / VLA</text>
    <text x="908" y="32" class="m-event-desc">身体性 AI の出現</text>
    <text x="908" y="46" class="m-event-title">2030+ 機械倫理学</text>
    <text x="908" y="60" class="m-event-desc">学術分野 確立</text>
    <text x="1038" y="18" class="m-event-title">2070+ 機械主観 哲学</text>
    <text x="1038" y="32" class="m-event-desc">経験論 拡張</text>
    <text x="1038" y="46" class="m-event-title">2100 惑星倫理 体系</text>
    <text x="1038" y="60" class="m-event-desc">人-機-自然 統合</text>
  </g>

  <!-- 行 6: 社会経済 -->
  <g transform="translate(0, 515)">
    <rect x="200" y="0" width="960" height="80" class="row-bg-even"/>
    <rect x="40" y="0" width="160" height="80" class="row-bg-even"/>
    <rect x="40" y="3" width="4" height="74" fill="#2E5E3E"/>
    <text x="190" y="22" class="m-row">社会経済</text>
    <text x="190" y="38" class="m-row-sub">Soc-Economy</text>
    <text x="190" y="56" class="m-row-sub">― 経済構造</text>

    <text x="208" y="18" class="m-event-title">BC3000 都市・労働分業</text>
    <text x="208" y="32" class="m-event-desc">職人カースト</text>
    <text x="208" y="46" class="m-event-title">BC500 貨幣・市場</text>
    <text x="208" y="60" class="m-event-desc">交換経済</text>
    <text x="368" y="18" class="m-event-title">1200 商業ギルド</text>
    <text x="368" y="32" class="m-event-desc">技能独占</text>
    <text x="488" y="18" class="m-event-title">1700 マニュファクチュア</text>
    <text x="488" y="32" class="m-event-desc">分業の組織化</text>
    <text x="608" y="18" class="m-event-title">1850 工場制度 確立</text>
    <text x="608" y="32" class="m-event-desc">資本-労働 分離</text>
    <text x="608" y="46" class="m-event-title">1880 テイラー主義</text>
    <text x="608" y="60" class="m-event-desc">科学的管理</text>
    <text x="748" y="18" class="m-event-title">1913 大量生産</text>
    <text x="748" y="32" class="m-event-desc">フォーディズム</text>
    <text x="748" y="46" class="m-event-title">1970s 情報経済</text>
    <text x="748" y="60" class="m-event-desc">サービス化</text>
    <text x="748" y="74" class="m-event-desc">1995 グローバル化</text>
    <text x="908" y="18" class="m-event-title">2010s ギグエコノミー</text>
    <text x="908" y="32" class="m-event-desc">プラットフォーム化</text>
    <text x="908" y="46" class="m-event-title">2035+ UBI 試行 拡大</text>
    <text x="908" y="60" class="m-event-desc">機械寄与 経済</text>
    <text x="1038" y="18" class="m-event-title">2060+ 労働 自発化</text>
    <text x="1038" y="32" class="m-event-desc">必須労働 = 機械</text>
    <text x="1038" y="46" class="m-event-title">2100 寄与経済 普遍</text>
    <text x="1038" y="60" class="m-event-desc">経済構造 再定義</text>
  </g>

  <!-- 行 7: メタ視点 -->
  <g transform="translate(0, 595)">
    <rect x="200" y="0" width="960" height="80" class="row-bg-odd"/>
    <rect x="40" y="0" width="160" height="80" class="row-bg-odd"/>
    <rect x="40" y="3" width="4" height="74" fill="#CC1400"/>
    <text x="190" y="22" class="m-row">メタ視点</text>
    <text x="190" y="38" class="m-row-sub">Meta-perspective</text>
    <text x="190" y="56" class="m-row-sub">― 5,100年俯瞰</text>

    <text x="208" y="18" class="m-event-title">道具 = 身体の延長</text>
    <text x="208" y="32" class="m-event-desc">力学的拡張の時代</text>
    <text x="208" y="46" class="m-event-title">機械 = 神聖／神秘</text>
    <text x="208" y="60" class="m-event-desc">職能の宗教化</text>
    <text x="368" y="18" class="m-event-title">機械 = 知の象徴</text>
    <text x="368" y="32" class="m-event-desc">時計仕掛けの宇宙観</text>
    <text x="488" y="18" class="m-event-title">機械 = 自然の模倣</text>
    <text x="488" y="32" class="m-event-desc">機械論的世界観</text>
    <text x="488" y="46" class="m-event-title">人 = 機械論</text>
    <text x="488" y="60" class="m-event-desc">心身二元論の挑戦</text>
    <text x="608" y="18" class="m-event-title">機械 = 生産手段</text>
    <text x="608" y="32" class="m-event-desc">資本主義の駆動軸</text>
    <text x="608" y="46" class="m-event-title">疎外 vs 解放 論争</text>
    <text x="608" y="60" class="m-event-desc">労働の意味 揺らぐ</text>
    <text x="748" y="18" class="m-event-title">機械 = 情報処理</text>
    <text x="748" y="32" class="m-event-desc">計算機モデルの人間観</text>
    <text x="748" y="46" class="m-event-title">機械 = 知能</text>
    <text x="748" y="60" class="m-event-desc">AI の概念出現</text>
    <text x="748" y="74" class="m-event-desc">機械 = 媒介者 (ネット)</text>
    <text x="908" y="18" class="m-event-title">機械 = 身体を持つ知能</text>
    <text x="908" y="32" class="m-event-desc">Physical AI 出現</text>
    <text x="908" y="46" class="m-event-title">機械 = パートナー</text>
    <text x="908" y="60" class="m-event-desc">関係の再定義</text>
    <text x="1038" y="18" class="m-event-title">機械 = 他者</text>
    <text x="1038" y="32" class="m-event-desc">主観/権利を持つ存在</text>
    <text x="1038" y="46" class="m-event-title">人 = 機械 = 自然</text>
    <text x="1038" y="60" class="m-event-desc">境界の融解・共存倫理</text>
  </g>

  <!-- 下罫 -->
  <line x1="40" y1="685" x2="1160" y2="685" class="grid" stroke="#121212" stroke-width="1.5"/>

  <!-- 時間軸（横） -->
  <line x1="40" y1="700" x2="1160" y2="700" stroke="#CC1400" stroke-width="2" class="accent"/>
  <circle cx="280" cy="700" r="3" fill="#CC1400" class="accent"/>
  <circle cx="420" cy="700" r="3" fill="#CC1400" class="accent"/>
  <circle cx="540" cy="700" r="3" fill="#CC1400" class="accent"/>
  <circle cx="670" cy="700" r="3" fill="#CC1400" class="accent"/>
  <circle cx="820" cy="700" r="3" fill="#CC1400" class="accent"/>
  <circle cx="900" cy="700" r="6" fill="#CC1400" class="accent"/>
  <circle cx="1160" cy="700" r="3" fill="#CC1400" class="accent"/>

  <text x="900" y="717" class="m-year" style="font-weight:600;fill:#CC1400">2026 現在</text>
  <text x="40" y="717" class="m-axis-label" text-anchor="start">← 5,100年前</text>
  <text x="1160" y="717" class="m-axis-label" text-anchor="end">74年後 →</text>

  <!-- 凡例・フッター -->
  <g transform="translate(40, 740)">
    <text x="0" y="0" class="m-sub">凡例</text>
    <rect x="40" y="-9" width="10" height="10" fill="#5A3E1F"/><text x="54" y="0" class="m-sub">道具・力学</text>
    <rect x="120" y="-9" width="10" height="10" fill="#3F1F5F"/><text x="134" y="0" class="m-sub">計算・情報</text>
    <rect x="200" y="-9" width="10" height="10" fill="#1F4E5F"/><text x="214" y="0" class="m-sub">自動人形</text>
    <rect x="276" y="-9" width="10" height="10" fill="#6E1F4A"/><text x="290" y="0" class="m-sub">思想</text>
    <rect x="334" y="-9" width="10" height="10" fill="#2E5E3E"/><text x="348" y="0" class="m-sub">社会経済</text>
    <rect x="402" y="-9" width="10" height="10" fill="#CC1400"/><text x="416" y="0" class="m-sub">人-機関係・メタ視点</text>
    <text x="1120" y="0" class="m-sub" text-anchor="end">D3-5 / 5,100年俯瞰</text>
  </g>
  <text x="40" y="775" class="m-sub">Note: 2026 現在は 5,100年の起点ではなく経過点。Physical AI は道具・自動人形・計算機・AIの 4 系譜が合流した瞬間。2100 までの 74 年は人類-機械関係の再定義期にあたる。</text>

  <!-- 下罫（最終） -->
  <line x1="40" y1="790" x2="1160" y2="790" class="grid" stroke="#121212" stroke-width="2"/>
</svg>
```

---

## 教科書 HTML 埋込み手順

1. 上記 5 SVG ブロックをそれぞれ章の該当箇所に直接埋め込む（外部ファイル不要）
2. ページ <head> に CSS ヒント（冒頭記載）を追加
3. ダークモード切替は既存 `[data-theme="dark"]` セレクタで自動動作
4. SVG はレスポンシブ前提（`viewBox` 指定により親要素幅に追随）
5. 印刷時は `.d3-tapestry-svg { page-break-inside: avoid; }` を別途付与

## 各図の役割整理

| ID | 図名 | viewBox | 役割 |
|----|------|---------|------|
| D3-1 | メインタペストリー | 1200×800 | Phase A-G 全体 × 12 行（系統 8 + 横断 4）一覧 |
| D3-2 | サブ A | 760×400 | 2026-2040 萌芽→実装期の詳細展開（3年刻み 5 列） |
| D3-3 | サブ B | 760×400 | 2040-2060 普及→統合期の詳細展開（4年刻み 5 列） |
| D3-4 | サブ C | 760×400 | 2060-2100 浸透→円熟→共存期の詳細展開（8年刻み 5 列） |
| D3-5 | メタタイムライン | 1200×800 | BC3000→2100 の人類-機械関係 5,100 年俯瞰 |
