
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(0, len(tokens)):
            if tokens[i] == "*" or tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "/":
                oper2 = int(stack.pop())
                oper1 = int(stack.pop())
                if tokens[i] == "*":
                    stack.append(oper1 * oper2)
                elif tokens[i] == "+":
                    stack.append(oper1 + oper2)
                elif tokens[i] == "-":
                    stack.append(oper1 - oper2)
                elif tokens[i] == "/":
                    stack.append(int(oper1 / oper2))
            else:
                    stack.append(tokens[i])
        return int(stack.pop())