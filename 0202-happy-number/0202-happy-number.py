class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        while n>0:
            seen[n] = n
            sum_squares = 0
            # sum_squares = (n//10)**2 + (n%10)**2
            while n:
                last_digit = n%10
                sum_squares += (last_digit)**2
                remove_last = n//10
                n = remove_last
            n = sum_squares
            if n == 1:
                return True
            if n in seen:
                return False
        return False


        