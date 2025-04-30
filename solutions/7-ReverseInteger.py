class Solution:
    def reverse(self, x: int) -> int:
        
        # if x is negative we want to keep track of that
        sign = -1 if x < 0 else 1
        abs_x = abs(x)
        
        # first convert the abx_x to a string because we can reverse it
        # wrap it in an int() method 
        # multiply it with the sign variable
        res = int(str(abs_x)[::-1]) * sign
        
        # check if the result is more then or less than 32 bit integers
        # [-2147483648, 2147483647] if it's out of this range then we return 0
        if res < -2 ** 31 or res > 2 ** 31 - 1:
            return 0

        return res