'''
Given an non-empty array of integers, write a function that returns an array of length 2. The first element in the
output array should be an integer value representing the greatest sum that can be generated from a strictly-increasing
subsequence in the array. The second element should be an array of the numbers in that subsequence. A subsequence is
defined as a set of numbers that are not necessarily adjacent but that are in the same order as they appear in the array.
Assume that there will only be one increasing subsequence with the greatest sum.
'''

def maxSumIncreasingSubsequence(array):
    maxsum = max(array)
    output = []
    current = 0
    if len(array) == 1:
        return [maxsum, array]
    for i, j in enumerate(array):
        if array[i] < array[i-1]:
            current += j
        else:
            current += j
            array.pop(i)
            break
    maxsum = max(maxsum, current)
    print(array)
    print(maxsum)
    return maxsum







print(maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]))
