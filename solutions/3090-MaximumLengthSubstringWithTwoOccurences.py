class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left,right = 0,0
        max_length = 0
        count = {}
        
        while right < len(s):
            if s[right] not in count:
                count[s[right]] = 0
            count[s[right]] += 1
            while count[s[right]] > 2:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            max_length = max(max_length,right-left+1)
            right += 1
        return max_length