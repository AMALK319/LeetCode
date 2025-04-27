class Solution(object):
    def gcdOfStrings(self, str1, str2):
       
        for l in range(min(len(str1), len(str2)), 0, -1):
            if(len(str1)%l == 0 and len(str2)%l == 0):
                f1, f2 = len(str1)//l , len(str2)//l
                base = str1[:l]
                if(base*f1 == str1 and base*f2 == str2):
                    return str1[:l]
        return ""


        
        