'''Створи послідовність інструкцій, яка:
Отримує від користувача ім'я, де кожна літера може буте як маленького так і великого регістру, також можливі пробіли перед та після імені, наприклад  wiLLiAm
Очищує ім'я від знаків пробілу спочатку та наприкінці (знайти метод для рядків, який це робить)
Друкує привітання для цього імені у форматі перша літера велика, інші маленькі
Друкує кількість літер у імені
Друкує ім'я задом наперед'''

username = input("Please, enter your name: ")
print("Wazzup,", username.strip().title())
#print("Wazzup,", username.strip().capitalize())
print(len(username.strip()), "letters in the name")
print(username.strip().title()[::-1])
#print("Wazzup,", username.strip().capitalize()[::-1])