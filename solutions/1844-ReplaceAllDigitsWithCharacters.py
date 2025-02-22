class Solution:
    def replaceDigits(self, s: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        arr = list(s)

        def shift(char, n):
            i = alphabet.index(char)
            return alphabet[i+n]

        for i in range(1,len(s)):
            if i % 2 != 0:  # this means the current i is a digit
                arr[i] = shift(arr[i-1],int(arr[i]))
        
        return ''.join(arr)
        