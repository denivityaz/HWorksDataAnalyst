from termcolor import colored       #косметика

class StrManipulation:
    
    def countRepeatWord(self, txt):
        keyCount = {} #хэшмап для подсчета
        result = 0
        
        for word in txt:          #считаем сколько раз слово повторяется в тексте
            if word in keyCount:
                keyCount[word] += 1 
            else:
                keyCount[word] = 1

        result = sum(value for value in keyCount.values() if value > 1)    #сумма повторов толко для повторяющихся слов, если я правильно понял, это и просили
        return keyCount, result

    def repeatWordInLists(self, list):
        result = set.intersection(*list)    #находим пересечение всех множеств с помощью метода intersection
        return result                       #в хабре видел что с пандас пересечения можно реализовать, но потом как-нибудь


    def upUrChar(self, txt):
        txt = txt.strip()     #убираем пробелы в начале и конце строки
        result = ''
        nextUp = True      #метка для upper()

        for _ in txt:
            if _.isalpha():      #фильтрация букв
                if nextUp:               #наша метка изначально трушная, 
                    result += _.upper()  #поэтому первая буква в верхний регистр закидывается
                    nextUp = False
                else:
                    result += _
            elif _ in ".!?":     #метка тру, после наших значений в тексте
                result += _
                nextUp = True
            else:
                result += _
        return result

    def isAnagramm(self, w1, w2):   
        w1 = w1.replace(" ", "").lower()    #удаляем пробелы, все к нижнему регистру
        w2 = w2.replace(" ", "").lower()
        if len(w1) != len(w2):      #если длина строки разная, сразу возвращаем, возможно так быстрее, если взять во внимание редкость анаграмм
            return False
        else:
            return set(w1) == set(w2)   #сравниваем множества


class UserInput:        #Методы для пользовательского ввода: строка, int и getEnter для удобства просмотра
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

    string = StrManipulation()       #as ... для удобства
    user = UserInput()
 
    while True:
        print(colored("\nSelect a task:", "green", attrs=['bold']))
        print("1.The number of words that are repeated") 
        print("2.Down with punctuation, confusing the computer thinks")              
        print("3.An anagram yes?") 
        print("4.Intersections")       
        print(colored("0.Exit", "yellow", attrs=['bold'])) 
        
        select = user.getStr(colored("\nEnter num task:", "green", attrs=['bold']))  

        if select == "1":   
            n = user.getInt("Enter the number of words: ")
            listWords = [input() for _ in range(n)]

            count, result = string.countRepeatWord(listWords)
            print("Ur values: ")
            for key, value in count.items():
                print(f'{key}: {value}')
            print("The sum of repeated words: ", result)
            user.getEnter()

        elif select == "4": 

            n = user.getInt("Enter the number of lists: ")
            sumLists = []

            for i in range(n):
                _ = user.getStr(f"Enter the items for the list {i + 1} separated by a space: ")
                list = set(_.split())
                sumLists.append(list)
            
            result = string.repeatWordInLists(sumLists)
            if len(result) == 0: 
                print("\nNo intersection")
            else:
                print("\nItems that are in all lists:", *result)
            user.getEnter()

        elif select == "2": 
            txt = user.getStr("Enter text: ")
            result = string.upUrChar(txt)
            print("Ur text with upper symbols:\n",result)
            user.getEnter()

        elif select == "3": 
            w1 = user.getStr("Enter first word: ")
            w2 = user.getStr("Enter second word: ")
            if string.isAnagramm(w1, w2): 
                print ("\nThe strings are an anagram") 
            else: print("\nStrings are not an anagram")
            user.getEnter()

        elif select == "0": 
            break 
            
        else:
            print("Error: Wrong choice. Please select the issue number from the list.")
    
Main()