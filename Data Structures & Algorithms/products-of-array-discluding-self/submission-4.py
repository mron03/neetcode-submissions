import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        suffix = [nums[-1]]

        for n in nums[1:]:
            prefix.append(prefix[-1] * n)
        
        for n in nums[::-1][1:]:
            suffix.append(suffix[-1] * n)
        suffix = suffix[::-1]

        res = []

        for i in range(len(nums)):
            pref = prefix[i - 1] if i - 1>= 0 else 1
            suf = suffix[i + 1] if i + 1 < len(nums) else 1

            res.append(pref * suf)
        return res
            