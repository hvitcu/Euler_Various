import numpy as np
import qpython as qp

def is_palendrome(funct, f_number, s_number):
    digit_list = map(int, str(funct(f_number, s_number)))
    print digit_list
    if digit_list == digit_list[::-1]:
        print digit_list
        print digit_list[::-1]
        return True


if __name__ == '__main__':
    mul = lambda x, y : x * y
    jl = [i for i in range(900, 1000)]

    n = 999
    while (n >= 1):
        for i in jl[::-1]:
            # print is_palendrome(mul, i, n)
            if is_palendrome(mul, i, n):
                n = 1
                break
        n -= 1