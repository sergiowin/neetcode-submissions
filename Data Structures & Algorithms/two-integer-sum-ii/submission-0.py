class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seenDiff = defaultdict(int)
        i = 0
        while i < len(numbers):
            diff = target - numbers[i]
            if numbers[i] in seenDiff.keys():
                return [seenDiff[numbers[i]] + 1,i + 1]
            seenDiff[diff] = i
            i += 1
