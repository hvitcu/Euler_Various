import os
import numpy as np

def get_resource_file(res_path):
    script_dir = os.path.dirname((os.path.abspath(__file__)))
    res_file = os.path.join(script_dir, res_path)
    return res_file

def get_digit_list(file):
    f = open(file_to_read, 'r+')
    init_list = f.read().splitlines()
    f.close()

    joined_list = ''.join(init_list)
    digit_list = map(int, joined_list)
    return digit_list

def multiply_list_elements(elem_list):
    multiply = lambda x, y: x * y
    return reduce(multiply, elem_list)


if __name__ == '__main__':

    res_path = "resources\\thousand_digit.txt"

    file_to_read = get_resource_file(res_path)

    digit_list = get_digit_list(file_to_read)

    first_sub_list = digit_list[0:4]

    start_point = 0
    end_point = 13
    # print digit_list
    # print multiply_list_elements(first_sub_list)
    res = []
    while True:
        res.append(multiply_list_elements(digit_list[start_point: end_point]))
        start_point += 1
        end_point += 1
        if end_point == 1000: break

    # print 'True and index is %s' %res.index(5832) if 5832 in res else 'False'
    print max(res)