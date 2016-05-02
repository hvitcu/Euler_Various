'''
Created on Nov 2, 2015

@author: Horia
'''
def fibonacci(first, second, numbersCount):
    fibList = []
    fibList.append(first)
    fibList.append(second)
    for i in range(2, numbersCount):
        if (first + second) <= 4000000:
            fibList.append(first + second)
            first = second
            second = fibList[i]
            print fibList[i]
    return fibList

if __name__ == '__main__':

    fibList = []
    for i in range(1, 10):
        fibList.append(i)
    a = [x for x in fibList if any([ x % 3 == 0, x % 5 == 0 ])]
    print sum(a)

    a = fibonacci(1, 2, 100)
    print [x for x in a if x % 2 == 0]
    print sum([x for x in a if x % 2 == 0])