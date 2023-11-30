from collections import Counter, defaultdict
from datetime import datetime
from math import sqrt


example_template = "NNCB"
example_readings = ["CH -> B", "HH -> N", "CB -> H", "NH -> C", "HB -> C", "HC -> B", "HN -> C", "NN -> C", "BH -> H", "NC -> B", "NB -> B", "BN -> B", "BB -> N", "BC -> B", "CC -> N", "CN -> C"]

template = "OHFNNCKCVOBHSSHONBNF"
readings = ["SV -> O", "KP -> H", "FP -> B", "VP -> V", "KN -> S", "KS -> O", "SB -> K", "BS -> K", "OF -> O", "ON -> S", "VS -> F", "CK -> C", "FB -> K", "CH -> K", "HS -> H", "PO -> F", "NP -> N", "FH -> C", "FO -> O", "FF -> C", "CO -> K", "NB -> V", "PP -> S", "BB -> N", "HH -> B", "KK -> H", "OP -> K", "OS -> V", "KV -> F", "VH -> F", "OB -> S", "CN -> H", "SF -> K", "SN -> P", "NF -> H", "HB -> V", "VC -> S", "PS -> P", "NK -> B", "CV -> P", "BC -> S", "NH -> K", "FN -> P", "SH -> F", "FK -> P", "CS -> O", "VV -> H", "OC -> F", "CC -> N", "HK -> N", "FS -> P", "VF -> B", "SS -> V", "PV -> V", "BF -> V", "OV -> C", "HO -> F", "NC -> F", "BN -> F", "HC -> N", "KO -> P", "KH -> F", "BV -> S", "SK -> F", "SC -> F", "VN -> V", "VB -> V", "BH -> O", "CP -> K", "PK -> K", "PB -> K", "FV -> S", "HN -> K", "PH -> B", "VK -> B", "PC -> H", "BO -> H", "SP -> V", "NS -> B", "OH -> N", "KC -> H", "HV -> F", "HF -> B", "HP -> S", "CB -> P", "PN -> S", "BK -> K", "PF -> N", "SO -> P", "CF -> B", "VO -> C", "OO -> K", "FC -> F", "NV -> F", "OK -> K", "NN -> O", "NO -> O", "BP -> O", "KB -> O", "KF -> O", ]

# template = example_template
# readings = example_readings


# PART 1
def build_rules(readings):
    rules = {}
    for r in readings:
        key, val = r.split(" -> ")
        rules[key] = val
    return rules


def apply_rules(rules, formula):
    new_formula = []  # assuming all rules are "2" elements wide
    for i, val in enumerate(formula):
        pair = str(formula[i:i+2])
        if len(pair) < 2:
            new_formula.append(f"{pair[0]}")
            break
        middle = rules[pair]
        new_formula.append(f"{pair[0]}{middle}")
    return "".join(new_formula)


iterations = 10
formula = str(template)
rules = build_rules(readings)
for i in range(iterations):
    formula = apply_rules(rules, formula)

cn = Counter(formula).most_common()
res = cn[0][1] - cn[-1][1]
print(res)
print(cn)


# PART 2... faster than Part 1... not even close as needed
def build_rules_with_size(readings):
    rules = defaultdict(dict)
    rules[2] = build_rules(readings)
    alphabet = set(r[0] for r in readings)
    print(f"building rules with size ...")
    for i in range(3, 7):
        print(f"size {i} ...")
        for r in rules[i - 1]:
            for a in alphabet:
                rules[i][f"{r}{a}"] = apply_rules(rules[2], f"{r}{a}")[:-1]
    print(f"done building rules")
    return rules


def apply_rules_long(rules, formula):
    new_formula = []
    i = 0
    base = [a for a in range(7)]

    while i < len(formula):
        for e in reversed(base):
            entry = str(formula[i:i + e])
            if e == 2:
                if len(entry) < 2:
                    new_formula.append(f"{entry[0]}")
                    i += 1
                    break
                middle = rules[2][entry]
                new_formula.append(f"{entry[0]}{middle}")
                i += 1
                break
            if len(entry) < e:
                continue
            middle = rules[e].get(entry, 0)
            if not middle:
                middle = apply_rules_long(rules, f"{entry}")[:-1]
                # rules[e][f"{entry}"] = middle
            new_formula.append(f"{middle}")
            i += e - 1
            break
    return "".join(new_formula)


iterations = 25  # still too slow for 40...
formula = str(template)
rules = build_rules_with_size(readings)

ini = datetime.now()
cn = Counter(formula[-1])
for i, val in enumerate(formula):  # split input in pairs and calculate those
    print(f"i {i}/{len(formula)} val {val} elapsed: {datetime.now() - ini}")
    pair = new_pair = str(formula[i:i+2])
    if len(pair) < 2:
        break
    for it in range(iterations):
        new_pair = apply_rules_long(rules, new_pair)
    cn += Counter(new_pair[:-1])  # count letters and discard to free memory

res = cn.most_common()[0][1] - cn.most_common()[-1][1]
print(res)
print(cn.most_common())
