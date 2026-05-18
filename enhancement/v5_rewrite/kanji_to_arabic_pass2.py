#!/usr/bin/env python3
"""Second pass: extended counters and edge cases."""
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

# Extended counters (added 領域/段/相/重/種/類/足/個/列/列車/室/階/桁/組/対/通り/筋/手/順)
COUNTERS = '|'.join([
    '年','月','日','時','分','秒','世紀','章','部','節','項','系統','段階',
    '件','個','人','名','歳','箇所','か所','倍','桁','円','兆','億','万',
    '台','本','首','社','国','州','軒','匹','頭','羽','杯','度目','度','順',
    '歩','語','文字','字','頁','ページ','冊','機','機種','型','世代','代',
    '波','相','層','軸','極',
    # Newly added
    '領域','段','種','類','足','重','次','回','室','階','組','対','通り','筋','手',
    'パターン','側','色','点','様','行','局','義','枝','枚','部位','つ',
    '％','%','割',  # percentage / proportion
])

# Idiom set (already-converted target words)
IDIOMS_REGEX = re.compile(
    r'(一方|一切|一概|一気|一斉|一見|一致|一貫|一旦|一連|一律|一行|一刻|一抹|'
    r'一筋|一読|一杯|一義|一服|一同|一礼|一望|一票|一目|一手|一例|一面|一向|'
    r'一通り|一郎|一身|一神|一形|一脳|一体|一緒|一般|一次|一段と|'
    r'万一|万全|万能|万人|万元|万級|万回|十全|二者択一|二者|二次|二重|二種|'
    r'二腕|二領|二段|二項|二原|二九|二三|二四|二五|二六|二七|二八|二十以|二二|二主|二七|二千年|'  # avoid converting these tricky ones
    r'三者|三大|三菱|三制|三経|三百|'  # 三百 we DO want converted but in context
    r'四足|四類|四地|四象|四原|四段|'  # debatable, keep for now
    r'五十|五段|五次|'
    r'六十|六五|六段|六基|六領|六十五学|'
    r'七十|七期|'
    r'八十|八割|八十五|'
    r'九十|九五|'
    r'十二|十二分|十人十色|'
    r'百八十|百五十超|百科|百花繚乱|百聞|'
    r'千五百|千規|千住|千差万別|千変万化|'
    r'万六千)'
)

# More targeted conversions
def convert(text):
    # 1. Fix Arabic-followed-by-〇 (e.g., "1・〇" should be "1.0")
    text = re.sub(r'(\d)・〇', r'\1.0', text)
    text = re.sub(r'(\d)・([一二三四五六七八九])', lambda m: m.group(1) + '.' + POS[m.group(2)], text)

    # 2. Two-digit positional followed by % or 割 (e.g., 二六%)
    text = re.sub(r'([〇一二三四五六七八九])([〇一二三四五六七八九])(%|％|割)',
                  lambda m: POS[m.group(1)] + POS[m.group(2)] + m.group(3),
                  text)
    # Three-digit positional followed by % (rarer)
    text = re.sub(r'([〇一二三四五六七八九])([〇一二三四五六七八九])([〇一二三四五六七八九])(%|％|割)',
                  lambda m: POS[m.group(1)] + POS[m.group(2)] + POS[m.group(3)] + m.group(4),
                  text)

    # 3. Number + extended counter (add 領域/段/種/類/足/相/重/次/回/室/階/組/対/側/通り/筋/手/つ)
    # Re-run with extended counter list
    text = re.sub(r'([〇一二三四五六七八九十百千万億]+)(領域|段|相|重|種|類|足|次(?!元)|回|室|階|組|対|通り|筋|手|％|%|割|つ(?!\w)|本|首|台|社|軒)',
                  lambda m: parse_kanji_number(m.group(1)) + m.group(2) if not IDIOMS_REGEX.fullmatch(m.group(1)+m.group(2)) else m.group(),
                  text)

    # 4. Number + 兆/億/万 standalone (e.g., 一千万 in "一千万円" already covered, but "一千万" with no counter is also worth converting)
    text = re.sub(r'(?<![一-龥])([〇一二三四五六七八九十百千]*[万億兆])(?=[人台社件回頭杯名箇所軒度回\s。、）\)<])',
                  lambda m: parse_kanji_number(m.group(1)),
                  text)

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
        # Count remaining
        kanji_total = len(re.findall(r'[〇一二三四五六七八九]', new))
        # Check specific patterns
        rem_pct = len(re.findall(r'[〇一二三四五六七八九]+%', new))
        rem_dom = len(re.findall(r'[〇一二三四五六七八九]+領域', new))
        rem_stage = len(re.findall(r'[〇一二三四五六七八九]+段', new))
        print(f"{p.name}: kanji digit chars remain = {kanji_total}, %={rem_pct}, 領域={rem_dom}, 段={rem_stage}")

if __name__ == "__main__":
    main()
