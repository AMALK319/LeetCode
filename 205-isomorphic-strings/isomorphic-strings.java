class Solution {
    public boolean isIsomorphic(String s, String t) {

        HashMap<Character,Character> map = new HashMap<>();
        HashSet<Character> disallowedChars = new HashSet<>();

        for(int i=0; i<s.length(); i++){

            if(!map.containsKey(s.charAt(i)) && disallowedChars.contains(t.charAt(i))) return false;
            if(map.containsKey(s.charAt(i)) && map.get(s.charAt(i)) != t.charAt(i)) return false;

            if(!map.containsKey(s.charAt(i))){
                map.put(s.charAt(i), t.charAt(i));
                disallowedChars.add(t.charAt(i));
            }  
        }

        return true;
        
    }
}