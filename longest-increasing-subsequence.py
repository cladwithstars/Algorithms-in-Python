def lengthOfLIS(nums):
        """
        Write a helper function that checks the LIS starting at a particular index in nums
        
        The function takes in a list and returns the longest increasing subsequence starting at index 0 of that list 
        
        Then all we have to do is return the max length list of all these helper function results to get our final answer
        """
        # def helper(l):
        #     currMax = 1
        #     for i in range(len(l)):
        #         currLen = 1
        #         j = i + 1
        #         while j < len(l):
        #             if l[j] > l[i]:
        #                 j += 1
        #                 currLen += 1
        #                 if currLen > currMax:
        #                     currMax = currLen
        #             else:
        #                 if currLen > currMax:
        #                     currMax = currLen
        #                 j+=1
        #                 currLen = 0
        #             j = i + 2
        
        #     return currMax

        def helper(l):
            currMax = 1
            for i in range(len(l)):
                currLen = 1
                for j in range(i + 1, len(l)):
                    print(i, j, currLen, currMax)
                    if l[j] > l[i]:
                        j += 1
                        currLen += 1
                        if currLen > currMax:
                            currMax = currLen
                    else:
                        if currLen > currMax:
                            currMax = currLen
                        j+=1
                        currLen = 0
        
            return currMax

        return helper(nums)


print(lengthOfLIS([1, 2, 3, 4]))

print(lengthOfLIS([2, 2, 3, 4]))

print(lengthOfLIS([4, 2, 3, 4]))

print(lengthOfLIS([7, 2, 1, 4, 8]))

print(lengthOfLIS([10,9,2,5,3,7,101,18]))

