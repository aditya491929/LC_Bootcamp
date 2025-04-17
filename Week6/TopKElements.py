from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        elem_freq = Counter(nums)
        
        max_heap = [(-freq, elem) for elem, freq in elem_freq.items()]
        heapq.heapify(max_heap)

        res = []
        while len(res) < k:
            res.append(heapq.heappop(max_heap)[1])

        return res