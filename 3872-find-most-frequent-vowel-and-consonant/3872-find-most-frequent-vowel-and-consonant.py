class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set("aeiou")
        freq = Counter(s)

        max_vowel = 0
        max_consonant = 0

        for char, count in freq.items():
            if char in vowels:
                max_vowel = max(max_vowel, count)
            else:
                max_consonant = max(max_consonant, count)

        return max_vowel + max_consonant
        