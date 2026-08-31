class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxHeightSeen = 0
        i = 0
        j = len(heights) - 1
        while i != j:
            maxHeight = min(heights[i], heights[j])
            vol = (j - i)  * maxHeight
            if (vol) > maxHeightSeen:
                maxHeightSeen = vol
            if heights[i] < heights[j]:
                i += 1
            elif heights[j] < heights[i]:
                j -= 1
            elif ((heights[i+1] - heights[i]) < (heights[j-1] - heights[j])):
                i += 1
            elif ((heights[i+1] - heights[i]) > (heights[j-1] - heights[j])):
                j -= 1
            else:
                i += 1
        return maxHeightSeen

          