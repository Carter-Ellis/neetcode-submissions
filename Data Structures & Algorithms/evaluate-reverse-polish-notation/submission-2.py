class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def is_int(token: str) -> bool:
            try:
                int(token)
                return True
            except ValueError:
                return False

        for token in tokens:
            print(stack)
            if is_int(token):
                stack.append(int(token))
            elif token == "+":
                right = stack.pop()
                left = stack.pop()
                stack.append(left + right)
            elif token == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)
            elif token == "*":
                right = stack.pop()
                left = stack.pop()
                stack.append(left * right)
            elif token == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left / right))
                
        return stack.pop()
