'''
На базі калькулятора з практичного завдання у розділі Розгалуження,
створи нескінченний цикл до доки користувач не введе exit замість будь-якого з операндів або оператора
'''


while True:
    first_operand = input("Enter number: ")
    if first_operand == "exit":
        break
    second_operand = input("Enter number: ")
    if second_operand == "exit":
        break
    _operator = input("Enter operator for your function (+, -, *, /, **): ")
    if _operator == "exit":
        break
    if "." in first_operand:
        first_operand = float(first_operand)
    else:
        first_operand = int(first_operand)
    if "." in second_operand:
        second_operand = float(second_operand)
    else:
        second_operand = int(second_operand)
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
        print("this else will not happen");
