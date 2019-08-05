''' Write a function that takes in two strings and returns the minimum number of edit operations that need to
be performed on the first string to obtain the second string. There are three edit operations: insertion of a character,
 deletion of a character, and substitution of a character for another.'''


def levenshteinDistance(s1, s2):
    if s1==s2:
        return 0
    elif len(s1) == 0 or len(s2) ==0:
        return max(len(s1), len(s2))
    else:








s1 = 'abc'
s2 = 'yabd'

print(levenshteinDistance(s1,s2))