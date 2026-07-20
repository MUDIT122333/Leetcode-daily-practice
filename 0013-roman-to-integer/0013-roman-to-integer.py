class Solution:
    def romanToInt(self, s: str) -> int:

        roman_int = {"I":             1,
                    "V":             5,
                    "X":             10,
                    'L':             50,
                    'C':             100,
                    'D':             500,
                    'M':             1000}
        integer = 0
        i=0
        while i < len(s):
            if i+1 < len(s) and roman_int[s[i]] < roman_int[s[i+1]]:
                integer += roman_int[s[i+1]] - roman_int[s[i]]
                i+=2
            else:
                integer += roman_int[s[i]]
                i+=1
        return integer