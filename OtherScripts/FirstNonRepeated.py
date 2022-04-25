from collections import defaultdict


if __name__ == '__main__':
    d = defaultdict(int)
    word = input("Input a word: ")
    for letter in word:
        d.update([(letter, d[letter] + 1)])
    for letter in word:
        if d[letter] == 1:
            print(letter)
            break
