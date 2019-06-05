'''
Write a function that takes in two non-empty arrays of integers. The function should find the pair of numbers
(one form the first array, one from the second array) whose absolut differnce is closest to zero. The function should
return an array containing these two numbers, with the number from the first array in the first position. Assume that
there will be one pair of numbers with the smallest differnce.

Input: [-1,5,10,20,28,3],[26,134,135,15,17]
Output: [28,26]
'''


def smallestDiffernce(arrayOne, arrayTwo):
    arrayTwo.sort()
    arrayOne.sort()
    smallestdiff = 100000000
    result = []
    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            currentdiff = ((arrayOne[i]) - (arrayTwo[j]))
            currentdiff = abs(currentdiff)
            if currentdiff <= smallestdiff:
                smallestdiff = currentdiff
                result.append(arrayOne[i])
                result.append(arrayTwo[j])
    return result[-2:]


def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if smallest>current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair



one = [-1, 5, 10, 20, 3]
two = [26, 134, 135, 15, 17]

print(smallestDifference(one, two))