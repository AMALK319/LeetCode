class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m , n = len(accounts), len(accounts[0])
        wealth = 0
        for i in range(m):
            cust = 0
            for j in range(n):
                cust += accounts[i][j]
            wealth = max(wealth, cust)
        return wealth

        