
class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        right_needed = 0

        for ch in s:
            if ch == '(':
                if right_needed % 2 == 1:
                    insertions += 1
                    right_needed -= 1

                right_needed += 2

            else:
                right_needed -= 1

                if right_needed < 0:
                    insertions += 1
                    right_needed = 1

        return insertions + right_needed
        