class Solution:
    def isPalindrome(self, x: int) -> bool:
            num = str(x)
            if num[::-1] == num:
                return True
            return False
