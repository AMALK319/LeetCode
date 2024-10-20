class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        int[] prefix = new int[n];
        int[] postfix = new int[n];
        
        int p = 1;
        for(int i = 0; i<n; i++){
            p *= nums[i];
            prefix[i] = p;
        }

        int q = 1;
        for(int i = n-1; i>0; i--){
            q *= nums[i];
            postfix[i] = q;
        }
        
        for(int i = 0; i<n; i++){
            if(i==0) res[i] = postfix[i+1];
            else if (i==n-1) res[i] = prefix[i-1];
            else{
                res[i]= prefix[i-1]*postfix[i+1];
            }
        }

        return res;
        
    }
}  
