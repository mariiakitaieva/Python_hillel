# 1. Виправ помилку у порівнянні 3 ! 5, нічого не видаляй
3!=5
# 2. Наведи усі комбінації арифметичних порівнянь для 5 _ 5, при яких результат буде True
comparison: bool = 5 == 5 and 5>=5 and 5<=5
print(comparison)
# 3. Наведи 5 комбінацій з логічних операторів (or, and, not) та дужок, так щоб результат виразу True _ True _ False був True
guess_what: bool= (True and True or False) and (True or True or False) and (True and True and not False) and (True or True or not False) and (True or not  True and not False)
print(guess_what)
# 4. Отримай логічні значення для пари аргументів (bool()) та порівняй (==) їх між собою. З'ясуй чому результат саме такий
# None, 7
who_knows_1: bool = None == 7 #false
print(who_knows_1)
# Пуста строка, вираз 10 - 1
who_knows_2: bool = () == 10-1 #false
print(who_knows_2)
# True or False, результат роботи функції print() з будь-яким текстом
func_1 = print("Hello, World")
who_knows_3: bool = func_1  == "Hello, World" #false
print(who_knows_3)
# Результат роботи функції type() від None, результат функції id() від None
who_knows_4: bool = type(None) == id(None) #false
print(who_knows_4)