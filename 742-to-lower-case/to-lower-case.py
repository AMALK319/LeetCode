class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        for c in s:
            temp = ord(c)
            if temp>=65 and temp<91:
                res += chr(32+temp)
            else:
                res += c
        return res 
       
        