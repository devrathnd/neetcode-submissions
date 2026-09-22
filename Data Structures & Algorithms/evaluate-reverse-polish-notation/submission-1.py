class Solution:
    def isMathOp(self, token) -> bool:
        ops = ['+', '-', '*', '/']
        if token in ops:
            return True
        return False

    def evalRPN(self, tokens: List[str]) -> int:
        evalStack = []

        for token in tokens:
            if self.isMathOp(token):
                operand2 = int(evalStack.pop())
                operand1 = int(evalStack.pop())
                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                elif token == '/':
                    result = int(operand1 / operand2)
                evalStack.append(result)
            else:
                evalStack.append(int(token))
            
        return evalStack[0]
