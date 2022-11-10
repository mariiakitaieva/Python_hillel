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

set_one = {1, 2, 3, 11, 22}
set_two = {11, 4, 5}
set_three = {11, 8, 9}
#set_four = set_one | set_two | set_three
#print(set_four)
set_one |= set_two | set_three #union
print(set_one)


set_uno = {1, 2, 3, 11, 22}
set_dos = {11, 4, 5}
set_treis = {11, 8, 9}
set_uno &= set_dos & set_treis
print(set_uno)   #intersection


set_un = {1, 2, 3, 11, 22}   #Результатом разности - является множество, содержащее элементы, которые есть в "уменьшаемом",
 #но их нет в "вычитаемом". То есть уникальные для "уменьшаемого". Результат зависит от порядка операндов:
set_deux = {11, 4, 5}
set_trois = {11, 8, 9, 22}
set_un -= set_deux
print(set_un)


#Результатом симметрической разности ^ (исключающего ИЛИ) является множество,
# состоящее только из уникальных элементов исходных множеств. Совпадающие элементы исключаются:Eins, zwei, drei.
set_eins = {1, 2, 3, 11, 22}
set_zwei = {11, 4, 5}
set_drei = {11, 8, 9}
set_eins ^= set_zwei
#set_one=set_one.symmetric_difference(set_three)
print(set_eins)