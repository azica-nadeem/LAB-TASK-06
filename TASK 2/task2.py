mark = {
    'Ali': 85,
    'Sara': 95,
    'Ahmed': 95,
    'Noor': 78
}

highest = max(mark.values())

for name, marks in mark.items():
    if marks == highest:
        print(name, marks)