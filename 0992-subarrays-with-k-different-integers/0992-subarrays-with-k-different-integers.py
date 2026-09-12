class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        hashmap = {}
        res = 0
        l = 0
        mid= 0
        for r in range(len(nums)):
            curr = nums[r]
            if curr not in hashmap:
                hashmap[curr] = 1
            else:
                hashmap[curr]+=1
            # print(hashmap,"before")
            while len(hashmap)>k:
                # print(l,"ll")
                # print(hashmap,"inremoveing",nums[l])
                
                hashmap[nums[mid]]-=1
                if hashmap[nums[mid]] == 0:
                    hashmap.pop(nums[mid],None)
                mid+=1
                l = mid
            while hashmap[nums[mid]]>1:
                hashmap[nums[mid]] -=1
                mid+=1
                
            # print(hashmap,"after")
            if len(hashmap) == k:
                # print(hashmap,"res")
                res+=mid-l+1
        return res        