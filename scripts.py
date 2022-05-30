import math

n = 1


# Метод половинного деления
def half_division():
    def f(x_):
        return 5 * (x_ ** 2) + 2 * x_ - n

    print('x = (-1 + ' + str((1 + 5 * n) ** 0.5) + ') / 5 =')
    print('x1 =', (-1 + (1 + 5 * n) ** 0.5) / 5, 'x2 =', true_x := (-1 - (1 + 5 * n) ** 0.5) / 5)
    a = math.floor(true_x)
    b = math.ceil(true_x)
    e = 10 ** (-3)
    print('E =', e)
    x = 0
    i = 0
    while True:
        x_prev = x
        x = (a + b) / 2
        print(i, ':', 'f(a):', f(a), 'xi - xi-1 =', math.fabs(x - x_prev))
        i += 1
        if math.fabs(x - x_prev) < e:
            break
        elif f(a) * f(x) > 0:
            a = x
        elif f(a) * f(x) < 0:
            b = x


# Метод Ньютона
def neut():
    def f(x_):
        return 5 * (x_ ** 2) + 2 * x_ - n

    def fp(x_):
        return 10 * x_ + 2

    print('x1 =', true_x := (-1 + (1 + 5 * n) ** 0.5) / 5, 'x2 =', (-1 - (1 + 5 * n) ** 0.5) / 5)
    b = math.ceil(true_x)
    e = 1e-9
    print('E =', e)
    i = 0
    x = b
    x_prev = 0
    print(i, '|', 'x:', x, '| f(x):', f(x), '| f\'(x):', fp(x), '| xi - xi-1 = -')
    while not math.fabs(x - x_prev) < e:
        x_prev = x
        i += 1
        x = x_prev - f(x_prev) / fp(x_prev)
        print(i, '|', 'x:', round(x, ndigits=9), '| f(x):', round(f(x), ndigits=9),
              '| f\'(x):', round(fp(x), ndigits=9), '| xi - xi-1 =',
              math.fabs(x - x_prev))


def simple_iteration():
    def f(x_):
        return x_ ** 2 * math.exp(x_) - n

    e = 1e-6
    print('E =', e)
    i = 0
    x = 0.75
    x_prev = 0
    print(i, '|', 'x:', x, '| f(x):', f(x), '| xi - xi-1 = -')
    while not math.fabs(x - x_prev) < e:
        x_prev = x
        i += 1
        x = x_prev - 1 / (3 * math.exp(1)) * f(x_prev)
        print(i, '|', 'x:', round(x, ndigits=8), '| f(x):', round(f(x), ndigits=8),
              '| xi - xi-1 =', math.fabs(x - x_prev))


# Метод Гаусса-Зейделя
def gauss_seidel():
    a_matrix = [
        [5, -1, 2],
        [2, 6, -1],
        [-3, -4, 1]
    ]
    b_matrix = [29.0 + n, n - 12.0, 5.0 + n]
    e = 1e-3
    print('E =', e)
    i = 0
    x1 = b_matrix[0]
    x2 = b_matrix[1]
    x3 = b_matrix[2]
    x_prev1 = x_prev2 = x_prev3 = 0
    print(i, '|', 'x1:', x1, 'x2:', x2, 'x3:', x3, '| E = -')

    while not (math.fabs(x1 - x_prev1) < e and math.fabs(x2 - x_prev2) < e and math.fabs(x3 - x_prev3) < e):
        x_prev1 = x1
        x_prev2 = x2
        x_prev3 = x3
        i += 1
        x1 = 1 / a_matrix[0][0] * (b_matrix[0] - a_matrix[0][1] * x2 - a_matrix[0][2] * x3)
        x2 = 1 / a_matrix[1][1] * (b_matrix[1] - a_matrix[1][0] * x1 - a_matrix[1][2] * x3)
        x3 = 1 / a_matrix[2][2] * (b_matrix[2] - a_matrix[2][0] * x1 - a_matrix[2][1] * x2)
        print(i, '|', 'x1:', x1, 'x2:', x2, 'x3:', x3, '| E =',
              max([math.fabs(x1 - x_prev1), math.fabs(x2 - x_prev2), math.fabs(x3 - x_prev3)]))


# Интерполирование методом Лагранжа
def lagrange_interpolation():
    def multiplication(equation_1, equation_2):
        result = {}
        for key_1, val_1 in equation_1.items():
            for key_2, val_2 in equation_2.items():
                try:
                    result[key_1 + key_2] += val_1 * val_2
                except KeyError:
                    result[key_1 + key_2] = val_1 * val_2
        return {key: val for key, val in result.items() if val != 0}

    def mul_digit(equation, digit):
        return {key: val * digit for key, val in equation.items() if val * digit != 0}

    def reformat_mul(mul_):
        return ' + '.join([(f'{val}x^{key}' if key != 0 else str(val))
                           if key != 1 else f'{val}x' for key, val in mul_.items() if
                           val != 0])

    x = [1, 3, 5, 7, 9]
    y = [n, 4 + n, 2 + n, 6 + n, 8 + n]

    result_ = {4: 0, 3: 0, 2: 0, 1: 0, 0: 0}

    for i in range(len(x)):
        mul = {0: 1}
        dig = 1
        for j in range(len(x)):
            if i != j:
                mul = multiplication(mul, {1: 1, 0: -y[j]})
                dig *= x[i] - x[j]
        print(i, reformat_mul(mul_digit(mul, y[i])),
              f'/({dig})')
        print(i, reformat_mul(mul_digit(mul, y[i] / dig)))
        mul = mul_digit(mul, y[i] / dig)
        print(i, mul)
        result_ = {i: result_[i] + mul[i] for i in range(len(x))}
        print(i, result_)
    print(reformat_mul(result_))

    answer = 0
    x_ = 6
    for key, val in result_.items():
        answer += val * (x_ ** key)
    print(answer)


# Метод прямоугольников для подсчёта определённых интегралов
def rect_method():
    def func_1(x):
        return math.sin(math.log(n * x, math.exp(1)))

    def func_2(x):
        return math.exp(- x ** 2) * math.sin(n * x)

    N = 1000
    h = n / N
    I = 0
    xi = 2
    for i in range(N):
        I += func_2((2 * xi + h) / 2)
        xi += h
    I *= h
    print(I)


rect_method()
