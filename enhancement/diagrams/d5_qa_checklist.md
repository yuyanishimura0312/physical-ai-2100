# D5 統一性検証チェックリスト ── 既存20 SVG + 新規5 SVG = 25 SVG

Physical AI 2100 教科書ブラッシュアップ時点の全 SVG を、配色・フォント・ダークモード・viewBox・凡例配置・アクセシビリティの 6 観点で査読。

## 対象 SVG 一覧（25 図）

| 区分 | ファイル | 図数 | 主要 viewBox |
|------|---------|------|-------------|
| 既存 | `output/index.html` | 15 | 680×360〜400 / 760×320〜380 |
| 既存 | `output/chapters/part1_ch1-3.html` | 3 | 680×360〜380 |
| 既存 | `output/chapters/part2_ch4-6.html` | 6 | 680系 中心 |
| 既存 | `output/chapters/part3_ch7-8.html` | 2 | 680系 中心 |
| 既存 | `output/chapters/part4_ch9-10_epilogue.html` | 1 | 680系 |
| 新規 | `enhancement/diagrams/d5_infographics.md` (D5-1〜D5-5) | 5 | 680×400 / 760×360〜400 |
|  | **合計** | **32 図 (うち既存重複あり、独立図 ~25)** | |

> 注: `output/index.html` と各章ファイルの間で同一 SVG が重複している箇所が存在する。書籍ビルド側で重複統合する場合は別タスク。

## 検証マトリクス

### 1. 配色一貫性

| チェック項目 | 基準 | 既存20図 | 新規5図 (D5-1〜D5-5) | 判定 |
|-------------|------|----------|---------------------|------|
| 主軸線 | `#121212` | OK 全図 | OK 全図 | **PASS** |
| 赤白CIアクセント | `#CC1400` | OK 全図 | OK 全図 | **PASS** |
| ラベル | `#555` | OK 全図 | OK 全図 | **PASS** |
| 注釈 | `#6B6B6B` | OK 全図 | OK 全図 | **PASS** |
| 補助グレー | `#999` | OK 大半 | OK 全図 | **PASS** |
| 背景tint | `rgba(204,20,0,0.02)` (figure wrapping) | OK 大半 | OK 全図 | **PASS** |
| 不要な追加色 | なし (青/緑/紫 禁止) | OK 全図 | OK 全図 | **PASS** |

### 2. フォント統一

| チェック項目 | 基準 | 既存 | 新規 | 判定 |
|-------------|------|------|------|------|
| SVG内 font-family | `Noto Sans JP, sans-serif` | OK 全図 | OK 全図 | **PASS** |
| Serif との混在 | なし（本文側 Serif、SVG ラベルは Sans） | OK | OK | **PASS** |
| font-size レンジ | 9〜14 (見出し 13-14 / ラベル 10-11 / 注釈 9-10) | OK | OK | **PASS** |
| font-weight | 通常 normal、強調 700 のみ | OK | OK | **PASS** |
| font-style italic | 注釈・年代に限定 | OK | OK | **PASS** |

### 3. ダークモード網羅

| チェック項目 | 基準 | 既存20図 | 新規5図 | 判定 |
|-------------|------|----------|---------|------|
| SVG内 hardcode 色の自動反転 | 教科書側CSS `[data-theme="dark"] figure svg [stroke="#121212"]` 等で対応 | **未整備** (要追加) | 同 | **WARN** |
| 赤の二段階 (#CC1400→#FF4030) | CSS変数で再マップ | 未整備 | 未整備 | **WARN** |
| figure 背景 `rgba(204,20,0,0.02)` のダーク時可視性 | 透過度低いため両モード可 | OK | OK | **PASS** |
| ダーク時 text fill `#555` の視認性 | `#555` は背景 `#121212` で AA 不合格 (3.0:1) | **FAIL** 全図 | **FAIL** 全図 | **FAIL** |

**推奨対応** (チェックリスト D4 失敗への処置):
教科書側 CSS に下記を追加し全 25 SVG を一括対応:

```css
[data-theme="dark"] figure svg [fill="#555"],
[data-theme="dark"] figure svg [fill="#6B6B6B"] { fill: #AAAAAA; }
[data-theme="dark"] figure svg [fill="#999"] { fill: #888888; }
[data-theme="dark"] figure svg [stroke="#121212"] { stroke: #E0E0E0; }
[data-theme="dark"] figure svg [fill="#121212"] { fill: #E0E0E0; }
[data-theme="dark"] figure svg [stroke="#CC1400"] { stroke: #FF4030; }
[data-theme="dark"] figure svg [fill="#CC1400"] { fill: #FF4030; }
[data-theme="dark"] figure svg [fill="#F7F7F5"] { fill: #1A1A1A; }
[data-theme="dark"] figure svg [stroke="#D9D9D9"] { stroke: #333333; }
[data-theme="dark"] figure svg [stroke="#999"] { stroke: #666666; }
```

### 4. viewBox 統一

| viewBox パターン | 用途 | 既存 | 新規 | 統一性 |
|-----------------|------|------|------|--------|
| `0 0 680 360` | 標準折れ線 | 主流 | D5-3 で採用 | **PASS** |
| `0 0 680 380` | 中段密度 | 多用 | - | **PASS** |
| `0 0 680 400` | 縦長密度 | 一部 | D5-3 | **PASS** |
| `0 0 760 320〜400` | 横長 (比較表/タイムライン/年表) | 一部 | D5-1/2/4/5 | **PASS** |
| 異常値 (上記外) | なし | - | - | **PASS** |
| `style="width:100%;max-width:680px;height:auto;"` | レスポンシブ統一 | OK | OK | **PASS** |

### 5. 凡例配置

| チェック項目 | 基準 | 既存 | 新規 | 判定 |
|-------------|------|------|------|------|
| `<figcaption>` 必須 | figure 内 SVG 直下 | OK 全図 | OK 全図 | **PASS** |
| figcaption style | `font-family:var(--font);font-size:0.78rem;color:#6B6B6B;margin-top:12px;text-align:center;` | OK | OK | **PASS** |
| 図番号 | 図 N-M または 図 D5-N | OK | OK | **PASS** |
| 軸ラベル位置 | 横軸=下中央、縦軸=左90度回転 | OK 大半 | OK 全図 | **PASS** |
| 凡例の色対応 | 図内テキスト色 = 線色と一致 | OK | OK | **PASS** |

### 6. アクセシビリティ (alt/title/desc)

| チェック項目 | 基準 | 既存20図 | 新規5図 | 判定 |
|-------------|------|----------|---------|------|
| `<svg role="img">` | 必須 | 0/20 | 5/5 | **要改修** |
| `<title>` 子要素 | 必須 | 0/20 | 5/5 | **要改修** |
| `<desc>` 子要素 | 推奨 | 0/20 | 5/5 | **要改修** |
| `aria-labelledby` で title/desc 紐付け | 必須 | 0/20 | 5/5 | **要改修** |
| 色のみで意味を伝えない | パス種別・ラベル併記 | OK 大半 | OK 全図 | **PASS** |
| キーボード操作 | SVG は装飾扱い (本文に説明あり) | OK | OK | **PASS** |

**推奨対応** (既存20図にも順次注入):

各 `<svg>` を以下のテンプレートで包む（最小コスト改修）:

```html
<svg viewBox="..." xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="fig-NN-title fig-NN-desc" style="...">
  <title id="fig-NN-title">図NN-MM のタイトル</title>
  <desc id="fig-NN-desc">図の内容を1-2文で説明</desc>
  <!-- 既存 SVG コンテンツ -->
</svg>
```

スクリプト一括変換例 (Python):

```python
# 既存20 SVG への title/desc 一括注入スクリプト雛形
import re, pathlib
fig_id = 0
for html in pathlib.Path("output").rglob("*.html"):
    text = html.read_text(encoding="utf-8")
    def inject(m):
        global fig_id
        fig_id += 1
        return (m.group(0).rstrip(">")
            + f' role="img" aria-labelledby="fig-{fig_id}-title fig-{fig_id}-desc">'
            + f'\n<title id="fig-{fig_id}-title">図 {fig_id}</title>'
            + f'\n<desc id="fig-{fig_id}-desc">(要記述)</desc>')
    text = re.sub(r'<svg viewBox="[^"]+" xmlns="[^"]+"(?: style="[^"]*")?>', inject, text)
    html.write_text(text, encoding="utf-8")
```

## 総合判定

| 観点 | スコア | コメント |
|------|--------|---------|
| 1. 配色一貫性 | **PASS (10/10)** | 25図ともに #121212/#CC1400/#555 軸で完全統一 |
| 2. フォント統一 | **PASS (10/10)** | Noto Sans JP のみ。サイズレンジも適正 |
| 3. ダークモード網羅 | **FAIL → 要CSS追加 (4/10)** | SVG内hardcode色がダーク時に視認性低下。教科書側CSS追加で一括解決可 |
| 4. viewBox 統一 | **PASS (10/10)** | 4パターン (680×360/380/400 + 760×320〜400) のみ。一貫 |
| 5. 凡例配置 | **PASS (10/10)** | figcaption・軸ラベル・色対応すべて整合 |
| 6. アクセシビリティ | **FAIL → 要既存20図改修 (5/10)** | 新規5図はOK、既存20図は title/desc/role 全欠落 |

**総合: 49/60 (81.7%)**

## 優先改修アクション

| 優先度 | アクション | 工数 | 影響範囲 |
|--------|-----------|------|---------|
| **HIGH** | 教科書側 style ブロックに `[data-theme="dark"]` SVG 色マッピング 10行追加 | 0.1 FDD | 全 25 図 一括対応 |
| **HIGH** | 既存20図に `role/title/desc` 注入スクリプト実行 | 0.5 FDD | アクセシビリティ即時改善 |
| MED | 各 `<desc>` の内容を図ごとに具体記述 (手動) | 1.0 FDD | スクリーンリーダー有効化 |
| LOW | 重複SVG (index.html ↔ chapters/*) の統合検討 | 0.5 FDD | ファイルサイズ削減 |

## 履歴

- 2026-05-18 初版策定。Physical AI 2100 教科書ブラッシュアップ D5図解設計隊として、既存20+新規5=25 SVGを6観点で査読。配色・フォント・viewBox・凡例は全PASS。ダークモードとアクセシビリティに改修必要箇所を特定し、解決パッチを提示。
