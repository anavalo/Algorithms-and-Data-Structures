'''Given a sorted list of positive numbers, find the smallest positive number that cannot be a sum of any subset in the list.'''

def findSmallest(array):
    hash = {}
    candidates = []
    for num in array:
        hash[num] = True
    for num in reversed(array):
        number = num-1
        while number in hash:
            number -= 1
        candidates.append(number)
    print(candidates)







print(findSmallest([1, 2, 8, 9, 10]))