class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        n = len(colors)

        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                # remove the smaller one
                total_time += min(neededTime[i], neededTime[i - 1])
                # keep the larger one (update neededTime[i])
                neededTime[i] = max(neededTime[i], neededTime[i - 1])

        return total_time
        