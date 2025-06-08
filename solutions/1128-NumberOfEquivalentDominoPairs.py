class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        m = [0] * 100
        count = 0

        for a,b in dominoes:
            key = a * 10 + b if a <= b else b * 10 + a
            count += m[key]
            m[key] += 1
        
        return count