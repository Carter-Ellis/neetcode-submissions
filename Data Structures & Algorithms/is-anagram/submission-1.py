class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1 = {}
        dic2 = {}
        i = len(s) - 1
        while i >= 0:
            dic1[s[i]] = 1 + dic1.get(s[i], 0)
            dic2[t[i]] = 1 + dic2.get(t[i], 0)
            i -= 1
        print(dic1)
        print(dic2)
        return dic1 == dic2
