class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in dic:
                dic[key] = [word]
            else:
                dic[key].append(word)
        ans = []
        for value in dic.values():
            ans.append(value)
        return ans