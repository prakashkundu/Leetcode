class Solution:
    def fourSum(self, a, target):
        if a is None or len(a) < 4:
            return []

        a.sort()
        result = []

        n = len(a)

        for i in range(n - 3):

            # Skip duplicate i
            if i > 0 and a[i] == a[i - 1]:
                continue

            for j in range(i + 1, n - 2):

                # Skip duplicate j
                if j > i + 1 and a[j] == a[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:

                    total = a[i] + a[j] + a[left] + a[right]

                    if total == target:
                        result.append([
                            a[i], a[j], a[left], a[right]
                        ])

                        left += 1
                        right -= 1

                        # Skip duplicate left
                        while left < right and a[left] == a[left - 1]:
                            left += 1

                        # Skip duplicate right
                        while left < right and a[right] == a[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return result