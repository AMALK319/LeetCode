class Solution {
    public int firstUniqChar(String s) {

        int[] frequencies = new int[26];

        for(char c : s.toCharArray()){
            frequencies[c-'a']++;
        }

        for(int i=0; i<s.length(); i++){
          if(frequencies[s.charAt(i)-'a'] == 1) return i;
        }

        return -1;
        
    }
}