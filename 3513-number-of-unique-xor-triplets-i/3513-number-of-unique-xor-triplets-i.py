class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        res = set()
        if len(nums)<3:
            return len(nums)

        noOfBit = bin(max(nums))[2:]
        print(len(noOfBit))
        k = len(noOfBit)
        return 2**k






        # for i in range(0,len(nums),3):
        #     res.add(nums[i]^nums[i+1]^nums[i+2])
        # print(res)
        
        # return len(res)+len(nums)


        