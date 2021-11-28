def lengthOfLongestSubstring(s):
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

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bb"))