class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = math.prod(nums)
        if result > 0:
            return 1
        elif result < 0:
            return -1
        elif result == 0:
            return 0
