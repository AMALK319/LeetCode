class Solution:
    """def longestPalindrome(self, s: str) -> str: 

        def isPalindromic(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        n = len(s)
        longest = ""
        for i in range(n):
            for j in range(i,n):
                sub = s[i:j+1]
                if isPalindromic(sub):
                    if len(longest) < len(sub):
                        longest = sub
        return longest"""
        
    def longestPalindrome(self, s: str) -> str: 
        longest = ""
        n = len(s)
        for i in range(n):
            l = r = i
            while(l>= 0 and r<n) and s[l] == s[r]:
                if len(longest) < r-l+1:
                    longest = s[l:r+1]
                r += 1
                l -= 1
            l , r = i, i+1
            while(l>= 0 and r<n) and s[l] == s[r]:
                if len(longest) < r-l+1:
                    longest = s[l:r+1]
                r += 1
                l -= 1
        return longest     