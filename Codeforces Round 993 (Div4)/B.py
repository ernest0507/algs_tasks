t = int(input())
words = [input() for _ in range(t)]

for i in range(t):
    new_word = ''
    for letter in words[i]:
        if letter == 'q':
            new_word += 'p'
        elif letter == 'p':
            new_word += 'q'
        else:
            new_word += letter
    print(new_word[::-1])
