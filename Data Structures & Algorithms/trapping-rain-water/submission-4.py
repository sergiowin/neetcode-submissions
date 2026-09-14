class Solution:
    def trap(self, height: List[int]) -> int:
        ## better planning two ptr solve, too inefficient bc list slicing sux
        mL = []
        mR = []
        waterCap = 0
        for h in height:
            if not mL:
                mL.append(h)
            else:
                mL.append(max(h, mL[-1]))
        for h in reversed(height):
            if not mR:
                mR.append(h)
            else:
                mR.append(max(h, mR[-1]))
        mR.reverse()
        
        for i, h in enumerate(height):
            area = min(mL[i], mR[i]) - h
            ## if it is negative, then dont add it...
            if area > 0:
                waterCap += area

        return waterCap
            











        ##chopped 30 min almost solve
#         stack = [] ## holds tuples of, index, height
#         spaceOcc = 0
#         waterCap = 0 ## total counter of the amount of water held so far

#         for i, h in enumerate(height): ## i = index, h = height of rect
            
#             if h == 0: ## is not relevant
#                 continue
#             elif not stack: ##if empty append
#                 stack.append((i, h))
#             elif h >= stack[0][1]: ## if the current height is greater than the first height in the stack
#                 maxRectHeight = min(stack[0][1], h)
#                 areaCalc = ((((i - stack[0][0]) - 1) * maxRectHeight) - spaceOcc)
#                 waterCap += areaCalc ## adds to water cap - space occupied by any rects inbetween
#                 while stack: ## clears stack
#                     stack.pop(-1)
#                 spaceOcc = 0 ## resets spaceOcc to 0 for new calcs
#                 stack.append((i,h))
#             elif h < stack[0][1]:
#                 spaceOcc += h
#                 stack.append((i,h))

# ##refine cleanup logic
# ##misses sub containers of water.. cant be based strictly on last index
         
#         for i, h in stack: ## has to have atleast three things because otherwise cant store any water
#             if 
#                 maxRectHeight = min(stack[0][1], h)
#                 areaCalc = ((((i - stack[0][0]) - 1) * maxRectHeight) - spaceOcc)
#                 waterCap += areaCalc ## adds to water cap - space occupied by any rects inbetween
#                 while stack: ## clears stack
#                     stack.pop(-1)
#                 spaceOcc = 0 ## resets spaceOcc to 0 for new calcs
#                 stack.append((i,h))

            
#         return waterCap
#         ## append everything and only do comparisons for first iteration based on first index
#         ## cleanup logic will handle any possible missed water.