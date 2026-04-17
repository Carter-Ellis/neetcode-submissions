class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []
        def rec(i, curr):
            if curr == curr[::-1]:
                res.append(curr)
            i += 1
            if i >= len(s):
                return
            rec(i, curr + s[i])
        for i in range(len(s)):
            rec(i,s[i])
        return len(res)