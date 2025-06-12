class Solution:
    def isPalindrome(self, x: int) -> bool:
        x= str(x)
        l = 0
        r = len(x)-1
        while l<r:
            if x[l] != x[r]:
                return False
            else :
                l +=1
                r -=1
        return True
        # orgno = x
        # result = 0
        # while x>0:
        #     cal = int(x%10)
        #     print(cal,"cal")
        #     result = result*10+cal
        #     x=int(x/10)

        # print(orgno,"orgnum")
        # if orgno == result:
        #     return True
        # else:
        #     return False