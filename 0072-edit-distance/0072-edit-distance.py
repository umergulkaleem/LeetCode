class Solution:
    def minDistance(self, word1: str, word2: str) -> int:


        memo = {}

        def helper(i,j):
            if (i,j) in memo:
                return memo[(i,j)]

            if len(word1) == i and len(word2) == j:
                return 0

            if len(word1) == i and j<len(word2):
                return len(word2)-j
            if len(word1) >i and j ==len(word2):
                return len(word1) - i

            if word1[i] == word2[j] :
                memo[(i,j)] = helper(i+1,j+1)

                return memo[(i,j)]

            insert = 1+helper(i+1,j)
            delete = 1+helper(i,j+1)
            sub = 1+helper(i+1,j+1)
            memo[(i,j)] = min(insert,delete,sub)
            return memo[(i,j)]
        return helper(0,0)