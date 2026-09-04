class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        retList = []
        ## sort the list of nums
        sNums = sorted(nums)
        for i in range(len(sNums)):
            if (i != 0) and sNums[i] == sNums[i-1]:
                continue
            elif sNums[i] > 0:
                break
            ## set relative to i so only numbers to the right of the current main index are looked at
            low = i + 1
            high = len(sNums) - 1
            while low < high:
                tot = sNums[i] + sNums[low] + sNums[high]
                if tot == 0:
                    retList.append([sNums[i], sNums[low], sNums[high]])
                    low += 1
                    high -= 1
                    while ((low < high) and(sNums[low] == sNums[low - 1])):
                        low += 1
                    while ((low < high) and (sNums[high] == sNums[high + 1])):
                        high -= 1
                elif tot < 0:
                    low += 1
                elif tot > 0:
                    high -= 1
        return retList
                
