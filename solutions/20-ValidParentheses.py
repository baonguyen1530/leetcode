class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                # Make sure stack isn't empty first
                if not stack:
                    return False
                temp = stack.pop()
                if (i == ")" and temp != "(") or \
                (i == "]" and temp != "[") or \
                (i == "}" and temp != "{"):
                    return False  # Mismatched brackets
                    
        return False if stack else True