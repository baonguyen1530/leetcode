class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse =True)
        result = 0
        for box,units in boxTypes:
            if truckSize > box:
                truckSize -= box
                result += box * units
            else:
                result += truckSize * units
                return result
        return result