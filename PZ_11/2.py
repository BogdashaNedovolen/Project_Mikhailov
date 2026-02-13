"""
Из заданной строки отобразить только цифры. Использовать библиотеку string.
Строка - TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand
481 feet (147 metres) high.
"""

from string import digits

strr = 'TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand 481 feet (147 metres) high.'

result = ''.join(filter(lambda x: x in digits, strr))

print(result)
