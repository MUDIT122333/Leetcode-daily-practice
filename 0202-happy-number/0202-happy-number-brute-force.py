class Solution:
    def isHappy(self, n: int) -> bool:
        while n > 0:
            n = (n//10)**2 + (n%10)**2

            if n ==1:
                return True
        return False
    
# this approach throws TLE
# because it not handle when squaring number form a digit more than two digits
# and not handle the edge cases 