class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pivot = -1
        l, r = 0, n - 1

        while True:
            pivot = l
        
            for i in range(l, r):
                if nums[i] <= nums[r]:
                    nums[pivot], nums[i] = nums[i], nums[pivot]
                    pivot += 1

            nums[pivot], nums[r] = nums[r], nums[pivot]

            if pivot == n - k:
                return nums[pivot]
            
            elif pivot > n - k:
                r = pivot - 1
            
            else:
                l = pivot + 1
        


