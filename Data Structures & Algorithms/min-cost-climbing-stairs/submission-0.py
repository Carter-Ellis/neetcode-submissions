class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        one, two = cost[len(cost) - 2], 0

        for i in range(len(cost) - 3, -1, -1):
            temp = one
            one = min(one, two) + cost[i]
            two = temp
        return min(one, two)
