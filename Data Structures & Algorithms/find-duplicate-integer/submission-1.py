class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            n = abs(n)
            
            if nums[n] > 0:
                nums[n] = nums[n] * -1
            else:
                return n