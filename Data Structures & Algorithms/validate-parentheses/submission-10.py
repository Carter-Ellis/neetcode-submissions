class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            match c:
                case '(' | '[' | '{':
                    stack.append(c)
                case _:
                    if not stack:
                        return False
                    bracket = stack.pop()
                    
                    if c == ")" and bracket != '(':
                        return False
                    elif c == "]" and bracket != '[':
                        return False
                    elif c == "}" and bracket != '{':
                        return False
        if stack:
            return False
        return True

