'''Надрукуй 4 рядки: помідор -> м'ясо -> сир -> хліб, умови:
Створи 4 функції, кожна друкує свій шар
Викликай лише одну функцію
Використай синтаксис декораторів
Очікуваний результат друку:
помідор
м'ясо
сир
хліб'''


def tomato(func):
    def wrapper():
        print("помідор")
        func()
    return wrapper


def meat(func):
    def wrapper():
        print("м'ясо")
        func()
    return wrapper


def cheese(func):
    def wrapper():
        print("сир")
        func()
    return wrapper


def bread(func):
    def wrapper():
        print("хлiб")
        func()
    return wrapper


def food():
    print()


#sandwich = bread(ingredients(sandwich))
#sandwich()

@tomato
@meat
@cheese
@bread
def food():
    print()
food()