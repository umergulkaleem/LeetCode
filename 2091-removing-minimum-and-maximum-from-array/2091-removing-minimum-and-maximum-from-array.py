class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        a = max(nums)
        b = min(nums)

        
        index_a = nums.index(a)
        index_b = nums.index(b)

        i = min(index_a,index_b)
        j = max(index_a,index_b)
        
        front = j+1
        back = len(nums)-i
        mixed = (i+1)+(len(nums)-j)

    

        return min(front,back,mixed)