class Solution {
    public int myAtoi(String s) {
        int sign = 1;
        boolean isSigned = false;
        String str = "";
        int res = 0;

        int i = 0;
        /*
         * while (i < s.length() && s.charAt(i) == ' ') {
         * i++;
         * }
         */
        s = s.trim();

        if (i < s.length() && (s.charAt(i) == '-' || s.charAt(i) == '+')) {
            if (s.charAt(i) == '-') {
                sign = -1;
            }
            i++;
        }

        int digit = 0;
        while (i < s.length() && Character.isDigit(s.charAt(i))) {
            digit = s.charAt(i) - '0';
            if (res > (Integer.MAX_VALUE - digit) / 10) {
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            res = res * 10 + digit;
            i++;
        }

        return res*sign;


    }
}