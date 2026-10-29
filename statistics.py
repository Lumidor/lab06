numbers = []
for part in input().split():
    numbers.append(int(part))

if len(numbers) == 0:
    print("Нет данных")
else:
    count = len(numbers)
    total_sum = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    average = total_sum / count
    
    print(f"Количество: {count}")
    print(f"Сумма: {total_sum}")
    print(f"Минимум: {minimum}")
    print(f"Максимум: {maximum}")
    print(f"Среднее: {average:.2f}")
