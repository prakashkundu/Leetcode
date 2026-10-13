from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=abs, reverse=True)

        n = len(nums)
        ans = 0

        for i, num in enumerate(nums):
            if i < (n + 1) // 2:
                ans += num * num
            else:
                ans -= num * num

        return ans
        