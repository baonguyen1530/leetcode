class Solution:
    def generateTag(self, caption: str) -> str:
        arr = caption.split()
        if not arr: 
            return "#"
        result = ''.join(char.capitalize() for char in arr if char.isalpha() and char.isascii())
        result =  "#" + result[0].lower() + result[1:]
        if len(result) > 100:
            diff = len(result) - 100
            return result[:len(result)-diff]
        return result