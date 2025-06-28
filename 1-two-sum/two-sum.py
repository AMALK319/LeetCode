class Solution(object):
    def twoSum(self, nums, target):
        index_map = {}
        for i in range(len(nums)):
            index_map[nums[i]]=i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in index_map and i != index_map[diff]:
                return [i, index_map[diff]]
        