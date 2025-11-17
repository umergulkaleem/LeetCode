class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = 0
        first_index = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                first_index = i
                break
        print(first_index)
        
        for i in range(first_index+1,len(nums)):
            if nums[i]==0:
                count+=1
                print(count,"c")
            elif count<k:
                return False
            else:
                count =0
        return True
            


        