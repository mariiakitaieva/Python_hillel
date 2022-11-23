#Створи  функцію, яка обчислюють суму чисел у списку з рекурсією
list2 = [1, 2, 3, 4, 5]
def summa(number, index=0):
    if index >= len(number):
        return 0
    else:
        return number[index] + summa(number, index+1)

task3_3 = summa(list2)
print(task3_3)

# def factorial(n):
#     if n == 0:
#         return 1
#
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(5))

#Створи функцію яка обчислює числа Фібоначчі. Функція повертає число з послідовності за порядковим номером
#f1=0 f2=1 fn = fn-1 + fn-2

def fibonachi(n):
    if n > 2:
        return (fibonachi(n - 1) + fibonachi(n - 2))
    else:
        return 1

fboo = fibonachi(6)
print(fboo)