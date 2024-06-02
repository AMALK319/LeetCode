class Solution {
    public int strStr(String haystack, String needle) {

        if (needle.length() == 0) return 0;

        if(needle.length() > haystack.length()) return -1;

        int i = 0;
        int n = needle.length();

        while(i < haystack.length()-n+1){
            if(haystack.substring(i,n+i).equals(needle)) return i;
            i++;
        }

        return -1;
        
    }
}