class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        result = 0
        c = capacity

        for i, water_needed in enumerate(plants):
            # reset the water capacity
            if c < water_needed:
                result += 2 * i
                c = capacity
            result += 1
            c -= water_needed
        
        return result