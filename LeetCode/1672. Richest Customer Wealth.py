class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            max_wealth = max(max_wealth, sum(account))
        return max_wealth
