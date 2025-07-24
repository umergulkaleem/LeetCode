class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        side1 =0
        side2=0
        side3 = 0
        # for i in range(len(nums)):
        #     side1=nums[i]
        #     print(side1,"side1",side2,"side2",side3,"side3","in I")
        #     for k in range(i,len(nums)):
        #         side2=nums[k]
        #         print(side1,"side1",side2,"side2",side3,"side3","in K")
        #         for j in range(i+k,len(nums)):
        #             side3=nums[k]
        #             print(side1,"side1",side2,"side2",side3,"side3","in J")
        #     if side1==side2 and side1>side3:
        #         print("in if")
        #         return side1+side2+side3
        # return 0
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            print(i,"i")
            side1=nums[i]
            side2=nums[i+1]
            side3=nums[i+2]
            print(side1,"side1",side2,"side2",side3,"side3","in J")
            
                
            if side1<side2+side3:
                # print(side1,"side1",side2,"side2",side3,"side3","in J")
                # print("in if")
                return side1+side2+side3
        return 0

