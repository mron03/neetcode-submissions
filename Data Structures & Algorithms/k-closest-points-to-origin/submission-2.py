class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            dist = (x**2 + y**2)**(1/2)
            
            heapq.heappush(distances, [dist, x, y])

        return [heapq.heappop(distances)[1:] for _ in range(k)]

