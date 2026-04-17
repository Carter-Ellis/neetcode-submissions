class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for i in range(1, len(strs)):
            j = 0
            new_res = ""
            while j < len(strs[i]) and j < len(res):
                if res[j] != strs[i][j]:
                    break
                new_res += strs[i][j]
                j += 1
            res = new_res if len(new_res) < len(res) else res
        return res