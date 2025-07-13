class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binarya = int(a,2)
        binaryb = int(b,2)
        sum1 = binarya+binaryb
        return bin(sum1)[2:]



        # inta = 0
        # intb = 0
        # for i in range(len(a)):
        #     inta+=2**i
        # for i in range(len(b)):
        #     intb+=2**i
        # sum1= inta+intb
        # binary = []
        # string =""
        # for i in range(sum1-2,-1,-1):
        #     print(i)
        #     val = sum1//2**i
        #     if val == 1:
        #         binary.append(1)
        #         string+="1"
        #         print(binary)
        #     else:
        #         binary.append(0)
        #         string+="0"
        # return string



            