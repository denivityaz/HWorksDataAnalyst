import sys

def evenOrNot(j):       #четное или нет
    return j % 2 == 0

while True:
    try:
        num = int(input("Enter ur num: "))
        result = "even" if evenOrNot(num) else "odd"
        print(f"Ur number {num} - {result}")
        break

    except Exception as e:
        print(f"Error:{e}")

sys.exit()