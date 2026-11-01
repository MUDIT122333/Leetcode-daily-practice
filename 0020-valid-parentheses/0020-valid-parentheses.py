class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in ('(', '[', '{'):
                stack.append(bracket)
            else:
                if len(stack)==0:
                    return False
                ch = stack.pop()
                if ch == '(' and bracket == ')' or ch == '[' and bracket == ']' or ch =='{' and bracket == '}':
                    continue
                else:
                    return False
        return len(stack) == 0



 
                

        
        