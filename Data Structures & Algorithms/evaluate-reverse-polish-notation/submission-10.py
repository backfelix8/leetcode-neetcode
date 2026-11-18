class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in operators:
                operands.append(int(token))
            else:
                o1 = operands.pop()
                o2 = operands.pop()
            
            if token == '+':
                operands.append(o1 + o2)
            elif token == '*':
                operands.append(o1 * o2)
            elif token == '-':
                operands.append(o2 - o1)
            elif token == '/':
                operands.append(int(o2 / o1))
        
        return operands[0]

