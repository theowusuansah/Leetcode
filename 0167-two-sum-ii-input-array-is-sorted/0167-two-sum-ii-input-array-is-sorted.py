class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lower, higher = 0, len(numbers) -1

        while lower < higher:
            if numbers[lower] + numbers[higher] == target:
                return [lower+1, higher+1]
            elif numbers[lower] + numbers[higher] > target:
                higher -= 1
            else:
                lower += 1  
        