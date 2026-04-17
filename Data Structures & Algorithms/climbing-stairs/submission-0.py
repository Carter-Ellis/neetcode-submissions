class Solution:
    def climbStairs(self, n: int) -> int:
        total = 0
        def rec(count):
            nonlocal total
            if count == n:
                total += 1
                return
            if count > n:
                return
            rec(count + 1)
            rec(count + 2)
        rec(0)
        return total