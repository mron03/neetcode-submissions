class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)
        starts = []


        for n in nums:
            if n - 1 in numset:
                continue
            
            starts.append(n)

        res = 0
        
        for s in starts:
            temp_res = 1
            i = 1
            while s + i in numset:
                temp_res +=1
                i += 1
            
            res = max(res, temp_res)

        return res
