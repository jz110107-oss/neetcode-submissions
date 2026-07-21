class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxheight = 0

        for i in range(len(heights)):
            if not stack or stack[-1][0] <= heights[i]:
                stack.append((heights[i], i))
            else:
                while stack and stack[-1][0] > heights[i]:
                    height, index = stack.pop()
                    maxheight = max(maxheight, height * (i-index))
                stack.append((heights[i], index))
        
        while stack:
            height, index = stack.pop()
            maxheight = max(maxheight, height * (len(heights)-index))
        
        return maxheight
            
            
        