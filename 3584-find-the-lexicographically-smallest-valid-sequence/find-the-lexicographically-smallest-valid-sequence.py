class Solution:
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)

        # suf[i] = maximum number of characters of word2
        # that can be matched starting from word1[i]
        suf = [0] * (n + 1)

        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                suf[i] = suf[i + 1] + 1
                j -= 1
            else:
                suf[i] = suf[i + 1]

        ans = []
        pos = 0
        mismatch = False

        for j in range(m):
            # First try the earliest exact match.
            while pos < n and word1[pos] != word2[j]:
                # We can use this position as our one mismatch
                # only if the remaining word2 can be matched.
                if not mismatch and suf[pos + 1] >= m - j - 1:
                    ans.append(pos)
                    mismatch = True
                    pos += 1
                    break

                pos += 1

            else:
                if pos >= n:
                    return []

                ans.append(pos)
                pos += 1
                continue

            if len(ans) != j + 1:
                return []

        return ans
        