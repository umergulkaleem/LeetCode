class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def helper(p1,p2):
            if p1 == p2:
                return piles[p1]
            
            if (p1,p2) in memo:
                return memo[(p1,p2)]
            left = piles[p1] - helper(p1+1,p2)
            right = piles[p2] - helper(p1,p2-1)
            memo[(p1,p2)] = max(left,right)

            return max(right,left)
        
        return helper(0,len(piles)-1)>0