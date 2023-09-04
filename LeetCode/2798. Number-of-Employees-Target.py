class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        final = [hour for hour in hours if hour >= target]
        return len(final)
