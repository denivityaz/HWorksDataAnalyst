import sys

def numsMultiples(num,mult):        #кратные числа до введенного значения
    for i in range(mult, num, mult):
        print (i)

while True:
    try:
        num = int(input('Enter num:'))
        mult = int(input(
            'Enter the multiplicity of nums you want to see within the previously entered number:'))
        numsMultiples(num,mult)
        break

    except Exception as e:
        print(f'Error: {e}')

sys.exit()