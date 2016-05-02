from multiprocessing.dummy import Pool as ThreadPool

def verify_prime(number):

    rev_list = reversed( [x for x in range(2, 200000, 1)])
    removed_list = []

    for i in rev_list:
        if i % number == 0 and i != number:
            removed_list.append(i)
    return removed_list

# def remove_elements(original_list):
#     for i in every_list:
#             if i in n_list:
#                 n_list.remove(i)

if __name__ == '__main__':

    pool = ThreadPool()

    start_at = 2
    end_at = 200000
    step_by = 1

    n_list = [number for number in range(start_at, end_at, step_by)]

    r_list = pool.map(verify_prime, n_list, 10000)
    print "Done"
    # f_list = pool.map(remove_elements,r_list, 10000)

    # print r_list
    # for every_list in r_list:
    #     for i in every_list:
    #         if i in n_list:
    #             n_list.remove(i)
    # print n_list
    pool.close()
    pool.join()


    """
    kdb code:

        isprime:{c:x mod 2+til floor sqrt x; (c?0) = count c}

        ls:3+til 2000000

        plist:isprime peach ls

        ilist:where plist=1

        flist:{ls[x]} ilist

        2 + sum flist

        142913828922

    """