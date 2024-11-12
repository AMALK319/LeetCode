

class Solution {
    public int minEatingSpeed(int[] piles, int h) {

        int max = 1;
        int n = piles.length;
        int j = 0;

        while(j<n){
            if(piles[j]>= max) max = piles[j];
            j++;
        }

        int l = 1, r = max;
        while(l<=r){
            int k = l + ((r-l)/2);
            long hours = 0;
            for(int i=0; i<n; i++){
                hours += piles[i]<k ? 1 : Math.ceil((double)piles[i]/k);
            }
            if(hours <= h) r = k-1;
            else{
                l = k+1;
            }
        }

        return l;

    }
}
