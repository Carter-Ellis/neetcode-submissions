class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        for p in s:
            if p not in dic:
                stack.append(p)           
            else:
                if not stack or dic[p] != stack.pop():
                    return False  
        return not stack