# Задача 1
for i in range(5):
    print(f"Строка {i + 1}: 0")
# Задача 2
num_list = list(range(1, 101))
print(num_list)
# Задача 3
for num in range(1, 498):
    if num % 2 == 0:
     print(num, "Четный")
else:
    print(num, "Нечетный")
# Задача 4
my_list = list(range(1, 1001))
print(min(my_list))
print(max(my_list))
print(sum(my_list))
# Задача 5
zero_list = [0] * 100
print(zero_list)
# Задача 6
while True:
    age = int(input("Введите свой возраст "))
    if age >= 18:
        print("Доступ разрешен")
        break
    else:
        print("Извините пользование данным ресурсом только с 18ти лет")
        continue
    