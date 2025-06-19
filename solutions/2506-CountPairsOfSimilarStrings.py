class Solution:
    def similarPairs(self, words: List[str]) -> int:
        wordMap = {}

        for word in words:
            # convert the word to unique characters 
            # this will the key for the wordMap
            current = sorted(set(word))
            current = ''.join(current)

            if current in wordMap:
                wordMap[current] += 1
            else:
                wordMap[current] = 1
        
        pairs = 0

        for word in wordMap:
            count = wordMap[word]
            pairs += (count*(count-1))//2
            
        return pairs