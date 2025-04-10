class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        result = [0] * (n+1)
        result[1] = nums[0]

        for i in range(2,n+1):
            result[i] = (max(result[i-1], result[i-2] + nums[i-1]))
        
        return result[-1]