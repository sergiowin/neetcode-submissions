class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberSeq = defaultdict(int)
        absoluteStartNums = []
        globalStreak = 0
        localStreak = 1
        i = 0
        while i in range(len(nums)):
            numberSeq[nums[i]] += 1
            i += 1
        i = 0
        for key in numberSeq:
            if key - 1 not in numberSeq:
             absoluteStartNums.append(key)
        for num in absoluteStartNums:
            curNum = num + 1 
            while curNum in numberSeq:
                curNum += 1
                localStreak += 1
            if localStreak > globalStreak:
                globalStreak = localStreak
            localStreak = 1           
        return globalStreak

