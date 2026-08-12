class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hashmap = {}
        for i in set(nums):
            hashmap[i] = 0
        # print(hashmap)
        l = 0
        # subarray = []
        longest = 0
        for r in range(len(nums)):
            # print(hashmap)
            # subarray.append(nums[r])
            hashmap[nums[r]]+=1
            while hashmap[nums[r]]>k:
                # print(nums[r],"curr element")
                # print(hashmap[nums[r]],"hashmap")
                # print(subarray,"left",l)
                hashmap[nums[l]]-=1
                # subarray.pop(l)
                l+=1
            longest = max(longest,r-l+1)
        return longest
            


        