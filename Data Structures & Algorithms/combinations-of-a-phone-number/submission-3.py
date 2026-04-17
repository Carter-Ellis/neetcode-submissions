class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToLetter = {'2' : ['a','b','c'], '3' : ['d', 'e', 'f'], '4' : ['g', 'h', 'i'], '5' : ['j', 'k', 'l'], '6' : ['m', 'n', 'o'], '7' : ['p', 'q', 'r', 's'], '8' : ['t', 'u', 'v'], '9' : ['w', 'x', 'y', 'z']}
        combinations = []

        def rec(i, currStr):
            if len(currStr) == len(digits):
                combinations.append(currStr)
                return
            for c in numToLetter[digits[i]]:
                rec(i + 1, currStr + c)
        if digits:    
            rec(0, "")
        return combinations

