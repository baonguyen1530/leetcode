class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        indices = []

        for i in range(len(binary)):
            if binary[i] == '1':
                indices.append(i)

        distance = 0

        for i in range(1, len(indices)):
            if indices[i]-indices[i-1] > distance:
                distance = indices[i]-indices[i-1]
        return distance

'''
1) convert the given integer into binary
2) go through the binary string and store the index of every
'1' in an array
3) go through that array of indices and find the longest one,
then we will return that distance
'''