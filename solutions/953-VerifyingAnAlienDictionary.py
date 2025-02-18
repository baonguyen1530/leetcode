class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # if it's only one word then it would be sorted
        if len(words) == 1:
            return True
        
        order_map = {}
        
        for index, val in enumerate(order):
            order_map[val] = index

        # traverse in array words
        for i in range(len(words)-1):
            # traverse each character in a word
            for j in range(len(words[i])):
                # if the index j of the current word is greater than 
                # the length of the next word then it is not in sorted order
                # therefore, we return False
                if j >= len(words[i+1]):
                    return False
                # check if the letters in the same position in the
                # two words are different
                if words[i][j] != words[i+1][j]:
                    if order_map[words[i][j]] > order_map[words[i+1][j]]:
                        return False
                    # if we found the first different word and their order
                    # is sorted then we don't ahve to check the rest
                    break
        return True