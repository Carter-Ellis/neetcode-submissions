#
#
#   Input: nums = [] (unsorted ints), int k
#
#   Output: kth largest element in the array
#
#   Note:
#       -kth largest element in the sorted order
#
#
#
#   heapify nums
#   res = 0
#   for i in range k
#       res = pop()
#   return res
#
#   Data Structure: MaxHeap
#
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        res = 0
        for i in range(k):
            res = heapq.heappop_max(nums)
        return res