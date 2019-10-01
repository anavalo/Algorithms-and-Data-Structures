'''
Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of
numbers contained in that array. The first number in the output array should be the first number in the range while the
second number should be the last number in the range. A range of numbers is defined as a set of numbers that come
right after each other in the set of real integers. For instance, the output array [2, 6]
represents the range {2, 3, 4, 5, 6}, which is a range of length 5. Note that numbers do not need to be ordered
or adjacent in the array in order to form a range. Assume that there will only be one largest range.
'''

def largestrange(array):
    array.sort()
    lidx = 0
    ridx = 1
    lastright = 0
    hashtable = {}
    if len(array) == 1:
        return [array[0], array[0]]
    else:
        while ridx < len(array):
            if array[ridx] == array[ridx - 1] + 1 or array[ridx] == array[ridx-1]:
                lastright = ridx
                if ridx == len(array)-1:
                    hashtable[(ridx-lidx)] = [lidx, ridx]
            else:
                hashtable[(lastright-lidx)] = [lidx, lastright]
                lidx = ridx
                ridx = lidx + 1
            ridx += 1
        lastkey = sorted(hashtable.keys())[-1]
        return [array[hashtable[lastkey][0]], array[hashtable[lastkey][1]]]

# O(n) time + space:

def largestRange(array):
    hash={}
    result = []
    longestLenght = 0
    for num in array:
        hash[num] = True
    for num in array:
        if not hash[num]:
            continue
        hash[num] = False
        currentLenght = 1
        left = num - 1
        right = num + 1
        while left in hash:
            hash[left] = False
            currentLenght +=1
            left -=1
        while right in hash:
            hash[right] = False
            currentLenght +=1
            right +=1
        if currentLenght > longestLenght:
            longestLenght = currentLenght
            result = [left+1, right-1]
    return result


print(largestrange([19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]))
print(largestRange([19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]))