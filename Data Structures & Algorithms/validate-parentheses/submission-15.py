class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(', ']': '[', '}': '{'}

        for c in s:
            match c:
                case '(' | '[' | '{':
                    stack.append(c)
                case _:    
                    if not stack or stack.pop() != closeToOpen[c]:
                        return False
        return not stack
