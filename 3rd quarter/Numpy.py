'''
Создайте массив NumPy из чисел от 1 до 5.
Найдите сумму всех элементов этого массива.
Создайте 3x3 массив со случайными числами от 1 до 10.
Найдите минимальное и максимальное значения в каждой строке этого массива.
Создайте массив из 10 случайных чисел от -1 до 1.
Найдите среднее значение и стандартное отклонение этого массива.
Создайте 4x4 массив, заполненный нулями.
Замените все элементы второго столбца массива на 1.
Создайте массив от 0 до 99.
Преобразуйте этот массив в 10x10 массив.
'''

import numpy as np

arr = np.arange(1,6)
print (*arr, 'and sum => ',np.sum(arr),'\n')

random_arr_3_3 = np.random.randint(1,10, size=(3,3))
print(random_arr_3_3)

for i in range(random_arr_3_3.shape[0]): #shape - размер массива - rows cols
    min = np.min(random_arr_3_3[i])
    max = np.max(random_arr_3_3[i])
    print(f'Строка {i+1}, минимум - {min}, максимум - {max}')

arr_uniform = np.random.uniform(-1,1, size=10)
print('\n',*arr_uniform)

print(f'Среднее зачение - {round(np.mean(arr_uniform), 5)}, среднее отклонение - {round(np.std(arr_uniform), 5)}\n')

arr_zeros = np.zeros((4,4))
print(arr_zeros,'\n')

arr_zeros[:,1] = 1
print(arr_zeros)

arr_99 = np.arange(100)
print(arr_99)

arr_99_v2 = np.reshape(arr_99, (10,10))
print(arr_99_v2)