class Solution(object):
    def majorityElement(self, nums):
        ''' count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
            if count_map[num] > len(nums)//2:
                return num '''
        votes = 0
        res = nums[0]
        for num in nums:
            if votes == 0:
                res = num
            if num == res:
                votes += 1
            else:
                votes -= 1 
        return res
            
