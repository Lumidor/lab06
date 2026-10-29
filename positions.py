numbers = []
for part in input().split():
    numbers.append(int(part))

if len(numbers) == 0:
    print("Нет данных")
else:
    max_value = max(numbers)
    positions = []
    for index, value in enumerate(numbers):
        if value == max_value:
            positions.append(index)       
    print(positions)
