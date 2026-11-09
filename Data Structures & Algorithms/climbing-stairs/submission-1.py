class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        nxt = 1
        nxtnxt = 1

        for i in range(n - 1):
            temp = nxt
            nxt = nxt + nxtnxt
            nxtnxt = temp
        
        return nxt