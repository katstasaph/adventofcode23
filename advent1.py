def first_last_digits_only(s):
    for (i, chr) in enumerate(s):
        first_chr = chr
        if first_chr.isdigit():
            break
    for (i, chr) in enumerate(reversed(s)):
        second_chr = chr
        if second_chr.isdigit():
            break
    return int(first_chr + second_chr)


DIGIT_WORDS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0"
}


def first_last_digits_with_words(s):
    first_digit = parse_first_digit(s)
    second_digit = parse_second_digit(s)
    return int(first_digit + second_digit)


def parse_first_digit(s):
    start = 0
    first_digit = s[start]
    first_three = s[0:3]
    first_four = s[0:4]
    first_five = s[0:5]
    while (True):
        if (first_digit.isdigit()):
            return first_digit
        elif (DIGIT_WORDS.get(first_three)):
            return DIGIT_WORDS.get(first_three)
        elif (DIGIT_WORDS.get(first_four)):
            return DIGIT_WORDS.get(first_four)
        elif (DIGIT_WORDS.get(first_five)):
            return DIGIT_WORDS.get(first_five)
        start += 1
        first_digit = s[start]
        first_three = s[start:(3 + start)]
        first_four = s[start:(4 + start)]
        first_five = s[start:(5 + start)]


def parse_second_digit(s):
    end = len(s) - 1
    second_digit = s[end]
    last_three = s[end - 2:]
    last_four = s[end - 3:]
    last_five = s[end - 4:]
    end_idx = 0
    while (True):
        if (second_digit.isdigit()):
            return second_digit
        elif (DIGIT_WORDS.get(last_three)):
            return DIGIT_WORDS.get(last_three)
        elif (DIGIT_WORDS.get(last_four)):
            return DIGIT_WORDS.get(last_four)
        elif (DIGIT_WORDS.get(last_five)):
            return DIGIT_WORDS.get(last_five)
        end -= 1
        end_idx -= 1
        second_digit = s[end]
        last_three = s[end - 2:end_idx]
        last_four = s[end - 3:end_idx]
        last_five = s[end - 4:end_idx]


with open("advent1.txt", "r") as f:
    strings = f.read().split()
    sum1 = 0
    sum2 = 0
    for s in strings:
        sum1 += first_last_digits_only(s)
        sum2 += first_last_digits_with_words(s)
    print(sum1, sum2)
