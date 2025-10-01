class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        total = numBottles          # total bottles you can drink
        empty = numBottles          # how many empty bottles you have

        while empty >= numExchange:
            # how many new full bottles you can get
            new_full = empty // numExchange  

            total += new_full       # drink them
            empty = empty - new_full * numExchange + new_full  
            # Explanation:
            #   empty - new_full*numExchange → empties spent in exchange
            #   + new_full → empties gained after drinking the new bottles

        return total 