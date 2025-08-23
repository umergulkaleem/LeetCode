class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count = 0
        # mcount = 0
        # zerocount = 0
        # tzero = 0
        # for i in range(len(nums)):
        #     print(nums[i],"at this")
        #     if nums[i] == 1:
        #         count+=1
        #         zerocount = 0
        #     if nums[i] == 0:
        #         tzero +=1
        #         zerocount+=1
        #         if zerocount>1:
        #             print("in")
        #             # count+=1
        #             zerocount =0
        #             # mcount = max(mcount,count)
        #             count = 0
        #     print(count,"count")
        #     print(zerocount,"zero")
        #     # print(mcount,"maxcount")
        # if tzero  == 1:
        #     return count
        # if 0 not in nums:
        #     count-=1
        # return count
        # count = 0        # current streak
        # prev_count = 0   # streak before the last zero
        # max_count = 0    # answer
        # zero_seen = 0

        # for num in nums:
        #     if num == 1:
        #         count += 1
        #     else:
        #         # When we see a zero, we keep the streak before it
        #         prev_count = count
        #         count = 0
        #         zero_seen += 1
            
        #     # max streak = streak before zero + streak after zero + flip(1)
        #     max_count = max(max_count, prev_count + count + 1)

        # # Edge case: if no zero was ever seen, we must subtract 1 (because we   can’t flip)
        # if zero_seen == 0:
        #     max_count -= 1
        
        # return max_count-1


        # proper solution gpt

        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len-1

        
        