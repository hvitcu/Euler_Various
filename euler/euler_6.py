


if __name__ == '__main__':
    square = lambda x: x * x

    starting_n = 1
    end_n = 101

    squares_sum = sum([square(i) for i in range(starting_n, end_n)])
    sum_squared = square(sum(range(starting_n, end_n)))  #(1 + 2 + ... + 10)^2

    print "Difference between the 2 is %d" %(sum_squared - squares_sum)

