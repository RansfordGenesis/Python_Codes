class Solution:
    def mySqrt(self, x: int) -> int:
        guess = x
        i = 0
        while(guess * guess != x and i < 20):
            guess = (guess + x/guess)/2.0
            i+=1
        return guess.__floor__()
