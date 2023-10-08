import sys

while True:
    try:
        print('Enter your float number with ".":')
        mainNum=float(input())
        print('Enter num of numbers after the decimal point that u want to leave:')
        numAfterPoint = int(input())
        result = round(mainNum,numAfterPoint)
        print(result)
        break
    except Exception as e:
        print(f'Ошибка:{e}')

sys.exit()