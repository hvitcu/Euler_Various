def get_triang( ls ):
    sum = []
    count = 0

    for count in len( ls ):
        sum.append( ls[ count ] + ls[ count+1 ]  )

    return sum

if __name__ == '__main__':
    ls = [ x for x in range( 1,10 ) ]
    print zip( ls )


