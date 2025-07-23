class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

      
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(m):
            for j in range(n):
                mul = int(num1[i]) * int(num2[j])
                result[i + j] += mul
                result[i + j + 1] += result[i + j] // 10  # carry
                result[i + j] %= 10

        # Remove leading zeros from the back
        while result[-1] == 0:
            result.pop()

        # Convert to string
        return ''.join(map(str, result[::-1]))

            
            
        