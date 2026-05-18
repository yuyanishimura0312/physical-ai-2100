#!/usr/bin/env python3
"""Build w4 remainder (ch7-epilogue) by extracting from v4 HTML and applying v5 rules:
1. Alphabet -> Japanese for company/institution/model names
2. Remove DB self-references
3. Keep SVG diagrams, japanize text labels where possible
"""
import re
from pathlib import Path

V4 = Path.home() / "projects/research/physical-ai-2100/output/index.html"
W4_PARTIAL = Path.home() / "projects/research/physical-ai-2100/enhancement/v5_rewrite/w4.html"
W4_OUT = Path.home() / "projects/research/physical-ai-2100/enhancement/v5_rewrite/w4.html"

v4 = V4.read_text()
lines = v4.split("\n")

# Extract ch7 through epilogue (lines 2170..3281)
def extract(start, end):
    """1-indexed line numbers inclusive."""
    return "\n".join(lines[start-1:end])

ch7 = extract(2170, 2332)
ch8 = extract(2333, 2438)
ch9 = extract(2439, 2655)
ch10 = extract(2656, 2861)
ch11 = extract(2862, 3016)
epilogue = extract(3017, 3281)

# ================ Substitution rules ================
SUBS = [
    # Core terminology
    (r'\bPhysical AI\b', 'フィジカルAI'),
    (r'\bphysical AI\b', 'フィジカルAI'),
    (r'\bAGI\b', '汎用人工知能'),
    (r'\bAGI:', '汎用人工知能:'),
    # Companies / institutions
    (r'\bWaymo\b', '米ウェイモ'),
    (r'\bPony\.ai\b', '中国ポニーAI'),
    (r'\bCruise\b', '米クルーズ'),
    (r'\bTesla\b', '米テスラ'),
    (r'\bJAXA\b', '宇宙航空研究開発機構'),
    (r'\bNASA\b', '米航空宇宙局'),
    (r'\bSpaceX\b', '米スペースX'),
    (r'\bIFR\b', '国際ロボット連盟'),
    (r'Goldman Sachs', '米ゴールドマン・サックス'),
    (r'McKinsey', '米マッキンゼー'),
    (r'WEF', '世界経済フォーラム'),
    (r'\bOECD\b', '経済協力開発機構'),
    (r'\bILO\b', '国際労働機関'),
    (r'\bWHO\b', '世界保健機関'),
    # Product / model names
    (r'Cyberdyne HAL', 'サイバーダイン社 補助スーツ'),
    (r'Toyota HSR', 'トヨタ 家庭支援ロボット'),
    (r'da Vinci 5', 'インテュイティブ社 ダ・ヴィンチ第5世代'),
    (r'da Vinci', 'インテュイティブ社 ダ・ヴィンチ'),
    (r'\bHugo\b', 'メドトロニック社 ヒューゴ'),
    (r'\bOttava\b', 'ジョンソン・エンド・ジョンソン社 オッタヴァ'),
    (r'Agility Digit', 'アジリティ社 ディジット'),
    (r'Apptronik Apollo', 'アプトロニク社 アポロ'),
    (r'Joby Aviation', '米ジョビー'),
    (r'Archer Aviation', '米アーチャー'),
    (r'\bEHang\b', '中国 EHang'),
    (r'\bICON\b', '米アイコン社'),
    (r'Autodesk Forma', 'オートデスク社 フォルマ'),
    (r'Project PLATEAU', '国土交通省 プラトー計画'),
    (r'Virtual Singapore', '仮想シンガポール基盤'),
    (r'Apollo Go', 'アポロ・ゴー'),
    (r'WeRide', '中国ウィーライド'),
    # Cultural / mythological
    (r'\bFrankenstein\b', 'フランケンシュタイン'),
    (r'\bGolem\b', 'ゴーレム'),
    (r'\bTalos\b', 'ギリシャ神話タロス'),
    (r'R\.U\.R\.', 'ロッスム万能ロボット会社'),
    (r'Ghost in Shell', '攻殻機動隊'),
    # SDG terms
    (r'SDG ?17', '持続可能な開発目標17項'),
    (r'\bSDGs?\b', '持続可能な開発目標'),
    # Foundation terms used in text
    (r'\bDOI:\s*[\d./]+', ''),
    (r'arXiv:\s*[\d.]+', ''),
    (r'https?://[^\s<>"]+', ''),
    # AI generic
    (r'\bAI\b(?![A-Za-z])', '人工知能'),
]

# DB self-reference removal patterns
DB_PATTERNS = [
    r'AR-DB[^。、）]*?(?=[。、）])',
    r'FTT-DB[^。、）]*?(?=[。、）])',
    r'PHAI-DB[^。、）]*?(?=[。、）])',
    r'signal-db[^。、）]*?(?=[。、）])',
    r'cla-db[^。、）]*?(?=[。、）])',
    r'mor-db[^。、）]*?(?=[。、）])',
    r'cti-db[^。、）]*?(?=[。、）])',
    r'innovation-db[^。、）]*?(?=[。、）])',
    r'pestle-db[^。、）]*?(?=[。、）])',
    r'gc-db[^。、）]*?(?=[。、）])',
    r'kgh-db[^。、）]*?(?=[。、）])',
    r'ftt_v2[^。、）]*?(?=[。、）])',
    r'_evidence\.md',
    r'codex_[a-z_]+\.md',
    r'mapping_report\.md',
    r'content_audit\.md',
]

def rewrite(html):
    out = html
    # Apply main substitutions
    for pat, repl in SUBS:
        out = re.sub(pat, repl, out)
    # Strip DB self-references
    for pat in DB_PATTERNS:
        out = re.sub(pat, '', out, flags=re.IGNORECASE)
    # Remove "DB Evidence" finding-boxes (search for finding-box that contains DB names)
    # Pattern: <div class="finding-box">...</div> blocks containing "Evidence" or "DB"
    def remove_db_box(match):
        content = match.group(0)
        if 'Evidence' in content or 'AR-DB' in content or 'FTT-DB' in content or 'PHAI-DB' in content:
            return ''
        return content
    out = re.sub(r'<div class="finding-box"[^>]*>.*?</div>', remove_db_box, out, flags=re.DOTALL)
    # Cleanup: empty parens, doubled punctuation
    out = re.sub(r'（\s*）', '', out)
    out = re.sub(r'\(\s*\)', '', out)
    out = re.sub(r'、\s*、', '、', out)
    out = re.sub(r'。\s*。', '。', out)
    out = re.sub(r'  +', ' ', out)
    return out

ch7_v5 = rewrite(ch7)
ch8_v5 = rewrite(ch8)
ch9_v5 = rewrite(ch9)
ch10_v5 = rewrite(ch10)
ch11_v5 = rewrite(ch11)
ep_v5 = rewrite(epilogue)

# Read existing w4 partial (ch6 only)
ch6_partial = W4_PARTIAL.read_text()

# Combine all
combined = "\n\n".join([ch6_partial.strip(), ch7_v5, ch8_v5, ch9_v5, ch10_v5, ch11_v5, ep_v5])

W4_OUT.write_text(combined)

# Stats
total = len(combined)
text_only = re.sub(r'<[^>]+>', '', combined)
text_only = re.sub(r'\s+', '', text_only)
print(f"w4.html written: {W4_OUT}")
print(f"  Total HTML: {total:,} chars")
print(f"  Body text (CJK+alphanum): {len(text_only):,} chars")
print(f"  Sections combined: ch6 + ch7 + ch8 + ch9 + ch10 + ch11 + epilogue")
# Count remaining DB references
remaining_db = sum(len(re.findall(p, combined, re.IGNORECASE)) for p in DB_PATTERNS)
print(f"  Remaining DB self-references: {remaining_db}")
# Count alphabet
ascii_letters = len(re.findall(r'[A-Za-z]', text_only))
print(f"  ASCII letters in body: {ascii_letters:,}")
