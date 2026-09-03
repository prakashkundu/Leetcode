class Solution {
    public boolean uniformArray(int[] nums1) {

        // Step 1: Find the minimum element
        int min_val = nums1[0];

        for (int x : nums1) {
            if (x < min_val) {
                min_val = x;
            }
        }

        // Step 2: If minimum is odd
        if (min_val % 2 != 0) {
            return true;
        }

        // Step 3: If minimum is even,
        // all elements must be even
        for (int x : nums1) {
            if (x % 2 != 0) {
                return false;
            }
        }

        return true;
    }
}