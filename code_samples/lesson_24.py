"""
Lesson 24
22.11.2023
Повторение основных моментов связанных с Git и Github
Поговорили про:
- переключение между коммитами
- сравнение коммитов
- откат коммитов
- сброс коммитов
- stash и shelve

Ветки:
- создание веток
- переключение между ветками
- слияние веток

"""
# Как работает ALL и ANY в этом декораторе?
# Any - возвращает True, если хотя бы один элемент истинный
# All - возвращает True, если все элементы истинные

password = '12345678Aa'

# Вариант на флаге и цикле. Вся строка состоит из цифр целиком.
flag = True

for char in password:
    if char.isdigit():
        continue
    else:
        flag = False
        break

if flag:
    print('Все символы строки являются цифрами')
else:
    print('В строке есть не цифровые символы')

# Вариант с all. Хотим убедится что все символы строки являются цифрами.
print(all(map(str.isdigit, password)))

# Простые примеры с any и all

print(any([True, False, False]))
print(any([False, False, False]))
print(any([False, False, True]))

print(all([True, False, False]))
print(all([True, True, True]))
print(all([False, False, False]))

#  более сложный пример с any и all
products = ['apple', 'banana', 'orange', 'pineapple', 'mango']

# В списке все элементы начинаются с буквы 'a'
# В списке есть хотя бы один элемент, который начинается с буквы 'a'

print(all(map(lambda x: x.startswith('a'), products)))
print(any(map(lambda x: x.startswith('a'), products)))



