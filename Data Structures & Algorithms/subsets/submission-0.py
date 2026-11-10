class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        retList = []
        
        curSub = []
        def dfs(i):
            if i >= len(nums):
                retList.append(curSub.copy())
                return
            
            #choice 1: include number at index i
            curSub.append(nums[i])
            dfs(i + 1)
            
            #now take the number off
            curSub.pop()
            dfs(i + 1)
        dfs(0)
        return retList