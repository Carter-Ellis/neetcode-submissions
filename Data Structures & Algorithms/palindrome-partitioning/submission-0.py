#
#
#
#   Given a string s, return all possible lists of palindromic substrins.
#
#   Notes:
#       - Split s into substrings where every substring is a palindrome
#       - Solution may be any order
#
#
#   Input: s = "aabbc"
#                 i
#
#   Output: [["a", "a", "b", "b", "c"], ["aa", "b", "b", c"], ["a", "a", "bb", "c"], ["aa", "bb", c]]
#                                                                                                   
#                                                                                                   
#
#
#   Input: s = "aba"
#
#   Output = [["a", "b", "a"], ["aba"]]
#


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res


    def isPalin(self, s, l, r) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1
        return True