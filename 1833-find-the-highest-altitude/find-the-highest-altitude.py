class Solution(object):
    def largestAltitude(self, gain):
        prev = curr = largest = 0
        for i in range(len(gain)):
            curr = gain[i] + prev
            largest = max(curr, largest)
            prev = curr

        return largest
      
        