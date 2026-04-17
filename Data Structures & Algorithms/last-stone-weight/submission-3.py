#
#
#
#   Given an array of ints (stones), return the wieight of the last remaining stone such that:
#       
#
#       - Each step we choose the two HEAVIEST stones, with weight x and y and smash them together:
#           - If x == y: both stones are destroyed
#           - If x < y: stone x is destroyed and stone y has a new weight y - x
#       
#       - Continue simulation until no more than one stone remaining
#       
#       - If none remain return 0
#
#
#
#
#
#

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if x == y:
                continue
            heapq.heappush_max(stones, abs(x-y))

        return 0 if not stones else stones[0]