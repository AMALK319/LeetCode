class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        nums_set = set(nums)
        for i in range(1,n+1):
            if i not in nums_set:
                return i
        return n+1

    
        