class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        result = []
        q = collections.deque()

        while r < len(nums):
            #pop the smaller value from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            #out of bound for the window
            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                result.append(nums[q[0]])
                l += 1
            r += 1
        return result