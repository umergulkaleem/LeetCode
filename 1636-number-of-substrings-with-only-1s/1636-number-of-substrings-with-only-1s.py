class Solution:
    def numSub(self, s: str) -> int:
        # count= 0 

        # for i in range(len(s)):
        #     if s[i] == '1':
        #         # count+=1
        #         # seen = True
        #         count_1= i
        #         while count_1<len(s) and s[count_1] =='1':
                    
        #             count+=1
        #             count_1+=1
        #             # seem =False
        # return count

        # total = 0
        # con = 0
        # for i in reversed(s):
        #     if i == '1':
        #         con +=1
        #     else:
        #         con=0
        #     total +=con
        # return total

        MOD = 10**9 + 7
        total = 0
        con = 0

        for ch in s:
            if ch == '1':
                con += 1
            else:
                total = (total + con * (con + 1) // 2) % MOD
                con = 0

        # Add last block (if string ends with ones)
        total = (total + con * (con + 1) // 2) % MOD

        return total

        