import matplotlib.pyplot as plt
import numpy as np

'''
Нарисуйте гистограмму, отображающую распределение оценок учеников в классе по предмету "Математика". 
Значения оценок: 2, 3, 3, 2, 5, 5, 3, 4, 5, 4. Установите подписи для осей и название гистограммы.

Создайте двумерный массив размером 4x4, заполненный случайными числами от 1 до 10 
с использованием функции numpy.random.randint().

Постройте круговую диаграмму, отображающую соотношение количества мальчиков и девочек в классе. 
Предположим, что в классе 32 человека, из которых 15 мальчиков и 17 девочек. Установите подписи для секторов диаграммы.

'''
# Оценки учеников по математике
marks = np.random.randint(2,6, size=10)
print(dict(zip(*np.unique(marks, return_counts=True))))
plt.figure('1', figsize=(5,5),facecolor='#F0F0F0')
plt.hist(marks, edgecolor='white', color="#FFA073")
plt.xlabel('Оценка')
plt.ylabel('Частота')
plt.title('Оценки учеников по математике')
plt.ylim(0, 10)
plt.xlim(1,6)
plt.show()

# arr random
arr_rnd = np.random.randint(1,11, size=(4,4))
print(arr_rnd)

boys_count = np.random.randint(1, 16)
girls_count = 20 - boys_count
print(f'Мальчики: {boys_count}, девочки: {girls_count}')
# в переменные
sizes = [boys_count, girls_count]
labels = ['Мальчики', 'Девочки']
colors = ['lightblue', 'pink']
explode = (0.1, 0)  # границы

plt.figure('4', figsize=(5,5),facecolor='#F0F0F0')
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
         autopct='%1.1f%%', shadow=True, startangle=200)
plt.title('Соотношение мальчиков и девочек в классе (rnd)')
plt.axis('equal')  # круг
plt.tight_layout()
plt.show()
