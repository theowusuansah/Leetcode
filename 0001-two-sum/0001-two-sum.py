class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,element in enumerate(nums):
            complement = target - element
            if complement in d:
                return [d[complement],i]
            else:
                d[element] = i
        return []
            
        return sorted(output)
        