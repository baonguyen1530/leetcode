class Solution:
    def countSubstrings(self, s: str) -> int:
        n, ans = len(s), 0

        def helper(left,right):
            count = 0
            while left >= 0 and right < n and s[right] == s[left]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(n):
            even = helper(i,i+1)
            odd = helper(i,i)
            ans += even + odd
        
        return ans