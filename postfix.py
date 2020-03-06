# postfix Макса ^)^)^)^^)^)^)^)^)^)
from stack import Stack


def checker(num):
    try:
        val = int(num)
        return True
    except ValueError:
        try:
            val = float(num)
            return True
        except ValueError:
            return False


def postfix(expr):
    priority = {"#": 3, "^": 3, "*": 2, "/": 2, "+": 1, "-": 1, "|(": 0, "(": 0}
    my_stack = Stack()
    inter_expr = expr.split(" ")
    out = []

    for token in inter_expr:
        if checker(token) or token.isalpha():
            out.append(token)
        elif token == "|(":
            my_stack.push(token)
        elif token == ")|":
            top_token = my_stack.pop()
            while top_token != "|(":
                out.append(top_token)
                top_token = my_stack.pop()
            out.append("|")
        elif token == "(":
            my_stack.push(token)
        elif token == ")":
            top_token = my_stack.pop()
            while top_token != "(":
                out.append(top_token)
                top_token = my_stack.pop()
        else:
            while not my_stack.empty() and priority[my_stack.peek()] >= priority[token]:
                out.append(my_stack.pop())
            my_stack.push(token)

    while not my_stack.empty():
        out.append(my_stack.pop())
    return " ".join(out)

# delete '#' and run program ^)^)^)^)

# example_with_letters = "( A + B ) * ( C + M )"
# print(postfix(example_with_letters))

# example_with_numbers = "# 488 - ( 17 ^ 2 - 17.3 * # ( |( # -16 + 1 )| ) )"
# print(postfix(example_with_numbers))
