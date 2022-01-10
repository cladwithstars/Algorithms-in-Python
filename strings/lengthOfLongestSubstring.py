def lengthOfLongestSubstring(s):
    '''
    Given a string s, find the length of the longest substring without repeating characters.
    '''
    if s == "":
        return 0
    def longestStartingAt(st):
        seen = set()
        j = 0
        while j < len(st):
            if st[j] in seen:
                return len(seen)
            else:
                seen.add(st[j])
            j+=1
        return len(seen)
    
    return max([longestStartingAt(s[i:]) for i in range(len(s))])

print(lengthOfLongestSubstring("abcabcbb")) # abc is the string, so expect 3