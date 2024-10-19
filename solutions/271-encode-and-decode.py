class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        # s = "4#neet4#code4#love3#you"
        result, i = [], 0
        
        while i < len(s):
            j = i   #initialize another pointer
            while s[j] != "#":  #increment j by 1 until we reach a "#"
                j += 1
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i = j+1+length
        return result