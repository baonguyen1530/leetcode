class Solution:
    def minimumPushes(self, word: str) -> int:
        unique_char = len(set(word))
        
        if unique_char <= 8:
            return unique_char
        elif unique_char <= 16:
            return 8 + 2 * (unique_char - 8)
        elif unique_char <= 24:
            return 8 + 16 + 3 * (unique_char - 16)
        else:
            return 8 + 16 + 24 + 4 * (unique_char - 24)