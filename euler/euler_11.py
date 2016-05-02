#do[20;s ,:prd each (4#'{1 rotate x}\[16;ls m]); m:m+1;];

#t:([]a:`long$();b:`long$();c:`long$();d:`long$();e:`long$();f:`long$();g:`long$();h:`long$();i:`long$();j:`long$();k:`long$();l:`long$();m:`long$();n:`long$();o:`long$();p:`long$();q:`long$();r:`long$();s:`long$();t:`long$())

import os


def get_resource_file(res_path):
    script_dir = os.path.dirname((os.path.abspath(__file__)))
    res_file = os.path.join(script_dir, res_path)
    return res_file

def get_digit_list(file):
    f = open(file_to_read, 'r+')
    dglist = []
    init_list = f.read().splitlines()
    f.close()

    for i in init_list:
        dglist.append(i.split())

    return dglist

def get_diagonal(matrix, m=0, n=0):
    ls = []
    matrix_len = len(matrix)
    while m <matrix_len:
        ls.append(matrix[m][n] if n < matrix_len else None)
        m +=1
        n += 1

    ls = [x for x in ls if x is not None]

    return ls if len(ls) > 3 else None


if __name__ == '__main__':

    res_path = "resources\\twenty"

    file_to_read = get_resource_file(res_path)

    dig_list = get_digit_list(file_to_read)

    ls_r_diags = []
    ls_l_diags = []
    for i in range(20):
        # ls_r_diags.append(get_diagonal(dig_list, 0, i))
        ls_l_diags.append(get_diagonal(dig_list,1,i))
    print ls_r_diags
    # print ls_l_diags
