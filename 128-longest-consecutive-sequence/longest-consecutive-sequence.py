class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums)<=1: return len(nums)
        nums.sort()
        count,counts = 1,[]
        longest = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1]+1:
                count += 1
            else:
                #counts.append(count)
                longest = max(longest, count)
                count = 1
        #counts.append(count)
        longest = max(longest, count)
        #return max(counts)
        return longest
        
    """ def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        for num in numsSet:
            if num-1 not in numsSet:
                length = 0
                while num+length in numsSet:
                    length += 1
                longest = max(longest, length)
        return longest"""
        