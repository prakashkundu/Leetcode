class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {

        int n = nums.length;

        Set<Integer> seen = new HashSet<>();

        for (int num : nums) {
            seen.add(num);
        }

        List<Integer> ans = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            if (!seen.contains(i)) {
                ans.add(i);
            }
        }

        return ans;
    }
}