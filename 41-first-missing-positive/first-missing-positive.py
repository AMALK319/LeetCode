class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """ n = 1
        nums.sort()
        for num in nums:
            if num <= 0:
                continue
            if num == n:
                n += 1
        return n"""
        n = len(nums)
        hashSet = set(nums)
        for i in range(1, n+1):
            if i not in hashSet:
                return i
        return n+1 