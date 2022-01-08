def isSubsequence(s, t):
    """
    s, t are strings - return whether s is a subsequence of t. 
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
    
print(isSubsequence('leetcode', 'yyylyyyeyyyeyyytycyoyydye') ) #True

print(isSubsequence('abc', 'hhbabc')) #True

print(isSubsequence('abc', 'hhacb')) # False
