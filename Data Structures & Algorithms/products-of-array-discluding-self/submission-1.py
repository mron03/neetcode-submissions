class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes, temp_p = [], 1
        suffixes, temp_s = [], 1
        res = []

        for p, s in zip(nums, nums[::-1]):
            prefixes.append(temp_p)
            temp_p *= p
        
            suffixes.append(temp_s)
            temp_s *= s


        for i in range(len(nums)):
            res.append(prefixes[i] * suffixes[len(nums) - 1 - i])

        return res






