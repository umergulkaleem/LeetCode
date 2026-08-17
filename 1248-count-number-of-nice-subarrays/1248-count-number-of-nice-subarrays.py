class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

       
        l  = 0
        res = 0
        oddno = 0
        m=0
        for r in range(len(nums)):
            curr = nums[r]
            if curr % 2:
                oddno+=1
            while oddno>k:
                if nums[l]% 2:
                    oddno-=1
                l+=1
                m=l
        
            if oddno == k:
                while not nums[m] % 2:
                    m+=1
                res+=(m-l)+1
            
        return res
        