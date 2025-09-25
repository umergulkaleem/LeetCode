class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # finalmin = 0
        # for i in range(len(triangle)):
        #     layermin = triangle[i][0]
        #     for k in triangle[i]:
        #         layermin = min(k,layermin)
        #         print(layermin,"layermin")
        #     finalmin+=layermin
        #     print(finalmin,"final")
        # return finalmin
        dp = triangle[-1]  # start from last row
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]
            
        