class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        duplicate = 0
        missing = 0
        seen = set()
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
        for i in range(1, n + 1):
            if i not in seen:
                missing = i
        return [duplicate, missing]