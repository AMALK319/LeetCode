/* class MinStack {

    private class StackNode{
        int data;
        StackNode previous;

        StackNode(int data){
            this.data = data;
        }
    }

    StackNode top;
    List<Integer> minArray = new ArrayList<>();
    int min;
    int minIndex;

    public MinStack() {
        
    }
    
    public void push(int val) {

        min = Math.min(top == null ? val : minArray.get(minArray.size()-1), val);
        minArray.add(min);
        
        StackNode item = new StackNode(val);
        item.previous = top;
        top = item;

    }
    
    public void pop() {
        if(top != null ){
            minArray.remove(minArray.size()-1);
            top = top.previous;
        } 
        
    }
    
    public int top() {
        if (top != null) return top.data;
        return 0;
    }
    
    public int getMin() {
        return minArray.get(minArray.size()-1);
    }
} */

class MinStack {

    private Stack<Integer> stack;
    private Stack<Integer> minStack;
    int min;
   
    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int val) {

        if(stack.isEmpty()) 
            min = val;
        else {
            min = Math.min(minStack.peek(), val);
        }
        minStack.push(min);
        stack.push(val);

    }
    
    public void pop() {

        minStack.pop();
        stack.pop();
    
    }
    
    public int top() {
        return stack.peek();
        
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
