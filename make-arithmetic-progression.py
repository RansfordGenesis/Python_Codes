class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        for i in range(len(arr)-2):
            current = arr[i+1]-arr[i]
            next = arr[i+2]-arr[i+1]
            if (current == next):
                continue
            else:
                return False
        return True
