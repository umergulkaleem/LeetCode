class Solution:
    def possibleStringCount(self, word: str) -> int:
        count=1
        for k in range(len(word)):
            firstletter = word[k]
            print(firstletter)
            if k+1<len(word):
                secondletter= word[k+1]
                if firstletter == secondletter:
                    count+=1
                    print(count)

            # for j in range(1,len(word)):
            #     secondletter = word[j]
            #     if firstletter == secondletter:
            #         count+=1
            #         print(count)
            #         break

        return count