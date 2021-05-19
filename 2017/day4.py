#!/bin/python3


#


def main():
    input = 'inputs/input_day4.txt'

    # part 1
    valid_lines = 0
    extra_valid_lines = 0
    with open(input, 'r') as file:
        for passphrase in file.readlines():
            if validate(passphrase):
                valid_lines += 1
            if validate_words(passphrase):
                extra_valid_lines += 1
    print(valid_lines)

    # part 2
    print(extra_valid_lines)


def validate(passphrase):
    words = passphrase.split()
    word_set = set(words)
    if len(words) == len(word_set):
        return True
    else:
        return False


def validate_words(passphrase):
    words = passphrase.split()
    codes = []
    alphabet = ''.join(chr(x) for x in range(ord('a'), ord('z')+1))
    for word in words:
        code = [str(word.count(letter)) for letter in alphabet]
        codes.append(''.join(code))

    codes = set(codes)
    if len(words) == len(codes):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
