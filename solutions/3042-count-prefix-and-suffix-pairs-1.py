class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                result += 1 if words[j].startswith(words[i]) and words[j].endswith(words[i]) else 0

        return result