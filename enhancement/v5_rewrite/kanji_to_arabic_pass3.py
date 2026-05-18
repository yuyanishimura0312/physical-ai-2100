#!/usr/bin/env python3
"""Third pass: fix missed cases (mid-万 numbers, 期, 段, etc.)"""
import re
from pathlib import Path

POS = {'〇':'0','一':'1','二':'2','三':'3','四':'4','五':'5','六':'6','七':'7','八':'8','九':'9'}

def parse_kanji_number(s: str) -> str:
    if not s: return s
    if all(c in POS for c in s):
        return ''.join(POS[c] for c in s)
    units = {'十':10,'百':100,'千':1000}
    big_units = {'万':10000,'億':100000000,'兆':1000000000000}
    n = 0; section = 0; digit = 0
    for c in s:
        if c in POS:
            digit = digit*10 + int(POS[c])
        elif c in units:
            if digit == 0: digit = 1
            section += digit * units[c]
            digit = 0
        elif c in big_units:
            section += digit
            n += section * big_units[c]
            section = 0; digit = 0
    section += digit
    n += section
    return str(n)

def convert(text):
    # Fix Arabic + 万 + kanji-number-string (e.g., "1万六千ドル" → "16,000ドル" or "1万6,000ドル")
    # Approach: convert "1万六千" → "16000" using full parse
    def fix_arabic_kanji_num(m):
        arabic = int(m.group(1))
        kanji_part = m.group(2)
        # Build full number: Arabic * 10000 + kanji_part_parsed
        try:
            kanji_n = int(parse_kanji_number(kanji_part))
            total = arabic * 10000 + kanji_n
            return f'{total:,}'
        except:
            return m.group()
    text = re.sub(r'(\d+)万([〇一二三四五六七八九十百千]+)', fix_arabic_kanji_num, text)

    # Plain "N万" with no following kanji digit — just "1万" → "10,000" or keep as "1万"?
    # User wants Arabic, but 1万 is a common mixed style. Let's keep "1万" as-is in normal context.
    # However "1万人" "1万台" etc are acceptable

    # Convert N期 (counter 期 for time periods)
    text = re.sub(r'([〇一二三四五六七八九十百千万億]+)期(?![一-龥])',
                  lambda m: parse_kanji_number(m.group(1)) + '期', text)

    # Convert N基 (counter for foundations/bases when standalone)
    text = re.sub(r'(?<![一-龥])([〇一二三四五六七八九十百千]+)基(?![一-龥])',
                  lambda m: parse_kanji_number(m.group(1)) + '基', text)

    # Convert 段 when not in 段階 (already handled) — explicit retry without idiom blocking
    text = re.sub(r'([〇一二三四五六七八九十百千万億]+)段(?![階一-龥])',
                  lambda m: parse_kanji_number(m.group(1)) + '段', text)

    # Convert N足 (歩行用語) — 二足/四足 → 2足/4足
    text = re.sub(r'([二四六八十])足(?!跡)',
                  lambda m: POS.get(m.group(1), parse_kanji_number(m.group(1))) + '足', text)

    # Convert 三百/二百/etc + counter or standalone-before-non-kanji
    text = re.sub(r'(?<![一-龥])([〇一二三四五六七八九])(百|千)(?![一-龥])',
                  lambda m: parse_kanji_number(m.group(1) + m.group(2)), text)

    # Convert "数十N" "数百N" "数千N" — keep as-is (これは「数」+kanji number)

    # Convert 第十二 etc. (再パス)
    text = re.sub(r'第([十百千]?[〇一二三四五六七八九十百千]+)',
                  lambda m: '第' + parse_kanji_number(m.group(1)), text)

    # 十二 standalone before noun: e.g., "十二の能力" → "12の能力", "十二ナノメートル" → "12ナノメートル"
    text = re.sub(r'(?<![一-龥])十([〇一二三四五六七八九])(?=[のな一-龥0-9])',
                  lambda m: '1' + POS[m.group(1)], text)
    text = re.sub(r'(?<![一-龥])十(?=[のナ一-龥])',
                  '10', text)

    # 二十以 → 20以
    text = re.sub(r'([〇一二三四五六七八九])十(?![一-龥])', lambda m: POS[m.group(1)] + '0', text)

    # 〜七期, 〜十期 in ranges: 第1〜七期 → 第1〜7期 (cleanup of mid-range)
    text = re.sub(r'(〜|～|から)([〇一二三四五六七八九十百千]+)(期|章|部|節|回|代|次)',
                  lambda m: m.group(1) + parse_kanji_number(m.group(2)) + m.group(3), text)

    # 二─十二か月 ranges
    text = re.sub(r'([〇一二三四五六七八九十百千]+)(─|—|-)([〇一二三四五六七八九十百千]+)(か月|ヶ月|か所|年|時間)',
                  lambda m: parse_kanji_number(m.group(1)) + m.group(2) + parse_kanji_number(m.group(3)) + m.group(4), text)

    # Final cleanup: 五十/六十/...九十/十 standalone before non-kanji → 50/60/.../90/10
    text = re.sub(r'(?<![一-龥])([二三四五六七八九])十(?![一-龥])',
                  lambda m: POS[m.group(1)] + '0', text)

    return text

def main():
    paths = [
        Path.home() / "projects/research/physical-ai-2100/output/index_v5.html",
        Path.home() / "projects/research/physical-ai-2100/output/index.html",
        Path.home() / "projects/research/physical-ai-2100/docs/index.html",
    ]
    for p in paths:
        if not p.exists(): continue
        orig = p.read_text()
        new = convert(orig)
        p.write_text(new)
        kanji_total = len(re.findall(r'[〇一二三四五六七八九]', new))
        print(f"{p.name}: kanji digit chars remain = {kanji_total}")

if __name__ == "__main__":
    main()
