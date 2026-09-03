class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if dividend == divisor:
            return 1

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp = temp << 1
                multiple = multiple << 1

            dividend -= temp
            result += multiple

        if negative:
            result = -result

        if result > 2**31 - 1:
            return 2**31 - 1

        if result < -2**31:
            return -2**31

        return result