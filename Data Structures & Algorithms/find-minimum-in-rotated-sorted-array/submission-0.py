class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2

            if (nums[mid] > nums[high]):
                # this implies that the min value is between the mid point and the high point so move low up
                low = mid + 1
            else:
                high = mid
                
        return nums[low]
                
                