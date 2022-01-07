def isSubsequence(s, t):
    """
    (1) First check if s is a subset of t. If not, return False 
    
    (2) Now that we know all the characters in s are in t as well, we just need to make sure that the order is right.
    I.e., we need to ensure that the first character in s also appears first in t, second character in s also appears second in t,
    and so on.
    We can use python's index() method here and just compare all in t. 
    """
    currString = ""
    sIdx = 0 # keep track of where we are in the s string
    tIdx = 0 # keep track of where we are in the t string
    while sIdx < len(s) and tIdx < len(t):
        if s[sIdx] == t[tIdx]: #found a match for the ch of s at idx sIdx, so can move on
            currString += s[sIdx]
            tIdx += 1
            sIdx += 1
        else: #not a match
            tIdx += 1
    return currString == s
    
print(isSubsequence('leetcode', 'yyylyyyeyyyeyyytycyoyydye') )

print(isSubsequence('abc', 'hhbabc'))

print(isSubsequence('abc', 'hhacb'))
