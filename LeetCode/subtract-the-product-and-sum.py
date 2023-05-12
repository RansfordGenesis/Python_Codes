class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1
        for x in str(n):
            sum += int(x)
            product *= int(x)
        return product - sum
         
#List Comprehension
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = [int(x) for x in str(n)]
        return (math.prod(n)-sum(n))
