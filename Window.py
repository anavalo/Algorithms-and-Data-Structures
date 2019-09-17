'''
write a function returns "windows" of items from a given list. Your function should takes a list and a number n and r
eturn a new list of tuples, each containing "windows" of n consecutive items. That is, each tuple should contain the
current item and the n-1 items after it.

Here are some examples:

>numbers = [1, 2, 3, 4, 5, 6]
>window(numbers, 2)
[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
>window(numbers, 3)
[(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
>window(numbers, 4)
[(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)]
Your window function should return an empty list if the given n is 0. It should also be able to accept strings,
tuples and other sequences.
'''


def helper(array, n):
    if n == 1:
        return [array]
    else:
        return [array] + helper(array[1:], n-1)


def windows(array, n):
    x = helper(array, n)
    return list(zip(*x))


numbers = [1, 2, 3, 4, 5, 6]
print(windows(numbers, 2))