class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def isPerm(dic: dict) -> bool:
            for value in dic.values():
                if value != 0:
                    return False
            return True

        if len(s1) > len(s2):
            return False

        origDic = {}
        for character in s1:
            origDic[character] = 1 + origDic.get(character, 0)
        
        l, r = 0, 0
        while r < len(s2):
            currDic = dict(origDic)
            while r < len(s2) and s2[r] in currDic:
                while currDic[s2[r]] <= 0:
                    currDic[s2[l]] += 1
                    l += 1
                currDic[s2[r]] -= 1
                r += 1
                if isPerm(currDic):
                    return True
            if isPerm(currDic):
                return True
            r += 1
            l = r
        return False
                