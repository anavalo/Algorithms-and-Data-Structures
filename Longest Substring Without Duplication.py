'''
Write a function that takes in a string and that returns its longest substring without duplicate characters.
Assume that there will only be one longest substring without duplication.
Sample input: "clementisacap"
Sample output: "mentisac"
'''


def longestSubString(string):
    lastSeen = {}
    longest = [0,1]
    startIdx = 0
    for i, char in enumerate(string):
        if char in lastSeen:
            startIdx = max(startIdx, lastSeen[char])
        if longest[1] - longest[0] < i + 1 - startIdx:
            longest = [startIdx, i+1]
        lastSeen[char] = i
    return string[longest[0]:longest[1]]

print(longestSubString('melenepopisantigiagiamouthnkalliopi'))









longestSubString("clementisacap")

