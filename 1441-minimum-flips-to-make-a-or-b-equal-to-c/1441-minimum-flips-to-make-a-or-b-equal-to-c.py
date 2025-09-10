class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a > 0 or b > 0 or c > 0:
            abit = a & 1
            bbit = b & 1
            cbit = c & 1

            if cbit == 1:
                # we need (a | b) = 1
                if (abit | bbit) == 0:
                    flips += 1
            else:  # cbit == 0
                # we need (a | b) = 0
                if (abit | bbit) == 1:
                    if abit == 1 and bbit == 1:
                        flips += 2
                    else:
                        flips += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return flips
        