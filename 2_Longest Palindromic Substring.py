'''Write a function that, given a string, returns its longest palindromic substring.
A palindrome is defined as a string that is written the same forward and backward.
Assume that there will only be one longest palindromic substring.
'''


def longestPalindromicSubstring(string):
    currentLongest=[0, 1]
    for i in range(1, len(string)):
        odd = getlongestpalindrome(string, i-1, i+1)
        even = getlongestpalindrome(string, i-1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
    return string[currentLongest[0]:currentLongest[1]]

def getlongestpalindrome(string, lidx, ridx):
    while lidx>=0 and ridx<len(string):
        if string[lidx] != string[ridx]:
            break
        lidx -=1
        ridx +=1
    return [lidx+1, ridx]


print(longestPalindromicSubstring('tracecars'))
