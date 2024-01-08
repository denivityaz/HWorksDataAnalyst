import sys

def AVGList(list):
    sumList = sum(list)
    count = len(list)
    avg = sumList//count #or use func round in print result like {round(result)}
    return avg

while True:
    try:
        numValues = int(input('Enter num of values:'))
        listValues = []

        for i in range(numValues):
            j = int(input(f'Enter {i+1} value:'))
            listValues.append(j)

        result = AVGList(listValues)
        print(f'AVG of ur values = {result}')
        break

    except Exception as e:
        print(f'Error:{e}')

sys.exit()