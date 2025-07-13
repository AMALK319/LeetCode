class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if sum(nums) < target: return 0
        
        l, n = 0, len(nums)
        sub_array_len = 0
        min_sub_array_len = float("inf")

        for r in range(n):
            sub_array_len += nums[r]
            while sub_array_len >= target:
                min_sub_array_len = min(min_sub_array_len, r-l+1)
                sub_array_len -= nums[l]
                l += 1
        return  min_sub_array_len