class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1

        while l < r:
            predicted = numbers[l] + numbers[r]

            if predicted == target:
                return [l+1, r+1]
            elif predicted > target:
                r -= 1
                continue
            else:
                l += 1
            