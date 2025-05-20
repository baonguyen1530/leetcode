class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        arr = ["a","b","c","d","e","f","g","h"]
        coordinate = (arr.index(coordinates[0])+1, int(coordinates[1]))

        return False if sum(coordinate) % 2 == 0 else True