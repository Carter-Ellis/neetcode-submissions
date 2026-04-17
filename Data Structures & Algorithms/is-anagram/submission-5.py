class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        length = len(s)
        
        dic = {}

        for i in range(length):
            dic[s[i]] = dic.get(s[i], 0) + 1
            dic[t[i]] = dic.get(t[i], 0) - 1
        
        for value in dic.values():
            if value != 0:
                return False
        
        return True