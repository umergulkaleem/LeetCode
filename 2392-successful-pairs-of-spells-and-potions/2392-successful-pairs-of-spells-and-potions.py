class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # create = []
        # for i in spells:
        #     length = 0
        #     print(i)
        #     for k in potions:
        #         if i*k >=success:
        #             length+=1
        #     create.append(length)
        # return create  

        potions.sort()
        n = len(potions)
        result = []

        for spell in spells:
            min_potion = (success + spell - 1) // spell  # same ceil(success / spell)
            # Manual binary search
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) // 2
                if potions[mid] < min_potion:
                    low = mid + 1
                else:
                    high = mid - 1
            # low now points to the first valid potion
            result.append(n - low)

        return result

        