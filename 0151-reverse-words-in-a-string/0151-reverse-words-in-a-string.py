class Solution:
    def reverseWords(self, s: str) -> str:
        # prev = ''
        # for i in range(len(s)):
        #     prev = s[i]
        #     if i<len(s)-1:
        #         if s[i+1] == " " and s[i] ==" ":
        #             s.replace(prev,"")
        #             print("in remove")
        # print(s)
        s=" ".join(s.split())
        print(s)
        s=s.split()
        print(s)
        s.reverse()
        print(s)
        news = " ".join(s)
        return news