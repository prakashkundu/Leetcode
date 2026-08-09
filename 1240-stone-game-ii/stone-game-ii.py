class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # Suffix sum
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dfs(i, M):
            if i >= n:
                return 0

            if (i, M) in memo:
                return memo[(i, M)]

            best = 0

            # Take X piles, where 1 <= X <= 2 * M
            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break

                # Current player gets:
                # remaining stones - opponent's best result
                opponent = dfs(i + X, max(M, X))
                current = suffix[i] - opponent

                best = max(best, current)

            memo[(i, M)] = best
            return best

        return dfs(0, 1)
        