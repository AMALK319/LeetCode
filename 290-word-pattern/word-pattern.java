class Solution {
    public boolean wordPattern(String pattern, String s) {

        HashMap<Character, Integer> pMap = new HashMap<>();
        HashMap<String, Integer> sMap = new HashMap<>();

        int pCounter = 0;
        int sCounter = 0;
        String[] words = s.split(" ");

        if(pattern.length() != words.length) return false;
        
        for(int i=0; i<pattern.length(); i++){
            if(!pMap.containsKey(pattern.charAt(i))) 
                pMap.put(pattern.charAt(i),pCounter++);
            if(!sMap.containsKey(words[i])) 
                sMap.put(words[i],sCounter++);
            if(pMap.get(pattern.charAt(i)) != sMap.get(words[i])) 
                return false;
        }

        return true;
       
    }
}