class Solution:
    def climbStairs(self, n: int) -> int:
        def rec(count) -> int:
            if count == n:
                return 1
            if count > n:
                return 0
            return rec(count + 1) + rec(count + 2)
        return rec(0)