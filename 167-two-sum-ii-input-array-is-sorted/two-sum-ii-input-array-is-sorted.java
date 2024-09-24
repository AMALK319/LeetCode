class Solution {
       public int[] twoSum(int[] numbers, int target) {
        
        int n = numbers.length;
        int p = 0;
        int q = n-1;


        while(p<q){
            if(numbers[p]+numbers[q] == target) break;
            if(numbers[p] < target - numbers[q]) p++;
            else{
                q--;
            }
        }


        return new int[]{p+1,q+1};
    }
}