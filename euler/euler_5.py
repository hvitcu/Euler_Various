from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool
from multiprocessing import Process

def divided_evenly(x, y):
    return bool(x % y == 0)

def process_division(number):
    range_plus_one = number + 1
    minimal_increment = number

    count = 0
    start = True
    while (start) :
        for i in reversed(range(1, range_plus_one)):
            if(bool(number % i == 0)):
                count += 1
            if count == minimal_increment: start = False
        else:
            count = 0
        number += minimal_increment
        print number

def actual_div_work(number):
    div_list = [i for i in reversed(range(1, 21))]
    result_list = []

    for divisor in div_list:
        if number % divisor == 0:
            # print "Number %s, divisor %s" %(number, divisor)
            result_list.append(1)
        else:
            result_list.append(0)

    if all(result_list) == 1:
        return True
    return False

if __name__ == '__main__':
    pool = ThreadPool()
    n = 20
    start_at = 20
    end_at = 1000000000
    step_by = 20

    r_list = pool.map(actual_div_work, [number for number in range(start_at, end_at, step_by)], 10000000)

    pool.close()
    pool.join()

    for i in r_list:
        if i == True:
            print r_list.index(i)
            n = n * r_list.index(i) + n
            print "n is %d" % n
            break

    # for i in results_map:
    #     if all(i) == 1:
    #         print i
    #         print results_map.index(i)
    #         break

