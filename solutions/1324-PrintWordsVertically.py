class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        max_length = len(max(s, key=len))
        result = []
        
        for i in range(max_length):
            ver = ''
            for word in s:
                if i < len(word):
                    ver += word[i]
                else:
                    ver += ' '
            result.append(ver.rstrip())
        return result