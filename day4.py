import sys
import functools

global_variable = 7

def addition(x, y=1):
    """
    Sum function
    :param x: first value
    :param y: second value
    :return: the sum of the values
    """
    return x + y


def interchange(value1: int | float, value2: int | float) -> None:
    aux = value1
    value1 = value2
    value2 = aux


def interchange2(value1, value2):
    return value2, value1


def interchange3(values):
    if len(values) > 1:
        aux = values[0]
        values[0] = values[1]
        values[1] = aux


def multiplication(*values):
    product = 1
    for v in values:
        product *= v
    return product


def total_sales(**author_sales):
    print(author_sales["John"])


def f():
    global_variable = 9
    print(global_variable)


def g():
    global global_variable
    global_variable = 9
    print(global_variable)


if __name__ == "__main__":
    print(sys.argv)
    result = addition(3, 4)
    print(result)

    incrementation = addition(7)
    print(incrementation)

    sum_result = addition(y=7, x=2)
    print(sum_result)

    a = 5
    b = 9
    interchange(a, b)
    print(a, b)

    a, b = interchange2(a, b)
    print(a, b)

    my_list = [a, b]
    interchange3(my_list)
    print(my_list)

    for z in my_list:
        z = 100

    print(my_list)
    print(multiplication(5))
    print(multiplication(5, 4))
    print(multiplication(5, 6, 7))
    print(multiplication())

    total_sales(John=500, Maria=200, George=400)

    l = lambda x,y: x**y
    print(l(2,3))

    names = ["John", "George", "Maria", "Ana"]
    upper_names = list(map(lambda s : s.upper(), names))
    print(upper_names)
    long_names = list(filter(lambda s : len(s) > 3, names))
    print(long_names)
    all_names = functools.reduce(lambda n1, n2: n1 + " | " + n2, names)
    print(all_names)

    upper_names = [s.upper() for s in names]
    print(upper_names)
    long_names = [s for s in names if len(s) > 3]
    print(long_names)

    f()
    print(global_variable)
    g()
    print(global_variable)

