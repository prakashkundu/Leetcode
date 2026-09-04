class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)

        # right[i] = minimum value from i to the end
        right = [0] * n
        right[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            right[i] = min(nums[i], right[i + 1])

        # Find the first stable index
        leftMax = nums[0]

        for i in range(n):
            leftMax = max(leftMax, nums[i])

            instability = leftMax - right[i]

            if instability <= k:
                return i

        return -1