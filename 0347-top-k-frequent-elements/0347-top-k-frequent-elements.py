class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
            
        sorted_d = {k: v for k, v in sorted(d.items(), key = lambda item: item[1], reverse = True)}
        keys = list(sorted_d.keys())
        if len(keys) == 1:
            return keys
        return keys[:k]