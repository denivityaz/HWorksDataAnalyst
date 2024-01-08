import sys
import statistics

while True:
    try:
        num = input("Enter numbers separated by a space: ")
        
        #фильтрация ввода
        list = [float(j) for j in num.split() 
                      if j.strip().replace('.','',1).isdigit()]
        
        print(f"Ur values:\n {list}")
        print(f'MAX = {max(list)}')
        print(f'MIN = {min(list)}')
        print(f'AVG = {statistics.mean(list)}')

        break

    except Exception as e:
        print(f'Error:{e}')

sys.exit()