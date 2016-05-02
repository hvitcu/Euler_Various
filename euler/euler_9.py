import math
from collections import defaultdict
from euler_3 import get_prime_numbers
from euler_3 import asc_list
import numpy as np
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc
"""
def is_square(integer):
    return math.sqrt(integer).is_integer()

def get_pythagorean_number_dict(a_list):
    multiply = lambda x, y: x * x + y * y
    pn_dict = defaultdict(list)
    for i in range(1, len(a_list)):
        for j in a_list[1:]:
            pn = multiply(i,j)
            if math.sqrt(pn).is_integer():
                pn_dict[i].append([i, j, pn, i + j + math.sqrt(pn)])
            if  i + j + math.sqrt(pn) == 1000:
                print "YES %s and %s and %s, product %s"%(i, j,  math.sqrt(pn), i * j * math.sqrt(pn))
    return pn_dict

if __name__ == '__main__':
    squared = lambda x: x * x
    small_list = [i for i in range(1, 1000)]

    dict_pn = get_pythagorean_number_dict(small_list)
    for i in dict_pn.keys():
        b = dict_pn.get(i)[0][0]
        c = dict_pn.get(i)[0][1]

        # print "%s, %s, %s and sum is %d" %(i, dict_pn.get(i)[0][0], dict_pn.get(i)[0][1],
        #                                    i + dict_pn.get(i)[0][0] + dict_pn.get(i)[0][1])
        each_list = dict_pn.get(i)
