import random


# CONSTANTS


ALLOW_NEGATIVE = False
ALLOW_EQUATION = False
ALLOW_SQRT = False
ALLOW_EXPRESSION = False
ALLOW_VIEW = False
ALLOW_QUADRATIC_EQUATION = True

ALLOW_BASIC = False


# GENERATORS


def clamp(n, a, b):
    return max(a, min(b, n))


def generate_operator(include_div = True, include_degree = True):
    s = ['+', '-', '*']

    if include_div:
        s.append('/')
    if include_degree:
        s.append('**')

    return s[random.randint(0, len(s)-1)]


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

    if operator == '**':
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


def generate_expression(level):
    num_of_clasters = random.randint(1, 3)

    s = ""

    for i in range(num_of_clasters):
        g = generate_basics(level)

        s += f"({g[1]['a']} {g[1]['o']} {g[1]['b']})"
        if i < num_of_clasters - 1:
            s += " " + generate_operator(False, False) + " "

    answer = int(eval(s))
    # answer = 0

    s += " = "

    print(s, end="")

    return [answer]


def generate_equation(level):
    inp = generate_basics(level)
    print(f"x {inp[1]['o']} {inp[1]['b']} = {inp[0]}")
    print("x = ", end="")
    return [inp[1]['a']]


def generate_simple(level):
    inp = generate_basics(level)

    print(f"{inp[1]['a']} {inp[1]['o']} {inp[1]['b']} = ", end="")
    return [inp[0]]


def generate_sqrt(level):

    a = random.randint(2, 20)

    print(f"sqrt({a**2}) = ", end="")

    return [a]


def generate_view(level):
    width = 5 * level
    height = (5 * level) // 2

    default_simbol = "*"
    point_simbol = "@"

    a = random.randint(3, 13)

    matrix = [[default_simbol for i in range(width)] for j in range(height)]

    def generate_point():
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        if matrix[y][x] == point_simbol:
            generate_point()
        else:
            matrix[y][x] = point_simbol

    for i in range(a):
        generate_point()

    for i in matrix:
        print("".join(i))

    print("Amount of points = ", end="")

    return [a]


def generate_quadratic_equation(level):
    # ax2 + bx + c = 0

    root1 = random.randint(-10, 10)
    root2 = random.randint(-10, 10)

    if root1 == 0:
        root1 += 1
    if root2 == 0 or root2 == root1:
        root2 += 1

    a = random.randint(1, 10)

    # x1 + x2 = -b/a
    # x1 * x2 = c/a

    c = root1 * root2 * a
    b = (root1 + root2) * -a

    print(f"{a}x^2 + {b}x + {c} = 0")
    # print(a, b, c, root1, root2)
    print("x1, x2 = ", end="")
    return [f"{root1} {root2}", f"{root2} {root1}"]


def generate_mode():
    mode = random.randint(0, 5)
    # mode = 4

    # modes = [generate_simple, generate_equation, generate_sqrt]

    assert ALLOW_BASIC or ALLOW_EQUATION or ALLOW_SQRT or ALLOW_EXPRESSION or ALLOW_VIEW or ALLOW_QUADRATIC_EQUATION

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

    elif mode == 3:
        if not ALLOW_EXPRESSION:
            return generate_mode()

    elif mode == 4:
        if not ALLOW_VIEW:
            return generate_mode()

    elif mode == 5:
        if not ALLOW_QUADRATIC_EQUATION:
            return generate_mode()

    return mode


def generate(level):

    mode = generate_mode()

    if mode == -1:
        return "[math core]: incorrect format"

    return [generate_simple, generate_equation, generate_sqrt, generate_expression, generate_view, generate_quadratic_equation][mode](level)
    # return generate_simple(level)
