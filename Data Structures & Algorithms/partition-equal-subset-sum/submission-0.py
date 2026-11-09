class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False

        half = total // 2

        def dfs(i, cur):
            if i >= n or cur > half: 
                return False

            if cur == half:
                return True

            return dfs(i + 1, cur + nums[i]) or dfs(i + 1, cur)
    
        return dfs(0, 0)

