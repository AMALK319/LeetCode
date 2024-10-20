class Solution {
    public int maxArea(int[] heights) {

        int p = 0, q = heights.length-1;
        int max = 0;
        int area = 0;

        while(p<q){
            if(heights[p]<heights[q]){
                area = heights[p]*(q-p);
                p++;
            }else{
                area = heights[q]*(q-p);
                q--;
            }
            if(area>=max) max = area;
        }

        return max;
        
    }
}
