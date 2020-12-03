#https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/secant/


def secant_method(f, x0, x1, tor, N, fl):
    """
    Secant Method
    :param f: given function
    :param x0: left endpoint
    :param x1: right endpoint
    :param tor: tolerance
    :param N: maximum number of iterations
    :param fl: given significant digits
    :return: approximate solution x
    """
    err = 1
    itr0 = 1
    if f(x0)*f(x1) >= 0:
        print("Fail, since f(x0)*f(x1) >= 0.")
        return None
    while(err > tor and itr0 < N):
        x = x1 - (f(x1)*(x1 - x0))/(f(x1) - f(x0))
        if f(x)*f(x0) < 0:
            x0 = x0
            x1 = x
        elif f(x)*f(x1) < 0:
            x0 = x
            x1 = x1
        elif f(x) == 0:
            break
        else:
            print("Fail.")
            break
        itr0 = itr0 + 1
    return format(x, f".{fl}g")


def secant_method_table(f, x0, x1, tor, N, fl):
    """
    Secant Method
    :param f: given function
    :param x0: left endpoint
    :param x1: right endpoint
    :param tor: tolerance
    :param N: maximum number of iterations
    :param fl: given significant digits
    :return: list of approximate solution x
    """
    err = 1
    itr0 = 1
    p_k = []
    if f(x0)*f(x1) >= 0:
        print("Fail, since f(x0)*f(x1) >= 0.")
        return None
    while(err > tor and itr0 < N):
        x = x1 - (f(x1)*(x1 - x0))/(f(x1) - f(x0))
        if f(x)*f(x0) < 0:
            x0 = x0
            x1 = x
        elif f(x)*f(x1) < 0:
            x0 = x
            x1 = x1
        elif f(x) == 0:
            break
        else:
            print("Fail.")
            break
        p_k.append(format(x, f".{fl}g"))
        itr0 = itr0 + 1
    return p_k


if __name__ == "__main__" :

    f = lambda x: x**3 - x**2 - 1
    x0 = 0
    x1 = 30
    tor = 10e-5
    N = 10000
    fl = 10

    secant_f = secant_method(f, x0, x1, tor, N, fl)
    print("\n", secant_f)
    print("\n", f(4))