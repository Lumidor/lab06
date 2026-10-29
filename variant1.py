numbers = []
for part in input().split():
    numbers.append(int(part))
selected = []
for number in numbers:
    if number % 2 == 0:
        selected.append(number)
count = len(selected)
total_sum = sum(selected)
sorted_copy = sorted(selected)

print(selected)
print(count)
print(total_sum)
print(sorted_copy)
