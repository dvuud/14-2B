# # Задача 1
# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)
# # Задача 2
# numbers = {'num_1' : 1, 'num_2' : 2, 'num_3' : 3, 'num_100' : 100}
# for key in numbers:
#     numbers[key] *= 5
#     print(numbers)
# # Задача 3
# student = {'name' : 'Askhat', 'age' : 17}
# student['age'] *= 2
# print(student)
# # Задача 4
# student = {'name' : 'Askhat', 'age' : 17, 'color' : 'white'}
# student['age'] = 16
# print(student)
# # Задача 5
# student = {'name' : 'Askhat', 'age' : '17'}
# del student['age']
# print(student)
# # Задача 6
# student = {'name' : 'Askhat'}
# student.setdefault('adress' , 'Западный Анар')
# print(student)
# Задача 7
# def chat_bot(question=None):
#     while True:
#         if not question:
#             print("Как классно, когда ты молчишь. Продолжай в том же духе")
#         elif question.isupper():
#             print("Успокойся")
#         elif "?" in question:
#             print("Конечно")
#         else:
#             print("Ну и что")
#         question = input("Ваш вопрос: ")
# chat_bot()
# Задача 8
# def reduction(phrase1):
#     words = phrase1.split()
#     reduction2 = [word[0].upper() for word in words if word[0].isalpha()]
#     return ''.join(reduction2)
# phrase = input("Введите слово ")
# result = reduction(phrase)
# print(result)
# reduction
# Задача 9
def count_word(phrase):
    words = repr.findall(r'\b\w+\b', phrase.lower())
    
    word_counts = {}
    
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    return word_counts

phrase = "Money, money, money, it's always sunny, in the richmen's world"
result = count_word(phrase)

for word, count in result.items():
    print(f"{word}: {count}")
# Задача 10
# def is_isogram(wordd):
#     word = wordd.lower()
#     return len(wordd) == len(set(wordd))
# result1 = is_isogram(input("Введите слово: "))
# print(result)
# result2 = is_isogram(input("Введите второе слово: "))
# print(result2)
# is_isogram
# # Задача 11
# def sum_and_reversed(n):
#     reversed_n = int(str(n)[::-1])
#     result = n + reversed_n
#     return result
# n = int(input("Введите число: "))
# result = sum_and_reversed(n)
# print(result)
# sum_and_reversed