class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = abs(nums[i])

            if nums[n] > 0:
                nums[n] = nums[n] * -1
            else:
                return n