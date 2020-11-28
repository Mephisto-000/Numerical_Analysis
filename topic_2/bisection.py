


def b_method(f, a, b, tor, N):
    """
    The Bisection Method
    :param f: Given function
    :param a: left endpoint
    :param b: right endpoint
    :param tor: tolerance
    :param N: maximum number of iterations
    :return: approximate solution p
    """
    err = 1
    itr0 = 0
    if f(a)*f(b) >= 0:
        print(f"\n a 與 b 異值同號或同值同號 \n a = {a}, b = {b}.")
        return None
    elif f(a)*f(b) < 0:
        while (err > tor and itr0 < N):
            p = (a + b)/2
            fp = f(p)
            if f(a)*fp > 0:
                a = p
            else:
                b = p
            if (b - a)/2 < tor:
                break
            itr0 = itr0 + 1
        return p


def b_method_table(f, a, b, tor, N, fl):
    """
    The Bisection Method
    :param f: Given function
    :param a: left endpoint
    :param b: right endpoint
    :param tor: tolerance
    :param N: maximum number of iterations
    :param fl: given significant digits
    :return: table of approximate solution p_k
    """
    err = 1
    itr0 = 0
    if f(a)*f(b) >= 0:
        print(f"\n a 與 b 異值同號或同值同號 \n a = {a}, b = {b}.")
        return None
    elif f(a)*f(b) < 0:
        p_k = []
        while (err > tor and itr0 < N):
            p = (a + b)/2
            p_k.append(format(p, f".{fl}g"))
            fp = f(p)
            if f(a)*fp > 0:
                a = p
            else:
                b = p
            if (b - a)/2 < tor:
                break
            itr0 = itr0 + 1
        return p_k





if __name__ == "__main__" :

    f = lambda x : x**3 + 4 * x**2 - 10
    p_v = b_method(f, 1, 2, 10e-5, 13)
    print(format(p_v, ".10g"))

    p_v_t = b_method_table(f, 1, 2, 10e-5, 13, 10)
    print("\n", p_v_t)