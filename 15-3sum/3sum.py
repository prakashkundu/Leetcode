class Solution:
    def threeSum(self, a):
        if a is None or len(a) < 3:
            return []

        a.sort()

        result = []

        for i in range(len(a) - 2):

            # Skip duplicates for i
            if i > 0 and a[i] == a[i - 1]:
                continue

            left = i + 1
            right = len(a) - 1

            while left < right:

                total = a[i] + a[left] + a[right]

                if total == 0:
                    result.append([a[i], a[left], a[right]])

                    left += 1
                    right -= 1

                    # Skip duplicates at left
                    while left < right and a[left] == a[left - 1]:
                        left += 1

                    # Skip duplicates at right
                    while left < right and a[right] == a[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result