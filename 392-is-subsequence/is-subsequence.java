class Solution {
    public boolean isSubsequence(String s, String t) {

        int p = 0;
        int q = 0;

        while(p<t.length() && q<s.length()){
            if(t.charAt(p)==s.charAt(q)) {
                p++;
                q++;
            }
            else{
                p++;
            }
        }


        if(q<s.length()) return false;

        return true;
        
    }
}