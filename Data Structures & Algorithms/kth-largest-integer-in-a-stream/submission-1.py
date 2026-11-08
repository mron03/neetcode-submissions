import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = nums
        self.k = k
        heapq.heapify_max(self.arr)


    def add(self, val: int) -> int:
        heapq.heappush_max(self.arr, val)

        ans = None
        temp = []
        for i in range(self.k):
            ans = heapq.heappop_max(self.arr)
            temp.append(ans)

        for t in temp:
            heapq.heappush_max(self.arr, t)
        
        return ans



        
        
