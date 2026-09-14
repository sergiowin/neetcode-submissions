class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] ## will keep track of index and height of each rectange, montonic stack
        maxArea = 0
        for i, h in enumerate(heights):
            if not stack:
                stack.append((i, h)) ## if stack is empty just add to the stack
            elif h >= stack[-1][1]:
                stack.append((i, h)) ## if a new element is greater than the one before, just add on 
            elif h < stack[-1][1]: 
                appendIndex = 0
                while stack and h < stack[-1][1]:## if a new element is less than
                    popArea = (i - stack[-1][0]) * stack[-1][1]
                    if popArea > maxArea:
                        maxArea = popArea
                    appendIndex = stack[-1][0]
                    stack.pop(-1)
                stack.append((appendIndex, h)) ##appends at this index to account for the extension of this height to the left
        while stack:
          index, height = stack.pop()
          popArea = (len(heights) - index) * height
          if popArea > maxArea:
            maxArea = popArea
        return maxArea
                    
