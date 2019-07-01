
def kadanesAlgorithm(array):
    lidx = 0
    ridx = (len(array))
    sum_right = []
    sum_left = []
    x = sum(array)
    z = max(array)
    while lidx < ridx:
        left_sum = sum(array[lidx:ridx])
        sum_left.append(left_sum)
        lidx +=1
    for i, j in enumerate(sum_left):
        if j == max(sum_left):
            maxlidx = i
    while ridx > 0:
        right_sum = sum(array[0:ridx])
        sum_right.append(right_sum)
        ridx -= 1
    for i, j in enumerate(sum_right):
        if j == max(sum_right):
            maxridx = i
    final_Array = array[maxlidx:(-abs(maxridx))]
    y =  sum(final_Array)
    print(final_Array)
    print(x, z, y)
    return max(x, z, y)


ex1 = [-1, -2, -3 , -4, -5, -6, -7, -8, -9, -10]

print(kadanesAlgorithm(ex1))