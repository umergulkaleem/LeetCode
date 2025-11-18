class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2   # skip next bit
            else:
                i += 1   # single-bit char
        return i == len(bits) - 1

        