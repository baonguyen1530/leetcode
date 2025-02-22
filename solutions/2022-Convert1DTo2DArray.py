class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        
        result = []

        for i in range(0,len(original),n):
            result.append(original[i:i+n])
        
        return result

'''
1) the size of the 2D array should be equal to m * n
so if m * n does not equal the length of the original array
then it's impossible to create a 2D array
2) go through the original array by n times
3) append to the result array starting i and ends with i+n
'''