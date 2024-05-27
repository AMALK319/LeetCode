class Solution {
    public void reverseString(char[] s) {

        int start = 0;
        int end = s.length-1;
        char c = s[start];
        
        while(start<end){
            c = s[start];
            s[start] = s[end];
            s[end] = c;
            start++;
            end--;
        }
        
    }
}