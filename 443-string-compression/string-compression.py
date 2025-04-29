class Solution(object):
    def compress(self, chars):
        n = len(chars)
        if n == 1: return 1
        s = ""
        l,f = 0,1
        while(l<f and f<=n):
            if(f<n and chars[f] == chars[l]):
                f += 1
            else:
                s = s + chars[l] + str(f-l) if f-l>1 else s + chars[l]
                l = f
                f += 1
        m = len(s)
        for i in range(m):
            chars[i] = s[i]
        
        return m

        
        