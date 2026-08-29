class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        arr = sorted((num, i) for i, num in enumerate(nums))

        ans = [0] * n
        start = 0

        while start < n:
            end = start

            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            indices = sorted(arr[i][1] for i in range(start, end + 1))
            values = sorted(arr[i][0] for i in range(start, end + 1))

            for i in range(len(indices)):
                ans[indices[i]] = values[i]

            start = end + 1

        return ans