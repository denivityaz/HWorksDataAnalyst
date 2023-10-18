import sys

def isBlack(row, col):
    return (row + col) % 2 == 0

while True:
    try:
        pos = input("Enter coordinates chess square through a point: ")  
        x, y = map(int, pos.split('.'))                                 #разделяем число

        if 0 < x < 9 and 0 < y < 9:                                 #фильтрация
            result = "black" if isBlack(x,y) else "white"
            print(f"This square is {result}")
            break
        else:
            print("The coordinates should be in the range from 1.1 to 8.8.")

    except Exception as e:
        print(f'Error:{e}')

sys.exit()

