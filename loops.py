'''Створи послідовність інструкцій, у вигляді 1 циклу. Цикл працює один раз. Відповіді виводяться у рядок,
у консолі буде роздруковано 3 рядки. Вимоги до кода:
Приймає від користувача рядок будь-яких символів, наприклад S f-FaGA a
Друкує усі літери з рядку, які у верхньому регістрі, у прикладі вище це SFGA
Друкує індекси усіх пробілів, якщо вони є, у прикладі вище це  1, 8
Друкує усі гласні букви з рядка, у прикладі вище це  aAa
Якщо у рядку буде послідовність з трьох цифр, наприклад ab-c474f g - цикл переривається та друкується повідомлення про цю подію.
 Інакше друкується повідомлення про коректне завершення циклу'''
letter = ""
vowels = ""
space = ""
capital = ""
row = input("enter whatever you want: ") #"S f-FaGA a 00 o 00"
# counter = 0
# for letter in row:
#     if letter in "aAoOuUyYiIeE":
#         vowels += letter
#     if letter in " ":
#         space += str(counter)
#     #if letter.isalpha() and letter == letter.capitalize():
#     if letter.isupper():
#         capital += letter
#     if row[counter].isdigit() and row[counter+1].isdigit() and row[counter+2].isdigit():
#         break
#     counter += 1
# print(f'vowels = {vowels} \nspace = {space} \ncapital = {capital}')
'''
В задании с циклами:
1.Тебе нужно считать строку через input.
2.Использовать counter - это хорошо, а вот enumerate - лучше.
3.В строке 10 индекс пробела просто добавляется, добавь запятые, чтобы можно было понять, что за индексы. Тоже самое для букв в других блоках.
4.В строке 23 у тебя вылетит ошибка, так как если у тебя длина строки = 10 и counter=10, то срезы +1 и +2 будут пытаться обратиться к несуществующим элементам.
'''
for index, letter in enumerate(row):
    if letter in "aAoOuUyYiIeE":
        vowels += letter+","
    if letter in " ":
        space += str(index)+",";
    if letter.isupper():
        capital += letter+","
    try:
        if row[index].isdigit() and row[index + 1].isdigit() and row[index + 2].isdigit():
            break
    except:
        continue
print(f'vowels = {vowels} \nspace = {space} \ncapital = {capital}')
