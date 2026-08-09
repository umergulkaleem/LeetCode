class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        memo  ={}
        def helper(index,M):
            if index >= len(piles):
                return 0
            
            if (index,M) in memo:
                return memo[(index,M)]
            total = 0
            best =  float(-inf)

            for N in  range(1,2*M+1):
                if index +N> len(piles):
                    break
                total += piles[index+N-1]
                best = max(best,total-helper(index+N,max(M,N)))
            memo[(index,M)]  =best
            return best
        total = sum(piles)
        delta = helper(0,1)
        return (total+delta)//2

        