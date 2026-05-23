class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # s = list(s)

        # new = [ ord(s[i]) - 97 for i in range(len(s)) ]
        
        # for i in shifts:
        #     print(i,"at this")
        #     start = i[0]
        #     end  = i[1]
        #     direction = i[2]
        #     for i in range(start, end + 1):
        #         if direction == 1:
        #             new[i] = (new[i] + 1) % 26
        #         else:
        #             new[i] = (new[i] - 1) % 26
        # for i in range(len(new)):
        #     new[i] = chr(new[i]+97)
        # return "".join(new)

        prefix_dif = [0]*(len(s)+1)

        for left,right,d in shifts:
            prefix_dif[left]  += -1 if d  else 1
            prefix_dif[right+1]+= 1 if d  else -1

        diff = 0
        res = [ord(c) - ord("a") for c in s]

        for i in reversed(range(len(prefix_dif))):
            diff+=prefix_dif[i]

            res[i-1] = (diff +res[i-1])%26

        s = [chr(ord("a") +n) for n in res]
        return "".join(s)

            
