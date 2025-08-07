class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
   
    
        write = 0  # Pointer where we write
        read = 0   # Pointer to read through chars

        while read < len(chars):
            char = chars[read]
            count = 0

            # Count occurrences of the current character
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # Write the character
            chars[write] = char
            write += 1

            # Write the count (if more than 1)
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write

        