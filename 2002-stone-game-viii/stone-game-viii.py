class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)

        # Prefix sum
        for i in range(1, n):
            stones[i] += stones[i - 1]

        # Take all stones
        ans = stones[-1]

        # DP from right to left
        for i in range(n - 2, 0, -1):
            ans = max(ans, stones[i] - ans)

        return ans
        