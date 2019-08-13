'''Write a function that takes in an array of integers and returns a sorted version of that array.
Use the Quick Sort algorithm to sort the array.'''

def quicksort(array):
    helper(array, 0, len(array)-1)
    return array

def helper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return
    pivotIdx = startIdx
    leftIdx = startIdx +1
    rightIdx = endIdx
    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx +=1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -=1
    swap(pivotIdx, rightIdx, array)
    leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx +1)
    if leftSubarrayIsSmaller:
        helper(array, startIdx, rightIdx -1)
        helper(array, rightIdx +1, endIdx)
    else:
        helper(array, rightIdx +1, endIdx)
        helper(array, startIdx, rightIdx - 1)

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def quicksort2(array):
    if len(array)<2:
        return array
    else:
        pivot = array[0]
        print('pivot is: ' + str(pivot))
        lesser = [x for x in array[1:] if x <= pivot]
        print('lesser is: ' + str(lesser))
        greater = [x for x in array[1:] if x > pivot]
        print ('greater is:' + str(greater))
    return quicksort2(lesser) + [pivot] + quicksort2(greater)

mmmm = [4, 7, 3, 1, 9, 5, 2, 8]

print(quicksort2(mmmm))