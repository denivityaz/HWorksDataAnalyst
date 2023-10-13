import sys

def evenOrNot(j):       #четное или нет
    if j % 2 == 0: return "even"
    else: return "odd" 

while True:
    try:
        num = float(input('Enter ur num:'))
        if num.is_integer():                #сокращаем число, если оно int
            num = round(num)
          
        result = evenOrNot(num)
        print(f'Ur number {num} - {result}')
        break

    except Exception as e:
        print(f'Error:{e}')

sys.exit()