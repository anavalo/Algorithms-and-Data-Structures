'''Write a function that takes in a string made up of brackets ("(", "[", "{", ")", "]", and "}")
and other optional characters. The function should return a boolean representing whether or not the
string is balanced in regards to brackets. A string is said to be balanced if it has as many opening
brackets of a given type as it has closing brackets of that type and if no bracket is unmatched.
Note that a closing bracket cannot match a corresponding opening bracket that comes after it.
Similarly, brackets cannot overlap each other as in "[(])".'''





def helper(string):
    dict = {'(': ')',
            '[': ']',
            '{': '}'}
    newstring = ''
    for char in string:
        if char in dict:
            newstring = string.replace(char, '', 1).replace(dict[char], '', 1)
            helper(newstring)
    return newstring

def balancedBrackets(string):
    return helper(string)




print(balancedBrackets('()[]{}{'))
