class Solution(object):
    def increasingTriplet(self, nums):
        n = len(nums)
        first = second = float('inf')

        for i in range(n):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            else:
                return True
        return False
             

      
        