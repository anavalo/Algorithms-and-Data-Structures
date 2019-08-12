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

mmmm = [3, 5, 12, 3, 4, 4, 7, 3, 8, 7, 8, 6, 10, 9, 4]
print(quicksort(mmmm))