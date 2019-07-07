'''write a function that takes in an array of unique integers and returns an array of all permutations of those
integers. If the input is empty, the function should return an empty array'''

def getPermutations(array):
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations

def permutationsHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1:]
            newPermutation = currentPermutation + [array[i]]
            permutationsHelper(newArray, newPermutation, permutations)



mmm = [1,2,3]



print(mmm[1:])






# print(getPermutations(mmm))
