class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        count=0
        mixlen = len(word1)+len(word2)
        finalstr = ""
        print(mixlen)
        # for i in range(mixlen):
        #     if count%
        point1 = 0
        point2=0
        len1=len(word1)
        len2 =len(word2)
        while point1<len1 or point2<len2:
                if point1<len1:
                    finalstr+=word1[point1]
                    point1+=1
                if point2<len2:
                    finalstr+=word2[point2]
                    point2+=1
        return finalstr
        