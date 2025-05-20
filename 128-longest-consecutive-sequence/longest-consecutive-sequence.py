class Solution:
    """def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums)<=1: return len(nums)
        nums.sort()
        count,counts = 1,[]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1]+1:
                count += 1
            else:
                counts.append(count)
                count = 1
        counts.append(count)
        return max(counts)""" 
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums)==0: return 0
        numsSet = set(nums)
        sequences = []
        for num in numsSet:
            if num-1 not in numsSet:
                seq = [num]
                temp = num
                while temp+1 in numsSet:
                    seq.append(temp+1)
                    temp += 1
                sequences.append(seq)
        return max([len(seq) for seq in sequences])
        