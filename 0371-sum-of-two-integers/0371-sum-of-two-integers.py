class Solution:
    def getSum(self, a: int, b: int) -> int:
        # res = ""
        # carry = 0
        # while a>0 or b>0:
        #     newBin = ""
        #     newBin +=str(a&1)
        #     newBin +=str(b&1)
        #     if carry ==1:

        #         newBin+=str(1)
        #     a = a>>1
        #     b = b>>1
        #     print(newBin)
 
        #     if newBin.count("1")==1:
        #         res+="1"
        #     elif  newBin.count("1")==2:
        #         carry = 1
        #         res+="0"
        #     elif newBin.count("1")==3:
        #         carry = 1
        #         res+="1"
        #     else:
        #         carry = 0
        #         res+="0"
        # if carry == 1:
        #     res += "1"

        # return int(res[::-1], 2)
        mask = 0xFFFFFFFF
        max_int =  0x7FFFFFFF 
        while b!=0:
            carry = (a&b) &mask
            a=(a^b) &mask
            b=(carry<<1)&mask
        return a if a <=max_int else ~(a^mask)
        