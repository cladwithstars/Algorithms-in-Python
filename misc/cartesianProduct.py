def product(nums):
    '''
    return cartesian product of nums
    '''
    res = []
    def dfs(path):
        if len(path) == len(nums):
            res.append(path)
            return # backtracking (reached a 'dead end')
        for i in range(len(nums)):
            dfs(path + [nums[i]])
    dfs([])
    return res

print(product([1, 2, 3]))
print(product([1, 2]))