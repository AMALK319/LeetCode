class Solution {
    public String defangIPaddr(String address) {
        return address.replace(".", "[.]");    
    }
}

/* class Solution {
    public String defangIPaddr(String address) {
        String defanged = "";
        String[] splitted = address.split("\\.");
        for(int i=0; i<splitted.length-1; i++){
            defanged += splitted[i].concat("[.]");
        }    
        return defanged.concat(splitted[splitted.length-1]);
    }
} */