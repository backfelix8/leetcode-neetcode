class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)

            elif len(stack) > 0 and stack[-1] == matches.get(c, "n0pe"):
                stack.pop()
            else:
                return False
        
        return len(stack) == 0

        