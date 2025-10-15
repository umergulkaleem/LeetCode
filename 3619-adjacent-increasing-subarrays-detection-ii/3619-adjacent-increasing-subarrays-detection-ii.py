class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        inc_from_left = [1] * n
        inc_from_right = [1] * n
        
        # Fill inc_from_left: lengths of increasing subarrays ending at i
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc_from_left[i] = inc_from_left[i-1] + 1
        
        # Fill inc_from_right: lengths of increasing subarrays starting at i
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                inc_from_right[i] = inc_from_right[i+1] + 1
        
        max_k = 0
        # Check for all possible splits between subarrays
        for i in range(n-1):
            # check if left subarray of length k exists ending at i
            # and right subarray of length k exists starting at i+1
            length_left = inc_from_left[i]
            length_right = inc_from_right[i+1]
            k = min(length_left, length_right)
            if k > max_k:
                max_k = k
        
        return max_k