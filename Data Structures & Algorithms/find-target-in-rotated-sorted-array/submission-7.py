class Solution:

    def bin_ser(self, nums, l, r, target):
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (r + l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l

        if nums[pivot] <= target <= nums[-1]:
            return self.bin_ser(nums, pivot, len(nums) - 1, target)
        else:
            return self.bin_ser(nums, 0, pivot, target)


            