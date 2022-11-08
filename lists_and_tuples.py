#Створи послідовність інструкцій, яка отримує рядок від користувача та друкує кожне третє слово з цього рядка. Цикли не використовувати
entrance ='hello world how are you yes all good'
#entrance = input("enter whatever you want: ")
split_string = entrance.split()
#print(f"{type(joined_string)=}, {joined_string=}")
print(split_string)
print(f'every third word in list - {split_string[2::3]}')
joined_string = ','.join(split_string[2::3])
print(f'every third word in string - {joined_string}')


'''
Створи генератор списка
Вхідний список [1, 2.1, "f", "2", 3, "1", 18, "df"]
Вихідний список [1, 2.1, -1, '6', 9, '3', 18, -1]
Як та які елементи потрапляють з вхідного до вихідного списка:
Елемент типу float
Елемент типу int та є парним
Елемент типу int та є непарним. Додатково звести у 2 ступінь. Приклад, елемент 3 -> 9
Елемент типу str у якому лише цифри. Додатково помножити на 3. Приклад, елемент "2" -> "6"
В інших випадках замість елемента підстав число -1'''
old_list = [1, 2.1, "f", "2", 3, "1", 18, "df"]
new_list = []
for element in (old_list):
    if type(element) == float:
        new_list.append(element);
    elif type(element) == int and element % 2 == 0:
        new_list.append(element)
    elif type(element) == int and element % 2 !=0:
        new_list.append(element**2)
    elif type(element) == str and element.isdigit():
        new_list.append(int(element)*3)
    else:
        new_list.append(-1)
print(new_list)


new_list = [element if type(element) == float else element if type(element) == int and element % 2 == 0 else element**2 if type(element) == int and element % 2 !=0 else int(element)*3 if type(element) == str and element.isdigit() else -1 for element in (old_list)]
print(new_list)