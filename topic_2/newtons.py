


def newtons_method(f, df, x0, tor, N, fl):
    """
    Newton's Method
    :param f: given function
    :param df: derivative of f
    :param x0: initial approximation value
    :param tor: tolerance
    :param N: maximum number of iterations
    :param fl: given significant digits
    :return: approximate solution x
    """
    err = 1
    itr0 = 0
    while(err > tor and itr0 < N):
        x = x0 - f(x0)/df(x0)
        err = abs(x0 - x)
        x0 = x
        itr0 = itr0 + 1
    return format(x, f".{fl}g")


def newtons_method_table(f, df, x0, tor, N, fl):
    """
    Newton's Method
    :param f: given function
    :param df: derivative of f
    :param x0: initial approximation value
    :param tor: tolerance
    :param N: maximum number of iterations
    :param fl: given significant digits
    :return: list of approximate solution x
    """
    err = 1
    itr0 = 0
    p_k = []
    while(err > tor and itr0 < N):
        x = x0 - f(x0)/df(x0)
        err = abs(x0 - x)
        x0 = x
        p_k.append(format(x0, f".{fl}g"))
        itr0 = itr0 + 1
    return p_k






if __name__ == "__main__" :

    f = lambda x: x**3 - x**2 - 1
    df = lambda x: 3 * x**2 - 2 * x

    newt_f = newtons_method(f, df, 1, 10e-5, 100, 10)
    print(newt_f)

    newt_f_t = newtons_method_table(f, df, 1, 10e-5, 100, 10)
    print(newt_f_t)