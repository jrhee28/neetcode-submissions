class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        l = 0
        r = len(heights) -1
        while l < r:
            output = max((r-l) * min(heights[l],heights[r]), output)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -=1

        return output