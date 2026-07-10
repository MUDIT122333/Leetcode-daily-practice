class Solution:
    def isHappy(self, n: int) -> bool:
        while n > 0:
            n = (n//10)**2 + (n%10)**2

            if n ==1:
                return True
        return False