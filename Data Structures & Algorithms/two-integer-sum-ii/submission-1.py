class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 1
        r = len(numbers)
        while True:
            answer = numbers[l-1] + numbers[r-1]
            if answer == target:
                return [l, r]
            elif answer > target:
                r -= 1
            else:
                l += 1
