class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[-1]
        b = nums[0]
        while b:
            a, b = b , a % b
        return a
