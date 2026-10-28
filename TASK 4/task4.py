
words = ['apple', 'ant', 'banana', 'ball', 'cat']

result = {}

for word in words:
    first = word[0]

    if first in result:
        result[first].append(word)
    else:
        result[first] = [word]

print(result)
