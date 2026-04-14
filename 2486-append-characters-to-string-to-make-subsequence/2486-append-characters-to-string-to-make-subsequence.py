class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # if len(t) == 1:
        #     return 0 if  t in s else 1
        p1,p2 = 0,0
        total = len(t)

        while p1<len(s) and p2 < len(t) :
            # print(p1,"p1")
            # print(p2,"p2")
            # print(s[p1])
            if s[p1] == t[p2]:
                # print("in")
                total-=1
                p1+=1
                p2+=1
            else:
                p1+=1
        return total
        