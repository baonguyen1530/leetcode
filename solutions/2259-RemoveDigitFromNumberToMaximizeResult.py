class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        temp = []
        for index,value in enumerate(number):
            if value == digit: 
                temp.append(int(number[:index] + number[index+1:]))
        return str(max(temp))