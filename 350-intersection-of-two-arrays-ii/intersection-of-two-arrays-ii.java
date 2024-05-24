class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {

        List<Integer> res = new ArrayList<>();
        Map<Integer, Integer> map = new HashMap<>();
        int nums3[];
        int nums4[];

        if(nums1.length < nums2.length) {
            nums3 = nums1;
            nums4 = nums2;
        }
        else { 
            nums3 = nums2;
            nums4 = nums1;
        }

        for(int e : nums3){
           map.put(e, map.getOrDefault(e, 0) + 1);
        }

        for(int e : nums4){
            if(map.containsKey(e) && map.get(e) != 0){
                    res.add(e);
                    map.put(e,map.get(e)-1);
            }
        }
         
        int[] result = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            result[i] = res.get(i);
        }

    return result;

        
        
    }
}