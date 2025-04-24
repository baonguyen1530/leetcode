class Solution:
    def hammingWeight(self, n: int) -> int:
        x = bin(n)[2:]
        res = 0

        for i in str(x):
            if i == "1":
                res += 1

        return res

'''
1. Convert n into binary
2. Run a for loop on the binary sequence and increment result whenever we encounter 1
'''