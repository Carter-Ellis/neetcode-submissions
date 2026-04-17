class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}

        for c in s:
            if c not in sMap:
                sMap[c] = 0
            sMap[c] += 1
        
        for c in t:
            if c not in sMap:
                print("Hello")
                return False
            sMap[c] -= 1
        
        for value, key in sMap.items():
            print(value)
            if key != 0:
                return False
        return True