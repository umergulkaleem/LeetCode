class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        while True:
            # str_n = str(n)
            # res = str_n[0]
            # for _ in len(1,str_n):
            #     res*=
            res = 1
            tmp = n
            while tmp:
                digit = tmp %10
                res*=digit
                tmp = tmp//10
            if res % t == 0:
                return n
            n+=1
            print(n)


                
        