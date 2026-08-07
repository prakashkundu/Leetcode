class Solution(object):
    def smallestNumber(self, num, t):
        # Count prime factors of t: 2, 3, 5, 7
        need = [0, 0, 0, 0]
        primes = [2, 3, 5, 7]

        for i in range(4):
            while t % primes[i] == 0:
                need[i] += 1
                t //= primes[i]

        # If t has any other prime factor, impossible
        if t != 1:
            return "-1"

        # Factor contribution of digits 0..9
        factors = [
            [0, 0, 0, 0],  # 0
            [0, 0, 0, 0],  # 1
            [1, 0, 0, 0],  # 2
            [0, 1, 0, 0],  # 3
            [2, 0, 0, 0],  # 4
            [0, 0, 1, 0],  # 5
            [1, 1, 0, 0],  # 6
            [0, 0, 0, 1],  # 7
            [3, 0, 0, 0],  # 8
            [0, 2, 0, 0]   # 9
        ]

        def subtract(a, b):
            return [
                max(0, a[0] - b[0]),
                max(0, a[1] - b[1]),
                max(0, a[2] - b[2]),
                max(0, a[3] - b[3])
            ]

        def factor_count(cnt):
            # 2^3 -> 8
            count8 = cnt[0] // 3
            remaining2 = cnt[0] % 3

            # 3^2 -> 9
            count9 = cnt[1] // 2
            count3 = cnt[1] % 2

            # 2^2 -> 4
            count4 = remaining2 // 2
            count2 = remaining2 % 2

            # 2 * 3 -> 6
            count6 = 0

            if count2 == 1 and count3 == 1:
                count2 = 0
                count3 = 0
                count6 = 1

            # 3 * 4 -> 6 * 2
            if count3 == 1 and count4 == 1:
                count2 = 1
                count6 = 1
                count3 = 0
                count4 = 0

            return [
                count2,   # digit 2
                count3,   # digit 3
                count4,   # digit 4
                cnt[2],   # digit 5
                count6,   # digit 6
                cnt[3],   # digit 7
                count8,   # digit 8
                count9    # digit 9
            ]

        def construct(cnt):
            # cnt corresponds to digits 2..9
            result = []

            for digit in range(2, 10):
                result.append(str(digit) * cnt[digit - 2])

            return ''.join(result)

        def total_digits(cnt):
            return sum(cnt)

        def is_subset(a, b):
            for i in range(4):
                if b[i] < a[i]:
                    return False
            return True

        # Minimum digits required for t
        required_digits = factor_count(need)

        # If even the shortest valid number is longer than num,
        # it is automatically the smallest valid answer.
        if total_digits(required_digits) > len(num):
            return construct(required_digits)

        # Count prime factors contributed by the whole num
        prefix = [0, 0, 0, 0]

        for ch in num:
            d = int(ch)

            for k in range(4):
                prefix[k] += factors[d][k]

        # Find first zero
        first_zero = num.find('0')

        if first_zero == -1:
            first_zero = len(num)

            # num itself is valid
            if is_subset(need, prefix):
                return num

        # Try changing a digit from right to left
        for i in range(len(num) - 1, -1, -1):

            d = int(num[i])

            # Remove current digit from prefix
            prefix = subtract(prefix, factors[d])

            space = len(num) - 1 - i

            # We cannot keep a prefix after the first zero
            if i > first_zero:
                continue

            # Try the smallest digit bigger than current digit
            for bigger in range(d + 1, 10):

                # Factors already supplied by:
                # prefix + bigger
                used = [
                    prefix[0] + factors[bigger][0],
                    prefix[1] + factors[bigger][1],
                    prefix[2] + factors[bigger][2],
                    prefix[3] + factors[bigger][3]
                ]

                # What factors are still required?
                remaining = subtract(need, used)

                # Convert remaining factors into actual digits
                suffix_digits = factor_count(remaining)

                required = total_digits(suffix_digits)

                # We have 'space' positions after this digit
                if required <= space:

                    # Extra positions can be filled with 1
                    ones = space - required

                    return (
                        num[:i]
                        + str(bigger)
                        + ('1' * ones)
                        + construct(suffix_digits)
                    )

        # No same-length answer.
        # Make a number with one extra digit.
        suffix_digits = factor_count(need)

        ones = len(num) + 1 - total_digits(suffix_digits)

        return ('1' * ones) + construct(suffix_digits)