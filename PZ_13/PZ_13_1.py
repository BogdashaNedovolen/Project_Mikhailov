"""
В исходном текстовом файле (Dostoevsky.txt) найти все фамилии с инициалами
(например, А. Ф. Куманиной и т.п.)
"""

import re

with open('Dostoevsky.txt', encoding='utf-8') as file:
    text = file.read()

pattern = r'[А-Я]\.\s[А-Я]\.\s[А-Яа-я]+'
matches = re.findall(pattern, text)

print(f"Найдено фамилий с инициалами: {len(matches)}")
for m in matches:
    print(f"{m}")
