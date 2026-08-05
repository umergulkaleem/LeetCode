class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1,p2 = 0,len(nums)-1
        count = 0
        while count<k:
            last = nums.pop()
            nums.insert(0,last)
            count+=1
            # print(nums)
            # print(p2,"p2")
            p2-=1
