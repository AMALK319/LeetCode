class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occurencies = []
        
        for i in range(len(nums)):
            if nums[i] == x:
                occurencies.append(i)
        
        answer = [0 for _ in range(len(queries))]
        print(answer)
        for i in range(len(queries)):
            if queries[i]-1 < len(occurencies):
                answer[i]=occurencies[queries[i]-1]
            else:
                answer[i]=-1
        return answer
        