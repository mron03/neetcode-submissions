class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = set(nums)
        res = 0
        
        for n in nums:
            if n-1 not in freq:
                temp_res = 0
                i = n

                while i in freq:
                    temp_res += 1
                    i += 1
                
                res = max(res, temp_res)
        
        return res


