class Solution:
    def totalNumbers(self, digits: List[int]) -> int:

        count= [0]*10

        for digit in digits:
            count[digit]+=1
        res=0
        def helper(pos,num):
            nonlocal res
            if pos == 3:
                res+=1
                return

            for i in range(10):
                if count[i]==0:
                    continue
                
                if pos==0 and i ==0:
                    continue
                
                if pos == 2 and i %2 !=0:
                    continue
                count[i]-=1
                helper(pos+1,num*10+i)
                count[i]+=1
        helper(0,0)
        return res

        