class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # if sum(nums)% 2==1:
        #     return False

        # to_find = sum(nums)//2
        # print(to_find,"to find")
        # for i in range(len(nums)):
        #     combination = []
        #     count=0
        #     count+=nums[i]
        #     print(count,"at i")
        #     combination.append(nums[i])
        #     for j in range(len(nums)):
        #         if j == i:
        #             break
        #         if count+nums[j]<=to_find:
        #             count+=nums[j]
        #             combination.append(nums[j])
        #             print(count,"at j")
        #         if count==to_find:
        #             print(combination)
        #             break
        # print(combination,"final")
        # new  = nums
        # for i in combination:
        #     print(i,"final")
        #     if i in new:
        #         new.remove(i)
        # print(new,"new")
        # sum(new)
        # if sum(new) == to_find:
        #     return True
        # else:
        #     return False
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        to_find = total // 2
        n = len(nums)

        dp = [False] * (to_find + 1)
        dp[0] = True

        for num in nums:
            for i in range(to_find, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[to_find]
                    

