class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        for i in range(len(s)):
            if s[i]=="I":
                # if else to check for IX or IV
                # i+1<len(s) to check if the last index i reached or not esle it will give error
                if i+1<len(s) and (s[i+1]=="V" or s[i+1]=="X"):
                    number -=1
                else:
                    number +=1
            elif s[i] == "V":
                number +=5
            elif s[i] == "X":
                if i+1<len(s) and (s[i+1]=="L" or s[i+1]=="C"):
                    number -=10
                else:
                    number +=10
            elif s[i] == "L":
                number +=50
            elif s[i] == "C":
                if i+1<len(s)and (s[i+1]=="D" or s[i+1]=="M"):
                    number -=100
                else:
                    number +=100
            elif s[i] == "D":
                number +=500
            elif s[i] == "M":
                number +=1000
            else:
                print("wrong input")
            print(number)
        return number