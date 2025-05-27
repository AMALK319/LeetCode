class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """points.sort(key=lambda p: math.sqrt(p[0]**2 + p[1]**2))
        return points[:k]"""

        maxHeap = []
        for x,y in points:
            dist= math.sqrt(x**2 + y**2)
            heapq.heappush(maxHeap,(-dist, x, y))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        result = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            result.append([x,y])
        return result
        