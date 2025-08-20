# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # def guess(pick):
        #     if n>pick:
        #         return -1
        #     elif n<pick:
        #         return 1
        #     else:
        #         return 0
        # return guess(n)        
        left, right = 1, n
        
        while left <= right:
            mid = left + (right - left) // 2
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res == -1:
                right = mid - 1
            else:  # res == 1
                left = mid + 1
