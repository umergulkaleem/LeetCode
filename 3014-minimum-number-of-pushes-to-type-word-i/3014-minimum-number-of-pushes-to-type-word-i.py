class Solution:
    def minimumPushes(self, word: str) -> int:
        total = 0
        count = 1
        tmp = 0
        res = 0
        while total < len(word):
            if tmp>7:
                count+=1
                tmp = 0
            res+=count
            total+=1
            tmp+=1
            # print(res,"re")
        return res

        