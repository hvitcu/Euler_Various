import numpy as np
import qpython as qp

def asc_list(number=12):
    simple_list = []
    for i in range(1, number):
        simple_list .append(i)
    return simple_list

def get_prime_numbers(original_list):
    removed_list = []

    for i in original_list[::-1]:
        for j in original_list[1:]:
            if i % j == 0 and i != j:
                removed_list.append(i)

    return [x for x in original_list if x not in removed_list and x != 1]

def divide(number, divisor):
    return number / divisor if number % divisor == 0 else 111

def get_prime_factors(number):
    prime_list = get_prime_numbers(asc_list(10000))
    print prime_list
    factors = []

    for i in prime_list:
        division_res = divide(number, i)
        if division_res not in prime_list and division_res != 111:
            factors.append(i)

            division_res = divide(division_res, i)

            if division_res in prime_list:
                factors.append(i)

    print factors
    print factors[-1]

if __name__ == '__main__':
    number = 600851475143
    get_prime_factors(number)
    # bigList= asc_list(60085147)