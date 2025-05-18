class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        i = 0
        time = 0

        while tickets[k] != 0:
            if i >= n:
                i = 0
            if tickets[i] == 0:
                i += 1
            else:
                tickets[i] -= 1
                time += 1
                i += 1
        
        return time