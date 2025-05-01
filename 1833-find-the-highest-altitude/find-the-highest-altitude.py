class Solution(object):
    def largestAltitude(self, gain):
        prev = 0
        curr = 0
        largest = 0
        n = len(gain)

        for i in range(n):
            curr = gain[i] + prev
            largest = max(curr, largest)
            prev = curr

        return largest
      
        