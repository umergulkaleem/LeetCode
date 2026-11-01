class Solution:
    def minMoves(self, nums: list[int]) -> int:
        """
        how much we need for the lowest to make it to the euqal to the other element in the list at each step
        all the element become equal to the min
        """

        move =0
        minimum = min(nums)

        for n in nums:
            move+=n-minimum
        return move
        