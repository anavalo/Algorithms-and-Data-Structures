'''
Two words can be 'chained' if the last character of the first word is the same as the first character of the second word.

Given a list of words, determine if there is a way to 'chain' all the words in a circle.
'''

from collections import defaultdict


def dfs(array, visited, curr, start, length):
   if length == 1:
      if start[0] == start[-1]:
         return True
      else:
         return False
   visited.add(curr)

   for neighbor in array:
      if neighbor not in visited:
         return dfs(array, visited, curr, start, length-1)

   visited.remove(curr)
   return False


def chainedWords(array):
   graph = defaultdict(list)
   for word in array:
      graph[word[0]].append(word)
   return dfs(graph, set(), array[0], array[0], len(array))



print (chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))