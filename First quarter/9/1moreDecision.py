from sympy import primerange
from math import gcd        # Наибольший общий делитель, чтобы велосипед не собирать
from functools import reduce    # Почитал на досуге, вот и юзанул
from termcolor import colored       # Косметичка

class UserInput:        # Методы для пользовательского ввода: строка, int и getEnter

    @staticmethod
    def getStr(prompt):     
            value = input(prompt)
            return value

    @staticmethod
    def getInt(prompt="Enter a natural number: "):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print(f"{colored('Error:', 'red')} Enter a valid integer!")
                

    @staticmethod
    def getInt_list(prompt="Enter numbers separated by a space: "):
            txt = UserInput.getStr(prompt)
            parts = txt.split()
            result = []

            for part in parts:
                if part.isdigit():      #если циферка пробуем в инт закинуть
                    result.append(int(part))
                else:                               #будет чтото ошибочное не заново, просто пропускаем и указываем
                    print(f"{colored('Incorrect input:', 'red')} '{part}' not a number.")

            if result:      #если все неправильно, ну извините
                return result
            else:
                print(f"{colored('Error:', 'red')} Enter a valid values!")

    @staticmethod
    def getEnter():
        input("\nPress Enter to continue...")


class MyFunc:
    
    def LCM_List(self, values):     # Наименьшее общее кратное
        result = reduce(lambda a, b: a * b // gcd(a,b), values)
        return result
        
    def primes(self, num):
        if num <= 0:
            return False
        return primerange(1, num + 1) # функция библиотеки sympy дял нахождения простых чисел
        
    def divisors(self, num):        # В описании не нуждается, делители числа
        if num <= 0:
            return False
        result = []
        for i in range(1, num):
            if num % i == 0:
                result.append(i)
        return result
        

class Main:

    func = MyFunc()       #as ... для удобства
    user = UserInput()
 
    while True:
        print(colored("\nSelect a task:", "magenta", attrs=['bold']))
        print("1.Least Common Multiple (LCM)") 
        print("2.Find primes")              
        print("3.Find divisors")   
        print(colored("0.Exit", "cyan", attrs=['bold'])) 
        
        select = user.getStr(colored("\nEnter num task: ", "green", attrs=['bold']))  

        if select == "1":   
            print()
            values = user.getInt_list()
            result = func.LCM_List(values)
            print(f"\nThe least common multiple of", *values, "is",colored(result, "magenta", attrs=["bold"]))
            user.getEnter()

        elif select == "2": 
            num = user.getInt()
            result = func.primes(num)
            print(f"Prime numbers from 1 to{num}:", *result) if result else print(f"{colored('Error:', 'red')} Try again pls")
            user.getEnter()

        elif select == "3": 
            
            num = user.getInt()
            result = func.divisors(num)
            print(*result) if result else print(f"{colored('Error:', 'red')} ZeroDivisionError")
            user.getEnter()

        elif select == "0": 
            break 
            
        else:
            print(f"{colored('Error:', 'red')} Wrong choice. Please select the issue number from the list.")
    
Main()