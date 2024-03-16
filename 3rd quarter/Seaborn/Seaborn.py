import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np

"""
1)Скачать датасет с данными о клиентах по ссылке ниже и загрузить его
2)Создать матрицу корреляции для датасета Customers.csv
3)Создать базовую тепловую карту корреляции для Customers.csv
4)Создать треугольную тепловую карту корреляции для Customers.csv.
5)Построить точечную диаграмму с соотношением годового дохода (Annual Income ($)) к размеру семьи (Family Size).
"""

df = pd.read_csv('Customers.csv')

# Преобразование категориальных признаков
df_encoded = pd.get_dummies(df, columns=['Gender', 'Profession'])
df_corr = df_encoded.corr()

plt.figure('Анализ Customers',figsize=(10, 8), facecolor='#FFE4E1')
sb.heatmap(df_corr, cmap='bwr', annot=True, fmt=".2f")
plt.title('Корреляция с seaborn', loc='center')
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

# Маска для скрытия верхней части матрицы корреляции
mask = np.triu(np.ones_like(df_corr, dtype=bool))
plt.figure('Анализ Customers',figsize=(10, 8), facecolor='#FFE4E1')
sb.heatmap(df_corr, cmap='bwr', annot=True, fmt=".2f", mask=mask)
plt.title('Треугольная тепловая карта корреляции')
plt.tight_layout()
plt.show()

plt.figure('Анализ Customers',figsize=(10, 8), facecolor='#FFE4E1')
#sb.kdeplot(x='Annual Income ($)', y='Family Size', data=df, cmap='viridis', fill=True)
sb.scatterplot(x='Annual Income ($)', y='Family Size', data=df, alpha=0.5, color='blue')
plt.title('Соотношение годового дохода и размера семьи')
plt.xlabel('Годовой доход ($)')
plt.ylabel('Размер семьи')
plt.grid(True)
plt.show()

# здесь ради интереса посмотрел на уровни дохода мужчин и женщин по профессиям учитывая возраст, 
# а в датасете возраст у многих указан 0 1 и другие нереальные значения
plt.figure(figsize=(10, 6))

sb.scatterplot(x='Profession', y='Annual Income ($)', hue='Age', data=df, alpha=0.7, palette='viridis')
plt.title('Уровень дохода по профессиям, полу и возрасту')
plt.xlabel('Профессия')
plt.ylabel('Уровень дохода ($)')
plt.xticks(rotation=45)

plt.legend(title='Возраст')
plt.tight_layout()
plt.show()