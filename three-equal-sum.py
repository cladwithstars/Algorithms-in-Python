def canThreePartsEqualSum(arr):
        """
        Return whether we can divide the array into three contiguous nonoverlapping subsets that sum to the same number. 
        [1, 1, 1] -> True. Subsets are [1], [1], [1], they all sum to 1. 
        [2, 4, 5, 7, 10] -> False. 
        
        """
        target = sum(arr) / 3
        
        if sum(arr) % 3 != 0:
            return False
        
        for i in range(1, len(arr) -1):
            startSum = sum(arr[0:i])
            if startSum == target: 
                for j in range(i+1, len(arr)):
                    midSum = sum(arr[i:j])
                    if midSum == target:
                        if sum(arr[j:]) == target:
                            return True

        return False
      
                
L = [18,12,-18,18,-19,-1,10,10]
print(canThreePartsEqualSum(L))