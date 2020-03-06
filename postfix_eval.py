# postfix evaluation Макса :)):):):):)):)

# guide to postfix:
# 1) всі елементи пишуться через пробіл: 25 - ( 10 + 5 ^ 2 ) - 3 -> ✔
# 2) від'ємне число пишеться разом: -10 -> ✔
# 3) модуль пишеться з відкриваючою і закриваючою дужкою: |( -10 + 5 )| -> ✔
# 4) для знаходження кореня, перед виразом поставте ришітку: # 16 -> ✔
# Можете спробувати ось цей приклад: # ( 485 - 1 ) - ( 17 ^ 2 - 17 * ( |( -15 + 1 )| ) )

from math import sqrt
from postfix import postfix, checker
from stack import Stack


def num(string):
    return int(string) if float(string) == int(float(string)) else float(string)


def evaluation(op1, op2, token):
    if token == "+":
        return op1 + op2
    elif token == "*":
        return op1 * op2
    elif token == "/":
        return op1 / op2
    elif token == "^":
        return pow(op1, op2)
    else:
        return op1 - op2


def postfix_evaluation(post_expr):
    my_stack = Stack()
    post_expr = post_expr.split()

    for token in post_expr:
        if checker(token):
            my_stack.push(token)
        elif token == '#':
            my_stack.push(sqrt(num(my_stack.pop())))
        elif token == "|":
            my_stack.push(abs(num(my_stack.pop())))
        else:
            op2 = num(my_stack.pop())
            op1 = num(my_stack.pop())
            result = evaluation(op1, op2, token)
            my_stack.push(result)
    return "{:.2f}".format(my_stack.pop())


infix_expression = input('Приклад:\n')
postfix_expresion = postfix(infix_expression)
postfix_result = postfix_evaluation(postfix_expresion)
print("Приклад записаний інфіксом = {}".format(infix_expression))
print("Приклад записаний постфіксом = {}".format(postfix_expresion))
print("Результат: {}".format(postfix_result))
