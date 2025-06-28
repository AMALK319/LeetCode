class Solution(object):
    def twoSum(self, nums, target):
        index_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in index_map:
                return [i, index_map[diff]]
            index_map[nums[i]]=i
        