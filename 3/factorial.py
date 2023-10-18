import sys
import math

def factorial(x):
    fac = 1
    for i in range(2, x + 1):
        fac *= i
    return(fac)

def factorial_2(x):         #дедовский метод из сишарпа
    if x == 0: return 1
    else: return x * factorial_2(x - 1)

while True:
    try:
        num = int(input('Enter num:'))
        # print(f"{num}! = {factorial(num)}")  #если бы юзали свою функцию
        fac = math.factorial(num)
        print(f"{num}! = {fac}")
        break

    except Exception as e:
        print(f'Error: {e}')

sys.exit()