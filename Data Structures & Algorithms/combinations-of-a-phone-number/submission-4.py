#
#
#
#   Given a string (digits), return all possible letter combinations that digits could represent.
#
#
#   Notes:
#       - Any order
#       - Does not include 1
#
#
#
#

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToLetters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        currStr = ""
        
        if not digits:
            return []

        def rec(i: int):
            nonlocal currStr
            if i >= len(digits):
                res.append(currStr[:])
                return

            for c in digitToLetters[digits[i]]:
                currStr += c
                rec(i + 1)
                currStr = currStr[:-1]
        rec(0)
        return res