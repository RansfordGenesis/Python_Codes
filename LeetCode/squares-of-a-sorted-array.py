class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        final = [x*x for x in nums]
        final.sort()
        return final
