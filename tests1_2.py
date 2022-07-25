"""Задание №1"""
def dictionary_generator(ls1: list, ls2: list) -> dict:
    for _ in range(len(ls1) - len(ls2)):
        ls2.append(None)

    new_dict = {}
    for key, val in zip(ls1, ls2):
        new_dict.setdefault(key, val)
    return new_dict


result = dictionary_generator(['A', 'B', 'C', 'D'], [1, 2, 3])
result1 = dictionary_generator(['A', 'B'], [1, 2, 3])
result2 = dictionary_generator([], [1, 2, 3])
# print(result)
# print(result1)
# print(result2)

"""Задание №2"""
numbers = [3, 4]
# Создание ряда Фибоначчи
while numbers[-1] < 7000000:
    need = numbers[-2] + numbers[-1]
    numbers.append(need)


def filter_func():
    """Функция для удаления нечётных чисел
    в последовательности"""
    for num in numbers:
        if (num % 2) != 0:
            numbers.remove(num)
    print(sum(numbers))

# filter_func()
