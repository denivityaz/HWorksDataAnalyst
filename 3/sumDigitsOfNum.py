import sys

while True:
    try:
        num = input('Enter num:')
        numList = list(num)
        num_with_signs = ' + '.join(numList)
        total = sum((map(int,numList)))     #преобразовывает и суммирует 

        print(num_with_signs,' = ', total)
        break

    except Exception as e:
        print(f'Error: {e}')

sys.exit()


# то,что сверху, в голове созрело, снизу - нашел в интернете и подправил
# что правильнее не знаю, наверное то, что менее ресурсоемкое

num = int(input())
sum = 0
digits = []

while num != 0:
    digit = num % 10
    digits.append(str(digit))
    sum += digit
    num = num // 10

formatted_output = ' + '.join(digits[::-1])     # обратно выводим цифры и объединяем их с плюсами
print(formatted_output, ' = ', sum)

