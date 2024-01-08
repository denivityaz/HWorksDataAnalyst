from termcolor import colored       #косметика в консоли

class StrManipulation:
    def reverseWords(self, getStr):
        words = getStr.split()  #разбиваем слова
        result = words[::-1]    #переворачиваем
        return result

    def evenChar(self, getStr):
        result = getStr[::2]    #каждый 2 символ четного индекса 
        return result

    def powerNum(self, getStr, degree):
        numbers = list(map(int, getStr.split()))    #разбиваем строку и конвертируем каждое значение, все в массив
        result = [x ** degree for x in numbers]     #возведение в степень каждого эдемента массива
        return result

    def x2Char(self, getStr, symbol):
        result = getStr.replace(symbol, symbol * 2)     #функция замены, удвоение символа
        return result

    def countChar(self, getStr, charF, charS):
        countF = getStr.count(charF)        #функция подсчета в строке
        countS = getStr.count(charS)
        result = f'{charF}: {countF}, {charS}: {countS}.'
        return result

    def scanTextInBraces(self, getStr):
        result= []                  
        point = 0       #метка старта
        while True:
            point = getStr.find("(", point) #ищем старт
            if point == -1:
                break
            end = getStr.find(")", point)   #ищем конец
            if end == -1:
                break
            part = getStr[point + 1:end]    #импортируем символы в скобках
            result.append(part)
            point = end + 1
        return result

class UserInput:        #Методы для пользовательского ввода: строка по вашей просьбе, int и getEnter для удобства просмотра сделал
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
        

class Main:

    changeStr = StrManipulation()       #метод as ... для удобства
    user = UserInput()
 
    while True:
        print(colored("\nSelect a task:", "green", attrs=['bold']))
        print("1.Flip words in a line") 
        print("2.Output characters with even indexes")              
        print("3.Raise numbers to a power") 
        print("4.Double the characters in the text")    
        print("5.Count characters") 
        print("6.Extract substrings in parentheses")    
        print(colored("0.Exit", "red", attrs=['bold'])) 
        
        select = user.getStr(colored("\nEnter num task:", "green", attrs=['bold'])) #структура для пользования  

        if select == "1":   
            getStr = user.getStr("Enter the text:") 
            result = changeStr.reverseWords(getStr) 
            print(*result)  
            user.getEnter()

        elif select == "2": 
            getStr = user.getStr("Enter a string (at least 15 characters):")    
            result = changeStr.evenChar(getStr) 
            print(result)  
            user.getEnter()

        elif select == "3": 
            getStr = user.getStr("Enter a list of numbers separated by a space:")   
            n = user.getInt("Enter a natural number for exponentiation:")   
            result = changeStr.powerNum(getStr, n)  
            print(*result) 
            user.getEnter()

        elif select == "4": 
            getStr = user.getStr("Enter the text: ")    
            symbol = getStr("Enter symbol for x2: ")    
            result = changeStr.x2Char(getStr, symbol)   
            print(result)   
            user.getEnter()

        elif select == "5": 
            getStr = user.getStr("Enter text ") 
            char1 = getStr("Enter the character u want to count:")  
            char2 = getStr("Enter second symbol for count: ")   
            result = changeStr.countChar(getStr, char1, char2)  
            print(result)   
            user.getEnter()

        elif select == "6": 
            getStr = user.getStr("Enter text: ")    
            result = changeStr.scanTextInBraces(getStr) 
            for _ in result:    
                print(_)    
            user.getEnter()

        elif select == "0": 
            break 
            
        else:
            print("Error: Wrong choice. Please select the issue number from the list.")
    
Main()