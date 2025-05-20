class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

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
        return max(counts)
            


        """ map = {}

        for num in nums:
            if num not in map:
                map[num] = set()
                map[num].add(num)
                temp = num-1
                while temp in map:
                    map[num].add(map[temp])
                    temp -= 1
                if num+1 in map:
                    map[num].add(map[num+1])

                
                
        print(map)
        ans = 0
        for val in map.values():
            ans = max(ans, len(val))
        
        return ans """

        