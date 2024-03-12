import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# 1
x = np.linspace(-10,10)
y = 0.1 * x**2 - x

plt.figure('1',facecolor='#F0F0F0')
plt.plot(x,y)
plt.title('График y = 0.1 * x^2 - x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()


# 2
x = np.linspace(-2*np.pi, 2*np.pi, 400)
y1 = np.sin(0.2 * x**2)
y2 = np.cos(0.2 * x**2)


plt.figure('2',facecolor='#F0F0F0')
f, = plt.plot(x, y1)
line2, = plt.plot(x, y2)
plt.grid(True)
plt.legend([f, line2], ['y = sin(0.2x^2)', 'y = cos(0.2x^2)'])
plt.show()

# 3

marks_1_quarter = np.random.randint(2,6,size=25)
marks_2_quarter = np.random.randint(2,6,size=25)

# подсчет оценок, забыл как это делается, вроде со словарем, крч нашел в np это
marks_count_1_quarter = dict(zip(*np.unique(marks_1_quarter, return_counts=True))) 
marks_count_2_quarter = dict(zip(*np.unique(marks_2_quarter, return_counts=True)))
print("Оценки 1 и 2 четверть"'\n',marks_count_1_quarter,'\n', marks_count_2_quarter)

t_stat, p_val = stats.ttest_ind(marks_1_quarter,marks_2_quarter)
print("Результаты t-теста:")
print("Значение t-статистики:", t_stat)
print("Значение p-значения:", p_val)

if p_val < 0.05:
    print("Средние значения различны")
else:
    print("Средние значения схожи")


fig, axes = plt.subplots(1,2, figsize=(15, 5), facecolor='#F0F0F0')

axes[0].hist(marks_1_quarter, edgecolor='white', color='green')
axes[0].set_title('Первая четверть')
axes[0].set_xlabel('Оценка')
axes[0].set_ylabel('Частота')
axes[0].set_xlim(1, 5)
axes[0].set_ylim(0, 25)

axes[1].hist(marks_2_quarter, edgecolor='white', color='orange')
axes[1].set_title('Вторая четверть')
axes[1].set_xlim(1, 5)
axes[1].set_ylim(0, 25) # надо было в переменные это делать, но уже поздно
fig.suptitle('Сравнение оценок за четверти 25 учеников, так интереснее')
plt.tight_layout() # - разметка авто
plt.show()

# 4
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
plt.show()
