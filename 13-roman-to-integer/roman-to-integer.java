class Solution {
    public int romanToInt(String s) {

        int[] values = new int[256];

        values['I'] = 1;
        values['V'] = 5;
        values['X'] = 10;
        values['L'] = 50;
        values['C'] = 100;
        values['D'] = 500;
        values['M'] = 1000;

        int r = 0;

        for (int i = 0; i < s.length(); i++) {

            if (i + 1 < s.length() && values[s.charAt(i)] < values[s.charAt(i + 1)]) {
                r = r - values[s.charAt(i)];
            } else {
                r = r + values[s.charAt(i)];
            }
        }

        return r;
    }
}