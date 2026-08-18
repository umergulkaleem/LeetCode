class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        hashmap = {}

        for x in set(nums):
            
            hashmap[x] = 0
        

        for i in range(len(nums)-k+1):
            arr = nums[i:i+k]
            for i in set(arr):
                hashmap[i]+=1

        ans = set()
        for i in hashmap:
            if hashmap[i] == 1:
                ans.add(i)
        print(ans)
        print(hashmap,"map")
        if len(ans) == 0:
            return -1
        else:
            return max(ans)
        
            
        
        