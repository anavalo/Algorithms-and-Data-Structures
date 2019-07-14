'''Write a function that, given a string, returns its longest palindromic substring.
A palindrome is defined as a string that is written the same forward and backward.
Assume that there will only be one longest palindromic substring.
'''


def longestPalindromicSubstring(string):
    reverse = string[::-1]
    palindrome = []

    for i in range(len(string)):
        for j in reversed(range(len(string)+1)):
            if string[i:j] in reverse:
                palindrome.append((string[i:j]))
    return max(palindrome, key=len)




print(longestPalindromicSubstring("banana"))