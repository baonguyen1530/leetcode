class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        #O(n)
        for num in nums:
            count[num] += 1
        sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)
        result = []
        for t in sorted_items[:k]:
            result.append(t[0])
        return result