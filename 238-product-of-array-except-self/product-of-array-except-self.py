class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        prefixes = [1] * n
        suffixes = [1] * n
        answer = []

        for i in range(1,n,1):
            prefixes[i] = nums[i-1]*prefixes[i-1]
        for i in range(n-2,-1,-1):
            suffixes[i] = nums[i+1]*suffixes[i+1]
        for i in range(n):
            answer.append(prefixes[i]*suffixes[i])
        
        return answer