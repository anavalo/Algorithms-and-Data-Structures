'''Write a function that takes in a non-empt array of integers and returns the max sum that can be obtained by summing
up all the numbers in a non-empty subarray of the input array. A subarray must contain only adjacent numbers'''

def kadanesAlgorithm(array):
    maxEnndingHere = array[0]
    maxSoFar = array[0]
    for num in array[1:]:
        maxEnndingHere = max(num, maxEnndingHere+num)
        maxSoFar = max(maxSoFar, maxEnndingHere)
    return maxSoFar



ex1 = [-1, -2, -3 , -4, -5, -6, -7, -8, -9, -10]

print(kadanesAlgorithm(ex1))