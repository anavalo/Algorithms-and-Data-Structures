def fourNumberSum(array, targetSum):
    pairsums = {}
    quadriplets = []
    for i in range(0, len(array)-1):
        for j in range(i+1, len(array)):
            if not (array[i] + array[j]) in pairsums:
                pairsums[(array[i] + array[j])] = [[array[i], array[j]]]
            else:
                pairsums[(array[i] + array[j])].append([array[i], array[j]])
    for key, value in pairsums.items():
        result = targetSum - key
        if result in pairsums:
            quadriplets.append([pairsums[key], pairsums[result]])
    return quadriplets



print(fourNumberSum([7, 6, 4, -1, 1, 2], 16))

