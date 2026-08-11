class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # hashset  = set(nums)
        # nums = set(nums)
        # nums = list(nums)
        # res = 0
        # curr_seq = 0
        # longest_seq = 0
        # prev = nums[0]
        # tmp = 0
        # once = False
        # for i in range(len(nums)):
        #     if  nums[i]+1 in hashset or not once:
        #         curr_seq+=1
        #         tmp+=nums[i]
        #         print(tmp,"tmp now at",nums[i])
        #     else:
        #         once = False
        #         print(curr_seq,longest_seq)
        #         longest_seq = max(longest_seq,curr_seq)
        #         if longest_seq == curr_seq and tmp not in hashset:
        #             print("in")
        #             res = tmp
        #             tmp = 0
                    
        #         curr_seq = 0
        #     if nums[i]+1 not in hashset:
        #         once = True
        #     prev = nums[i]
        #     # print(res)
        #     # print(curr_seq)
        # return res
        hashset = set(nums)
        total  = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                total+=nums[i]
            else:
                break
        while total in hashset:
            total+=1
        return total
        
            

        