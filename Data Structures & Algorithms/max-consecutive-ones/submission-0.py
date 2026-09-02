class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLen = 0
        curLen = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                curLen += 1
            else:
                curLen = 0
            if curLen > maxLen:
                maxLen = curLen
        return maxLen