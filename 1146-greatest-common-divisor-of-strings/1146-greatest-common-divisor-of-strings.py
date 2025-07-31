class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # point1 = 0
        # point2= 0 
        # string = ""
        # count = 0
        # occurance = True
        # while point1<len(str1):
        #     # if count == len(str2):
        #     #     return ""
        #     # if str2[point2] == str1[point1]:
        #     #     if str2[point2] not in string:
        #     #         string+=str2[point2]
        #     #     point1+=1
        #     #     point2+=1
        #     # else:
        #     #     point1+=1
        #     # print(string)
        #     # count+=1
        #     # if point2==3:
        #     #     point2 = 0
        #     #     for i in range()
                
        #     #         return string
        #     if str2[point2] == str1[point1]:
        #         string+=str2[point2]
        #         point1+=1
        #         point2+=1
        #     else:
        #         point1+=1
        #     if point2== len(str2):
        #         point2=0
        #         if str1[point1] != string[count]:
        #             occurance =False
        # if occurance :
        #     return string
        # else:
        #     return ""

        if str1 + str2 != str2 + str1:
            return ""
    
        # Helper function to find GCD of lengths
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]



        