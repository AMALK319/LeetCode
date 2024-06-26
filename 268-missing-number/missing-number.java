class Solution {
    public int missingNumber(int[] nums) {
        int res = 0;
        int n = nums.length;
        int[] occ = new int[n+1];

        for(int e : nums){
            occ[e]++;
        }

        for(int i=0; i<=n; i++){
            if(occ[i]==0) res = i;
        }
        return res; 
    }
}