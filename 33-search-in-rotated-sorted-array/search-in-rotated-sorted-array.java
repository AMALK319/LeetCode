class Solution {
    public int search(int[] nums, int target) {

        int l = 0, r = nums.length-1;
        int mid = 0;

        while(l<=r){
            mid = l + (r-l)/2;
            if(nums[mid] == target) return mid;
            if(nums[l]<=nums[mid]){
                if(nums[mid]>target && nums[l] <= target) r = mid - 1;
                else{
                   l = mid + 1;
                }
            }
            else{
                if(nums[mid]<target && target <= nums[r]) l = mid + 1;
                else{
                    r = mid - 1;
                }
            }
        }

        return -1;
        
    }
}
