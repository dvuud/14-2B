# Задача 1
# Я думаю что исключения программисту нужны для того что бы сообщать программу о ошибках.
# Задача 2
name1 = "Davud"
try:
    print(neme1)
except NameError:
    print("Пишите правильно, будьте по внимательнее!")
try:    
    print(name1[6])
except IndexError:
    print("Такого индекса не существует!")
# Задача 3
# nums = input("Введите числа разделенные запятой: ")
# nums2 = set(nums.split(','))
# print(nums2)
# Задача 4
try:
    while True:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        sum_num = num1 + num2
        subraction = num1 - num2
        multiplication = num1 * num2 
        division = num1 / num2
        even_num = sum_num % 2 == 0
        print("Сумма", sum_num)
        print("Вычитание", subraction)
        print("Умножение", multiplication)
        print("Деление", division)
        if even_num:
            print("Сумма четное")
        else:
            print("Сумма нечетное")
        break 
except ValueError:
    print("Введите числа, а не цифры")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
    
    