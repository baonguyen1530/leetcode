class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        minSum = float('inf')
        prefix = [0] * (n+1)

        for i in range(1,n+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        
        for left in range(0, n - l + 1):
            for right in range(left + l, min(left + r, n) + 1):
                curSum = prefix[right] - prefix[left]
                if curSum > 0:
                    minSum = min(minSum, curSum)
        return minSum if minSum != float('inf') else -1

