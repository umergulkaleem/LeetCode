class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # hashmap = Counter(nums)
        # res = []
        # for i in hashmap:
        #     print(i)
        #     if hashmap[i] >1:
        #         res.append(i)
        # return res

        nums.sort()
        print(nums)
        res= []
        prev = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == prev:
                res.append(nums[i])
            prev= nums[i]

        return res

        