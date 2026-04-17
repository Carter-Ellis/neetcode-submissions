#
#
#
#   Given an int (n), return all well-formed parentheses strings that you can generate with n pairs of parentheses.
#
#   Notes:
#       - Input: n = 1 -> Output: ["()"]
#
#
#
#
#
#



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        stack = []
        def rec(opened, closed) -> None:
            if closed == opened == n:
                res.append("".join(stack))

            if opened < n:
                stack.append("(")
                rec(opened + 1, closed)
                stack.pop()

            if closed < opened:
                stack.append(")")
                rec(opened, closed + 1)
                stack.pop()

            

        rec(0, 0)
        return res