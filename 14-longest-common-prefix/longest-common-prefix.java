import java.util.*;

class Solution {
    public String longestCommonPrefix(String[] strs) {

        String prefix = "";
        if(strs.length == 0) return prefix;

        for(int i = 0; i<strs[0].length(); i++){
            for(String str : strs){
                if(i == str.length() || str.charAt(i)!= strs[0].charAt(i)) return prefix;
            }
            prefix += strs[0].charAt(i);
        }

        return prefix;
/* 
        String ex = "";
        String res = strs[0];
        for (String s : strs){
            if(s.length()<res.length()) {
                ex = res;
                res = s;
            }
            else{
                ex = s;
            }
            while(!ex.substring(0, res.length()).equals(res)){
                res = res.substring(0, res.length()-1);
            }
        }
        return res; */
    }
}

/* class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        String s1 = strs[0];
        String s2 = strs[strs.length-1];
        int idx = 0;
        while(idx < s1.length() && idx < s2.length()){
            if(s1.charAt(idx) == s2.charAt(idx)){
                idx++;
            } else {
                break;
            }
        }
        return s1.substring(0, idx);
    }
} */