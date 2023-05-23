class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in nums:
            for x in nums:
                if i-x == k:
                    count += 1
        return count
