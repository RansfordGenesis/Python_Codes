class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        binary = ""
        while n > 0:
            remainder = n % 2
            n = n // 2
            binary = str(remainder) + binary
        for i in binary:
            if int(i) == 1:
                count += 1
        return count
