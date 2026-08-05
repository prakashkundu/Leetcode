class Solution(object):
    def twoSum(self, nums, target):
        d = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in d:
                return [d[diff], i]

            d[nums[i]] = i