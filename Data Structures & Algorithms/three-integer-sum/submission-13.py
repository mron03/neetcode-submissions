class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = set()

        i = 0
        while i < len(nums) - 2:
            l = i + 1
            r = len(nums) - 1

            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if temp > 0:
                    r -= 1
                elif temp < 0:
                    l += 1
                else:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
            
            i += 1
        
        return [list(r) for r in res]
