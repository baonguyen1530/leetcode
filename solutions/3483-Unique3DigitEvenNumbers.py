class Solution:
    # store the solution in a set
    # if the mod of it is even then we'll store it in a set
    # find the length of the set and that would be the result

    def totalNumbers(self, digits: List[int]) -> int:
        result = set()

        for a,b,c in permutations(digits,3):
            if a != 0 and c % 2 == 0:
                result.add((a,b,c))
        
        return len(result)
        