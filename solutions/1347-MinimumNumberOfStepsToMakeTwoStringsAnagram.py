class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = Counter(s)
        counter_t = Counter(t)
        steps = 0

        for i in counter_s: 
            diff = counter_s[i] - counter_t.get(i,0)
            if diff > 0:
                steps += diff
        
        return steps