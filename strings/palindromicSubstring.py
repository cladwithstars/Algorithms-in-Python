def longestPalindrome(s):
    def helper(midIdx, evenLength):
        '''
        return longest palindromic substring in string s with middle index at midIdx
        '''
        i = midIdx - 1
        j = midIdx + 1 if not evenLength else midIdx
        currLongest = s[midIdx]
        while i > -1 and j < len(s) and s[i] == s[j]:
            currLongest = s[i:j + 1]
            i-=1
            j+=1
        return currLongest
    currLongestPalindrome = ''
    for i in range(len(s)):
        p1 = helper(i, False) #we need to call the helper function once when NOT considering even length strs 
        p2 = helper(i, True)  # and once again when considering even length strs
        p = p1 if len(p1) > len(p2) else p2
        if len(p) > len(currLongestPalindrome):
            currLongestPalindrome = p
    return currLongestPalindrome

s = "babad"
print(longestPalindrome(s)) #expect bab

s = "cbbd"
print(longestPalindrome(s)) #expect bb

s = 'bb'
print(longestPalindrome(s)) # expect bb

s = "aaaa"
print(longestPalindrome(s)) #expect aaaa

