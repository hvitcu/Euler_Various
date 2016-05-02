from multiprocessing.dummy import Pool as ThreadPool

def get_prime_numbers_list(number):
    for divisor in range_list:
        if number % divisor == 0 and number != divisor:
            return number


def calling(pool, starting_n, end_n):
    r_list = pool.map(get_prime_numbers_list, reversed(range(starting_n, end_n)))
    return r_list

def diff_lists(f_list, sec_list):
    for i in f_list:
        if i is not None:
            sec_list.remove(i)

    return sec_list

if __name__ == '__main__':
    starting_n = 2
    end_n = 100000

    pool = ThreadPool()
    range_list = [i for i in range(starting_n, end_n)]

    prime_list = []

    while True:
        prime_list = diff_lists(calling(pool, starting_n, end_n), range_list)
        end_n += 10000
        range_list= [i for i in range(starting_n, end_n)]
        if len(prime_list) > 10003: break

    print prime_list[496]
    print prime_list[497]
    print prime_list[498]
    print prime_list[499]
    print prime_list[500]

    print prime_list[10000]
    print prime_list[10001]
    print prime_list[10002]

    pool.close()
    pool.join()
