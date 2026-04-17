class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, length, maxLength = 0, 0, 0, 0
        #Set of space O(1) since we only use 26 letters worst case
        visited = set()

        while r < len(s):
            if s[r] in visited:
                while l < r:
                    visited.remove(s[l])
                    length -= 1
                    l += 1
                    if s[r] not in visited:
                        break
            visited.add(s[r])
            length += 1
            maxLength = max(maxLength, length)
            r += 1
        return maxLength