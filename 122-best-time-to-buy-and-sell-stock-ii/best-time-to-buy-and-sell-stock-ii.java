import java.util.*;

class Solution {
    public int maxProfit(int[] prices) {

        int maxProfit = 0;

        for(int i=0; i<prices.length-1; i++){
            maxProfit = Math.max(maxProfit, maxProfit + (prices[i+1]-prices[i]));
        }

        return maxProfit;
        
    }
}