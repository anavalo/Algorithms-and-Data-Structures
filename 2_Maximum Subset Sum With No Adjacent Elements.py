'''Write a function that takes in an array of positive integers and returns an integer representing the maximum sum of
nob-adjacent elements in the array. If a sum cannot be generated, the function should return 0'''

def maxSubsetSumNoAdjacent(array):
    # edge case of empty array
    if not len(array):
        return 0
    # edge case whre lenght of array = 1
    elif len(array) == 1:
        return array[0]
    maxSums = array
    maxSums[1] = max(array[0], array[1])
    for i in range (2, len(array)):
        maxSums[i] = max(maxSums[i-1], maxSums[i-2] + array[i])
    return maxSums[-1]





mmm = [7, 10, 12, 7, 9, 14]

print(maxSubsetSumNoAdjacent(mmm))



