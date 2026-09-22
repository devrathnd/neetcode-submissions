class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        maxVol = 0

        while i < j:
            volume = (j-i) * min(heights[i], heights[j])
            maxVol = max(maxVol, volume)

            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1

        return maxVol