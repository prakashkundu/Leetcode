class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        t = list(range(numRows)) + list(range(numRows - 2, 0, -1))

        r = [""] * numRows

        for i, char in enumerate(s):
            r[t[i % len(t)]] += char

        return ''.join(r)
        