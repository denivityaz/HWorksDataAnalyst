import sys

def blckOrWht(i,j):    
    if i % 2 == 0 and j % 2 == 0: 
        return "black"
    else: 
        return "white" 

while True:
    try:
        num = float(input("Enter coordinates chess square through a point: "))
        x = int(num)
        y = int((num - x) * 10)

        if x < 9 and y < 9: 
            result = blckOrWht(x,y)  
            print(f'Ur square - {result}')
        else:
            print("Incorrect coordinates") 

        break

    except Exception as e:
        print(f'Error:{e}')

sys.exit()