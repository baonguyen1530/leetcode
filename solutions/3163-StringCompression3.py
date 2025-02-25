class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""   #hold the result
        cnt = 1 
        ch = word[0] #the first word

        for char in range(1, len(word)):
            if word[char] == ch and cnt < 9:
                cnt += 1
            else:
                comp += str(cnt) + ch
                ch = word[char]
                cnt = 1
        comp += str(cnt) + ch
        return comp

'''
1) create your variables
        comp will hold the result string
        cnt will be 1 because the first word will always be 1
        ch will be the current character we are checking
2) loop through the word starting at the second character
3) if the word[char] match with with our ch and the cnt is less than 9, then we will only increment the cnt
4) else, either the word does not match or the count for that word exceed 9. then we will add it to the comp, change ch to the current word[char] and reset our cnt to 1
5) lastly, add the remaining word to comp and return it
'''