/* class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

       
        ArrayList<Integer> temp ;
        Set<List<Integer>> set = new HashSet<>();
       
        int t = nums[0];

        Arrays.sort(nums);

        for(int i = 0; i<nums.length; i++){
            
            if(nums[i] > 0 ) break;
            if (i>0 && nums[i] == t) continue;
            t = nums[i];

            int p = 0;
            int q = nums.length - 1;
            while(p<q){
                if(nums[p]+nums[q] == - nums[i]){
                    temp = new ArrayList<>();
                    temp.add(nums[i]);
                    temp.add(nums[p]);
                    temp.add(nums[q]);
                    set.add(temp);
                    p++;
                    q--;
                }
                else if(nums[p]+nums[q] < - nums[i]) 
                    p++;
                else{
                    q--;
                }
            }
        }

        return  new ArrayList<>(set);
        
    }
        

} */

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int l = i + 1, r = nums.length - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum > 0) {
                    r--;
                } else if (sum < 0) {
                    l++;
                } else {
                    res.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    l++;
                    r--;
                    while (l < r && nums[l] == nums[l - 1]) {
                        l++;
                    }
                }
            }
        }
        return res;
    }
}