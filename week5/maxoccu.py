def max_occurrence(s):
    freq = {}

    for ch in s:
        if ch.isalpha():
            ch = ch.lower()
            freq[ch] = freq.get(ch,0)+1

    max_char = max(freq,key=freq.get)

    return max_char, freq[max_char]


def main():
    s = "programming"

    char, count = max_occurrence(s)

    print("Character:", char)
    print("Count:", count)


if __name__ == "__main__":
    main()