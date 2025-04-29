class Solution(object):
    def moveZeroes(self, nums):
        slow = fast = 0
        n = len(nums)
        count = 0
        for num in nums:
            if num != 0 : count += 1
        

        while(slow<count and fast<n):
            if(nums[slow] == 0):
                while(nums[fast] == 0):
                    fast += 1
                nums[slow], nums[fast] = nums[fast], 0
                slow += 1
            else:
                slow += 1
                fast += 1
        return nums
            
   