class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        sum = 0
        for num in nums:
            sum += num
            output.append(sum)
        return output
