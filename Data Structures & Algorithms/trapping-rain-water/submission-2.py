class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0: return 0

        prefix, suffix = [0] * n, [0] * n

        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], height[i - 1])

        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i + 1])

        res = 0

        print(prefix)
        print(suffix)

        for i in range(n):
            l, r = prefix[i], suffix[i]

            water = min(l, r) - height[i]

            if water > 0: res += water

        return res