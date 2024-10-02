class Solution {
    public int[] dailyTemperatures(int[] temperatures) {

        int n = temperatures.length;
        Stack<Integer> warmTemperatures = new Stack<>();
        int[] res = new int[n];

        for(int i = n-1; i>=0; i--){
            
            while(!warmTemperatures.isEmpty()){
                if(temperatures[i]<temperatures[warmTemperatures.peek()]) {
                    res[i] = warmTemperatures.peek() - i;
                    break;

                }
                else{
                    warmTemperatures.pop();
                }
            }
            
            warmTemperatures.push(i);
        }

        return res;
        
    }
}
