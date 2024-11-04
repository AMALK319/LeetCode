class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        int l1 = 0;
        int r1 = matrix.length-1;

        int l2 = 0;
        int r2 = matrix[0].length-1;

        while(l1<=r1 && l2<=r2){
            int m1 = l1 + (r1-l1)/2;
            int m2 = l2 + (r2-l2)/2;
            if(matrix[m1][m2]>target){
                r2 = m2 - 1;
                if(r2<0){
                    r2 = matrix[0].length-1;
                    r1 = m1 - 1;
                }
            }
            else if(matrix[m1][m2]<target){
                l2 = l2 + 1;
                if(l2>matrix[0].length-1){
                    l2 =0;
                    l1 = l1 + 1;
                }
            }
            else{
                return true;
            }
        }

        return false;

    }
}
