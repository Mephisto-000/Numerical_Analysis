


def fix_p(f, x0, tor, N, fl):
    """
    Fixed-Point Iteration
    :param f: given function
    :param x0: initial approximation value
    :param tor: tolerance
    :param N: maximum number of iterations
    :param fl: given significant digits
    :return: approximate solution p
    """
    err = 1
    itr0 = 0
    while(err > tor and itr0 < N):
        x = f(x0)
        err = abs(x0 - x)
        x0 = x
        itr0 = itr0 + 1
    return format(x, f".{fl}g")


def fix_p_table(f, x0, tor, N, fl):
    """
    Fixed-Point Iteration
    :param f: given function
    :param x0: initial approximation value
    :param tor: tolerance
    :param N: maximum number of iterations
    :param fl: given significant digits
    :return: list of approximate solution p_k
    """
    err = 1
    itr0 = 0
    p_k = []
    while(err > tor and itr0 < N):
        x = f(x0)
        err = abs(x0 - x)
        x0 = x
        p_k.append(format(x0, f".{fl}g"))
        itr0 = itr0 + 1
    return p_k




if __name__ == "__main__" :

    f = lambda x : x**(1/2)

    x_f = fix_p(f, 0.5, 10e-5, 100, 10)
    print(x_f)

    x_f_t = fix_p_table(f, 0.5, 10e-5, 100, 10)
    print(x_f_t)