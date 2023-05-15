class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        for i in range(len(arr)-2):
            current_dif = arr[i+1]-arr[i]
            next_dif = arr[i+2]-arr[i+1]
            if (current_dif == next_dif):
                continue
            else:
                return False

        return True
