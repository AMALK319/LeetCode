class Solution {
    public int[] plusOne(int[] digits) {

        int[] resp = new int[digits.length+1];

        for(int i = digits.length-1; i>=0; i--){
            if(digits[i] != 9) {
                digits[i] += 1;
                return digits;
                
            }
            else{
                if(i==0) resp[0] = 1;
                digits[i] = 0;
            }
            
        }
        for (int i = 0; i < digits.length; i++){
            if(resp[0] == 1) resp[i+1] = digits[i];
            else{
                resp[i] = digits[i];
            }
        }
        return resp;
        
    }
}