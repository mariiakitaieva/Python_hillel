'''П 1, 2, 3.1, 3.2
1. Створи функцію, яка приймає параметри start та end, підсумовує всі цілі числа від значення start до величини end включно. Я
кщо користувач задасть перше число більше, ніж друге, поміняй їх місцями
'''
# task1

'''
def func_1(a, b):
    c = 0
    if a > b:
        for i in range(b, a + 1, 1):
            c += i
    else:
        for i in range(a, b + 1, 1):
            c += i
    return c


start = int(input("Enter the start digit: "))
end = int(input("Enter the end digit: "))
task1 = func_1(start, end)
print(task1)
# task2
# 2. Створи функцію, яка відображає число секунд у вигляді дні:години:хвилини:секунди. Функція може прийняти число як рядок так і як ціле число.
'''
'''
seconds = 92000
# /60 = minutes
# /3600 hours
# /86400
def time(seconds):
    days = int(seconds / 86400)
    houres = int(seconds % 86400/3600)
    minutes = int(seconds%86400%3600/60)
    seconds = int(seconds%86400%3600%60)
    return f'{days} : {houres} : {minutes} : {seconds}'


task2 = time(seconds)
print(task2)
'''
#task3 3. Створи функції, які обчислюють суму чисел у списку
#з for-циклом
#з while-циклом
list1 = [1, 2, 3, 4]


def summa_for(a):
    c = 0
    for i in a:
        c += i
    return c


task3_1 = summa_for(list1)
print(task3_1)



def summa_while(b):
    index = 0
    element = 0
    while index < len(b):
        element += b[index]
        index += 1
    return element


task3_2 = summa_while(list1)
print(task3_2)
