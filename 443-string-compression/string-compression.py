class Solution(object):
    def compress(self, chars):
        n = len(chars)
        s = ""
        i = 0
        while(i<n):
            old = chars[i]
            s += old
            dup = ""
            i += 1
            while(i<n and chars[i]==old):
                dup += chars[i]
                i += 1
            s += str(len(dup)+1) if len(dup)>0 else ""
        
        print(s)

        m = len(s)
        for i in range(m):
            chars[i] = s[i]
        
        return m

        
        