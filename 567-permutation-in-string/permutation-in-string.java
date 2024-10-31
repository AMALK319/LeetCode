class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if(s1.length() > s2.length()) return false;
       
        int[] freq = new int[26];
        int l = 0, r = 0;
        

        for(char c : s1.toCharArray()){
           
            freq[ c - 'a']++;
        }

        while(l<s2.length()){
            
            if(freq[ s2.charAt(l) - 'a'] != 0){
                while(r<s2.length() && freq[s2.charAt(r) - 'a'] != 0 && r-l<s1.length()){
                    
                    freq[s2.charAt(r) - 'a']--;
                    r++;
                }
                if(r-l == s1.length()) return true;
                while(r>l){
                    
                    freq[s2.charAt(r-1) - 'a']++;
                    r--;
                }
            }
            l++; r++;
        }
        return false;
    }
}
