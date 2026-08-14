class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        minPriInd = 0;
        maxProf = 0;
        while i < len(prices):
            if prices[i] - prices[minPriInd] > maxProf:
                maxProf = prices[i] - prices[minPriInd]
            if prices[i] < prices[minPriInd]:
                minPriInd = i
            i += 1
        return maxProf

            
