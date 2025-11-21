class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        n = len(s)
    
    # For each character from 'a' to 'z'
        for c in range(26):
            char = chr(ord('a') + c)
            
            # Find first and last occurrence of char in s
            first = s.find(char)
            last = s.rfind(char)
            
            # If char appears at least twice and there is space for middle character
            if first != -1 and last != -1 and last - first > 1:
                # Collect unique characters between first and last occurrence of char
                unique_middle_chars = set(s[first+1:last])
                result += len(unique_middle_chars)
        
        return result
        