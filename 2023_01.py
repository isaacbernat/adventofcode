# PART 1
vals = []
nums = '0123456789'
with open("2023_01.input") as f:
    for l in f.readlines():
        for char in l:
            if char in nums:
                init = char
                break
        for char in l[::-1]:
            if char in nums:
                end = char
                break
        vals += [f"{init}{end}"]
    print(sum([int(n) for n in vals]))


# A cleaner pt1...
# vals = []
# nums = '0123456789'
# with open("2023_01.input") as f:
#     for l in f.readlines():
#         _, init = first_digit(l, order=1)
#         _, end = first_digit(l, order=-1)
#         vals += [f"{init}{end}"]
#     print(sum([int(n) for n in vals]))


# PART 2
def first_digit(line, order):
    for idx, char in enumerate(l[::order]):
        if char in nums:
            return idx, char
    return len(line), 'Z'


def first_text(line, max_idx, order):
    line = ''.join([c for c in line[::order]]).strip()
    min_num, min_idx = 0, max_idx
    digits = text_digits if order == 1 else reversed_text_digits
    for idx, t in enumerate(digits):
        res = line[:max_idx].split(t)
        if len(res) > 1:
            if min_idx > len(res[0]):
                min_num = nums[idx]
                min_idx = len(res[0])
    return min_idx, min_num


vals = []
nums = '0123456789'
text_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
reversed_text_digits = [''.join([c for c in word[::-1]]) for word in text_digits]
# ugly hack above. Pt 2 took me 30 minutes... had to debug several times because of that ^_^U
with open("2023_01.input") as f:
    for l in f.readlines():
        init_idx, init = first_digit(l, order=1)
        text_idx, text_init = first_text(l, init_idx, order=1)
        init = text_init if text_idx < init_idx else init

        end_idx, end = first_digit(l, order=-1)
        text_idx, text_end = first_text(l, end_idx, order=-1)
        end = text_end if text_idx < end_idx else end

        vals += [f"{init}{end}"]
    print(sum([int(n) for n in vals]))


# A cleaner pt2... TODO
