import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

#Загрузите датасет и выведите его содержимое.

df = pd.read_csv('2018.csv')
# print(df.shape)
# print(df.info())
# print(df.head)
# """
# Столбцы: Общий рейтинг,страна или регион, Оценка,ВВП на душу населения, 
# Социальная поддержка, ожидаемая продолжительность здоровой жизни, 
# Свобода выбора в жизни, Щедрость, восприятие коррупции
# """

# # Необходимо вывести основные статистические показатели по датасету  
# print('\nОсновные статиcтические данные\n',df.describe())


# # и построить гистограмму по столбцу "Social support" (Социальная поддержка)
# plt.figure('1',figsize=(10, 6))
# sns.set_style("dark")
# sns.histplot(data=df, x='Social support', bins=10, alpha=0.7)
# plt.title('Cоциальная поддержка')
# plt.xlabel('Уровень социальной поддержки')
# plt.ylabel('Частота')
# plt.grid(True)
# plt.show()


# # Необходимо расчитать корреляцию, постройте тепловую карту корреляции

# # Дропаем столбец "Country or region"
# only_num_df = df.drop(columns=["Country or region"]) # это явно проще, чем указывать столбцы
# correlation_matrix = only_num_df.corr()

# plt.figure('2',figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=1.5)
# plt.title('Матрица корреляции')
# plt.tight_layout()
# plt.show()

# # Необходимо построить линейный график между столбцами Score (рекорд) 
# # и Country or region (страна или регион) и вывести его.

# # Сортировка
df_sorted = df.sort_values(by='Score', ascending=False)  # ascending=False - начиная с максимального

# plt.figure('3',figsize=(16, 8))
# sns.set_style("darkgrid")
# plt.plot( df_sorted["Country or region"], df_sorted["Score"], color='skyblue')
# plt.ylabel('Score')
# plt.xlabel('Страна или регион')
# plt.title('Очки уровня "счастья" по странам или регионам')
# plt.xticks(rotation=90, fontsize=8)
# plt.gca().invert_xaxis()  # инверсия для читаемости
# plt.tight_layout()
# plt.show()

# Необходимо получить первые 10 стран с максимальным уровнем счастья (Score)
df_top_10 = df_sorted.head(10)
print(df_top_10)
# и построить barplot по ним

my_palette = sns.color_palette("Blues_r", (len(df_top_10)+5))

plt.figure('4',figsize=(12, 8))
sns.set_style('ticks')
sns.barplot(data=df_top_10, x='Country or region', y='Score', hue='Country or region', legend=False, palette=my_palette).set_ylim(6, 8) # установка пределов оси Y
plt.title('Очки уровня "счастья" по топ 10 странам')
plt.xlabel('Страна или регион')
plt.xticks(rotation=90, fontsize=12)
plt.gca().invert_xaxis()
plt.tight_layout()
plt.show()
