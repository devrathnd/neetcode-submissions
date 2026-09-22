class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxA = 0

        for i, h in enumerate(heights + [0]):
            left = i

            while stack and stack[-1][1] > h:
                lastIndex, lastH = stack.pop()
                maxA = max(maxA, lastH * (i - lastIndex))
                left = lastIndex
            
            stack.append((left, h))

        return maxA
