import random

def random_choice(list):
    return random.choice(list)
language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]
result = random.choice(language)
r = open('random.txt', 'w')
r.write(result)
r.close
# Задача 2 
text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
has been the industry's standard dummy text ever since the 1500s, when an unknown
printer took a galley of type and scrambled it to make a type specimen book. It has
survived not only five centuries, but also the leap into electronic typesetting, remaining
essentially unchanged. It was popularized in the 1960s with the release of Letraset
sheets containing Lorem Ipsum passages, and more recently with desktop publishing
software like Aldus PageMaker including versions of Lorem Ipsum.
"""
f = open('text.txt', 'w')
f.write(text)
f.close
# 2 Способ
with open('text.txt', 'w') as file:
    file.write(text)
# Задача 3
with open('wikipedia.txt', 'w') as target_file:
    target_file.write(text)
