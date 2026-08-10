class Solution {
    public boolean isPalindrome(int x) {
        String s = String.valueOf(x);
        String y = new StringBuilder(s).reverse().toString();

        if (y.equals(s)) {
            return true;
        } else {
            return false;
        }
    }
}