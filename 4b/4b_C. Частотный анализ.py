words = dict()
data = open('input.txt', 'r', encoding='utf8')
for line in data:
    string = line.split()
    for i in range(len(string)):
        if string[i] not in words:
            words[string[i]] = 1
        else:
            words[string[i]] = words[string[i]] + 1
list_words = list(words.items())
list_words.sort(key=lambda x: (-x[1], x[0]))
for i in range(len(words)):
    print(list_words[i][0])
