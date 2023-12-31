from termcolor import colored       # Косметичка
from datetime import datetime

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
    
    def NOD(self, x, y):      
        while y:
            x, y = y, x % y
        return x
    
    def NOK(self, x, y, z):
        return x * y // z
    
    def simple_brute_force(self, num):     #метод перебора, другие способы не очень понимаю
    
        def isSimple(num):
            if num < 2:
                return False
            # Перебираем числа от 2 до корня из num
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            # Если не нашли делителей, то num простое
            return True

        # Все в список
        primes = [i for i in range(2, num + 1) if isSimple(i)]
        return primes
        
        # список делителей
    def dividers(self, num):
        start_time = datetime.now ()
        result = [i for i in range (1, num // 2 + 1) if num % i == 0] + [num]   # Генерирует все числа от 1 до num\\2
        end_time = datetime.now ()
        print ('time: ', end_time - start_time)
        return result
        

        
        

class Main:

    func = MyFunc()       #as ... для удобства
    user = UserInput()
 
    while True:
        print(colored("\nSelect a task:", "magenta", attrs=['bold']))
        print("1.Summ 2 lists") 
        print("2.Multiple of 19 and 13")              
        print("3.Max with reduce")   
        print(colored("0.Exit", "cyan", attrs=['bold'])) 
        
        select = user.getStr(colored("\nEnter num task: ", "green", attrs=['bold']))  

        if select == "1":   
            print()
            num1 = user.getInt()
            num2 = user.getInt()
            NOD = func.NOD(num1, num2)
            NOK = func.NOK(num1, num2, NOD)
            print(f"\nThe least common multiple of {num1} and {num2} is",colored(NOK, "magenta", attrs=["bold"]))
            user.getEnter()

        elif select == "2": 
            num = user.getInt()
            result = func.simple_brute_force(num)
            print(f"Простые числа от 1 до {num}:", *result)
            user.getEnter()

        elif select == "3": 
            
            num = user.getInt()
            result = func.dividers(num)
            print(*result)
            user.getEnter()

        elif select == "0": 
            break 
            
        else:
            print("Error: Wrong choice. Please select the issue number from the list.")
    
Main()