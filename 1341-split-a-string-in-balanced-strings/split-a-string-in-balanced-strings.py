class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = countR = countL = 0
        for i in range(len(s)):
            if s[i] == 'R':
                countR += 1
            elif s[i] == 'L':
                countL += 1
            if countR == countL:
                ans += 1
        return ans
