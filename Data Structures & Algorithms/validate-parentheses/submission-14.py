class Solution:
    def isValid(self, s: str) -> bool:
       
        stack = []
        matches = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in matches:
                if not stack:
                    return False
                cop = stack.pop()
                if cop != matches[c]:
                    return False

            else:
                stack.append(c)
   
        return stack == []