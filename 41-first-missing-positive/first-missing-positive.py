class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = 1
        nums.sort()
        for num in nums:
            if num <= 0:
                continue
            if num == n:
                n += 1
        return n
  