class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxamount = 0
        for i in accounts:
            amount = 0
            for j in i:
                amount+=j
            maxamount = max(maxamount,amount)
        return maxamount
            
            
        