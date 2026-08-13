class Solution:
    def longestCommonPrefix(self, strs):
        if strs is None or len(strs) == 0:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix
        