from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_res = max(piles)


        while l <= r:
            target = h
            temp = (l + r) // 2

            time = 0

            for pile in piles:
                time += ceil(pile / temp)

            print(target, time, temp)
            if target == time:
                min_res = min(min_res, temp)
                r = temp - 1
            elif target > time:
                r = temp - 1
                min_res = min(min_res, temp)
            else:
                l = temp + 1

        return min_res
