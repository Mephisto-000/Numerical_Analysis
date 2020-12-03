import numpy as np
import matplotlib.pyplot as plt
from bisection import*
from fixed_point import*
from newtons import*
from secant import*

f = lambda x: x**3 - x**2 - 1
df = lambda x: 3 * x**2 - 2 * x
x0 = 1
x1 = 4
tor = 10e-4
N = 100
fl = 7




if __name__ == "__main__" :


    bf = b_method(f, x0, x1, tor, N, fl)
    # ff = fix_p_table(f, x0, tor, N, fl)
    nf = newtons_method(f, df, x0, tor, N, fl)
    sf = secant_method(f, x0, x1, tor, N, fl)

    bf = float(bf)
    nf = float(nf)
    sf = float(sf)

    print("\nBisection Method : ", bf)
    # print("\nFixed-Point Iteration : ", ff)
    print("\nNewton's method : ", nf)
    print("\nSecant method : ", sf)




