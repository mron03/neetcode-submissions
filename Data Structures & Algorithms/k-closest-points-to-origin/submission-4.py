class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = {}

        for point in points:
            x = point[0]
            y = point[1]

            dist = (x**2 + y**2)**(1/2)

            if not dist in distances:
                distances[dist] = [[x,y]]

            else:
                distances[dist].append([x,y])
            
        heapmin = list(distances.keys())
        heapq.heapify(heapmin)

        ans = []
        
        while len(ans) != k:
            closest_dist = heapq.heappop(heapmin)

            for point in distances[closest_dist]:
                ans.append(point)
                if len(ans) == k:
                    break

        return ans