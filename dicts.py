'''Відтвори ASCII таблицю у вигляді словника, обов'язкові умови:
Використай генератор словника
Використай вбудовану функцію chr()'''
ASCII_dict = {element: chr(element) for element in range(32,128)}
print(type(ASCII_dict), ASCII_dict)

