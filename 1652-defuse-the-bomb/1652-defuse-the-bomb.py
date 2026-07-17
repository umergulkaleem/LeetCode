class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        res = [0] * N

        l = 0
        curr_sum = 0
        for r in range(N+abs(k)):
            curr_sum += code[r%N]

            if (r-l+1)>abs(k):
                curr_sum-=code[l%N]
                l = (l+1)%N
            if (r-l+1) == abs(k):
                if k>0:
                    res[(l-1)%N] = curr_sum
                else:
                    res[(r+1)%N] = curr_sum
        return res


        