from termcolor import colored       #косметичка
from functools import reduce

class UserInput:        #Методы для пользовательского ввода: строка, int и getEnter

    @staticmethod
    def getStr(prompt):     
            value = input(prompt)
            return value

    @staticmethod
    def getInt(prompt):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Error: Enter a valid integer!")

    @staticmethod
    def getInt_list(prompt="Enter numbers separated by a space: "): #вывод по дефолту, странно что раньше не юзал
        while True:
            txt = UserInput.getStr(prompt)
            parts = txt.split()
            result = []

            for part in parts:
                if part.isdigit():      #если циферка пробуем в инт закинуть
                    result.append(int(part))
                else:                               #будет чтото ошибочное не заново, просто пропускаем и указываем
                    print(f"Incorrect input: '{part}' not a number.")

            if result:      #если все неправильно, ну извините
                return result
            else:
                print("Error: Enter a valid values!")

    @staticmethod
    def getEnter():
        input("\nPress Enter to continue...")


class MyFunc:
    
    def sumInt_list(self, lst1, lst2):
        result = list(map(lambda x, y: x + y, lst1, lst2)) #но это все дело не складывается полностью, если они разной длины, то список в результате будет длины совпадения
        len1 = len(lst1)        #вроде функция len вызывается каждый раз, экономнее присвоить переменную
        len2 = len(lst2)
        minimaLen = min(len1, len2) #мин для того, чтобу узнать откуда добавлять значения вне совпадений

        if len1 > minimaLen:                #недостающие значения добавляем
            result.extend(lst1[minimaLen:])
        elif len2 > minimaLen:
            result.extend(lst2[minimaLen:])
        return result

    def maxValuesWithReduceWhy(self, lst):
        maximum = reduce(lambda x, y: x if x > y else y, lst)
        return maximum
        

class Main:

    func = MyFunc()       #as ... для удобства
    user = UserInput()
 
    while True:
        print(colored("\nSelect a task:", "magenta", attrs=['bold']))
        print("1.Summ 2 lists") 
        print("2.Multiple of 19 and 13")              
        print("3.Max with reduce")   
        print(colored("0.Exit", "cyan", attrs=['bold'])) 
        
        select = user.getStr(colored("\nEnter num task:", "green", attrs=['bold']))  

        if select == "1":   
            list1 = user.getInt_list()
            list2 = user.getInt_list("Enter second numbers separated by a space: ")
            result = func.sumInt_list(list1, list2)
            print("Summ of this 2 lists: ", *result)
            user.getEnter()

        elif select == "2": 
            list1 = user.getInt_list()
            result = set(filter(lambda j: j % 19 == 0 or j % 13 == 0, list1)) #set, чтобы не дублировался ответ, можно было вынести в функцию с пользовательским вводом кратности, но мне еще успеть надо до 12го все сдать
            print(*result)
            user.getEnter()

        elif select == "3": 
            list1 = user.getInt_list()  
            result = func.maxValuesWithReduceWhy(list1)
            print("Max value in list: ", result)
            user.getEnter()

        elif select == "0": 
            break 
            
        else:
            print("Error: Wrong choice. Please select the issue number from the list.")
    
Main()