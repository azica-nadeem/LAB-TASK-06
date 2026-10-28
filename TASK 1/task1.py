numbers = [2, 3, 2, 5, 3, 2, 5, 8]

result = {}

for num in numbers:
    if num in result:
        result[num] += 1
    else:
        result[num] = 1

print(result)