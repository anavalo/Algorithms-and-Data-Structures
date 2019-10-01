'''Write a function that takes a non-empty string and returns a boolean representing whether or not the string is a
palindrome'''


def isPalindrome(string):
    leftindex = 0
    rightindex = len(string) - 1
    while leftindex<rightindex:
        if string[leftindex] != string[rightindex]:
            return False
        leftindex += 1
        rightindex -=1
    return True

#recursivly:

def palindrome(string, i=0):
    j = len(string)-i-1
    return True if i>=j else string[i]==string[j] and palindrome(string, i+1)