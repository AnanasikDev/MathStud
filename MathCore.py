import random


# CONSTANTS


ALLOW_NEGATIVE = True
ALLOW_EQUATION = True
ALLOW_SQRT = True
ALLOW_BASIC = True


# GENERATORS


def clamp(n, a, b):
    return max(a, min(b, n))


def generate_operator():
    return "+-*/^"[random.randint(0, 4)]


def generate_basics(level):
    operator = generate_operator()

    if operator == '+':

        a = random.randint(3, 100 + 55*(level-1))
        b = random.randint(3, 100 + 55*(level-1))

        return [a + b, {'a' : a, 'b' : b, 'o' : operator}]

    if operator == '-':

        a = random.randint(3, 100 + 55*(level-1))
        b = random.randint(3, 100 + 55*(level-1))

        if ALLOW_NEGATIVE:
            return [a - b, {'a': a, 'b': b, 'o': operator}]
        else:
            if a > b:
                return [a - b, {'a': a, 'b': b, 'o': operator}]

            else:
                return [b - a, {'a': b, 'b': a, 'o': operator}]

    if operator == '*':

        a = random.randint(2, 10 * int(level ** 0.75))
        b = random.randint(2, 10 * int(level ** 0.7))

        return [a * b, {'a': a, 'b': b, 'o': operator}]

    if operator == '/':

        b = random.randint(3, 31 + level)
        a = b * random.randint(2, 19 + level)

        return [a // b, {'a': a, 'b': b, 'o': operator}]

    if operator == '^':
        a = random.randint(2, 20)

        n = 2

        if a == 2:
            n = random.randint(2, 14)
        if a == 3:
            n = random.randint(2, 5)
        if a == 4:
            n = random.randint(2, 4)
        if a == 5:
            n = random.randint(2, 4)

        return [a ** n, {'a': a, 'b': n, 'o': operator}]


def generate_equation(level):
    inp = generate_basics(level)
    print(f"x {inp[1]['o']} {inp[1]['b']} = {inp[0]}")
    print("x = ", end="")
    return inp[1]['a']


def generate_simple(level):
    inp = generate_basics(level)

    print(f"{inp[1]['a']} {inp[1]['o']} {inp[1]['b']} = ", end="")
    return inp[0]


def generate_sqrt(level):

    a = random.randint(2, 20)

    print(f"sqrt({a**2}) = ", end="")

    return a


def generate_mode():
    mode = random.randint(0, 2)

    # modes = [generate_simple, generate_equation, generate_sqrt]

    assert ALLOW_BASIC or ALLOW_EQUATION or ALLOW_SQRT

    # if not ALLOW_BASIC and not ALLOW_EQUATION and not ALLOW_SQRT:
    #     return -1

    if mode == 0:
        if not ALLOW_BASIC:
            return generate_mode()

    elif mode == 1:
        if not ALLOW_EQUATION:
            return generate_mode()

    elif mode == 2:
        if not ALLOW_SQRT:
            return generate_mode()

    return mode


def generate(level):

    mode = generate_mode()

    if mode == -1:
        return "[math core]: incorrect format"

    return [generate_simple, generate_equation, generate_sqrt][mode](level)
    # return generate_simple(level)
