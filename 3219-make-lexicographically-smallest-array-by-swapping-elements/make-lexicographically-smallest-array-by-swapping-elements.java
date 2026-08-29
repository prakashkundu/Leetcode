class Solution {
    public int[] lexicographicallySmallestArray(int[] nums, int limit) {
        int n = nums.length;

        // Store {value, original index}
        int[][] arr = new int[n][2];

        for (int i = 0; i < n; i++) {
            arr[i][0] = nums[i];
            arr[i][1] = i;
        }

        // Sort by value
        Arrays.sort(arr, (a, b) -> Integer.compare(a[0], b[0]));

        int[] ans = new int[n];
        int start = 0;

        while (start < n) {
            int end = start;

            // Find one group
            while (end + 1 < n &&
                   arr[end + 1][0] - arr[end][0] <= limit) {
                end++;
            }

            // Get indices
            int size = end - start + 1;
            int[] indices = new int[size];
            int[] values = new int[size];

            for (int i = 0; i < size; i++) {
                indices[i] = arr[start + i][1];
                values[i] = arr[start + i][0];
            }

            // Sort original indices
            Arrays.sort(indices);

            // values are already sorted

            // Put smallest values at smallest indices
            for (int i = 0; i < size; i++) {
                ans[indices[i]] = values[i];
            }

            start = end + 1;
        }

        return ans;
    }
}