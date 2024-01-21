import math

# 1
result_1 = math.factorial(3)

print("1:\nКоличество способов выстроить 3 машины в очередь на обслуживание\n", result_1, "способов")

# 2
# Формула C(n, k) = n! / (k!(n-k)!)
result_2 = math.factorial(5) // (math.factorial(5) * math.factorial(0))

print("2:\nКоличество способов раздать спортивные номера 1-5 пяти хоккеистам\n", result_2, "способ")

# 3
result_3a = math.factorial(6)
result_3b = math.factorial(8)
result_3c = math.factorial(10)

print("3:\nКоличество различных последовательностей выхода лыжников на старт") 
print("   а) Результат:", result_3a, "способов")
print("   б) Результат:", result_3b, "способов")
print("   в) Результат:", result_3c, "способов")
print("   д) Результат: 1 (где k - 1)")

# 4

print("4:\nВероятность того, что фамилии будут записаны:")
print("   а) В алфавитном порядке: 1/10!")
print("   б) Обратном алфавитному: 1/10!")

# 5
# Формула: C(n, k) = n! / (k!(n-k)!)
result_5 = math.factorial(7) // (math.factorial(3) * math.factorial(7-3))
print("5:\nКоличество способов выбрать 3 газеты из 7\n", result_5, "способов")



