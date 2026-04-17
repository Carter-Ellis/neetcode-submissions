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

        def rec(currStr, opened, closed) -> None:
            if closed == opened == n:
                res.append(currStr)

            if opened < n:
                currStr += "("
                rec(currStr, opened + 1, closed)
                currStr = currStr[:-1]
                

            if closed < opened:
                currStr += ")"
                rec(currStr, opened, closed + 1)
                currStr = currStr[:-1]

            

        rec("", 0, 0)
        return res