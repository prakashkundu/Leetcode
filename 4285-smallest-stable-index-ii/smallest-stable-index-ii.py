class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)

        # right[i] = minimum from i to the end
        right = [nums[-1]] * n

        for i in range(n - 2, -1, -1):
            right[i] = min(nums[i], right[i + 1])

        # Maximum from index 0 to i
        left = 0

        for i in range(n):
            left = max(left, nums[i])

            instability = left - right[i]

            if instability <= k:
                return i

        return -1
        