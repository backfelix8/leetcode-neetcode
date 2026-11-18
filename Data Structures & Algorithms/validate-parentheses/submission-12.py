class Solution:
    def isValid(self, s: str) -> bool:
       
        stack = []
        matches = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            
            elif c in [')', ']', '}']:
                if not stack:
                    return False
                cop = stack.pop()
                if cop != matches[c]:
                    return False
            
            else:
                continue
            
        return stack == []