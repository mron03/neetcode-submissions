class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1


        while l <= r:
            pointer = (r - l) // 2 + l

            if nums[pointer] == target:
                return pointer

            elif nums[pointer] < target:
                l = pointer + 1
            
            else:
                r = pointer - 1

        return -1