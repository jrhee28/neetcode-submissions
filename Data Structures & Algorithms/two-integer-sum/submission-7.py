class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i, n in enumerate(nums):
            solution = target - n
            if solution in prev:
                return [prev[solution], i]
            prev[n] = i


        