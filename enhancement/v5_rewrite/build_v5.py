#!/usr/bin/env python3
"""Assemble v5 HTML from v4 base + 6 rewrite fragments."""
import re
from pathlib import Path

BASE = Path.home() / "projects/research/physical-ai-2100"
V4 = BASE / "output/index.html"
V5 = BASE / "output/index_v5.html"
RW = BASE / "enhancement/v5_rewrite"

v4 = V4.read_text()
overview = (RW / "overview.html").read_text().strip()
w1 = (RW / "w1.html").read_text().strip()
w2 = (RW / "w2.html").read_text().strip()
w3 = (RW / "w3.html").read_text().strip()
w4 = (RW / "w4.html").read_text().strip()
w5 = (RW / "w5_appendix.html").read_text().strip()

# === Step 1: Extract head/body-start/cover/main-end-and-footer from v4 ===
# Find <main class="book-main"> start and </main> end
main_start = v4.index('<main class="book-main">')
main_end = v4.index('</main>')

header = v4[:main_start]  # everything before <main>, including TOC sidebar
footer = v4[main_end:]    # </main> + footer + scripts

# === Step 2: Update book-cover meta to v5 ===
# Find book-cover-meta and replace
new_cover_meta = (
    '<div class="book-cover-meta">'
    '<span>概観+序+11章+終+付録 = 19章</span><span>·</span>'
    '<span>約170,000字</span><span>·</span>'
    '<span>図解35点</span><span>·</span>'
    '<span>主要研究機関の動向 / 学術論文集積 / 政府統計</span><span>·</span>'
    '<span>v5 平易化版</span>'
    '</div>'
)
header = re.sub(
    r'<div class="book-cover-meta">.*?</div>',
    new_cover_meta,
    header,
    count=1,
    flags=re.DOTALL,
)

# === Step 3: Rebuild TOC sidebar ===
new_toc = """<aside class="toc-sidebar" aria-label="連載目次">
<div class="toc-title">目次</div>
<div class="toc-part">概観</div>
<ul class="toc-list">
<li><a href="#overview"><span class="toc-num">概</span>知性が物質に降りる74年の輪郭</a></li>
</ul>
<div class="toc-part">序</div>
<ul class="toc-list">
<li><a href="#prologue"><span class="toc-num">序</span>知性が物質に降りる夜明け</a></li>
</ul>
<div class="toc-part">第1部</div>
<div class="toc-part-title">5系統合流から8系統オーケストラへ</div>
<ul class="toc-list">
<li><a href="#ch1"><span class="toc-num">01</span>双子峰の高原とフィジカルAIの位置</a></li>
<li><a href="#ch2"><span class="toc-num">02</span>5系統合流の系譜と現在地</a></li>
<li><a href="#ch3"><span class="toc-num">03</span>8系統への拡張</a></li>
</ul>
<div class="toc-part">第2部</div>
<div class="toc-part-title">7フェーズロードマップ 2026-2100</div>
<ul class="toc-list">
<li><a href="#ch4"><span class="toc-num">04</span>フェーズA-B：視覚言語行動モデル基盤定着〜物理操作汎化</a></li>
<li><a href="#ch5"><span class="toc-num">05</span>フェーズC-D：人間-機械並走〜自律物理エージェント</a></li>
<li><a href="#ch6"><span class="toc-num">06</span>フェーズE-G：知性のオーケストラ〜関係論的物理生態系</a></li>
</ul>
<div class="toc-part">第3部</div>
<div class="toc-part-title">6波及分野での未来社会</div>
<ul class="toc-list">
<li><a href="#ch7"><span class="toc-num">07</span>製造・医療・農業の組み換え</a></li>
<li><a href="#ch8"><span class="toc-num">08</span>都市・宇宙・教育の組み換え</a></li>
<li><a href="#ch9"><span class="toc-num">09</span>4時点の高解像度社会像</a></li>
</ul>
<div class="toc-part">第4部</div>
<div class="toc-part-title">統合と展望</div>
<ul class="toc-list">
<li><a href="#ch10"><span class="toc-num">10</span>譜面を書く者の作法</a></li>
<li><a href="#ch11"><span class="toc-num">11</span>未来洞察補論シリーズへの位置づけ</a></li>
</ul>
<div class="toc-part">終</div>
<ul class="toc-list">
<li><a href="#epilogue"><span class="toc-num">終</span>譜面を書く者と、譜面を奏でる物質</a></li>
</ul>
<div class="toc-part">付録</div>
<div class="toc-part-title">人物・図解・概念・年表</div>
<ul class="toc-list">
<li><a href="#appendix-people"><span class="toc-num">A</span>100人物プロファイル抄</a></li>
<li><a href="#appendix-figures"><span class="toc-num">B</span>図解インデックス全35図</a></li>
<li><a href="#appendix-glossary"><span class="toc-num">C</span>キー概念集50語</a></li>
<li><a href="#appendix-timeline"><span class="toc-num">D</span>主要事実年表 2017-2026</a></li>
</ul>
</aside>"""

# Replace existing TOC
header = re.sub(
    r'<aside class="toc-sidebar"[^>]*>.*?</aside>',
    new_toc,
    header,
    count=1,
    flags=re.DOTALL,
)

# === Step 4: Assemble final HTML ===
parts = [
    header,
    '<main class="book-main">\n',
    overview,
    '\n\n',
    w1,
    '\n\n',
    w2,
    '\n\n',
    w3,
    '\n\n',
    w4,
    '\n\n',
    w5,
    '\n\n',
    footer.replace('</main>', '', 0),  # footer starts with </main>, keep as-is since we open main above
]

# Actually footer starts with `</main>` — we need to keep that
# Re-check: footer = v4[main_end:]  where main_end is index of '</main>'
# So footer already starts with '</main>'. Good.
# Re-assemble correctly:
final = (
    header
    + '<main class="book-main">\n'
    + overview + '\n\n'
    + w1 + '\n\n'
    + w2 + '\n\n'
    + w3 + '\n\n'
    + w4 + '\n\n'
    + w5 + '\n\n'
    + footer
)

V5.write_text(final)

# === Stats ===
total_chars = len(final)
text_only = re.sub(r'<svg.*?</svg>', '', final, flags=re.DOTALL)
text_only = re.sub(r'<style.*?</style>', '', text_only, flags=re.DOTALL)
text_only = re.sub(r'<script.*?</script>', '', text_only, flags=re.DOTALL)
text_only = re.sub(r'<[^>]+>', '', text_only)
text_only = re.sub(r'\s+', '', text_only)
ascii_letters = len(re.findall(r'[A-Za-z]', text_only))
sections = len(re.findall(r'<section class="chapter-section" id="([^"]+)"', final))
ids = re.findall(r'<section class="chapter-section" id="([^"]+)"', final)
svgs = final.count('<svg ') + final.count('<svg\n')

print(f"v5 HTML written: {V5}")
print(f"  Total HTML: {total_chars:,} chars")
print(f"  Body text approx: {len(text_only):,} chars")
print(f"  Sections: {sections}")
print(f"  Section IDs: {ids}")
print(f"  SVG count: {svgs}")
print(f"  ASCII letters in body: {ascii_letters:,}")

# Check for duplicate IDs
from collections import Counter
dupes = [k for k, v in Counter(ids).items() if v > 1]
print(f"  Duplicate IDs: {dupes if dupes else 'none'}")
# Check TOC anchors
toc_anchors = re.findall(r'href="#([^"]+)"', new_toc)
missing = [a for a in toc_anchors if a not in ids]
print(f"  TOC missing targets: {missing if missing else 'none'}")
