class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        result = len(nums)
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                result += (len(set(nums[i:j+1]))) ** 2
        return result