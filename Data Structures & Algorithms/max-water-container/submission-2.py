class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        res = 0


        while l < r:
            lh = heights[l]
            rh = heights[r]

            area = min(lh, rh) * (r - l)
            res = max(res, area)

            if lh < rh:
                l += 1
            else:
                r -= 1

        return res
