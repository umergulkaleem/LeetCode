class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        # if min(hashmap.values())<2:
        #     return -1

        # sorted_nums = sorted(nums)
        # count = 0
        res = 0
        # while True:
        #     if len(sorted_nums) ==0:
        #         break
        #     curr = sorted_nums[count]
        #     if hashmap[curr] % 3 == 0:
        #         for _ in range(3):
        #             sorted_nums.pop(0)
        #         res+=1
        #     elif hashmap[curr] % 2 == 0:
        #         for _ in range(2):
        #             sorted_nums.pop(0)
        #         res+=1
               
        #     print(sorted_nums)
        # return res

        for i in hashmap.values():
            if i == 1:
                return -1
            res+= i//3
            if i % 3:
                res+=1
        return res



            


        
        