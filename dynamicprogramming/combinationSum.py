
def combinationSum(candidates, target):
    res = []
    def dfs(nums, target, path):
        if target < 0:
            return # backtracking (reached a 'dead end')
        if target == 0:
            res.append(path)
        for i in range(len(nums)):
            dfs(nums[i:], target - nums[i], path + [nums[i]])
    dfs(candidates, target, [])
    return res

candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target)) #expect 
