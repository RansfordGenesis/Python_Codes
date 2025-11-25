class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = [num for num in arr if arr.count(num) == num]
        return max(lucky) if lucky else -1
