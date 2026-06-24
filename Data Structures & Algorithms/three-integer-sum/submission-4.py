class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                predicted = nums[j] + nums[k]

                if predicted == -nums[i]:
                    res.add((nums[i], nums[j], nums[k]))
                    j+=1
                elif predicted > -nums[i]:
                    k -= 1
                else:
                    j +=1

        return [sublist for sublist in res]

                
        