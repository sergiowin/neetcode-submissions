class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        retList = []
        i = 0
        product = math.prod(nums)
        while i < len(nums):
            if (nums[i] != 0):
                retList.append(product//nums[i])
            else:
                retList.append(math.prod((nums[:i] + nums[i + 1:])))
            
            i += 1
        return retList