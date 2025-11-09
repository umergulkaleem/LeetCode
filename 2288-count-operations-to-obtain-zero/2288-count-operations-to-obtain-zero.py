class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        op = 0
        while num1 !=0 and num2!=0:

            if num1<num2:
                num2-=num1
                print(num2,"num2")
                op+=1
            else:
                num1-=num2
                print(num1,"num1")

                op+=1
            print(op,"op")
            
        return op
                    