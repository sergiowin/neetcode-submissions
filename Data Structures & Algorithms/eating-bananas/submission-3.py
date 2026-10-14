class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
     
        def canEat(speed) -> bool:
            totHrs = 0
            for p in piles:
                time = math.ceil(p / speed)
                totHrs += time
            if totHrs > h:
                return False
            else:
                return True

        low = 1
        high = max(piles)
        while low < high:
            mid = low + (high - low) // 2

            if canEat(mid):
                high = mid
            else: 
                low = mid + 1
        return low
