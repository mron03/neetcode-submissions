class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes, temp_p = [], 1
        suffixes, temp_s = [], 1
        res = []

        for num in nums:
            prefixes.append(temp_p)
            temp_p *= num
        
        for num in nums[::-1]:
            suffixes.append(temp_s)
            temp_s *= num



        for i in range(len(nums)):

            res.append(prefixes[i] * suffixes[len(nums) - 1 - i])

        return res






