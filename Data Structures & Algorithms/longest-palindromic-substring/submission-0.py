class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestSub = ""
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                longestSub = longestSub if len(longestSub) >= (r - l) + 1 else s[l:r + 1]   
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                longestSub = longestSub if len(longestSub) >= (r - l) + 1 else s[l:r + 1]   
                l -= 1
                r += 1
        return longestSub