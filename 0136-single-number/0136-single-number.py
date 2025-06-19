class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # numsnew = sorted(nums)
        # # print(numsnew)
        # count =0
        # for i in range(0,len(numsnew),2):
        #     # print(i,"i")
        #     if i<len(numsnew)-1:
        #         if numsnew[i] != numsnew[i+1]:
        #             return numsnew[i]
        #     else:
        #         return numsnew[i]
        res = 0
        for i in nums:
            res = res ^ i  #xor for checing different input
        return res
        