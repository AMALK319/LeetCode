class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

       
        ArrayList<Integer> temp ;
        Set<List<Integer>> set = new HashSet<>();

        Arrays.sort(nums);

        for(int i = 0; i<nums.length; i++){
            
            if(nums[i] > 0 ) break;
            if (i>0 && nums[i] == nums[i-1]) continue;

            int p = i+1 , q = nums.length-1;
            while(p<q){
                int sum = nums[p]+nums[q]+nums[i];
                if(sum == 0){
                    temp = new ArrayList<>();
                    temp.add(nums[i]);
                    temp.add(nums[p]);
                    temp.add(nums[q]);
                    set.add(temp);
                    p++;
                    q--;
                }
                else if(sum < 0) 
                    p++;
                else{
                    q--;
                }
            }
        }

        return  new ArrayList<>(set);
        
    }
        

}
/* 
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> res = new HashSet<>();

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
                   /*  while (l < r && nums[l] == nums[l - 1]) {
                        l++;
                    } 
                }
            }
        }
        return new ArrayList<>(res);
    }
} */