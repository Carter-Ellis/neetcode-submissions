class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        for p in s:
            if p == "(":
                stack.append(p)
            elif p == "{":
                stack.append(p)
            elif p == "[":
                stack.append(p)
            else:
                if not stack or dic[p] != stack.pop():
                    return False
        if stack:
            return False
        return True