class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        max_floor_outside = max(special[0]-bottom, top-special[-1])

        max_floor_inside = 0
        for i in range(1,len(special)):
            max_floor_inside = max(max_floor_inside, special[i]-special[i-1]-1)
        
        return max(max_floor_outside,max_floor_inside)