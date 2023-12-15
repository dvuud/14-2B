# # Задача 1
# password = input('password: ')
# if password =="davudB":
#     print("Password is correct. You are welcome")
# else:
#     print("Password is incorrect. Please try again")
# # Задача 2
# temperature = float(input("Введите температуру за окном: "))
# if temperature < -30:
#     print("Там так холодно. Лучше дома сиди!")
# elif -30 <= temperature < 0:
#     print("Холодновато. Оденься по теплее!")
# elif 0 <= temperature < 15:
#     print("Прохладно. Куртку накинь!")
# elif 15 <= temperature < 30:
#     print("Тепло. Иди погуляй в парке!")
# elif 30 <= temperature < 50:
#     print("Ого, как жарко!")
# elif temperature >= 50:
#     print("Там такая жара, лучше дома сиди!")
# else:
    # print("Ошибка!")
# Задача 3 
hour = float(input("Введите текущий час: "))
if 0 <= hour <= 6:
    print("Ночь")
elif 7 <= hour <= 12:
    print("Утро")
elif 13 <= hour <= 18:
    print("День")
elif 18 <= hour <= 23:
    print("Вечер")
else:
    print("Ошибка")
# Доп задача 4 
student = float(input("Ваша оценка: "))
if student >= 90:
    print("Отлично")
elif 80 <= student < 90:
    print("Хорошо")
elif 70 <= student < 80:
    print("Удовлетворительно")
elif 60 <= student < 70:
    print("Неудовлетворительно")
else:
    print("Студент должен пересдать экзамен")
 
    

 
    
