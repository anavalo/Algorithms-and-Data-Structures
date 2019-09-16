



def fourNumberSum(array, targetSum):
    pairsums = {}
    quadriplets = []
    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)):
            currentSum = array[i] + array[j]
            diff = targetSum - currentSum
            if diff in pairsums:
                for pair in pairsums[diff]:
                    quadriplets.append(pair + [array[i], array[j]])
        for k in range(0, i):
            currentSum = array[k] + array[i]
            if currentSum not in pairsums:
                pairsums[currentSum] = [[array[k], array[i]]
            else:
                pairsums[currentSum].append([array[k], array[i]])

    return quadriplets




print(fourNumberSum([7, 6, 4, -1, 1, 2], 16))

