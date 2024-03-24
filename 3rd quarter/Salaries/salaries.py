import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''
1) Скачать датасет Data Science Salaries 2023, доступный по ссылке 
https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023 
Импортировать необходимые для построения графиков библиотеки и загрузить датасет. 
Вывести первые 5 строк датасета.
2) Составить barplot, с помощью которого можно изучить уровень дохода (в долларах) в зависимости от профессии.
3) Построить линейную диаграмму по всем стобцам датафрейма
4) Cоздать диаграмму рассеяния где по оси X будет находится зарплата в долларах и по оси y должность. 
Привести график в такой вид, что бы его было удобно читать.
5) Построить линейный график зависимости уровня зарплаты специалистов от региона.
'''
dataset = pd.read_csv('ds_salaries.csv')

# 1. здесь первый график без sns и отсортирован для удобства с агрегацией, во 2м графике sns делает среднее сам, но не отсортирован
print(dataset.head(5))

plt.figure('1) Зарплаты о которых все мечтают', figsize=(10,10))
done_set = dataset.groupby('job_title')['salary_in_usd'].mean().sort_values().plot(kind='barh')
plt.ylabel('Проффессия', fontsize=10)
plt.xlabel('Зарплата в год?')
#plt.yticks(rotation=0, ha='right')
plt.grid(axis='x', linestyle='-')
plt.tight_layout()
done_set.tick_params(axis='y',labelsize=6)
plt.show()

plt.figure('1.2)',figsize=(12, 6))
sns.barplot(x='job_title', y='salary_in_usd', data=dataset, errorbar=None)
plt.title('Средняя зарплата по профессии с seaborn')
plt.ylabel('Средняя зарплата в USD')
plt.xlabel('Профессия')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# не совсем понял, что значит линейный график по всем столбцам, но вот

plt.figure('2)',figsize=(16, 10))

plt.subplot(3, 2, 1)
sns.lineplot(x='work_year', y='salary_in_usd', data=dataset)
plt.title('Зарплата от года работы')

plt.subplot(3, 2, 2)
sns.lineplot(x='experience_level', y='salary_in_usd', data=dataset)
plt.title('Зарплата от уровня опыта')

plt.subplot(3, 2, 3)
sns.lineplot(x='employment_type', y='salary_in_usd', data=dataset)
plt.title('Зарплата от типа занятости')

plt.subplot(3, 2, 4)
sns.lineplot(x='employee_residence', y='salary_in_usd', data=dataset)
plt.xticks(rotation=90, fontsize=6)
plt.title('Зарплата от места проживания')

plt.subplot(3, 2, 5)
sns.lineplot(x='remote_ratio', y='salary_in_usd', data=dataset)
plt.title('Зарплата от удаленной работы')

plt.tight_layout()
plt.show()



plt.figure('3)', figsize=(16, 8))
sns.scatterplot(x='job_title', y='salary_in_usd', data=dataset, hue='experience_level', s=50)
plt.title('Зависимость зарплаты от профессии')
plt.xlabel('Профессия')
plt.ylabel('Зарплата в USD')
plt.xticks(rotation=90)
plt.legend(title='Уровень опыта')
plt.tight_layout()
plt.show()


plt.figure('4) Зарплата от региона', figsize=(15,8))
sns.lineplot(x='employee_residence', y='salary_in_usd', data=dataset, hue='experience_level')
plt.xticks(rotation=90, fontsize=8)
plt.title('Зарплата от региона')
plt.legend(title='Уровень специалиста')
plt.xlabel('Регион')
plt.ylabel('Зарплата')
plt.show()