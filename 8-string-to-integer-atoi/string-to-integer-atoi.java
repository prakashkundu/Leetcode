class Solution {
    public int myAtoi(String s) {

        int i = 0;
        int n = s.length();

        // Skip leading spaces
        while (i < n && s.charAt(i) == ' ') {
            i++;
        }

        // Sign
        int sign = 1;

        if (i < n && s.charAt(i) == '-') {
            sign = -1;
            i++;
        } else if (i < n && s.charAt(i) == '+') {
            i++;
        }

        int num = 0;

        // Convert digits
        while (i < n && Character.isDigit(s.charAt(i))) {

            int digit = s.charAt(i) - '0';

            // Check overflow
            if (num > (Integer.MAX_VALUE - digit) / 10) {
                if (sign == 1) {
                    return Integer.MAX_VALUE;
                } else {
                    return Integer.MIN_VALUE;
                }
            }

            num = num * 10 + digit;
            i++;
        }

        return num * sign;
    }
}