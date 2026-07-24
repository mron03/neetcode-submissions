class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None

        heapq.heapify_max(nums)
        ans = None
        while k != 0:
            ans = heapq.heappop_max(nums)
            k -= 1
        
        return ans