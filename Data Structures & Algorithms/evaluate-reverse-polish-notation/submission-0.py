# if you see a number, add it to the stack. when we encounter a sign then we pop the last two numbers from the stack, and we compute that, and add that to the stack. 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operands = ["+", "-", "*", "/"]

        for token in tokens:
            if token in operands:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    res = self.compute(num1, num2, token)
                    stack.append(res)
            else:
                stack.append(int(token))

        result = stack.pop()
        return result

    def compute(self, num1, num2, token):
        if token == "+":
            return (num2 + num1)
        elif token == "-":
            return (num2 - num1)
        elif token == "*":
            return (num2 * num1)
        else:
            return int(num2 / num1)
        
            





        