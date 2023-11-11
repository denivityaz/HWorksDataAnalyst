import timeit   # Время тестирования
import random   # Заполнение списков
from functools import reduce    # Так и не понял зачем этот reduce, как нибудь на досуге почитаю
from termcolor import colored       # Косметичка

# Линейный поиск
def linear_search_max(lst):
    # if not lst:
    #     return None
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

# Функция reduce
def reduce_max(lst):
    # if not lst:
    #     return None
    return reduce(lambda x, y: x if x > y else y, lst)



# Метод максимального значения через sort, удивительно, что довольно шустро, надо исходники посмотреть, что там такое
def sort_max(lst):
    # if not lst:
    #     return None
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[0]

# Встроенная функция Python, только это С по факту
def maxFuncPy(lst):
    # if not lst:
    #     return None
    return max(lst)

# Разделяй и влавствуй типо CS50 посмотрели и умные
def find_max_divide_and_conquer(lst, start=0, end=None):
    if end is None:
        end = len(lst) - 1

    if start == end:
        return lst[start]

    mid = (start + end) // 2

    left_max = find_max_divide_and_conquer(lst, start, mid)
    right_max = find_max_divide_and_conquer(lst, mid + 1, end)

    return max(left_max, right_max)

# Рекурсивный метод ВООБЩЕ НЕ ПОНЯЛ ЗАЧЕМ ОН НУЖЕН В КОНТЕКСТЕ НАХОЖДЕНИЯ МАКСИМУМА, я протестировал его на 10000, было нормально, поставил лям и стек превратился в очередь из бабушек с мелочью в семишагове
# хорошо что на орбиту не отправился, подходит для разгона проца эта рекурсия
def find_max_recursively(lst):
    try:
        if not lst:
            return None
        else:
            rest_max = find_max_recursively(lst[1:])
            return lst[0] if rest_max is None or lst[0] > rest_max else rest_max
    except:
        return None
    
    # Сама домашняя работа в этих 8 строчках
def recursiveByMe(lst, _ = 0):  # _ - флажок итерации. Функция вроде ничем особо не отличается от метода нейронки выше, но результаты в десятки быстрее
    try:
        if _ == len(lst):
            return None
    
        max = recursiveByMe(lst, _ + 1)
        return lst[_] if max is None or lst[_] > max else max   # Обычный линейный поиск, только рекурсией. И при тестировании они почти всегда одинаковые
    except:
        return None
# Тестирование
def test_algorithm(algorithm, lst):
    start_time = timeit.default_timer()
    result = algorithm(lst)
    elapsed_time = timeit.default_timer() - start_time
    return result, elapsed_time

# Вычисление среднего времени выполнения для конкретного алгоритма и размера списка
def average_time(algorithm, lst_size, repetitions):
    total_time = 0
    for _ in range(repetitions):
        lst = random.sample(range(1, lst_size + 1), lst_size)  # Генерация нового случайного списка
        _, elapsed_time = test_algorithm(algorithm, lst)
        total_time += elapsed_time
    return total_time / repetitions

class Main:
    sizes = [100, 1000, 10000]  #ставить больше 10 000 не советую при использовании рекурсии!!! мне лень переписывать все для авто выкл
    repetitions = 1  # Количество повторений для каждого алгоритма

    # Словарь, ну вроде так удобнее и читабельнее
    algorithms = {
        "Линейный поиск": linear_search_max,
        "Метод reduce": reduce_max,
        "Сортировка и возврат последнего значения": sort_max,
        "Дефолтная функция max() Python, но вообще это C": maxFuncPy,
        "Разделяй и всластвуй CS50 посмотрели и типо умные":find_max_divide_and_conquer,
        "Нейронка делала рекурсию, видимо ну не получилось у нее": find_max_recursively,
        "А это моя, не украл, а переделал предыдущую": recursiveByMe
    }
    # Вывод
    for size in sizes:
        print(colored(f"\nResults for List Size: {size}\n", "green", attrs=['bold']))
        for algo_name, algo_func in algorithms.items():
            avg_time = average_time(algo_func, size, repetitions)
            if avg_time:
                print(colored(f"{algo_name}", "blue", attrs=['bold']))
                print(colored(f"AVG Time: {avg_time:.9f}\n", "white"))
            else:
                print(f"{algo_name}: Error. I think this is recursive method")
