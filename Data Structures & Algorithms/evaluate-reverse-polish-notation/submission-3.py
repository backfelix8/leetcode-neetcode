class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]

        value_stack = []
        
        for t in tokens:
            if not (t in operators):
                value_stack.append(int(t))
            
            elif t in operators:
                value1 = value_stack.pop()
                value2 = value_stack.pop()

                if t == "+":
                    value_stack.append(value1 + value2)
                if t == "-":
                    value_stack.append(value2 - value1)
                if t == "*":
                    value_stack.append(value1 * value2)
                if t == "/":
                    value_stack.append(int(value2 / value1))

        return value_stack[0]
                 