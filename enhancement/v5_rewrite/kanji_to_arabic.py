#!/usr/bin/env python3
"""Convert kanji numerals to Arabic in PHAI v5 HTML.

Safe rules:
1. Year-like positional 4-digit (一九四九/二〇二六/二一〇〇) → 1949/2026/2100
2. 第N + (章/部/節/項) → 第N (Arabic)
3. Kanji number + counter (年/月/日/時/世紀/章/部/節/項/系統/段階/件/個/人/名/歳/箇所/か所/分/秒/倍/桁/円/兆/億/万) → Arabic + counter
4. Standalone large numbers with 十百千万億 → Arabic
5. Preserve idiomatic phrases: 一方/一切/一概/一気/一斉/一見/一致/一貫/一旦/一連/一律/一行/一刻/一抹/一筋/一読/一杯/一義/万一/万全/万能/万人/十全/十二分/二項/二者
6. SVG <text> labels also converted

Avoid converting:
- 第一原則/第一義/第二次世界大戦 (well-known names) — case by case
- 一つ/一人/二人 — convert
"""
import re
from pathlib import Path

# Digit map for positional notation
POS = {'〇':'0','一':'1','二':'2','三':'3','四':'4','五':'5','六':'6','七':'7','八':'8','九':'9'}

def parse_kanji_number(s: str) -> str:
    """Parse a kanji-number string (digits + 十百千万億) to Arabic."""
    if not s:
        return s
    # Pure positional
    if all(c in POS for c in s):
        return ''.join(POS[c] for c in s)

    units = {'十':10, '百':100, '千':1000}
    big_units = {'万':10000, '億':100000000, '兆':1000000000000}

    # Parse: split by big units first
    n = 0
    section = 0
    digit = 0

    i = 0
    while i < len(s):
        c = s[i]
        if c in POS:
            digit = digit * 10 + int(POS[c])
        elif c in units:
            u = units[c]
            if digit == 0:
                digit = 1
            section += digit * u
            digit = 0
        elif c in big_units:
            bu = big_units[c]
            section += digit
            n += section * bu
            section = 0
            digit = 0
        i += 1
    section += digit
    n += section
    return str(n)

# Idioms to preserve (don't convert these intact phrases)
IDIOMS = {
    '一方': '一方', '一切': '一切', '一概': '一概', '一気': '一気', '一斉': '一斉',
    '一見': '一見', '一致': '一致', '一貫': '一貫', '一旦': '一旦', '一連': '一連',
    '一律': '一律', '一行': '一行', '一刻': '一刻', '一抹': '一抹', '一筋': '一筋',
    '一読': '一読', '一杯': '一杯', '一義': '一義', '一服': '一服', '一同': '一同',
    '一礼': '一礼', '一望': '一望', '一票': '一票', '一目': '一目', '一手': '一手',
    '一例': '一例', '一段と': '一段と', '一面': '一面', '一向': '一向', '一通り': '一通り',
    '万一': '万一', '万全': '万全', '万能': '万能', '十全': '十全',
    '二者択一': '二者択一', '三者三様': '三者三様', '十人十色': '十人十色',
    '千差万別': '千差万別', '千変万化': '千変万化', '百花繚乱': '百花繚乱',
    '百聞': '百聞', '一見は': '一見は', '一見の': '一見の',
}

def protect_idioms(text: str):
    """Replace idioms with placeholders, return (text, mapping)."""
    placeholders = {}
    for i, idiom in enumerate(sorted(IDIOMS, key=len, reverse=True)):
        ph = f'IDIOM{i}'
        placeholders[ph] = idiom
        text = text.replace(idiom, ph)
    return text, placeholders

def restore_idioms(text: str, placeholders: dict):
    for ph, idiom in placeholders.items():
        text = text.replace(ph, idiom)
    return text

def convert_text(text: str) -> str:
    # 1) Protect idioms
    text, ph = protect_idioms(text)

    # 2) Convert 4-digit year-like positional sequences (一九XX, 二〇XX, 二一XX, etc.)
    text = re.sub(r'[一二][〇一二三四五六七八九]{3}',
                  lambda m: ''.join(POS[c] for c in m.group()),
                  text)

    # 3) Convert 第N (chapter/section refs)
    text = re.sub(r'第([〇一二三四五六七八九十百千]+)',
                  lambda m: '第' + parse_kanji_number(m.group(1)),
                  text)

    # 4) Convert kanji number + counter
    counters = '年|月|日|時|分|秒|世紀|章|部|節|項|系統|段階|件|個|人|名|歳|箇所|か所|倍|桁|円|兆|億|万|台|本|首|社|国|州|軒|匹|頭|羽|杯|杯目|度目|度|順|歩|語|文字|字|頁|ページ|冊|機|機種|型|世代|代|波|相|層|軸|極|つ|つの|つで|つに|つを|つは|つも|つや|つしか'
    text = re.sub(r'([〇一二三四五六七八九十百千万億]+)(' + counters + ')',
                  lambda m: parse_kanji_number(m.group(1)) + m.group(2),
                  text)

    # 5) Convert "N・N" decimal style (e.g., 二・〇)
    text = re.sub(r'([〇一二三四五六七八九])・([〇一二三四五六七八九])',
                  lambda m: POS[m.group(1)] + '.' + POS[m.group(2)],
                  text)

    # 6) Long standalone numbers with 十百千万億 (3+ chars, not preceded/followed by other kanji)
    # E.g., 三〇〇 standalone, 一千万
    text = re.sub(r'(?<![一-龥])([〇一二三四五六七八九][〇一二三四五六七八九十百千万億]{2,})(?![一-龥])',
                  lambda m: parse_kanji_number(m.group(1)),
                  text)

    # 7) Restore idioms
    text = restore_idioms(text, ph)
    return text

def main():
    paths = [
        Path.home() / "projects/research/physical-ai-2100/output/index_v5.html",
        Path.home() / "projects/research/physical-ai-2100/output/index.html",
        Path.home() / "projects/research/physical-ai-2100/docs/index.html",
    ]

    for p in paths:
        if not p.exists():
            continue
        original = p.read_text()
        converted = convert_text(original)
        p.write_text(converted)

        # Stats
        kanji_before = len(re.findall(r'[〇一二三四五六七八九]', original))
        kanji_after = len(re.findall(r'[〇一二三四五六七八九]', converted))
        # Remove kanji within likely-CJK-text contexts
        sample_remain = re.findall(r'[〇一二三四五六七八九]+[年月日章部節項系統段階件個人名歳倍]', converted)[:10]
        print(f"{p.name}:")
        print(f"  Kanji digit chars: {kanji_before:,} → {kanji_after:,} ({100*kanji_after/kanji_before:.1f}% remain)")
        print(f"  Sample remaining kanji+counter: {sample_remain[:5]}")

if __name__ == "__main__":
    main()
