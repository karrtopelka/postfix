# Стек Макса :)
# ..*.*... \O/..*..*
# *.....*...|....*...
# *......../.\....*..*


# клас
class Stack:
    # вхідні значення
    def __init__(self):
        self.items = []

    # перевірка чи пустий стек чи ні
    def empty(self):
        return self.items == []

    # присвоюєм стеку значення
    def push(self, item):
        self.items.append(item)

    # вилучаєм зі стеку значення
    def pop(self):
        return self.items.pop()

    # піковий елемент, береться останній максимальний індекс масиву
    def peek(self):
        return self.items[len(self.items) - 1]

    # розмір стеку
    def size(self):
        return len(self.items)

    # виведення всіх елементів стеку
    def print_all_items(self):
        return ', '.join(self.items)
