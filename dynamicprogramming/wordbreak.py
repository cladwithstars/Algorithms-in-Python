def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1) 
    dp[0] = True #base case
    for i in range(len(s)):
        if dp[i]:
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict:
                    dp[j] = True
    print(dp)
    return dp[-1]

s = "leetcode"
wd = ["leetco","code", "leet"]

print(wordBreak(s, wd)) #expect True