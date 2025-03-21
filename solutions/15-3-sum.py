class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, value in enumerate(nums):
            if value > 0:
                break
                
            if i > 0 and value == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums)-1
            while l < r:
                threeSum = value + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([value,nums[l],nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result