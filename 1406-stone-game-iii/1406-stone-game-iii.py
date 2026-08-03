class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        memo = {}

        def helper(p1):
            if p1 >= len(stoneValue):
                return 0

            if p1 in memo:
                return memo[p1]
            
            best = float("-inf")
            total = 0
            for k in range(3):
                if p1+k<len(stoneValue):
                    total+=stoneValue[p1+k]
                    best = max(best,total-helper(p1+k+1))
            memo[p1] = best
            return best      

        ans = helper(0)
        if ans>0:
            return "Alice"
        elif ans<0:
            return "Bob"
        else:
            return "Tie" 