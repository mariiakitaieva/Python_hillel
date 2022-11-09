'''Створити послідовність інструкцій, яка друкує результат аналізу 2 наборів текстових даних з будь-яких символів, отриманих від користувача
Список літер, які присутні в обох наборах, регістр має значення ("A" та "a" - окремі літери). Літери не повторювати
Список цифр, які є в першому або в другому наборі, але не в обох. Цифри не повторювати'''


input_one = set(input("Enter whatever you want: "))
print(type(input_one), input_one)
input_two = set(input("Enter whatever you want: "))
print(type(input_two), input_two)
input_three = input_one.symmetric_difference(input_two)
print(input_three)
input_four = input_one.intersection(input_two)
print(input_four)
#
#exit_letters = set()
# exit_numbers =set()
# for element in input_three:
#     if element.isdigit():
#         exit_numbers.add(element)
# print(exit_numbers)
exit_numbers = set([element for element in input_three if element.isdigit()])
print(type(exit_numbers), exit_numbers)
exit_letters = set([element for element in input_four if element.isalpha()])
print(type(exit_letters), exit_letters)
