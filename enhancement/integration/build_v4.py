#!/usr/bin/env python3
"""
Physical AI 2100 教科書 v4 統合スクリプト
原本 index.html + W1-W5 を結合して output/index_v4.html を生成
"""
import re
from pathlib import Path

ROOT = Path("/Users/nishimura+/projects/research/physical-ai-2100")
SRC = ROOT / "output" / "index.html"
INT = ROOT / "enhancement" / "integration"
OUT = ROOT / "output" / "index_v4.html"

def read(p): return Path(p).read_text(encoding="utf-8")

src = read(SRC)
w1 = read(INT / "chapter_w1.html")
w2 = read(INT / "chapter_w2.html")
w3 = read(INT / "chapter_w3.html")
w4 = read(INT / "chapter_w4.html")
w5 = read(INT / "appendix_w5.html")

# --- ヘルパ: id指定の <section class="chapter-section" id="XXX">...</section> を抽出 ---
def extract_section(html: str, section_id: str) -> str:
    """指定idのsectionを抽出。終了タグ </section> はネストを考慮しない（chapter-sectionはネストなし）"""
    pattern = re.compile(
        r'<section class="chapter-section" id="' + re.escape(section_id) + r'">.*?</section>',
        re.DOTALL,
    )
    m = pattern.search(html)
    if not m:
        raise ValueError(f"section id={section_id} not found")
    return m.group(0)

def extract_section_renamed(html: str, old_id: str, new_id: str) -> str:
    s = extract_section(html, old_id)
    return s.replace(
        f'<section class="chapter-section" id="{old_id}">',
        f'<section class="chapter-section" id="{new_id}">',
        1,
    )

# --- W1: prologue + ch0_5 + ch1 + ch2 + ch3 ---
sec_prologue = extract_section(w1, "prologue")
sec_ch0_5 = extract_section(w1, "ch0_5")
sec_ch1 = extract_section(w1, "ch1")
sec_ch2 = extract_section(w1, "ch2")
sec_ch3 = extract_section(w1, "ch3")

# --- W2: ch4 (Phase A) + ch5 (Phase A->B 連鎖, リネーム ch4b) + ch6 (Phase B, リネーム ch4c) ---
sec_ch4_a = extract_section(w2, "ch4")
sec_ch4_b = extract_section_renamed(w2, "ch5", "ch4b")
sec_ch4_c = extract_section_renamed(w2, "ch6", "ch4c")

# --- W3: W3 の章セクションを抽出 → 原本ch5 として配置 ---
# W3 のセクションIDを確認
w3_sec_ids = re.findall(r'<section class="chapter-section" id="([^"]+)"', w3)
# 取得した順に並べ、最初を ch5、以降を ch5b, ch5c ...
new_w3_sections = []
for i, sid in enumerate(w3_sec_ids):
    if i == 0:
        new_w3_sections.append(extract_section_renamed(w3, sid, "ch5"))
    else:
        new_w3_sections.append(extract_section_renamed(w3, sid, f"ch5_{i+1}"))

# W3 にセクションが0個の場合は W3 の <h1 class="chapter-title"> から </body> までの本文を ch5 ラッパで包む
if not w3_sec_ids:
    # W3 は <head> 含む完全HTML、本文は <body> 内 → <main class="book-main"> の中
    body_m = re.search(r"<main[^>]*>(.*?)</main>", w3, re.DOTALL)
    if body_m:
        inner = body_m.group(1)
        # 既存 chapter-section があれば抽出
        sec_matches = re.findall(
            r'<section class="chapter-section"[^>]*>.*?</section>', inner, re.DOTALL
        )
        if sec_matches:
            new_w3_sections = []
            for i, sec_html in enumerate(sec_matches):
                sid_m = re.search(r'id="([^"]+)"', sec_html)
                old_sid = sid_m.group(1) if sid_m else f"w3_{i}"
                new_id = "ch5" if i == 0 else f"ch5_{i+1}"
                sec_renamed = re.sub(
                    r'id="' + re.escape(old_sid) + r'"',
                    f'id="{new_id}"',
                    sec_html,
                    count=1,
                )
                new_w3_sections.append(sec_renamed)
        else:
            # fallback: 全body を ch5 として包む
            new_w3_sections = [
                f'<section class="chapter-section" id="ch5">\n{inner}\n</section>'
            ]
    else:
        # main がない場合、h1 chapter-title から末尾までを抽出
        h1_m = re.search(r'<h1 class="chapter-title".*', w3, re.DOTALL)
        if h1_m:
            new_w3_sections = [
                f'<section class="chapter-section" id="ch5">\n{h1_m.group(0)}\n</section>'
            ]
        else:
            new_w3_sections = [f'<section class="chapter-section" id="ch5">\n{w3}\n</section>']

# --- W4: ch6 (Phase E-G) + ch9 + ch10 + ch11 + epilogue ---
sec_ch6 = extract_section(w4, "ch6")
sec_ch9 = extract_section(w4, "ch9")
sec_ch10 = extract_section(w4, "ch10")
sec_ch11 = extract_section(w4, "ch11")
sec_epilogue = extract_section(w4, "epilogue")

# --- 原本 ch7, ch8 を保持 ---
sec_ch7 = extract_section(src, "ch7")
sec_ch8 = extract_section(src, "ch8")

# --- W5: 付録 A-E ---
sec_app_ardb = extract_section(w5, "appendix-ardb")
sec_app_people = extract_section(w5, "appendix-people")
sec_app_figures = extract_section(w5, "appendix-figures")
sec_app_glossary = extract_section(w5, "appendix-glossary")
sec_app_timeline = extract_section(w5, "appendix-timeline")

# --- W4 共通 <style> ブロック（SVG クラス定義）を抽出してmainに先行注入 ---
w4_style_m = re.search(r"<style>.*?</style>", w4, re.DOTALL)
w4_style = w4_style_m.group(0) if w4_style_m else ""

# W3 共通 <style> ブロック（SVG クラス定義）も同様に抽出
w3_style_m = re.search(r"<style>.*?</style>", w3, re.DOTALL)
w3_style = w3_style_m.group(0) if w3_style_m else ""

# --- 原本の <head>〜<body> 開始〜top-bar まで保持 ---
# 原本 行 1-109 が <head> + </head>, 110 = <body>, 111-116 = top-bar, 118-124 = book-cover, 127-164 = aside, 165 = <main>
# 元 book-cover を書き換え + 元 aside を書き換え

# 1) head 部分 (1-109) 保持: <body> 開始の前まで
head_end_idx = src.find("</head>")
head_section = src[: head_end_idx + len("</head>")]

# 2) <body> 開始〜top-bar 終了 を取り出す: top-bar の </div> 直後まで
body_start_idx = src.find("<body>")
top_bar_end_marker = '<div class="top-bar-actions">\n<button class="theme-toggle"'
# 簡易に top-bar を一気に取得
top_bar_match = re.search(r'<body>\s*<div class="top-bar">.*?</div>\s*</div>', src, re.DOTALL)
body_open_topbar = top_bar_match.group(0) if top_bar_match else "<body>"

# 3) 新 book-cover (meta 更新)
new_book_cover = '''
<section class="book-cover">
<div class="book-cover-tag">SPECIAL REPORT · PHYSICAL AI ROADMAP · 2026.05 · v4</div>
<h1 class="book-cover-title">フィジカルAIが拓く2100年<br><em>—</em> 知性が物質と出会う74年の道程</h1>
<p class="book-cover-subtitle">5系統合流から8系統オーケストラへ。<br>VLA基盤の定着から関係論的物理生態系へ向かう、74年の精緻なロードマップ。<br>v4 ブラッシュアップ版 — AR-DB 46DB + PHAI-DB + FTT-DB 41,070論文基盤の全面再編。</p>
<div class="book-cover-divider"></div>
<div class="book-cover-meta"><span>序+ch0.5+11章+終+付録 = 18章</span><span>·</span><span>約160,000字</span><span>·</span><span>図解55点</span><span>·</span><span>AR-DB 46DB + PHAI-DB + FTT-DB 41K論文基盤</span><span>·</span><span>30+並列チーム解析</span><span>·</span><span>v4 ブラッシュアップ版</span></div>
</section>
'''

# 4) 新 TOC sidebar
new_toc = '''
<div class="book-layout">
<aside class="toc-sidebar" aria-label="連載目次">
<div class="toc-title">目次</div>
<div class="toc-part">序</div>
<ul class="toc-list">
<li><a href="#prologue"><span class="toc-num">序</span>知性が物質に降りる夜明け</a></li>
<li><a href="#ch0_5"><span class="toc-num">序+</span>AR-DB が映すフィジカルAI 知識生態系</a></li>
</ul>
<div class="toc-part">第1部</div>
<div class="toc-part-title">5系統合流から8系統オーケストラへ</div>
<ul class="toc-list">
<li><a href="#ch1"><span class="toc-num">01</span>双子峰の高原とフィジカルAIの位置</a></li>
<li><a href="#ch2"><span class="toc-num">02</span>5系統合流の系譜と現在地</a></li>
<li><a href="#ch3"><span class="toc-num">03</span>8系統への拡張</a></li>
</ul>
<div class="toc-part">第2部</div>
<div class="toc-part-title">7フェーズ 74年ロードマップ</div>
<ul class="toc-list">
<li><a href="#ch4"><span class="toc-num">04</span>Phase A 2026-2030 — VLA基盤定着期</a></li>
<li><a href="#ch4b"><span class="toc-num">04+</span>Phase A→B 連鎖と移行論</a></li>
<li><a href="#ch4c"><span class="toc-num">04++</span>Phase B 2030-2040 — 物理操作汎化期</a></li>
<li><a href="#ch5"><span class="toc-num">05</span>Phase C-D 2040-2060 — 人間-機械並走から自律物理エージェントへ</a></li>
<li><a href="#ch6"><span class="toc-num">06</span>Phase E-G 2060-2100 — 知性のオーケストラから関係論的物理生態系へ</a></li>
</ul>
<div class="toc-part">第3部</div>
<div class="toc-part-title">領域別波及と社会構造</div>
<ul class="toc-list">
<li><a href="#ch7"><span class="toc-num">07</span>製造・医療・農業 — 三領域の波及解析</a></li>
<li><a href="#ch8"><span class="toc-num">08</span>都市・宇宙・教育 — 三領域の波及解析</a></li>
</ul>
<div class="toc-part">第4部</div>
<div class="toc-part-title">情景 × 能力地図 × 補論 × 終</div>
<ul class="toc-list">
<li><a href="#ch9"><span class="toc-num">09</span>2050年の朝シーン — 共生する物理AI</a></li>
<li><a href="#ch10"><span class="toc-num">10</span>能力の譜面 — 8系統の対等駆動マップ</a></li>
<li><a href="#ch11"><span class="toc-num">11</span>FVCP補論 — 5不確実性と政策設計</a></li>
<li><a href="#epilogue"><span class="toc-num">終</span>物質が思考し始める時代へ</a></li>
</ul>
<div class="toc-part">付録</div>
<div class="toc-part-title">参照系譜・人物・図解・概念・年表</div>
<ul class="toc-list">
<li><a href="#appendix-ardb"><span class="toc-num">A</span>AR-DB 参照系譜</a></li>
<li><a href="#appendix-people"><span class="toc-num">B</span>100人物プロファイル抄</a></li>
<li><a href="#appendix-figures"><span class="toc-num">C</span>図解インデックス全40図</a></li>
<li><a href="#appendix-glossary"><span class="toc-num">D</span>キー概念集50語</a></li>
<li><a href="#appendix-timeline"><span class="toc-num">E</span>主要事実年表 2017-2026</a></li>
</ul>
</aside>
'''

# 5) footer + script を原本から抽出
footer_m = re.search(r'<footer style="margin-top:80px.*?</body>\s*</html>', src, re.DOTALL)
if footer_m:
    footer_and_close = footer_m.group(0)
else:
    # フォールバック: </main> 以降全部
    main_end_idx = src.rfind("</main>")
    footer_and_close = src[main_end_idx + len("</main>"):]

# --- 組み立て ---
parts = [
    head_section,
    "\n",
    body_open_topbar,
    "\n",
    # W3/W4 の共通 SVG style を <body> 内先頭に追加（CSS変数 svg-* を有効化）
    w3_style if w3_style else "",
    "\n",
    w4_style if w4_style else "",
    "\n",
    new_book_cover,
    new_toc,
    '<main class="book-main">\n',
    # 序 + ch0.5
    sec_prologue, "\n\n",
    sec_ch0_5, "\n\n",
    # 第1部
    sec_ch1, "\n\n",
    sec_ch2, "\n\n",
    sec_ch3, "\n\n",
    # 第2部 (Phase A-B from W2)
    sec_ch4_a, "\n\n",
    sec_ch4_b, "\n\n",
    sec_ch4_c, "\n\n",
    # Phase C-D from W3
    "\n\n".join(new_w3_sections), "\n\n",
    # Phase E-G from W4
    sec_ch6, "\n\n",
    # 第3部 (原本保持)
    sec_ch7, "\n\n",
    sec_ch8, "\n\n",
    # 第4部 (from W4)
    sec_ch9, "\n\n",
    sec_ch10, "\n\n",
    sec_ch11, "\n\n",
    sec_epilogue, "\n\n",
    # 付録 (from W5)
    sec_app_ardb, "\n\n",
    sec_app_people, "\n\n",
    sec_app_figures, "\n\n",
    sec_app_glossary, "\n\n",
    sec_app_timeline, "\n\n",
    "</main>\n",
    "</div>\n",  # close book-layout
    footer_and_close,
]

result = "".join(parts)

# 検証
chapter_sections = re.findall(r'<section class="chapter-section" id="([^"]+)"', result)
print(f"Chapter sections found: {len(chapter_sections)}")
print(f"Section IDs: {chapter_sections}")

# 重複検査
from collections import Counter
dup = [k for k, v in Counter(chapter_sections).items() if v > 1]
if dup:
    print(f"WARNING: duplicate IDs: {dup}")
else:
    print("All section IDs unique.")

# SVG カウント
svg_count = len(re.findall(r'<svg ', result))
print(f"SVG count: {svg_count}")

# 文字数 (body内テキスト推定): タグ除去後の文字数
text_only = re.sub(r"<script.*?</script>", "", result, flags=re.DOTALL)
text_only = re.sub(r"<style.*?</style>", "", text_only, flags=re.DOTALL)
text_only = re.sub(r"<[^>]+>", "", text_only)
text_only = re.sub(r"\s+", "", text_only)
print(f"Body text approx chars: {len(text_only)}")

# 出力
OUT.write_text(result, encoding="utf-8")
size_kb = OUT.stat().st_size / 1024
print(f"\nOutput: {OUT}")
print(f"File size: {size_kb:.1f} KB")
