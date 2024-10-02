class Solution {
    public int evalRPN(String[] tokens) {

        Stack<Integer> stack = new Stack<>();

        int op1 , op2;

        for(int i = 0; i<tokens.length; i++){
            switch(tokens[i]){
            case "+": 
                stack.push(stack.pop()+stack.pop());
                break;
            case "*": 
                stack.push(stack.pop()*stack.pop());
                break; 
            case "/": 
                op2 = stack.pop(); 
                op1 = stack.pop();
                stack.push(op1 / op2);
                break;
            case "-": 
                op2 = stack.pop(); 
                op1 = stack.pop();
                stack.push(op1 - op2);
                break;   
            default:
                stack.push(Integer.parseInt(tokens[i]));
            }

        }
        return stack.peek();
    }

}
