class Solution {
    public int evalRPN(String[] tokens) {

        Stack<Integer> stack = new Stack<>();
        int op = 0;
        int op1 = 0;
        int op2 = 0;
        if(tokens.length == 1) return Integer.parseInt(tokens[0]); 
        int res = 0;
        for(int i = 0; i<tokens.length; i++){
            try{
                op = Integer.parseInt(tokens[i]);
                stack.push(op);
            }
            catch (NumberFormatException e) {
                op2 = stack.pop();
                op1 = stack.pop();
                res = operate(tokens[i], op1,op2);
                stack.push(res);
            }
        }
        return res;
    }

    private int operate(String operation, int op1, int op2){
        int res = 0;
        switch(operation){
            case "+": 
                res = op1 + op2;
                break;
            case "*": 
                res = op1 * op2;
                break; 
            case "/": 
                res = op1 / op2;
                break;
            case "-": 
                res = op1 - op2;
                break;           
        }
        return res;
    }
}
