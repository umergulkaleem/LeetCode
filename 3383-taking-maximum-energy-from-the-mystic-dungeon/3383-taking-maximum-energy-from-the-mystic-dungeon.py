class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # maxenergy = float(-inf)
        # count = 0
        # while count<len(energy):
        #     temp = 0
        #     print(count,"cpunt")
        #     for i in range(count,len(energy),k):
        #         temp+=energy[i]
            
        #     print(temp)
        #     maxenergy = max(maxenergy,temp)
        #     count+=1
        # return maxenergy
    
        n = len(energy)
        dp = [0] * n

        # Process from the end backwards
        for i in range(n - 1, -1, -1):
            dp[i] = energy[i]
            if i + k < n:
                dp[i] += dp[i + k]

        return max(dp)


        