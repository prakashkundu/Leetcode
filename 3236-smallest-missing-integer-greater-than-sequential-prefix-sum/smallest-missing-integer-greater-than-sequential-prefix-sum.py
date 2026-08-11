class Solution(object):
    def missingInteger(self, nums):
        # Find sequential prefix sum
        total = nums[0]

        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        # Put all numbers into a set
        num_set = set(nums)

        # Find the smallest missing integer
        while total in num_set:
            total += 1

        return total
        