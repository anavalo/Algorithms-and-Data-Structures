def spiral(array):

    # k: start row idx
    # l: end row idx
    # m: start column idx
    # n: end column idx

    k, m = 0, 0
    n = len(array[0])-1
    l = len(array)-1
    result = []
    for i in range(m, n-1):
        result.append([i][k])
    return result


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]]
print(spiral(matrix))
