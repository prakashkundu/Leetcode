class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            lh = height[l]
            rh = height[r]

            min_h = min(lh, rh)
            length = r - l
            curr_area = min_h * length

            max_area = max(max_area, curr_area)

            if lh < rh:
                l += 1
            else:
                r -= 1

        return max_area