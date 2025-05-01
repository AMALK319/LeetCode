class Solution(object):
    def largestAltitude(self, gain):
        prev = 0
        curr = 0
        largest = 0
        for i in range(len(gain)):
            curr = gain[i] + prev
            largest = max(curr, largest)
            prev = curr

        return largest
      
        