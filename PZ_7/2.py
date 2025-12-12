"""
Дана строка полного имени файла. 
Выделить из этой строки название последнего каталога. 
Если файл содержится в корневом каталоге, то вывести символ "\"
"""

#string = r'C:\folder\folder1\file.txt'
#string = r'C:\file.txt'

string = str(input('Введите путь до файла: '))
while '\\' not in string or ':' not in string:
    try:
        print('Ошибка: это не путь')
        string = str(input('Введите путь до файла: '))
    except Exception as e:
        print('Ошибка: это не путь')
        string = str(input('Введите путь до файла: '))


string_list = string.split('\\')
print(f'Сырая строка - {string_list}')

if len(string_list) <= 2:
    catalog = '\\'
    print(f'Файл в корневом каталоге, путь - {catalog}')
else:
    print(f'Последний каталог - {string_list[-2]}')
