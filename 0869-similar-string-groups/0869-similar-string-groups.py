class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        count = 0
        def strcheck(str1,str2):
            diff =0
            if len(str1) == len(str2):

                for i in range(len(str2)):
                    if str1[i]!= str2[i]:
                        diff+=1
                if diff == 2:
                    return True
                elif diff == 0:
                    return True
                else:
                    return False
        def dfs(i):
            for j in range(n):
                if checked[j] == False and strcheck(strs[i],strs[j]):
                    checked[j] =True
                    dfs(j)
        n = len(strs)
        checked = [False]*n
        print(checked)
        for i in range(len(strs)):
            if  checked[i] == False:
                checked[i] = True
                res = dfs(i)
                count+=1
        return count
        


        