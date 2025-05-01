class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        n = len(nums)
        s, e = 0, n-1
        count = 0

        while(s<e):
            if nums[s]+nums[e] == k:
                s += 1
                e -= 1
                count += 1
            elif k-nums[s] > nums[e]:
                s += 1
            elif k-nums[e] < nums[s]:
                e -= 1
        return count


        