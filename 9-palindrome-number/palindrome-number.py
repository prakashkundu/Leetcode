class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        y = s[::-1]

        if y == s:
            return True
        else:
            return False