'''Створи послідовність інструкцій, у вигляді 1 циклу. Цикл працює один раз. Відповіді виводяться у рядок,
у консолі буде роздруковано 3 рядки. Вимоги до кода:
Приймає від користувача рядок будь-яких символів, наприклад S f-FaGA a
Друкує усі літери з рядку, які у верхньому регістрі, у прикладі вище це SFGA
Друкує індекси усіх пробілів, якщо вони є, у прикладі вище це  1, 8
Друкує усі гласні букви з рядка, у прикладі вище це  aAa
Якщо у рядку буде послідовність з трьох цифр, наприклад ab-c474f g - цикл переривається та друкується повідомлення про цю подію.
 Інакше друкується повідомлення про коректне завершення циклу'''
letter = str()
vowels = ""
space = ""
capital = ""
row = "S f-FaGA a 000 o"
counter = 0
for letter in row:
    if letter in "aAoOuUyYiIeE":
        vowels += letter
    if letter in " ":
        space += str(counter)
    if letter.isalpha() and letter == letter.capitalize():
        capital += letter
    if row[counter].isdigit() and row[counter+1].isdigit() and row[counter+2].isdigit():
        break
    counter += 1
print(f'vowels = {vowels} \nspace = {space} \ncapital = {capital}')
