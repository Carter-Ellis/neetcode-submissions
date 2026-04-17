class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dic = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in dic:
                dic[sortedWord] = []
            dic[sortedWord].append(word)
        for key, value in dic.items():
            res.append(value)
        return res