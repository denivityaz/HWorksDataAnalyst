from termcolor import colored       #косметичка

class UserInput:        #Методы для пользовательского ввода: строка, int и getEnter
    @staticmethod
    def getInt(prompt):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Error: Enter a valid integer!")

    @staticmethod
    def getStr(prompt):     
            value = input(prompt)
            return value

    @staticmethod
    def getEnter():
        input("\nPress Enter to continue...")

class MyFunc:
    
    def isPalindrome(self, txt):
        txt = [j.lower() for j in txt if j not in ('.!?, ')] #массив букв без знаков в нижнем регистре
        return  txt == txt[::-1]    #тру стори если совпадает при перевороте                  

    def CreateUpdate(self):
        user = UserInput()

        table = user.getStr("Enter table name: ")

        data = {                #пустой словарь, некая таблица
            'table': table,
            'persons': []
        }

        #вообще хотел с постгресом, но тогда вам для проверки придеться данные менять, неудобства 

        first_name = user.getStr("Enter first name: ")    
        last_name = user.getStr("Enter last name: ")
        middle_name = user.getStr("Enter middle name: ")
        age = user.getInt("Enter age: ")

        person = {                      #закидываем значения пользователя
            'first_name': first_name,
            'last_name': last_name,
            'middle_name': middle_name,
            'age': age
        }
        data['persons'].append(person)
        return data
    
    def Read(self, data):        #вывод "таблицы"
        t = data['table']
        p = data['persons']

        print(f"Data from the table {t}:")
        for i in p:
            result = f"\nFirst Name: {i['first_name']}, \nLast Name: {i['last_name']}, \nMiddle Name: {i['middle_name']}, \nAge: {i['age']}" 
            print(result)

    def maxValuesWithNotMax(self, str):
        try:
            numbers = list(map(int, str.split()))   #строку в список, и не пользуясь Max() пользуемся sort, условий про него не было
            numbers.sort()
            return numbers[-1]
        except:
            print ("\nError. Access only natural numbers separated by a space")
        

class Main:

    func = MyFunc()       #as ... для удобства
    user = UserInput()
 
    while True:
        print(colored("\nSelect a task:", "green", attrs=['bold']))
        print("1.Is poliandrome?") 
        print("2.Person description as like struct")              
        print("3.Max with not max()")   
        print(colored("0.Exit", "yellow", attrs=['bold'])) 
        
        select = user.getStr(colored("\nEnter num task:", "green", attrs=['bold']))  

        if select == "1":   
            txt = user.getStr('Pls enter text: ')
            result = '\nThis poliandrome' if func.isPalindrome(txt) else '\nThis not poliandrome'
            print(result)
            user.getEnter()

        elif select == "2": 
            data = func.CreateUpdate()
            func.Read(data)
            user.getEnter()

        elif select == "3": 
            list = user.getStr("Enter a list of numbers separated by a space:")  
            result = func.maxValuesWithNotMax(list)
            print('\n', result)
            user.getEnter()

        elif select == "0": 
            break 
            
        else:
            print("Error: Wrong choice. Please select the issue number from the list.")
    
Main()