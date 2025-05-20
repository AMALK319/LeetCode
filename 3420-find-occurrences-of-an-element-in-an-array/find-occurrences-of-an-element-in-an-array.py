class Solution:

    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occurencies = []
        
        for i in range(len(nums)):
            if nums[i] == x:
                occurencies.append(i)
        
        answer = [0 for _ in range(len(queries))]
        for i in range(len(queries)):
            if queries[i]-1 < len(occurencies):
                answer[i]=occurencies[queries[i]-1]
            else:
                answer[i]=-1
        return answer
    
    """def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        map = {}
        occ = 0
        for i in range(len(nums)):
            if nums[i] == x:
                occ += 1
                map[occ] = i
        m = len(queries)
        answer = [0 for _ in range(m)]
        for i in range(m):
            answer[i] = map[queries[i]] if queries[i] in map else -1
        
        return answer"""

        