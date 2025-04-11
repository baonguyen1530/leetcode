class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Split the problem into 2 scenarios
            Rob the houses but the avoid the last house 
            Rob the houses but the avoid the first house
        Find the maximum between the two results so we don't rob the first and the last house together.
        '''
        def helper(arr):
            n = len(arr)
            res = [0] * (n+1)
            res[1] = arr[0]

            for i in range(2,n+1):
                res[i] = max(res[i-1], res[i-2] + arr[i-1])
            
            return res[-1]
        
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        else:
            return max(helper(nums[1:]), helper(nums[:-1]))