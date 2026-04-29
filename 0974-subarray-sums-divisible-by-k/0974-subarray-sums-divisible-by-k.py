class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        pre_sum = 0
        res= 0 
        pre_cnt = defaultdict(int)
        pre_cnt[0] =1
        for n in nums:
            pre_sum+=n
            remain = pre_sum % k
            res+=pre_cnt[remain]
            pre_cnt[remain] +=1
        return res
        