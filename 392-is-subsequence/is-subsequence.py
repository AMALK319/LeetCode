class Solution(object):
    def isSubsequence(self, s, t):
        n, m = len(s), len(t)
        slow, fast = 0, 0

        while(slow<n and fast<m):
            if(s[slow] == t[fast]):
                slow += 1
            fast += 1

        return slow == n
        
            
        