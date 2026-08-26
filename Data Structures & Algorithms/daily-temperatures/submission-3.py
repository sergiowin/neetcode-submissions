class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        retList = [0] * (len(temperatures)) 
        stack.append(0)
        for i in range(1, len(temperatures)):
            while stack and (temperatures[i] > temperatures[stack[-1]]):
                oIndex = stack.pop()
                retList[oIndex] = i - oIndex
            stack.append(i)

        return retList
                