class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:

        MOD = 10**9 + 7
        res = 0
        stack = [] # idex num
        arr = [float("-inf")] + arr +[ float("-inf")]

        for i,n in enumerate(arr):

            while stack and stack[-1][1]>arr[i]:
                j,m = stack.pop()

                right = j - stack[-1][0] if stack else j+1
                left = i-j

                res = (res + m *left *right)  % MOD

            stack.append([i,n])

        # for i in range(len(stack)):

        #     j,n = stack[i]

        #     right = j - stack[i-1][0] if i>0 else j+1
        #     left = len(arr) - j

        #     res = (res + n * left * right)  % MOD

        return res

        