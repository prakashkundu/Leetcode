class Solution:
    def maxPalindromes(self, s, k):
        n = len(s)

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        # dp[i] = maximum palindromes in s[0:i]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):

            # Don't take a palindrome ending here
            dp[i] = dp[i - 1]

            # Check palindrome of length k
            if i >= k and isPalindrome(i - k, i - 1):
                dp[i] = max(dp[i], dp[i - k] + 1)

            # Check palindrome of length k + 1
            if i >= k + 1 and isPalindrome(i - k - 1, i - 1):
                dp[i] = max(dp[i], dp[i - k - 1] + 1)

        return dp[n]
        