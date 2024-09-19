def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы {i}')
            incorrect_data += 1
    else:
        pass
    return (result, incorrect_data)

def calculate_average(numbers):
    try:
        iter(numbers)
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    r = personal_sum(numbers)
    try:
        cal_ave = r[0]/(len(numbers) - r[1])
    except ZeroDivisionError:
        return 0
    return cal_ave

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')

