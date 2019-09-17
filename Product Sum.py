'''
Write a function that takes in a "special" array and returns its product sum. A "special" array is a non-empty array
that contains either integers or other "special" arrays. The product sum of a "special" array is the sum of its elements,
 where "special" arrays inside it should be summed themselves and then multiplied by their level of depth. For example,
  the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2y + 2z.
'''

def productSum(array, multiplier = 1):
    sum = 0
    for item in array:
        if type(item) == int:
            sum += item
        else:
            sum += productSum(item, multiplier + 1)
    return sum * multiplier



bbb= [[[[[[5]]]]]]

print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
print(productSum(bbb))