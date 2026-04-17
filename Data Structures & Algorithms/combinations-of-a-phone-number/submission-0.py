class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToLetter = {'2' : ['a','b','c'], '3' : ['d', 'e', 'f'], '4' : ['g', 'h', 'i'], '5' : ['j', 'k', 'l'], '6' : ['m', 'n', 'o'], '7' : ['p', 'q', 'r', 's'], '8' : ['t', 'u', 'v'], '9' : ['w', 'x', 'y', 'z']}
        combinations, currStr = [], ""

        def rec(i, currStr):
            if len(currStr) == len(digits) and currStr != "":
                combinations.append(currStr[::])
                return
            if i >= len(digits):
                return
            for j in range(0, len(numToLetter[digits[i]])):
                currStr += numToLetter[digits[i]][j]
                rec(i + 1, currStr)
                currStr = currStr[:i]
            
        rec(0, currStr)
        return combinations

