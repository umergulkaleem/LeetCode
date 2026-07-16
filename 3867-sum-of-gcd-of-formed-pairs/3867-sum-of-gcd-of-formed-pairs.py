class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        
        n = len(nums)
        mx = 0
        prefix_gcd = []

        for i in range(n):
            mx = max(nums[i],mx)
            prefix_gcd.append(gcd(nums[i],mx))

        prefix_gcd.sort()
        total = 0

        for i in range(n//2):
            total += gcd(prefix_gcd[i],prefix_gcd[n-i-1])
        return total
        