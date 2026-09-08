class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(arr):
            rob1, rob2 = 0, 0

            for r in arr:
                temp = max(r + rob1, rob2)
                rob1=rob2
                rob2=temp
            
            return rob2
    
        return max(nums[0], f(nums[:-1]), f(nums[1:]))