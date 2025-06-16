class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = "0123456789"
        result = []

        for i in range(len(word)):
            if word[i] not in nums:
                word = word.replace(word[i],' ')
        num_list = word.split()
        for i in range(len(num_list)):
            result.append(int(num_list[i]))
        
        return len(set(result))