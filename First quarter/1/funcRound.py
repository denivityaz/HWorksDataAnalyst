import sys

while True:
    try:
        mainNum=float(input('Enter your float number with ".":'))
        numAfterPoint = int(input('Enter num of numbers after the decimal point that u want to leave: '))
        result = round(mainNum,numAfterPoint)
        print(result)
        break
    except Exception as e:
        print(f'Error: {e}')

sys.exit()