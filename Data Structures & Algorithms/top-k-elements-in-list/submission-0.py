class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurDict = defaultdict(int)
        for num in nums:
            occurDict[num] += 1
        
        topKlargestelements = heapq.nlargest(k, occurDict.items(), key=lambda item: item[1])

        return [num for num, occur in topKlargestelements]