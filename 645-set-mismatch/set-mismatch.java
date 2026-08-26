import java.util.HashSet;

class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        int duplicate = 0;
        int missing = 0;
        HashSet<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) {
                duplicate = num;
            }
            seen.add(num);
        }
        for (int i = 1; i <= n; i++) {
            if (!seen.contains(i)) {
                missing = i;
            }
        }
        return new int[]{duplicate, missing};
    }
}