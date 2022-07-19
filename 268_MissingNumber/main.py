class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        target = (n ** 2 + n)//2
        return target - sum(nums)