class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = defaultdict(int)

        dp[0]  =1

        for i in range(len(nums)):

            next_dp = defaultdict(int)
            for curr_sum,count in dp.items():
                next_dp[curr_sum + nums[i]]+=count       
                next_dp[curr_sum - nums[i]]+=count       

            dp = next_dp
        return dp[target]