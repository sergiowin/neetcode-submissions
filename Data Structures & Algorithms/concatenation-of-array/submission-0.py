class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numsCopy = nums.copy()
        for num in numsCopy:
            nums.append(num)
        return nums