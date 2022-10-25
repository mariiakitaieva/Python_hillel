'''Створи послідовність інструкцій, яка:
Отримує від користувача його ім'я, виводить на друк привітання для цього імені, використовуючи f-string
Отримує від користувача дрібне число, виводить на друк:
Отримане число
Ціле число (число без дрібної частини)
4ту ступінь цілого числа
Корінь цілого числа
Залишок від ділення цілого числа на 2'''

username=input("Please, enter your name: ")
print(f"Wazzap, {username}")
number=float(input("Please, enter fractional number: "))
print(number)
print(int(number))
print(int(number)**4)
print(int(number)**0.5)
print(int(number)%2)
