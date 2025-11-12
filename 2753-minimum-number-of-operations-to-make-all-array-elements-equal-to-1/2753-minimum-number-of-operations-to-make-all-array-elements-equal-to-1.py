class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        steps = 0

        overall_gcd = nums[0]
        for num in nums[1:]:
            overall_gcd = math.gcd(overall_gcd,num)
        if overall_gcd >1:
            return -1
        
        ones = nums.count(1)
        if ones >0:
            return n-ones

        min_len = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i)
                    break  # no need to check longer subarrays starting at i
        
        # Step 4: Return (length - 1) + (n - 1)
        return min_len + n - 1      