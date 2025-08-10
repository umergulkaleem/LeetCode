class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def digit_count(x):
            return ''.join(sorted(str(x)))

    # Precompute all digit patterns for powers of two up to 10^9
        power_patterns = {digit_count(1 << i) for i in range(31)}

        return digit_count(n) in power_patterns

        