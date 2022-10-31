'''Створи послідовність інструкцій, яка реалізує функціонал калькулятора - складання, віднімання, поділ, множення, возведення в ступінь. Умови:
Гарантована послідовність введення 3 параметрів: операнд 1, операнд 2, дія для калькулятора
Користувач може помилитися зі знаком арифметичної дії, у цьому разі вивести сповіщення про некоректний знак
Гарантовано що операнди будуть типу int, float або комбінацією цих типів
Калькулятор мусить повернути результат типу int якщо якщо операнди були типу int. Або повернути float, якщо хоч один операнд був float
'''
first_operand = input("Enter number: ")
if "." in first_operand:
    first_operand = float(first_operand)
else:
    first_operand = int(first_operand)
# first_operand_type = isinstance(first_operand, int)
# print(first_operand_type)
# first_operand_type = isinstance(first_operand, float)
# print(first_operand_type)
second_operand = input("Enter number: ")
if "." in second_operand:
    second_operand = float(second_operand)
else:
    second_operand = int(second_operand)
_operator = input("Enter operator for your function (+, -, *, /, **): ")
'''if not (_operator=="+" or _operator=="-" or _operator=="*" or _operator=="/" or _operator=="**"):
    print("You entered wrong value for operator")
else:
    pass
'''
if _operator not in ["+","-","*","/", "**"]:
    print("Your operator value is incorrect");
    _operator = input("Enter operator for your function (+, -, *, /, **): ")
elif _operator == "+":
    print(first_operand+second_operand);
elif _operator == "-":
    print(first_operand-second_operand);
elif _operator == "*":
    print(first_operand*second_operand);
elif _operator == "/":
    try:
        first_operand/second_operand
    except ZeroDivisionError:
        print("You can't divide by 0")
    else:
        print(first_operand/second_operand);
elif _operator == "**":
    print(first_operand**second_operand);
else:
    print("this else will not happen")

'''
За бажанням - проаналізуй операнди та сповісти користувача про:
Тип операнду
Скільки порядків має операнд
Результат порівняння операндів'''
print("first_operand_type:", type(first_operand), "second_operand_type: ", type(second_operand))
print("first_operand_length:", len(str(int(first_operand))), "second_operand_length:", len(str(int(second_operand))))
print(bool(type(first_operand) == type(second_operand)))

