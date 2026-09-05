class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        hashmap = {}
        print(hashmap)
        l = 0
        res = 0
        max_ele = max(nums)
        max_cnt = 0
        for r in range(len(nums)):
            # curr = nums[r]
            # if curr not in hashmap:
            #     hashmap[curr] = 1
            # else:
            #     hashmap[curr]+=1
            # if hashmap[curr]>=k:
            #     max_ele = curr

            #     while hashmap[max_ele]>=k:
            #         print(l,"l",r,"r")            
            #         hashmap[nums[l]]-=1
            #         l+=1
            #         res+=1

            curr = nums[r]
            if curr == max_ele:
                max_cnt+=1
            
            while max_cnt == k:
                if nums[l] == max_ele:
                    max_cnt-=1
                l+=1
            
            res +=l


        return res

        