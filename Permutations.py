import math
import random
import itertools

def getPermutations(array):
    return  list(itertools.permutations(array))

    # comb = [None] * (math.factorial(len(array)))
    # times = int(math.factorial((len(array)))/len(array))
    # current = array[:]















mmm = [1,2,3]
print(getPermutations(mmm))
