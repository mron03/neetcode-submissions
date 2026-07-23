class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        mp = {}
        for x, y in points:
            distance = (x**2 + y**2)**(1/2)
            
            if distance in mp:
                mp[distance].append([x,y])
            else:
                mp[distance] = [[x, y]]

            heapq.heappush(distances, distance)


        res = []
        for _ in range(k):
            dist = heapq.heappop(distances)
            if dist in mp:
                res.extend(mp[dist])
                mp.pop(dist)

        return res[:k]

