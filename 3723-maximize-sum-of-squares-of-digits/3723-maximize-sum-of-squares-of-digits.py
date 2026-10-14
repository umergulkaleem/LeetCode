class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:

        # arr = [0,1,2,3,4,5,6,7,8,9]
        
        # count=9
        # maximum = 0
        # ans = 0

        # while count!=0:
        #     tmp= 0
        #     n = 0
        #     n = (n*10)+arr[count]
        #     tmp +=arr[count]**2
        #     for i in range(num-1):
        #         if sum-n in arr:
        #             tmp +=arr[sum-n]**2
        #             n = (n*10)+arr[sum-n]
        #         else:
        #             tmp = 0

        #     print(tmp,"tmp")
        #     if tmp>maximum:
        #         maximum = tmp
        #         ans = n   

        #     # if count>num:
        #     #     for i in range(2):
        #     #         print(count-i)
        #     #         n=(n*10)+arr[count-i]
            
        #     # if  == sum:
        #     #     return n

        
        #     print(n)
        #     count-=1


        # return str(ans)
        
        if sum>9*num:
            return ""

        ans = []

        for i in range(num):
            digit = min(9,sum)
            ans.append(str(digit))

            sum-=digit
        return "".join(ans)