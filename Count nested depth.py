def flat(l):
    res = []
    for item in l:
        if type(item) == list:
            res.append(flat(item))
    print(res)
    if len(res) > 0:
        return 1 + max(res)
    return 1


print(flat([1,2,[3,4],5,[6,[5]],7]))
# print(flat([2]))
# print(flat([]))
# print(flat([[2]]))
# print(flat([3, 4, 5, [2, 4, [4, 5]], 6, [5]]))