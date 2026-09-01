class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        # count = 0

        # tmp = 0
        # res = 0
        # l = 0
        # arr = []
        # for r in range(len(nums)):
        #     # print(arr)
        #     curr = nums[r]
        #     tmp+=curr
        #     while curr in arr or len(arr)>=k:
        #         tmp-=arr[0]
        #         arr.pop(0)
        #     arr.append(curr)
        #     if len(arr) == k:

        #         res= max(res,tmp)
 
        # return res


        res = 0
        curr = 0
        curr_sum = 0
        l =0 
        hashmap = defaultdict(int)
        for r in range(len(nums)):
            curr = nums[r]
            curr_sum+=curr
            hashmap[curr]+=1
            
            if r-l+1>k:
                
                hashmap[nums[l]] -=1
                if hashmap[nums[l]] == 0:
                    hashmap.pop(nums[l])
                curr_sum-=nums[l]
                l+=1
            if len(hashmap) == r-l+1 == k:
                res = max(res,curr_sum)
        return res
        


        