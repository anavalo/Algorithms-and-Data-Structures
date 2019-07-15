''' Write a function that takes in an array of unique integers and returns its powerset. The powerset P(X) of a set X
is the set of all subsets of X. For example, the powerset of [1,2] is[[],[1],[2],[1,2]].
Note that the sets in the powerset do not nedd to be in any particular order'''


def powerset(array):
    powersets = [[]]
    helper(array, [], powersets)
    return powersets

def helper(array, currentset, powersets):
    for i in range(len(array)):
        print('i is: ' + str(i) + '\n')
        newarray = array[i+1:]
        print('newarray is: ' + str(newarray) + '\n')
        newpowerset = currentset + [array[i]]
        print('newpowerset is: ' + str(newpowerset) + '\n')
        powersets.append(newpowerset)
        helper(newarray, newpowerset, powersets)


mmm = [1,2,3,5,6]
print(powerset(mmm))
