def nod(a, b):
    while b:
         a, b = b, a % b
    return a

class Main():
    a = int(input("Введите первое натуральное число: "))
    b = int(input("Введите второе натуральное число: "))

    # находим НОД чисел a и b
    nod_result = nod(a, b)

    # вычисляем НОК чисел a и b
    nok_result = (a * b) // nod_result

    print(f"\nНаименьшее общее кратное чисел {a} и {b} равно {nok_result}")