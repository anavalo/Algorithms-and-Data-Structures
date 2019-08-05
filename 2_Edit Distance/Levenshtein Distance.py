''' Write a function that takes in two strings and returns the minimum number of edit operations that need to
be performed on the first string to obtain the second string. There are three edit operations: insertion of a character,
 deletion of a character, and substitution of a character for another.'''


def levenshteinDistance(s1, s2):
    # built the matrix, we add +1 because of the positions '' and '' at the beginning of the matrix .
    matrix = [[x for x in range(len(s1)+1)] for y in range(len(s2)+1)]
    for i in range(1, len(s2)+1):
        matrix[i][0] = matrix[i-1][0]+1

    # go through the matrix:
    for i in range(1, len(s2)+1):
        for j in range(1, len(s1)+1):
            if s2[i-1] == s1[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])
    return matrix[-1][-1]




s1 = 'abc'
s2 = 'yabd'

print(levenshteinDistance(s1,s2))