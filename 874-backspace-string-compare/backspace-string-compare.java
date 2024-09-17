class Solution {
    public boolean backspaceCompare(String s, String t) {

        Stack<Character> stackS = new Stack<>();
        Stack<Character> stackT = new Stack<>();

        for(char c : s.toCharArray()){
            if(c == '#' && !stackS.isEmpty()) stackS.pop();
            else if(c == '#') continue;
            else{
                stackS.push(c);
            }
        }

        for(char c : t.toCharArray()){
            if(c == '#' && !stackT.isEmpty()) stackT.pop();
            else if(c == '#') continue;
            else{
                stackT.push(c);
            }
        }

        while( !stackS.isEmpty() && !stackT.isEmpty() ){
            if(stackS.pop() != stackT.pop()) return false;
        }

        if(stackS.isEmpty() && stackT.isEmpty()) return true;
        
        return false;
        
    }
}