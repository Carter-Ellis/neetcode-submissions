class Solution:
    def isPalindrome(self, s: str) -> bool:
        r, l = len(s) - 1, 0  
           
        while r > l:
            while r > l and not self.isAlpha(s[r]):
                r -= 1
            while r > l and not self.isAlpha(s[l]):
                l += 1
            if s[r].lower() != s[l].lower():
                return False
            r -= 1
            l += 1
        return True
    
    def isAlpha(self, string):
        if (ord("A") <= ord(string) <= ord("Z") or ord("a") <= ord(string) <= ord("z") or ord("0") <= ord(string) <= ord("9")):
           return True
        return False
