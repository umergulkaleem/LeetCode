class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:

        final  = []
        count = 0
        temp   = ''
        for i in range(len(s)):
            temp+=s[i]
            count+=1
            if i == len(s)-1 and count != k:
                # print("in ini in")
                while count<k:
                    temp+=fill
                    count+=1
            if count == k:
                final.append(temp)
                temp = ""
                count = 0
            # print(i,"at length",len(s))
            # print(count,"count")
            # print(temp,"at",s[i])
        return final

        



        