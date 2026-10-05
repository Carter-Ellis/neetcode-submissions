class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        dic = {}

        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i], 0) + 1
            dic[t[i]] = dic.get(t[i], 0) - 1
        
        for key, value in dic.items():
            if value != 0:
                return False
        
        return True

        