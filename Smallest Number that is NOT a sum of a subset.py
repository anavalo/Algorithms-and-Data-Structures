'''Given a sorted list of positive numbers, find the smallest positive number that cannot be a sum of any subset in the list.'''


def findSmallest2(array):
    missing = []
    hash = {}
    for num in array:
        hash[num] = True
    for i in range(1, max(array)):
        if i not in hash:
            missing.append(i)
    for num in missing:
        if not isSum(array, num):
            return num


def isSum(array, target):
    if target == 0:
        return True
    if not len(array):
        return False
    if array[len(array)-1] > target:
        return isSum(array[:-1], target)
    return isSum(array[:-1], target-array[len(array)-1])


# result will always be +1 of the smallest sum
def findSmallest(nums):
    res = 1
    for n in nums:
        if n <= res:
            res += n
        else:
            break
    return res


print(findSmallest([1, 2, 3, 8, 9, 10]))
print(findSmallest2([1, 2, 3, 8, 9, 10]))
