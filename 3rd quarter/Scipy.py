'''
1. Задание на работу с распределениями:
   - Создайте объекты распределений для нормального и равномерного распределений.
   - Получите значения функции плотности вероятности (PDF) для каждого распределения при различных значениях.
   - Получите значения функции кумулятивной вероятности (CDF) для каждого распределения при различных значениях.
   - Сгенерируйте 10 случайных чисел из каждого распределения.

2. Задание на статистические тесты:
   - Проверьте гипотезу о среднем значении выборки с помощью одновыборочного t-теста.
     - Создайте выборку из 10 случайных чисел из Uniform(-1, 1).
     - Проверьте гипотезу о том, что среднее значение выборки равно 0.

'''



from scipy import stats
import numpy as np

# 1

dist_norm = stats.norm(loc=0, scale=1)
pdf_val_norm = dist_norm.pdf(0)
cdf_val_norm = dist_norm.cdf(1)
rnd_val_norm = dist_norm.rvs(size=10)

print("\nЗначения для нормального распределения:")
print("PDF(0) =", pdf_val_norm)
print("CDF(1) =", cdf_val_norm)
print("Случайные числа из нормального распределения:", rnd_val_norm)

dist_uniform = stats.uniform(loc=-1, scale=2)
pdf_val = dist_uniform.pdf(0)
cdf_val = dist_uniform.cdf(1)
rnd_val = dist_uniform.rvs(size=10)

print("\nЗначения для равномерного распределения:")
print("PDF(0) =", pdf_val)
print("CDF(1) =", cdf_val)
print("Случайные числа из равномерного распределения:", rnd_val)

# PDF (Probability Density Function) — функция плотности вероятности, 
# используется для оценки вероятности того, что случайная величина 
# примет определенное значение. Она помогает понять, как вероятность 
# распределена вдоль оси значений случайной величины.

# CDF (Cumulative Distribution Function) — функция кумулятивной 
# вероятности, используется для вычисления вероятности того, что 
# случайная величина будет меньше или равна определенному значению. 
# Она представляет собой сумму вероятностей до заданного значения, 
# включая это значение.

# 2

sample_1 = np.random.uniform(-1,1, size=5)
print(sample_1)
sample_2 = np.random.uniform(-1,1, size=5)
print(sample_2)
# sample_1 = np.arange(1,6)
# sample_2 = np.arange(1,6)

t_stat, p_val = stats.ttest_ind(sample_1,sample_2)

print("Результаты t-теста:")
print("Значение t-статистики:", t_stat)
print("Значение p-значения:", p_val)

# Тест возвращает два значения: t-статистику и p-значение. Если 
# p-значение меньше уровня значимости (обычно 0.05), то мы можем 
# отвергнуть нулевую гипотезу о том, что средние значения выборок 
# равны, и заключить, что существует статистически значимая разница 
# между средними значениями выборок.

