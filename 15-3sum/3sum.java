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
                //int sum = nums[p]+nums[q]+nums[i];
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
        

}