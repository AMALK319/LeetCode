class Solution:

    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occurencies = [i for i in range(len(nums)) if nums[i] == x]
        answer = []
        for q in queries:
            if q-1 < len(occurencies):
                answer.append(occurencies[q-1])
            else:
                answer.append(-1)
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

        