import java.util.*;

class Solution {
    public List<List<Integer>> fourSum(int[] a, int target) {

        if (a == null || a.length < 4) {
            return new ArrayList<>();
        }

        Arrays.sort(a);

        List<List<Integer>> result = new ArrayList<>();

        int n = a.length;

        for (int i = 0; i < n - 3; i++) {

            // Skip duplicate i
            if (i > 0 && a[i] == a[i - 1]) {
                continue;
            }

            for (int j = i + 1; j < n - 2; j++) {

                // Skip duplicate j
                if (j > i + 1 && a[j] == a[j - 1]) {
                    continue;
                }

                int left = j + 1;
                int right = n - 1;

                while (left < right) {

                    long total = (long) a[i] + a[j] + a[left] + a[right];

                    if (total == target) {

                        result.add(Arrays.asList(
                            a[i],
                            a[j],
                            a[left],
                            a[right]
                        ));

                        left++;
                        right--;

                        // Skip duplicate left
                        while (left < right && a[left] == a[left - 1]) {
                            left++;
                        }

                        // Skip duplicate right
                        while (left < right && a[right] == a[right + 1]) {
                            right--;
                        }

                    } else if (total < target) {
                        left++;

                    } else {
                        right--;
                    }
                }
            }
        }

        return result;
    }
}