class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        high = 0
        highest = 0
        for i in gain:
            high +=i
            highest = max(high,highest)
        return highest

        