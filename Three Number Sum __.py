'''Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
The function should find all triplets in the array that sum up to the target sum and return  a two-dimensional array
of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets should be
ordered in ascending order with respect to the numbers they hold. If no three numbers sup up the target sum, the function
should return an empty array
Input: [12,3,1,2,-6,5,-8,6], 0
Output: [[-8,2,6],[-8,3,5],[-6,1,5]]
'''


def threeNumberSum(array, targetSum):
    array.sort()
    n = len(array)
    triplets = []
    for i in range(n-2):
        r = n - 1
        l = i + 1
        while l < r:
            currentSum = array[i] + array[l] + array[r]
            if currentSum == targetSum:
                triplets.append([array[i], array[l], array[r]])
                l += 1
                r -= 1
            elif currentSum < targetSum:
                l += 1
            elif currentSum > targetSum:
                r -= 1
    return triplets





print(threeNumberSum([12,3,1,2,-6,5,-8,6], 5))