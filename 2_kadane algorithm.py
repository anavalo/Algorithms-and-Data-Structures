
def kadanesAlgorithm(array):
    maxEnndingHere = array[0]
    maxSoFar = array[0]
    for num in array[1:]:
        maxEnndingHere = max(num, maxEnndingHere+num)
        maxSoFar = max(maxSoFar, maxEnndingHere)
    return maxSoFar



ex1 = [-1, -2, -3 , -4, -5, -6, -7, -8, -9, -10]

print(kadanesAlgorithm(ex1))