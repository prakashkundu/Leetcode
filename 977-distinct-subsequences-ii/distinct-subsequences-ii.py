class Solution:
    def distinctSubseqII(self, s):
        MOD = 1000000007

        dp = [0] * 26
        total = 0

        for c in s:
            i = ord(c) - ord('a')

            new = (total + 1) % MOD
            total = (total - dp[i] + new) % MOD
            dp[i] = new

        return total