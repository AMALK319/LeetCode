class Solution {
    public void moveZeroes(int[] nums) {

        int t = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                if (i != t) {
                    nums[t] = nums[i];
                    nums[i] = 0;
                }
                t++;
            }
        }
        
    }
}