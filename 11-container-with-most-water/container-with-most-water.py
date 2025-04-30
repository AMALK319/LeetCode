class Solution(object):
    def maxArea(self, height):
        n = len(height)
        s, e = 0,n-1
        maxVol = 0

        while(s<e):
            maxVol = max(maxVol, (e-s) * min(height[e], height[s]))
            if(height[e]>height[s]):
                s += 1
            else:
                e -= 1
        return maxVol