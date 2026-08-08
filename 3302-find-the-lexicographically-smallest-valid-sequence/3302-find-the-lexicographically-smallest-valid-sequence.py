class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:

        n1 = len(word1)
        n2 = len(word2)
        arr = [None] * n2
        j = n2-1
        for i in range(n1-1,-1,-1):
            if word1[i] == word2[j]:
                arr[j] = i
                j-=1
            if j <0:
                break
        print(arr)
        ans = []
        j = 0
        dif = False
        for i in range(n1):
            if j ==  n2:
                break
            if word2[j] == word1[i]:
                ans.append(i)
                j+=1
                continue
            elif not dif:
                if j+1==n2 or (arr[j+1] !=None  and  i <arr[j+1]):
                    ans.append(i)
                    j+=1
                    dif = True



        if len(ans)!= n2:
            return []
        return ans




            
                

        