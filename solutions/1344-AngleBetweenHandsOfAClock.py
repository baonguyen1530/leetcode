class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minDegree = minutes * 6
        hourDegree = (hour%12 * 30) + (minutes * 0.5)
        angle = abs(hourDegree - minDegree)
        
        if angle > 180:
            angle -= 360.0

        return abs(angle)