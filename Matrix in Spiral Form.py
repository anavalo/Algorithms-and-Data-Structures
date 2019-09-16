import numpy
def spiral(array):
    # k: start row idx
    # l: end row idx
    # m: start column idx
    # n: end column idx
    result = []
    if len(array) != 0:
        if len(array[0]) == 1:
             result.append(array[0][0])
             result.append(array[1][0])
        else:
            k, m = 0, 0
            n = len(array[0]) - 1
            l = len(array) - 1
            while m <= n:
                result.append(array[k][m])
                m +=1
            while k < l:
                result.append(array[k+1][n])
                k += 1
            k, m = 0, 0
            while n > m:
                result.append(array[l][n-1])
                n -=1
            while l > k:
                result.append(array[l-1][m])
                l -= 1
    newar = numpy.array(array)[1:-1, 1:-1]
    x = newar.tolist()
    print(result)
    return result[:-1] + spiral(x)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]]
print(spiral(matrix))
