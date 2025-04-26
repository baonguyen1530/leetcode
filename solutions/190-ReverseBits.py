class Solution:
    def reverseBits(self, n: int) -> int:
        x = format(n, '032b')
        return (int(x[::-1],2))