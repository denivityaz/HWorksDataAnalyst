import pandas as pd
import seaborn as sb
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

print(dataset.head(5))

plt.figure('salaryes', figsize=(8,10))
sb.barplot(
    dataset,
    y='job_title', 
    x='salary', 
    palette='bright',
    hue='job_title')
plt.tight_layout()
plt.show()


