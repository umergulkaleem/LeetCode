class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum = sum(nums[:k])
        max_sum = window_sum  # ✅ start with the first window's sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        ans = float(max_sum) / k
        return ans

        
        # Return maximum average


        # my code try
        # return max_sum / k
        max_sum = 0
        # max_sum = float('-inf')
        # for i in range(len(nums) - k + 1):
        #     temp = 0
        #     for j in range(i, i + k):
        #         temp += nums[j]
        #     max_sum = max(max_sum, temp)
        # ans = float(max_sum) / k
        # return ans



