'''Створити послідовність інструкцій, яка друкує результат аналізу 2 наборів текстових даних з будь-яких символів, отриманих від користувача
Список літер, які присутні в обох наборах, регістр має значення ("A" та "a" - окремі літери). Літери не повторювати
Список цифр, які є в першому або в другому наборі, але не в обох. Цифри не повторювати'''


input_one = set(input("Enter whatever you want: "))
#print(type(input_one), input_one)
input_two = set(input("Enter whatever you want: "))
#print(type(input_two), input_two)
#exit_letters = set()
# exit_numbers =set()
# for element in input_three:
#     if element.isdigit():
#         exit_numbers.add(element)
# print(exit_numbers)
exit_numbers = set([element for element in input_one.symmetric_difference(input_two) if element.isdigit()])
print(type(exit_numbers), exit_numbers)
exit_letters = set([element for element in input_one.intersection(input_two) if element.isalpha()])
print(type(exit_letters), exit_letters)
'''Знайди та ознайомся з операторами |=, &=, -=, ^=, та методами які відповідають цим операторам. 
Наведи по 1 прикладу для кожного оператора, використовуй 3 множини одночасно у якості операндів '''
set_one = set(1, 2, 3, 11, 22)
set_two = set(11, 4, 5)
set_three = set(11, 8, 9)
