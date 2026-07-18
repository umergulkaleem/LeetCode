class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a= float('-inf')
        b= float('inf')
        
        for i in nums:
            if a<i:
                a = i
            if b>i:
                b = i
        print(a,b)

        res=  0
        def gcd(a,b):

            while b!=0:
                a,b = b,a%b
            return a

        return gcd(a,b)