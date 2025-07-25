class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = []
        i = 0
        temp = 1

        while i < len(num) - 1:
            if num[i+1] == num[i]:
                temp += 1
                if temp == 3:
                    result.append(num[i]*3)
            else:
                temp = 1
            i += 1
        
        if result:
            return max(result)
        else:
            return ""