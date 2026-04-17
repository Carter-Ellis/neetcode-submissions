class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum()).lower()

        if not s:
            return True

        l, r = int(len(s) / 2), int(len(s) / 2)
        print(f'l: {l} r: {r} {s}')
        while l >= 0 and r < len(s):
            
            if (s[l] != s[r]):
                break
            if (l == 0 and r == len(s) - 1):
                return True
            l -= 1
            r += 1

        l, r = int(len(s) / 2) - 1, int(len(s) / 2)    
        while l >= 0 and r < len(s):
            if (s[l] != s[r]):
                break
            if (l == 0 and r == len(s) - 1):
                return True
            l -= 1
            r += 1
        
        return False
