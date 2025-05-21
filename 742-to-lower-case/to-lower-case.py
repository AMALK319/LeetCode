class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        for c in s:
            if ord(c)>=65 and ord(c)<91:
                res += chr(32+ord(c))
            else:
                res += c
        return res 
       
        