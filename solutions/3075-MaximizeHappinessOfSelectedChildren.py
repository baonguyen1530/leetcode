class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        i = 0
        result = 0

        while k > 0:
            happiness[i] = max(happiness[i]-i,0)
            result += happiness[i]
            i+=1
            k-=1
        
        return result