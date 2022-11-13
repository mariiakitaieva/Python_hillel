'''Відтвори ASCII таблицю у вигляді словника, обов'язкові умови:
Використай генератор словника
Використай вбудовану функцію chr()'''
ASCII_dict = {element: chr(element) for element in range(32,128)}
print(type(ASCII_dict), ASCII_dict)

'''Реалізувати послідовність операцій яка
Приймає від користувача строку тільки з літер, без пробілів
Приймає від користувача пароль у вигляді цілого числа
Створює словник шифра метода одноалфавітної підстановки на базі пароля. Тобто пароль - число на яке треба збільшити порядковий номер літери у алфавіті 
Шифрує строку на базі словника шифра. Приклад
Звичайний порядок "a" - 1, "b" - 2, ..., "z" - 26 -> словник "a"="a", "b"="b", ..., "z"="z"
З паролем у 4 порядок стає "a" - 5, "b" - 6, ..., "z" - 4 -> словник "a"="e", "b"="f", ..., "z"="d"
Рядок "hello" перетворюється на "lipps"
Друкує зашифровану строку'''
try:
    entrance = input("enter string without space: ").lower()
    if " " in entrance:
        entrance = input("You entered \'space\'. Please, enter string without space: ").lower()
except:
    print(entrance)
print(entrance)
try:
    password = int(input("please, enter only integer number: "));
    if password%26 == 0:
        password = input("you entered invalid value. please, enter only integer number");
except:
    print(password)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
dict2 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
letter = 'hell'
dict3 = {}
for key, value in dict2.items():
    for ix, exc in dict1.items():
        if ix == dict2[key]:
            if dict1[ix]+password > 26:
                dict3[(dict1[ix]+password) % 26] = dict2[key]
            else:
                dict3[dict1[ix]+password] = dict2[key]
print(dict3)

for el in letter:
    for key, value in dict3.items():
        if dict3[key] == el:
            print(dict2[key], end="")

