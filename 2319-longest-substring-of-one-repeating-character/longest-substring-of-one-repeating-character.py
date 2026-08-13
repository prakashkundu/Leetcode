class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):

        n = len(s)
        tree = [None] * (4 * n)

        # (left_char, right_char, prefix, suffix, best, length)
        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            lc1, rc1, pre1, suf1, best1, len1 = a
            lc2, rc2, pre2, suf2, best2, len2 = b

            prefix = pre1
            suffix = suf2
            best = max(best1, best2)

            if rc1 == lc2:
                best = max(best, suf1 + pre2)

                if pre1 == len1:
                    prefix = len1 + pre2

                if suf2 == len2:
                    suffix = suf1 + len2

            return (
                lc1,
                rc2,
                prefix,
                suffix,
                best,
                len1 + len2
            )

        def build(node, left, right):
            if left == right:
                tree[node] = (
                    s[left],
                    s[left],
                    1,
                    1,
                    1,
                    1
                )
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, left, right, index, char):
            if left == right:
                tree[node] = (
                    char,
                    char,
                    1,
                    1,
                    1,
                    1
                )
                return

            mid = (left + right) // 2

            if index <= mid:
                update(node * 2, left, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, right, index, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        ans = []

        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)
            ans.append(tree[1][4])

        return ans