'''Write a function that takes in an array of integers of length at least 2. The function should return an array of the
starting and ending indices of the smallest subarray in the input array that needs to be sorted in place in order for
the entire input array to be sorted. If the input array is already sorted, the function should return [-1, -1].'''

def subarraySort(array):
    minOutOfORder = float("inf")
    maxOutOFOrder = float("-inf")
    for i, j in enumerate(array):
        num = array[i]
        if isOutOfOrder(i, num, array):
            minOutOfORder = min(num, minOutOfORder)
            maxOutOFOrder = max(num, maxOutOFOrder)
    if minOutOfORder == ("inf"):
        return [-1, -1]
    subarraylidx = 0
    while minOutOfORder >= array[subarraylidx]:
        subarraylidx +=1
    subarrayridx = len(array) -1
    while subarrayridx <= array[subarrayridx]:
        subarrayridx -= 1
    return [subarraylidx, subarrayridx]


def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i+1]
    if i == len(array) -1:
        return num < array[i-1]
    else:
        return num < array[i-1] or num > array[i+1]


bbbb = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print(subarraySort(bbbb))
