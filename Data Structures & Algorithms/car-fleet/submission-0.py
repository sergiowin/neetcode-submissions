class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed))[::-1]
        stack = []
        for pos, spd in cars:
            cycles = (target - pos) / spd

            if not stack or cycles > stack[-1]:
                stack.append(cycles)
        
        return len(stack)

        # usDict = {}
        # ## create dict with all pos and speed pairs
        # for i in range(len(position)):
        #     usDict[position[i]] = speed[i]
        # sDict = {}
        # ## create new dictionary that is sorted by key
        # for key, value in usDict.items():
        #     sDict[key] = value
        # ##now that it has been sorted in nlogn time we can iterate over and it wont add to time complexity because the dominating factor is nlogn
        # stack = []
        # for key, value in sDict.items():
        #     cycles = math.ceil((target - key) / value)
        #     if not stack:
        #         stack.append(cycles)
        #     elif cycles < stack[-1]:
        #         ##clear stack and add to group
        #         while stack:
        #             stack.pop()
        #         groups += 1
        #         stack.append(cycles)
        #     ##return if equal because when they arrive at the destination at the same time it counts!!    
        #     elif cycles >= stack[-1]:
        #         ## just add on because it will combine with the previous group
        #         stack.append(cycles)
        # ## add one because there should be atleast one remaining car inside
        # return groups + 1
