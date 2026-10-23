import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        result = []
        heapq.heapify(nums)

        while nums:
            smallest = heapq.heappop(nums)
            result.append(smallest)

        return result



