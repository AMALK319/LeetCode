class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        count = 0
        n = len(s)

        i = n-1
        while i>= 0:
            print(s[i])
            if s[i] != '*':
                res.append(s[i])
                i -= 1
            else:
                while((i>= 0 and s[i] == '*') or count>0):
                    print(s[i])
                    count = count+1 if s[i] == '*' else count-1
                    i -= 1
        
        return "".join(res[::-1])

      