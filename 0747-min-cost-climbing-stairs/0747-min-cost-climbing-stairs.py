class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
    
        # Base cases
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        # Fill dp array
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        # Answer is the minimum of last two
        return min(dp[n-1], dp[n-2])