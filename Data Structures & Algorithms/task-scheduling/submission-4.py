from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        arr = [-count for count in counter.values()]
        heapq.heapify(arr)

        time = 0
        queue = deque()

        while arr or queue:
            if queue and queue[0][0] == time:
                heapq.heappush(arr, queue.popleft()[1])
            
            if arr:
                task = heapq.heappop(arr)

                if task + 1 < 0:
                    queue.append([time + n + 1, task + 1])
            
            time += 1
        
        return time
