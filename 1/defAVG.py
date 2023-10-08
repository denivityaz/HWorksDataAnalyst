import sys

def AVGList(list):
    sumList = sum(list)
    count = len(list)
    avg = sumList//count
    return avg

while True:
    try:
        print('Enter num of values:')
        numValues = int(input())
        listValues = []

        for i in range(numValues):
            j = int(input(f'Enter {i+1} value:'))
            listValues.append(j)

        result = AVGList(listValues)
        print(f'AVG of ur values = {result}')
        break

    except Exception as e:
        print(f'РћС€РёР±РєР°:{e}')

sys.exit()